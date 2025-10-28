# Using a Java client to connect to a Neptune DB

instance

The following section walks you through the running of a complete Java sample that
connects to a Neptune DB instance and performs a Gremlin traversal using the Apache TinkerPop
Gremlin client.

These instructions must be followed from an Amazon EC2 instance in the same virtual private
cloud (VPC) as your Neptune DB instance.

###### To connect to Neptune using Java

1. Install Apache Maven on your EC2 instance. If using Amazon Linux 2023 (preferred), use:

```
sudo dnf update -y
sudo dnf install maven -y
```

If using Amazon Linux 2, download the latest binary from [https://maven.apache.org/download.cgi:](https://maven.apache.org/download.cgi: "https://maven.apache.org/download.cgi:")

```
sudo yum remove maven -y
wget https://dlcdn.apache.org/maven/maven-3/ <version>/binaries/apache-maven-<version>-bin.tar.gz
sudo tar -xzf apache-maven-<version>-bin.tar.gz -C /opt/
sudo ln -sf /opt/apache-maven-<version> /opt/maven
echo 'export MAVEN_HOME=/opt/maven' >> ~/.bashrc
echo 'export PATH=$MAVEN_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

2. **Install Java.**
   The Gremlin libraries need Java 8 or 11. You can install Java 11 as follows:
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

3. **Set Java 11 as the default runtime on your EC2 instance:**
   Enter the following to set Java 8 as the default runtime on your EC2 instance:

```
sudo /usr/sbin/alternatives --config java
```

When prompted, enter the number for Java 11. 4. **Create a new directory named
`gremlinjava`:**

```
mkdir gremlinjava
cd gremlinjava
```

5. In the `gremlinjava` directory, create a
   `pom.xml` file, and then open it in a text editor:

```
nano pom.xml
```

6. Copy the following into the `pom.xml` file and save it:

```
<project xmlns="https://maven.apache.org/POM/4.0.0"
         xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="https://maven.apache.org/POM/4.0.0 https://maven.apache.org/maven-v4_0_0.xsd">
  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
  <modelVersion>4.0.0</modelVersion>
  <groupId>com.amazonaws</groupId>
  <artifactId>GremlinExample</artifactId>
  <packaging>jar</packaging>
  <version>1.0-SNAPSHOT</version>
  <name>GremlinExample</name>
  <url>https://maven.apache.org</url>
  <dependencies>
    <dependency>
      <groupId>org.apache.tinkerpop</groupId>
      <artifactId>gremlin-driver</artifactId>
      <version>`3.7.2`</version>
    </dependency>
    <!-- https://mvnrepository.com/artifact/org.apache.tinkerpop/gremlin-groovy
      (Not needed for TinkerPop version 3.5.2 and up)
    <dependency>
      <groupId>org.apache.tinkerpop</groupId>
      <artifactId>gremlin-groovy</artifactId>
      <version>3.7.2</version>
    </dependency> -->
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-jdk14</artifactId>
      <version>1.7.25</version>
    </dependency>
  </dependencies>
  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>2.5.1</version>
        <configuration>
          <source>11</source>
          <target>11</target>
        </configuration>
      </plugin>
        <plugin>
          <groupId>org.codehaus.mojo</groupId>
          <artifactId>exec-maven-plugin</artifactId>
          <version>1.3</version>
          <configuration>
            <executable>java</executable>
            <arguments>
              <argument>-classpath</argument>
              <classpath/>
              <argument>com.amazonaws.App</argument>
            </arguments>
            <mainClass>com.amazonaws.App</mainClass>
            <complianceLevel>1.11</complianceLevel>
            <killAfter>-1</killAfter>
          </configuration>
        </plugin>
    </plugins>
  </build>
</project>
```

###### Note

If you are modifying an existing Maven project, the required dependency is
highlighted in the preceding code. 7. Create subdirectories for the example source code
(`src/main/java/com/amazonaws/`) by typing the following at the command
line:

```
mkdir -p `src/main/java/com/amazonaws/`
```

8. In the `src/main/java/com/amazonaws/` directory, create a file
   named `App.java`, and then open it in a text editor.

```
nano `src/main/java/com/amazonaws/App.java`
```

9. Copy the following into the `App.java` file. Replace
   `your-neptune-endpoint` with the address of your Neptune DB instance. Do
   _not_ include the `https://` prefix in the
   `addContactPoint` method.

###### Note

For information about finding the hostname of your Neptune DB instance, see [Connecting to Amazon Neptune Endpoints](feature-overview-endpoints.md "feature-overview-endpoints.md").

```
package com.amazonaws;
import org.apache.tinkerpop.gremlin.driver.Cluster;
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversalSource;
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal;
import static org.apache.tinkerpop.gremlin.process.traversal.AnonymousTraversalSource.traversal;
import org.apache.tinkerpop.gremlin.driver.remote.DriverRemoteConnection;
import org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.__;
import org.apache.tinkerpop.gremlin.structure.T;

public class App
{
  public static void main( String[] args )
  {
    Cluster.Builder builder = Cluster.build();
    builder.addContactPoint("`your-neptune-endpoint`");
    builder.port(8182);
    builder.enableSsl(true);

    Cluster cluster = builder.create();

    GraphTraversalSource g = traversal().withRemote(DriverRemoteConnection.using(cluster));

    // Add a vertex.
    // Note that a Gremlin terminal step, e.g. iterate(), is required to make a request to the remote server.
    // The full list of Gremlin terminal steps is at https://tinkerpop.apache.org/docs/current/reference/#terminal-steps
    g.addV("Person").property("Name", "Justin").iterate();

    // Add a vertex with a user-supplied ID.
    g.addV("Custom Label").property(T.id, "CustomId1").property("name", "Custom id vertex 1").iterate();
    g.addV("Custom Label").property(T.id, "CustomId2").property("name", "Custom id vertex 2").iterate();

    g.addE("Edge Label").from(__.V("CustomId1")).to(__.V("CustomId2")).iterate();

    // This gets the vertices, only.
    GraphTraversal t = g.V().limit(3).elementMap();

    t.forEachRemaining(
      e ->  System.out.println(t.toList())
    );

    cluster.close();
  }
}
```

For help connecting to Neptune with SSL/TLS (which is required), see [SSL/TLS configuration](#access-graph-gremlin-java-ssl "#access-graph-gremlin-java-ssl"). 10. Compile and run the sample using the following Maven command:

```
mvn compile exec:exec
```

The preceding example returns a map of the key and values of each property for the first
two vertexes in the graph by using the `g.V().limit(3).elementMap()`
traversal. To query for something else, replace it with another Gremlin traversal with one of
the appropriate ending methods.

###### Note

The final part of the Gremlin query, `.toList()`, is required to submit the
traversal to the server for evaluation. If you don't include that method or another
equivalent method, the query is not submitted to the Neptune DB instance.

You also must append an appropriate ending when you add a vertex or edge, such as
when you use the `addV( )` step.

The following methods submit the query to the Neptune DB instance:

- `toList()`
- `toSet()`
- `next()`
- `nextTraverser()`
- `iterate()`

## SSL/TLS configuration for Gremlin Java client

Neptune requires SSL/TLS to be enabled by default. Typically, if the Java driver
is configured with `enableSsl(true)`, it can connect to Neptune
without having to set up a `trustStore()` or `keyStore()` with a
local copy of a certificate. Earlier versions of TinkerPop encouraged use of
`keyCertChainFile()` to configure a locally stored `.pem` file,
but that has been deprecated and no longer available after 3.5.x. If you were using
that setup with a public certificate, using `SFSRootCAG2.pem`, you can now
remove the local copy.

However, if the instance with which you are connecting doesn't have an internet
connection through which to verify a public certificate, or if the certificate you're
using isn't public, you can take the following steps to configure a local certificate
copy:

###### Setting up a local certificate copy to enable SSL/TLS

1. Download and install [keytool](https://docs.oracle.com/javase/9/tools/keytool.htm#JSWOR-GUID-5990A2E4-78E3-47B7-AE75-6D1826259549 "https://docs.oracle.com/javase/9/tools/keytool.htm#JSWOR-GUID-5990A2E4-78E3-47B7-AE75-6D1826259549")
   from Oracle. This will make setting up the local key store much easier.
2. Download the `SFSRootCAG2.pem`CA certificate (the Gremlin Java
   SDK requires a certificateto verify the remote certificate):

```
wget https://www.amazontrust.com/repository/SFSRootCAG2.pem
```

3. Create a key store in either JKS or PKCS12 format. This example uses JKS. Answer
   the questions that follow at the prompt. The password that you create here will be
   needed later:

```
keytool -genkey -alias `(host name)` -keyalg RSA -keystore server.jks
```

4. Import the `SFSRootCAG2.pem` file that you downloaded into the
   newly created key store:

```
keytool -import -keystore server.jks -file .pem
```

5. Configure the `Cluster` object programmatically:

```

Cluster cluster = Cluster.build("`(your neptune endpoint)`")
                         .port(`8182`)
                         .enableSSL(true)
                         .keyStore(‘server.jks’)
                         .keyStorePassword("`(the password from step 2)`")
                         .create();
```

You can do the same thing in a configuration file if you want, as you might do with
the Gremlin console:

```
hosts: [`(your neptune endpoint)`]
port: `8182`
connectionPool: { enableSsl: true, keyStore: server.jks, keyStorePassword: `(the password from step 2)` }
serializer: { className: org.apache.tinkerpop.gremlin.util.ser.GraphBinaryMessageSerializerV1, config: { serializeResultToString: true }}
```
