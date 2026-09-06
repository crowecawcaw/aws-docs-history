

# AWS managed policies for Amazon Aurora DSQL
<a name="security-iam-awsmanpol"></a>



An AWS managed policy is a standalone policy that is created and administered by AWS. AWS managed policies are designed to provide permissions for many common use cases so that you can start assigning permissions to users, groups, and roles.

Keep in mind that AWS managed policies might not grant least-privilege permissions for your specific use cases because they're available for all AWS customers to use. We recommend that you reduce permissions further by defining [ customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#customer-managed-policies) that are specific to your use cases.

You cannot change the permissions defined in AWS managed policies. If AWS updates the permissions defined in an AWS managed policy, the update affects all principal identities (users, groups, and roles) that the policy is attached to. AWS is most likely to update an AWS managed policy when a new AWS service is launched or new API operations become available for existing services.

For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

 





## AWS managed policy: AmazonAuroraDSQLFullAccess
<a name="security-iam-awsmanpol-AmazonAuroraDSQLFullAccess"></a>



You can attach `AmazonAuroraDSQLFullAccess` to your users, groups, and roles.

This policy grants permissions that allows full administrative access to Aurora DSQL. Principals with these permissions can:
+ Create, delete, and update Aurora DSQL clusters, including multi-Region clusters
+ Manage cluster inline policies (create, view, update, and delete policies)
+ Create, update, delete, and manage CDC streams for clusters
+ Add and remove tags from clusters and CDC streams
+ List clusters and view information about individual clusters
+ See tags attached to Aurora DSQL clusters
+ Connect to the database as any user, including admin
+ Pass IAM roles to CDC streams for data delivery to target destinations
+ Perform backup and restore operations for Aurora DSQL clusters, including starting, stopping, and monitoring backup and restore jobs
+ Use customer-managed AWS KMS keys for cluster encryption
+ View any metrics from CloudWatch for their account
+ Use AWS Fault Injection Service (AWS FIS) to inject failures into Aurora DSQL clusters for fault tolerance testing
+ Create service-linked roles for the `dsql.amazonaws.com` service, which is required for creating clusters



**Permissions details**

This policy includes the following permissions.


+ `dsql` – grants principals full access to Aurora DSQL.
+ `cloudwatch` – grants permission to publish metric data points to Amazon CloudWatch.
+ `iam` – grants permission to create a service-linked role and pass roles to CDC streams for data delivery.
+ `backup and restore` – grants permissions to start, stop, and monitor backup and restore jobs for Aurora DSQL clusters. 
+ `kms` – grants permissions required to validate access to customer-managed keys used for Aurora DSQL cluster encryption when creating, updating, or connecting to clusters. 
+ `fis` – grants permissions to use AWS Fault Injection Service (AWS FIS) to inject failures into Aurora DSQL clusters for fault tolerance testing.

You can find the `AmazonAuroraDSQLFullAccess` policy in the IAM console and in the [AWS Managed Policy Reference Guide](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAuroraDSQLFullAccess.html).

## AWS managed policy: AmazonAuroraDSQLReadOnlyAccess
<a name="security-iam-awsmanpol-AmazonAuroraDSQLReadOnlyAccess"></a>



You can attach `AmazonAuroraDSQLReadOnlyAccess` to your users, groups, and roles.

Allows read access to Aurora DSQL. Principals with these permissions can list clusters and view information about individual clusters. They can see the tags attached to Aurora DSQL clusters and CDC streams, view information about individual CDC streams, and view cluster inline policies. They can retrieve and see any metrics from CloudWatch on your account. 



**Permissions details**

This policy includes the following permissions.




+ `dsql` – grants read only permissions to all resources in Aurora DSQL.
+ `cloudwatch` – grants permission to retrieve batch amounts of CloudWatch metric data and perform metric math on retrieved data 
+ `iam` – grants permissions to pass roles to CDC streams for data delivery configuration.

You can find the `AmazonAuroraDSQLReadOnlyAccess` policy in the IAM console and the [AWS Managed Policy Reference Guide](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAuroraDSQLReadOnlyAccess.html).

## AWS managed policy: AmazonAuroraDSQLConsoleFullAccess
<a name="security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess"></a>



You can attach `AmazonAuroraDSQLConsoleFullAccess` to your users, groups, and roles.

Allows full administrative access to Amazon Aurora DSQL via the AWS Management Console. Principals with these permissions can:
+ Create, delete, and update Aurora DSQL clusters, including multi-Region clusters, with the console
+ Manage cluster inline policies through the console (create, view, update, and delete policies)
+ List clusters and view information about individual clusters
+ See tags on any resource on your account
+ Connect to the database as any user, including the admin
+ Perform backup and restore operations for Aurora DSQL clusters, including starting, stopping, and monitoring backup and restore jobs
+ Use customer-managed AWS KMS keys for cluster encryption
+ Launch AWS CloudShell from the AWS Management Console
+ View any metrics from CloudWatch on your account
+ Use AWS Fault Injection Service (AWS FIS) to inject failures into Aurora DSQL clusters for fault tolerance testing
+ Create service linked roles for the `dsql.amazonaws.com` service, which is required for creating clusters

You can find the `AmazonAuroraDSQLConsoleFullAccess` policy on the IAM console and [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAuroraDSQLConsoleFullAccess.html) in the AWS Managed Policy Reference Guide.



**Permissions details**

This policy includes the following permissions.




+ `dsql` – grants full administrative permissions to all resources in Aurora DSQL via the AWS Management Console.
+ `cloudwatch` – grants permission to retrieve batch amounts of CloudWatch metric data and perform metric math on retrieved data. 
+ `tag` – grants permission to returns tag keys and values currently in use in the specified AWS Region for the calling account.
+ `backup and restore` – grants permissions to start, stop, and monitor backup and restore jobs for Aurora DSQL clusters. 
+ `kms` – grants permissions required to validate access to customer-managed keys used for Aurora DSQL cluster encryption when creating, updating, or connecting to clusters. 
+ `cloudshell` – grants permissions to launch AWS CloudShell to interact with Aurora DSQL.
+ `ec2` – grants permission to view Amazon VPC endpoint information needed for Aurora DSQL connections.
+ `fis` – grants permissions to use AWS FIS to inject failures into Aurora DSQL clusters for fault tolerance testing.
+ `access-analyzer:ValidatePolicy` grants permission for the linter in the policy editor, which provides real-time feedback about errors, warnings, and security issues in the current policy.
+ `fis` – grants permissions to use AWS Fault Injection Service (AWS FIS) to inject failures into Aurora DSQL clusters for fault tolerance testing.

You can find the `AmazonAuroraDSQLConsoleFullAccess` policy in the IAM console and the [AWS Managed Policy Reference Guide](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonAuroraDSQLConsoleFullAccess.html).

## AWS managed policy: AuroraDSQLServiceRolePolicy
<a name="security-iam-awsmanpol-AuroraDSQLServiceRolePolicy"></a>



You can't attach AuroraDSQLServiceRolePolicy to your IAM entities. This policy is attached to a service-linked role that allows Aurora DSQL to access account resources.

You can find the `AuroraDSQLServiceRolePolicy` policy on the IAM console and [AuroraDSQLServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AuroraDSQLServiceRolePolicy.html) in the AWS Managed Policy Reference Guide.





## Aurora DSQL updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Aurora DSQL since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Aurora DSQL Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| AmazonAuroraDSQLFullAccess and AmazonAuroraDSQLConsoleFullAccess update | Added support for AWS Fault Injection Service (AWS FIS) integration with Aurora DSQL. This allows you to inject failures into single-Region and multi-Region Aurora DSQL clusters to test fault tolerance of your applications. You can create experiment templates in the AWS FIS console to define failure scenarios and target specific Aurora DSQL clusters for testing.<br />For more on these policies, see [AmazonAuroraDSQLFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLFullAccess) and [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess). | August 19, 2025 | 
| AmazonAuroraDSQLFullAccess, AmazonAuroraDSQLReadOnlyAccess, and AmazonAuroraDSQLConsoleFullAccess update | Added resource-based policy (RBP) support with new permissions: `PutClusterPolicy`, `GetClusterPolicy`, and `DeleteClusterPolicy`. These permissions allow managing inline policies attached to Aurora DSQL clusters for fine-grained access control.<br />For more information, see [AmazonAuroraDSQLFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLFullAccess), [AmazonAuroraDSQLReadOnlyAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLReadOnlyAccess), and [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess). | October 15, 2025 | 
| AmazonAuroraDSQLFullAccess update | Adds the capability to perform backup and restore operations for Aurora DSQL clusters, including starting, stopping, and monitoring jobs. It also adds the capability to use customer-managed KMS keys for cluster encryption.<br />For more information, see [AmazonAuroraDSQLFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLFullAccess) and [Using service-linked roles in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 21, 2025 | 
| AmazonAuroraDSQLConsoleFullAccess update | Adds the capability to perform backup and restore operations for Aurora DSQL clusters through the AWS Console Home. This includes starting, stopping, and monitoring jobs. It also supports using customer-managed KMS keys for cluster encryption and launching AWS CloudShell.<br />For more information, see [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess) and [Using service-linked roles in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 21, 2025 | 
| AmazonAuroraDSQLFullAccess update | The policy adds four new permissions to create and manage database clusters across multiple AWS Regions: `PutMultiRegionProperties`, `PutWitnessRegion`, `AddPeerCluster`, and `RemovePeerCluster`. These permissions include resource-level controls and condition keys so you can control which clusters users you can modify.<br />The policy also adds the `GetVpcEndpointServiceName` permission to help you connect to your Aurora DSQL clusters through AWS PrivateLink.<br />For more information, see For more information, see [AmazonAuroraDSQLFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLFullAccess) and [Using service-linked roles in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 13, 2025 | 
| AmazonAuroraDSQLReadOnlyAccess update | Includes the ability to determine the correct VPC endpoint service name when connecting to your Aurora DSQL clusters through AWS PrivateLink Aurora DSQL creates unique endpoints per cell, so this API helps ensure you can identify the correct endpoint for your cluster and avoid connection errors.For more information, see [AmazonAuroraDSQLReadOnlyAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLReadOnlyAccess) and [Using service-linked roles in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 13, 2025 | 
| AmazonAuroraDSQLConsoleFullAccess update | Adds new permissions to Aurora DSQL to support multi-Region cluster management and VPC endpoint connection. The new permissions include: PutMultiRegionPropertiesPutWitnessRegionAddPeerClusterRemovePeerClusterGetVpcEndpointServiceNameFor more information, see [AmazonAuroraDSQLConsoleFullAccess](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-AmazonAuroraDSQLConsoleFullAccess) and [Using service-linked roles in Aurora DSQL ](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 13, 2025 | 
| AuroraDsqlServiceLinkedRolePolicy update | Adds the ability to publish metrics to the AWS/AuroraDSQL and AWS/Usage CloudWatch namespaces to the policy. This allows the associated service or role to emit more comprehensive usage and performance data to your CloudWatch environment. For more information, see [AuroraDsqlServiceLinkedRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AuroraDsqlServiceLinkedRolePolicy.html) and [Using service-linked roles in Aurora DSQL](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/working-with-service-linked-roles.html). | May 8, 2025 | 
| Page created | Started tracking AWS managed policies related to Amazon Aurora DSQL | December 3, 2024 | 