# Download and configure the Java

producer library code

In this section of the Java producer library procedure, you download the Java example
code, import the project into your Java IDE, and configure the library locations.

For prerequisites and other details about this example, see [Using the Java producer
library](producer-sdk-javaapi.md "producer-sdk-javaapi.md").

1. Create a directory, and then clone the example source code from the GitHub
   repository.

```
git clone https://github.com/awslabs/amazon-kinesis-video-streams-producer-sdk-java
```

2.  Open the Java integrated development environment (IDE) that you use (for
    example, [Eclipse](https://www.eclipse.org/ "https://www.eclipse.org/") or [JetBrains IntelliJ IDEA](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/")), and
    import the Apache Maven project that you downloaded:

        * **In IntelliJ IDEA:**  Choose
         **Import**. Navigate to the `pom.xml`
         file in the root of the downloaded package.
        * **In Eclipse:** Choose
         **File**, **Import**,
         **Maven**, **Existing Maven
         Projects**. Then navigate to the
         `kinesis-video-java-demo` directory.

    For more information, see the documentation for your IDE.

3.  The Java example code uses the current AWS credentials. To use a different
    credentials profile, locate the following code in
    `DemoAppMain.java`:

```
final KinesisVideoClient kinesisVideoClient = KinesisVideoJavaClientFactory
    .createKinesisVideoClient(
        Regions.US_WEST_2,
        AuthHelper.getSystemPropertiesCredentialsProvider());
```

Change the code to the following:

```
final KinesisVideoClient kinesisVideoClient = KinesisVideoJavaClientFactory
    .createKinesisVideoClient(
        Regions.US_WEST_2,
        new ProfileCredentialsProvider("`credentials-profile-name`"));
```

For more information, see [ProfileCredentialsProvider](../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/profile/ProfileCredentialsProvider.md "../../../AWSJavaSDK/latest/javadoc/com/amazonaws/auth/profile/ProfileCredentialsProvider.md") in the _AWS SDK for Java_
reference.
