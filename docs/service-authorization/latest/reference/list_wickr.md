

# Actions, resources, and condition keys for AWS Wickr
<a name="list_wickr"></a>

AWS Wickr (service prefix: `wickr`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/wickr/latest/adminguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/wickr/latest/adminguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/wickr/wickr.json) for this service.

**Topics**
+ [API operations defined by AWS Wickr](#list_wickr-operations)
+ [Actions defined by AWS Wickr](#list_wickr-actions-as-permissions)
+ [Resource types defined by AWS Wickr](#list_wickr-resources-for-iam-policies)
+ [Condition keys for AWS Wickr](#list_wickr-policy-keys)

## API operations defined by AWS Wickr
<a name="list_wickr-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_wickr-actions-as-permissions).




- **   BatchCreateUser  **
  - **IAM action:**  [wickr:BatchCreateUser](#list_wickr-action-BatchCreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDeleteUser  **
  - **IAM action:**  [wickr:BatchDeleteUser](#list_wickr-action-BatchDeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchLookupUserUname  **
  - **IAM action:**  [wickr:BatchLookupUserUname](#list_wickr-action-BatchLookupUserUname) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchReinviteUser  **
  - **IAM action:**  [wickr:BatchReinviteUser](#list_wickr-action-BatchReinviteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchResetDevicesForUser  **
  - **IAM action:**  [wickr:BatchResetDevicesForUser](#list_wickr-action-BatchResetDevicesForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchToggleUserSuspendStatus  **
  - **IAM action:**  [wickr:BatchToggleUserSuspendStatus](#list_wickr-action-BatchToggleUserSuspendStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateBot  **
  - **IAM action:**  [wickr:CreateBot](#list_wickr-action-CreateBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataRetentionBot  **
  - **IAM action:**  [wickr:CreateDataRetentionBot](#list_wickr-action-CreateDataRetentionBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataRetentionBotChallenge  **
  - **IAM action:**  [wickr:CreateDataRetentionBotChallenge](#list_wickr-action-CreateDataRetentionBotChallenge) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateNetwork  **
  - **IAM action:**  [wickr:CreateNetwork](#list_wickr-action-CreateNetwork)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [wickr:TagResource](#list_wickr-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateSecurityGroup  **
  - **IAM action:**  [wickr:CreateSecurityGroup](#list_wickr-action-CreateSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBot  **
  - **IAM action:**  [wickr:DeleteBot](#list_wickr-action-DeleteBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataRetentionBot  **
  - **IAM action:**  [wickr:DeleteDataRetentionBot](#list_wickr-action-DeleteDataRetentionBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNetwork  **
  - **IAM action:**  [wickr:DeleteNetwork](#list_wickr-action-DeleteNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSecurityGroup  **
  - **IAM action:**  [wickr:DeleteSecurityGroup](#list_wickr-action-DeleteSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetBot  **
  - **IAM action:**  [wickr:GetBot](#list_wickr-action-GetBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetBotsCount  **
  - **IAM action:**  [wickr:GetBotsCount](#list_wickr-action-GetBotsCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataRetentionBot  **
  - **IAM action:**  [wickr:GetDataRetentionBot](#list_wickr-action-GetDataRetentionBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGuestUserHistoryCount  **
  - **IAM action:**  [wickr:GetGuestUserHistoryCount](#list_wickr-action-GetGuestUserHistoryCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetwork  **
  - **IAM action:**  [wickr:GetNetwork](#list_wickr-action-GetNetwork) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNetworkSettings  **
  - **IAM action:**  [wickr:GetNetworkSettings](#list_wickr-action-GetNetworkSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOidcInfo  **
  - **IAM action:**  [wickr:GetOidcInfo](#list_wickr-action-GetOidcInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOpentdfConfig  **
  - **IAM action:**  [wickr:GetOpentdfConfig](#list_wickr-action-GetOpentdfConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSecurityGroup  **
  - **IAM action:**  [wickr:GetSecurityGroup](#list_wickr-action-GetSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUser  **
  - **IAM action:**  [wickr:GetUser](#list_wickr-action-GetUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUsersCount  **
  - **IAM action:**  [wickr:GetUsersCount](#list_wickr-action-GetUsersCount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBlockedGuestUsers  **
  - **IAM action:**  [wickr:ListBlockedGuestUsers](#list_wickr-action-ListBlockedGuestUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListBots  **
  - **IAM action:**  [wickr:ListBots](#list_wickr-action-ListBots) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDevicesForUser  **
  - **IAM action:**  [wickr:ListDevicesForUser](#list_wickr-action-ListDevicesForUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListGuestUsers  **
  - **IAM action:**  [wickr:ListGuestUsers](#list_wickr-action-ListGuestUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListNetworks  **
  - **IAM action:**  [wickr:ListNetworks](#list_wickr-action-ListNetworks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSecurityGroupUsers  **
  - **IAM action:**  [wickr:ListSecurityGroupUsers](#list_wickr-action-ListSecurityGroupUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSecurityGroups  **
  - **IAM action:**  [wickr:ListSecurityGroups](#list_wickr-action-ListSecurityGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUsers  **
  - **IAM action:**  [wickr:ListUsers](#list_wickr-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   RegisterOidcConfig  **
  - **IAM action:**  [wickr:RegisterOidcConfig](#list_wickr-action-RegisterOidcConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterOidcConfigTest  **
  - **IAM action:**  [wickr:RegisterOidcConfigTest](#list_wickr-action-RegisterOidcConfigTest) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterOpentdfConfig  **
  - **IAM action:**  [wickr:RegisterOpentdfConfig](#list_wickr-action-RegisterOpentdfConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateBot  **
  - **IAM action:**  [wickr:UpdateBot](#list_wickr-action-UpdateBot) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataRetention  **
  - **IAM action:**  [wickr:UpdateDataRetention](#list_wickr-action-UpdateDataRetention) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateGuestUser  **
  - **IAM action:**  [wickr:UpdateGuestUser](#list_wickr-action-UpdateGuestUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateNetworkSettings  **
  - **IAM action:**  [wickr:UpdateNetworkSettings](#list_wickr-action-UpdateNetworkSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSecurityGroup  **
  - **IAM action:**  [wickr:UpdateSecurityGroup](#list_wickr-action-UpdateSecurityGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateUser  **
  - **IAM action:**  [wickr:UpdateUser](#list_wickr-action-UpdateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Wickr
<a name="list_wickr-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchCreateUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch create users in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDeleteUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch delete users from a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchLookupUserUname](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch lookup user unames in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchReinviteUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch reinvite users in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchResetDevicesForUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch reset devices for a user in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchToggleUserSuspendStatus](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to batch toggle user suspend status in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAdminSession](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create and manage Wickr networks
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create a bot in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create a data retention bot in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDataRetentionBotChallenge](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create a data retention bot challenge in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateNetwork](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create a new Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wickr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wickr-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSecurityGroup](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to create a security group in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to delete a bot from a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to delete a data retention bot from a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNetwork](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to delete Wickr networks
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSecurityGroup](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to delete a security group from a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get bot information in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetBotsCount](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get bot count for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDataRetentionBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get data retention bot information in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetGuestUserHistoryCount](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get guest user history count for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetwork](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get details of a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNetworkSettings](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get network settings for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOidcInfo](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get OIDC information for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOpentdfConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_GetOpentdfConfig.html)  **
  - **Description:** Grants permission to retrieve the OpenTDF integration configuration for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSecurityGroup](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get security group information in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get information about a user in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUsersCount](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to get user count for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBlockedGuestUsers](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list blocked guest users in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListBots](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list bots in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDevicesForUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list devices for a user in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListGuestUsers](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list guest users in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListNetworks](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list Wickr networks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSecurityGroupUsers](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list users in a security group in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListSecurityGroups](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list security groups in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list the tags applied to a Wickr resource
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUsers](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to list users in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [RegisterOidcConfig](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to register OIDC configuration for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterOidcConfigTest](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to test OIDC configuration for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterOpentdfConfig](https://docs.aws.amazon.com/wickr/latest/APIReference/API_RegisterOpentdfConfig.html)  **
  - **Description:** Grants permission to register and save OpenTDF integration configuration for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to add tags to a specified Wickr resource
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_wickr-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wickr-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to untag the specified tags from the specified Wickr resource
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_wickr-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateBot](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update a bot in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataRetention](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update data retention settings in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGuestUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update guest user status in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkDetails](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update Wickr network details
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateNetworkSettings](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update network settings for a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSecurityGroup](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update a security group in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateUser](https://docs.aws.amazon.com/wickr/latest/adminguide/security-iam.html)  **
  - **Description:** Grants permission to update user information in a Wickr network
  - **Resource types (\*required):** [network\*](#list_wickr-resource-network)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Wickr
<a name="list_wickr-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [network](https://docs.aws.amazon.com/wickr/latest/adminguide/)  | arn:${Partition}:wickr:${Region}:${Account}:network/${NetworkId} | [aws:ResourceTag/${TagKey}](#list_wickr-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Wickr
<a name="list_wickr-policy-keys"></a>

AWS Wickr defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 