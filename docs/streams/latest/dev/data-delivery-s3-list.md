# List Amazon S3 deliveries

List the deliveries in your account, optionally filtered to the deliveries attached to
a specific stream. Use this to find deliveries before deleting a stream, or to audit
the deliveries configured in a AWS Region.

## Using the AWS Management Console

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. In the navigation pane, choose **S3 general purpose delivery**
   to view the list of deliveries, with columns such as name, status, source
   stream, and destination bucket.

## Using the AWS CLI

Use the `list-channels` command to list deliveries in the current
AWS Region:

```
aws kinesis list-channels
```

To list only the deliveries attached to a specific stream, provide a stream filter:

```
aws kinesis list-channels \
    --stream-filter StreamARN="arn:aws:kinesis:us-east-1:123456789012:stream/my-stream"
```

The response returns up to 100 deliveries per page. Use the pagination token in the
response to retrieve additional results.

**API reference** – see `ListChannels` in
the _Amazon Kinesis Data Streams API Reference_.
