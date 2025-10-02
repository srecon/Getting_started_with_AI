# All CLI commands from the chapter 1

## Installing and setting up the local LLM inference

__Download and Install Ollama.__:

 - Visit the [Ollama website](https://ollama.com) to download the latest version of the Ollama installer for your operating system. Look for a direct download link or an installation guide.

- For __macOS__: Open the downloaded file and follow the on-screen instructions to install Ollama on your system. This typically involves dragging the application to the Applications folder on macOS.

- For __Linux__:
	- execute the command ```curl -fsSL https://ollama.com/install.sh | sh```

- For __Windows__: At the time of writing this book, Ollama is available as a preview version specifically for the Windows operating system.

- For __Docker__: Make sure that, your Docker instance is up and running. Execute the following command to run Ollama inside a Docker container.

```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
__Start the Ollama instance.__:

There are two easy steps to start an Ollama instance:

- To start an Ollama instance *without* LLM, use the following command:

```bash
ollama serve
```

- To start an Ollama instance *with* a LLM. Use the following command to start Ollama instance with model [Llama3.1](https://ollama.com/library/llama3.1):

```bash
ollama run llama3.1

```
