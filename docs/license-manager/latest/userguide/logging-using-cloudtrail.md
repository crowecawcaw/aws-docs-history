# Logging AWS License Manager API calls using AWS CloudTrail

AWS License Manager is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in License Manager. CloudTrail captures all API calls for
License Manager as events. The calls captured include calls from the License Manager console and
code calls to the License Manager API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for License Manager. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to License Manager, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Topics

- [License Manager information in CloudTrail](license-manager-info-in-cloudtrail.md "license-manager-info-in-cloudtrail.md")
- [Understanding License Manager log
  file entries](understanding-license-manager-entries.md "understanding-license-manager-entries.md")
