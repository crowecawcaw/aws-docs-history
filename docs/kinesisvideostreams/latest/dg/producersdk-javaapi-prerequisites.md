# Prerequisites

Before you set up the Java producer SDK, ensure that you have the following prerequisites:

- In the sample code, you provide credentials by specifying a profile that
  you set up in your AWS credentials profile file. If you haven't already done
  so, first set up your credentials profile. For more information, see [Set up AWS Credentials and Region for Development](../../../sdk-for-java/v1/developer-guide/setup-credentials.md "../../../sdk-for-java/v1/developer-guide/setup-credentials.md") in the
  _AWS SDK for Java_.

###### Note

The Java example uses a
`SystemPropertiesCredentialsProvider` object to obtain
your credentials. The provider retrieves these credentials from the
`aws.accessKeyId` and `aws.secretKey` Java
system properties. You set these system properties in your Java
development environment. For information about how to set Java system
properties, see the documentation for your particular integrated
development environment (IDE).

- Your `NativeLibraryPath` must contain your
  `KinesisVideoProducerJNI` file, available at [https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-cpp").
  The file name extension for this file depends on your operating system:
  - **KinesisVideoProducerJNI.so** for
    Linux
  - **KinesisVideoProducerJNI.dylib** for
    macOS
  - **KinesisVideoProducerJNI.dll** for
    Windows

###### Note

Pre-built libraries for macOS, Ubuntu, Windows, and Raspbian are
available in `src/main/resources/lib` at [https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java.git](https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java "https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java").
For other environments, compile the [C++](producer-sdk-cpp.md "producer-sdk-cpp.md").
