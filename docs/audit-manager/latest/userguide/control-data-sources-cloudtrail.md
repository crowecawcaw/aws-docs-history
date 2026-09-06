

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# AWS CloudTrail event names supported by AWS Audit Manager
<a name="control-data-sources-cloudtrail"></a>



You can use Audit Manager to capture AWS CloudTrail [management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-management-events) and [global service events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-global-service-events) as evidence for audits. When you create or edit a custom control, you can specify one or more CloudTrail event names as a data source mapping for evidence collection. Audit Manager then filters your CloudTrail logs based on your chosen keywords, and imports the results as user activity evidence.

**Note**  
Audit Manager captures management events and global service events only. Data events and insights events are not available as evidence. For more information about the different types of CloudTrail events, see [CloudTrail concepts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-data-events) in the *AWS CloudTrail User Guide*. 

As an exception to the above, the following CloudTrail events aren't supported by Audit Manager:
+ kms\_GenerateDataKey
+ kms\_Decrypt
+ sts\_AssumeRole
+ kinesisvideo\_GetDataEndpoint
+ kinesisvideo\_GetSignalingChannelEndpoint 
+ kinesisvideo\_DescribeSignalingChannel 
+ kinesisvideo\_DescribeStream

As of May 11, 2023, Audit Manager no longer supports read-only CloudTrail events as keywords for evidence collection. We removed a total of 3,135 read-only keywords. Because customers and AWS services both make read calls to APIs, read-only events are noisy. As a result, read-only keywords collect a lot of evidence that isn't reliable or relevant for audits. Read-only keywords include `List`, `Describe`, and `Get` API calls (for example, [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) and [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) for Amazon S3). If you were using one of these keywords for evidence collection, you don't need to do anything. The keywords were automatically removed from the Audit Manager console and from your assessments, and evidence is no longer collected for these keywords.

## Additional resources
<a name="using-cloudtrail-events-additional-resources"></a>
+ To find help with evidence collection issues for this data source type, see [My assessment isn’t collecting user activity evidence from AWS CloudTrail](evidence-collection-issues.md#no-evidence-from-cloudtrail).
+ To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md).
+ To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md). 
+ To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md).