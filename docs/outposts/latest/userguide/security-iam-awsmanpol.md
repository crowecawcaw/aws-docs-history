

# AWS managed policies for AWS Outposts
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

## AWS managed policy: AWSOutpostsServiceRolePolicy
<a name="AWSOutpostsServiceRolePolicy"></a>

This policy is attached to a service-linked role that allows AWS Outposts to perform actions on your behalf. For more information, see [Service-linked roles](using-service-linked-roles.md).

## AWS Outposts updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for AWS Outposts since this service began tracking these changes.


| Change | Description | Date | 
| --- | --- | --- | 
| Updates to the AWS Identity and Access Management service-linked role AWSServiceRoleForOutposts\_{{OutpostID}} | The AWSServiceRoleForOutposts\_{{OutpostID}} service-linked role permissions are updated to refine how AWS Outposts manages networking resources for private connectivity, with more precise controls over network interface and security group operations needed for service link endpoint instances. | April 18, 2025 | 
| AWS Outposts started tracking changes | AWS Outposts started tracking changes for its AWS managed policies. | December 03, 2019 | 