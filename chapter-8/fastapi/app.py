from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import redis
from fastapi_mcp import FastApiMCP

# Initialize FastAPI app
app = FastAPI(title="Warehouse Order System")

# Connect to Redis (localhost, port 6379, database 1)
#redis_client = redis.StrictRedis(host="127.0.0.1", port=6379, db=1, decode_responses=True)

redis_host = os.getenv("REDIS_HOST", "127.0.0.1")
redis_port = int(os.getenv("REDIS_PORT", 6379))

redis_client = redis.StrictRedis(host=redis_host, port=redis_port, db=1, decode_responses=True)

# Pydantic model for a complete order
class Order(BaseModel):
    order_id: int
    customer_name: str
    items: List[str]
    status: str  # Example statuses: 'pending', 'shipped', 'cancelled'

# Model used for creating new orders
class OrderCreate(BaseModel):
    customer_name: str
    items: List[str]

# Model used for updating existing orders
class OrderUpdate(BaseModel):
    customer_name: str | None = None
    items: List[str] | None = None
    status: str | None = None

# Endpoint to create a new order
@app.post("/orders")
def create_order(order: OrderCreate) -> dict:
    # Generate a new unique order ID
    order_id = redis_client.incr("order_id")

    # Prepare order data to store in Redis
    order_data = {
        "order_id": order_id,
        "customer_name": order.customer_name,
        "items": ",".join(order.items),  # Convert list to comma-separated string
        "status": "pending"  # Default status when order is created
    }

    # Store order hash in Redis
    redis_client.hset(f"order:{order_id}", mapping=order_data)

    # Track all order IDs in a Redis set
    redis_client.sadd("orders", order_id)

    return {"order_id": order_id, "message": "Order created successfully."}

# Endpoint to get a specific order by ID
@app.get("/orders/{order_id}")
def get_order(order_id: int) -> dict:
    # Check if order exists
    if not redis_client.exists(f"order:{order_id}"):
        raise HTTPException(status_code=404, detail="Order not found.")

    # Retrieve order data from Redis
    data = redis_client.hgetall(f"order:{order_id}")
    data["items"] = data["items"].split(",")  # Convert string back to list

    return {"order": data}

# Endpoint to list all orders
@app.get("/orders")
def list_orders() -> dict:
    # Get all order IDs from the Redis set
    order_ids = redis_client.smembers("orders")
    orders = []

    for oid in order_ids:
        data = redis_client.hgetall(f"order:{oid}")
        if data:
            data["items"] = data["items"].split(",")  # Convert string to list
            orders.append(data)

    return {"orders": orders}

# Endpoint to update an existing order
@app.put("/orders/{order_id}")
def update_order(order_id: int, update: OrderUpdate) -> dict:
    # Check if the order exists
    if not redis_client.exists(f"order:{order_id}"):
        raise HTTPException(status_code=404, detail="Order not found.")

    # Update customer name if provided
    if update.customer_name:
        redis_client.hset(f"order:{order_id}", "customer_name", update.customer_name)

    # Update items list if provided
    if update.items:
        redis_client.hset(f"order:{order_id}", "items", ",".join(update.items))

    # Update status if provided
    if update.status:
        redis_client.hset(f"order:{order_id}", "status", update.status)

    return {"message": "Order updated successfully."}

# Endpoint to delete an order by ID
@app.delete("/orders/{order_id}")
def delete_order(order_id: int) -> dict:
    # Check if the order exists
    if not redis_client.exists(f"order:{order_id}"):
        raise HTTPException(status_code=404, detail="Order not found.")

    # Remove order data and ID reference
    redis_client.delete(f"order:{order_id}")
    redis_client.srem("orders", order_id)

    return {"message": "Order deleted successfully."}

# Add the MCP server to your FastAPI app
mcp = FastApiMCP(
    app,  
    name="My API MCP",  # Name for your MCP server
    description="MCP server for my API",  # Description
)

# Mount the MCP server to your FastAPI app
mcp.mount(app)