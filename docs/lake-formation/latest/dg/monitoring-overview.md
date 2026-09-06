

# Security event logging in AWS Lake Formation
<a name="monitoring-overview"></a>

AWS Lake Formation is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Lake Formation. CloudTrail captures all API calls for Lake Formation as events. The calls captured include calls from the Lake Formation console, the AWS Command Line Interface, and code calls to the Lake Formation API operations. 

For more information about event logging in Lake Formation, see [Logging AWS Lake Formation API calls using AWS CloudTrail](logging-using-cloudtrail.md).

**Note**  
`GetTableObjects`, `UpdateTableObjects`, and `GetWorkUnitResults` are high-volume data plane operations. Calls to these APIs are not currently logged to CloudTrail. For more information about data plane operations in CloudTrail, see [Logging data events for trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.  
Changes in Lake Formation to support additional CloudTrail events will be documented at [Document history for AWS Lake Formation](doc-history.md).