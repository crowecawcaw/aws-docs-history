# Access logging

AWS Elemental MediaPackage v2 provides access logs that capture detailed information about requests sent to
your channels. MediaPackage generates two log types:

- Ingress access logs are for requests sent to the channel's input endpoints
- Egress access logs are for requests sent to the channel's endpoints or packaging
  group's assets
  Each log contains information such as the time the request was received, the client's IP
  address, latencies, request paths, and server responses. You can use these access logs to
  analyze service performance and troubleshoot issues. They can also help you learn about your
  customer base and understand your MediaPackage bill.

Access logging is an optional feature of MediaPackage that's disabled by default. After you
enable access logging, MediaPackage captures the logs and sends them to a destination. Amazon CloudWatch
vending log charges apply. For more information, see [CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs").

###### Topics

- [Permissions](#permissions "#permissions")
- [Enable access logging](#enable-access-logging "#enable-access-logging")
- [Manage and disable access logging](#disable-access-logging "#disable-access-logging")
- [Read access logs](#read-access-logs "#read-access-logs")

## Permissions

MediaPackage uses CloudWatch vended logs to deliver access logging. To deliver access logs, you
need permissions to the logging destination that you specify.

To see the required permissions for each logging destination, choose from the
following AWS services in the _Amazon CloudWatch Logs User
Guide_.

- [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs")
- [Amazon Simple Storage Service (Amazon S3)](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3")
- [Amazon Data Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose")

To create, view, or modify logging configuration in MediaPackage, you must have the required
permissions. Your IAM role must include the following minimum permissions to manage
access logging in the MediaPackage console.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ServiceLevelAccessForLogDelivery",
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "arn:aws:mediapackagev2:`us-east-1`:123456789012:channelGroup/*"
 }
 ]
}`

```

For more information about permissions to manage access logging, see [Enable logging
from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the _Amazon CloudWatch Logs User Guide_.

## Enable access logging

After you set up permissions to the logging destination, you can enable access logging
for MediaPackage.

For each log type, you can configure up to 3 log deliveries.

###### To enable access logs for an existing channel (console)

1.  Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2.  Select your channel group from the list of channel groups.
3.  Under **Access Logging**, do the following:
    1. For **Log deliveries – Egress Access Logs** or
       **Log deliveries – Ingress Access Logs**,
       choose **Add**, and then do the following:
    2. Choose one of the following logging destinations.
       - Amazon CloudWatch Logs
       - Amazon S3
       - Firehose

    ###### Tip

        * If you choose Amazon S3 or Firehose, you can deliver your logs to
         a **Cross account** or **In current
         account**.
        * To enable cross-account delivery, both AWS accounts must
         have the required permissions. For more information, see the
         [Cross-account delivery example](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example") in the
         *Amazon CloudWatch Logs User Guide*.

4.  For the **Delivery destination ARN**, choose or enter the
    ARN. If you don't have one already, follow the prompts to create one.
5.  For **Additional settings - _optional_**,
    choose the following:
    1. For **Field selection**, select the log fields to
       include in each log record.
    2. For **Output format**, choose the output format for
       the log.
    3. For **Field delimiter**, choose how to separate each
       log field.
    4. (Amazon S3) For **Suffix**, specify the suffix path to
       partition your data. You can use the following fields: {accountid},
       {region}, {channel_group_id}, {yyyy}, {MM}, {dd}, {HH}
    5. (Amazon S3) For **Hive-compatible**, choose
       **Enable** if you want to use Hive-compatible S3
       paths.

6.  To apply your changes to all log types, choose **Apply to all log
    types**.
7.  To create another log destination, repeat steps 3 – 5.
8.  Follow the prompts to update your channel group.

You can also use the CloudWatch API to enable access logs for your channel groups.

###### To enable access logs for an existing channel (API)

1. After you a create a channel group by using either the MediaPackage v2 API or the
   MediaPackage v2 console, get the Amazon Resource Name (ARN) of the channel group.

You can find the ARN from the **Channel groups** page in the
MediaPackage console or you can use the [GetChannel](../APIReference/API_GetChannel.md "../APIReference/API_GetChannel.md") API operation. A channel group ARN
follows this format:
`arn:aws:mediapackagev2:`region`:`123456789012`:`channelGroup`/`channelGroupName`` 2. Next, use the CloudWatch [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") API operation to create a delivery source for the
channel group.

    1. Pass the `resourceArn`.
    2. For `logType`, specify the type of logs that are collected:




    	* `EGRESS_ACCESS_LOGS` for requests sent to the endpoint or
    	 asset
    	* `INGRESS_ACCESS_LOGS` for requests sent to channel###### Example PutDeliverySource operation

```
{
    "logType": "EGRESS_ACCESS_LOGS",
    "name": "my-channel-group-source",
    "resourceArn": "arn:aws:mediapackagev2:`region`:`123456789012`:`channelGroup`/`channelGroupName`"
}
```

3. Use the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") API operation to
   configure where to store your logs. You can choose either CloudWatch Logs, Amazon S3, or Firehose
   as the destination. You must specify the ARN of one of the destination options
   for where your logs will be stored. You can choose the `outputFormat`
   of the logs to be one of the following: json, plain, w3c, raw, parquet.

The following is an example of configuring logs to store in an Amazon S3 bucket and
in JSON format.

```
{
   "deliveryDestinationConfiguration": {
      "destinationResourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket-name`"
   },
   "name": "string",
   "outputFormat": "json",
   "tags": {
      "key" : "value"
   }
}
```

###### Note

If you're delivering logs cross-account, you must use the
`PutDeliveryDestinationPolicy` API to assign an AWS Identity and Access Management
(IAM) policy to the destination account. The IAM policy allows delivery
from one account to another account. 4. Use the [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") API operation to link the
delivery source to the destination that you created in the previous steps. This
API operation associates the delivery source with the end destination.

```
{
   "deliveryDestinationArn": "string",
   "deliverySourceName": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Manage and disable access logging

Follow these procedures to manage or disable access logging for MediaPackage.

###### To manage access logging for a channel

(console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Select your channel group from the list of channel groups.
3. In the **Access Logging** section, select the destination and
   choose **Edit**.
4. Modify the log configuration as needed and then choose **Update**.

###### Note

You can't modify the logging destination. If you need to change the
logging destination, delete the current configuration and create a new
logging destination.

You can disable access logs for your MediaPackage channel at any
time.

###### To disable access logging for a channel

(console)

1. Open the MediaPackage console at [https://console.aws.amazon.com/mediapackage/](https://console.aws.amazon.com/mediapackage/ "https://console.aws.amazon.com/mediapackage/").
2. Select your channel group from the list of channel groups.
3. In the **Access Logging** section, select the destination to
   disable and choose **Remove**.
4. Review your changes and then choose **Delete**.

## Read access logs

MediaPackage v2 uses ingestion hub to deliver your access logs.

If you're using CloudWatch Logs as the destination, you can use CloudWatch Logs Insights to read the
access logs. Typical CloudWatch Logs charges apply. For more information, see [Analyzing Log Data with CloudWatch Logs Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") in the _AWS CloudWatch Logs
User Guide_.

###### Note

Access logs can take a few minutes to appear in your destination. If you don't see
the logs, wait a few minutes and try again.

### Access log format

The access log files consist of a sequence of formatted log records, where each
log record represents one request. The order of the fields within the log can vary.

###### Example: Ingress access log

```
{
    "event_timestamp": "2020-07-13T18:59:56.293656Z",
    "resource_arn": "arn:aws:mediapackagev2:us-east-1:007862077394:123456789012/my_channel_group",
    "client_ip": "192.0.2.0/24",
    "time_to_first_byte": 0.445,
    "status_code": "200",
    "received_bytes": 468,
    "sent_bytes": 2587370,
    "method": "GET",
    "request": "https://aabbcc-1.ingest.eeffgg.mediapackagev2.us-east-1.amazonaws.com:443/in/v1/my_channel_group/1/my_channel/manifest.m3u8",
    "protocol": "HTTP/1.1",
    "user_agent": "sabr/3.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Safari/528.17",
    "account": "123456789012",
    "channel_id": "my_channel",
    "channel_arn": "arn:aws:mediapackage:us-west-2:111122223333:channels/ExampleChannelID",
    "domain_name": "aaabbbcccdddee.mediapackage.us-east-1.amazonaws.com",
    "request_id": "aaaAAA111bbbBBB222cccCCC333dddDDD",
    "channel_group_id": "my_channel_group",
    "input_type": "HLS",
    "input_index": "1"
}
```

###### Example: Egress access log

```
{
    "event_timestamp": "2020-07-13T18:59:56.293656Z",
    "resource_arn": "arn:aws:mediapackagev2:us-east-1:007862077394:123456789012/my_channel_group",
    "client_ip": "192.0.2.0/24",
    "time_to_first_byte": 0.445,
    "status_code": "200",
    "received_bytes": 468,
    "sent_bytes": 2587370,
    "method": "GET",
    "request": "https://aabbcc.egress.eeffgg.mediapackagev2.us-east-1.amazonaws.com:443/out/v1/my_channel_group/my_channel/my_endpoint/index.mpd?param1=value1&param2=value2",
    "request_query_params": "param1=value1&param2=value2",
    "protocol": "HTTP/1.1",
    "user_agent": "sabr/3.0 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Safari/528.17",
    "account": "111122223333",
    "channel_id": "my_channel",
    "channel_arn": "arn:aws:mediapackage:us-west-2:123456789012:channels/ExampleChannelID",
    "domain_name": "aaabbbcccdddee.mediapackage.us-east-1.amazonaws.com",
    "request_id": "aaaAAA111bbbBBB222cccCCC333dddDDD",
    "endpoint_id": "my_endpoint",
    "endpoint_arn": "arn:aws:mediapackage:us-west-2:123456789012:origin_endpoints/ExampleEndpointID",
    "channel_group_id": "my_channel_group",
    "manifest_name": "index",
    "manifest_type": "DASH"
}
```

The following list describes the log record fields, in order:

**event_timestamp**

The time of day when the request was received. The value is
`ISO-8601` date time and is based on the system clock of
the host that served the request.

**resource_arn**

The Amazon Resource Name (ARN) of the channel group that received the
request.

**client_ip**

The IP address of the requesting client.

**time_to_first_byte**

The number of seconds that MediaPackage spent processing your request. This
value is measured from the time the last byte of your request was
received until the time the first byte of the response was sent.

**status_code**

The numeric HTTP status code of the response.

**received_bytes**

The number of bytes in the request body that the MediaPackage server
receives.

**sent_bytes**

The number of bytes in the response body that the MediaPackage server sends.
This value often is the same as the value of the
`Content-Length` header that's included with server
responses.

**method**

The HTTP request method that was used for the request: DELETE, GET,
HEAD, OPTIONS, PATCH, POST, or PUT.

**request**

The request URL.

**protocol**

The type of protocol used for the request, such as HTTP.

**user_agent**

A user-agent string that identifies the client that originated the
request, enclosed in double quotes. The string consists of one or more
product identifiers, product/version. If the string is longer than 8 KB,
it is truncated.

**account**

The AWS account ID of the account that was used to make the
request.

**channel_id**

The ID of the channel that received the request.

**channel_arn**

The Amazon Resource Name (ARN) of the channel that received the
request.

**domain_name**

The server name indication domain provided by the client during the
TLS handshake, enclosed in double quotes. This value is set to
`-` if the client doesn't support SNI or the domain
doesn't match a certificate and the default certificate is presented to
the client.

**request_id**

A string that's generated by MediaPackage to uniquely identify each
request.

**endpoint_id**

The ID of the endpoint that received the request.

**endpoint_arn**

The Amazon Resource Name (ARN) of the endpoint that received the
request.

**input_type**

The ingest file formats and protocol.

**input_index**

The input source index.

**manifest_name**

The name of the egress request manifest request. Remains empty for
segment egress request.

**manifest_type**

The type of the egress request manifest request. Remains empty for
segment egress request.

**request_query_params**

The manifest filtering query parameter names and values.

### Examples

The following are queries that you can use to read MediaPackage debug log data.

###### Example View the HTTP status code responses for a channel

Use this query to view the responses by HTTP status code for a channel. You
can use this to view HTTP error code responses to help you to troubleshoot
issues.

````
fields @timestamp, @message
| filter `channelId` like `my-channel`
| stats count() by statusCode ``` ###### Example Get the number of requests per endpoint on a channel ``` fields @timestamp, @message
| filter `channelId` like `my-channel`
| stats count() by `endpointId` ```
````
