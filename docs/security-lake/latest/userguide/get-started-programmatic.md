# Enabling Security Lake programmatically

This tutorial explains how to enable and start using Security Lake programmatically. The Amazon Security Lake API gives you
comprehensive, programmatic access to your Security Lake account, data, and resources. Alternatively, you can use AWS command line tools—
the [AWS Command Line Interface](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") or the
[AWS Tools for PowerShell](../../../powershell/latest/userguide/pstools-welcome.md "../../../powershell/latest/userguide/pstools-welcome.md")—or the [AWS SDKs](https://aws.amazon.com/developertools/ "https://aws.amazon.com/developertools/") to access Security Lake.

## Step 1: Create IAM roles

If you access Security Lake programmatically, it's necessary to create some AWS Identity and Access Management (IAM) roles in order to
configure your data lake.

###### Important

It's not necessary to create these IAM roles if you use the Security Lake console to enable and configure Security Lake.

You must create roles in IAM if you'll be taking one or more of the following actions
(choose the links to see more information about IAM roles for each action):

- [Creating a custom source](custom-sources.md#iam-roles-custom-sources "custom-sources.md#iam-roles-custom-sources")
  – Custom sources are sources other than natively-supported
  AWS services that send data to Security Lake.
- [Creating a subscriber with data
  access](prereqs-creating-subscriber.md#iam-role-subscriber "prereqs-creating-subscriber.md#iam-role-subscriber") – Subscribers with permissions can directly access
  S3 objects from your data lake.
- [Creating a subscriber with query
  access](prereqs-query-subscriber.md#iam-role-query-subscriber "prereqs-query-subscriber.md#iam-role-query-subscriber") – Subscribers with permissions can query data from
  Security Lake using services like Amazon Athena.
- [Configuring a rollup Region](add-rollup-region.md#iam-role-replication "add-rollup-region.md#iam-role-replication")
  – A rollup Region consolidates data from multiple
  AWS Regions.

After creating the roles previously mentioned, attach the [AmazonSecurityLakeAdministrator](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeAdministrator") AWS managed policy to
the role that you're using to enable Security Lake. This policy grants administrative permissions that allow a principal to onboard to Security Lake and access
all Security Lake actions.

Attach the [AmazonSecurityLakeMetaStoreManager](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeAdministrator "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonSecurityLakeAdministrator") AWS managed policy to
create your data lake or query data from Security Lake. This policy is necessary for Security Lake to support extract, transform,
and load (ETL) jobs on raw log and event data that it receives from sources.

## Step 2: Enable Amazon Security Lake

To enable Security Lake programmatically, use the [CreateDataLake](../APIReference/API_CreateDataLake.md "../APIReference/API_CreateDataLake.md") operation of the Security Lake API. If you're
using the AWS CLI, run the [create-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/create-data-lake.html") command. In your request,
use the `region` field of the `configurations` object
to specify the Region code for the Region in which to enable Security Lake. For a list of Region codes, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md") in the _AWS General Reference_.

**Example 1**

The following example command enables Security Lake in the `us-east-1` and `us-east-2` Regions. In both Regions, this data lake is encrypted with Amazon S3 managed keys. Objects expire after 365 days, and objects transition to the `ONEZONE_IA` S3 storage
class after 60 days. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake create-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"`S3_MANAGED_KEY`"},"region":"`us-east-1`","lifecycleConfiguration": {"expiration":{"days":`365`},"transitions":[{"days":`60`,"storageClass":"`ONEZONE_IA`"}]}}, {"encryptionConfiguration": {"kmsKeyId":"`S3_MANAGED_KEY`"},"region":"`us-east-2`","lifecycleConfiguration": {"expiration":{"days":`365`},"transitions":[{"days":`60`,"storageClass":"`ONEZONE_IA`"}]}}]' \
--meta-store-manager-role-arn "`arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager`"`
```

**Example 2**

The following example command enables Security Lake in the `us-east-2` Region. This data lake is encrypted with a customer managed key that was created in
AWS Key Management Service (AWS KMS). Objects expire after 500 days, and objects transition to the `GLACIER` S3 storage class after 30 days. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake create-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"`1234abcd-12ab-34cd-56ef-1234567890ab`"},"region":"`us-east-2`","lifecycleConfiguration": {"expiration":{"days":`500`},"transitions":[{"days":`30`,"storageClass":"`GLACIER`"}]}}]' \
--meta-store-manager-role-arn "`arn:aws:iam:us-east-1:123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager`"`
```

###### Note

If you've already enabled Security Lake and want to update the
configuration settings for a Region or source, use the [UpdateDataLake](../APIReference/API_UpdateDataLake.md "../APIReference/API_UpdateDataLake.md") operation, or if using the AWS CLI, the [update-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html") command. Don't use the
`CreateDataLake` operation.

## Step 3: Configure sources

Security Lake collects log and event data from a variety of sources and across your
AWS accounts and AWS Regions. Follow these instructions to identify which data you want
Security Lake to collect. You can only use these instructions to add a natively-supported
AWS service as a source. For information about adding a custom source, see [Collecting data from custom sources in Security Lake](custom-sources.md "custom-sources.md").

To define one or more collection sources programmatically, use the [CreateAwsLogSource](../APIReference/API_CreateAwsLogSource.md "../APIReference/API_CreateAwsLogSource.md") operation of the Security Lake API. For each
source, specify a Regionally unique value for the `sourceName`
parameter. Optionally use additional parameters to limit the scope of the
source to specific accounts (`accounts`) or a specific version
(`sourceVersion`).

###### Note

If you don't include an optional parameter in your request, Security Lake applies your
request to all accounts or all versions of the specified source,
depending on the parameter that you exclude. For example, if you're the
delegated Security Lake administrator for an organization and you exclude the
`accounts` parameter, Security Lake applies your request to
all the accounts in your organization. Similarly, if you exclude the
`sourceVersion` parameter, Security Lake applies your request
to all versions of the specified source.

If your request specifies a Region in which you haven't enabled Security Lake,
an error occurs. To address this error, ensure that the `regions`
array specifies only those Regions in which you've enabled Security Lake.
Alternatively, you can enable Security Lake in the Region, and then submit your
request again.

When you enable Security Lake in an account for the first time, all the
selected log and event sources will be a part of a 15-day free trial period. For more
information about usage statistics, see
[Reviewing usage and estimated costs](reviewing-usage-costs.md "reviewing-usage-costs.md").

## Step 4: Configure storage settings and rollup Regions (optional)

You can specify the Amazon S3 storage class in which you want Security Lake to store your data
and for how long. You can also specify a rollup Region to consolidate data from multiple
Regions. These are optional steps. For more information, see [Lifecycle management in Security Lake](lifecycle-management.md "lifecycle-management.md").

To define a target objective programmatically when you enable Security Lake,
use the [CreateDataLake](../APIReference/API_CreateDataLake.md "../APIReference/API_CreateDataLake.md") operation of the Security Lake API. If you've
already enabled Security Lake and want to define a target objective, use the
[UpdateDataLake](../APIReference/API_UpdateDataLake.md "../APIReference/API_UpdateDataLake.md") operation, not the
`CreateDataLake` operation.

For either operation, use the supported parameters to specify the
configuration settings that you want:

- To specify a rollup Region, use the `region` field to
  specify the Region that you want to contribute data to the rollup
  Regions. In the `regions` array of the `replicationConfiguration` object,
  specify the Region code for each rollup Region. For a list of Region codes, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md") in the _AWS General Reference_.
- To specify retention settings for your data, use the
  `lifecycleConfiguration` parameters:

      + For `transitions`, specify the total number of
       days (`days`) that you want to store S3 objects
       in a particular Amazon S3 storage class
       (`storageClass`).
      + For `expiration`, specify the total number of
       days that you want to store objects in Amazon S3, using any
       storage class, after objects are created. When this
       retention period ends, objects expire and Amazon S3 deletes
       them.

  Security Lake applies the specified retention settings to the Region
  that you specify in the `region` field of the
  `configurations` object.

For example, the following command creates a data lake with `ap-northeast-2` as a rollup Region.
The `us-east-1` Region will contribute data to the `ap-northeast-2` Region. This example also establishes a
10-day expiration period for objects that are added to the data lake.

```
`$` `aws securitylake create-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"`S3_MANAGED_KEY`"},"region":"`us-east-1`","replicationConfiguration": {"regions": ["`ap-northeast-2`"],"roleArn":"`arn:aws:iam::123456789012:role/service-role/AmazonSecurityLakeS3ReplicationRole`"},"lifecycleConfiguration": {"expiration":{"days":`10`}}}]' \
--meta-store-manager-role-arn "`arn:aws:iam::123456789012:role/service-role/AmazonSecurityLakeMetaStoreManager`"`
```

You have now created your data lake. Use the [ListDataLakes](../APIReference/API_ListDataLakes.md "../APIReference/API_ListDataLakes.md") operation of the
Security Lake API to verify enablement of Security Lake and your data lake settings in each Region.

If issues or errors arise in the creation of your data lake, you can view a list of exceptions by using the [ListDataLakeExceptions](../APIReference/API_ListDataLakeExceptions.md "../APIReference/API_ListDataLakeExceptions.md")
operation, and notify users of exceptions with the [CreateDataLakeExceptionSubscription](../APIReference/API_CreateDataLakeExceptionSubscription.md "../APIReference/API_CreateDataLakeExceptionSubscription.md") operation. For more information, see [Troubleshooting data lake status](securitylake-data-lake-troubleshoot.md "securitylake-data-lake-troubleshoot.md").

## Step 5: View and query your own data

After creating your data lake, you can use Amazon Athena or similar services to view and
query your data from AWS Lake Formation databases and tables. When you programmatically enable Security Lake, database view
permissions aren't granted automatically. The data lake administrator account
in AWS Lake Formation must grant `SELECT` permissions to the IAM role you want to use
to query the relevant databases and tables. At a minimum, the role must have
_Data analyst_ permissions. For more information on permission
levels, see [Lake Formation personas and IAM
permissions reference](../../../lake-formation/latest/dg/permissions-reference.md "../../../lake-formation/latest/dg/permissions-reference.md"). For instructions on granting `SELECT`
permissions, see [Granting Data
Catalog permissions using the named resource method](../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md "../../../lake-formation/latest/dg/granting-cat-perms-named-resource.md") in the
_AWS Lake Formation Developer Guide_.

## Step 6: Create subscribers

After creating your data lake, you can add subscribers to consume your data.
Subscribers can consume data by directly accessing objects in your Amazon S3 buckets or by
querying the data lake. For more information about subscribers, see [Subscriber management in Security Lake](subscriber-management.md "subscriber-management.md").
