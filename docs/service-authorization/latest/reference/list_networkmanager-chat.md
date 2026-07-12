# Actions, resources, and condition keys for AWS Network Manager Chat

AWS Network Manager Chat (service prefix: `networkmanager-chat`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../vpc/latest/reachability/what-is-reachability-analyzer.md "../../../vpc/latest/reachability/what-is-reachability-analyzer.md").
- View a list of the [API operations available for
  this service](../../../AWSEC2/latest/APIReference/Welcome.md "../../../AWSEC2/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../vpc/latest/reachability/identity-access-management.md "../../../vpc/latest/reachability/identity-access-management.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/networkmanager-chat/networkmanager-chat.json "https://servicereference.us-east-1.amazonaws.com/v1/networkmanager-chat/networkmanager-chat.json") for this service.

###### Topics

- [Actions defined by AWS Network Manager Chat](#list_networkmanager-chat-actions-as-permissions "#list_networkmanager-chat-actions-as-permissions")
- [Permission-only actions for AWS Network Manager Chat](#list_networkmanager-chat-permission-only-actions "#list_networkmanager-chat-permission-only-actions")
- [Resource types defined by AWS Network Manager Chat](#list_networkmanager-chat-resources-for-iam-policies "#list_networkmanager-chat-resources-for-iam-policies")
- [Condition keys for AWS Network Manager Chat](#list_networkmanager-chat-policy-keys "#list_networkmanager-chat-policy-keys")

## Actions defined by AWS Network Manager Chat

AWS Network Manager Chat has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Network Manager Chat

The following actions are defined by AWS Network Manager Chat but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                             | Description                                                             | Resource types (\*required) | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CancelMessageResponse](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")      | Grants permission to cancel a response to a message                     |                             |                | Write        |
| [CreateConversation](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")         | Grants permission to create a conversation                              |                             |                | Write        |
| [DeleteConversation](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")         | Grants permission to delete a conversation                              |                             |                | Write        |
| [ListConversationMessages](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")   | Grants permission to list conversation messages                         |                             |                | List         |
| [ListConversations](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")          | Grants permission to list conversations                                 |                             |                | List         |
| [NotifyConversationIsActive](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md") | Grants permission to notify whether there is activity in a conversation |                             |                | Write        |
| [SendConversationMessage](../../../vpc/latest/reachability/security_iam_required-API-permissions.md "../../../vpc/latest/reachability/security_iam_required-API-permissions.md")    | Grants permission to send a conversation message                        |                             |                | Write        |

## Resource types defined by AWS Network Manager Chat

AWS Network Manager Chat does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Network Manager Chat

AWS Network Manager Chat has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
