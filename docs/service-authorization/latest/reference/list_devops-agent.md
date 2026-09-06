

# Actions, resources, and condition keys for AWS DevOps Agent Service
<a name="list_devops-agent"></a>

AWS DevOps Agent Service (service prefix: `aidevops`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/devopsagent/latest/userguide/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/devopsagent/latest/userguide/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/devopsagent/latest/userguide/aws-devops-agent-security-devops-agent-iam-permissions.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aidevops/aidevops.json) for this service.

**Topics**
+ [API operations defined by AWS DevOps Agent Service](#list_devops-agent-operations)
+ [Actions defined by AWS DevOps Agent Service](#list_devops-agent-actions-as-permissions)
+ [Permission-only actions for AWS DevOps Agent Service](#list_devops-agent-permission-only-actions)
+ [Resource types defined by AWS DevOps Agent Service](#list_devops-agent-resources-for-iam-policies)
+ [Condition keys for AWS DevOps Agent Service](#list_devops-agent-policy-keys)

## API operations defined by AWS DevOps Agent Service
<a name="list_devops-agent-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_devops-agent-actions-as-permissions).




- **   AssociateService  **
  - **IAM action:**  [aidevops:AssociateService](#list_devops-agent-action-AssociateService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aidevops.amazonaws.com / **Access level:** Write

- **   CreateAgentSpace  **
  - **IAM action:**  [aidevops:CreateAgentSpace](#list_devops-agent-action-CreateAgentSpace)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aidevops:TagResource](#list_devops-agent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePrivateConnection  **
  - **IAM action:**  [aidevops:CreatePrivateConnection](#list_devops-agent-action-CreatePrivateConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aidevops:TagResource](#list_devops-agent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAgentSpace  **
  - **IAM action:**  [aidevops:DeleteAgentSpace](#list_devops-agent-action-DeleteAgentSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePrivateConnection  **
  - **IAM action:**  [aidevops:DeletePrivateConnection](#list_devops-agent-action-DeletePrivateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterService  **
  - **IAM action:**  [aidevops:DeregisterService](#list_devops-agent-action-DeregisterService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribePrivateConnection  **
  - **IAM action:**  [aidevops:DescribePrivateConnection](#list_devops-agent-action-DescribePrivateConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisableOperatorApp  **
  - **IAM action:**  [aidevops:DisableOperatorApp](#list_devops-agent-action-DisableOperatorApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateService  **
  - **IAM action:**  [aidevops:DisassociateService](#list_devops-agent-action-DisassociateService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableOperatorApp  **
  - **IAM action:**  [aidevops:EnableOperatorApp](#list_devops-agent-action-EnableOperatorApp)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aidevops.amazonaws.com / **Access level:** Write

- **   GetAgentSpace  **
  - **IAM action:**  [aidevops:GetAgentSpace](#list_devops-agent-action-GetAgentSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAssociation  **
  - **IAM action:**  [aidevops:GetAssociation](#list_devops-agent-action-GetAssociation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOperatorApp  **
  - **IAM action:**  [aidevops:GetOperatorApp](#list_devops-agent-action-GetOperatorApp) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetService  **
  - **IAM action:**  [aidevops:GetService](#list_devops-agent-action-GetService) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAgentSpaces  **
  - **IAM action:**  [aidevops:ListAgentSpaces](#list_devops-agent-action-ListAgentSpaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociations  **
  - **IAM action:**  [aidevops:ListAssociations](#list_devops-agent-action-ListAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPrivateConnections  **
  - **IAM action:**  [aidevops:ListPrivateConnections](#list_devops-agent-action-ListPrivateConnections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServices  **
  - **IAM action:**  [aidevops:ListServices](#list_devops-agent-action-ListServices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [aidevops:ListTagsForResource](#list_devops-agent-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWebhooks  **
  - **IAM action:**  [aidevops:ListWebhooks](#list_devops-agent-action-ListWebhooks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RegisterService  **
  - **IAM action:**  [aidevops:RegisterService](#list_devops-agent-action-RegisterService)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [aidevops:TagResource](#list_devops-agent-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aidevops.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [aidevops:TagResource](#list_devops-agent-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [aidevops:UntagResource](#list_devops-agent-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAgentSpace  **
  - **IAM action:**  [aidevops:UpdateAgentSpace](#list_devops-agent-action-UpdateAgentSpace) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateAssociation  **
  - **IAM action:**  [aidevops:UpdateAssociation](#list_devops-agent-action-UpdateAssociation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** aidevops.amazonaws.com / **Access level:** Write

- **   UpdateOperatorAppIdpConfig  **
  - **IAM action:**  [aidevops:UpdateOperatorAppIdpConfig](#list_devops-agent-action-UpdateOperatorAppIdpConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePrivateConnectionCertificate  **
  - **IAM action:**  [aidevops:UpdatePrivateConnectionCertificate](#list_devops-agent-action-UpdatePrivateConnectionCertificate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ValidateAwsAssociations  **
  - **IAM action:**  [aidevops:ValidateAwsAssociations](#list_devops-agent-action-ValidateAwsAssociations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS DevOps Agent Service
<a name="list_devops-agent-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateService](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_AssociateService.html)  **
  - **Description:** Grants permission to associate service
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAccessToken](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateAccessToken.html)  **
  - **Description:** Grants permission to create an access token
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAgentSpace](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateAgentSpace.html)  **
  - **Description:** Grants permission to create agentspace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAsset](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateAsset.html)  **
  - **Description:** Grants permission to create an asset
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateAssetFile](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateAssetFile.html)  **
  - **Description:** Grants permission to create an asset file
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateBacklogTask](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateBacklogTask.html)  **
  - **Description:** Grants permission to create a new backlog task
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateChat](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateChat.html)  **
  - **Description:** Grants permission to create a chat
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateKnowledgeItem](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateKnowledgeItem.html)  **
  - **Description:** Grants permission to create a new knowledge item
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOneTimeLoginSession](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to generate secure one-time session for initiating off-console Application login
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePrivateConnection](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreatePrivateConnection.html)  **
  - **Description:** Grants permission to create a private connection
  - **Resource types (\*required):** [private-connection\*](#list_devops-agent-resource-private-connection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTrigger](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_CreateTrigger.html)  **
  - **Description:** Grants permission to create a trigger
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAgentSpace](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeleteAgentSpace.html)  **
  - **Description:** Grants permission to delete agentspace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAsset](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeleteAsset.html)  **
  - **Description:** Grants permission to delete an asset
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssetFile](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeleteAssetFile.html)  **
  - **Description:** Grants permission to delete an asset file
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteKnowledgeItem](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to delete a knowledge item
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePrivateConnection](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeletePrivateConnection.html)  **
  - **Description:** Grants permission to delete a private connection
  - **Resource types (\*required):** [private-connection\*](#list_devops-agent-resource-private-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTrigger](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeleteTrigger.html)  **
  - **Description:** Grants permission to delete a trigger
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeregisterService](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DeregisterService.html)  **
  - **Description:** Grants permission to deregister a service
  - **Resource types (\*required):** [service\*](#list_devops-agent-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribePrivateConnection](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DescribePrivateConnection.html)  **
  - **Description:** Grants permission to describe a private connection
  - **Resource types (\*required):** [private-connection\*](#list_devops-agent-resource-private-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeServices](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to describe support services
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSupportLevel](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to describe customer support level
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisableOperatorApp](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DisableOperatorApp.html)  **
  - **Description:** Grants permission to disable the Operator App access to the given AgentSpace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateService](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_DisassociateService.html)  **
  - **Description:** Grants permission to disassociate service
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [associations\*](#list_devops-agent-resource-associations) / **Condition keys:**  
  - **Access level:** Write

- **   [DiscoverTopology](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to discover topology information
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EnableOperatorApp](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_EnableOperatorApp.html)  **
  - **Description:** Grants permission to enable the Operator App to access the given AgentSpace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [EndChatForCase](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to end a chat for a case
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetAccessToken](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAccessToken.html)  **
  - **Description:** Grants permission to get access token details
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAccountUsage](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAccountUsage.html)  **
  - **Description:** Grants permission to retrieve account usage information
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAgentSpace](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAgentSpace.html)  **
  - **Description:** Grants permission to get agentspace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAsset](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAsset.html)  **
  - **Description:** Grants permission to get an asset
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssetContent](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAssetContent.html)  **
  - **Description:** Grants permission to get asset content
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssetFile](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAssetFile.html)  **
  - **Description:** Grants permission to get an asset file
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAssociation](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetAssociation.html)  **
  - **Description:** Grants permission to get association
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [associations\*](#list_devops-agent-resource-associations) / **Condition keys:**  
  - **Access level:** Read

- **   [GetBacklogTask](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetBacklogTask.html)  **
  - **Description:** Grants permission to get a backlog task
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetKnowledgeItem](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to get a knowledge item
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOperatorApp](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetOperatorApp.html)  **
  - **Description:** Grants permission to get operator auth config for any enabled auth flow
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRecommendation](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetRecommendation.html)  **
  - **Description:** Grants permission to get a recommendation
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetService](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetService.html)  **
  - **Description:** Grants permission to get services
  - **Resource types (\*required):** [service\*](#list_devops-agent-resource-service)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTrigger](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_GetTrigger.html)  **
  - **Description:** Grants permission to get a trigger
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InitiateChatForCase](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to initiate a chat for a case
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListAccessTokens](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAccessTokens.html)  **
  - **Description:** Grants permission to list access tokens
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAgentSpaces](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAgentSpaces.html)  **
  - **Description:** Grants permission to list agentspace
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetFiles](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssetFiles.html)  **
  - **Description:** Grants permission to list asset files
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssetTypes](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssetTypes.html)  **
  - **Description:** Grants permission to list asset types
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetVersions](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssetVersions.html)  **
  - **Description:** Grants permission to list asset versions
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssets](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssets.html)  **
  - **Description:** Grants permission to list assets
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociations](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListAssociations.html)  **
  - **Description:** Grants permission to list associations
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBacklogTasks](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListBacklogTasks.html)  **
  - **Description:** Grants permission to list backlog tasks
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListChats](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListChats.html)  **
  - **Description:** Grants permission to list chats
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListExecutions](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListExecutions.html)  **
  - **Description:** Grants permission to list executions
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListGoals](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListGoals.html)  **
  - **Description:** Grants permission to list goals
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListJournalRecords](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListJournalRecords.html)  **
  - **Description:** Grants permission to list journal records
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKnowledgeItemVersions](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to list knowledge item versions
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListKnowledgeItems](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to list knowledge items
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPendingMessages](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListPendingMessages.html)  **
  - **Description:** Grants permission to list pending messages
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPrivateConnections](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListPrivateConnections.html)  **
  - **Description:** Grants permission to list private connections
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRecommendations](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListRecommendations.html)  **
  - **Description:** Grants permission to list recommendations
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListServices](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListServices.html)  **
  - **Description:** Grants permission to list services
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [agentspace](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [private-connection](#list_devops-agent-resource-private-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_devops-agent-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Read

- **   [ListTriggers](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListTriggers.html)  **
  - **Description:** Grants permission to list triggers
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWebhooks](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ListWebhooks.html)  **
  - **Description:** Grants permission to list webhooks for association
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [associations\*](#list_devops-agent-resource-associations) / **Condition keys:**  
  - **Access level:** List

- **   [RegisterService](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RegisterService.html)  **
  - **Description:** Grants permission to register specific service
  - **Resource types (\*required):** [service\*](#list_devops-agent-resource-service)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Write

- **   [RevokeAccessToken](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RevokeAccessToken.html)  **
  - **Description:** Grants permission to revoke an access token
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RotateAccessToken](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_RotateAccessToken.html)  **
  - **Description:** Grants permission to rotate an access token
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchServiceAccessibleResource](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to look up a registered service accessible resources
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SendMessage](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_SendMessage.html)  **
  - **Description:** Grants permission to send chat messages
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [agentspace](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [private-connection](#list_devops-agent-resource-private-connection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_devops-agent-resource-service) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_devops-agent-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [agentspace](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [private-connection](#list_devops-agent-resource-private-connection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Resource types (\*required):** [service](#list_devops-agent-resource-service) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_devops-agent-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAgentSpace](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateAgentSpace.html)  **
  - **Description:** Grants permission to update agentspace
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApprovalAction](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateApprovalAction.html)  **
  - **Description:** Grants permission to update an approval action (approve or reject) for an agent tool invocation
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAsset](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateAsset.html)  **
  - **Description:** Grants permission to update an asset
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssetFile](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateAssetFile.html)  **
  - **Description:** Grants permission to update an asset file
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateAssociation](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateAssociation.html)  **
  - **Description:** Grants permission to update association
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [associations\*](#list_devops-agent-resource-associations) / **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBacklogTask](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateBacklogTask.html)  **
  - **Description:** Grants permission to update a task
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateGoal](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateGoal.html)  **
  - **Description:** Grants permission to update a goal
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateKnowledgeItem](https://docs.aws.amazon.com/devopsagent/latest/APIReference/what-is.html)  **
  - **Description:** Grants permission to update a knowledge item
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateOperatorAppIdpConfig](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateOperatorAppIdpConfig.html)  **
  - **Description:** Grants permission to update the external Identity Provider configuration for the Operator App
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePrivateConnectionCertificate](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdatePrivateConnectionCertificate.html)  **
  - **Description:** Grants permission to update a private connection certificate
  - **Resource types (\*required):** [private-connection\*](#list_devops-agent-resource-private-connection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRecommendation](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateRecommendation.html)  **
  - **Description:** Grants permission to update a recommendation
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTrigger](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_UpdateTrigger.html)  **
  - **Description:** Grants permission to update a trigger
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ValidateAwsAssociations](https://docs.aws.amazon.com/devopsagent/latest/APIReference/API_ValidateAwsAssociations.html)  **
  - **Description:** Grants permission to validate aws association
  - **Resource types (\*required):** [agentspace\*](#list_devops-agent-resource-agentspace)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS DevOps Agent Service
<a name="list_devops-agent-permission-only-actions"></a>

The following actions are defined by AWS DevOps Agent Service but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AllowVendedLogDeliveryForResource](https://docs.aws.amazon.com/devopsagent/latest/userguide/configuring-capabilities-for-aws-devops-agent-vended-logs-and-metrics.html)  | Grants permission to authorize vended logs |  |   | Permissions management, Write | 

## Resource types defined by AWS DevOps Agent Service
<a name="list_devops-agent-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [agentspace](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:agentspace/${AgentSpaceId} | [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_) | 
|  [asset](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:agentspace/${AgentSpaceId}/asset/${AssetId} |   | 
|  [associations](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:agentspace/${AgentSpaceId}/association/${AssociationId} |   | 
|  [private-connection](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:private-connection/${Name} | [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_) | 
|  [service](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:service/${ServiceId} | [aws:ResourceTag/${TagKey}](#list_devops-agent-aws_ResourceTag___TagKey_) | 
|  [trigger](https://docs.aws.amazon.com/devopsagent/latest/userguide/)  | arn:${Partition}:aidevops:${Region}:${Account}:agentspace/${AgentSpaceId}/trigger/${TriggerId} |   | 

## Condition keys for AWS DevOps Agent Service
<a name="list_devops-agent-policy-keys"></a>

AWS DevOps Agent Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 