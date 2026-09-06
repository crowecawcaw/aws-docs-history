

# AWS managed policies for Amazon EVS
<a name="security-iam-awsmanpol"></a>

An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they’re available for all AWS customers to use. We recommend that you reduce permissions further by defining [customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the * IAM User Guide*.

## AWS managed policy: AmazonEVSServiceRolePolicy
<a name="security-iam-awsmanpol-amazonevsservicerolepolicy"></a>

You can’t attach `AmazonEVSServiceRolePolicy` to your IAM entities. This policy is attached to a service-linked role that allows Amazon EVS to perform actions on your behalf. For more information, see [Using service-linked roles for Amazon EVS](using-service-linked-roles.md). When you create an environment using an IAM principal that has the `iam:CreateServiceLinkedRole` permission, the `AWSServiceRoleforAmazonEVS` service-linked role is automatically created for you with this policy attached to it.

This policy allows the `AWSServiceRoleForAmazonEVS` service-linked role to call AWS services on your behalf.

 **Permissions details** 

This policy includes the following permissions that allow Amazon EVS to complete the following tasks.
+  `ec2` - Discover VPC networking components, including subnets and VPCs. Create, modify, tag, and delete elastic network interfaces that are used to establish a persistent connection between Amazon EVS and the VMware Cloud Foundation (VCF) SDDC Manager appliance in your VPC subnet. This connectivity is required for Amazon EVS to deploy, manage, and monitor the VCF deployment.
+  `ec2` - Delete EC2 instances that Amazon EVS creates when you make an EVS host deletion request. Describe and modify EC2 instance attributes so that default EC2 instance termination and stop protection can be disabled if needed to support EVS host deletion.
+  `ec2` - Manage EBS volumes for Cloud Builder installation and cleanup. During environment creation, Cloud Builder is installed onto one of the Amazon EVS deployed hosts to perform VCF configuration changes. After completion, Amazon EVS removes Cloud Builder by detaching and deleting the EC2 volume it is stored on.
+  `ec2` - Delete EVS VLAN subnets on your behalf if you request environment deletion.
+  `secretsmanager` - Delete VCF passwords that Amazon EVS creates and stores in AWS Secrets Manager during environment creation. Amazon EVS deletes all secrets that the service creates in your account if environment creation fails, or if you request environment deletion. Retrieve vCenter credentials from AWS Secrets Manager when you configure a vCenter connector by providing a secret ARN. The permission is scoped with a resource tag condition `EvsAccess=true` to ensure Amazon EVS only accesses secrets explicitly tagged for Amazon EVS vCenter access.
+  `kms` - Decrypt secrets and describe KMS keys when vCenter credentials stored in Secrets Manager are encrypted with KMS keys. The permission is scoped with a resource tag condition `EvsAccess=true` to ensure Amazon EVS only accesses KMS keys explicitly tagged for vCenter access.
+  `cloudwatch` - Publish AWS usage metrics to CloudWatch for Amazon EVS resources that have quotas.

To view more details about the policy, including the latest version of the JSON policy document, see [AmazonEVSServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEVSServiceRolePolicy.html) in the * AWS Managed Policy Reference Guide*.

## Amazon EVS updates to AWS managed policies
<a name="security-iam-awsmanpol-account-updates"></a>

View details about updates to AWS managed policies for Amazon EVS since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [Document history for the Amazon Elastic VMware Service User Guide](doc-history.md) page.


| Change | Description | Date | 
| --- | --- | --- | 
| AmazonEVSServiceRolePolicy — Policy updated | Amazon EVS updated the policy to allow the service to retrieve vCenter credentials from AWS Secrets Manager and decrypting secrets encrypted with KMS keys. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | March 23, 2026 | 
| AmazonEVSServiceRolePolicy — Policy updated | Amazon EVS updated the policy to add comprehensive resource management capabilities including EC2 instance management, EBS volume operations, and AWS Secrets Manager integration. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | August 14, 2025 | 
| AmazonEVSServiceRolePolicy — Policy updated | Amazon EVS updated the policy to allow the service to delete EVS VLAN subnets, as well as publish Amazon EVS usage metrics to CloudWatch. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | July 14, 2025 | 
| AmazonEVSServiceRolePolicy — New policy added | Amazon EVS added a new policy that allow the service to connect to a VPC subnet in the customer account. This connection is required for service functionality. To learn more, see [AWS managed policy: AmazonEVSServiceRolePolicy](#security-iam-awsmanpol-amazonevsservicerolepolicy). | June 09, 2025 | 
| Amazon EVS started tracking changes | Amazon EVS started tracking changes for its AWS managed policies. | June 09, 2025 | 