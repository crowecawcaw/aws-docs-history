

# Update Python applications
<a name="troubleshooting-async-deadlock-update-python-apps"></a>

Python applications can use connectors in 2 different ways: packaging connectors and other Java dependencies as part of single uber-jar, or use connector jar directly. To fix applications affected by Async Sink deadlock:
+ If the application uses an uber jar, follow the instructions for [Update Java applications](troubleshooting-async-deadlock-update-java-apps.md).
+ To rebuild connector jars from source, use the following steps:

**Building connectors from source:**

Prerequisites, similar to Flink [build requirements](https://nightlies.apache.org/flink/flink-docs-release-1.15/docs/flinkdev/building/#build-flink):
+ Java 11
+ Maven 3.2.5

## flink-sql-connector-kinesis
<a name="troubleshooting-async-deadlock-update-python-apps-flink-sql-connector-kinesis"></a>

1. Download source code for Flink 1.15.4:

   ```
   wget https://archive.apache.org/dist/flink/flink-1.15.4/flink-1.15.4-src.tgz
   ```

1. Uncompress source code:

   ```
   tar -xvf flink-1.15.4-src.tgz
   ```

1. Navigate to kinesis connector directory

   ```
   cd flink-1.15.4/flink-connectors/flink-connector-kinesis/
   ```

1. Compile and install connector jar, specifying required AWS SDK version. To speed up build use `-DskipTests` to skip test execution and `-Dfast` to skip additional source code checks:

   ```
   mvn clean install -DskipTests -Dfast -Daws.sdkv2.version=2.20.144
   ```

1. Navigate to kinesis connector directory

   ```
   cd ../flink-sql-connector-kinesis
   ```

1. Compile and install sql connector jar:

   ```
   mvn clean install -DskipTests -Dfast
   ```

1. Resulting jar will be available at:

   ```
   target/flink-sql-connector-kinesis-1.15.4.jar
   ```

## flink-sql-connector-aws-kinesis-streams
<a name="troubleshooting-async-deadlock-update-python-apps-flink-sql-connector-aws-kinesis-streams"></a>

1. Download source code for Flink 1.15.4:

   ```
   wget https://archive.apache.org/dist/flink/flink-1.15.4/flink-1.15.4-src.tgz
   ```

1. Uncompress source code:

   ```
   tar -xvf flink-1.15.4-src.tgz
   ```

1. Navigate to kinesis connector directory

   ```
   cd flink-1.15.4/flink-connectors/flink-connector-aws-kinesis-streams/
   ```

1. Compile and install connector jar, specifying required AWS SDK version. To speed up build use `-DskipTests` to skip test execution and `-Dfast` to skip additional source code checks:

   ```
   mvn clean install -DskipTests -Dfast -Daws.sdk.version=2.20.144
   ```

1. Navigate to kinesis connector directory

   ```
   cd ../flink-sql-connector-aws-kinesis-streams
   ```

1. Compile and install sql connector jar:

   ```
   mvn clean install -DskipTests -Dfast
   ```

1. Resulting jar will be available at:

   ```
   target/flink-sql-connector-aws-kinesis-streams-1.15.4.jar
   ```

## flink-sql-connector-aws-kinesis-firehose
<a name="troubleshooting-async-deadlock-update-python-apps-flink-sql-connector-kinesis-firehose"></a>

1. Download source code for Flink 1.15.4:

   ```
   wget https://archive.apache.org/dist/flink/flink-1.15.4/flink-1.15.4-src.tgz
   ```

1. Uncompress source code:

   ```
   tar -xvf flink-1.15.4-src.tgz
   ```

1. Navigate to connector directory

   ```
   cd flink-1.15.4/flink-connectors/flink-connector-aws-kinesis-firehose/
   ```

1. Compile and install connector jar, specifying required AWS SDK version. To speed up build use `-DskipTests` to skip test execution and `-Dfast` to skip additional source code checks:

   ```
   mvn clean install -DskipTests -Dfast -Daws.sdk.version=2.20.144
   ```

1. Navigate to sql connector directory

   ```
   cd ../flink-sql-connector-aws-kinesis-firehose
   ```

1. Compile and install sql connector jar:

   ```
   mvn clean install -DskipTests -Dfast
   ```

1. Resulting jar will be available at:

   ```
   target/flink-sql-connector-aws-kinesis-firehose-1.15.4.jar
   ```

## flink-sql-connector-dynamodb
<a name="troubleshooting-async-deadlock-update-python-apps-flink-sql-connector-dynamodb"></a>

1. Download source code for Flink 1.15.4:

   ```
   wget https://archive.apache.org/dist/flink/flink-connector-aws-3.0.0/flink-connector-aws-3.0.0-src.tgz
   ```

1. Uncompress source code:

   ```
   tar -xvf flink-connector-aws-3.0.0-src.tgz
   ```

1. Navigate to connector directory

   ```
   cd flink-connector-aws-3.0.0
   ```

1. Compile and install connector jar, specifying required AWS SDK version. To speed up build use `-DskipTests` to skip test execution and `-Dfast` to skip additional source code checks:

   ```
   mvn clean install -DskipTests -Dfast -Dflink.version=1.15.4 -Daws.sdk.version=2.20.144
   ```

1. Resulting jar will be available at:

   ```
   flink-sql-connector-dynamodb/target/flink-sql-connector-dynamodb-3.0.0.jar
   ```