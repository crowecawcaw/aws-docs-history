# Log AWS CodeBuild API calls with AWS CloudTrail

AWS CodeBuild is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in CodeBuild. CloudTrail captures all API calls for CodeBuild as
events, including calls from the CodeBuild console and from code calls to the CodeBuild APIs. If you
create a trail, you can enable continuous delivery of CloudTrail events to an S3 bucket, including
events for CodeBuild. If you don't configure a trail, you can still view the most recent events
in the CloudTrail console in **Event history**. Using the information collected
by CloudTrail, you can determine the request that was made to CodeBuild, the IP address from which the
request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [About AWS CodeBuild information in
  CloudTrail](service-name-info-in-cloudtrail.md "service-name-info-in-cloudtrail.md")
- [About AWS CodeBuild log file
  entries](understanding-service-name-entries.md "understanding-service-name-entries.md")
