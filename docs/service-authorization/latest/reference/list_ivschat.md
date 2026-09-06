

# Actions, resources, and condition keys for Amazon Interactive Video Service Chat
<a name="list_ivschat"></a>

Amazon Interactive Video Service Chat (service prefix: `ivschat`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/ivs/latest/ChatUserGuide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ivschat/ivschat.json) for this service.

**Topics**
+ [API operations defined by Amazon Interactive Video Service Chat](#list_ivschat-operations)
+ [Actions defined by Amazon Interactive Video Service Chat](#list_ivschat-actions-as-permissions)
+ [Resource types defined by Amazon Interactive Video Service Chat](#list_ivschat-resources-for-iam-policies)
+ [Condition keys for Amazon Interactive Video Service Chat](#list_ivschat-policy-keys)

## API operations defined by Amazon Interactive Video Service Chat
<a name="list_ivschat-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ivschat-actions-as-permissions).




- **   CreateChatToken  **
  - **IAM action:**  [ivschat:CreateChatToken](#list_ivschat-action-CreateChatToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLoggingConfiguration  **
  - **IAM action:**  [ivschat:CreateLoggingConfiguration](#list_ivschat-action-CreateLoggingConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivschat:TagResource](#list_ivschat-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRoom  **
  - **IAM action:**  [ivschat:CreateRoom](#list_ivschat-action-CreateRoom)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ivschat:TagResource](#list_ivschat-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteLoggingConfiguration  **
  - **IAM action:**  [ivschat:DeleteLoggingConfiguration](#list_ivschat-action-DeleteLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMessage  **
  - **IAM action:**  [ivschat:DeleteMessage](#list_ivschat-action-DeleteMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRoom  **
  - **IAM action:**  [ivschat:DeleteRoom](#list_ivschat-action-DeleteRoom) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisconnectUser  **
  - **IAM action:**  [ivschat:DisconnectUser](#list_ivschat-action-DisconnectUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLoggingConfiguration  **
  - **IAM action:**  [ivschat:GetLoggingConfiguration](#list_ivschat-action-GetLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRoom  **
  - **IAM action:**  [ivschat:GetRoom](#list_ivschat-action-GetRoom) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLoggingConfigurations  **
  - **IAM action:**  [ivschat:ListLoggingConfigurations](#list_ivschat-action-ListLoggingConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRooms  **
  - **IAM action:**  [ivschat:ListRooms](#list_ivschat-action-ListRooms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ivschat:ListTagsForResource](#list_ivschat-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SendEvent  **
  - **IAM action:**  [ivschat:SendEvent](#list_ivschat-action-SendEvent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ivschat:TagResource](#list_ivschat-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ivschat:UntagResource](#list_ivschat-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLoggingConfiguration  **
  - **IAM action:**  [ivschat:UpdateLoggingConfiguration](#list_ivschat-action-UpdateLoggingConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRoom  **
  - **IAM action:**  [ivschat:UpdateRoom](#list_ivschat-action-UpdateRoom) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Interactive Video Service Chat
<a name="list_ivschat-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateChatToken](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateChatToken.html)  **
  - **Description:** Grants permission to create an encrypted token that is used to establish an individual WebSocket connection to a room
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateLoggingConfiguration.html)  **
  - **Description:** Grants permission to create a logging configuration that allows clients to record room messages
  - **Resource types (\*required):** [Logging-Configuration\*](#list_ivschat-resource-Logging-Configuration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_CreateRoom.html)  **
  - **Description:** Grants permission to create a room that allows clients to connect and pass messages
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteLoggingConfiguration.html)  **
  - **Description:** Grants permission to delete the logging configuration for a specified logging configuration ARN
  - **Resource types (\*required):** [Logging-Configuration\*](#list_ivschat-resource-Logging-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMessage](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteMessage.html)  **
  - **Description:** Grants permission to send an event to a specific room which directs clients to delete a specific message
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DeleteRoom.html)  **
  - **Description:** Grants permission to delete the room for a specified room ARN
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisconnectUser](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_DisconnectUser.html)  **
  - **Description:** Grants permission to disconnect all connections using a specified user ID from a room
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_GetLoggingConfiguration.html)  **
  - **Description:** Grants permission to get the logging configuration for a specified logging configuration ARN
  - **Resource types (\*required):** [Logging-Configuration\*](#list_ivschat-resource-Logging-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_GetRoom.html)  **
  - **Description:** Grants permission to get the room configuration for a specified room ARN
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListLoggingConfigurations](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListLoggingConfigurations.html)  **
  - **Description:** Grants permission to get summary information about logging configurations
  - **Resource types (\*required):** [Logging-Configuration\*](#list_ivschat-resource-Logging-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRooms](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListRooms.html)  **
  - **Description:** Grants permission to get summary information about rooms
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to get information about the tags for a specified ARN
  - **Resource types (\*required):** [Room](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Read

- **   [SendEvent](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_SendEvent.html)  **
  - **Description:** Grants permission to send an event to a room
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add or update tags for a resource with a specified ARN
  - **Resource types (\*required):** [Logging-Configuration](#list_ivschat-resource-Logging-Configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Resource types (\*required):** [Room](#list_ivschat-resource-Room) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ivschat-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags for a resource with a specified ARN
  - **Resource types (\*required):** [Logging-Configuration](#list_ivschat-resource-Logging-Configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Resource types (\*required):** [Room](#list_ivschat-resource-Room) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ivschat-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateLoggingConfiguration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UpdateLoggingConfiguration.html)  **
  - **Description:** Grants permission to update the logging configuration for a specified logging configuration ARN
  - **Resource types (\*required):** [Logging-Configuration\*](#list_ivschat-resource-Logging-Configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRoom](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_UpdateRoom.html)  **
  - **Description:** Grants permission to update the room configuration for a specified room ARN
  - **Resource types (\*required):** [Room\*](#list_ivschat-resource-Room)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Interactive Video Service Chat
<a name="list_ivschat-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Logging-Configuration](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_LoggingConfiguration.html)  | arn:${Partition}:ivschat:${Region}:${Account}:logging-configuration/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_) | 
|  [Room](https://docs.aws.amazon.com/ivs/latest/ChatAPIReference/API_Room.html)  | arn:${Partition}:ivschat:${Region}:${Account}:room/${ResourceId} | [aws:ResourceTag/${TagKey}](#list_ivschat-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Interactive Video Service Chat
<a name="list_ivschat-policy-keys"></a>

Amazon Interactive Video Service Chat defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags associated with the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 