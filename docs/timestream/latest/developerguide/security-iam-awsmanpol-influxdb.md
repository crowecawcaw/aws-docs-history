

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# AWS managed policies for Amazon Timestream for InfluxDB
<a name="security-iam-awsmanpol-influxdb"></a>







To add permissions to users, groups, and roles, it is easier to use AWS managed policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) that provide your team with only the permissions they need. To get started quickly, you can use our AWS managed policies. These policies cover common use cases and are available in your AWS account. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. Services occasionally add additional permissions to an AWS managed policy to support new features. This type of update affects all identities (users, groups, and roles) where the policy is attached. Services are most likely to update an AWS managed policy when a new feature is launched or when new operations become available. Services do not remove permissions from an AWS managed policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple services. For example, the **ReadOnlyAccess** AWS managed policy provides read-only access to all AWS services and resources. When a service launches a new feature, AWS adds read-only permissions for new operations and resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.









## AWS managed policy: AmazonTimestreamInfluxDBServiceRolePolicy
<a name="security-iam-awsmanpol-timestreamforinfluxdbServiceRolePolicy"></a>







You cannot attach the AmazonTimestreamInfluxDBServiceRolePolicy AWS managed policy to identities in your account. This policy is part of the AWS TimestreamforInfluxDB service-linked role. This role allows the service to manage network interfaces and security groups in your account. 



Timestream for InfluxDB uses the permissions in this policy to manage EC2 security groups and network interfaces. This is required to manage Timestream for InfluxDB DB instances.





To review this policy in JSON format, see [AmazonTimestreamInfluxDBServiceRolePolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBServiceRolePolicy.html).

## AWS-managed policies for Amazon Timestream for InfluxDB
<a name="iam.identitybasedpolicies.predefinedpolicies"></a>

AWS addresses many common use cases by providing standalone IAM policies that are created and administered by AWS. Managed policies grant necessary permissions for common use cases so you can avoid having to investigate what permissions are needed. For more information, see [AWS Managed Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*. 

The following AWS managed policies, which you can attach to users in your account, are specific to Timestream for InfluxDB:

### AmazonTimestreamInfluxDBFullAccess
<a name="iam.identitybasedpolicies.predefinedpolicies-fullaccess"></a>

You can attach the `AmazonTimestreamInfluxDBFullAccess` policy to your IAM identities. This policy grants administrative permissions that allow full access to all Timestream for InfluxDB resources. 

You can also create your own custom IAM policies to allow permissions for Amazon Timestream for InfluxDB API actions. You can attach these custom policies to the IAM users or groups that require those permissions. 

To review this policy in JSON format, see [AmazonTimestreamInfluxDBFullAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccess.html).

## AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess
<a name="iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access"></a>

You can attach the `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` policy to your IAM identities. This policy grants administrative permissions that allow full access to all Timestream for InfluxDB resources, excluding any marketplace-related actions.

You can also create your own custom IAM policies to allow permissions for Timestream for InfluxDB API actions. You can attach these custom policies to the IAM users or groups that require those permissions.

To review this policy in JSON format, see [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess.html).





## Timestream for InfluxDB updates to AWS managed policies
<a name="security-iam-awsmanpol-updates"></a>



View details about updates to AWS managed policies for Timestream for InfluxDB since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the Timestream for InfluxDB Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB has added the `CreateDbBackup`, `GetDbBackup`, `ListDbBackups`, `DeleteDbBackup`, and `RestoreFromDbBackup` actions to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy for backup and restore operations on Amazon Timestream InfluxDB resources. | August 4, 2026 | 
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access) – Update to an existing policy | Amazon Timestream for InfluxDB has added the `CreateDbBackup`, `GetDbBackup`, `ListDbBackups`, `DeleteDbBackup`, and `RestoreFromDbBackup` actions to the existing `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` managed policy for backup and restore operations on Amazon Timestream InfluxDB resources. | August 4, 2026 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB has added the RebootDbInstance and RebootDbCluster actions to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy for rebooting Amazon Timestream InfluxDB resources. | 12/17/2025 | 
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access) – Update to an existing policy | Amazon Timestream for InfluxDB has added the RebootDbInstance and RebootDbCluster actions to the existing `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` managed policy for rebooting Amazon Timestream InfluxDB resources. | 12/17/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB has added the `ec2:DescribeVpcEndpoints` action to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy for describing the VPC endpoints. | 11/13/2025 | 
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access) – Update to an existing policy | Amazon Timestream for InfluxDB has added the `ec2:DescribeVpcEndpoints` action to the existing `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` managed policy for describing the VPC endpoints. | 11/13/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds necessary permissions to access Marketplace APIs for managing subscription required for creating and updating Timestream for InfluxDB cluster resources. | 4/16/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds marketplace product ID to support subscription to InfluxDB enterprise marketplace offerings for Timestream for InfluxDB cluster resources. | 10/17/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds necessary permissions to access Marketplace APIs for managing subscription required for creating and updating Timestream for InfluxDB cluster resources. | 4/16/2025 | 
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access) – New policy | Amazon Timestream for InfluxDB added a new policy to provide administrative access to manage Amazon Timestream for InfluxDB instances and parameter groups except marketplace operations. | 04/16/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` to also provide full administrative access to create, update, delete, and list Amazon Timestream InfluxDB clusters. | 2/17/2025 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – Update to an existing policy | Added the `ec2:DescribeRouteTables` action to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy. This action is used for describing your route tables | 10/08/2024 | 
| [AWS managed policy: AmazonTimestreamInfluxDBServiceRolePolicy](#security-iam-awsmanpol-timestreamforinfluxdbServiceRolePolicy) – New policy | Amazon Timestream for InfluxDB added a new policy that allows the service to manage network interfaces and security groups in your account. | 03/14/2024 | 
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess) – New policy | Amazon Timestream for InfluxDB added a new policy to provide full administrative access to create, update, delete and list Amazon Timestream InfluxDB instances and create and list parameter groups. | 03/14/2024 | 