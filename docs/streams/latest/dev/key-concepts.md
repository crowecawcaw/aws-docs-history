# Amazon Kinesis Data Streams Terminology and concepts

Before you get started with Amazon Kinesis Data Streams, learn about its architecture and
terminology.

###### Topics

- [Review the high-level architecture of
  Kinesis Data Streams](#high-level-architecture "#high-level-architecture")
- [Become familiar with the terminology of Kinesis Data Streams](#terminology "#terminology")

## Review the high-level architecture of

Kinesis Data Streams

The following diagram illustrates the high-level architecture of Kinesis Data Streams. The
_producers_ continually push data to Kinesis Data Streams, and the
_consumers_ process the data in real time. Consumers (such as a
custom application running on Amazon EC2 or an Amazon Data Firehose delivery stream) can store their
results using an AWS service such as Amazon DynamoDB, Amazon Redshift, or Amazon S3.

![Kinesis Data Streams high-level architecture diagram](images/architecture.png)

## Become familiar with the terminology of Kinesis Data Streams

### Kinesis Data Stream

A _Kinesis data stream_ is a set of [shards](#shard "#shard").
Each shard has a sequence of data records. Each data record has a [sequence number](#sequence-number "#sequence-number") that is assigned by Kinesis Data Streams.

### Data Record

A _data record_ is the unit of data stored in a [Kinesis data stream](#stream "#stream"). Data records are composed of a [sequence number](#sequence-number "#sequence-number"), a [partition key](#partition-key "#partition-key"), and a data blob, which is an
immutable sequence of bytes. Kinesis Data Streams does not inspect, interpret, or change the data
in the blob in any way. A data blob can be up to 1 MB.

### Capacity Mode

A data stream _capacity mode_ determines how capacity is
managed and how you are charged for the usage of your data stream. Currently, in
Kinesis Data Streams, you can choose between an **on-demand** mode and a **provisioned** mode
for your data streams. For more information, see [Choose the data stream capacity mode](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md").

With the **on-demand** mode, Kinesis Data Streams
automatically manages the shards in order to provide the necessary throughput. You
are charged only for the actual throughput that you use and Kinesis Data Streams
automatically accommodates your workloads’ throughput needs as they ramp up or down.
For more information, see [On-demand mode features and use cases](how-do-i-size-a-stream.md#ondemandmode "how-do-i-size-a-stream.md#ondemandmode").

With the **provisioned** mode, you must specify the
number of shards for the data stream. The total capacity of a data stream is the sum
of the capacities of its shards. You can increase or decrease the number of shards
in a data stream as needed and you are charged for the number of shards at an hourly
rate. For more information, see [Provisioned mode features and use cases](how-do-i-size-a-stream.md#provisionedmode "how-do-i-size-a-stream.md#provisionedmode").

### Retention Period

The _retention period_ is the length of time that data records
are accessible after they are added to the stream. A stream’s retention period is
set to a default of 24 hours after creation. You can increase the retention period
up to
8760
hours
(365
days) using the [IncreaseStreamRetentionPeriod](../../../kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.md "../../../kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.md") operation, and decrease the
retention period down to a minimum of 24 hours using the
[DecreaseStreamRetentionPeriod](../../../kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.md "../../../kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.md") operation. Additional charges apply for streams
with a retention period set to more than 24 hours. For more information, see
[Amazon Kinesis Data Streams Pricing](https://aws.amazon.com/kinesis/pricing/ "https://aws.amazon.com/kinesis/pricing/").

### Producer

_Producers_ put records into Amazon Kinesis Data Streams. For example, a web
server sending log data to a stream is a producer.

### Consumer

_Consumers_ get records from Amazon Kinesis Data Streams and process them. These
consumers are known as [Amazon Kinesis Data Streams Application](#enabled-application "#enabled-application").

### Amazon Kinesis Data Streams Application

An _Amazon Kinesis Data Streams application_ is a consumer of a stream that commonly runs on a
fleet of EC2 instances.

There are two types of consumers that you can develop: shared fan-out consumers
and enhanced fan-out consumers. To learn about the differences between them, and to
see how you can create each type of consumer, see [Read data from Amazon Kinesis Data Streams](building-consumers.md "building-consumers.md").

The output of a Kinesis Data Streams application can be input for another stream, enabling you to
create complex topologies that process data in real time. An application can also
send data to a variety of other AWS services. There can be multiple applications
for one stream, and each application can consume data from the stream independently
and concurrently.

### Shard

A _shard_ is a uniquely identified sequence of data records in
a stream. A stream is composed of one or more shards, each of which provides a fixed
unit of capacity. Each shard can support up to 5 transactions per second for reads, up to a maximum total data read rate of 2 MB per second and up to 1,000 records per second for writes, up to a maximum total data write rate of 1 MB per second (including partition keys). The
data capacity of your stream is a function of the number of shards that you specify
for the stream. The total capacity of the stream is the sum of the capacities of its
shards.

If your data rate increases, you can increase or decrease the number of shards
allocated to your stream. For more information, see [Reshard a stream](kinesis-using-sdk-java-resharding.md "kinesis-using-sdk-java-resharding.md").

### Partition Key

A _partition key_ is used to group data by shard within a
stream. Kinesis Data Streams segregates the data records belonging to a stream into multiple
shards. It uses the partition key that is associated with each data record to
determine which shard a given data record belongs to. Partition keys are Unicode
strings, with a maximum length limit of 256 characters for each key. An MD5 hash
function is used to map partition keys to 128-bit integer values and to map
associated data records to shards using the hash key ranges of the shards. When an
application puts data into a stream, it must specify a partition key.

### Sequence Number

Each data record has a _sequence number_ that is unique per
partition-key within its shard. Kinesis Data Streams assigns the sequence number after you write to
the stream with `client.putRecords` or `client.putRecord`.
Sequence numbers for the same partition key generally increase over time. The longer
the time period between write requests, the larger the sequence numbers
become.

###### Note

Sequence numbers cannot be used as indexes to sets of data within the same
stream. To logically separate sets of data, use partition keys or create a
separate stream for each dataset.

### Kinesis Client Library

Kinesis Client Library is compiled into your application to enable fault-tolerant
consumption of data from the stream. Kinesis Client Library makes sure that for every
shard there is a record processor running and processing that shard. The library
also simplifies reading data from the stream. Kinesis Client Library uses Amazon DynamoDB
tables to store metadata related to data consumption. It creates three tables per
application that is processing data. For more information, see [Use Kinesis Client Library](kcl.md "kcl.md").

### Application Name

The name of an Amazon Kinesis Data Streams application identifies the application. Each of your applications must
have a unique name that is scoped to the AWS account and Region used by the
application. This name is used as a name for the control table in Amazon DynamoDB and the
namespace for Amazon CloudWatch metrics.

### Server-Side Encryption

Amazon Kinesis Data Streams can automatically encrypt sensitive data as a producer enters it into a
stream. Kinesis Data Streams uses [AWS KMS](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md") master keys for
encryption. For more information, see [Data protection in Amazon Kinesis Data Streams](server-side-encryption.md "server-side-encryption.md").

###### Note

To read from or write to an encrypted stream, producer and consumer
applications must have permission to access the master key. For information
about granting permissions to producer and consumer applications, see [Permissions to use user-generated
KMS keys](permissions-user-key-KMS.md "permissions-user-key-KMS.md").

###### Note

Using server-side encryption incurs AWS Key Management Service (AWS KMS) costs. For more
information, see [AWS Key
Management Service Pricing](http://aws.amazon.com/kms/pricing "http://aws.amazon.com/kms/pricing").
