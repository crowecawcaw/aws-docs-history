# Monitoring Amazon Connect Health

Monitoring is an important part of maintaining the reliability, availability, and performance of Amazon Connect Health and your other AWS solutions. AWS provides the following monitoring tools to watch Amazon Connect Health, report when something is wrong, and take automatic actions when appropriate.

## AWS CloudTrail

Amazon Connect Health is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Connect Health. CloudTrail captures all API calls for Amazon Connect Health as events. The calls captured include calls from the Amazon Connect Health console and code calls to the Amazon Connect Health API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Connect Health. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in Event history. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Connect Health, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

All Amazon Connect Health API actions are logged by CloudTrail, including:

- Management events: All API calls to Amazon Connect Health services are logged, providing an audit trail of administrative actions.
- Data events: Optional data event logging captures Lambda invocations and Amazon S3 object access for detailed audit trails.
