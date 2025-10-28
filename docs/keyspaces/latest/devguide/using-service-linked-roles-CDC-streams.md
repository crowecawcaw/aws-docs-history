# Using roles for Amazon Keyspaces CDC streams

Amazon Keyspaces (for Apache Cassandra) uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Keyspaces. Service-linked roles are predefined by Amazon Keyspaces and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up Amazon Keyspaces easier because you don’t have to
manually add the necessary permissions. Amazon Keyspaces defines the permissions of its
service-linked roles, and unless defined otherwise, only Amazon Keyspaces can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can't delete the service-linked role.

## Service-linked role

permissions for Amazon Keyspaces

Amazon Keyspaces uses the service-linked role named **AWSServiceRoleForAmazonKeyspacesCDC**
to allow Amazon Keyspaces CDC streams to publish CloudWatch metrics into your account on your behalf.

The AWSServiceRoleForAmazonKeyspacesCDC service-linked role trusts the following service to assume the
role:

- `cassandra-streams.amazonaws.com`

The role permissions policy named [KeyspacesCDCServiceRolePolicy](../../../aws-managed-policy/latest/reference/KeyspacesCDCServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/KeyspacesCDCServiceRolePolicy.md") allows Amazon Keyspaces to complete the following action on
resources in the CloudWatch namespace `AWS/Cassandra`:

- Action: `cloudwatch:PutMetricData` on
  `*`

The AWSServiceRoleForAmazonKeyspacesCDC provides the permissions: Action: cloudwatch:PutMetricData on
all resources that match the following condition: `"cloudwatch:namespace": "AWS/Cassandra"`.

For more information about KeyspacesCDCServiceRolePolicy, see [AWS managed
policy: KeyspacesCDCServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-KeyspacesCDCServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-KeyspacesCDCServiceRolePolicy").

To enable CDC streams for a table, which automatically creates the service-linked role
AWSServiceRoleForAmazonKeyspacesCDC, the IAM principal needs the following permissions.

```
{
    "Sid": "KeyspacesCDCServiceLinkedRole",
    "Effect": "Allow",
    "Action": "iam:CreateServiceLinkedRole",
    "Resource": "arn:aws:iam::*:role/aws-service-role/cassandra-streams.amazonaws.com/AWSServiceRoleForAmazonKeyspacesCDC",
    "Condition": {
    "StringLike": {
        "iam:AWSServiceName": "cassandra-streams.amazonaws.com"
    }
}
```

Permissions to create the service-linked role AWSServiceRoleForAmazonKeyspacesCDC are included in the
`AmazonKeyspacesFullAccess` managed policy. For more information, see [AWS managed policy:
AmazonKeyspacesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonKeyspacesFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonKeyspacesFullAccess").

## Creating a service-linked role for

Amazon Keyspaces

You don't need to manually create a service-linked role for Amazon Keyspaces CDC streams. When you
enable Amazon Keyspaces CDC streams on a table with the AWS Management Console, CQL, the AWS CLI, or the AWS API, Amazon Keyspaces
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use the
same process to recreate the role in your account. When you enable Amazon Keyspaces CDC streams for a
table, Amazon Keyspaces creates the service-linked role for you again.

## Editing a service-linked role for

Amazon Keyspaces

Amazon Keyspaces doesn’t allow you to edit the AWSServiceRoleForAmazonKeyspacesCDC service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Amazon Keyspaces

service-linked roles

Amazon Keyspaces supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
