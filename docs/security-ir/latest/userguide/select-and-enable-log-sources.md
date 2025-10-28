# Select and enable log sources

Ahead of a security investigation, you need to capture relevant logs to
retroactively reconstruct activity in an AWS account. Select and enable
log sources relevant to their AWS account workloads.

AWS CloudTrail is a logging service that tracks API calls made against an AWS account capturing
AWS service activity. It is enabled by default with 90-day retention of management events that can be
[retrieved through CloudTrail’s Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md")
facility using AWS Management Console, the AWS CLI, or an AWS SDK. For
longer retention and visibility of data events, you need to
[create a CloudTrail Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
and associated with an Amazon S3 bucket, and optionally, with a CloudWatch
log group. Alternatively, you can create a
[CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md"),
which retains CloudTrail logs for up to seven years and provides a SQL-based querying facility.

AWS recommends that customers using a VPC enable network traffic and DNS logs using, respectively,
[VPC Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md") and
[Amazon Route 53 resolver query logs](../../../Route53/latest/DeveloperGuide/resolver-query-logs.md "../../../Route53/latest/DeveloperGuide/resolver-query-logs.md"),
streaming them to either an Amazon S3 bucket or a CloudWatch log group. You can create a VPC flow
log for a VPC, a subnet, or a network interface. For VPC Flow Logs, you can be selective
on how and where you enable Flow Logs to reduce cost.

AWS CloudTrail Logs, VPC Flow Logs, and Route 53 resolver query logs are the _basic
logging trifecta_ to support security investigations in AWS.

AWS services can generate logs not captured by the basic logging trifecta,
such as Elastic Load Balancing logs, AWS WAF logs, AWS Config recorder
logs, Amazon GuardDuty findings, Amazon Elastic Kubernetes Service (Amazon EKS)
audit logs, and Amazon EC2 instance operating system and application logs. Refer
to [Appendix A: Cloud capability definitions](appendix-a-cloud-capability-definitions.md "appendix-a-cloud-capability-definitions.md") for the full list of logging and monitoring options.
