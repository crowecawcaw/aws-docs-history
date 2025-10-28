# Logging WorkSpaces Secure Browser API calls using AWS CloudTrail

WorkSpaces Secure Browser is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Amazon WorkSpaces Secure Browser. CloudTrail captures all API calls for Amazon WorkSpaces Secure Browser as
events. These include calls from the Amazon WorkSpaces Secure Browser console and code calls to Amazon WorkSpaces Secure Browser API
operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for Amazon WorkSpaces Secure Browser. If you don't configure a trail, you can still view the
most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can identify the request that was made to Amazon WorkSpaces Secure Browser, the IP
address from which the request was made, who made the request, when it was made, as well as
additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Topics

- [WorkSpaces Secure Browser information in CloudTrail](service-name-info-in-cloudtrail.md "service-name-info-in-cloudtrail.md")
- [Understanding WorkSpaces Secure Browser log file entries](understanding-service-name-entries.md "understanding-service-name-entries.md")
