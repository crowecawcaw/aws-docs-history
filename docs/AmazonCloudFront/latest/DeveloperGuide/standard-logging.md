# Configure standard logging (v2)

You can enable access logs (standard logs) when you create or update a distribution. Standard logging
(v2) includes the following features:

- Send access logs to Amazon CloudWatch Logs, Amazon Data Firehose, and Amazon Simple Storage Service (Amazon S3).
- Select the log fields that you want. You can also select a [subset of real-time access log
  fields](#standard-logging-real-time-log-selection "#standard-logging-real-time-log-selection").
- Select additional [output log file](#supported-log-file-format "#supported-log-file-format") formats.
  If you’re using Amazon S3, you have the following optional features:

- Send logs to opt-in AWS Regions.
- Organize your logs with partitioning.
- Enable Hive-compatible file names.
  For more information, see [Send logs to Amazon S3](#send-logs-s3 "#send-logs-s3").

To get started with standard logging, complete the following steps:

1. Set up your required permissions for the specified AWS service that will receive
   your logs.
2. Configure standard logging from the CloudFront console or the CloudWatch API.
3. View your access logs.

###### Note

- If you enable standard logging (v2), this doesn’t affect or change standard logging (legacy). You can
  continue to use standard logging (legacy) for your distribution, in addition to using
  standard logging (v2). For more information, see [Configure standard logging (legacy)](standard-logging-legacy-s3.md "standard-logging-legacy-s3.md").
- If you already enabled standard logging (legacy) and you want to enable standard logging (v2) to Amazon S3,
  we recommend that you specify a _different_ Amazon S3 bucket or
  use a _separate path_ in the same bucket (for
  example, use a log prefix or partitioning). This helps you keep track of which
  log files are associated with which distribution and prevents log files from
  overwriting each other.

## Permissions

CloudFront uses CloudWatch vended logs to deliver access logs. To do so, you need permissions to
the specified AWS service so that you can enable logging delivery.

To see the required permissions for each logging destination, choose from the
following topics in the _Amazon CloudWatch Logs User Guide_.

- [CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs")
- [Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose")
- [Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3")

After you have set up permissions to your logging destination, you can enable standard
logging for your distribution.

###### Note

CloudFront supports sending access logs to different AWS accounts (cross accounts). To
enable cross-account delivery, both accounts (your account and the receiving
account) must have the required permissions. For more information, see the [Enable standard logging for cross-account delivery](#enable-standard-logging-cross-accounts "#enable-standard-logging-cross-accounts") section or the [Cross-account delivery example](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#vended-logs-crossaccount-example") in the _Amazon CloudWatch Logs User
Guide_.

## Enable standard logging

To enable standard logging, you can use the CloudFront console or the CloudWatch API.

###### Contents

- [Enable standard logging (CloudFront console)](standard-logging.md#access-logging-console "standard-logging.md#access-logging-console")
- [Enable standard logging (CloudWatch API)](standard-logging.md#enable-access-logging-api "standard-logging.md#enable-access-logging-api")

### Enable standard logging (CloudFront console)

###### To enable standard logging for a CloudFront distribution (console)

1. Use the CloudFront console to
   [update an existing
   distribution](HowToUpdateDistribution.md#HowToUpdateDistributionProcedure "HowToUpdateDistribution.md#HowToUpdateDistributionProcedure").
2. Choose the **Logging** tab.
3. Choose **Add**, then select the service to
   receive your logs:
   - CloudWatch Logs
   - Firehose
   - Amazon S3

4. For the **Destination**, select the resource for your
   service. If you haven’t already created your resource, you can choose
   **Create** or see the following documentation.
   - For CloudWatch Logs, enter the **[Log group name](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md")**.
   - For Firehose, enter the **[Firehose delivery
     stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md")**.
   - For Amazon S3, enter the **[Bucket name](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md")**.

   ###### Tip

   To specify a prefix, enter the prefix after the bucket name,
   such as
   `amzn-s3-demo-bucket.s3.amazonaws.com/`MyLogPrefix``.
   If you don't specify a prefix, CloudFront will automatically add one
   for you. For more information, see [Send logs to Amazon S3](#send-logs-s3 "#send-logs-s3").

5. For **Additional settings –
   _optional_**, you can specify the following
   options:
   1. For **Field selection**, select the log field
      names that you want to deliver to your destination. You can select
      [access log
      fields](standard-logs-reference.md#BasicDistributionFileFormat "standard-logs-reference.md#BasicDistributionFileFormat") and a subset of [real-time access log
      fields](#standard-logging-real-time-log-selection "#standard-logging-real-time-log-selection").
   2. (Amazon S3 only) For **Partitioning**, specify the
      path to partition your log file data.
   3. (Amazon S3 only) For **Hive-compatible file format**,
      you can select the checkbox to use Hive-compatible S3 paths. This
      helps simplify loading new data into your Hive-compatible
      tools.
   4. For **Output format**, specify your preferred
      format.

   ###### Note

   If you choose **Parquet**, this option incurs
   CloudWatch charges for converting your access logs to Apache Parquet.
   For more information, see the [Vended Logs section for CloudWatch
   pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). 5. For **Field delimiter**, specify how to separate
   log fields.

6. Complete the steps to update or create your distribution.
7. To add another destination, repeat steps 3–6.
8. From the **Logs** page, verify that the standard logs
   status is **Enabled** next to the distribution.
9. (Optional) To enable cookie logging, choose **Manage**, **Settings** and turn on **Cookie logging**, then choose **Save changes**.

###### Tip

Cookie logging is a global setting that applies to _all_ standard logging for your distribution. You can’t override this setting for separate delivery destinations.

For more information about the standard logging delivery and log fields,
see the [Standard logging reference](standard-logs-reference.md "standard-logs-reference.md").

### Enable standard logging (CloudWatch API)

You can also use the CloudWatch API to enable standard logging for your distributions.

###### Notes

- When calling the CloudWatch API to enable standard logging, you must specify
  the US East (N. Virginia) Region (`us-east-1`), even if you want to enable
  cross Region delivery to another destination. For example, if you want
  to send your access logs to an S3 bucket in the Europe (Ireland) Region
  (`eu-west-1`), use the CloudWatch API in the
  `us-east-1` Region.
- There is an additional option to include cookies in standard logging.
  In the CloudFront API, this is the `IncludeCookies` parameter. If
  you configure access logging by using the CloudWatch API and you specify that
  you want to include cookies, you must use the CloudFront console or CloudFront API
  to update your distribution to include cookies. Otherwise, CloudFront can’t
  send cookies to your log destination. For more information, see [Cookie logging](DownloadDistValuesGeneral.md#DownloadDistValuesCookieLogging "DownloadDistValuesGeneral.md#DownloadDistValuesCookieLogging").

###### To enable standard logging for a distribution (CloudWatch API)

1. After you a create a distribution, get the Amazon Resource Name (ARN).

You can find the ARN from the **Distribution** page in
the CloudFront console or you can use the [GetDistribution](../../../cloudfront/latest/APIReference/API_GetDistribution.md "../../../cloudfront/latest/APIReference/API_GetDistribution.md") API operation. A
distribution ARN follows the format:
`arn:aws:cloudfront::123456789012:distribution/d111111abcdef8` 2. Next, use the CloudWatch [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") API operation to create a delivery source for
the distribution.

    1. Enter a name for the delivery source.
    2. Pass the `resourceArn` of the distribution.
    3. For `logType`, specify `ACCESS_LOGS` as the
     type of logs that are collected.
    4. ###### Example AWS CLI put-delivery-source command

    The following is an example of configuring a delivery source
     for a distribution.


    ```
    aws logs put-delivery-source --name S3-delivery --resource-arn arn:aws:cloudfront::123456789012:distribution/d111111abcdef8 --log-type ACCESS_LOGS
    ```
    **Output**


    ```
    {
     "deliverySource": {
     "name": "S3-delivery",
     "arn": "arn:aws:logs:us-east-1:123456789012:delivery-source:S3-delivery",
     "resourceArns": [
     "arn:aws:cloudfront::123456789012:distribution/d111111abcdef8"
     ],
     "service": "cloudfront",
     "logType": "ACCESS_LOGS"
     }
    }
    ```

3. Use the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") API operation to
   configure where to store your logs.
   1. For `destinationResourceArn`, specify the ARN of the
      destination. This can be a CloudWatch Logs log group, a Firehose delivery stream,
      or an Amazon S3 bucket.
   2. For `outputFormat`, specify the output format for your
      logs.
   3. ###### Example AWS CLI put-delivery-destination command

   The following is an example of configuring a delivery
   destination to an Amazon S3 bucket.

   ```
   aws logs put-delivery-destination --name S3-destination --delivery-destination-configuration destinationResourceArn=arn:aws:s3:::amzn-s3-demo-bucket
   ```

   **Output**

   ````
   {
       "name": "S3-destination",
       "arn": "arn:aws:logs:us-east-1:123456789012:delivery-destination:S3-destination",
       "deliveryDestinationType": "S3",
       "deliveryDestinationConfiguration": {
           "destinationResourceArn": "arn:aws:s3:::amzn-s3-demo-bucket"
       }
   }
   ```###### Note
   ````

If you're delivering logs cross-account, you must use the [PutDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md") API operation to assign an
AWS Identity and Access Management (IAM) policy to the destination account. The IAM policy
allows delivery from one account to another account. 4. Use the [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") API operation to link the
delivery source to the destination that you created in the previous steps.
This API operation associates the delivery source with the end
destination.

    1. For `deliverySourceName`, specify the source
     name.
    2. For `deliveryDestinationArn`, specify the ARN for the
     delivery destination.
    3. For `fieldDelimiter`, specify the string to separate
     each log field.
    4. For `recordFields`, specify the log fields that you
     want.
    5. If you’re using S3, specify whether to use
     `enableHiveCompatiblePath` and
     `suffixPath`.###### Example AWS CLI create-delivery command

The following is an example of creating a delivery.

```
aws logs create-delivery --delivery-source-name cf-delivery --delivery-destination-arn arn:aws:logs:us-east-1:123456789012:delivery-destination:S3-destination
```

**Output**

```
{
    "id": "abcNegnBoTR123",
    "arn": "arn:aws:logs:us-east-1:123456789012:delivery:abcNegnBoTR123",
    "deliverySourceName": "cf-delivery",
    "deliveryDestinationArn": "arn:aws:logs:us-east-1:123456789012:delivery-destination:S3-destination",
    "deliveryDestinationType": "S3",
    "recordFields": [
        "date",
        "time",
        "x-edge-location",
        "sc-bytes",
        "c-ip",
        "cs-method",
        "cs(Host)",
        "cs-uri-stem",
        "sc-status",
        "cs(Referer)",
        "cs(User-Agent)",
        "cs-uri-query",
        "cs(Cookie)",
        "x-edge-result-type",
        "x-edge-request-id",
        "x-host-header",
        "cs-protocol",
        "cs-bytes",
        "time-taken",
        "x-forwarded-for",
        "ssl-protocol",
        "ssl-cipher",
        "x-edge-response-result-type",
        "cs-protocol-version",
        "fle-status",
        "fle-encrypted-fields",
        "c-port",
        "time-to-first-byte",
        "x-edge-detailed-result-type",
        "sc-content-type",
        "sc-content-len",
        "sc-range-start",
        "sc-range-end",
        "c-country",
        "cache-behavior-path-pattern"
    ],
     "fieldDelimiter": ""
}
```

5. From the CloudFront console, on the **Logs** page, verify that
   the standard logs status is **Enabled** next to the
   distribution.

For more information about the standard logging delivery and log fields,
see the [Standard logging reference](standard-logs-reference.md "standard-logs-reference.md").

###### Note

To enable standard logging (v2) for CloudFront by using AWS CloudFormation, you can use the following CloudWatch Logs
properties:

- [Delivery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md")
- [DeliveryDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md")
- [DeliverySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md")
  The `ResourceArn` is the CloudFront distribution and `LogType` must be `ACCESS_LOGS` as the supported log type.

## Enable standard logging for cross-account delivery

If you enable standard logging for your AWS account and you want to deliver your
access logs to another account, make sure that you configure the source account and the
destination account correctly. The _source account_ with the CloudFront
distribution sends its access logs to the _destination
account_.

In this example procedure, the source account
`111111111111`) sends its access logs to an Amazon S3
bucket in the destination account (`222222222222`).
To send access logs to an Amazon S3 bucket in the destination account, use the AWS CLI.

### Configure the destination account

For destination account, complete the following procedure.

###### To configure the destination account

1. To create the log delivery destination, you can enter the following AWS CLI
   command. This example uses the
   `MyLogPrefix` string to create a
   prefix for your access logs.

```
aws logs put-delivery-destination --name `cloudfront-delivery-destination` --delivery-destination-configuration "destinationResourceArn=arn:aws:s3:::`amzn-s3-demo-bucket-cloudfront-logs`/`MyLogPrefix`"
```

**Output**

```
{
    "deliveryDestination": {
        "name": "cloudfront-delivery-destination",
        "arn": "arn:aws:logs:us-east-1:`222222222222`:delivery-destination:`cloudfront-delivery-destination`",
        "deliveryDestinationType": "S3",
        "deliveryDestinationConfiguration": {"destinationResourceArn": "arn:aws:s3:::`amzn-s3-demo-bucket-cloudfront-logs/`MyLogPrefix``"}
    }
}
```

###### Note

If you specify an S3 bucket _without_ a prefix,
CloudFront will automatically append the
`AWSLogs/`<account-ID>`/CloudFront`
as a prefix that appears in the `suffixPath` of the S3
delivery destination. For more information, see [S3DeliveryConfiguration](../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md"). 2. Add the resource policy for the log delivery destination to allow the
source account to create a log delivery.

In the following policy, replace
`111111111111` with the source
account ID and specify the delivery destination ARN from the output in step

1.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCreateDelivery",
 "Effect": "Allow",
 "Principal": {"AWS": "`111111111111`"},
 "Action": ["logs:CreateDelivery"],
 "Resource": "arn:aws:logs:us-east-1:`222222222222`:delivery-destination:`cloudfront-delivery-destination`"
 }
 ]
}`

```

3. Save the file, such as `deliverypolicy.json`.
4. To attach the previous policy to the delivery destination, enter the
   following AWS CLI command.

```
aws logs put-delivery-destination-policy --delivery-destination-name `cloudfront-delivery-destination` --delivery-destination-policy file://deliverypolicy.json
```

5. Add the below statement to the destination Amazon S3 bucket policy, replacing
   the resource ARN and the source account ID. This policy allows the
   `delivery.logs.amazonaws.com` service principal to perform
   the `s3:PutObject` action.

```
{
    "Sid": "AWSLogsDeliveryWrite",
    "Effect": "Allow",
    "Principal": {"Service": "delivery.logs.amazonaws.com"},
    "Action": "s3:PutObject",
    "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket-cloudfront-logs`/*",
    "Condition": {
        "StringEquals": {
            "s3:x-amz-acl": "bucket-owner-full-control",
            "aws:SourceAccount": "`111111111111`"
        },
        "ArnLike": {"aws:SourceArn": "arn:aws:logs:us-east-1:`111111111111`:delivery-source:*"}
    }
}
```

6. If you're using AWS KMS for your bucket, add the following statement to the
   KMS key policy to grant permissions to the
   `delivery.logs.amazonaws.com` service principal.

```
{
    "Sid": "Allow Logs Delivery to use the key",
    "Effect": "Allow",
    "Principal": {"Service": "delivery.logs.amazonaws.com"},
    "Action": [
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:ReEncrypt*",
        "kms:GenerateDataKey*",
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {"aws:SourceAccount": "`111111111111`"},
        "ArnLike": {"aws:SourceArn": "arn:aws:logs:us-east-1:`111111111111`:delivery-source:*"}
    }
}
```

### Configure the source account

After you configure the destination account, follow this procedure to create the
delivery source and enable logging for the distribution in the source
account.

###### To configure the source account

1. Create a delivery source for CloudFront standard logging so that you can send log
   files to CloudWatch Logs.

You can enter the following AWS CLI command, replacing the name and your
distribution ARN.

```
aws logs put-delivery-source --name `s3-cf-delivery` --resource-arn arn:aws:cloudfront::`111111111111`:distribution/`E1TR1RHV123ABC` --log-type ACCESS_LOGS
```

**Output**

```
{
    "deliverySource": {
        "name": "s3-cf-delivery",
        "arn": "arn:aws:logs:us-east-1:`111111111111`:delivery-source:`s3-cf-delivery`",
        "resourceArns": ["arn:aws:cloudfront::`111111111111`:distribution/`E1TR1RHV123ABC`"],
        "service": "cloudfront",
        "logType": "ACCESS_LOGS"
    }
}
```

2. Create a delivery to map the source account's log delivery source and the
   destination account's log delivery destination.

In the following AWS CLI command, specify the delivery destination ARN from the
output in [Step 1: Configure the
destination account](#steps-destination-account "#steps-destination-account").

```
aws logs create-delivery --delivery-source-name `s3-cf-delivery` --delivery-destination-arn arn:aws:logs:us-east-1:`222222222222`:delivery-destination:`cloudfront-delivery-destination`
```

**Output**

```
{
    "delivery": {
        "id": "OPmOpLahVzhx1234",
        "arn": "arn:aws:logs:us-east-1:111111111111:delivery:OPmOpLahVzhx1234",
        "deliverySourceName": "s3-cf-delivery",
        "deliveryDestinationArn": "arn:aws:logs:us-east-1:222222222222:delivery-destination:cloudfront-delivery-destination",
        "deliveryDestinationType": "S3",
        "recordFields": [
            "date",
            "time",
            "x-edge-location",
            "sc-bytes",
            "c-ip",
            "cs-method",
            "cs(Host)",
            "cs-uri-stem",
            "sc-status",
            "cs(Referer)",
            "cs(User-Agent)",
            "cs-uri-query",
            "cs(Cookie)",
            "x-edge-result-type",
            "x-edge-request-id",
            "x-host-header",
            "cs-protocol",
            "cs-bytes",
            "time-taken",
            "x-forwarded-for",
            "ssl-protocol",
            "ssl-cipher",
            "x-edge-response-result-type",
            "cs-protocol-version",
            "fle-status",
            "fle-encrypted-fields",
            "c-port",
            "time-to-first-byte",
            "x-edge-detailed-result-type",
            "sc-content-type",
            "sc-content-len",
            "sc-range-start",
            "sc-range-end",
            "c-country",
            "cache-behavior-path-pattern"
        ],
        "fieldDelimiter": "\t"
    }
}
```

3. Verify your cross-account delivery is successful.
   1. From the `source` account, sign in to the
      CloudFront console and choose your distribution. On the
      **Logging** tab, under **Type**,
      you will see an entry created for the S3 cross-account log
      delivery.
   2. From the `destination` account, sign in to
      the Amazon S3 console and choose your Amazon S3 bucket. You will see the prefix
      `MyLogPrefix` in the
      bucket name and any access logs delivered to that folder.

## Output file format

Depending on the delivery destination that you choose, you can specify one of the
following formats for log files:

- JSON
- Plain
- w3c
- Raw
- Parquet (Amazon S3 only)

###### Note

You can only set the output format when you first create the delivery destination.
This can't be updated later. To change the output format, delete the delivery and
create another one.

For more information, see [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") in the _Amazon CloudWatch Logs API
Reference_.

## Edit standard logging settings

You can enable or disable logging and update other log settings by using the [CloudFront console](https://console.aws.amazon.com/cloudfront/v4/home "https://console.aws.amazon.com/cloudfront/v4/home") or the CloudWatch API. Your
changes to logging settings take effect within 12 hours.

For more information, see the following topics:

- To update a distribution by using the CloudFront console, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md").
- To update a distribution by using the CloudFront API, see [UpdateDistribution](../../../cloudfront/latest/APIReference/API_UpdateDistribution.md "../../../cloudfront/latest/APIReference/API_UpdateDistribution.md") in the
  _Amazon CloudFront API Reference_.
- For more information about CloudWatch Logs API operations, see the [Amazon CloudWatch Logs API
  Reference](../../../AmazonCloudWatchLogs/latest/APIReference/Welcome.md "../../../AmazonCloudWatchLogs/latest/APIReference/Welcome.md").

## Access log fields

You can select the same log fields that standard logging (legacy) supports. For more information,
see [log file fields](standard-logs-reference.md#BasicDistributionFileFormat "standard-logs-reference.md#BasicDistributionFileFormat").

In addition, you can select the following [real-time access log fields](real-time-logs.md#understand-real-time-log-config "real-time-logs.md#understand-real-time-log-config").

1. `**timestamp(ms)**` – Timestamp in
   milliseconds.
2. `**origin-fbl**` – The number of seconds of
   first-byte latency between CloudFront and your origin.
3. `**origin-lbl**` – The number of seconds of
   last-byte latency between CloudFront and your origin.
4. `**asn**` – The autonomous system number
   (ASN) of the viewer.
5. `**c-country**` – A country code that represents the
   viewer's geographic location, as determined by the viewer's IP address. For a
   list of country codes, see [ISO 3166-1
   alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2 "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2").
6. `**cache-behavior-path-pattern**` – The path pattern that identifies the cache behavior that matched the viewer request.

## Send logs to CloudWatch Logs

To send logs to CloudWatch Logs, create or use an existing CloudWatch Logs log group. For more information
about configuring a CloudWatch Logs log group, see [Working with Log Groups and Log Streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

After you create your log group, you must have the required permissions to allow
standard logging. For more information about the required permissions, see [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs") in the _Amazon CloudWatch Logs User Guide_.

###### Notes

- When you specify the name of the CloudWatch Logs log group, only use the regex
  pattern `[\w-]`. For more information, see the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax") API operation in the
  _Amazon CloudWatch Logs API Reference_.
- Verify that your log group resource policy doesn't exceed the size limit.
  See the [Log group resource policy size limit considerations](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-CloudWatchLogs") section in
  the CloudWatch Logs topic.

### Example access log sent to CloudWatch Logs

```
{
"date": "2024-11-14",
"time": "21:34:06",
"x-edge-location": "SOF50-P2",
"asn": "16509",
"timestamp(ms)": "1731620046814",
"origin-fbl": "0.251",
"origin-lbl": "0.251",
"x-host-header": "d111111abcdef8.cloudfront.net",
"cs(Cookie)": "examplecookie=value"
}
```

## Send logs to Firehose

To send logs to Firehose, create or use an existing Firehose delivery stream. Then, specify
the Firehose delivery stream as the log delivery destination. You must specify a Firehose
delivery stream in the US East (N. Virginia) us-east-1 Region.

For information about creating your delivery stream, see [Creating an
Amazon Data Firehose delivery stream](../../../firehose/latest/dev/basic-create.md "../../../firehose/latest/dev/basic-create.md").

After you create your delivery stream, you must have the required permissions to allow
standard logging. For more information, see [Logs sent to Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-Firehose") in the _Amazon CloudWatch Logs User Guide_.

###### Note

When you specify the name of the Firehose stream, only use the regex pattern
`[\w-]`. For more information, see the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax") API operation in the
_Amazon CloudWatch Logs API Reference_.

### Example access log sent to Firehose

```
{"date":"2024-11-15","time":"19:45:51","x-edge-location":"SOF50-P2","asn":"16509","timestamp(ms)":"1731699951183","origin-fbl":"0.254","origin-lbl":"0.254","x-host-header":"d111111abcdef8.cloudfront.net","cs(Cookie)":"examplecookie=value"}
{"date":"2024-11-15","time":"19:45:52","x-edge-location":"SOF50-P2","asn":"16509","timestamp(ms)":"1731699952950","origin-fbl":"0.125","origin-lbl":"0.125","x-host-header":"d111111abcdef8.cloudfront.net","cs(Cookie)":"examplecookie=value"}
```

## Send logs to Amazon S3

To send your access logs to Amazon S3, create or use an existing S3 bucket. When you enable
logging in CloudFront, specify the bucket name. For information about creating a bucket, see
[Create a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md")
in the _Amazon Simple Storage Service User
Guide_.

After you create your bucket, you must have the required permissions to allow standard
logging. For more information, see [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3 "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-V2-S3") in the _Amazon CloudWatch Logs User Guide_.

- After you enable logging, AWS automatically adds the required bucket
  policies for you.
- You can also use S3 buckets in the [opt-in
  AWS Regions](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md").

###### Note

If you already enabled standard logging (legacy) and you want to enable standard logging (v2) to Amazon S3, we
recommend that you specify a _different_ Amazon S3 bucket or use a
_separate path_ in the same bucket (for
example, use a log prefix or partitioning). This helps you keep track of which log
files are associated with which distribution and prevents log files from overwriting
each other.

###### Topics

- [Specify an S3 bucket](#prefix-s3-buckets "#prefix-s3-buckets")
- [Partitioning](#partitioning "#partitioning")
- [Hive-compatible file name format](#hive-compatible-file-name-format "#hive-compatible-file-name-format")
- [Example paths to access logs](#bucket-path-examples "#bucket-path-examples")
- [Example access log sent to Amazon S3](#example-access-logs-s3 "#example-access-logs-s3")

### Specify an S3 bucket

When you specify an S3 bucket as the delivery destination, note the
following.

The S3 bucket name can only use the regex pattern `[\w-]`. For more
information, see the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md#API_PutDeliveryDestination_RequestSyntax") API operation in the
_Amazon CloudWatch Logs API Reference_.

If you specified a prefix for your S3 bucket, your logs appear under that path. If
you don't specify a prefix, CloudFront will automatically append the
`AWSLogs/`{account-id}`/CloudFront`
prefix for you.

For more information, see [Example paths to access logs](#bucket-path-examples "#bucket-path-examples").

### Partitioning

You can use partitioning to organize your access logs when CloudFront sends them to your
S3 bucket. This helps you organize and locate your access logs based on the path
that you want.

You can use the following variables to create a folder path.

- `{DistributionId}` or `{distributionid}`
- `{yyyy}`
- `{MM}`
- `{dd}`
- `{HH}`
- `{accountid}`

You can use any number of variables and specify folder names in your path. CloudFront
then uses this path to create a folder structure for you in the S3 bucket.

###### Examples

- ``my_distribution_log_data`/{DistributionId}/`logs``
- `/`cloudfront`/{DistributionId}/`my_distribution_log_data`/{yyyy}/{MM}/{dd}/{HH}/`logs``

###### Note

You can use either variable for distribution ID in the suffix path. However,
if you're sending access logs to AWS Glue, you must use the
`{distributionid}` variable because AWS Glue expects partition names
to be in lowercase. Update your existing log configuration in CloudFront to replace
`{DistributionId}` with `{distributionid}`.

### Hive-compatible file name format

You can use this option so that S3 objects that contain delivered access logs use
a prefix structure that allows for integration with Apache Hive. For more
information, see the [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") API operation.

###### Example

```
/`cloudfront`/DistributionId={DistributionId}/`my_distribution_log_data`/year={yyyy}/month={MM}/day={dd}/hour={HH}/`logs`
```

For more information about partitioning and the Hive-compatible options, see the
[S3DeliveryConfiguration](../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md") element in the
_Amazon CloudWatch Logs API Reference_.

### Example paths to access logs

When you specify an S3 bucket as the destination, you can use the following
options to create the path to your access logs:

- An Amazon S3 bucket, with or without a prefix
- Partitioning, by using a CloudFront provided variable or entering your
  own
- Enabling the Hive-compatible option

The following tables show how your access logs appear in your bucket, depending on
the options that you choose.

#### Amazon S3 bucket with a prefix

| Amazon S3 bucket name             | Partition that you specify in the suffix path | Updated suffix path | Hive-compatible enabled? | Access logs are sent to                               |
| --------------------------------- | --------------------------------------------- | ------------------- | ------------------------ | ----------------------------------------------------- |
| `amzn-s3-demo-bucket/MyLogPrefix` | None                                          | None                | No                       | `amzn-s3-demo-bucket/MyLogPrefix/`                    |
| `amzn-s3-demo-bucket/MyLogPrefix` | `myFolderA/`                                  | `myFolderA/`        | No                       | `amzn-s3-demo-bucket/MyLogPrefix/myFolderA/`          |
| `amzn-s3-demo-bucket/MyLogPrefix` | `myFolderA/{yyyy}`                            | `myFolderA/{yyyy}`  | Yes                      | `amzn-s3-demo-bucket/MyLogPrefix/myFolderA/year=2025` |

#### Amazon S3 bucket without a prefix

| Amazon S3 bucket name | Partition that you specify in the suffix path | Updated suffix path                                | Hive-compatible enabled? | Access logs are sent to                                                                         |
| --------------------- | --------------------------------------------- | -------------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------- |
| `amzn-s3-demo-bucket` | None                                          | `AWSLogs/{account-id}/CloudFront/`                 | No                       | `amzn-s3-demo-bucket/AWSLogs/`<your-account-ID>`/CloudFront/`                                   |
| `amzn-s3-demo-bucket` | `myFolderA/`                                  | `AWSLogs/{account-id}/CloudFront/myFolderA/`       | No                       | `amzn-s3-demo-bucket/AWSLogs/`<your-account-ID>`/CloudFront/myFolderA/`                         |
| `amzn-s3-demo-bucket` | `myFolderA/`                                  | `AWSLogs/{account-id}/CloudFront/myFolderA/`       | Yes                      | `amzn-s3-demo-bucket/AWSLogs/aws-account-id=`<your-account-ID>`/CloudFront/myFolderA/`          |
| `amzn-s3-demo-bucket` | `myFolderA/{yyyy}`                            | `AWSLogs/{account-id}/CloudFront/myFolderA/{yyyy}` | Yes                      | `amzn-s3-demo-bucket/AWSLogs/aws-account-id=`<your-account-ID>`/CloudFront/myFolderA/year=2025` |

#### AWS account ID as a partition

| Amazon S3 bucket name | Partition that you specify in the suffix path | Updated suffix path                                     | Hive-compatible enabled? | Access logs are sent to                                                                                             |
| --------------------- | --------------------------------------------- | ------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `amzn-s3-demo-bucket` | None                                          | `AWSLogs/{account-id}/CloudFront/`                      | Yes                      | `amzn-s3-demo-bucket/AWSLogs/aws-account-id=`<your-account-ID>`/CloudFront/`                                        |
| `amzn-s3-demo-bucket` | `myFolderA/{accountid}`                       | `AWSLogs/{account-id}/CloudFront/myFolderA/{accountid}` | Yes                      | `amzn-s3-demo-bucket/AWSLogs/aws-account-id=`<your-account-ID>`/CloudFront/myFolderA/accountid=`<your-account-ID>`` |

###### Notes

- The `{account-id}` variable is reserved for CloudFront. CloudFront
  automatically adds this variable to your suffix path if you specify an
  Amazon S3 bucket _without_ a prefix. If your logs are
  Hive-compatible, this variable appears as
  `aws-account-id`.
- You can use the `{accountid}` variable so that CloudFront adds
  your account ID to the suffix path. If your logs are Hive-compatible,
  this variable appears as `accountid`.
- For more information about the suffix path, see [S3DeliveryConfiguration](../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_S3DeliveryConfiguration.md").

### Example access log sent to Amazon S3

```
#Fields: date time x-edge-location asn timestamp(ms) x-host-header cs(Cookie)
2024-11-14    22:30:25    SOF50-P2    16509    1731623425421
d111111abcdef8.cloudfront.net    examplecookie=value2
```

## Disable standard logging

You can disable standard logging for your distribution if you no longer need
it.

###### To disable standard logging

1. Sign in to the CloudFront console.
2. Choose **Distribution** and then choose your distribution ID.
3. Choose **Logging** and then under **Access log
   destinations**, select the destination.
4. Choose **Manage** and then choose
   **Delete**.
5. Repeat the previous step if you have more than one standard logging.

###### Note

When you delete standard logging from the CloudFront console, this action only deletes
the delivery and the delivery destination. It doesn't delete the delivery source
from your AWS account. To delete a delivery source, specify the delivery source
name in the `aws logs delete-delivery-source --name DeliverySourceName`
command. For more information, see [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md") in the _Amazon CloudWatch Logs API
Reference_.

## Troubleshoot

Use the following information to fix common issues when you work with CloudFront
standard logging (v2).

### Delivery source already exists

When you enable standard logging for a distribution, you create a delivery source.
You then use that delivery source to create deliveries to destination type that you
want: CloudWatch Logs, Firehose, Amazon S3. Currently, you can only have one delivery source per
distribution. If you try to create another delivery source for the same
distribution, the following error message appears.

```
This ResourceId has already been used in another Delivery Source in this account
```

To create another delivery source, delete the existing one first. For more
information, see [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md") in the _Amazon CloudWatch Logs API
Reference_.

### I changed the suffix path and the Amazon S3 bucket can't receive my logs

If you enabled standard logging (v2) and specify a bucket ARN without a prefix, CloudFront will
append the following default to the suffix path:
`AWSLogs/{account-id}/CloudFront`. If you use the CloudFront console or the
[UpdateDeliveryConfiguration](../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.md") API operation to specify a different suffix
path, you must update the Amazon S3 bucket policy to use the same path.

###### Example: Updating the suffix path

1.  Your default suffix path is `AWSLogs/{account-id}/CloudFront` and
    you replace it with `myFolderA`.
2.  Because your new suffix path is different than the path specified in
    the Amazon S3 bucket policy, your access logs won't be delivered.
3.  You can do one of the following steps:

        * Update the Amazon S3 bucket permission from
         `amzn-s3-demo-bucket/AWSLogs/`<your-account-ID>`/CloudFront/*`
         to `amzn-s3-demo-bucket/myFolderA/*`.
        * Update your logging configuration to use the default suffix
         again: `AWSLogs/{account-id}/CloudFront`

    For more information, see [Permissions](#permissions-standard-logging "#permissions-standard-logging").

## Delete log files

CloudFront doesn't automatically delete log files from your destination. For information
about deleting log files, see the following topics:

###### Amazon S3

- [Deleting
  objects](../../../AmazonS3/latest/userguide/DeletingObjects.md "../../../AmazonS3/latest/userguide/DeletingObjects.md") in the _Amazon Simple Storage Service Console User
  Guide_

###### CloudWatch Logs

- [Working with log groups and log streams](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md") in the
  _Amazon CloudWatch Logs User Guide_
- [DeleteLogGroup](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteLogGroup.md") in the _Amazon CloudWatch Logs API Reference_

###### Firehose

- [DeleteDeliveryStream](../../../firehose/latest/APIReference/API_DeleteDeliveryStream.md "../../../firehose/latest/APIReference/API_DeleteDeliveryStream.md") in the _Amazon Data Firehose API
  Reference_

## Pricing

CloudFront doesn’t charge for enabling standard logs. However, you can incur charges for the
delivery, ingestion, storage or access, depending on the log delivery destination that
you select. For more information, see [Amazon CloudWatch Logs Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"). Under **Paid Tier**, choose the
**Logs** tab, and then under **Vended Logs**, see
the information for each delivery destination.

For more information about pricing for each AWS service, see the following
topics:

- [Amazon CloudWatch Logs
  Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
- [Amazon Data Firehose
  Pricing](https://aws.amazon.com/kinesis/data-firehose/pricing/ "https://aws.amazon.com/kinesis/data-firehose/pricing/")
- [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")

###### Note

There are no additional charges for log delivery to Amazon S3, though you incur
Amazon S3 charges for storing and accessing the log files. If you enable the
**Parquet** option to convert your access logs to
Apache Parquet, this option incurs CloudWatch charges. For more information, see
the [Vended Logs section
for CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
