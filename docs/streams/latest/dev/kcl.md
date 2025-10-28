# Use Kinesis Client Library

## What is Kinesis Client Library?

Kinesis Client Library (KCL) is a standalone Java software library designed to
simplify the process of consuming and processing data from Amazon Kinesis Data Streams. KCL
handles many of the complex tasks associated with distributed computing, letting
developers focus on implementing their business logic for processing data. It manages
activities such as load balancing across multiple workers, responding to worker
failures, checkpointing processed records, and responding to changes in the number of
shards in the stream.

KCL is frequently updated to incorporate newer versions of underlying
libraries, security improvements, and bug fixes. We recommend that you use the latest
version of KCL to avoid known issues and benefit from all latest improvements.
To find the latest KCL version, see [KCL Github](https://github.com/awslabs/amazon-kinesis-client "https://github.com/awslabs/amazon-kinesis-client").

###### Important

- We recommend that you use the latest KCL version to avoid known
  bugs and issues. If you are using KCL 2.6.0 or earlier, upgrade to
  KCL 2.6.1 or later to avoid a rare condition that can block shard
  processing when stream capacity changes.
- KCL is a Java library. Support for languages other than Java is
  provided using a Java-based daemon called MultiLangDaemon. MultiLangDaemon
  interacts with the KCL application over STDIN and STDOUT. For more
  information about the MultiLangDaemon on GitHub, see [Develop consumers with KCL in non-Java languages](develop-kcl-consumers-non-java.md "develop-kcl-consumers-non-java.md").
- Do not use AWS SDK for Java version 2.27.19 to 2.27.23 with KCL 3.x.
  These versions include an issue that causes an exception error related to
  KCL's DynamoDB usage. We recommend that you use the AWS SDK for Java version
  2.28.0 or later to avoid this issue.

## KCL key features and benefits

Following are the key features and related benefits of the KCL:

- **Scalability**: KCL enables
  applications to scale dynamically by distributing the processing load across
  multiple workers. You can scale your application in or out, manually or with
  auto-scaling, without worrying about load redistribution.
- **Load balancing**: KCL automatically
  balances the processing load across available workers, resulting in an even
  distribution of work across workers.
- **Checkpointing**: KCL manages
  checkpointing of processed records, enabling applications to resume processing
  from their last successfully processed position.
- **Fault tolerance**: KCL provides
  built-in fault tolerance mechanisms, making sure that data processing continues
  even if individual workers fail. KCL also provides at-least-once
  delivery.
- **Handling stream-level changes**: KCL
  adapts to shard splits and merges that might occur due to changes in data
  volume. It maintains ordering by making sure that child shards are processed
  only after their parent shard is completed and checkpointed.
- **Monitoring**: KCL integrates with
  Amazon CloudWatch for consumer-level monitoring.
- **Multi-language support**: KCL natively
  supports Java and enables multiple non-Java programming languages through
  MultiLangDaemon.
