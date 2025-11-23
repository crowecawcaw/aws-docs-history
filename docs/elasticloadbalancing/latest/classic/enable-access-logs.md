# Enable access logs for your Classic Load Balancer

To enable access logs for your load balancer, you must specify the name of the Amazon S3
bucket where the load balancer will store the logs. You must also attach a bucket policy
to this bucket that grants ELB permission to write to the bucket.

###### Tasks

- [Step 1: Create an S3 bucket](#create-s3-bucket "#create-s3-bucket")
- [Step 2: Attach a policy to your S3 bucket](#attach-bucket-policy "#attach-bucket-policy")
- [Step 3: Configure access logs](#configure-access-logs "#configure-access-logs")
- [Step 4: Verify bucket permissions](#verify-access-logs "#verify-access-logs")
- [Troubleshooting](#enable-access-logs-troubleshooting "#enable-access-logs-troubleshooting")

## Step 1: Create an S3 bucket

When you enable access logs, you must specify an S3 bucket for the access log files.
The bucket must meet the following requirements.

###### Requirements

- The bucket must be located in the same Region as the load balancer. The
  bucket and the load balancer can be owned by different accounts.
- The only server-side encryption option that's supported is Amazon S3-managed
  keys (SSE-S3). For more information, see [Amazon S3-managed encryption keys (SSE-S3)](../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md "../../../AmazonS3/latest/userguide/UsingServerSideEncryption.md").

###### To create an S3 bucket using the Amazon S3 console

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. On the **Create bucket** page, do the following:
   1. For **Bucket name**, enter a name for your bucket. This name must be
      unique across all existing bucket names in Amazon S3. In some
      Regions, there might be additional restrictions on bucket names.
      For more information, see [Bucket quotas,
      limitations, and restrictions](../../../AmazonS3/latest/userguide/BucketRestrictions.md "../../../AmazonS3/latest/userguide/BucketRestrictions.md") in the
      _Amazon S3 User Guide_.
   2. For **AWS Region**, select the Region where you created
      your load balancer.
   3. For **Default encryption**, choose **Amazon S3-managed keys (SSE-S3)**.
   4. Choose **Create bucket**.

## Step 2: Attach a policy to your S3 bucket

Your S3 bucket must have a bucket policy that grants ELB permission to write the access
logs to the bucket. Bucket policies are a collection of JSON statements written
in the access policy language to define access permissions for your bucket. Each
statement includes information about a single permission and contains a series
of elements.

If you're using an existing bucket that already has an attached policy, you can add the
statement for ELB access logs to the policy. If you do so, we recommend
that you evaluate the resulting set of permissions to ensure that they are
appropriate for the users that need access to the bucket for access logs.

This policy grants permissions to the log delivery service.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "logdelivery.elasticloadbalancing.amazonaws.com"
 },
 "Action": "s3:PutObject",
 "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/`prefix`/AWSLogs/`123456789012`/*"
 }
 ]
}`

```

For `Resource`, enter the ARN of the location for the access logs,
using the format shown in the example policy. Always include the account ID of
the account with the load balancer in the resource path of the S3 bucket ARN.
This ensures that only load balancers from the specified account can write
access logs to the S3 bucket.

The ARN that you specify depends on whether you plan to include a prefix when
you enable access logs in [step 3](enable-access-logs.md "enable-access-logs.md").

###### Example S3 bucket ARN with a prefix

The S3 bucket name is amzn-s3-demo-logging-bucket and the
prefix is logging-prefix.

```
arn:aws:s3:::amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/*
```

[AWS GovCloud (US)] The following example uses the ARN syntax for the AWS GovCloud (US) Regions.

```
arn:aws-us-gov:s3:::amzn-s3-demo-logging-bucket/logging-prefix/AWSLogs/123456789012/*
```

###### Example S3 bucket ARN with no prefix

The S3 bucket name is amzn-s3-demo-logging-bucket. There is
no prefix portion in the S3 bucket ARN.

```
arn:aws:s3:::amzn-s3-demo-logging-bucket/AWSLogs/123456789012/*
```

[AWS GovCloud (US)] The following example uses the ARN syntax for the AWS GovCloud (US) Regions.

```
arn:aws-us-gov:s3:::amzn-s3-demo-logging-bucket/AWSLogs/123456789012/*
```

Previously, for Regions available before August 2022, we required a policy
that granted permissions to an ELB account that was specific to the Region.
This legacy policy is still supported, but we recommend that you replace it
with the newer policy above. If you prefer to keep using the legacy bucket
policy, which is not shown here, you can.

For reference, here are the IDs of the ELB accounts to
specify in `Principal`. Note that Regions that are not in this list
never supported the legacy bucket policy.

- US East (N. Virginia) – 127311923021
- US East (Ohio) – 033677994240
- US West (N. California) – 027434742980
- US West (Oregon) – 797873946194
- Africa (Cape Town) – 098369216593
- Asia Pacific (Hong Kong) – 754344448648
- Asia Pacific (Jakarta) – 589379963580
- Asia Pacific (Mumbai) – 718504428378
- Asia Pacific (Osaka) – 383597477331
- Asia Pacific (Seoul) – 600734575887
- Asia Pacific (Singapore) – 114774131450
- Asia Pacific (Sydney) – 783225319266
- Asia Pacific (Tokyo) – 582318560864
- Canada (Central) – 985666609251
- Europe (Frankfurt) – 054676820928
- Europe (Ireland) – 156460612806
- Europe (London) – 652711504416
- Europe (Milan) – 635631232127
- Europe (Paris) – 009996457667
- Europe (Stockholm) – 897822967062
- Middle East (Bahrain) – 076674570225
- South America (São Paulo) – 507241528517
- AWS GovCloud (US-East) – 190560391635
- AWS GovCloud (US-West) – 048591011584
  To enhance security, use precise S3 bucket ARNs.

- Use the full resource path, not just the S3 bucket ARN.
- Include the account ID portion of the S3 bucket ARN.
- Don't use wildcards (\*) in the account ID portion of the S3 bucket ARN.

After you create your bucket policy, use an Amazon S3 interface, such as the Amazon S3 console
or AWS CLI commands, to attach your bucket policy to your S3 bucket.

###### To attach your bucket policy to your bucket using the console

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the name of the bucket to open its details page.
3. Choose **Permissions** and then choose **Bucket
   policy**, **Edit**.
4. Update the bucket policy to grant the required permissions.
5. Choose **Save changes**.

###### To attach your bucket policy to your S3 bucket using the AWS CLI

Use the [put-bucket-policy](../../../cli/latest/reference/s3api/put-bucket-policy.md "../../../cli/latest/reference/s3api/put-bucket-policy.md") command. In this example, the
bucket policy was saved to the specified .json file.

```
aws s3api put-bucket-policy \
    --bucket `amzn-s3-demo-bucket` \
    --policy file://`access-log-policy.json`
```

## Step 3: Configure access logs

Use the following procedure to configure access logs to capture request information
and deliver log files to your S3 bucket.

###### Requirements

The bucket must meet the requirements described in [step 1](#create-s3-bucket "#create-s3-bucket"), and you must attach a bucket
policy as described in [step 2](#attach-bucket-policy "#attach-bucket-policy").
If you specify a prefix, it must not include the string "AWSLogs".

###### To configure access logs for your load balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
3. Select the name of your load balancer to open its details page.
4. On the **Attributes** tab, choose **Edit**.
5. On the **Edit load balancer attributes** page, in the **Monitoring** section, do the following:
   1. Enable **Access logs**.
   2. For **S3 URI**, enter the S3 URI for your log files. The URI
      that you specify depends on whether you're using a prefix.
      - URI with a prefix: `s3://`amzn-s3-demo-logging-bucket`/`logging-prefix``
      - URI without a prefix: `s3://`amzn-s3-demo-logging-bucket``

   3. Keep **Logging interval** as `60 minutes - default`.
   4. Choose **Save changes**.

###### To configure access logs for your load balancer using the AWS CLI

First, create a .json file that enables ELB to capture and deliver logs every 60 minutes to the S3 bucket
that you created for the logs:

```
{
  "AccessLog": {
    "Enabled": true,
    "S3BucketName": "`amzn-s3-demo-logging-bucket`",
    "EmitInterval": 60,
    "S3BucketPrefix": "`my-app`"
  }
}
```

Next, specify the .json file in the [modify-load-balancer-attributes](../../../cli/latest/reference/elb/modify-load-balancer-attributes.md "../../../cli/latest/reference/elb/modify-load-balancer-attributes.md") command as follows:

```
aws elb modify-load-balancer-attributes --load-balancer-name `my-loadbalancer` --load-balancer-attributes file://`my-json-file`.json
```

The following is an example response.

```
{
    "LoadBalancerAttributes": {
        "AccessLog": {
            "Enabled": true,
            "EmitInterval": 60,
            "S3BucketName": "amzn-s3-demo-logging-bucket",
            "S3BucketPrefix": "my-app"
        }
    },
    "LoadBalancerName": "my-loadbalancer"
}
```

###### To manage the S3 bucket for your access logs

Be sure to disable access logs before you delete the bucket that you configured
for access logs. Otherwise, if there is a new bucket with the same name and the
required bucket policy created in an AWS account that you don't own, ELB
could write the access logs for your load balancer to this new bucket.

## Step 4: Verify bucket permissions

After access logs are enabled for your load balancer, ELB validates the S3 bucket and
creates a test file to ensure that the bucket policy specifies the required
permissions. You can use the S3 console to verify that the test file was created.
The test file is not an actual access log file; it doesn't contain example
records.

###### To verify that ELB created a test file in your S3 bucket

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Select the name of the S3 bucket that you specified for access logs.
3. Navigate to the test file, `ELBAccessLogTestFile`.
   The location depends on whether you're using a prefix.
   - Location with a prefix: `amzn-s3-demo-loadbalancer-logs`/`logging-prefix`/AWSLogs/`123456789012`/ELBAccessLogTestFile
   - Location without a prefix: `amzn-s3-demo-loadbalancer-logs`/AWSLogs/`123456789012`/ELBAccessLogTestFile

## Troubleshooting

###### Access Denied for bucket: `bucket-name`. Please check S3bucket permission

If you receive this error, the following are possible causes:

- The bucket policy does not grant ELB permission to write access logs to the bucket.
  Verify that you are using the correct bucket policy for the Region.
  Verify that the resource ARN uses the same bucket name that you
  specified when you enabled access logs. Verify that the resource ARN
  does not include a prefix if you did not specify a prefix when you
  enabled access logs.
- The bucket uses an unsupported server-side encryption option. The bucket must use Amazon S3-managed keys (SSE-S3).
