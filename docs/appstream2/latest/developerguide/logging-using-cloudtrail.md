# Logging AppStream 2.0 API Calls with AWS CloudTrail

Amazon AppStream 2.0 is integrated with AWS CloudTrail. CloudTrail is a service that provides a record of actions taken
by a user, role, or an AWS service in AppStream 2.0. CloudTrail captures API calls for
AppStream 2.0 as events. The calls captured include calls from the AppStream 2.0 console and
code calls to the AppStream 2.0 API operations. If you create a trail, you can enable continuous delivery
of CloudTrail events to an Amazon S3 bucket, including events for AppStream 2.0. If you don't configure a trail, you can
still view the most recent events in the CloudTrail console in **Event history**.
You can use the information collected by CloudTrail to determine details such as request information. For example, CloudTrail collects the following information: What request was made to
AppStream 2.0, the IP address from which the request was made, who made the request, and when it was
made.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [AppStream 2.0 Information in CloudTrail](service-name-info-in-cloudtrail.md "service-name-info-in-cloudtrail.md")
- [Example: AppStream 2.0 Log File Entries](understanding-service-name-entries.md "understanding-service-name-entries.md")
