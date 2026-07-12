# Using Service-Linked Roles for Third-Party Cloud Integrations

## Service-Linked Role Permissions for AWS Config Third Party

AWS Config uses the service-linked role named **AWSServiceRoleForConfigThirdParty** –
Provides permissions for AWS Config to inventory and evaluate compliance of third-party cloud resources.

The AWSServiceRoleForConfigThirdParty service-linked role trusts the following services to assume the
role:

- `thirdparty.config.amazonaws.com`

The role permissions policy named **AWSConfigThirdPartyServiceRolePolicy** allows AWS Config to complete the following actions
on the specified resources:

- Action: `sts:GetWebIdentityToken` on all AWS resources, limited to
  identity token audiences that match `api://AzureADTokenExchange`
- Action: `config:PutEvaluations` on all AWS resources
- Action: `config:GetComplianceDetailsByConfigRule` on all AWS
  resources
- Action: `cloudwatch:PutMetricData` on all AWS resources, restricted
  to the `AWS/Config` namespace

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a Service-Linked Role for AWS Config Third Party

You don't need to manually create a service-linked role. When you create a third-party
connector by using the `PutConnector` API in the AWS Management Console, the AWS CLI, or the
AWS API, AWS Config creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you create a third-party
connector by using the `PutConnector` API, AWS Config creates the service-linked role
for you again.

You can also use the IAM console to create a service-linked role with the
**Config - Third Party** use case. In the AWS CLI or the AWS API, create
a service-linked role with the service name:

`thirdparty.config.amazonaws.com`

For more information, see [Creating a service-linked
role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md") in the _IAM User Guide_. If you delete this
service-linked role, you can use this same process to create the role again.

## Editing a Service-Linked Role for AWS Config Third Party

AWS Config does not allow you to edit the AWSServiceRoleForConfigThirdParty service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked
role](../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_update-service-linked-role.md") in the _IAM User Guide_.

## Deleting a Service-Linked Role for AWS Config Third Party

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

**To delete AWS Config resources used by the
AWSServiceRoleForConfigThirdParty**

- Delete all service-linked recorders that reference third-party connectors.
- Delete all third-party connectors in your account across all supported AWS
  Regions.

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForConfigThirdParty
service-linked role. For more information, see [Deleting a
service-linked role](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md") in the _IAM User Guide_.

## Supported Regions for AWSServiceRoleForConfigThirdParty role

AWS Config does not support using service-linked roles in every Region where the service is
available. You can use the AWSServiceRoleForConfigThirdParty role in the following Regions.

| Region         | Support |
| -------------- | ------- |
| af-south-1     | Yes     |
| ap-east-1      | Yes     |
| ap-east-2      | Yes     |
| ap-northeast-1 | Yes     |
| ap-northeast-2 | Yes     |
| ap-northeast-3 | Yes     |
| ap-south-1     | Yes     |
| ap-south-2     | Yes     |
| ap-southeast-1 | Yes     |
| ap-southeast-2 | Yes     |
| ap-southeast-3 | Yes     |
| ap-southeast-4 | Yes     |
| ap-southeast-5 | Yes     |
| ap-southeast-6 | Yes     |
| ap-southeast-7 | Yes     |
| ca-central-1   | Yes     |
| ca-west-1      | Yes     |
| eu-central-1   | Yes     |
| eu-central-2   | Yes     |
| eu-north-1     | Yes     |
| eu-south-1     | Yes     |
| eu-south-2     | Yes     |
| eu-west-1      | Yes     |
| eu-west-2      | Yes     |
| eu-west-3      | Yes     |
| il-central-1   | Yes     |
| mx-central-1   | Yes     |
| sa-east-1      | Yes     |
| us-east-1      | Yes     |
| us-east-2      | Yes     |
| us-west-1      | Yes     |
| us-west-2      | Yes     |
