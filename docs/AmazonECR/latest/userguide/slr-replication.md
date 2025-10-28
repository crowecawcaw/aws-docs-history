# Amazon ECR service-linked role for replication

Amazon ECR uses a service-linked role named **AWSServiceRoleForECRReplication**
that allows Amazon ECR to replicate images across multiple accounts.

## Service-linked role permissions for

Amazon ECR

The AWSServiceRoleForECRReplication service-linked role trusts the following services to assume the
role:

- `replication.ecr.amazonaws.com`

The following `ECRReplicationServiceRolePolicy` role permissions policy
allows Amazon ECR to use the following actions on resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:CreateRepository",
 "ecr:ReplicateImage"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Note

The `ReplicateImage` is an internal API that Amazon ECR uses for
replication and can't be called directly.

You must configure permissions to allow an IAM entity (for example a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

Amazon ECR

You don't need to manually create the Amazon ECR service-linked role. When you
configure replication settings for your registry in the AWS Management Console, the AWS CLI, or the
AWS API, Amazon ECR creates the service-linked role for you.

If you delete this service-linked role and need to create it again, you can use
the same process to recreate the role in your account. When you configure
replication settings for your registry, Amazon ECR creates the service-linked
role for you again.

## Editing a service-linked role for Amazon ECR

Amazon ECR doesn't allow manually editing the AWSServiceRoleForECRReplication service-linked role.
After you create a service-linked role, you can't change the name of the role
because various entities might reference the role. However, you can edit the
description of the role using IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the service-linked role for

Amazon ECR

If you no longer need to use a feature or service that requires a service-linked
role, we recommend that you delete that role. That way, you don’t have an unused
entity that isn't actively monitored or maintained. However, you must remove the
replication configuration for your registry in every Region before you can manually
delete the service-linked role.

###### Note

If you try to delete resources while the Amazon ECR service is still using
the roles, your delete action might fail. If that happens, wait for a few
minutes and try again.

###### To delete Amazon ECR resources used by the AWSServiceRoleForECRReplication

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region your replication configuration
   is set on.
3. In the navigation pane, choose **Private
   registry**.
4. On the **Private registry** page, on the
   **Replication configuration** section, choose
   **Edit**.
5. To delete all of your replication rules, choose **Delete
   all**. This step requires confirmation.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the
**AWSServiceRoleForECRReplication** service-linked role. For more information, see
[Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.
