# Using service-linked roles for

Amazon Aurora

Amazon Aurora uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon Aurora. Service-linked roles are
predefined by Amazon Aurora and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes using Amazon Aurora easier because you don't have to manually
add the necessary permissions. Amazon Aurora defines the permissions of its service-linked
roles, and unless defined otherwise, only Amazon Aurora can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This protects
your Amazon Aurora resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

Amazon Aurora

Amazon Aurora
uses the service-linked role named AWSServiceRoleForRDS to allow Amazon RDS to call AWS services on behalf of your DB clusters.

The AWSServiceRoleForRDS service-linked role trusts the following services to assume the
role:

- `rds.amazonaws.com`

This service-linked role has a permissions policy attached to it called
`AmazonRDSServiceRolePolicy` that grants it permissions to operate in your
account.

For more information about this policy, including the JSON policy document, see
[AmazonRDSServiceRolePolicy](../../../aws-managed-policy/latest/reference/AmazonRDSServiceRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonRDSServiceRolePolicy.md")
in the _AWS Managed Policy Reference Guide_.

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. If you encounter the following
error message:

**Unable to create the resource. Verify that you have permission
to create service linked role. Otherwise wait and try again later.**

Make sure you have the following permissions enabled:

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/rds.amazonaws.com/AWSServiceRoleForRDS",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"rds.amazonaws.com"
        }
    }
}

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

### Creating a service-linked role for Amazon Aurora

You don't need to manually create a service-linked role. When you
create a DB cluster, Amazon Aurora creates the service-linked role for you.

###### Important

If you were using the Amazon Aurora service before December 1, 2017, when it
began supporting service-linked roles, then Amazon Aurora created the
AWSServiceRoleForRDS role in your account. To learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a DB cluster, Amazon Aurora creates the service-linked role for you
again.

### Editing a service-linked role for Amazon Aurora

Amazon Aurora does not allow you to edit the AWSServiceRoleForRDS service-linked role.
After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

### Deleting a service-linked role for Amazon Aurora

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity
that is not actively monitored or maintained. However, you must delete all of your DB

clusters before you can delete the service-linked
role.

#### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first confirm
that the role has no active sessions and remove any resources used by the
role.

###### To check whether the service-linked role has an active session in the IAM

console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose
   **Roles**. Then choose the name (not the check box) of
   the AWSServiceRoleForRDS role.
3. On the **Summary** page for the chosen role, choose the
   **Last Accessed** tab.
4. On the **Last Accessed** tab, review recent activity for
   the service-linked role.

###### Note

If you are unsure whether Amazon Aurora is
using the AWSServiceRoleForRDS role, you can try to delete the role. If the
service is using the role, then the deletion fails and you can view the
AWS Regions where the role is being used. If the role is being used,
then you must wait for the session to end before you can delete the
role. You cannot revoke the session for a service-linked role.

If you want to remove the AWSServiceRoleForRDS role, you must first delete _all_ of your DB
clusters.

##### Deleting all of

your clusters

Use one of the following procedures to delete a single cluster. Repeat the
procedure for each of your clusters.

###### To delete a cluster (console)

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the **Databases** list, choose the cluster that you
   want to delete.
3. For **Cluster Actions**, choose
   **Delete**.
4. Choose **Delete**.

###### To delete a cluster (CLI)

See `delete-db-cluster` in the
_AWS CLI Command Reference_.

###### To delete a cluster (API)

See `DeleteDBCluster` in the
_Amazon RDS API Reference_.

You can use the IAM console, the IAM CLI, or the IAM API to delete the
AWSServiceRoleForRDS service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Service-linked role permissions for Amazon RDS Beta

Amazon Aurora
uses the service-linked role named `AWSServiceRoleForRDSBeta` to
allow Amazon Aurora
to call AWS services on behalf of your RDS DB resources.

The AWSServiceRoleForRDSBeta service-linked role trusts the following services to assume
the role:

- `rds.amazonaws.com`

This service-linked role has a permissions policy attached to it called
`AmazonRDSBetaServiceRolePolicy` that grants it permissions to operate in
your account. For more information, see [AWS managed policy: AmazonRDSBetaServiceRolePolicy](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSBetaServiceRolePolicy "rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSBetaServiceRolePolicy").

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. If you encounter the following
error message:

**Unable to create the resource. Verify that you have permission
to create service linked role. Otherwise wait and try again later.**

Make sure you have the following permissions enabled:

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/custom.rds.amazonaws.com/AmazonRDSBetaServiceRolePolicy",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"custom.rds.amazonaws.com"
        }
    }
}

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Service-linked role for Amazon RDS Preview

Amazon Aurora
uses the service-linked role named `AWSServiceRoleForRDSPreview` to
allow Amazon Aurora
to call AWS services on behalf of your RDS DB resources.

The AWSServiceRoleForRDSPreview service-linked role trusts the following services to assume
the role:

- `rds.amazonaws.com`

This service-linked role has a permissions policy attached to it called
`AmazonRDSPreviewServiceRolePolicy` that grants it permissions to operate in
your account. For more information, see [AWS managed policy: AmazonRDSPreviewServiceRolePolicy](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPreviewServiceRolePolicy "rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPreviewServiceRolePolicy").

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. If you encounter the following
error message:

**Unable to create the resource. Verify that you have permission
to create service linked role. Otherwise wait and try again later.**

Make sure you have the following permissions enabled:

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/custom.rds.amazonaws.com/AmazonRDSPreviewServiceRolePolicy",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"custom.rds.amazonaws.com"
        }
    }
}

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.
