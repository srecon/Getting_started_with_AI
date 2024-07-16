# Getting started with AI
All code samples, scripts and more in-depth examples for the book [Getting started with AI](https://github.com/srecon/the-apache-ignite-book)


## Naming conventions

Each chapter in the book has a corresponding folder within the repository. Each folder contains a set of files or folders related to each section of the chapter.

## What is this book about?

## Prerequirities

We recommend a workstation with the following configurations

## build and install


## Conventions

The following typographical conventions are used in this book:

_Italic_ and __Bold__ indicates new terms, important words, URL's, filenames, and file extensions.

A block code is set as follows:

{title="Listing 1.1", lang=JAVA}
```
public class MySuperExtractor implements StreamSingleTupleExtractor<SinkRecord, String, String> {

  @Override public Map.Entry<String, String> extract(SinkRecord msg) {
      String[] parts = ((String)msg.value()).split("_");
      return new AbstractMap.SimpleEntry<String, String>(parts[1], parts[2]+":"+parts[3]);
  }
}
```
Any command-line __input__ or __output__ is written as follows:

```
[2024-06-30 15:39:04,479] INFO Kafka version : 2.0.0 (org.apache.kafka.common.utils.AppInfoParser)
[2024-06-30 15:39:04,479] INFO Kafka commitId : 3402a8361b734732 (org.apache.kafka.common.utils.AppInfoParser)
[2024-06-30 15:39:04,480] INFO [KafkaServer id=0] started (kafka.server.KafkaServer)
```
