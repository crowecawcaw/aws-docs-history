# Using service-linked roles for

Amazon RDS

Amazon RDS uses AWS Identity and Access Management (IAM)[service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to Amazon RDS. Service-linked roles are
predefined by Amazon RDS and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes using Amazon RDS easier because you don't have to manually
add the necessary permissions. Amazon RDS defines the permissions of its service-linked
roles, and unless defined otherwise, only Amazon RDS can assume its roles. The defined
permissions include the trust policy and the permissions policy, and that permissions policy
cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources. This protects
your Amazon RDS resources because you can't inadvertently remove permission to access the
resources.

For information about other services that support service-linked roles, see [AWS services that work with
IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the
**Service-Linked Role** column. Choose a **Yes** with a link to view the service-linked role documentation for that
service.

## Service-linked role permissions for

Amazon RDS

Amazon RDS
uses the service-linked role named AWSServiceRoleForRDS to allow Amazon RDS to call AWS services on behalf of your DB instances.

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

### Creating a service-linked role for Amazon RDS

You don't need to manually create a service-linked role. When you
create a DB instance, Amazon RDS creates the service-linked role for you.

###### Important

If you were using the Amazon RDS service before December 1, 2017, when it
began supporting service-linked roles, then Amazon RDS created the
AWSServiceRoleForRDS role in your account. To learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a DB instance, Amazon RDS creates the service-linked role for you
again.

### Editing a service-linked role for Amazon RDS

Amazon RDS does not allow you to edit the AWSServiceRoleForRDS service-linked role.
After you create a service-linked role, you cannot change the name of the role because
various entities might reference the role. However, you can edit the description of the
role using IAM. For more information, see [Editing
a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the _IAM User Guide_.

### Deleting a service-linked role for Amazon RDS

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity
that is not actively monitored or maintained. However, you must delete all of your DB
instances
before you can delete the service-linked
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

If you are unsure whether Amazon RDS is
using the AWSServiceRoleForRDS role, you can try to delete the role. If the
service is using the role, then the deletion fails and you can view the
AWS Regions where the role is being used. If the role is being used,
then you must wait for the session to end before you can delete the
role. You cannot revoke the session for a service-linked role.

If you want to remove the AWSServiceRoleForRDS role, you must first delete _all_ of your DB instances
.

##### Deleting all

of your instances

Use one of these procedures to delete each of your instances.

###### To delete an instance (console)

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the instance that you want to delete.
4. For **Actions**, choose
   **Delete**.
5. If you are prompted for **Create final Snapshot?**,
   choose **Yes** or **No**.
6. If you chose **Yes** in the previous step, for
   **Final snapshot name** enter the name of your final
   snapshot.
7. Choose **Delete**.

###### To delete an instance (CLI)

See `delete-db-instance` in the
_AWS CLI Command Reference_.

###### To delete an instance (API)

See `DeleteDBInstance` in the
_Amazon RDS API Reference_.

You can use the IAM console, the IAM CLI, or the IAM API to delete the
AWSServiceRoleForRDS service-linked role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Service-linked role permissions for

Amazon RDS Custom

Amazon RDS Custom uses the service-linked role named `AWSServiceRoleForRDSCustom` to
allow RDS Custom to call AWS services on behalf of your RDS DB resources.

The AWSServiceRoleForRDSCustom service-linked role trusts the following services to assume
the role:

- `custom.rds.amazonaws.com`

This service-linked role has a permissions policy attached to it called
`AmazonRDSCustomServiceRolePolicy` that grants it permissions to operate in
your account.

Creating, editing, or deleting the service-linked role for RDS Custom works the same as for
Amazon RDS. For more information, see [AWS managed policy: AmazonRDSCustomServiceRolePolicy](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSCustomServiceRolePolicy "rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSCustomServiceRolePolicy").

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
    "Resource": "arn:aws:iam::*:role/aws-service-role/custom.rds.amazonaws.com/AmazonRDSCustomServiceRolePolicy",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"custom.rds.amazonaws.com"
        }
    }
}

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Service-linked role permissions for Amazon RDS Beta

Amazon RDS
uses the service-linked role named `AWSServiceRoleForRDSBeta` to
allow Amazon RDS
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

Amazon RDS
uses the service-linked role named `AWSServiceRoleForRDSPreview` to
allow Amazon RDS
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
