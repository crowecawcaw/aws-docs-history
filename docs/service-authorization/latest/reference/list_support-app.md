

# Actions, resources, and condition keys for AWS Support App in Slack
<a name="list_support-app"></a>

AWS Support App in Slack (service prefix: `supportapp`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/supportapp/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/awssupport/latest/user/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/supportapp/supportapp.json) for this service.

**Topics**
+ [API operations defined by AWS Support App in Slack](#list_support-app-operations)
+ [Actions defined by AWS Support App in Slack](#list_support-app-actions-as-permissions)
+ [Permission-only actions for AWS Support App in Slack](#list_support-app-permission-only-actions)
+ [Resource types defined by AWS Support App in Slack](#list_support-app-resources-for-iam-policies)
+ [Condition keys for AWS Support App in Slack](#list_support-app-policy-keys)

## API operations defined by AWS Support App in Slack
<a name="list_support-app-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_support-app-actions-as-permissions).




- **   CreateSlackChannelConfiguration  **
  - **IAM action:**  [supportapp:CreateSlackChannelConfiguration](#list_support-app-action-CreateSlackChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** supportapp.amazonaws.com / **Access level:** Write

- **   DeleteAccountAlias  **
  - **IAM action:**  [supportapp:DeleteAccountAlias](#list_support-app-action-DeleteAccountAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlackChannelConfiguration  **
  - **IAM action:**  [supportapp:DeleteSlackChannelConfiguration](#list_support-app-action-DeleteSlackChannelConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlackWorkspaceConfiguration  **
  - **IAM action:**  [supportapp:DeleteSlackWorkspaceConfiguration](#list_support-app-action-DeleteSlackWorkspaceConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountAlias  **
  - **IAM action:**  [supportapp:GetAccountAlias](#list_support-app-action-GetAccountAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSlackChannelConfigurations  **
  - **IAM action:**  [supportapp:ListSlackChannelConfigurations](#list_support-app-action-ListSlackChannelConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSlackWorkspaceConfigurations  **
  - **IAM action:**  [supportapp:ListSlackWorkspaceConfigurations](#list_support-app-action-ListSlackWorkspaceConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutAccountAlias  **
  - **IAM action:**  [supportapp:PutAccountAlias](#list_support-app-action-PutAccountAlias) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterSlackWorkspaceForOrganization  **
  - **IAM action:**  [supportapp:RegisterSlackWorkspaceForOrganization](#list_support-app-action-RegisterSlackWorkspaceForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSlackChannelConfiguration  **
  - **IAM action:**  [supportapp:UpdateSlackChannelConfiguration](#list_support-app-action-UpdateSlackChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** supportapp.amazonaws.com / **Access level:** Write



## Actions defined by AWS Support App in Slack
<a name="list_support-app-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.html)  | Grants permission to create a Slack channel configuration for your account |  |   | Write | 
|   [DeleteAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteAccountAlias.html)  | Grants permission to delete an alias from your account |  |   | Write | 
|   [DeleteSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteSlackChannelConfiguration.html)  | Grants permission to delete a Slack channel configuration from your account |  |   | Write | 
|   [DeleteSlackWorkspaceConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_DeleteSlackWorkspaceConfiguration.html)  | Grants permission to delete a Slack workspace configuration from your account |  |   | Write | 
|   [GetAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_GetAccountAlias.html)  | Grants permission to get the alias for your account |  |   | Read | 
|   [ListSlackChannelConfigurations](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackChannelConfigurations.html)  | Grants permission to list all Slack channel configurations for your account |  |   | Read | 
|   [ListSlackWorkspaceConfigurations](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_ListSlackWorkspaceConfigurations.html)  | Grants permission to list all Slack workspace configurations for your account |  |   | Read | 
|   [PutAccountAlias](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_PutAccountAlias.html)  | Grants permission to create or update an alias for your account |  |   | Write | 
|   [RegisterSlackWorkspaceForOrganization](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.html)  | Grants permission to register a Slack workspace for an AWS account that is part of an organization |  |   | Write | 
|   [UpdateSlackChannelConfiguration](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_UpdateSlackChannelConfiguration.html)  | Grants permission to update a Slack channel configuration for your account |  |   | Write | 

## Permission-only actions for AWS Support App in Slack
<a name="list_support-app-permission-only-actions"></a>

The following actions are defined by AWS Support App in Slack but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [DescribeSlackChannels](https://docs.aws.amazon.com/awssupport/latest/user/slack-authorization-permissions.html)  | Grants permission to list all public Slack channels in a workspace that have invited the AWS Support App |  |   | Read | 
|   [GetSlackOauthParameters](https://docs.aws.amazon.com/awssupport/latest/user/slack-authorization-permissions.html)  | Grants permission to get parameters for the Slack OAuth code, which the AWS Support App uses to authorize the workspace |  |   | Read | 
|   [RedeemSlackOauthCode](https://docs.aws.amazon.com/awssupport/latest/user/slack-authorization-permissions.html)  | Grants permission to redeem the Slack OAuth code, which the AWS Support App uses to authorize the workspace |  |   | Write | 

## Resource types defined by AWS Support App in Slack
<a name="list_support-app-resources-for-iam-policies"></a>

AWS Support App in Slack does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Support App in Slack
<a name="list_support-app-policy-keys"></a>

AWS Support App in Slack has no service-specific condition keys that can be used in the `Condition` element of policy statements.