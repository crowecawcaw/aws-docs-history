

# Actions, resources, and condition keys for Amazon Q
<a name="list_q"></a>

Amazon Q (service prefix: `q`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/q/q.json) for this service.

**Topics**
+ [Actions defined by Amazon Q](#list_q-actions-as-permissions)
+ [Permission-only actions for Amazon Q](#list_q-permission-only-actions)
+ [Resource types defined by Amazon Q](#list_q-resources-for-iam-policies)
+ [Condition keys for Amazon Q](#list_q-policy-keys)

## Actions defined by Amazon Q
<a name="list_q-actions-as-permissions"></a>

Amazon Q has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for Amazon Q
<a name="list_q-permission-only-actions"></a>

The following actions are defined by Amazon Q but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateConnectorResource](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to associate an AWS resource with an Amazon Q connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateLoginDomain](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to associate a login domain with an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDescribeGroups](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to describe multiple groups for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchDescribeUsers](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to describe multiple users for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetGroups](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to get multiple groups for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetUsers](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to get multiple users for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [CreateArtifact](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to create an artifact with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateAssignment](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to create a user or group assignment for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[identitystore:GroupId](#list_q-identitystore_GroupId)<br />[identitystore:UserId](#list_q-identitystore_UserId)
  - **Access level:** Write

- **   [CreateAuthGrant](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to create OAuth user in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOAuthAppConnection](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to register an OAuth application in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to create and configure a third party plugin in Amazon Q
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Access level:** Write

- **   [CreateScimAccessToken](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to create a SCIM access token for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAssignment](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to delete a user or group assignment for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[identitystore:GroupId](#list_q-identitystore_GroupId)<br />[identitystore:UserId](#list_q-identitystore_UserId)
  - **Access level:** Write

- **   [DeleteConversation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to delete a conversation with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOAuthAppConnection](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to delete an OAuth application in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePlugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to delete a configured plugin in Amazon Q
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteScimAccessToken](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to delete a SCIM access token for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateLoginDomain](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to disassociate a login domain from an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GenerateCodeFromCommands](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to generate code from CLI commands in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GenerateCodeRecommendations](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to generate code recommendations in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetArtifact](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to view an Amazon Q artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetArtifactActionResult](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to view results of an action in an Amazon Q artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnector](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to view information about a specific Amazon Q connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConversation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to get individual messages associated with a specific conversation with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetIdentityMetadata](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to Amazon Q to get the identity metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPlugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to view information about a specific configured Amazon Q plugin
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTroubleshootingResults](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to get troubleshooting results with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListConversations](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list individual conversations associated with a specific Amazon Q user
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDashboardMetrics](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to read metrics to populate Amazon Q dashboard
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListGroups](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list groups for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLoginDomains](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list login domains for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPluginProviders](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list available plugins in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPlugins](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list configured plugins in Amazon Q
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScimAccessTokens](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list SCIM access tokens for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list all tags associated with an Amazon Q resource
  - **Resource types (\*required):** [plugin](#list_q-resource-plugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListUsers](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to list users for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PassRequest](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to allow Amazon Q to perform actions on your behalf
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PerformArtifactAction](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to perform an action in an Amazon Q artifact
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectConnector](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to reject a connection request for an Amazon Q connector
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendEvent](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to trigger asynchronous Amazon Q actions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SendMessage](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to send a message to Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartConversation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to start a conversation with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartTroubleshootingAnalysis](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to start a troubleshooting analysis with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartTroubleshootingResolutionExplanation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to start a troubleshooting resolution explanation with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to associate tags with an Amazon Q resource
  - **Resource types (\*required):** [plugin](#list_q-resource-plugin) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_q-resource-profile) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to remove tags associated with an Amazon Q resource
  - **Resource types (\*required):** [plugin](#list_q-resource-plugin) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Resource types (\*required):** [profile](#list_q-resource-profile) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAssignment](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update a user or group assignment for an Amazon Q Developer Profile
  - **Resource types (\*required):** [profile\*](#list_q-resource-profile)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[identitystore:GroupId](#list_q-identitystore_GroupId)<br />[identitystore:UserId](#list_q-identitystore_UserId)
  - **Access level:** Write

- **   [UpdateAuthGrant](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update OAuth user in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateConversation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update a conversation with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateOAuthAppConnection](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update an OAuth application in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePlugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update a third party plugin in Amazon Q
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_q-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_q-aws_TagKeys)
  - **Access level:** Write

- **   [UpdateTroubleshootingCommandResult](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to update a troubleshooting command result with Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UsePlugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to use Amazon Q plugins
  - **Resource types (\*required):** [plugin\*](#list_q-resource-plugin)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [VerifyOAuthAppConnection](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_manage-access-with-policies.html)  **
  - **Description:** Grants permission to verify an OAuth application in Amazon Q
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Q
<a name="list_q-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [plugin](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/plugins.html)  | arn:${Partition}:qdeveloper:${Region}:${Account}:plugin/${Identifier} | [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_) | 
|  [profile](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/as-whisper-admin.html#about-profiles)  | arn:${Partition}:codewhisperer:${Region}:${Account}:profile/${Identifier} | [aws:ResourceTag/${TagKey}](#list_q-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Q
<a name="list_q-policy-keys"></a>

Amazon Q defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html)  | Filters access by the tags associated with the Amazon Q resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 
|   [identitystore:GroupId](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html)  | Filters access by IAM Identity Center Group ID | ArrayOfString | 
|   [identitystore:UserId](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html)  | Filters access by IAM Identity Center User ID | ArrayOfString | 