# Amazon Keyspaces (for Apache Cassandra) libraries and tools

This section provides information about Amazon Keyspaces (for Apache Cassandra) libraries, code examples, and tools.

###### Topics

- [Libraries and examples](#examples "#examples")
- [Highlighted sample and developer tool repos](#highlights "#highlights")

## Libraries and examples

You can find Amazon Keyspaces open-source libraries and developer tools on GitHub in the [AWS](https://github.com/aws "https://github.com/aws") and [AWS samples](https://github.com/aws-samples "https://github.com/aws-samples") repos.

### Amazon Keyspaces (for Apache Cassandra) developer toolkit

This repository provides a docker image with helpful developer tools for Amazon Keyspaces.
For example, it includes a CQLSHRC file with best practices, an optional AWS authentication expansion for cqlsh, and helper tools to perform common tasks.
The toolkit is optimized for Amazon Keyspaces, but also works with Apache Cassandra clusters.

[https://github.com/aws-samples/amazon-keyspaces-toolkit](https://github.com/aws-samples/amazon-keyspaces-toolkit "https://github.com/aws-samples/amazon-keyspaces-toolkit").

### Amazon Keyspaces (for Apache Cassandra) examples

This repo is our official list of Amazon Keyspaces example code. The repo is subdivided into sections by
language (see [Examples](https://github.com/aws-samples/amazon-keyspaces-examples#Examples/ "https://github.com/aws-samples/amazon-keyspaces-examples#Examples/")). Each language has
its own subsection of examples.
These examples demonstrate common Amazon Keyspaces service implementations and patterns that you can use when building applications.

[https://github.com/aws-samples/amazon-keyspaces-examples/](https://github.com/aws-samples/amazon-keyspaces-examples/ "https://github.com/aws-samples/amazon-keyspaces-examples/").

### AWS Signature Version 4 (SigV4) authentication plugins

The plugins enable you to manage access to Amazon Keyspaces by using AWS Identity and Access Management (IAM) users and roles.

Java: [https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-java-driver-plugin").

Node.js: [https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-nodejs-driver-plugin").

Python: [https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-python-driver-plugin").

Go: [https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin](https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin "https://github.com/aws/aws-sigv4-auth-cassandra-gocql-driver-plugin").

## Highlighted sample and developer tool repos

Below are a selection of helpful community tools for Amazon Keyspaces (for Apache Cassandra).

### Amazon Keyspaces Protocol Buffers

You can use Protocol Buffers (Protobuf) with Amazon Keyspaces to provide an alternative to Apache Cassandra User Defined Types (UDTs).
Protobuf is a free and open-source cross-platform data format which is used to serialize structured data. You can store
Protobuf data using the CQL `BLOB` data type and refactor UDTs while preserving structured data across
applications and programming languages.

This repository provides a code example that connects to Amazon Keyspaces, creates a new table, and inserts a row containing a
Protobuf message. Then the row is read with strong consistency.

[https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/protobuf-user-defined-types](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/protobuf-user-defined-types "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/protobuf-user-defined-types")

### AWS CloudFormation template to create Amazon CloudWatch dashboard for Amazon Keyspaces (for Apache Cassandra) metrics

This repository provides AWS CloudFormation templates to quickly set up CloudWatch metrics for Amazon Keyspaces. Using this template will allow you to get started
more easily by providing deployable prebuilt CloudWatch dashboards with commonly used metrics.

[https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates](https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates "https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates").

### Using Amazon Keyspaces (for Apache Cassandra) with AWS Lambda

The repository contains examples that show how to connect to Amazon Keyspaces from Lambda. Below are some examples.

C#/.NET: [https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/dotnet/datastax-v3/connection-lambda](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/dotnet/datastax-v3/connection-lambda "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/dotnet/datastax-v3/connection-lambda").

Java: [https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/connection-lambda](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/connection-lambda "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/connection-lambda").

Another Lambda example that shows how to deploy and use Amazon Keyspaces from a Python Lambda is available from the following repo.

[https://github.com/aws-samples/aws-keyspaces-lambda-python](https://github.com/aws-samples/aws-keyspaces-lambda-python "https://github.com/aws-samples/aws-keyspaces-lambda-python")

### Using Amazon Keyspaces (for Apache Cassandra) with Spring

This is an example that shows you how to use Amazon Keyspaces with Spring Boot.

[https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/java/datastax-v4/spring")

### Using Amazon Keyspaces (for Apache Cassandra) with Scala

This is an example that shows how to connect to Amazon Keyspaces using the SigV4 authentication plugin with Scala.

[https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/connection-sigv4](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/connection-sigv4 "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/connection-sigv4")

### Using Amazon Keyspaces (for Apache Cassandra) with AWS Glue

This is an example that shows how to use Amazon Keyspaces with AWS Glue.

[https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue](https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue "https://github.com/aws-samples/amazon-keyspaces-examples/tree/main/scala/datastax-v4/aws-glue")

### Amazon Keyspaces (for Apache Cassandra) Cassandra query language (CQL) to AWS CloudFormation converter

This package implements a command-line tool for converting Apache Cassandra Query Language (CQL) scripts to AWS CloudFormation
(CloudFormation) templates, which allows Amazon Keyspaces schemas to be easily managed in CloudFormation stacks.

[https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter](https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter "https://github.com/aws/amazon-keyspaces-cql-to-cfn-converter").

### Amazon Keyspaces (for Apache Cassandra) helpers for Apache Cassandra driver for Java

This repository contains driver policies, examples, and best practices when using the DataStax Java Driver with Amazon Keyspaces (for Apache Cassandra).

[https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers](https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers "https://github.com/aws-samples/amazon-keyspaces-java-driver-helpers").

### Amazon Keyspaces (for Apache Cassandra) snappy compression demo

This repository demonstrates how to compress, store, and read/write large objects for faster performance and lower throughput and storage costs.

[https://github.com/aws-samples/amazon-keyspaces-compression-example](https://github.com/aws-samples/amazon-keyspaces-compression-example "https://github.com/aws-samples/amazon-keyspaces-compression-example").

### Amazon Keyspaces (for Apache Cassandra) and Amazon S3 codec demo

Custom Amazon S3 Codec supports transparent, user-configurable mapping of UUID pointers to Amazon S3 objects.

[https://github.com/aws-samples/amazon-keyspaces-large-object-s3-demo](https://github.com/aws-samples/amazon-keyspaces-large-object-s3-demo "https://github.com/aws-samples/amazon-keyspaces-large-object-s3-demo").
