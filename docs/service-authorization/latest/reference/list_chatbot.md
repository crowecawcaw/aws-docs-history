

# Actions, resources, and condition keys for AWS Chatbot
<a name="list_chatbot"></a>

AWS Chatbot (service prefix: `chatbot`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/chatbot/latest/adminguide/security_iam_service-with-iam-id-based-policies.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/chatbot/chatbot.json) for this service.

**Topics**
+ [API operations defined by AWS Chatbot](#list_chatbot-operations)
+ [Actions defined by AWS Chatbot](#list_chatbot-actions-as-permissions)
+ [Resource types defined by AWS Chatbot](#list_chatbot-resources-for-iam-policies)
+ [Condition keys for AWS Chatbot](#list_chatbot-policy-keys)

## API operations defined by AWS Chatbot
<a name="list_chatbot-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_chatbot-actions-as-permissions).




- **   AssociateToConfiguration  **
  - **IAM action:**  [chatbot:AssociateToConfiguration](#list_chatbot-action-AssociateToConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateChimeWebhookConfiguration  **
  - **IAM action:**  [chatbot:CreateChimeWebhookConfiguration](#list_chatbot-action-CreateChimeWebhookConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [chatbot:TagResource](#list_chatbot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write

- **   CreateCustomAction  **
  - **IAM action:**  [chatbot:CreateCustomAction](#list_chatbot-action-CreateCustomAction)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [chatbot:TagResource](#list_chatbot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateMicrosoftTeamsChannelConfiguration  **
  - **IAM action:**  [chatbot:CreateMicrosoftTeamsChannelConfiguration](#list_chatbot-action-CreateMicrosoftTeamsChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [chatbot:TagResource](#list_chatbot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write

- **   CreateSlackChannelConfiguration  **
  - **IAM action:**  [chatbot:CreateSlackChannelConfiguration](#list_chatbot-action-CreateSlackChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [chatbot:TagResource](#list_chatbot-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write

- **   DeleteChimeWebhookConfiguration  **
  - **IAM action:**  [chatbot:DeleteChimeWebhookConfiguration](#list_chatbot-action-DeleteChimeWebhookConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCustomAction  **
  - **IAM action:**  [chatbot:DeleteCustomAction](#list_chatbot-action-DeleteCustomAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMicrosoftTeamsChannelConfiguration  **
  - **IAM action:**  [chatbot:DeleteMicrosoftTeamsChannelConfiguration](#list_chatbot-action-DeleteMicrosoftTeamsChannelConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMicrosoftTeamsConfiguredTeam  **
  - **IAM action:**  [chatbot:DeleteMicrosoftTeamsConfiguredTeam](#list_chatbot-action-DeleteMicrosoftTeamsConfiguredTeam) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMicrosoftTeamsUserIdentity  **
  - **IAM action:**  [chatbot:DeleteMicrosoftTeamsUserIdentity](#list_chatbot-action-DeleteMicrosoftTeamsUserIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlackChannelConfiguration  **
  - **IAM action:**  [chatbot:DeleteSlackChannelConfiguration](#list_chatbot-action-DeleteSlackChannelConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlackUserIdentity  **
  - **IAM action:**  [chatbot:DeleteSlackUserIdentity](#list_chatbot-action-DeleteSlackUserIdentity) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSlackWorkspaceAuthorization  **
  - **IAM action:**  [chatbot:DeleteSlackWorkspaceAuthorization](#list_chatbot-action-DeleteSlackWorkspaceAuthorization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeChimeWebhookConfigurations  **
  - **IAM action:**  [chatbot:DescribeChimeWebhookConfigurations](#list_chatbot-action-DescribeChimeWebhookConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSlackChannelConfigurations  **
  - **IAM action:**  [chatbot:DescribeSlackChannelConfigurations](#list_chatbot-action-DescribeSlackChannelConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSlackUserIdentities  **
  - **IAM action:**  [chatbot:DescribeSlackUserIdentities](#list_chatbot-action-DescribeSlackUserIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSlackWorkspaces  **
  - **IAM action:**  [chatbot:DescribeSlackWorkspaces](#list_chatbot-action-DescribeSlackWorkspaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateFromConfiguration  **
  - **IAM action:**  [chatbot:DisassociateFromConfiguration](#list_chatbot-action-DisassociateFromConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountPreferences  **
  - **IAM action:**  [chatbot:GetAccountPreferences](#list_chatbot-action-GetAccountPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCustomAction  **
  - **IAM action:**  [chatbot:GetCustomAction](#list_chatbot-action-GetCustomAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMicrosoftTeamsChannelConfiguration  **
  - **IAM action:**  [chatbot:GetMicrosoftTeamsChannelConfiguration](#list_chatbot-action-GetMicrosoftTeamsChannelConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssociations  **
  - **IAM action:**  [chatbot:ListAssociations](#list_chatbot-action-ListAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCustomActions  **
  - **IAM action:**  [chatbot:ListCustomActions](#list_chatbot-action-ListCustomActions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMicrosoftTeamsChannelConfigurations  **
  - **IAM action:**  [chatbot:ListMicrosoftTeamsChannelConfigurations](#list_chatbot-action-ListMicrosoftTeamsChannelConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMicrosoftTeamsConfiguredTeams  **
  - **IAM action:**  [chatbot:ListMicrosoftTeamsConfiguredTeams](#list_chatbot-action-ListMicrosoftTeamsConfiguredTeams) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMicrosoftTeamsUserIdentities  **
  - **IAM action:**  [chatbot:ListMicrosoftTeamsUserIdentities](#list_chatbot-action-ListMicrosoftTeamsUserIdentities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [chatbot:ListTagsForResource](#list_chatbot-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [chatbot:TagResource](#list_chatbot-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [chatbot:UntagResource](#list_chatbot-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAccountPreferences  **
  - **IAM action:**  [chatbot:UpdateAccountPreferences](#list_chatbot-action-UpdateAccountPreferences) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateChimeWebhookConfiguration  **
  - **IAM action:**  [chatbot:UpdateChimeWebhookConfiguration](#list_chatbot-action-UpdateChimeWebhookConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write

- **   UpdateCustomAction  **
  - **IAM action:**  [chatbot:UpdateCustomAction](#list_chatbot-action-UpdateCustomAction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMicrosoftTeamsChannelConfiguration  **
  - **IAM action:**  [chatbot:UpdateMicrosoftTeamsChannelConfiguration](#list_chatbot-action-UpdateMicrosoftTeamsChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write

- **   UpdateSlackChannelConfiguration  **
  - **IAM action:**  [chatbot:UpdateSlackChannelConfiguration](#list_chatbot-action-UpdateSlackChannelConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** chatbot.amazonaws.com / **Access level:** Write



## Actions defined by AWS Chatbot
<a name="list_chatbot-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateToConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_AssociateToConfiguration.html)  **
  - **Description:** Grants permission to associate a resource with a configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom-action\*](#list_chatbot-resource-custom-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateChimeWebhookConfiguration.html)  **
  - **Description:** Grants permission to create an AWS Chatbot Chime Webhook Configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateCustomAction.html)  **
  - **Description:** Grants permission to create a custom action
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateMicrosoftTeamsChannelConfiguration.html)  **
  - **Description:** Grants permission to create an AWS Chatbot Microsoft Teams Channel Configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Write

- **   [CreateSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_CreateSlackChannelConfiguration.html)  **
  - **Description:** Grants permission to create an AWS Chatbot Slack Channel Configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteChimeWebhookConfiguration.html)  **
  - **Description:** Grants permission to delete an AWS Chatbot Chime Webhook Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteCustomAction.html)  **
  - **Description:** Grants permission to delete a custom action
  - **Resource types (\*required):** [custom-action\*](#list_chatbot-resource-custom-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsChannelConfiguration.html)  **
  - **Description:** Grants permission to delete an AWS Chatbot Microsoft Teams Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMicrosoftTeamsConfiguredTeam](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsConfiguredTeam.html)  **
  - **Description:** Grants permission to delete the Microsoft Teams configured with AWS Chatbot in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMicrosoftTeamsUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteMicrosoftTeamsUserIdentity.html)  **
  - **Description:** Grants permission to delete an AWS Chatbot Microsoft Teams User Identity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackChannelConfiguration.html)  **
  - **Description:** Grants permission to delete an AWS Chatbot Slack Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteSlackUserIdentity](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackUserIdentity.html)  **
  - **Description:** Grants permission to delete an AWS Chatbot Slack User Identity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSlackWorkspaceAuthorization](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DeleteSlackWorkspaceAuthorization.html)  **
  - **Description:** Grants permission to delete the Slack workspace authorization with AWS Chatbot, associated with an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeChimeWebhookConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeChimeWebhookConfigurations.html)  **
  - **Description:** Grants permission to list all AWS Chatbot Chime Webhook Configurations in an AWS Account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSlackChannelConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackChannelConfigurations.html)  **
  - **Description:** Grants permission to list all AWS Chatbot Slack Channel Configurations in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSlackChannels](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)  **
  - **Description:** Grants permission to list all public Slack channels in the Slack workspace connected to the AWS Account onboarded with AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSlackUserIdentities](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackUserIdentities.html)  **
  - **Description:** Grants permission to describe AWS Chatbot Slack User Identities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeSlackWorkspaces](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DescribeSlackWorkspaces.html)  **
  - **Description:** Grants permission to list all authorized Slack workspaces connected to the AWS Account onboarded with AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateFromConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_DisassociateFromConfiguration.html)  **
  - **Description:** Grants permission to disassociate a resource from a configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [custom-action\*](#list_chatbot-resource-custom-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccountPreferences](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetAccountPreferences.html)  **
  - **Description:** Grants permission to retrieve AWS Chatbot account preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetCustomAction.html)  **
  - **Description:** Grants permission to get a custom action
  - **Resource types (\*required):** [custom-action\*](#list_chatbot-resource-custom-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_GetMicrosoftTeamsChannelConfiguration.html)  **
  - **Description:** Grants permission to get a single AWS Chatbot Microsoft Teams Channel Configurations in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMicrosoftTeamsOauthParameters](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)  **
  - **Description:** Grants permission to generate OAuth parameters to request Microsoft Teams OAuth code to be used by the AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSlackOauthParameters](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)  **
  - **Description:** Grants permission to generate OAuth parameters to request Slack OAuth code to be used by the AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAssociations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListAssociations.html)  **
  - **Description:** Grants permission to list resources associated with a configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCustomActions](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListCustomActions.html)  **
  - **Description:** Grants permission to list custom actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMicrosoftTeamsChannelConfigurations](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsChannelConfigurations.html)  **
  - **Description:** Grants permission to list all AWS Chatbot Microsoft Teams Channel Configurations in an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMicrosoftTeamsConfiguredTeams](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsConfiguredTeams.html)  **
  - **Description:** Grants permission to list all Microsoft Teams connected to the AWS Account onboarded with AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListMicrosoftTeamsUserIdentities](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListMicrosoftTeamsUserIdentities.html)  **
  - **Description:** Grants permission to describe AWS Chatbot Microsoft Teams User Identities
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to List all tags associated with the AWS Chatbot Channel Configuration
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [RedeemMicrosoftTeamsOauthCode](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)  **
  - **Description:** Grants permission to redeem previously generated parameters with Microsoft APIs, to acquire OAuth tokens to be used by the AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RedeemSlackOauthCode](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_Operations.html)  **
  - **Description:** Grants permission to redeem previously generated parameters with Slack API, to acquire OAuth tokens to be used by the AWS Chatbot service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to create tags on AWS Chatbot Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration](#list_chatbot-resource-ChatbotConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Resource types (\*required):** [custom-action](#list_chatbot-resource-custom-action) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_chatbot-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags on AWS Chatbot Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration](#list_chatbot-resource-ChatbotConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Resource types (\*required):** [custom-action](#list_chatbot-resource-custom-action) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_chatbot-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAccountPreferences](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateAccountPreferences.html)  **
  - **Description:** Grants permission to update AWS Chatbot account preferences
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateChimeWebhookConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateChimeWebhookConfiguration.html)  **
  - **Description:** Grants permission to update an AWS Chatbot Chime Webhook Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateCustomAction](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateCustomAction.html)  **
  - **Description:** Grants permission to update a custom action
  - **Resource types (\*required):** [custom-action\*](#list_chatbot-resource-custom-action)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMicrosoftTeamsChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateMicrosoftTeamsChannelConfiguration.html)  **
  - **Description:** Grants permission to update an AWS Chatbot Microsoft Teams Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSlackChannelConfiguration](https://docs.aws.amazon.com/chatbot/latest/APIReference/API_UpdateSlackChannelConfiguration.html)  **
  - **Description:** Grants permission to update an AWS Chatbot Slack Channel Configuration
  - **Resource types (\*required):** [ChatbotConfiguration\*](#list_chatbot-resource-ChatbotConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Chatbot
<a name="list_chatbot-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [ChatbotConfiguration](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html)  | arn:${Partition}:chatbot::${Account}:chat-configuration/${ConfigurationType}/${ChatbotConfigurationName} | [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_) | 
|  [custom-action](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html)  | arn:${Partition}:chatbot::${Account}:custom-action/${ActionName} | [aws:ResourceTag/${TagKey}](#list_chatbot-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Chatbot
<a name="list_chatbot-policy-keys"></a>

AWS Chatbot defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 