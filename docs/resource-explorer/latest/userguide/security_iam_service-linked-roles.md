

# Using service-linked roles for Resource Explorer
<a name="security_iam_service-linked-roles"></a>

AWS Resource Explorer uses AWS Identity and Access Management (IAM)[ service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to Resource Explorer. Service-linked roles are predefined by Resource Explorer and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes configuring Resource Explorer easier because you don’t have to manually add the necessary permissions. Resource Explorer defines the permissions of its service-linked roles, and unless defined otherwise, only Resource Explorer can assume its roles. The defined permissions include both the trust policy and the permissions policy, and that permissions policy can't be assigned to any other IAM entity.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*. There, look for the services that have **Yes **in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for Resource Explorer
<a name="slr-permissions"></a>

Resource Explorer uses the service-linked role named `AWSServiceRoleForResourceExplorer`. This role grants permissions to the Resource Explorer service to view resources and AWS CloudTrail events in your AWS account on your behalf and to index those resources to support searching.

The `AWSServiceRoleForResourceExplorer` service-linked role trusts only the service with the following service principal to assume the role:
+ `resource-explorer-2.amazonaws.com`

The role permissions policy named [AWSResourceExplorerServiceRolePolicy](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_awsmanpol.html#security_iam_awsmanpol_AWSResourceExplorerServiceRolePolicy) allows Resource Explorer read-only access to retrieve resource names and properties for supported AWS resources. To view the services and resources that Resource Explorer supports, see [Resource types you can search for with Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/supported-resource-types.html). To see the latest version of this AWS managed policy, [`AWSResourceExplorerServiceRolePolicy`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSResourceExplorerServiceRolePolicy.html) in the *AWS Managed Policy Reference Guide*. To see permission changes to this policy, see [Resource Explorer updates to AWS managed policies](security_iam_awsmanpol.md#security_iam_awsmanpol_updates). 

A principal is an IAM entity such as a user, group, or role. If you let Resource Explorer create the service-linked role for you when it creates the index in the first Region of the account, then the principal performing the task needs only the permissions required to create the Resource Explorer index. To create the service-linked role manually using IAM, then the principal performing the task must have permission to create a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for Resource Explorer
<a name="create-slr"></a>

You don't need to manually create a service-linked role. When you first access Resource Explorer with appropriate permissions, or run [CreateIndex](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_CreateIndex.html) in the first AWS Region in your account using the AWS CLI or an AWS API, Resource Explorer creates the service-linked role for you. 

If you delete this service-linked role, and then need to create it again, you can use the same process to re-create the role in your account. When you [RegisterResourceExplorer](https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_RegisterResourceExplorer.html) in the first Region in your account, Resource Explorer creates the service-linked role for you again. 

## Editing a service-linked role for Resource Explorer
<a name="edit-slr"></a>

Resource Explorer doesn't allow you to edit the `AWSServiceRoleForResourceExplorer` service-linked role. After you create a service-linked role, you can't change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for Resource Explorer
<a name="delete-slr"></a>

You can use the IAM console, the AWS CLI, or the AWS API to manually delete the service-linked role. To do this, you must first remove the Resource Explorer indexes from every AWS Region in your account and then you can manually delete the service-linked role.

**Note**  
If the Resource Explorer service is using the role when you try to delete the resources, the deletion fails. If that happens, ensure that all indexes from all Regions are deleted, then wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the `AWSServiceRoleForResourceExplorer` service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for Resource Explorer service-linked roles
<a name="slr-regions"></a>

Resource Explorer supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the *Amazon Web Services General Reference*.