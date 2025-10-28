Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Compile error: "Could not resolve dependencies for

project"

In order to compile the Managed Service for Apache Flink sample applications, you must first download
and compile the Apache Flink Kinesis connector and add it to your local Maven
repository. If the connector hasn't been added to your repository, a compile error
similar to the following appears:

```
Could not resolve dependencies for project `your project name`: Failure to find org.apache.flink:flink-connector-kinesis_2.11:jar:1.8.2 in https://repo.maven.apache.org/maven2 was cached in the local repository, resolution will not be reattempted until the update interval of central has elapsed or updates are forced
```

To resolve this error, you must download the Apache Flink source code (version
1.8.2 from [https://flink.apache.org/downloads.html](https://flink.apache.org/downloads.html "https://flink.apache.org/downloads.html")) for the connector. For
instructions about how to download, compile, and install the Apache Flink source
code, see [Using the Apache Flink Kinesis Streams connector
with previous Apache Flink versions](earlier.md#how-creating-apps-building-kinesis "earlier.md#how-creating-apps-building-kinesis").
