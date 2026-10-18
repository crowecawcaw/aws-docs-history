

# Using service-linked roles for AWS Transfer Family
<a name="using-service-linked-roles"></a>

AWS Transfer Family uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Transfer Family. Service-linked roles are predefined by Transfer Family and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up Transfer Family easier because you don't have to manually add the necessary permissions. Transfer Family defines the permissions of its service-linked roles, and unless defined otherwise, only Transfer Family can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy can't be attached to any other IAM entity.

You can delete a service-linked role only after first deleting its related resources. This protects your Transfer Family resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have *Yes* in the *Service-linked role* column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for AWS Transfer Family
<a name="slr-permissions"></a>

AWS Transfer Family uses the service-linked role named **AWSServiceRoleForTransfer** – Allows Transfer Family to integrate with other AWS services on your behalf.

The AWSServiceRoleForTransfer service-linked role trusts the following services to assume the role:
+ `transfer.amazonaws.com`

The role permissions policy named `AWSTransferServiceRolePolicy` allows Transfer Family to complete the following actions on the specified resources:
+ `secretsmanager:BatchGetSecretValue` and `secretsmanager:ListSecrets` on secrets in the same AWS account as the calling principal – Lets Transfer Family discover and read the host key secrets that it manages in AWS Secrets Manager.
+ `secretsmanager:DescribeSecret` and `secretsmanager:GetSecretValue` on Transfer Family managed secrets (secrets with an ARN that matches `arn:*:secretsmanager:*:*:secret:transfer!*` and the `aws:secretsmanager:owningService` tag value `transfer`) – Lets Transfer Family retrieve SFTP host key material to serve to incoming connections.
+ `secretsmanager:DeleteSecret` on Transfer Family managed secrets (the same `transfer!` ARN and tag scope) – Lets Transfer Family clean up orphaned secrets that are no longer associated with a Transfer Family host key resource.

These are managed secrets: only Transfer Family can create them, and their names include the `transfer!` prefix that identifies Transfer Family as the managing service. For more information, see [AWS Secrets Manager secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS Transfer Family
<a name="create-slr"></a>

You don't need to manually create a service-linked role. Transfer Family creates the service-linked role for you when you create a server, import a host key, or update a host key that uses AWS Secrets Manager storage. This applies whether you use the AWS Management Console, the AWS CLI, or the AWS API.

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a server, import a host key, or update a host key that uses AWS Secrets Manager storage, Transfer Family creates the service-linked role for you again.

You can also use the IAM console to create a service-linked role with the **Transfer** use case. In the IAM CLI or the IAM API, create a service-linked role with the `transfer.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*.

## Editing a service-linked role for AWS Transfer Family
<a name="edit-slr"></a>

AWS Transfer Family does not allow you to edit the AWSServiceRoleForTransfer service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Transfer Family
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don't have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

To delete the Transfer Family resources used by the AWSServiceRoleForTransfer role, complete the following steps.

1. Delete the host keys that use AWS Secrets Manager storage from your Transfer Family servers, or delete the servers that use them. Removing these resources also removes the AWS Secrets Manager secrets that the service-linked role manages. For more information, see [Delete a server host key](server-host-key-delete.md).

1. After the resources are cleaned up, use IAM to delete the service-linked role, as described in the following section.

**To manually delete the service-linked role using IAM**

Use the IAM console, the IAM CLI, or the IAM API to delete the AWSServiceRoleForTransfer service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS Transfer Family service-linked roles
<a name="slr-regions"></a>

AWS Transfer Family supports using service-linked roles in all of the AWS Regions where the service is available. For more information, see [AWS Transfer Family endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/transfer-service.html).