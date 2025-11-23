# Logging configurable AD sync

errors

You can enable logging on your configurable Active Directory (AD) sync
configurations to receive logs with information about errors that can occur during the sync
process. With these logs, you can monitor if there is an issue with your
configurable AD sync and take action if applicable. You can send your logs to an Amazon CloudWatch Logs
log group, an Amazon Simple Storage Service (Amazon S3) bucket, or an Amazon Data Firehose with cross account delivery supported
for Amazon S3 buckets and Firehose.

For more information about limitations, permissions, and vended logs, see [Enabling logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md").

###### Note

You are charged for logging. For more information, see [Vended Logs](https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs "https://aws.amazon.com/cloudwatch/pricing/#Vended_Logs") on the
[Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
page.

## To enable configurable AD sync

error logs

1. Sign in to the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage logs**.
4. Choose **Add log delivery** and one of the following destination
   types.
   1. Choose **To Amazon CloudWatch Logs**. Then choose or enter the destination
      log group.
   2. Choose **To Amazon S3**. Then choose or enter the destination
      bucket.
   3. Choose **To Firehose**. Then choose or enter the destination
      delivery stream.

5. Choose **Submit**.

## To disable configurable AD

sync error logs

1. Sign in to the [IAM Identity Center
   console](https://console.aws.amazon.com/singlesignon/ "https://console.aws.amazon.com/singlesignon/").
2. Choose **Settings**.
3. On the **Settings** page, choose the **Identity
   source** tab, choose **Actions**, and then choose
   **Manage logs**.
4. Choose **Remove** for the destination that you want to remove.
5. Choose **Submit**.

## Configurable AD sync error log

fields

See the following list for possible error log fields.

`sync_profile_name`

The name of the sync profile.

`error_code`

The error code that represents what type of error has occurred.

`error_message`

A message that contains detailed information about the error that
occurred.

`sync_source`

The sync source is where entities are being synced from. For IAM Identity Center, this is an
Active Directory (AD) managed by Directory Service. The sync source contains the domain and ARN
of the directory affected.

`sync_target`

The sync target is the destination where entities are being saved. For IAM Identity Center,
this is an Identity Store. The sync target contains the Identity Store ARN
affected.

`source_entity_id`

A unique identifier for the entity that is causing the error. For IAM Identity Center, this is
the SID of the entity.

`source_entity_type`

The type of entity causing the error. The value can be `USER` or
`GROUP`.

`eventTimestamp`

The timestamp when the error occurred.

## Configurable AD sync error

log examples

**Example 1: An error log for an expired password for an AD
directory**

```
{
    "sync_profile_name": "EXAMPLE-PROFILE-NAME",
    "error" : {
        "error_code": "InvalidDirectoryCredentials",
        "error_message": "The password for your AD directory has expired. Please reset the password to allow Identity Sync to access the directory."
    },
    "sync_source": {
        "arn": "arn:aws:ds:us-east-1:123456789:directory/d-123456",
        "domain": "EXAMPLE.com"
    },
    "eventTimestamp": "1683355579981"
}
```

**Example 2: An error log for a user with a non-unique
username**

```
{
    "sync_profile_name": "EXAMPLE-PROFILE-NAME",
    "error" : {
        "error_code": "ConflictError",
        "error_message": "The source entity has a username conflict with the sync target. Please verify that the source identity has a unique username in the target."
    },
    "sync_source": {
        "arn": "arn:aws:ds:us-east-1:111122223333:directory/d-123456",
        "domain": "EXAMPLE.com"
    },
    "sync_target": {
        "arn": "arn:aws:identitystore::111122223333:identitystore/d-123456"
    },
    "source_entity_id": "SID-1234",
    "source_entity_type": "USER",
    "eventTimestamp": "1683355579981"
}
```
