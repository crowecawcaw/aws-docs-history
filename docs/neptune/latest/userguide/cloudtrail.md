# Logging Amazon Neptune API Calls with AWS CloudTrail

Amazon Neptune is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Neptune. CloudTrail captures API calls for Neptune
as events, including calls from the Neptune console and from code calls to the
Neptune APIs.

CloudTrail only logs events for Neptune Management API calls, such as creating an instance or
cluster. If you want to audit changes to your graph, you can use audit logs. For more
information, see [Using Audit Logs with Amazon Neptune Clusters](auditing.md "auditing.md").

###### Important

Amazon Neptune console, AWS CLI, and API calls are logged as calls made to the Amazon Relational Database Service
(Amazon RDS) API.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Neptune. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Neptune, the IP address
from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
