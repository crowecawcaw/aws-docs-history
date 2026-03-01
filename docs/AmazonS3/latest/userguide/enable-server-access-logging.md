# Enabling Amazon S3 server access logging

Server access logging provides detailed records for the requests that are made to an Amazon S3
bucket. Server access logs are useful for many applications. For example, access log information
can be useful in security and access audits. This information can also help you learn about your
customer base and understand your Amazon S3 bill.

By default, Amazon S3 doesn't collect server access logs. When you enable logging, Amazon S3 delivers
access logs for a source bucket to a destination bucket (also known as a _target bucket_) that you choose. The destination bucket must be in the same
AWS Region and AWS account as the source bucket.

An access log record contains details about the requests that are made to a bucket. This
information can include the request type, the resources that are specified in the request, and
the time and date that the request was processed. For more information about logging basics, see
[Logging requests with server access logging](ServerLogs.md "ServerLogs.md").

###### Important

- There is no extra charge for enabling server access logging on an Amazon S3 bucket.
  However, any log files that the system delivers to you will accrue the usual charges for
  storage. (You can delete the log files at any time.) We do not assess data-transfer
  charges for log file delivery, but we do charge the normal data-transfer rate for
  accessing the log files.
- Your destination bucket should not have server access logging enabled. You can have
  logs delivered to any bucket that you own that is in the same Region as the source bucket,
  including the source bucket itself. However, delivering logs to the source bucket will
  cause an infinite loop of logs and is not recommended. For simpler log management, we
  recommend that you save access logs in a different bucket. For more information, see [How do I enable log delivery?](ServerLogs.md#server-access-logging-overview "ServerLogs.md#server-access-logging-overview")
- S3 buckets that have S3 Object Lock enabled can't be used as destination buckets for
  server access logs. Your destination bucket must not have a default retention period
  configuration.
- The destination bucket must not have Requester Pays enabled.
  You can enable or disable server access logging by using the Amazon S3 console, Amazon S3 API, the
  AWS Command Line Interface (AWS CLI), or AWS SDKs.

## Permissions for log delivery

Amazon S3 uses a special log delivery account to write server access logs. These writes are
subject to the usual access control restrictions. For access log delivery, you must grant the
logging service principal (`logging.s3.amazonaws.com`) access to your destination
bucket.

To grant permissions to Amazon S3 for log delivery, you can use either a bucket policy or
bucket access control lists (ACLs), depending on your destination bucket's
S3 Object Ownership settings. However, we recommend that you use a bucket policy instead of
ACLs.

###### Bucket owner enforced setting for S3 Object Ownership

If the destination bucket uses the Bucket owner enforced setting for Object Ownership,
ACLs are disabled and no longer affect permissions. In this case, you must update the bucket
policy for the destination bucket to grant access to the logging service principal. You
can't update your bucket ACL to grant access to the S3 log delivery group. You also can't
include destination grants (also known as _target grants_)
in your [PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md") configuration.

For information about migrating existing bucket ACLs for access log delivery to a bucket
policy, see [Grant access to the S3 log delivery group for server access logging](object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs "object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs"). For more information about
Object Ownership, see [Controlling ownership of objects and disabling ACLs for your bucket](about-object-ownership.md "about-object-ownership.md"). When you create new buckets, ACLs are disabled by
default.

###### Granting access by using a bucket policy

To grant access by using the bucket policy on the destination bucket, update the bucket
policy to grant the `s3:PutObject` permission to the logging service principal.
If you use the Amazon S3 console to enable server access logging, the console automatically
updates the bucket policy on the destination bucket to grant this permission to the logging
service principal. If you enable server access logging programmatically, you must manually
update the bucket policy for the destination bucket to grant access to the logging service
principal.

For an example bucket policy that grants access to the logging service principal, see
[Grant permissions to the logging service principal by using a bucket policy](#grant-log-delivery-permissions-bucket-policy "#grant-log-delivery-permissions-bucket-policy").

###### Granting access by using bucket ACLs

You can alternately use bucket ACLs to grant access for access log delivery. You add a
grant entry to the bucket ACL that grants `WRITE` and `READ_ACP`
permissions to the S3 log delivery group. However, granting access to the S3 log delivery
group by using bucket ACLs is not recommended. For more information, see [Controlling ownership of objects and disabling ACLs for your bucket](about-object-ownership.md "about-object-ownership.md"). For information
about migrating existing bucket ACLs for access log delivery to a bucket policy, see [Grant access to the S3 log delivery group for server access logging](object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs "object-ownership-migrating-acls-prerequisites.md#object-ownership-server-access-logs"). For an example ACL that grants
access to the logging service principal, see [Grant permissions to the log delivery group by using a bucket ACL](#grant-log-delivery-permissions-acl "#grant-log-delivery-permissions-acl").

### Grant permissions to the logging service principal by using a bucket policy

This example bucket policy grants the `s3:PutObject` permission to the
logging service principal (`logging.s3.amazonaws.com`). To use this bucket
policy, replace the `user input placeholders` with
your own information. In the following policy, `amzn-s3-demo-destination-bucket`
is the destination bucket where server access logs will be delivered, and
`amzn-s3-demo-source-bucket` is the source bucket.
`EXAMPLE-LOGGING-PREFIX` is the optional
destination prefix (also known as a _target prefix_) that
you want to use for your log objects.
`SOURCE-ACCOUNT-ID` is the AWS account that owns
the source bucket.

###### Note

If there are `Deny` statements in your bucket policy, make sure that they
don't prevent Amazon S3 from delivering access logs.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "S3ServerAccessLogsPolicy",
 "Effect": "Allow",
 "Principal": {
 "Service": "logging.s3.amazonaws.com"
 },
 "Action": [
 "s3:PutObject"
 ],
 "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket/`EXAMPLE-LOGGING-PREFIX`*",
 "Condition": {
 "ArnLike": {
 "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-source-bucket"
 },
 "StringEquals": {
 "aws:SourceAccount": "`SOURCE-ACCOUNT-ID`"
 }
 }
 }
 ]
}`

```

### Grant permissions to the log delivery group by using a bucket ACL

###### Note

As a security best practice, Amazon S3 disables access control lists (ACLs) by default in
all new buckets. For more information about ACL permissions in the Amazon S3 console, see [Configuring ACLs](managing-acls.md "managing-acls.md").

Although we do not recommend this approach, you can grant permissions to the log
delivery group by using a bucket ACL. However, if the destination bucket uses the Bucket
owner enforced setting for Object Ownership, you can't set bucket or object ACLs. You also
can't include destination grants (also known as _target
grants_) in your [PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md") configuration. Instead, you must use a bucket
policy to grant access to the logging service principal
(`logging.s3.amazonaws.com`). For more information, see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

In the bucket ACL, the log delivery group is represented by the following URL:

```
http://acs.amazonaws.com/groups/s3/LogDelivery
```

To grant `WRITE` and `READ_ACP` (ACL read) permissions, add the
following grants to the destination bucket ACL:

```
<Grant>
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:type="Group">
        <URI>http://acs.amazonaws.com/groups/s3/LogDelivery</URI>
    </Grantee>
    <Permission>WRITE</Permission>
</Grant>
<Grant>
    <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xsi:type="Group">
        <URI>http://acs.amazonaws.com/groups/s3/LogDelivery</URI>
    </Grantee>
    <Permission>READ_ACP</Permission>
</Grant>
```

For examples of adding ACL grants programmatically, see [Configuring ACLs](managing-acls.md "managing-acls.md").

###### Important

When you enable Amazon S3 server access logging by using AWS CloudFormation on a bucket and you're
using ACLs to grant access to the S3 log delivery group, you must also add
"`AccessControl": "LogDeliveryWrite"` to your CloudFormation template. Doing so
is important because you can grant those permissions only by creating an ACL for the
bucket, but you can't create custom ACLs for buckets in CloudFormation. You can use only
canned ACLs with CloudFormation.

## To enable server access logging

To enable server access logging by using the Amazon S3 console, Amazon S3 REST API, AWS SDKs, and
AWS CLI, use the following procedures.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **General purpose buckets**.
3. In the buckets list, choose the name of the bucket that you
   want to enable server access logging for.
4. Choose **Properties**.
5. In the **Server access logging** section, choose
   **Edit**.
6. Under **Server access logging**, choose
   **Enable**.
7. Under **Destination bucket**, specify a bucket and an optional
   prefix. If you specify a prefix, we recommend including a forward slash
   (`/`) after the prefix to make it easier to find your logs.

###### Note

Specifying a prefix with a slash (`/`) makes it simpler for you to
locate the log objects. For example, if you specify the prefix value
`logs/`, each log object that Amazon S3 creates begins with the
`logs/` prefix in its key, as follows:

```
logs/2013-11-01-21-32-16-E568B2907131C0C0
```

If you specify the prefix value `logs`, the log object appears as
follows:

```
logs2013-11-01-21-32-16-E568B2907131C0C0
```

8. Under **Log object key format**, do one of the following:
   - To choose non-date-based partitioning, choose
     **[DestinationPrefix][YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]**.
   - To choose date-based partitioning, choose
     **[DestinationPrefix][SourceAccountId]/[SourceRegion]/[SourceBucket]/[YYYY]/[MM]/[DD]/[YYYY]-[MM]-[DD]-[hh]-[mm]-[ss]-[UniqueString]**,
     then choose **S3 event time** or **Log file delivery
     time**.

9. Choose **Save changes**.

When you enable server access logging on a bucket, the console both enables
logging on the source bucket and updates the bucket policy for the destination bucket
to grant the `s3:PutObject` permission to the logging service principal
(`logging.s3.amazonaws.com`). For more information about this bucket
policy, see [Grant permissions to the logging service principal by using a bucket policy](#grant-log-delivery-permissions-bucket-policy "#grant-log-delivery-permissions-bucket-policy").

You can view the logs in the destination bucket.
After
you enable server access logging, it might take a few hours before the logs are
delivered to the target bucket. For more information about how and when logs are
delivered, see [How are logs delivered?](ServerLogs.md#how-logs-delivered "ServerLogs.md#how-logs-delivered")
For
more information, see [Viewing the properties for an S3 general purpose bucket](view-bucket-properties.md "view-bucket-properties.md").

To enable logging, you submit a [PutBucketLogging](../API/RESTBucketPUTlogging.md "../API/RESTBucketPUTlogging.md") request to add the logging configuration on
the source bucket. The request specifies the destination bucket (also known as a _target bucket_) and, optionally, the prefix to be used with all
log object keys.

The following example identifies `amzn-s3-demo-destination-bucket` as the
destination bucket and `logs/` as the prefix.

```
<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <LoggingEnabled>
    <TargetBucket>`amzn-s3-demo-destination-bucket`</TargetBucket>
    <TargetPrefix>`logs/`</TargetPrefix>
  </LoggingEnabled>
</BucketLoggingStatus>
```

The following example identifies `amzn-s3-demo-destination-bucket` as the
destination bucket, `logs/` as the prefix, and
`EventTime` as the log object key format.

```
<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
  <LoggingEnabled>
    <TargetBucket>`amzn-s3-demo-destination-bucket`</TargetBucket>
    <TargetPrefix>`logs/`</TargetPrefix>
    <TargetObjectKeyFormat>
      <PartitionedPrefix>
         <PartitionDateSource>EventTime</PartitionDateSource>
      </PartitionedPrefix>
  </TargetObjectKeyFormat>
  </LoggingEnabled>
</BucketLoggingStatus>
```

The log objects are written and owned by the S3 log delivery account, and the bucket
owner is granted full permissions on the log objects. You can optionally use destination
grants (also known as _target grants_) to grant
permissions to other users so that they can access the logs. For more information, see
[PutBucketLogging](../API/RESTBucketPUTlogging.md "../API/RESTBucketPUTlogging.md").

###### Note

If the destination bucket uses the Bucket owner enforced setting for
Object Ownership, you can't use destination grants to grant permissions to other users.
To grant permissions to others, you can update the bucket policy on the destination
bucket. For more information, see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

To retrieve the logging configuration on a bucket, use the [GetBucketLogging](../API/RESTBucketGETlogging.md "../API/RESTBucketGETlogging.md") API
operation.

To delete the logging configuration, you send a `PutBucketLogging` request
with an empty `BucketLoggingStatus`:

```
<BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01">
</BucketLoggingStatus>
```

To enable logging on a bucket, you can use either the Amazon S3 API or the AWS SDK
wrapper libraries.

The following
examples
enable logging on a bucket. You must create two buckets, a source bucket and a destination
(target) bucket.
The
examples update the bucket ACL on the destination bucket first. They then grant the log
delivery group the necessary permissions to write logs to the destination bucket, and then
they enable logging on the source bucket.

These examples won't work on destination buckets that use the Bucket owner enforced
setting for Object Ownership.

If the destination (target) bucket uses the Bucket owner enforced setting for Object Ownership, you can't set bucket or
object ACLs. You also can't include destination (target) grants in your
[PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md") configuration.
You must use a bucket policy to grant access to the logging service principal (`logging.s3.amazonaws.com`).
For more information, see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/S3#code-examples").

```
    using System;
    using System.IO;
    using System.Threading.Tasks;
    using Amazon.S3;
    using Amazon.S3.Model;
    using Microsoft.Extensions.Configuration;

    /// <summary>
    /// This example shows how to enable logging on an Amazon Simple Storage
    /// Service (Amazon S3) bucket. You need to have two Amazon S3 buckets for
    /// this example. The first is the bucket for which you wish to enable
    /// logging, and the second is the location where you want to store the
    /// logs.
    /// </summary>
    public class ServerAccessLogging
    {
        private static IConfiguration _configuration = null!;

        public static async Task Main()
        {
            LoadConfig();

            string bucketName = _configuration["BucketName"];
            string logBucketName = _configuration["LogBucketName"];
            string logObjectKeyPrefix = _configuration["LogObjectKeyPrefix"];
            string accountId = _configuration["AccountId"];

            // If the AWS Region defined for your default user is different
            // from the Region where your Amazon S3 bucket is located,
            // pass the Region name to the Amazon S3 client object's constructor.
            // For example: RegionEndpoint.USWest2 or RegionEndpoint.USEast2.
            IAmazonS3 client = new AmazonS3Client();

            try
            {
                // Update bucket policy for target bucket to allow delivery of logs to it.
                await SetBucketPolicyToAllowLogDelivery(
                    client,
                    bucketName,
                    logBucketName,
                    logObjectKeyPrefix,
                    accountId);

                // Enable logging on the source bucket.
                await EnableLoggingAsync(
                    client,
                    bucketName,
                    logBucketName,
                    logObjectKeyPrefix);
            }
            catch (AmazonS3Exception e)
            {
                Console.WriteLine($"Error: {e.Message}");
            }
        }

        /// <summary>
        /// This method grants appropriate permissions for logging to the
        /// Amazon S3 bucket where the logs will be stored.
        /// </summary>
        /// <param name="client">The initialized Amazon S3 client which will be used
        /// to apply the bucket policy.</param>
        /// <param name="sourceBucketName">The name of the source bucket.</param>
        /// <param name="logBucketName">The name of the bucket where logging
        /// information will be stored.</param>
        /// <param name="logPrefix">The logging prefix where the logs should be delivered.</param>
        /// <param name="accountId">The account id of the account where the source bucket exists.</param>
        /// <returns>Async task.</returns>
        public static async Task SetBucketPolicyToAllowLogDelivery(
            IAmazonS3 client,
            string sourceBucketName,
            string logBucketName,
            string logPrefix,
            string accountId)
        {
            var resourceArn = @"""arn:aws:s3:::" + logBucketName + "/" + logPrefix + @"*""";

            var newPolicy = @"{
                                ""Statement"":[{
                                ""Sid"": ""S3ServerAccessLogsPolicy"",
                                ""Effect"": ""Allow"",
                                ""Principal"": { ""Service"": ""logging.s3.amazonaws.com"" },
                                ""Action"": [""s3:PutObject""],
                                ""Resource"": [" + resourceArn + @"],
                                ""Condition"": {
                                ""ArnLike"": { ""aws:SourceArn"": ""arn:aws:s3:::" + sourceBucketName + @""" },
                                ""StringEquals"": { ""aws:SourceAccount"": """ + accountId + @""" }
                                        }
                                    }]
                                }";
            Console.WriteLine($"The policy to apply to bucket {logBucketName} to enable logging:");
            Console.WriteLine(newPolicy);

            PutBucketPolicyRequest putRequest = new PutBucketPolicyRequest
            {
                BucketName = logBucketName,
                Policy = newPolicy,
            };
            await client.PutBucketPolicyAsync(putRequest);
            Console.WriteLine("Policy applied.");
        }

        /// <summary>
        /// This method enables logging for an Amazon S3 bucket. Logs will be stored
        /// in the bucket you selected for logging. Selected prefix
        /// will be prepended to each log object.
        /// </summary>
        /// <param name="client">The initialized Amazon S3 client which will be used
        /// to configure and apply logging to the selected Amazon S3 bucket.</param>
        /// <param name="bucketName">The name of the Amazon S3 bucket for which you
        /// wish to enable logging.</param>
        /// <param name="logBucketName">The name of the Amazon S3 bucket where logging
        /// information will be stored.</param>
        /// <param name="logObjectKeyPrefix">The prefix to prepend to each
        /// object key.</param>
        /// <returns>Async task.</returns>
        public static async Task EnableLoggingAsync(
            IAmazonS3 client,
            string bucketName,
            string logBucketName,
            string logObjectKeyPrefix)
        {
            Console.WriteLine($"Enabling logging for bucket {bucketName}.");
            var loggingConfig = new S3BucketLoggingConfig
            {
                TargetBucketName = logBucketName,
                TargetPrefix = logObjectKeyPrefix,
            };

            var putBucketLoggingRequest = new PutBucketLoggingRequest
            {
                BucketName = bucketName,
                LoggingConfig = loggingConfig,
            };
            await client.PutBucketLoggingAsync(putBucketLoggingRequest);
            Console.WriteLine($"Logging enabled.");
        }

        /// <summary>
        /// Loads configuration from settings files.
        /// </summary>
        public static void LoadConfig()
        {
            _configuration = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("settings.json") // Load settings from .json file.
                .AddJsonFile("settings.local.json", true) // Optionally, load local settings.
                .Build();
        }
    }



```

- For API details, see
  [PutBucketLogging](../../../goto/DotNetSDKV3/s3-2006-03-01/PutBucketLogging.md "../../../goto/DotNetSDKV3/s3-2006-03-01/PutBucketLogging.md")
  in _AWS SDK for .NET API Reference_.

Java

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.BucketLoggingStatus;
import software.amazon.awssdk.services.s3.model.LoggingEnabled;
import software.amazon.awssdk.services.s3.model.PartitionedPrefix;
import software.amazon.awssdk.services.s3.model.PutBucketLoggingRequest;
import software.amazon.awssdk.services.s3.model.TargetObjectKeyFormat;

// Class to set a bucket policy on a target S3 bucket and enable server access logging on a source S3 bucket.
public class ServerAccessLogging {
    private static S3Client s3Client;

    public static void main(String[] args) {
        String sourceBucketName = "SOURCE-BUCKET";
        String targetBucketName = "TARGET-BUCKET";
        String sourceAccountId = "123456789012";
        String targetPrefix = "logs/";

        // Create S3 Client.
        s3Client = S3Client.builder().
                region(Region.US_EAST_2)
                .build();

        // Set a bucket policy on the target S3 bucket to enable server access logging by granting the
        // logging.s3.amazonaws.com principal permission to use the PutObject operation.
        ServerAccessLogging serverAccessLogging = new ServerAccessLogging();
        serverAccessLogging.setTargetBucketPolicy(sourceAccountId, sourceBucketName, targetBucketName);

        // Enable server access logging on the source S3 bucket.
        serverAccessLogging.enableServerAccessLogging(sourceBucketName, targetBucketName,
                targetPrefix);

    }

    // Function to set a bucket policy on the target S3 bucket to enable server access logging by granting the
    // logging.s3.amazonaws.com principal permission to use the PutObject operation.
    public void setTargetBucketPolicy(String sourceAccountId, String sourceBucketName, String targetBucketName) {
        String policy = "{\n" +
                "    \"Version\": \"2012-10-17\",\n" +
                "    \"Statement\": [\n" +
                "        {\n" +
                "            \"Sid\": \"S3ServerAccessLogsPolicy\",\n" +
                "            \"Effect\": \"Allow\",\n" +
                "            \"Principal\": {\"Service\": \"logging.s3.amazonaws.com\"},\n" +
                "            \"Action\": [\n" +
                "                \"s3:PutObject\"\n" +
                "            ],\n" +
                "            \"Resource\": \"arn:aws:s3:::" + targetBucketName + "/*\",\n" +
                "            \"Condition\": {\n" +
                "                \"ArnLike\": {\n" +
                "                    \"aws:SourceArn\": \"arn:aws:s3:::" + sourceBucketName + "\"\n" +
                "                },\n" +
                "                \"StringEquals\": {\n" +
                "                    \"aws:SourceAccount\": \"" + sourceAccountId + "\"\n" +
                "                }\n" +
                "            }\n" +
                "        }\n" +
                "    ]\n" +
                "}";
        s3Client.putBucketPolicy(b -> b.bucket(targetBucketName).policy(policy));
    }

    // Function to enable server access logging on the source S3 bucket.
    public void enableServerAccessLogging(String sourceBucketName, String targetBucketName,
            String targetPrefix) {
        TargetObjectKeyFormat targetObjectKeyFormat = TargetObjectKeyFormat.builder()
                .partitionedPrefix(PartitionedPrefix.builder().partitionDateSource("EventTime").build())
                .build();
        LoggingEnabled loggingEnabled = LoggingEnabled.builder()
                .targetBucket(targetBucketName)
                .targetPrefix(targetPrefix)
                .targetObjectKeyFormat(targetObjectKeyFormat)
                .build();
        BucketLoggingStatus bucketLoggingStatus = BucketLoggingStatus.builder()
                .loggingEnabled(loggingEnabled)
                .build();
        s3Client.putBucketLogging(PutBucketLoggingRequest.builder()
                .bucket(sourceBucketName)
                .bucketLoggingStatus(bucketLoggingStatus)
                .build());
    }

}
```

We recommend that you create a dedicated logging bucket in each AWS Region that you
have S3 buckets in. Then have your Amazon S3 access logs delivered to that S3 bucket. For more
information and examples, see [put-bucket-logging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-logging.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-logging.html") in the _AWS CLI
Reference_.

If the destination (target) bucket uses the Bucket owner enforced setting for Object Ownership, you can't set bucket or
object ACLs. You also can't include destination (target) grants in your
[PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md") configuration.
You must use a bucket policy to grant access to the logging service principal (`logging.s3.amazonaws.com`).
For more information, see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

###### Example— Enable access logs with five buckets across two Regions

In this example, you have the following five buckets:

- ``amzn-s3-demo-source-bucket`-us-east-1`
- ``amzn-s3-demo-source-bucket1`-us-east-1`
- ``amzn-s3-demo-source-bucket2`-us-east-1`
- ``amzn-s3-demo-bucket1`-us-west-2`
- ``amzn-s3-demo-bucket2`-us-west-2`

###### Note

The final step of the following procedure provides example bash scripts that you
can use to create your logging buckets and enable server access logging on these
buckets. To use those scripts, you must create the `policy.json`
and `logging.json` files, as described in the following
procedure.

1. Create two logging destination buckets in the US West (Oregon) and
   US East (N. Virginia) Regions and give them the following names:
   - ``amzn-s3-demo-destination-bucket`-logs-us-east-1`
   - ``amzn-s3-demo-destination-bucket1`-logs-us-west-2`

2. Later in these steps, you will enable server access logging as follows:
   - ``amzn-s3-demo-source-bucket`-us-east-1` logs to the S3 bucket
``amzn-s3-demo-destination-bucket`-logs-us-east-1` with the prefix
     ``amzn-s3-demo-source-bucket`-us-east-1`
   - ``amzn-s3-demo-source-bucket1`-us-east-1` logs to the S3
bucket ``amzn-s3-demo-destination-bucket`-logs-us-east-1` with the
     prefix ``amzn-s3-demo-source-bucket1`-us-east-1`
   - ``amzn-s3-demo-source-bucket2`-us-east-1` logs to the S3 bucket
``amzn-s3-demo-destination-bucket`-logs-us-east-1` with the prefix
     ``amzn-s3-demo-source-bucket2`-us-east-1`
   - ``amzn-s3-demo-bucket1`-us-west-2` logs to the S3 bucket
``amzn-s3-demo-destination-bucket1`-logs-us-west-2` with the prefix
     ``amzn-s3-demo-bucket1`-us-west-2`
   - ``amzn-s3-demo-bucket2`-us-west-2` logs to the S3
bucket ``amzn-s3-demo-destination-bucket1`-logs-us-west-2` with the
     prefix ``amzn-s3-demo-bucket2`-us-west-2`

3. For each destination logging bucket, grant permissions for server access log
   delivery by using a bucket ACL _or_ a bucket
   policy:
   - Update the bucket policy (Recommended)
     – To grant permissions to the logging service principal, use the
     following `put-bucket-policy` command. Replace
     ``amzn-s3-demo-destination-bucket`-logs`
     with the name of your destination bucket.

   ```
   aws s3api put-bucket-policy --bucket ``amzn-s3-demo-destination-bucket`-logs` --policy file://policy.json
   ```

   `Policy.json` is a JSON document in the current folder
   that contains the following bucket policy. To use this bucket policy, replace
   the `user input placeholders` with your
   own information. In the following policy,
   ```amzn-s3-demo-destination-bucket`-logs``
   is the destination bucket where server access logs will be delivered, and
   `amzn-s3-demo-source-bucket` is the source bucket.
   `SOURCE-ACCOUNT-ID` is the
   AWS account that owns the source bucket.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "S3ServerAccessLogsPolicy",
    "Effect": "Allow",
    "Principal": {
    "Service": "logging.s3.amazonaws.com"
    },
    "Action": [
    "s3:PutObject"
    ],
    "Resource": "arn:aws:s3:::amzn-s3-demo-destination-bucket`-logs`/*",
    "Condition": {
    "ArnLike": {
    "aws:SourceArn": "arn:aws:s3:::amzn-s3-demo-source-bucket"
    },
    "StringEquals": {
    "aws:SourceAccount": "`SOURCE-ACCOUNT-ID`"
    }
    }
    }
    ]
   }`

   ```

   - Update the bucket ACL – To grant
     permissions to the S3 log delivery group, use the following
     `put-bucket-acl` command. Replace
     ```amzn-s3-demo-destination-bucket`-logs``
     with the name of your destination (target) bucket.

   ```

   aws s3api put-bucket-acl --bucket ``amzn-s3-demo-destination-bucket`-logs`  --grant-write URI=http://acs.amazonaws.com/groups/s3/LogDelivery --grant-read-acp URI=http://acs.amazonaws.com/groups/s3/LogDelivery

   ```

4. Then, create a `logging.json` file that contains your logging
   configuration (based on one of the three examples that follow). After you create the
   `logging.json` file, you can apply the logging configuration by
   using the following `put-bucket-logging` command. Replace
   ```amzn-s3-demo-destination-bucket`-logs``
   with the name of your destination (target) bucket.

```

aws s3api put-bucket-logging --bucket ``amzn-s3-demo-destination-bucket`-logs` --bucket-logging-status file://logging.json

```

###### Note

Instead of using this `put-bucket-logging` command to apply the
logging configuration on each destination bucket, you can use one of the bash
scripts provided in the next step. To use those scripts, you must create the
`policy.json` and `logging.json` files, as
described in this procedure.

The `logging.json` file is a JSON document in the current
folder that contains your logging configuration. If a destination bucket uses the
Bucket owner enforced setting for Object Ownership, your logging configuration
can't contain destination (target) grants. For more information, see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

###### Example– `logging.json` without destination (target) grants

The following example `logging.json` file doesn't contain
destination (target) grants. Therefore, you can apply this configuration to a
destination (target) bucket that uses the Bucket owner enforced setting for
Object Ownership.

```

  {
      "LoggingEnabled": {
          "TargetBucket": "`amzn-s3-demo-destination-bucket``-logs`",
          "TargetPrefix": "`amzn-s3-demo-destination-bucket`/"
       }
   }

```

###### Example– `logging.json` with destination (target) grants

The following example `logging.json` file contains
destination (target) grants.

If the destination bucket uses the Bucket owner enforced setting for
Object Ownership, you can't include destination (target) grants in your [PutBucketLogging](../API/API_PutBucketLogging.md "../API/API_PutBucketLogging.md") configuration. For more information,
see [Permissions for log delivery](#grant-log-delivery-permissions-general "#grant-log-delivery-permissions-general").

```

  {
      "LoggingEnabled": {
          "TargetBucket": "`amzn-s3-demo-destination-bucket``-logs`",
          "TargetPrefix": "`amzn-s3-demo-destination-bucket`/",
          "TargetGrants": [
               {
                  "Grantee": {
                      "Type": "CanonicalUser",
                      "ID": "`79a59df900b949e55d96a1e698fbacedfd6e09d98eacf8f8d5218e7cd47ef2be`"
                   },
                  "Permission": "FULL_CONTROL"
               }
           ]
       }
   }

```

###### Grantee values

You can specify the person (grantee) to whom you're assigning access rights (by using
request elements) in the following ways:

    * By the person's ID:



    ```
    {
      "Grantee": {
        "Type": "CanonicalUser",
        "ID": "`ID`"
      }
    }
    ```
    * By URI:



    ```
    {
      "Grantee": {
        "Type": "Group",
        "URI": "`http://acs.amazonaws.com/groups/global/AuthenticatedUsers`"
      }
    }
    ```

###### Example– `logging.json` with the log object key format set to S3 event time

The following `logging.json` file changes the log object
key format to S3 event time. For more information about setting the log object key
format, see [How do I enable log delivery?](ServerLogs.md#server-access-logging-overview "ServerLogs.md#server-access-logging-overview")

```

  {
    "LoggingEnabled": {
        "TargetBucket": "`amzn-s3-demo-destination-bucket``-logs`",
        "TargetPrefix": "`amzn-s3-demo-destination-bucket`/",
        "TargetObjectKeyFormat": {
            "PartitionedPrefix": {
                "PartitionDateSource": "EventTime"
            }
         }
    }
}

```

5. Use one of the following bash scripts to add access logging for all the buckets
   in your account. Replace
   ```amzn-s3-demo-destination-bucket`-logs``
   with the name of your destination (target) bucket, and replace
   `us-west-2` with the name of the Region
   that
   your
   buckets are located in.

###### Note

This script works only if all of
your
buckets are in the same Region. If you have buckets in multiple
Regions, you must adjust the script.

###### Example– Grant access with bucket policies and add logging for the buckets in your account

```

  loggingBucket='`amzn-s3-demo-destination-bucket``-logs`'
  region='`us-west-2`'


  # Create the logging bucket.
  aws s3 mb s3://$loggingBucket --region $region

  aws s3api put-bucket-policy --bucket $loggingBucket --policy file://policy.json

  # List the buckets in this account.
  buckets="$(aws s3 ls | awk '{print $3}')"

  # Put a bucket logging configuration on each bucket.
  for bucket in $buckets
      do
        # This if statement excludes the logging bucket.
        if [ "$bucket" == "$loggingBucket" ] ; then
            continue;
        fi
        printf '{
          "LoggingEnabled": {
            "TargetBucket": "%s",
            "TargetPrefix": "%s/"
        }
      }' "$loggingBucket" "$bucket"  > logging.json
      aws s3api put-bucket-logging --bucket $bucket --bucket-logging-status file://logging.json
      echo "$bucket done"
  done

  rm logging.json

  echo "Complete"

```

###### Example– Grant access with bucket ACLs and add logging for the buckets in your account

```

  loggingBucket='`amzn-s3-demo-destination-bucket``-logs`'
  region='`us-west-2`'


  # Create the logging bucket.
  aws s3 mb s3://$loggingBucket --region $region

  aws s3api put-bucket-acl --bucket $loggingBucket --grant-write URI=http://acs.amazonaws.com/groups/s3/LogDelivery --grant-read-acp URI=http://acs.amazonaws.com/groups/s3/LogDelivery

  # List the buckets in this account.
  buckets="$(aws s3 ls | awk '{print $3}')"

  # Put a bucket logging configuration on each bucket.
  for bucket in $buckets
      do
        # This if statement excludes the logging bucket.
        if [ "$bucket" == "$loggingBucket" ] ; then
            continue;
        fi
        printf '{
          "LoggingEnabled": {
            "TargetBucket": "%s",
            "TargetPrefix": "%s/"
        }
      }' "$loggingBucket" "$bucket"  > logging.json
      aws s3api put-bucket-logging --bucket $bucket --bucket-logging-status file://logging.json
      echo "$bucket done"
  done

  rm logging.json

  echo "Complete"

```

## Verifying your server access logs setup

After you enable server access logging, complete the following steps:

- Access the destination bucket and verify that the log files are being delivered. After
  the access logs are set up, Amazon S3 immediately starts capturing requests and logging them.
  However, it might take a few hours before the logs are delivered to the destination
  bucket. For more information, see [Bucket logging status changes take effect over time](ServerLogs.md#BucketLoggingStatusChanges "ServerLogs.md#BucketLoggingStatusChanges") and [Best-effort server log delivery](ServerLogs.md#LogDeliveryBestEffort "ServerLogs.md#LogDeliveryBestEffort").

You can also automatically verify log delivery by using Amazon S3 request metrics and
setting up Amazon CloudWatch alarms for these metrics. For more information, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md").

- Verify that you are able to open and read the contents of the log files.

For server access logging troubleshooting information, see [Troubleshoot server access logging](troubleshooting-server-access-logging.md "troubleshooting-server-access-logging.md").
