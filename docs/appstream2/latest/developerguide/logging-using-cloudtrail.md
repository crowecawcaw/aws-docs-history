# Logging Amazon WorkSpaces Applications API Calls with AWS CloudTrail

Amazon WorkSpaces Applications is integrated with AWS CloudTrail. CloudTrail is a service that provides a record of actions taken
by a user, role, or an AWS service in WorkSpaces Applications. CloudTrail captures API calls for
WorkSpaces Applications as events. The calls captured include calls from the WorkSpaces Applications console and
code calls to the WorkSpaces Applications API operations. If you create a trail, you can enable continuous delivery
of CloudTrail events to an Amazon S3 bucket, including events for WorkSpaces Applications. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in **Event history**.
You can use the information collected by CloudTrail to determine details such as request information. For example, CloudTrail collects the following information: What request was made to
WorkSpaces Applications, the IP address from which the request was made, who made the request, and when it was
made.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [WorkSpaces Applications Information in CloudTrail](service-name-info-in-cloudtrail.md "service-name-info-in-cloudtrail.md")
- [Example: WorkSpaces Applications Log File Entries](understanding-service-name-entries.md "understanding-service-name-entries.md")
