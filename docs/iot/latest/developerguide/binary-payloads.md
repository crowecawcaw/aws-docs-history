# Working with binary payloads

To handle your message payload as raw binary data (rather than a JSON object), you can
use the \* operator to refer to it in a SELECT clause.

###### In this topic:

- [Binary payload examples](#binary-payloads-examples "#binary-payloads-examples")
- [Decoding protobuf message
  payloads](#binary-payloads-protobuf "#binary-payloads-protobuf")

## Binary payload examples

When you use \* to refer to the message payload as raw binary data, you can add
data to the rule. If you have an empty or a JSON payload, the resulting payload can
have data added using the rule. The following shows examples of supported
`SELECT` clauses.

- You can use the following `SELECT` clauses with only a \* for
  binary payloads.
  - ```
    SELECT * FROM 'topic/subtopic'
    ```

  ````
  + ```
  SELECT * FROM 'topic/subtopic' WHERE timestamp() % 12 = 0
  ````

- You can also add data and use the following `SELECT`
  clauses.
  - ```
    SELECT *, principal() as principal, timestamp() as time FROM 'topic/subtopic'
    ```

  ````
  + ```
  SELECT encode(*, 'base64') AS data, timestamp() AS ts FROM 'topic/subtopic'
  ````

- You can also use these `SELECT` clauses with binary
  payloads.
  - The following refers to `device_type` in the WHERE clause.

  ```
  SELECT * FROM 'topic/subtopic' WHERE device_type = 'thermostat'
  ```

  - The following is also supported.

  ```
  {
  	"sql": "SELECT * FROM 'topic/subtopic'",
  	"actions": [
  		{
  			"republish": {
  				"topic": "device/${device_id}"
  			}
  		}
  	]
  }
  ```

The following rule actions don't support binary payloads so you must decode
them.

- Some rule actions don't support binary payload input, such as a [Lambda
  action](iot-rule-actions.md#lambda-rule "iot-rule-actions.md#lambda-rule"), so you must decode binary payloads. The Lambda rule
  action can receive binary data, if it's base64 encoded and in a JSON
  payload. You can do this by changing the rule to the following.

```
SELECT encode(*, 'base64') AS data FROM 'my_topic'
```

- The SQL statement doesn't support string as input. To convert a string
  input to JSON, you can run the following command.

```
SELECT decode(encode(*, 'base64'), 'base64') AS payload FROM 'topic'
```

## Decoding protobuf message

payloads

[Protocol Buffers
(protobuf)](https://developers.google.com/protocol-buffers "https://developers.google.com/protocol-buffers") is an open-source data format used to serialize structured
data in a compact, binary form. It's used for transmitting data over networks or
storing it in files. Protobuf allows you to send data in small packet sizes and at a
faster rate than other messaging formats. AWS IoT Core Rules support protobuf by
providing the [decode(value,
decodingScheme)](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64") SQL function, which allows you to decode protobuf-encoded
message payloads to JSON format and route them to downstream services. This section
details the step-by-step process to configure protobuf decoding in AWS IoT Core
Rules.

###### In this section:

- [Prerequisites](#binary-payloads-protobuf-prerequisites "#binary-payloads-protobuf-prerequisites")
- [Create descriptor
  files](#binary-payloads-protobuf-descriptor-steps "#binary-payloads-protobuf-descriptor-steps")
- [Upload descriptor files to
  S3 bucket](#binary-payloads-protobuf-s3-steps "#binary-payloads-protobuf-s3-steps")
- [Configure protobuf decoding in
  Rules](#binary-payloads-protobuf-steps "#binary-payloads-protobuf-steps")
- [Limitations](#binary-payloads-protobuf-limitations "#binary-payloads-protobuf-limitations")
- [Best practices](#binary-payloads-protobuf-bestpractices "#binary-payloads-protobuf-bestpractices")

### Prerequisites

- A basic understanding of [Protocol
  Buffers (protobuf)](https://developers.google.com/protocol-buffers "https://developers.google.com/protocol-buffers")
- The [`.proto` files](https://developers.google.com/protocol-buffers/docs/proto3 "https://developers.google.com/protocol-buffers/docs/proto3") that define message types and
  related dependencies
- Installing [Protobuf
  Compiler (protoc)](https://github.com/protocolbuffers/protobuf/releases "https://github.com/protocolbuffers/protobuf/releases") on your system

### Create descriptor

files

If you already have your descriptor files, you can skip this step. A
descriptor file (`.desc`) is a compiled version of a
`.proto` file, which is a text file that defines the data
structures and message types to be used in a protobuf serialization. To generate
a descriptor file, you must define a `.proto` file and use the [protoc](https://github.com/protocolbuffers/protobuf/releases "https://github.com/protocolbuffers/protobuf/releases")
compiler to compile it.

1. Create `.proto` files that define the message types. An example
   `.proto` file can look like the following:

```
syntax = "proto3";

message Person {
  optional string name = 1;
  optional int32 id = 2;
  optional string email = 3;
}
```

In this example `.proto` file, you use proto3 syntax and define
message type `Person`. The `Person` message
definition specifies three fields (name, id, and email). For more
information about `.proto` file message formats, see [Language Guide (proto3)](https://developers.google.com/protocol-buffers/docs/proto3 "https://developers.google.com/protocol-buffers/docs/proto3"). 2. Use the [protoc](https://github.com/protocolbuffers/protobuf/releases "https://github.com/protocolbuffers/protobuf/releases") compiler to compile the `.proto` files
and generate a descriptor file. An example command to create a
descriptor (`.desc`) file can be the following:

```
protoc --descriptor_set_out=<FILENAME>.desc \
    --proto_path=<PATH_TO_IMPORTS_DIRECTORY> \
    --include_imports \
    <PROTO_FILENAME>.proto
```

This example command generates a descriptor file
`<FILENAME>.desc`, which AWS IoT Core Rules can use to decode
protobuf payloads that conform to the data structure defined in
`<PROTO_FILENAME>.proto`.

    * `--descriptor_set_out`


    Specifies the name of the descriptor file
     (`<FILENAME>.desc` ) that should be generated.
    * `--proto_path`


    Specifies the locations of any imported `.proto` files that
     are referenced by the file being compiled. You can specify the flag
     multiple times if you have multiple imported `.proto` files
     with different locations.
    * `--include_imports`


    Specifies that any imported `.proto` files should also be
     compiled and included in the `<FILENAME>.desc` descriptor
     file.
    * `<PROTO_FILENAME>.proto`


    Specifies the name of the `.proto` file that you want to
     compile.

For more information about the protoc reference, see [API Reference](https://developers.google.com/protocol-buffers/docs/reference/overview "https://developers.google.com/protocol-buffers/docs/reference/overview").

### Upload descriptor files to

S3 bucket

After you create your descriptor files `<FILENAME>.desc`, upload
the descriptor files `<FILENAME>.desc` to an Amazon S3 bucket, using
the AWS API, AWS SDK, or the AWS Management Console.

**Important considerations**

- Make sure that you upload the descriptor files to an Amazon S3 bucket in
  your AWS account in the same AWS Region where you intend to
  configure your Rules.
- Make sure that you grant AWS IoT Core access to read the `FileDescriptorSet` from S3.
  If your S3 bucket has server-side encryption (SSE) disabled or if your
  S3 bucket is encrypted using Amazon S3-managed keys (SSE-S3), no additional
  policy configurations are required. This can be accomplished with the
  example bucket policy:

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "Service": "iot.amazonaws.com"
 },
 "Action": "s3:Get*",
 "Resource": "arn:aws:s3:::`<BUCKET NAME>`/`<FILENAME>.desc`"
 }
 ]
}`

```

- If your S3 bucket is encrypted using an AWS Key Management Service key (SSE-KMS), make
  sure that you grant AWS IoT Core permission to use the key when accessing
  your S3 bucket. You can do this by adding this statement to your key
  policy:

```
{
	"Sid": "Statement1",
	"Effect": "Allow",
	"Principal": {
		"Service": "iot.amazonaws.com"
	},
	"Action": [
		"kms:Decrypt",
		"kms:GenerateDataKey*",
		"kms:DescribeKey"
	],
        "Resource": "arn:aws:kms:`us-west-2`:`111122223333`:key/`1234abcd-12ab-34cd-56ef-1234567890ab`"

}
```

### Configure protobuf decoding in

Rules

After you upload the descriptor files to your Amazon S3 bucket, configure a [Rule](iot-create-rule.md "iot-create-rule.md") that can decode your protobuf message payload format using the
[decode(value, decodingScheme)](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64")
SQL function. A detailed function signature and example can be found in the
[decode(value, decodingScheme)](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64")
SQL function of the _AWS IoT SQL
reference_.

The following is an example SQL expression using the [decode(value, decodingScheme)](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64")
function:

```
SELECT VALUE decode(*, 'proto', '<BUCKET NAME>', '<FILENAME>.desc', '<PROTO_FILENAME>', '<PROTO_MESSAGE_TYPE>') FROM '<MY_TOPIC>'
```

In this example expression:

- You use the [decode(value,
  decodingScheme)](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64") SQL function to decode the binary message
  payload referenced by `*`. This can be a binary
  protobuf-encoded payload or a JSON string that represents a
  base64-encoded protobuf payload.
- The message payload provided is encoded using the `Person`
  message type defined in `PROTO_FILENAME.proto`.
- The Amazon S3 bucket named `BUCKET NAME` contains the
  `FILENAME.desc` generated from
  `PROTO_FILENAME.proto`.

After you complete the configuration, publish a message to AWS IoT Core on the
topic to which the Rule is subscribed.

### Limitations

AWS IoT Core Rules support protobuf with the following limitations:

- Decoding protobuf message payloads within [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md") is not supported.
- When decoding protobuf message payloads, you can use the [decode SQL function](iot-sql-functions.md#iot-sql-decode-base64 "iot-sql-functions.md#iot-sql-decode-base64") within a
  single SQL expression up to two times.
- The maximum inbound payload size is 128 KiB (1KiB =1024 bytes), the
  maximum outbound payload size is 128 KiB, and the maximum size for a
  `FileDescriptorSet` object stored in an Amazon S3 bucket is 32
  KiB.
- Amazon S3 buckets encrypted with SSE-C encryption are not supported.

### Best practices

Here are some best practices and troubleshooting tips.

- Back up your proto files in the Amazon S3 bucket.

It's a good practice to back up your proto files in case something
goes wrong. For example, if you incorrectly modify the proto files
without backups when running protoc, this can cause issues in your
production stack. There are multiple ways to back up your files in an
Amazon S3 bucket. For example, you can [use versioning in
S3 buckets](../../../AmazonS3/latest/userguide/Versioning.md "../../../AmazonS3/latest/userguide/Versioning.md"). For more information about how to back up files
in Amazon S3 buckets, refer to the _[Amazon S3 Developer Guide](../../../aws-backup/latest/devguide/recovery-points.md "../../../aws-backup/latest/devguide/recovery-points.md")_.

- Configure AWS IoT logging to view log entries.

It's a good practice to configure AWS IoT logging so that you can check
AWS IoT logs for your account in CloudWatch. When a rule's SQL query calls an
external function, AWS IoT Core Rules generates a log entry with an
`eventType` of `FunctionExecution`, which
contains the reason field that will help you troubleshoot failures.
Possible errors include an Amazon S3 object not found, or invalid protobuf
file descriptor. For more information about how to configure AWS IoT
logging and see the log entries, see [Configure
AWS IoT logging](configure-logging.md "configure-logging.md") and [Rules engine log entries](cwl-format.md#log-rules-fn-exec "cwl-format.md#log-rules-fn-exec").

- Update `FileDescriptorSet` using a new object key and update the object
  key in your Rule.

You can update `FileDescriptorSet` by uploading an updated
descriptor file to your Amazon S3 bucket. Your updates to
`FileDescriptorSet` can take up to 15 minutes to be
reflected. To avoid this delay, it's a good practice to upload your
updated `FileDescriptorSet` using a new object key, and
update the object key in your Rule.
