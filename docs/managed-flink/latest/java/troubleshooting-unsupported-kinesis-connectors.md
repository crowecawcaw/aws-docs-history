

# Applications with unsupported Kinesis connectors
<a name="troubleshooting-unsupported-kinesis-connectors"></a>

Managed Service for Apache Flink for Apache Flink version 1.15 or later will [automatically reject applications from starting or updating](https://docs.aws.amazon.com/managed-flink/latest/java/flink-1-15-2.html) if they are using unsupported Kinesis Connector versions (pre-version 1.15.2) bundled into application JARs or archives (ZIP). 

## Rejection error
<a name="troubleshooting-unsupported-kinesis-connectors-error"></a>

You will see the following error when submitting create / update application calls through:

```
An error occurred (InvalidArgumentException) when calling the CreateApplication operation: An unsupported Kinesis connector version has been detected in the application. Please update flink-connector-kinesis to any version equal to or newer than 1.15.2.
For more information refer to connector fix: https://issues.apache.org/jira/browse/FLINK-23528
```

## Steps to remediate
<a name="troubleshooting-unsupported-kinesis-connectors-steps-to-remediate"></a>
+ Update the application’s dependency on `flink-connector-kinesis`. If you are using Maven as your project’s build tool, follow [Update a Maven dependency](#troubleshooting-unsupported-kinesis-connectors-update-maven-dependency). If you are using Gradle, follow [Update a Gradle dependency](#troubleshooting-unsupported-kinesis-connectors-update-gradle-dependency).
+ Repackage the application.
+ Upload to an Amazon S3 bucket.
+ Resubmit the create / update application request with the revised application just uploaded to the Amazon S3 bucket.
+ If you continue to see the same error message, re-check your application dependencies. If the problem persists please create a support ticket. 

### Update a Maven dependency
<a name="troubleshooting-unsupported-kinesis-connectors-update-maven-dependency"></a>

1. Open the project’s `pom.xml`.

1. Find the project’s dependencies. They look like:

   ```
   <project>
   
       ...
   
       <dependencies>
   
           ...
   
           <dependency>
               <groupId>org.apache.flink</groupId>
               <artifactId>flink-connector-kinesis</artifactId>
           </dependency>
   
           ...
   
       </dependencies>
   
       ...
   
   </project>
   ```

1. Update `flink-connector-kinesis` to a version that is equal to or newer than 1.15.2. For instance:

   ```
   <project>
   
       ...
   
       <dependencies>
   
           ...
   
           <dependency>
               <groupId>org.apache.flink</groupId>
               <artifactId>flink-connector-kinesis</artifactId>
               <version>1.15.2</version>
           </dependency>
   
           ...
   
       </dependencies>
   
       ...
   
   </project>
   ```

### Update a Gradle dependency
<a name="troubleshooting-unsupported-kinesis-connectors-update-gradle-dependency"></a>

1. Open the project’s `build.gradle` (or `build.gradle.kts` for Kotlin applications). 

1. Find the project’s dependencies. They look like:

   ```
   ...
   
   dependencies {
   
       ...
   
       implementation("org.apache.flink:flink-connector-kinesis")
   
       ...
   
   }
   
   ...
   ```

1. Update `flink-connector-kinesis` to a version that is equal to or newer than 1.15.2. For instance:

   ```
   ...
   
   dependencies {
   
       ...
   
       implementation("org.apache.flink:flink-connector-kinesis:1.15.2")
   
       ...
   
   }
   
   ...
   ```