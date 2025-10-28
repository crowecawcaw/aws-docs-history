# Lifecycle management in Security Lake

You can customize Security Lake to store data in your preferred AWS Regions for your
preferred amount of time. Lifecycle management can help you comply with different compliance
requirements.

## Retention management

To manage your data so that it is stored cost effectively, you can configure
retention for the data using the lifecycle settings in Security Lake. These retention settings help you
specify your preferred [Amazon S3 storage class](../../../AmazonS3/latest/userguide/storage-class-intro.md "../../../AmazonS3/latest/userguide/storage-class-intro.md")
and the time period for the Amazon S3 objects to stay
in that storage class before they transition to a different storage class to expire.

###### Warning

We recommend managing the retention settings
through Security Lake console, API, or CLI. This is because modifying Amazon S3
Lifecycle settings directly in the Amazon S3 service can potentially
delete metadata and prevent you from accessing your data.

### Important considerations for retention settings in Security Lake

Review the following considerations when managing data retention in Security Lake:

- Security Lake doesn't support [Amazon S3 Object Lock](../../../AmazonS3/latest/userguide/object-lock.md "../../../AmazonS3/latest/userguide/object-lock.md").
  When the data lake buckets are created, S3 Object Lock is disabled by
  default. Enabling S3 Object Lock with default retention mode interrupts the
  delivery of normalized log data to the data lake.
- The default Amazon S3 storage class is **S3 Standard**.
  If you don't configure retention settings,
  Security Lake uses the default settings for an
  Amazon S3 Lifecycle configuration — store
  the data indefinitely using the **S3 Standard** storage
  class.
- In Security Lake, you specify retention settings at the Region level. For example, you
  might configure all S3 objects in a specific AWS Region to transition
  to the **S3 Standard-IA** storage class
  30 days after they're written to the data lake.
- While retention settings are applied only to the data stored in the S3 bucket,
  Apache Iceberg metadata is excluded from the retention policy.

### Configuring retention settings when

enabling Security Lake

Follow these instructions to configure retention settings for one or more Regions
when you're onboarding to Security Lake.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. When you reach **Step 2: Define target
   objective** of the onboarding workflow, choose
   **Add transition** under **Select
   storage classes**. Then choose the Amazon S3 storage
   class that you want to transition S3 objects to. (The unlisted,
   default storage class is **S3 Standard**.) Also
   specify a retention period (in days) for that storage class. To
   transition objects to another storage class after that time,
   choose **Add transition** and enter the
   settings for the subsequent storage class and retention period.
3. To specify when you want S3 objects to expire, choose
   **Add transition**. Then, for storage
   class, choose **Expire**. For retention period,
   enter the total number of days that you want to store objects in
   Amazon S3, using any storage class, after objects are created. When
   this time period ends, objects expire and Amazon S3 deletes
   them.
4. When you finish, choose **Next**.

Your changes will apply to all the Regions that you enabled Security Lake
in during earlier onboarding steps.

API
To configure retention settings programmatically when you're
onboarding to Security Lake, use the [CreateDataLake](../APIReference/API_CreateDataLake.md "../APIReference/API_CreateDataLake.md") operation of the Security Lake API. If you're using the
AWS CLI, run the [create-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html") command.
Specify the retention settings you want in the `lifecycleConfiguration` parameters as follows:

- For `transitions`, specify the total number of days
  (`days`) that you want to store S3 objects in a
  particular Amazon S3 storage class
  (`storageClass`).
- For `expiration`, specify the total number of days
  that you want to store objects in Amazon S3, using any storage class,
  after objects are created. When this time period ends, objects
  expire and Amazon S3 deletes them.

Security Lake applies the settings to the Region that you specify in the
`region` field of the `configurations`
object.

For example, the following command enables Security Lake in the `us-east-1` Region. In this Region, objects expire after 365 days, and objects transition to the `ONEZONE_IA` S3 storage
class after 60 days. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake create-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"`S3_MANAGED_KEY`"},"region":"`us-east-1`","lifecycleConfiguration": {"expiration":{"days":`365`},"transitions":[{"days":`60`,"storageClass":"`ONEZONE_IA`"}]}}]' \
--meta-store-manager-role-arn "`arn:aws:securitylake:ap-northeast-2:123456789012:data-lake/default`"`
```

### Updating retention settings

Follow these instructions to update retention settings for one or more Regions
after enabling Security Lake.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, choose
   **Regions**
3. Select a Region, and then choose
   **Edit**.
4. In the **Select storage classes** section,
   enter the settings that you want. For storage class, choose the
   Amazon S3 storage class that you want to transition S3 objects to.
   (The unlisted, default storage class is **S3
   Standard**.) For retention period, enter the number
   of days that you want to store objects in that storage class.
   You can specify multiple transitions.

To also specify when you want S3 objects to expire, choose
**Expire** for storage class. Then, for
retention period, enter the total number of days that you want
to store objects in Amazon S3, using any storage class, after objects
are created. When this time period ends, objects expire and Amazon S3
deletes them. 5. When you finish, choose **Save**.

API
To update retention settings programmatically, use the [UpdateDataLake](../APIReference/API_UpdateDataLake.md "../APIReference/API_UpdateDataLake.md") operation of the Security Lake API. If you're using the AWS CLI, run the
[update-data-lake](../../../cli/latest/reference/securitylake/update-data-lake.md "../../../cli/latest/reference/securitylake/update-data-lake.md") command. In your
request, use the `lifecycleConfiguration` parameter to
specify the new settings:

- To change the transition settings, use the
  `transitions` parameters to specify each new time
  period in days (`days`) that you want to store S3
  objects in a particular Amazon S3 storage class
  (`storageClass`).
- To change the overall retention period, use the
  `expiration` parameter to specify the total
  number of days that you want to store S3 objects, using any
  storage class, after objects are created. When this retention
  period ends, objects expire and Amazon S3 deletes them.

Security Lake applies the settings to the Region that you specify in the
`region` field of the `configurations`
object.

The `UpdateDataLake` operation of the Security Lake API works as an "upsert"
operation that performs an insert if the specified item or record does
not exist, or an update if it already exists. Security Lake securely stores your
data at rest using AWS encryption solutions.

Omitting the key `encryptionConfiguration` from a Region
that is included in an update call that currently uses KMS will leave
that Region's KMS key in place, but specifying a key will reset the key
in the same region.

For example, the following AWS CLI command updates the data expiration settings and storage transition settings for the
`us-east-1` Region. In this Region, objects expire after 500 days, and objects transition to the `ONEZONE_IA` S3 storage
class after 30 days. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake update-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"`S3_MANAGED_KEY`"},"region":"`us-east-1`","lifecycleConfiguration": {"expiration":{"days":`500`},"transitions":[{"days":`30`,"storageClass":"`ONEZONE_IA`"}]}}]' \
--meta-store-manager-role-arn "`arn:aws:securitylake:ap-northeast-2:123456789012:data-lake/default`"`
```

## Rollup Regions

A rollup Region consolidates data from one or more contributing Regions. This can help
you comply with regional data compliance requirements.

For instructions on configuring rollup Regions, see [Configuring rollup Regions in Security Lake](add-rollup-region.md "add-rollup-region.md").
