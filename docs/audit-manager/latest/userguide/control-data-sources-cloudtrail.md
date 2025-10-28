# AWS CloudTrail event names supported by

AWS Audit Manager

You can use Audit Manager to capture AWS CloudTrail [management events](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-management-events "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-management-events") and [global service events](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-global-service-events "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-global-service-events") as evidence for audits. When you create or edit a custom
control, you can specify one or more CloudTrail event names as a data source mapping for evidence
collection. Audit Manager then filters your CloudTrail logs based on your chosen keywords, and imports the
results as user activity evidence.

###### Note

Audit Manager captures management events and global service events only. Data events and insights
events are not available as evidence. For more information about the different types of CloudTrail
events, see [CloudTrail concepts](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-data-events "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md#cloudtrail-concepts-data-events") in the _AWS CloudTrail User Guide_.

As an exception to the above, the following CloudTrail events aren't supported by Audit Manager:

- kms_GenerateDataKey
- kms_Decrypt
- sts_AssumeRole
- kinesisvideo_GetDataEndpoint
- kinesisvideo_GetSignalingChannelEndpoint
- kinesisvideo_DescribeSignalingChannel
- kinesisvideo_DescribeStream
  As of May 11, 2023, Audit Manager no longer supports read-only CloudTrail events as keywords for evidence
  collection. We removed a total of 3,135 read-only keywords. Because customers and
  AWS services both make read calls to APIs, read-only events are noisy. As a result,
  read-only keywords collect a lot of evidence that isn't reliable or relevant for audits.
  Read-only keywords include `List`, `Describe`, and `Get` API
  calls (for example, [GetObject](../../../AmazonS3/latest/API/API_GetObject.md "../../../AmazonS3/latest/API/API_GetObject.md") and [ListBuckets](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md") for Amazon S3). If you were
  using one of these keywords for evidence collection, you don't need to do anything. The
  keywords were automatically removed from the Audit Manager console and from your assessments, and
  evidence is no longer collected for these keywords.

## Additional resources

- To find help with evidence collection issues for this data source type, see [My assessment isn’t collecting user activity evidence from
  AWS CloudTrail](evidence-collection-issues.md#no-evidence-from-cloudtrail "evidence-collection-issues.md#no-evidence-from-cloudtrail").
- To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md "create-controls.md").
- To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md").
- To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md").
