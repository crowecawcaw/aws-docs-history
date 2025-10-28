# Create trails in additional accounts

You can use the console or the AWS CLI to create trails in additional AWS accounts and aggregate their log files to one Amazon S3 bucket.
Alternatively, you could create an organization trail to log all AWS accounts that
are part of an organization in AWS Organizations. For more information, see [Creating a trail for an organization](creating-trail-organization.md "creating-trail-organization.md").

## Using the console to create trails in additional AWS accounts

You can use the CloudTrail console to create trails in additional accounts.

1. Sign in to AWS Management Console with the account for which you want to create a trail. Follow the steps in [Creating a trail with the console](cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console "cloudtrail-create-a-trail-using-the-console-first-time.md#creating-a-trail-in-the-console") to create a trail using the console.
2. For **Storage location**, choose **Use existing S3 bucket**. Use the text box to enter the name of the bucket
   you're using to store log files across accounts.

###### Note

The bucket policy must grant CloudTrail permission to write to it. For information about
manually editing the bucket policy, see [Setting bucket policy for multiple accounts](cloudtrail-set-bucket-policy-for-multiple-accounts.md "cloudtrail-set-bucket-policy-for-multiple-accounts.md").

![Use existing S3 bucket](images/cloudtrail-use-existing-bucket.png) 3. For **Prefix**, enter the prefix you
are using to store log files across accounts. If you choose to use a prefix that is
different from what you specified in your bucket policy, you must edit the bucket policy on your destination bucket to allow CloudTrail to
write log files to your bucket using this new prefix.

## Using the CLI to create a trail in additional AWS accounts

You can use the AWS command line tools to create trails in additional accounts and
aggregate their log files to one Amazon S3 bucket. For more information about these tools,
see [cloudtrail](../../../cli/latest/reference/cloudtrail.md "../../../cli/latest/reference/cloudtrail.md") in the _AWS CLI Command Reference_.

Create a trail by using the **create-trail**
command, specifying the following:

- `--name` specifies the name of the trail.
- `--s3-bucket-name` specifies the Amazon S3 bucket you
  are using to store log files across accounts.
- `--s3-prefix` specifies a prefix for the log file delivery path
  (optional).
- `--is-multi-region-trail` specifies that this trail will log
  events in all AWS Regions in the partition in which you are working.

You can create one trail for each Region in which an
account is running AWS resources.

The following example command shows how to create a trail for your additional accounts
by using the AWS CLI. To have log files for these account delivered to the bucket you
created in your first account (111111111111 in this example), specify the
bucket name in the `--s3-bucket-name` option. Amazon S3 bucket names are globally
unique.

```
aws cloudtrail create-trail --name `my-trail` --s3-bucket-name `amzn-s3-demo-bucket` --is-multi-region-trail
```

When you run the command, you will see output similar to the following:

```
{
    "IncludeGlobalServiceEvents": true,
    "Name": "`AWSCloudTrailExample`",
    "TrailARN": "arn:aws:cloudtrail:`us-east-2`:`222222222222`:trail/`my-trail`",
    "LogFileValidationEnabled": false,
    **"IsMultiRegionTrail": true**,
    "IsOrganizationTrail": false,
    "S3BucketName": "`amzn-s3-demo-bucket`"
}
```

For more information about using CloudTrail from the AWS command line tools, see the
[CloudTrail command line
reference](../../../cli/latest/reference/cloudtrail/index.md "../../../cli/latest/reference/cloudtrail/index.md").
