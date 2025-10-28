# Using service-linked roles for Oracle Database@AWS

Oracle Database@AWS uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts").
A service-linked role is a unique type of IAM role that is linked directly to Oracle Database@AWS.
Service-linked roles are predefined by Oracle Database@AWS and include all
the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes using Oracle Database@AWS easier because you don't
have to manually add the necessary permissions. Oracle Database@AWS defines the permissions
of its service-linked roles, and unless defined otherwise, only Oracle Database@AWS can assume its roles.
The defined permissions include the trust policy and the permissions policy,
and that permissions policy cannot be attached to any other IAM entity.

You can delete the roles only after first deleting their related resources.
This protects your Oracle Database@AWS resources because you can't
inadvertently remove permission to access the resources.

## Service-linked role permissions for Oracle Database@AWS

Oracle Database@AWS uses the service-linked role named AWSServiceRoleForODB
to allow Oracle Database@AWS to call AWS services on behalf of your resources.

The AWSServiceRoleForODB service-linked role trusts the following services to assume the role:

- `odb.amazonaws.com`
- `vpc-lattice.amazonaws.com`

This service-linked role has a permissions policy attached to it called
`AmazonODBServiceRolePolicy` that grants it permissions to operate in your account.
For more information, see [AWS managed policy: AmazonODBServiceRolePolicy](odb-security-iam-awsmanpol.md#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy "odb-security-iam-awsmanpol.md#odb-security-iam-awsmanpol-AmazonODBServiceRolePolicy").

###### Note

You must configure permissions to allow an IAM entity
(such as a user, group, or role) to create, edit, or delete a service-linked role.
If you encounter the following error message:

**Unable to create the resource. Verify that you have permission to create service-linked role.
Otherwise wait and try again later.**

Make sure you have the following permissions enabled:

```
{
    "Action": "iam:CreateServiceLinkedRole",
    "Effect": "Allow",
    "Resource": "arn:aws:iam::*:role/aws-service-role/odb.amazonaws.com/AWSServiceRoleForODB",
    "Condition": {
        "StringLike": {
            "iam:AWSServiceName":"odb.amazonaws.com",
            "iam:AWSServiceName":"vpc-lattice.amazonaws.com"
        }
    }
}
```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions") in the _IAM User Guide_.

### Creating a service-linked role for Oracle Database@AWS

You don't need to manually create a service-linked role. When you create an
Exadata database, Oracle Database@AWS creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again,
you can use the same process to recreate the role in your account.
When you create an Exadata database, Oracle Database@AWS creates the service-linked role for you again.

### Editing a service-linked role for Oracle Database@AWS

Oracle Database@AWS does not allow you to edit the AWSServiceRoleForODB service-linked role.
After you create a service-linked role, you cannot change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#edit-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#edit-service-linked-role") in the _IAM User Guide_.

### Deleting a service-linked role for Oracle Database@AWS

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity
that is not actively monitored or maintained. However, you must delete all of your resources
before you can delete the service-linked role.

### Cleaning up a service-linked role for Oracle Database@AWS

Before you can use IAM to delete a service-linked role,
you must first confirm that the role has no active sessions and
remove any resources used by the role.

###### To check whether the service-linked role has an active session in the IAM console

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**.
   Then choose the name (not the check box) of the AWSServiceRoleForODB role.
3. On the **Summary** page for the chosen role,
   choose the **Access Advisor** tab.
4. On the **Access Advisor** tab,
   review recent activity for the service-linked role.

###### Note

If you're unsure whether Oracle Database@AWS is using the AWSServiceRoleForODB role, you
can try to delete the role. If the service is using the role, then the deletion
fails and you can view the AWS Regions where the role is being used. If the
role is being used, then you must wait for the session to end before you can
delete the role. You cannot revoke the session for a service-linked role.

If you want to remove the AWSServiceRoleForODB role, you must first delete all of your Oracle Database@AWS resources.

## Supported Regions for Oracle Database@AWS service-linked roles

Oracle Database@AWS supports using service-linked roles in all of the AWS Regions where the service is available.
For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
