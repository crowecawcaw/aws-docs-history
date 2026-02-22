# Disabling Security Lake

When you disable Amazon Security Lake, Security Lake stops collecting logs and events from your AWS
sources. Existing Security Lake settings and the resources that were created in your
AWS account are retained. In addition, the data that you stored in or published to other
AWS services, such as sensitive data in AWS Lake Formation tables and AWS CloudTrail logs, remains
available. Data that's stored in your Amazon Simple Storage Service (Amazon S3) bucket remains available in accordance
with your [Amazon S3 storage
lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md").

Disabling Security Lake from the **Settings** page on the Security Lake console
stops the collection of AWS logs and events in all AWS Regions in which Security Lake is
currently enabled. You can use the **Regions** page on the console to stop
log collection in specific Regions. The Security Lake API and AWS CLI also stop log collection in
the Regions that you specify in your request.

If you use the integration with AWS Organizations and your account is part of an organization
that centrally manages multiple Security Lake accounts, only the delegated Security Lake administrator can disable Security Lake for itself and for member
accounts. However, leaving an organization stops log collection for a member account.

When you disable Security Lake for an organization, the delegated administrator designation is
retained if you follow the disablement instructions provided on this page. You don't have to
designate the delegated administrator again before you can re-enable Security Lake.

If you configured one or more custom sources in Security Lake and you disable the service, you must also disable each source
independently from Security Lake. Otherwise, the custom source will continue to send logs to Amazon S3. Additionally, you must disable a subscriber
integration or the subscriber will still be able to consume data from Security Lake. For
details on how to remove the a custom source or a subscriber integration, see the respective
provider's documentation.

###### Important

If you disable Security Lake, also delete the existing AWS Glue resources for your data lake.
Otherwise, subsequent querying won't work properly if you enable Security Lake again later.
Although deletion of AWS Glue resources is a primary requirement, organizations have flexibility
in how they manage additional resources associated with the data lake.

If you choose to remove resources beyond the AWS Glue components, it's crucial to follow an "all or nothing" approach. If you decide to delete auxiliary resources, you
must comprehensively remove all associated components. These additional resources include: Security Lake SQS Queues (`AmazonSecurityLakeManager-xxx`), the Security Lake
Lambda function, event source mappings, and related IAM roles such as the `AmazonSecurityLakeMetaStoreManagerV2` role.

During this process, you do not need to remove Amazon S3 buckets that store data for the data lake. Organizations can retain these buckets without impacting the cleanup
procedure. The key consideration is to avoid partial removal of resources, which could potentially cause configuration issues in future deployments.

When planning to decommission your data lake, carefully evaluate whether you want to remove only the AWS Glue resources or perform a complete resource cleanup. If you opt
for comprehensive removal, ensure that you follow a systematic deletion process and remove all associated components.

When Security Lake is re-enabled, a new data lake is created in a new Amazon S3 bucket and data is
collected in this new S3 bucket. If you had previously deleted AWS Glue tables, a new set of
AWS Glue tables are created.

All the data that was collected before disabling Security Lake will stay in the previous Amazon S3 bucket. If you want to
query old data, you must move the data to the new bucket using the Amazon S3 `Sync`
command. For more details, see the [Sync command](https://awscli.amazonaws.com/v2/documentation/api/2.7.12/reference/s3/sync.html "https://awscli.amazonaws.com/v2/documentation/api/2.7.12/reference/s3/sync.html") in the AWS CLI Command Reference.

This topic explains how to disable Security Lake by using the Security Lake console, Security Lake API, or AWS CLI.

Console

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/ "https://console.aws.amazon.com/securitylake/").
2. In the navigation pane, under **Settings**, choose
   **General**.
3. Choose **Disable Security Lake**.
4. When prompted for confirmation, enter `Disable`, and then choose **Disable**.

API
To disable Security Lake programmatically, use the [DeleteDataLake](../APIReference/API_DeleteDataLake.md "../APIReference/API_DeleteDataLake.md") operation of the Security Lake API. If you're using the AWS CLI, run the
[delete-date-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/delete-data-lake.html") command. In your request, use
the `regions` list to specify the Region code for each Region in
which you want to disable Security Lake. For a list of Region codes, see [Amazon Security Lake endpoints](../../../general/latest/gr/securitylake.md "../../../general/latest/gr/securitylake.md") in the _AWS General Reference_.

For a Security Lake deployment utilizing AWS Organizations, only the delegated Security Lake administrator
for the organization can disable Security Lake for accounts in the
organization.

For example, the following AWS CLI command disables Security Lake in the `ap-northeast-1` and `eu-central-1` Regions.
This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\) line-continuation character to improve readability.

```
`$` `aws securitylake delete-data-lake \
--regions "`ap-northeast-1`" "`eu-central-1`"`
```
