This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Logging AWS Wickr API calls using AWS CloudTrail

AWS Wickr is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Wickr. CloudTrail captures all API calls for Wickr as
events. The calls captured include calls from the AWS Management Console for Wickr and code calls to the
Wickr API operations. If you create a trail, you can enable continuous delivery of CloudTrail events
to an Amazon S3 bucket, including events for Wickr. If you don't configure a trail, you can still
view the most recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request that was made to Wickr, the IP
address from which the request was made, who made the request, when it was made, and additional
details. To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
