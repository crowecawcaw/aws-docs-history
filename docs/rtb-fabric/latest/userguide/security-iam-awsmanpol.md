

# AWS managed policies for AWS RTB Fabric
<a name="security-iam-awsmanpol"></a>

AWS RTB Fabric uses AWS managed policies and service-linked roles to securely access AWS services on your behalf. AWS managed policies are standalone policies created and maintained by AWS that provide permissions for common use cases. A service-linked role is a unique type of IAM role that is linked directly to RTB Fabric and uses these managed policies to include all the permissions that the service requires to call other AWS services on your behalf.

For information about the service-linked role that RTB Fabric creates, see [Using service-linked roles for RTB Fabric](https://docs.aws.amazon.com/using-service-linked-roles.html).

## RTBFabricServiceRolePolicy
<a name="aws-managed-policy-RTBFabricServiceRolePolicy"></a>

The RTBFabricServiceRolePolicy managed policy allows RTB Fabric to manage network interfaces and publish CloudWatch metrics on your behalf. This policy provides the necessary permissions for RTB Fabric to create, modify, and delete network interfaces with proper tagging controls, as well as to publish custom metrics to CloudWatch.

This policy grants the following permissions:
+ *Amazon EC2 network interface management* – Allows creating network interfaces in specified subnets and security groups, with conditional permissions to create tagged network interfaces and manage network interface permissions.
+ *Amazon EC2 network interface operations* – Allows deleting and detaching network interfaces that are tagged with RTBFabricManaged=true, ensuring operations are limited to RTB Fabric-managed resources.
+ *Amazon EC2 tagging* – Allows creating tags on network interfaces during the CreateNetworkInterface action to properly identify RTB Fabric-managed resources.
+ *Amazon EC2 describe operations* – Allows describing availability zones, network interfaces, subnets, VPCs, and security groups to gather necessary information for network interface management.
+ *Amazon CloudWatch metrics* – Allows publishing custom metrics to the AWS/RTBFabric namespace for monitoring and observability purposes.

To view more details about the policy, including the latest version of the JSON policy document, see [RTBFabricServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/RTBFabricServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*.

## RTB Fabric updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>

View details about updates to AWS managed policies for RTB Fabric since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the RTB Fabric Document history page.


| Change | Description | Date | 
| --- | --- | --- | 
| [RTBFabricServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/RTBFabricServiceRolePolicy.html) – Policy updated | RTB Fabric updated the CloudWatch namespace from `rtbfabric` to `AWS/RTBFabric` for publishing custom metrics. | October 16, 2025 | 
| [RTBFabricServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/RTBFabricServiceRolePolicy.html) – New policy | RTB Fabric added a new managed policy that allows RTB Fabric to manage network interfaces and publish CloudWatch metrics on your behalf. | August 19, 2025 | 
| RTB Fabric started tracking changes | RTB Fabric started tracking changes for its AWS managed policies. | March 1, 2021 | 