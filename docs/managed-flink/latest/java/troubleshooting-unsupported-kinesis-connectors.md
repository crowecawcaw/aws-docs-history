Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Applications with unsupported Kinesis connectors

Managed Service for Apache Flink for Apache Flink version 1.15 or later will [automatically reject applications
from starting or updating](flink-1-15-2.md "flink-1-15-2.md") if they are using unsupported Kinesis Connector
versions (pre-version 1.15.2) bundled into application JARs or archives (ZIP).

## Rejection

error

You will see the following error when submitting create / update application calls through:

```
An error occurred (InvalidArgumentException) when calling the CreateApplication operation: An unsupported Kinesis connector version has been detected in the application. Please update flink-connector-kinesis to any version equal to or newer than 1.15.2.
For more information refer to connector fix: https://issues.apache.org/jira/browse/FLINK-23528
```

## Steps to remediate

- Update the application’s dependency on `flink-connector-kinesis`. If you are using Maven as your project’s build tool,
  follow [Update a Maven dependency](#troubleshooting-unsupported-kinesis-connectors-update-maven-dependency "#troubleshooting-unsupported-kinesis-connectors-update-maven-dependency") . If you are using Gradle, follow
  [Update a Gradle dependency](#troubleshooting-unsupported-kinesis-connectors-update-gradle-dependency "#troubleshooting-unsupported-kinesis-connectors-update-gradle-dependency") .
- Repackage the application.
- Upload to an Amazon S3 bucket.
- Resubmit the create / update application request with the revised application just uploaded to the Amazon S3 bucket.
- If you continue to see the same error message, re-check your application dependencies. If the problem persists please create a support ticket.

### Update a Maven dependency

1. Open the project’s `pom.xml`.
2. Find the project’s dependencies. They look like:

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

3. Update `flink-connector-kinesis` to a version that is equal to or newer than 1.15.2. For instance:

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

1. Open the project’s `build.gradle` (or `build.gradle.kts` for Kotlin applications).
2. Find the project’s dependencies. They look like:

```
...

dependencies {

    ...

    implementation("org.apache.flink:flink-connector-kinesis")

    ...

}

...
```

3. Update `flink-connector-kinesis` to a version that is equal to or newer than 1.15.2. For instance:

```
...

dependencies {

    ...

    implementation("org.apache.flink:flink-connector-kinesis:1.15.2")

    ...

}

...
```
