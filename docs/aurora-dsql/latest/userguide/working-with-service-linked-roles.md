# Using service-linked roles in Aurora DSQL

Aurora DSQL uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts"). A service-linked role is a unique type of IAM role that is linked directly to Aurora DSQL.
Service-linked roles are predefined by Aurora DSQL and include all the permissions that the service requires to call AWS services on behalf of your Aurora DSQL cluster.

Service-linked roles make the setup process easier because you don't have to manually add the necessary permissions to use Aurora DSQL. When you create a cluster, Aurora DSQL automatically
creates a service-linked role for you. You can delete the service-linked role only after you delete all of your clusters. This protects your Aurora DSQL resources because you can't inadvertently
remove permissions needed for access to the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a **Yes**
with a link to view the service-linked role documentation for that service.

Service-linked roles are available in all supported Aurora DSQL Regions.

## Service-linked role permissions for Aurora DSQL

Aurora DSQL uses the service-linked role named `AWSServiceRoleForAuroraDsql` –
Allows Amazon Aurora DSQL to create and manage AWS resources on your behalf.
This service-linked role is attached to the following managed policy: [AuroraDsqlServiceLinkedRolePolicy](../../../aws-managed-policy/latest/reference/AuroraDsqlServiceLinkedRolePolicy.md "../../../aws-managed-policy/latest/reference/AuroraDsqlServiceLinkedRolePolicy.md").

###### Note

You must configure permissions to allow an IAM entity (such as a user, group, or role) to create, edit, or delete a service-linked role. You might encounter the following error message: `You don't have the permissions to create an Amazon Aurora DSQL service-linked role`. If you see this message, make sure that you have the following permissions enabled:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": ["dsql:CreateCluster"],
 "Resource": [
 "arn:aws:dsql:us-east-1:*:cluster/*",
 "arn:aws:dsql:us-east-2:*:cluster/*"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions.html "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#service-linked-role-permissions.html").

## Create a service-linked role

You don't need to manually create an AuroraDSQLServiceLinkedRolePolicy service-linked role. Aurora DSQL creates the service-linked role for you. If the AuroraDSQLServiceLinkedRolePolicy
service-linked role has been deleted from your account, Aurora DSQL creates the role when you create a new Aurora DSQL cluster.

## Edit a service-linked role

Aurora DSQL doesn't allow you to edit the AuroraDSQLServiceLinkedRolePolicy
service-linked role. After you create a service-linked role,
you can't change the name of the role because various entities might reference the role.
However, you can edit the description of the role using the IAM console, the AWS Command Line Interface (AWS CLI), or IAM API.

## Delete a service-linked role

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way, you don't have an unused entity that is not actively monitored or maintained.

Before you can delete a service-linked role for an account, you must delete any clusters in the account.

You can use the IAM console, the AWS CLI, or the IAM API to delete a service-linked role. For more information, see
[Create a service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md#delete-service-linked-role") in the IAM User Guide.

## Supported Regions for Aurora DSQL service-linked roles

Aurora DSQL supports using service-linked roles in all of the Regions where the service
is available. For more information, see [AWS Regions and endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").
