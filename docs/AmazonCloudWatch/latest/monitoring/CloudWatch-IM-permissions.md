# AWS managed policies for Internet Monitor

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed 
 to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because 
 they're available for all AWS customers to use. We recommend that you reduce permissions further by defining 
 [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies") that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS 
 managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is 
 most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for
 existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies "https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies") in the 
 *IAM User Guide*.


## AWS managed policy: CloudWatchInternetMonitorServiceRolePolicy


This policy is attached to the service-linked role named **AWSServiceRoleForInternetMonitor**
 to allow Internet Monitor to access resources in your account, such as Amazon Virtual Private Cloud resources or Network Load Balancers, so 
 that you can select them when you create a monitor. For more information, see [Service-linked role for Internet Monitor](using-service-linked-roles-CWIM.md "using-service-linked-roles-CWIM.md").


## AWS managed policy: CloudWatchInternetMonitorReadOnlyAccess


You can attach `CloudWatchInternetMonitorReadOnlyAccess` to your IAM entities.
 This policy grants access to read-only actions to work with monitors and data in with Internet Monitor. 
 Attach it to IAM users and other principals who need access to only read-only actions. 


Specifically, the scope of this policy includes `internetmonitor:` so that users can
 use read-only Internet Monitor actions and resources. It includes some `cloudwatch:` policies to retrieve information on
 CloudWatch metrics. It includes some `logs:` policies to manage log queries. 


To view the permissions for this policy, see [CloudWatchInternetMonitorReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorReadOnlyAccess.html") in the *AWS Managed Policy Reference*.


## AWS managed policy: CloudWatchInternetMonitorFullAccess


You can attach `CloudWatchInternetMonitorFullAccess` to your IAM entities.
 This policy grants full access to [Actions for Internet Monitor](https://docs.aws.amazon.com/internet-monitor/latest/api/API_Operations.html "https://docs.aws.amazon.com/internet-monitor/latest/api/API_Operations.html") for working with Internet Monitor. Attach it to IAM users and other principals 
 who need full access to Internet Monitor actions. 


Specifically, scope of this policy includes `internetmonitor:` so that users can
 use Internet Monitor actions and resources. It includes some `cloudwatch:` policies to retrieve information on
 CloudWatch alarms and metrics. It includes some `logs:` policies to manage log queries. It includes some
 `ec2:`, `cloudfront:`, `elasticloadbalancing:`, and `workspaces:` 
 policies to work with resources that you add to monitors so that Internet Monitor can create a traffic profile for
 your application. It contains some `iam:` policies to manage IAM roles. 


To view the permissions for this policy, see [CloudWatchInternetMonitorFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorFullAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/CloudWatchInternetMonitorFullAccess.html") in the *AWS Managed Policy Reference*.


## Internet Monitor updates to AWS managed policies


To view details about updates to AWS managed policies for Internet Monitor since this service
 began tracking these changes,
 see [CloudWatch updates to AWS managed policies](managed-policies-cloudwatch.md#security-iam-awsmanpol-updates "managed-policies-cloudwatch.md#security-iam-awsmanpol-updates").
 For automatic alerts about managed policy changes in CloudWatch, subscribe to the RSS feed on the CloudWatch 
 [Document history](DocumentHistory.md "DocumentHistory.md") page.
