Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Configuring Amazon S3 compatible storage on Snowball Edge event

notifications

Amazon S3 compatible storage on Snowball Edge supports Amazon S3 event notifications for object API calls based on the Message Queuing Telemetry Transport (MQTT)
protocol.

You can use Amazon S3 compatible storage on Snowball Edge to receive notifications when certain events happen in your S3
bucket. To enable notifications, add a notification configuration that identifies the
events that you want the service to publish.

Amazon S3 compatible storage on Snowball Edge supports the following notification types:

- New object created events
- Object removal events
- Object tagging events

###### Configure Amazon S3 event notifications

1. Before you begin, you must have MQTT infrastructure in your network.
2. In your Snowball Edge client, run the `snowballEdge configure`
   command to set up the Snowball Edge device.

When prompted, enter the following information:

    * The path to your manifest file.
    * The device's unlock code.
    * The device's endpoint (for example,
     `https://10.0.0.1`).

3. Run the following `put-notification-configuration` command to send
   notifications to an external broker.

```
snowballEdge put-notification-configuration --broker-endpoint ssl://`mqtt-broker-ip-address`:8883 --enabled true --service-id s3-snow --ca-certificate file:`path-to-mqtt-broker-ca-cert`
```

4. Run the following `get-notification-configuration` command to
   verify that everything is set up correctly:

```
snowballEdge get-notification-configuration --service-id s3-snow
```

This returns the broker endpoint and enabled field.
After you configure the entire cluster to send notifications to the MQTT broker in the
network, every object API call will result in an event notification.

###### Note

You need to subscribe to the topic s3SnowEvents/`Device
 ID` (or `Cluster Id` if it is a
cluster)/bucketName. You can also use wildcards, for example topic name can be
`#` or
`s3SnowEvents/#`.

The following is an example Amazon S3 compatible storage on Snowball Edge event log:

```

{
    "eventDetails": {
        "additionalEventData": {
            "AuthenticationMethod": "AuthHeader",
            "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "SignatureVersion": "SigV4",
            "bytesTransferredIn": 1205,
            "bytesTransferredOut": 0,
            "x-amz-id-2": "uLdTfvdGTKlX6TBgCZtDd9Beef8wzUurA+Wpht7rKtfdaNsnxeLILg=="
        },
        "eventName": "PutObject",
        "eventTime": "2023-01-30T14:13:24.772Z",
        "requestAuthLatencyMillis": 40,
        "requestBandwidthKBs": 35,
        "requestID": "140CD93455CB62B4",
        "requestLatencyMillis": 77,
        "requestLockLatencyNanos": 1169953,
        "requestParameters": {
            "Content-Length": "1205",
            "Content-MD5": "GZdTUOhYHvHgQgmaw2gl4w==",
            "Host": "10.0.2.251",
            "bucketName": "bucket",
            "key": "file-key"
        },
        "requestTTFBLatencyMillis": 77,
        "responseElements": {
            "ETag": ""19975350e8581ef1e042099ac36825e3"",
            "Server": "AmazonS3",
            "x-amz-id-2": "uLdTfvdGTKlX6TBgCZtDd9Beef8wzUurA+Wpht7rKtfdaNsnxeLILg==",
            "x-amz-request-id": "140CD93455CB62B4"
        },
        "responseStatusCode": 200,
        "sourceIPAddress": "172.31.37.21",
        "userAgent": "aws-cli/1.27.23 Python/3.7.16 Linux/4.14.301-224.520.amzn2.x86_64 botocore/1.29.23",
        "userIdentity": {
            "identityType": "IAMUser",
            "principalId": "531520547609",
            "arn": "arn:aws:iam::531520547609:root",
            "userName": "root"
        }
    }
}

```

For more information about Amazon S3 event notifications, see [Amazon S3 Event
Notifications](../../../AmazonS3/latest/userguide/EventNotifications.md "../../../AmazonS3/latest/userguide/EventNotifications.md").
