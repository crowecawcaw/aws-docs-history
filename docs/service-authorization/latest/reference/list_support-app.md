# Actions, resources, and condition keys for AWS Support App in Slack

AWS Support App in Slack (service prefix: `supportapp`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awssupport/latest/user/aws-support-app-for-slack.md "../../../awssupport/latest/user/aws-support-app-for-slack.md").
- View a list of the [API operations available for
  this service](../../../supportapp/latest/APIReference/Welcome.md "../../../supportapp/latest/APIReference/Welcome.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awssupport/latest/user/security-iam.md "../../../awssupport/latest/user/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/supportapp/supportapp.json "https://servicereference.us-east-1.amazonaws.com/v1/supportapp/supportapp.json") for this service.

###### Topics

- [API operations defined by AWS Support App in Slack](#list_support-app-operations "#list_support-app-operations")
- [Actions defined by AWS Support App in Slack](#list_support-app-actions-as-permissions "#list_support-app-actions-as-permissions")
- [Permission-only actions for AWS Support App in Slack](#list_support-app-permission-only-actions "#list_support-app-permission-only-actions")
- [Resource types defined by AWS Support App in Slack](#list_support-app-resources-for-iam-policies "#list_support-app-resources-for-iam-policies")
- [Condition keys for AWS Support App in Slack](#list_support-app-policy-keys "#list_support-app-policy-keys")

## API operations defined by AWS Support App in Slack

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_support-app-actions-as-permissions "#list_support-app-actions-as-permissions").

| Operation                                                                                                                       | IAM action                                                                                                                                                                          | Condition key            | Possible value(s) | Access level |
| ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ----------------- | ------------ |
| CreateSlackChannelConfiguration                                                                                                 | [supportapp:CreateSlackChannelConfiguration](#list_support-app-action-CreateSlackChannelConfiguration "#list_support-app-action-CreateSlackChannelConfiguration")                   |                          |                   | Write        |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                                                 | supportapp.amazonaws.com | Write             |
| DeleteAccountAlias                                                                                                              | [supportapp:DeleteAccountAlias](#list_support-app-action-DeleteAccountAlias "#list_support-app-action-DeleteAccountAlias")                                                          |                          |                   | Write        |
| DeleteSlackChannelConfiguration                                                                                                 | [supportapp:DeleteSlackChannelConfiguration](#list_support-app-action-DeleteSlackChannelConfiguration "#list_support-app-action-DeleteSlackChannelConfiguration")                   |                          |                   | Write        |
| DeleteSlackWorkspaceConfiguration                                                                                               | [supportapp:DeleteSlackWorkspaceConfiguration](#list_support-app-action-DeleteSlackWorkspaceConfiguration "#list_support-app-action-DeleteSlackWorkspaceConfiguration")             |                          |                   | Write        |
| GetAccountAlias                                                                                                                 | [supportapp:GetAccountAlias](#list_support-app-action-GetAccountAlias "#list_support-app-action-GetAccountAlias")                                                                   |                          |                   | Read         |
| ListSlackChannelConfigurations                                                                                                  | [supportapp:ListSlackChannelConfigurations](#list_support-app-action-ListSlackChannelConfigurations "#list_support-app-action-ListSlackChannelConfigurations")                      |                          |                   | Read         |
| ListSlackWorkspaceConfigurations                                                                                                | [supportapp:ListSlackWorkspaceConfigurations](#list_support-app-action-ListSlackWorkspaceConfigurations "#list_support-app-action-ListSlackWorkspaceConfigurations")                |                          |                   | Read         |
| PutAccountAlias                                                                                                                 | [supportapp:PutAccountAlias](#list_support-app-action-PutAccountAlias "#list_support-app-action-PutAccountAlias")                                                                   |                          |                   | Write        |
| RegisterSlackWorkspaceForOrganization                                                                                           | [supportapp:RegisterSlackWorkspaceForOrganization](#list_support-app-action-RegisterSlackWorkspaceForOrganization "#list_support-app-action-RegisterSlackWorkspaceForOrganization") |                          |                   | Write        |
| UpdateSlackChannelConfiguration                                                                                                 | [supportapp:UpdateSlackChannelConfiguration](#list_support-app-action-UpdateSlackChannelConfiguration "#list_support-app-action-UpdateSlackChannelConfiguration")                   |                          |                   | Write        |
| [iam:PassRole](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") | iam:PassedToService                                                                                                                                                                 | supportapp.amazonaws.com | Write             |

## Actions defined by AWS Support App in Slack

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                              | Description                                                                                        | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateSlackChannelConfiguration](../../../supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.md "../../../supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.md")                   | Grants permission to create a Slack channel configuration for your account                         |                             |                | Write        |
| [DeleteAccountAlias](../../../supportapp/latest/APIReference/API_DeleteAccountAlias.md "../../../supportapp/latest/APIReference/API_DeleteAccountAlias.md")                                                          | Grants permission to delete an alias from your account                                             |                             |                | Write        |
| [DeleteSlackChannelConfiguration](../../../supportapp/latest/APIReference/API_DeleteSlackChannelConfiguration.md "../../../supportapp/latest/APIReference/API_DeleteSlackChannelConfiguration.md")                   | Grants permission to delete a Slack channel configuration from your account                        |                             |                | Write        |
| [DeleteSlackWorkspaceConfiguration](../../../supportapp/latest/APIReference/API_DeleteSlackWorkspaceConfiguration.md "../../../supportapp/latest/APIReference/API_DeleteSlackWorkspaceConfiguration.md")             | Grants permission to delete a Slack workspace configuration from your account                      |                             |                | Write        |
| [GetAccountAlias](../../../supportapp/latest/APIReference/API_GetAccountAlias.md "../../../supportapp/latest/APIReference/API_GetAccountAlias.md")                                                                   | Grants permission to get the alias for your account                                                |                             |                | Read         |
| [ListSlackChannelConfigurations](../../../supportapp/latest/APIReference/API_ListSlackChannelConfigurations.md "../../../supportapp/latest/APIReference/API_ListSlackChannelConfigurations.md")                      | Grants permission to list all Slack channel configurations for your account                        |                             |                | Read         |
| [ListSlackWorkspaceConfigurations](../../../supportapp/latest/APIReference/API_ListSlackWorkspaceConfigurations.md "../../../supportapp/latest/APIReference/API_ListSlackWorkspaceConfigurations.md")                | Grants permission to list all Slack workspace configurations for your account                      |                             |                | Read         |
| [PutAccountAlias](../../../supportapp/latest/APIReference/API_PutAccountAlias.md "../../../supportapp/latest/APIReference/API_PutAccountAlias.md")                                                                   | Grants permission to create or update an alias for your account                                    |                             |                | Write        |
| [RegisterSlackWorkspaceForOrganization](../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md "../../../supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.md") | Grants permission to register a Slack workspace for an AWS account that is part of an organization |                             |                | Write        |
| [UpdateSlackChannelConfiguration](../../../supportapp/latest/APIReference/API_UpdateSlackChannelConfiguration.md "../../../supportapp/latest/APIReference/API_UpdateSlackChannelConfiguration.md")                   | Grants permission to update a Slack channel configuration for your account                         |                             |                | Write        |

## Permission-only actions for AWS Support App in Slack

The following actions are defined by AWS Support App in Slack but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                            | Description                                                                                                             | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [DescribeSlackChannels](../../../awssupport/latest/user/slack-authorization-permissions.md "../../../awssupport/latest/user/slack-authorization-permissions.md")   | Grants permission to list all public Slack channels in a workspace that have invited the AWS Support App                |                             |                | Read         |
| [GetSlackOauthParameters](../../../awssupport/latest/user/slack-authorization-permissions.md "../../../awssupport/latest/user/slack-authorization-permissions.md") | Grants permission to get parameters for the Slack OAuth code, which the AWS Support App uses to authorize the workspace |                             |                | Read         |
| [RedeemSlackOauthCode](../../../awssupport/latest/user/slack-authorization-permissions.md "../../../awssupport/latest/user/slack-authorization-permissions.md")    | Grants permission to redeem the Slack OAuth code, which the AWS Support App uses to authorize the workspace             |                             |                | Write        |

## Resource types defined by AWS Support App in Slack

AWS Support App in Slack does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Support App in Slack

AWS Support App in Slack has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
