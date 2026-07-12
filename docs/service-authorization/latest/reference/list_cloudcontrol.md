# Actions, resources, and condition keys for AWS Cloud Control API

AWS Cloud Control API (service prefix: `cloudformation`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md "../../../cloudcontrolapi/latest/userguide/what-is-cloudcontrolapi.md").
- View a list of the [API operations available for
  this service](../../../cloudcontrolapi/latest/APIReference/Welcome.md "../../../cloudcontrolapi/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../cloudcontrolapi/latest/userguide/security.md "../../../cloudcontrolapi/latest/userguide/security.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/cloudformation/cloudformation.json "https://servicereference.us-east-1.amazonaws.com/v1/cloudformation/cloudformation.json") for this service.

###### Topics

- [API operations defined by AWS Cloud Control API](#list_cloudcontrol-operations "#list_cloudcontrol-operations")
- [Actions defined by AWS Cloud Control API](#list_cloudcontrol-actions-as-permissions "#list_cloudcontrol-actions-as-permissions")
- [Resource types defined by AWS Cloud Control API](#list_cloudcontrol-resources-for-iam-policies "#list_cloudcontrol-resources-for-iam-policies")
- [Condition keys for AWS Cloud Control API](#list_cloudcontrol-policy-keys "#list_cloudcontrol-policy-keys")

## API operations defined by AWS Cloud Control API

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_cloudcontrol-actions-as-permissions "#list_cloudcontrol-actions-as-permissions").

| Operation                                                                                                                       | IAM action                                                                                                                                         | Condition key                | Possible value(s) | Access level |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ----------------- | ------------ |
| CancelResourceRequest                                                                                                           | [cloudformation:CancelResourceRequest](#list_cloudcontrol-action-CancelResourceRequest "#list_cloudcontrol-action-CancelResourceRequest")          |                              |                   | Write        |
| CreateResource                                                                                                                  | [cloudformation:CreateResource](#list_cloudcontrol-action-CreateResource "#list_cloudcontrol-action-CreateResource")                               |                              |                   | Write        |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                | cloudformation.amazonaws.com | Write             |
| DeleteResource                                                                                                                  | [cloudformation:DeleteResource](#list_cloudcontrol-action-DeleteResource "#list_cloudcontrol-action-DeleteResource")                               |                              |                   | Write        |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                | cloudformation.amazonaws.com | Write             |
| GetResource                                                                                                                     | [cloudformation:GetResource](#list_cloudcontrol-action-GetResource "#list_cloudcontrol-action-GetResource")                                        |                              |                   | Read         |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                | cloudformation.amazonaws.com | Write             |
| GetResourceRequestStatus                                                                                                        | [cloudformation:GetResourceRequestStatus](#list_cloudcontrol-action-GetResourceRequestStatus "#list_cloudcontrol-action-GetResourceRequestStatus") |                              |                   | Read         |
| ListResourceRequests                                                                                                            | [cloudformation:ListResourceRequests](#list_cloudcontrol-action-ListResourceRequests "#list_cloudcontrol-action-ListResourceRequests")             |                              |                   | Read         |
| ListResources                                                                                                                   | [cloudformation:ListResources](#list_cloudcontrol-action-ListResources "#list_cloudcontrol-action-ListResources")                                  |                              |                   | Read         |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                | cloudformation.amazonaws.com | Write             |
| UpdateResource                                                                                                                  | [cloudformation:UpdateResource](#list_cloudcontrol-action-UpdateResource "#list_cloudcontrol-action-UpdateResource")                               |                              |                   | Write        |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                | cloudformation.amazonaws.com | Write             |

## Actions defined by AWS Cloud Control API

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                 | Description                                                   | Resource types (\*required) | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CancelResourceRequest](../../../cloudcontrolapi/latest/APIReference/API_CancelResourceRequest.md "../../../cloudcontrolapi/latest/APIReference/API_CancelResourceRequest.md")          | Grants permission to cancel resource requests in your account |                             |                | Write        |
| [CreateResource](../../../cloudcontrolapi/latest/APIReference/API_CreateResource.md "../../../cloudcontrolapi/latest/APIReference/API_CreateResource.md")                               | Grants permission to create resources in your account         |                             |                | Write        |
| [DeleteResource](../../../cloudcontrolapi/latest/APIReference/API_DeleteResource.md "../../../cloudcontrolapi/latest/APIReference/API_DeleteResource.md")                               | Grants permission to delete resources in your account         |                             |                | Write        |
| [GetResource](../../../cloudcontrolapi/latest/APIReference/API_GetResource.md "../../../cloudcontrolapi/latest/APIReference/API_GetResource.md")                                        | Grants permission to get resources in your account            |                             |                | Read         |
| [GetResourceRequestStatus](../../../cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.md "../../../cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.md") | Grants permission to get resource requests in your account    |                             |                | Read         |
| [ListResourceRequests](../../../cloudcontrolapi/latest/APIReference/API_ListResourceRequests.md "../../../cloudcontrolapi/latest/APIReference/API_ListResourceRequests.md")             | Grants permission to list resource requests in your account   |                             |                | Read         |
| [ListResources](../../../cloudcontrolapi/latest/APIReference/API_ListResources.md "../../../cloudcontrolapi/latest/APIReference/API_ListResources.md")                                  | Grants permission to list resources in your account           |                             |                | Read         |
| [UpdateResource](../../../cloudcontrolapi/latest/APIReference/API_UpdateResource.md "../../../cloudcontrolapi/latest/APIReference/API_UpdateResource.md")                               | Grants permission to update resources in your account         |                             |                | Write        |

## Resource types defined by AWS Cloud Control API

AWS Cloud Control API does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Cloud Control API

AWS Cloud Control API has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
