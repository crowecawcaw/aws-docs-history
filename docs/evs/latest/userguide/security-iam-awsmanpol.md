

# AWS managed policies for Amazon EVS

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

 AWS managed policies might not grant least-privilege permissions for your use cases because they’re available to all AWS customers. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You can’t change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the * IAM User Guide*.

## AWS managed policy: AmazonEVSServiceRolePolicy
<a name="security-iam-awsmanpol-amazonevsservicerolepolicy"></a>

You can’t attach `AmazonEVSServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon Elastic VMware Service to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon EVS](using-service-linked-roles.md). When you create an environment using an IAM principal that has the `iam:CreateServiceLinkedRole` permission, the `AWSServiceRoleForAmazonEVS` service-linked role is automatically created for you with this policy attached to it.

This policy allows the `AWSServiceRoleForAmazonEVS` service-linked role to call AWS services on your behalf.

The following table lists the permissions in this policy and what Amazon EVS does with each of them.


| Permission scope | What Amazon EVS does | 
| --- | --- | 
|  `ec2`  | Amazon EVS discovers VPC networking components, including subnets and VPCs. Amazon EVS creates, modifies, tags, and deletes elastic network interfaces. These interfaces keep a persistent connection between Amazon EVS and the VMware Cloud Foundation (VCF) SDDC Manager appliance in your VPC subnet. Amazon EVS requires this connectivity to deploy, manage, and monitor the VCF deployment. | 
|  `ec2`  | Amazon EVS deletes the Amazon EC2 instances that it creates when you make an Amazon EVS host deletion request. Amazon EVS describes and modifies Amazon EC2 instance attributes so that it can disable default Amazon EC2 instance termination and stop protection if host deletion needs it. | 
|  `ec2`  | Amazon EVS manages EBS volumes for Cloud Builder installation and cleanup. During environment creation, Amazon EVS installs Cloud Builder onto one of the hosts that it deploys to perform VCF configuration changes. After completion, Amazon EVS removes Cloud Builder by detaching and deleting the EBS volume that Cloud Builder is stored on. | 
|  `ec2`  | Amazon EVS deletes Amazon EVS VLAN subnets on your behalf if you request environment deletion. | 
|  `secretsmanager` (delete) | Amazon EVS deletes the VCF passwords that it creates and stores in AWS Secrets Manager during environment creation. Amazon EVS deletes all secrets that it creates in your account if environment creation fails, or if you request environment deletion. | 
|  `secretsmanager` (read) | Amazon EVS retrieves vCenter credentials from AWS Secrets Manager when you configure a vCenter connector by providing a secret ARN. The permission is scoped with the resource tag condition `EvsAccess=true`, so Amazon EVS only accesses secrets that are explicitly tagged for Amazon EVS vCenter access. | 
|  `kms`  | Amazon EVS decrypts secrets and describes KMS keys when vCenter credentials stored in Secrets Manager are encrypted with KMS keys. The permission is scoped with the resource tag condition `EvsAccess=true`, so Amazon EVS only accesses KMS keys that are explicitly tagged for vCenter access. | 
|  `cloudwatch`  | Amazon EVS publishes AWS usage metrics to CloudWatch for Amazon EVS resources that have quotas. | 

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonEVSServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEVSServiceRolePolicy.html) in the * AWS Managed Policy Reference Guide*.

## Amazon EVS updates to AWS managed policies
<a name="security-iam-awsmanpol-account-updates"></a>

View details about updates to AWS managed policies for Amazon EVS since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history for the Amazon Elastic VMware Service User Guide](doc-history.md) page. The following table lists each change in the first column, a description in the second column, and the date in the third column.


| Change | Description | Date | 
| --- | --- | --- | 
| AmazonEVSServiceRolePolicy: Policy updated | Amazon EVS updated the policy to allow the service to retrieve vCenter credentials from AWS Secrets Manager and decrypt secrets encrypted with KMS keys. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | March 23, 2026 | 
| AmazonEVSServiceRolePolicy: Policy updated | Amazon EVS updated the policy to add resource management permissions, including Amazon EC2 instance management, EBS volume operations, and AWS Secrets Manager integration. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | August 14, 2025 | 
| AmazonEVSServiceRolePolicy: Policy updated | Amazon EVS updated the policy to allow the service to delete Amazon EVS VLAN subnets, and to publish Amazon EVS usage metrics to CloudWatch. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | July 14, 2025 | 
| AmazonEVSServiceRolePolicy: New policy added | Amazon EVS added a new policy that allows the service to connect to a VPC subnet in your account. Amazon EVS requires this connection to work. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | June 09, 2025 | 
| Amazon EVS started tracking changes | Amazon EVS started tracking changes for its AWS managed policies. | June 09, 2025 | 