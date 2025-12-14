For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# AWS managed policies for Amazon Timestream for InfluxDB

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To get
started quickly, you can use our AWS managed policies. These policies cover common use cases
and are available in your AWS account. For more information about AWS managed policies,
see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to an
AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update an
AWS managed policy when a new feature is launched or when new operations become available.
Services do not remove permissions from an AWS managed policy, so policy updates won't
break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service launches
a new feature, AWS adds read-only permissions for new operations and resources. For a list
and descriptions of job function policies, see [AWS managed policies for
job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.

## AWS managed policy: AmazonTimestreamInfluxDBServiceRolePolicy

You cannot attach the AmazonTimestreamInfluxDBServiceRolePolicy AWS managed policy to identities in your account. This policy is part of the AWS TimestreamforInfluxDB service-linked role.
This role allows the service to manage network interfaces and security groups in your account.

Timestream for InfluxDB uses the permissions in this policy to manage EC2 security groups and network interfaces. This is required to manage Timestream for InfluxDB DB instances.

To review this policy in JSON format, see [AmazonTimestreamInfluxDBServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBServiceRolePolicy.md").

## AWS-managed policies for Amazon Timestream for InfluxDB

AWS addresses many common use cases by providing standalone IAM policies that are
created and administered by AWS. Managed policies grant necessary permissions for
common use cases so you can avoid having to investigate what permissions are needed.
For more information, see [AWS Managed Policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

The following AWS managed policies, which you can attach to users in your account, are specific to Timestream for InfluxDB:

### AmazonTimestreamInfluxDBFullAccess

You can attach the `AmazonTimestreamInfluxDBFullAccess` policy to your IAM identities.
This policy grants administrative permissions that allow full access to all Timestream for InfluxDB resources.

You can also create your own custom IAM policies to allow permissions for
Amazon Timestream for InfluxDB API actions. You can attach these custom policies to the IAM users or
groups that require those permissions.

To review this policy in JSON format, see [AmazonTimestreamInfluxDBFullAccess](../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccess.md").

## AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess

You can attach the `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` policy to your IAM identities.
This policy grants administrative permissions that allow full access to all Timestream for InfluxDB resources, excluding any marketplace-related actions.

You can also create your own custom IAM policies to allow permissions for Timestream for InfluxDB API
actions. You can attach these custom policies to the IAM users or groups that require
those permissions.

To review this policy in JSON format,
see [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess.md "../../../aws-managed-policy/latest/reference/AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess.md").

## Timestream for InfluxDB updates to AWS managed

policies

View details about updates to AWS managed policies for Timestream for InfluxDB since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe to
the RSS feed on the Timestream for InfluxDB Document history page.

| Change                                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                   | Date       |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB has added the `ec2:DescribeNetworkAcls` action to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy for describing network ACLs.                                                                                                | 12/08/2025 |
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access "#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access") – Update to an existing policy | Amazon Timestream for InfluxDB has added the `ec2:DescribeNetworkAcls` action to the existing `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` managed policy for describing network ACLs.                                                                        | 12/08/2025 |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB has added the `ec2:DescribeVpcEndpoints` action to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy for describing the VPC endpoints.                                                                                          | 11/13/2025 |
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access "#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access") – Update to an existing policy | Amazon Timestream for InfluxDB has added the `ec2:DescribeVpcEndpoints` action to the existing `AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess` managed policy for describing the VPC endpoints.                                                                  | 11/13/2025 |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds necessary permissions<br>to access Marketplace APIs for managing subscription required for creating and updating Timestream for InfluxDB cluster resources. | 4/16/2025  |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds<br>marketplace product ID to support subscription to InfluxDB enterprise marketplace offerings for Timestream for InfluxDB cluster resources.               | 10/17/2025 |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` that adds necessary permissions<br>to access Marketplace APIs for managing subscription required for creating and updating Timestream for InfluxDB cluster resources. | 4/16/2025  |
| [AmazonTimestreamInfluxDBFullAccessWithoutMarketplaceAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access "#iam.identitybasedpolicies.predefinedpolicies-fullaccess-without-marketplace-access") – New policy                   | Amazon Timestream for InfluxDB added a new policy to provide administrative access to manage Amazon Timestream for InfluxDB instances and parameter groups except marketplace operations.                                                                                     | 04/16/2025 |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Amazon Timestream for InfluxDB updated the existing managed policy `AmazonTimestreamInfluxDBFullAccess` to also provide full administrative access to create, update, delete, and list Amazon Timestream InfluxDB clusters.                                                   | 2/17/2025  |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – Update to an existing policy                                                                               | Added the `ec2:DescribeRouteTables` action to the existing `AmazonTimestreamInfluxDBFullAccess` managed policy. This action is used for describing your route tables                                                                                                          | 10/08/2024 |
| [AWS managed policy: AmazonTimestreamInfluxDBServiceRolePolicy](#security-iam-awsmanpol-timestreamforinfluxdbServiceRolePolicy "#security-iam-awsmanpol-timestreamforinfluxdbServiceRolePolicy") – New policy                                                          | Amazon Timestream for InfluxDB added a new policy that allows the service to manage network interfaces and security groups in your account.                                                                                                                                   | 03/14/2024 |
| [AmazonTimestreamInfluxDBFullAccess](#iam.identitybasedpolicies.predefinedpolicies-fullaccess "#iam.identitybasedpolicies.predefinedpolicies-fullaccess") – New policy                                                                                                 | Amazon Timestream for InfluxDB added a new policy to provide full administrative access to create, update, delete and list Amazon Timestream InfluxDB instances and create and list parameter groups.                                                                         | 03/14/2024 |
