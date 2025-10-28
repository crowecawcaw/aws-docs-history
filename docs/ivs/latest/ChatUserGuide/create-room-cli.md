# CLI Instructions for Creating an IVS Chat Room

This document takes you through the steps involved in creating an Amazon IVS chat room using the AWS CLI.

## Creating a Chat Room

Creating a chat room with the AWS CLI is an advanced option and requires that
you first download and configure the CLI on your machine. For details, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

1. Run the chat `create-room` command and pass in an optional
   name:

```
aws ivschat create-room --name test-room
```

2. This returns a new chat room:

```
{
   "arn": "arn:aws:ivschat:us-west-2:123456789012:room/g1H2I3j4k5L6",
   "id": "string",
   "createTime": "2021-06-07T14:26:05-07:00",
   "maximumMessageLength": 200,
   "maximumMessageRatePerSecond": 10,
   "name": "test-room",
   "tags": {},
   "updateTime": "2021-06-07T14:26:05-07:00"
}
```

3. Note the `arn` field. You will need this to create a client
   token and connect to a chat room.

## Setting Up a Logging Configuration

(Optional)

As with
creating a chat room, setting up a logging configuration with the AWS CLI is
an advanced option and requires that you first download and configure the
CLI on your machine. For details, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md").

1. Run the chat `create-logging-configuration` command and
   pass in an optional name and a destination configuration pointing to an
   Amazon S3 bucket by name. This Amazon S3 bucket must exist before
   creating the logging configuration. (For details on creating an Amazon
   S3 bucket, see [Amazon S3 Documentation](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md").)

```
aws ivschat create-logging-configuration \
   --destination-configuration s3={bucketName=demo-logging-bucket} \
   --name "test-logging-config"
```

2. This returns a new logging configuration:

```
{
   "Arn": "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ",
   "createTime": "2022-09-14T17:48:00.653000+00:00",
   "destinationConfiguration": {
      "s3": {"bucketName": "demo-logging-bucket"}
   },
   "id": "ABcdef34ghIJ",
   "name": "test-logging-config",
   "state": "ACTIVE",
   "tags": {},
   "updateTime": "2022-09-14T17:48:01.104000+00:00"
}
```

3. Note the `arn` field. You need this to attach the logging configuration to the chat
   room.
   1. If you are creating a new chat room, run the `create-room` command and pass the
      logging-configuration `arn`:

   ```
   aws ivschat create-room --name test-room \
   --logging-configuration-identifiers \
   "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"
   ```

   2. If you are updating an existing chat room, run the `update-room` command and pass
      the logging-configuration `arn`:

   ```
   aws ivschat update-room --identifier \
   "arn:aws:ivschat:us-west-2:12345689012:room/g1H2I3j4k5L6" \
   --logging-configuration-identifiers \
   "arn:aws:ivschat:us-west-2:123456789012:logging-configuration/ABcdef34ghIJ"
   ```
