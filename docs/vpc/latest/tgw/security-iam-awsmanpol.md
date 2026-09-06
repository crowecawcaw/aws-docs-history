

# AWS managed policies for transit gateways in AWS Transit Gateway
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

To work with a transit gateway, one of the following AWS managed policies might meet your needs:
+ [AmazonEC2FullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2FullAccess.html)
+ [AmazonEC2ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html)
+ [PowerUserAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/PowerUserAccess.html)
+ [ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/ReadOnlyAccess.html)

## AWS managed policy: AWSVPCTransitGatewayServiceRolePolicy
<a name="AWSVPCTransitGatewayServiceRolePolicy"></a>

This policy is attached to the role [AWSServiceRoleForVPCTransitGateway](service-linked-roles.md). This allows Amazon VPC to create and manage resources for your transit gateway attachments.

To view the permissions for this policy, see [AWSVPCTransitGatewayServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSVPCTransitGatewayServiceRolePolicy.html) in the *AWS Managed Policy Reference*.

## Transit gateway updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for transit gateways since Amazon VPC began tracking these changes in March 2021.


| Change | Description | Date | 
| --- | --- | --- | 
| Amazon VPC started tracking changes | Amazon VPC started tracking changes to its AWS managed policies. | March 1, 2021 | 