# Using roles for Amazon Keyspaces Multi-Region Replication

Amazon Keyspaces (for Apache Cassandra) uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Keyspaces. Service-linked roles are predefined by Amazon Keyspaces and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon Keyspaces easier because you don’t have to
manually add the necessary permissions. Amazon Keyspaces defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Keyspaces can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This
protects your Amazon Keyspaces resources because you can't inadvertently remove permission to
access the resources.

## Service-linked role

permissions for Amazon Keyspaces

Amazon Keyspaces uses the service-linked role named **AWSServiceRoleForAmazonKeyspacesReplication**
to allow Amazon Keyspaces to add new AWS Regions to a keyspace on your behalf, and replicate tables and all their data and
settings to the new Region. The role also allows Amazon Keyspaces to replicate writes to tables in all Regions on your behalf.

The AWSServiceRoleForAmazonKeyspacesReplication service-linked role trusts the following services to assume the
role:

- `replication.cassandra.amazonaws.com`

The role permissions policy named KeyspacesReplicationServiceRolePolicy allows Amazon Keyspaces to complete
the following actions:

- Action: `cassandra:Select`
- Action: `cassandra:SelectMultiRegionResource`
- Action: `cassandra:Modify`
- Action: `cassandra:ModifyMultiRegionResource`
- Action: `cassandra:AlterMultiRegionResource`
- Action: `application-autoscaling:RegisterScalableTarget` – Amazon Keyspaces uses the application auto scaling
  permissions when you add a replica to a single Region table in provisioned mode with
  auto scaling enabled.
- Action: `application-autoscaling:DeregisterScalableTarget`
- Action: `application-autoscaling:DescribeScalableTargets`
- Action: `application-autoscaling:PutScalingPolicy`
- Action: `application-autoscaling:DescribeScalingPolicies`
- Action: `cassandra:Alter`
- Action: `cloudwatch:DeleteAlarms`
- Action: `cloudwatch:DescribeAlarms`
- Action: `cloudwatch:PutMetricAlarm`

Although the Amazon Keyspaces service-linked role AWSServiceRoleForAmazonKeyspacesReplication provides the permissions:
"Action:" for the specified Amazon Resource Name (ARN) "arn:\*" in the policy, Amazon Keyspaces supplies
the ARN of your account.

Permissions to create the service-linked role AWSServiceRoleForAmazonKeyspacesReplication are included in the
`AmazonKeyspacesFullAccess` managed policy. For more information, see [AWS managed policy:
AmazonKeyspacesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonKeyspacesFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonKeyspacesFullAccess").

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon Keyspaces

You can't manually create a service-linked role. When you
create a multi-Region keyspace in the AWS Management Console, the AWS CLI, or the AWS API, Amazon Keyspaces
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a multi-Region keyspace, Amazon Keyspaces creates the service-linked role for you again.

## Editing a service-linked role for

Amazon Keyspaces

Amazon Keyspaces does not allow you to edit the AWSServiceRoleForAmazonKeyspacesReplication service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for

Amazon Keyspaces

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is not
actively monitored or maintained. However, you must first delete all multi-Region keyspaces
in the account across all AWS Regions before you can delete the service-linked role
manually.

### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first delete any
multi-Region keyspaces and tables used by the role.

###### Note

If the Amazon Keyspaces service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the
operation again.

###### To delete Amazon Keyspaces resources used by the AWSServiceRoleForAmazonKeyspacesReplication (console)

1. Sign in to the AWS Management Console, and open the Amazon Keyspaces console at [https://console.aws.amazon.com/keyspaces/home](https://console.aws.amazon.com/keyspaces/home "https://console.aws.amazon.com/keyspaces/home").
2. Choose **Keyspaces** from the left-side panel.
3. Select all multi-Region keyspaces from the list.
4. Choose **Delete** confirm the deletion and choose **Delete keyspaces**.

You can also delete multi-Region keyspaces programmatically using any of the following
methods.

- The Cassandra Query Language (CQL) [DROP KEYSPACE](cql.ddl.md#cql.ddl.keyspace.drop "cql.ddl.md#cql.ddl.keyspace.drop") statement.
- The [delete-keyspace](../../../cli/latest/reference/keyspaces/delete-keyspace.md "../../../cli/latest/reference/keyspaces/delete-keyspace.md") operation of the AWS CLI.
- The [DeleteKeyspace](../APIReference/API_DeleteKeyspace.md "../APIReference/API_DeleteKeyspace.md") operation of the Amazon Keyspaces API.

### Manually delete the service-linked

role

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAmazonKeyspacesReplication
service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Amazon Keyspaces

service-linked roles

Amazon Keyspaces does not support using service-linked roles in every Region where the
service is available. You can use the AWSServiceRoleForAmazonKeyspacesReplication role in the following Regions.

| Region name               | Region identity | Support in Amazon Keyspaces |
| ------------------------- | --------------- | --------------------------- |
| US East (N. Virginia)     | us-east-1       | Yes                         |
| US East (Ohio)            | us-east-2       | Yes                         |
| US West (N. California)   | us-west-1       | Yes                         |
| US West (Oregon)          | us-west-2       | Yes                         |
| Asia Pacific (Mumbai)     | ap-south-1      | Yes                         |
| Asia Pacific (Osaka)      | ap-northeast-3  | Yes                         |
| Asia Pacific (Seoul)      | ap-northeast-2  | Yes                         |
| Asia Pacific (Singapore)  | ap-southeast-1  | Yes                         |
| Asia Pacific (Sydney)     | ap-southeast-2  | Yes                         |
| Asia Pacific (Tokyo)      | ap-northeast-1  | Yes                         |
| Canada (Central)          | ca-central-1    | Yes                         |
| Europe (Frankfurt)        | eu-central-1    | Yes                         |
| Europe (Ireland)          | eu-west-1       | Yes                         |
| Europe (London)           | eu-west-2       | Yes                         |
| Europe (Paris)            | eu-west-3       | Yes                         |
| Africa (Cape Town)        | af-south-1      | Yes                         |
| South America (São Paulo) | sa-east-1       | Yes                         |
| AWS GovCloud (US-East)    | us-gov-east-1   | No                          |
| AWS GovCloud (US-West)    | us-gov-west-1   | No                          |
