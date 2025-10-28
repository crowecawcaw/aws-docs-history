# Set up the Gremlin console to connect to a

Neptune DB instance

The Gremlin Console allows you to experiment with TinkerPop graphs and queries in a REPL
(read-eval-print loop) environment.

## Installing the Gremlin

console and connecting to it in the usual way

You can use the Gremlin Console to connect to a remote graph database. The following
section walks you through installing and configuring the Gremlin Console to connect remotely to a
Neptune DB instance. You must follow these instructions from an Amazon EC2 instance in the same virtual
private cloud (VPC) as your Neptune DB instance.

For help connecting to Neptune with SSL/TLS (which is required), see [SSL/TLS configuration](access-graph-gremlin-java.md#access-graph-gremlin-java-ssl "access-graph-gremlin-java.md#access-graph-gremlin-java-ssl").

###### Note

If you have [IAM authentication enabled](iam-auth-enable.md "iam-auth-enable.md") on
your Neptune DB cluster, follow the instructions in [Connecting to Amazon Neptune databases using IAM authentication with Gremlin console](iam-auth-connecting-gremlin-console.md "iam-auth-connecting-gremlin-console.md") to install the Gremlin console rather
than the instructions here.

###### To install the Gremlin Console and connect to Neptune

1. The Gremlin Console binaries require Java 8 or Java 11. These instructions assume
   usage of Java 11. You can install Java 11 on your EC2 instance as follow:
   - If you're using [Amazon
     Linux 2 (AL2)](https://aws.amazon.com/amazon-linux-2 "https://aws.amazon.com/amazon-linux-2"):

   ```
   sudo amazon-linux-extras install java-openjdk11
   ```

   - If you're using [Amazon
     Linux 2023 (AL2023)](../../../linux/al2023/ug/what-is-amazon-linux.md "../../../linux/al2023/ug/what-is-amazon-linux.md"):

   ```
   sudo yum install java-11-amazon-corretto-devel
   ```

   - For other distributions, use whichever of the following is appropriate:

   ```
   sudo yum install java-11-openjdk-devel
   ```

   or:

   ```
   sudo apt-get install openjdk-11-jdk
   ```

2. Enter the following to set Java 11 as the default runtime on your EC2 instance.

```
sudo /usr/sbin/alternatives --config java
```

When prompted, enter the number for Java 11. 3. Download the appropriate version of the Gremlin console from the Apache
web site. You can check the
[java gremlin client
page](access-graph-gremlin-client.md#best-practices-gremlin-java-latest "access-graph-gremlin-client.md#best-practices-gremlin-java-latest") for the Neptune engine version you are currently running to
determine which Gremlin version it supports. For example, for version
3.7.2, you can download the [Gremlin console](https://archive.apache.org/dist/tinkerpop/3.7.2/apache-tinkerpop-gremlin-console-3.7.2-bin.zip "https://archive.apache.org/dist/tinkerpop/3.7.2/apache-tinkerpop-gremlin-console-3.7.2-bin.zip") from the [Apache Tinkerpop3](https://tinkerpop.apache.org/download.html "https://tinkerpop.apache.org/download.html") website onto your EC2 instance like this:

```
wget https://archive.apache.org/dist/tinkerpop/3.7.2/apache-tinkerpop-gremlin-console-3.7.2-bin.zip
```

4. Unzip the Gremlin Console zip file.

```
unzip apache-tinkerpop-gremlin-console-3.7.2-bin.zip
```

5. Change directories into the unzipped directory.

```
cd apache-tinkerpop-gremlin-console-3.7.2
```

6. In the `conf` subdirectory of the extracted directory, create a
   file named `neptune-remote.yaml` with the following text. Replace
   `your-neptune-endpoint` with the hostname or IP address of your
   Neptune DB instance. The square brackets (`[ ]`) are required.

###### Note

For information about finding the hostname of your Neptune DB instance, see the [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md") section.

```
hosts: [`your-neptune-endpoint`]
port: 8182
connectionPool: { enableSsl: true }
serializer: { className: org.apache.tinkerpop.gremlin.util.ser.GraphBinaryMessageSerializerV1,
              config: { serializeResultToString: true }}
```

###### Note

Serializers were moved from the `gremlin-driver` module to the new `gremlin-util` module in
version 3.7.0. The package changed from org.apache.tinkerpop.gremlin.driver.ser to
org.apache.tinkerpop.gremlin.util.ser. 7. In a terminal, navigate to the Gremlin Console directory
(`apache-tinkerpop-gremlin-console-3.7.2`), and then enter
the following command to run the Gremlin Console.

```
bin/gremlin.sh
```

You should see the following output:

```
         \,,,/
         (o o)
-----oOOo-(3)-oOOo-----
plugin activated: tinkerpop.server
plugin activated: tinkerpop.utilities
plugin activated: tinkerpop.tinkergraph
gremlin>
```

You are now at the `gremlin>` prompt. You will enter the remaining steps
at this prompt. 8. At the `gremlin>` prompt, enter the following to connect to the
Neptune DB instance.

```
:remote connect tinkerpop.server conf/neptune-remote.yaml
```

9. At the `gremlin>` prompt, enter the following to switch to remote mode.
   This sends all Gremlin queries to the remote connection.

```
:remote console
```

10. Enter the following to send a query to the Gremlin Graph.

```
g.V().limit(1)
```

11. When you are finished, enter the following to exit the Gremlin Console.

```
:exit
```

###### Note

Use a semicolon (`;`) or a newline character (`\n`) to separate
each statement.

Each traversal preceding the final traversal must end in `next()` to be
executed. Only the data from the final traversal is returned.

For more information on the Neptune implementation of Gremlin, see [Gremlin standards compliance in Amazon Neptune](access-graph-gremlin-differences.md "access-graph-gremlin-differences.md").
