Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Configuring a JDBC

connection with Apache Maven

Apache Maven is a software project management and comprehension tool. The AWS SDK for Java
supports Apache Maven projects. For more information, see [Using
the SDK with Apache Maven](../../../sdk-for-java/v1/developer-guide/setup-project-maven.md "../../../sdk-for-java/v1/developer-guide/setup-project-maven.md") in the _AWS SDK for Java Developer Guide._

If you use Apache Maven, you can configure and build your projects to use an Amazon Redshift JDBC
driver to connect to your Amazon Redshift cluster. To do this, add the JDBC driver as a dependency
in your project's `pom.xml` file. If you use Maven to build your project
and want to use a JDBC connection, take the steps in the following section.

###### To configure the JDBC driver as a Maven dependency

1. Add either the Amazon repository or the Maven Central repository to the
   repositories section of your `pom.xml` file.

###### Note

The URL in the following code example returns an error if used in a
browser. Use this URL only in the context of a Maven project.

To connect using Secure Sockets Layer (SSL), add the following repository
to your `pom.xml` file.

```
<repositories>
    <repository>
      <id>redshift</id>
      <url>https://s3.amazonaws.com/redshift-maven-repository/release</url>
    </repository>
</repositories>
```

For a Maven Central repository, add the following to your
`pom.xml` file.

```
<repositories>
    <repository>
      <id>redshift</id>
      <url>https://repo1.maven.org/maven2</url>
    </repository>
</repositories>
```

2. Declare the version of the driver that you want to use in the dependencies
   section of your `pom.xml` file.

Amazon Redshift offers drivers for tools that are compatible with the JDBC 4.2
API. For information about the
functionality supported by these drivers, see [Download the Amazon Redshift JDBC driver, version
2.1](jdbc20-download-driver.md "jdbc20-download-driver.md").

Replace `driver-version` in the
following example with your driver version, for example
`2.1.0.1`. For a JDBC 4.2–compatible driver, use the
following.

```
<dependency>
   <groupId>com.amazon.redshift</groupId>
   <artifactId>redshift-jdbc42</artifactId>
   <version>`driver-version`</version>
</dependency>
```

The class name for this driver is
`com.amazon.redshift.Driver`.

The Amazon Redshift Maven drivers need the following optional dependencies when you use IAM
database authentication.

```
<dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-java-sdk-core</artifactId>
      <version>1.12.23</version>
      <scope>runtime</scope>
      <optional>true</optional>
</dependency>
    <dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-java-sdk-redshift</artifactId>
      <version>1.12.23</version>
      <scope>runtime</scope>
      <optional>true</optional>
</dependency>
<dependency>
      <groupId>com.amazonaws</groupId>
      <artifactId>aws-java-sdk-sts</artifactId>
      <version>1.12.23</version>
      <scope>runtime</scope>
      <optional>true</optional>
</dependency>
```

To upgrade or change the Amazon Redshift JDBC driver to the latest version, first modify the
version section of the dependency to the latest version of the driver. Then clean
your project with the Maven Clean Plugin, as shown following.

```
mvn clean
```
