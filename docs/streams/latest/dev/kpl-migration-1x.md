

# Migrate from KPL 0.x to KPL 1.x
<a name="kpl-migration-1x"></a>

This topic provides step-by-step instructions to migrate your consumer from KPL 0.x to KPL 1.x. KPL 1.x introduces support for the AWS SDK for Java 2.x while maintaining interface compatibility with previous versions. You don’t have to update your core data processing logic to migrate to KPL 1.x. 

1. **Make sure that you have the following prerequisites:**
   + Java Development Kit (JDK) 8 or later
   + AWS SDK for Java 2.x
   + Maven or Gradle for dependency management

1. **Add dependencies**

   If you're using Maven, add the following dependency to your pom.xml file. Make sure you updated the groupId from `com.amazonaws` to `software.amazon.kinesis` and the version `1.x.x` to the latest KPL version. 

   ```
   <dependency>
       <groupId>software.amazon.kinesis</groupId>
       <artifactId>amazon-kinesis-producer</artifactId>
       <version>1.x.x</version> <!-- Use the latest version -->
   </dependency>
   ```

   If you're using Gradle, add the following to your `build.gradle` file. Make sure to replace `1.x.x` with the latest KPL version. 

   ```
   implementation 'software.amazon.kinesis:amazon-kinesis-producer:1.x.x'
   ```

   You can check for the latest version of the KPL on the [Maven Central Repository](https://central.sonatype.com/search?q=amazon-kinesis-producer). 

1. **Update import statements for KPL**

   KPL 1.x uses the AWS SDK for Java 2.x and uses an updated package name that starts with `software.amazon.kinesis`, compared to the package name in the previous KPL that starts with `com.amazonaws.services.kinesis`.

   Replace the import for `com.amazonaws.services.kinesis` with `software.amazon.kinesis`. The following table lists the imports that you must replace.  
**Import replacements**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/streams/latest/dev/kpl-migration-1x.html)

1. **Update import statements for AWS credentials provider classes**

   When migrating to KPL 1.x, you must update packages and classes in your imports in your KPL application code that are based on the AWS SDK for Java 1.x to corresponding ones based on the AWS SDK for Java 2.x. Common imports in the KPL application are credentials provider classes. See [Credentials provider changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-credentials.html) in the AWS SDK for Java 2.x migration guide documentation for the full list of credentials provider changes. Here is the common import change that you might need to make in your KPL applications. 

   **Import in KPL 0.x**

   ```
   import com.amazonaws.auth.DefaultAWSCredentialsProviderChain;
   ```

   **Import in KPL 1.x**

   ```
   import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider;
   ```

   If you import any other credentials providers based on the AWS SDK for Java 1.x, you must update them to the AWS SDK for Java 2.x equivalent ones. If you didn’t import any classes/packages from the AWS SDK for Java 1.x, you can ignore this step.

1. **Update the credentials provider configuration in the KPL configuration**

   The credentials provider configuration in KPL 1.x requires the AWS SDK for Java 2.x credential providers. If you are passing credentials providers for the AWS SDK for Java 1.x in the `KinesisProducerConfiguration` by overriding the default credentials provider, you must update it with the AWS SDK for Java 2.x credential providers. See [Credentials provider changes](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/migration-client-credentials.html) in the AWS SDK for Java 2.x migration guide documentation for the full list of credentials provider changes. If you didn’t override the default credentials provider in the KPL configuration, you can ignore this step.

   For example, if you are overriding the default credentials provider for the KPL with the following code:

   ```
   KinesisProducerConfiguration config = new KinesisProducerConfiguration();
   // SDK v1 default credentials provider
   config.setCredentialsProvider(new DefaultAWSCredentialsProviderChain());
   ```

   You must update them with the following code to use the AWS SDK for Java 2.x credentials provider:

   ```
   KinesisProducerConfiguration config = new KinesisProducerConfiguration();
   // New SDK v2 default credentials provider
   config.setCredentialsProvider(DefaultCredentialsProvider.create());
   ```