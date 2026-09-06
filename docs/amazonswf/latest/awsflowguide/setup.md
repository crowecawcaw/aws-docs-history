

# Setting up the AWS Flow Framework for Java
<a name="setup"></a>

The AWS Flow Framework for Java is included with the [AWS SDK for Java](https://aws.amazon.com/sdkforjava/). If you have not already set up the AWS SDK for Java, visit [Getting Started](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/getting-started.html) in the AWS SDK for Java Developer Guide for information about installing and configuring the SDK itself.

## Add the flow framework with Maven
<a name="installing-maven"></a>

The Amazon SWF build tools are open source—to view or download the code or to build the tools yourself, visit the repository at [https://github.com/aws/aws-swf-build-tools](https://github.com/aws/aws-swf-build-tools).

Amazon provides [Amazon SWF build tools](https://mvnrepository.com/artifact/com.amazonaws/aws-swf-build-tools) in the Maven Central Repository.

To set up the flow framework for Maven, add the following dependency to your project's `pom.xml` file:

```
<dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-swf-build-tools</artifactId>
    <version>2.0.0</version>
</dependency>
```