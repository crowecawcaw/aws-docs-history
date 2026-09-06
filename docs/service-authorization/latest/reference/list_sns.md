

# Actions, resources, and condition keys for Amazon SNS
<a name="list_sns"></a>

Amazon SNS (service prefix: `sns`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/sns/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/sns/latest/api/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/sns/latest/dg/UsingIAMwithSNS.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/sns/sns.json) for this service.

**Topics**
+ [API operations defined by Amazon SNS](#list_sns-operations)
+ [Actions defined by Amazon SNS](#list_sns-actions-as-permissions)
+ [Resource types defined by Amazon SNS](#list_sns-resources-for-iam-policies)
+ [Condition keys for Amazon SNS](#list_sns-policy-keys)

## API operations defined by Amazon SNS
<a name="list_sns-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_sns-actions-as-permissions).




- **   AddPermission  **
  - **IAM action:**  [sns:AddPermission](#list_sns-action-AddPermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   CheckIfPhoneNumberIsOptedOut  **
  - **IAM action:**  [sns:CheckIfPhoneNumberIsOptedOut](#list_sns-action-CheckIfPhoneNumberIsOptedOut) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ConfirmSubscription  **
  - **IAM action:**  [sns:ConfirmSubscription](#list_sns-action-ConfirmSubscription) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreatePlatformApplication  **
  - **IAM action:**  [sns:CreatePlatformApplication](#list_sns-action-CreatePlatformApplication)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   CreatePlatformEndpoint  **
  - **IAM action:**  [sns:CreatePlatformEndpoint](#list_sns-action-CreatePlatformEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSMSSandboxPhoneNumber  **
  - **IAM action:**  [sns:CreateSMSSandboxPhoneNumber](#list_sns-action-CreateSMSSandboxPhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTopic  **
  - **IAM action:**  [sns:CreateTopic](#list_sns-action-CreateTopic)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sns:PutDataProtectionPolicy](#list_sns-action-PutDataProtectionPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [sns:TagResource](#list_sns-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [sns:DeleteEndpoint](#list_sns-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePlatformApplication  **
  - **IAM action:**  [sns:DeletePlatformApplication](#list_sns-action-DeletePlatformApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSMSSandboxPhoneNumber  **
  - **IAM action:**  [sns:DeleteSMSSandboxPhoneNumber](#list_sns-action-DeleteSMSSandboxPhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTopic  **
  - **IAM action:**  [sns:DeleteTopic](#list_sns-action-DeleteTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetDataProtectionPolicy  **
  - **IAM action:**  [sns:GetDataProtectionPolicy](#list_sns-action-GetDataProtectionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEndpointAttributes  **
  - **IAM action:**  [sns:GetEndpointAttributes](#list_sns-action-GetEndpointAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPlatformApplicationAttributes  **
  - **IAM action:**  [sns:GetPlatformApplicationAttributes](#list_sns-action-GetPlatformApplicationAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSMSAttributes  **
  - **IAM action:**  [sns:GetSMSAttributes](#list_sns-action-GetSMSAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSMSSandboxAccountStatus  **
  - **IAM action:**  [sns:GetSMSSandboxAccountStatus](#list_sns-action-GetSMSSandboxAccountStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSubscriptionAttributes  **
  - **IAM action:**  [sns:GetSubscriptionAttributes](#list_sns-action-GetSubscriptionAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTopicAttributes  **
  - **IAM action:**  [sns:GetTopicAttributes](#list_sns-action-GetTopicAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEndpointsByPlatformApplication  **
  - **IAM action:**  [sns:ListEndpointsByPlatformApplication](#list_sns-action-ListEndpointsByPlatformApplication) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOriginationNumbers  **
  - **IAM action:**  [sns:ListOriginationNumbers](#list_sns-action-ListOriginationNumbers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPhoneNumbersOptedOut  **
  - **IAM action:**  [sns:ListPhoneNumbersOptedOut](#list_sns-action-ListPhoneNumbersOptedOut) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPlatformApplications  **
  - **IAM action:**  [sns:ListPlatformApplications](#list_sns-action-ListPlatformApplications) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSMSSandboxPhoneNumbers  **
  - **IAM action:**  [sns:ListSMSSandboxPhoneNumbers](#list_sns-action-ListSMSSandboxPhoneNumbers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptions  **
  - **IAM action:**  [sns:ListSubscriptions](#list_sns-action-ListSubscriptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSubscriptionsByTopic  **
  - **IAM action:**  [sns:ListSubscriptionsByTopic](#list_sns-action-ListSubscriptionsByTopic) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [sns:ListTagsForResource](#list_sns-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTopics  **
  - **IAM action:**  [sns:ListTopics](#list_sns-action-ListTopics) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   OptInPhoneNumber  **
  - **IAM action:**  [sns:OptInPhoneNumber](#list_sns-action-OptInPhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   Publish  **
  - **IAM action:**  [sns:Publish](#list_sns-action-Publish) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PublishBatch  **
  - **IAM action:**  [sns:Publish](#list_sns-action-Publish) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutDataProtectionPolicy  **
  - **IAM action:**  [sns:PutDataProtectionPolicy](#list_sns-action-PutDataProtectionPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RemovePermission  **
  - **IAM action:**  [sns:RemovePermission](#list_sns-action-RemovePermission) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   SetEndpointAttributes  **
  - **IAM action:**  [sns:SetEndpointAttributes](#list_sns-action-SetEndpointAttributes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SetPlatformApplicationAttributes  **
  - **IAM action:**  [sns:SetPlatformApplicationAttributes](#list_sns-action-SetPlatformApplicationAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   SetSMSAttributes  **
  - **IAM action:**  [sns:SetSMSAttributes](#list_sns-action-SetSMSAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   SetSubscriptionAttributes  **
  - **IAM action:**  [sns:SetSubscriptionAttributes](#list_sns-action-SetSubscriptionAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   SetTopicAttributes  **
  - **IAM action:**  [sns:SetTopicAttributes](#list_sns-action-SetTopicAttributes)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   Subscribe  **
  - **IAM action:**  [sns:Subscribe](#list_sns-action-Subscribe)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** sns.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [sns:TagResource](#list_sns-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   Unsubscribe  **
  - **IAM action:**  [sns:Unsubscribe](#list_sns-action-Unsubscribe) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UntagResource  **
  - **IAM action:**  [sns:UntagResource](#list_sns-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   VerifySMSSandboxPhoneNumber  **
  - **IAM action:**  [sns:VerifySMSSandboxPhoneNumber](#list_sns-action-VerifySMSSandboxPhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon SNS
<a name="list_sns-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddPermission](https://docs.aws.amazon.com/sns/latest/api/API_AddPermission.html)  **
  - **Description:** Grants permission to add a statement to a topic's access control policy, granting access for the specified AWS accounts to the specified actions
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [CheckIfPhoneNumberIsOptedOut](https://docs.aws.amazon.com/sns/latest/api/API_CheckIfPhoneNumberIsOptedOut.html)  **
  - **Description:** Grants permission to accept a phone number and indicate whether the phone holder has opted out of receiving SMS messages from your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ConfirmSubscription](https://docs.aws.amazon.com/sns/latest/api/API_ConfirmSubscription.html)  **
  - **Description:** Grants permission to verify an endpoint owner's intent to receive messages by validating the token sent to the endpoint by an earlier Subscribe action
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformApplication.html)  **
  - **Description:** Grants permission to create a platform application object for one of the supported push notification services, such as APNS and GCM, to which devices and mobile apps may register
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreatePlatformEndpoint](https://docs.aws.amazon.com/sns/latest/api/API_CreatePlatformEndpoint.html)  **
  - **Description:** Grants permission to create an endpoint for a device and mobile app on one of the supported push notification services, such as GCM and APNS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateSMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_CreateSMSSandboxPhoneNumber.html)  **
  - **Description:** Grants permission to add a destination phone number and send a one-time password (OTP) to that phone number for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateTopic](https://docs.aws.amazon.com/sns/latest/api/API_CreateTopic.html)  **
  - **Description:** Grants permission to create a topic to which notifications can be published
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sns-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/sns/latest/api/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete the endpoint for a device and mobile app from Amazon SNS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_DeletePlatformApplication.html)  **
  - **Description:** Grants permission to delete a platform application object for one of the supported push notification services, such as APNS and GCM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_DeleteSMSSandboxPhoneNumber.html)  **
  - **Description:** Grants permission to delete an AWS account's verified or pending phone number
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTopic](https://docs.aws.amazon.com/sns/latest/api/API_DeleteTopic.html)  **
  - **Description:** Grants permission to delete a topic and all its subscriptions
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_GetDataProtectionPolicy.html)  **
  - **Description:** Grants permission to return the data protection policy of the topic
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetEndpointAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetEndpointAttributes.html)  **
  - **Description:** Grants permission to retrieve the endpoint attributes for a device on one of the supported push notification services, such as GCM and APNS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPlatformApplicationAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetPlatformApplicationAttributes.html)  **
  - **Description:** Grants permission to retrieve the attributes of the platform application object for the supported push notification services, such as APNS and GCM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html)  **
  - **Description:** Grants permission to return the settings for sending SMS messages from your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSMSSandboxAccountStatus](https://docs.aws.amazon.com/sns/latest/api/API_GetSMSSandboxAccountStatus.html)  **
  - **Description:** Grants permission to retrieve the sandbox status for the calling account in the target region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetSubscriptionAttributes.html)  **
  - **Description:** Grants permission to return all of the properties of a subscription
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTopicAttributes](https://docs.aws.amazon.com/sns/latest/api/API_GetTopicAttributes.html)  **
  - **Description:** Grants permission to return all of the properties of a topic
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListEndpointsByPlatformApplication](https://docs.aws.amazon.com/sns/latest/api/API_ListEndpointsByPlatformApplication.html)  **
  - **Description:** Grants permission to list the endpoints and endpoint attributes for devices in a supported push notification service, such as GCM and APNS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOriginationNumbers](https://docs.aws.amazon.com/sns/latest/api/API_ListOriginationNumbers.html)  **
  - **Description:** Grants permission to list all origination numbers, and their metadata
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPhoneNumbersOptedOut](https://docs.aws.amazon.com/sns/latest/api/API_ListPhoneNumbersOptedOut.html)  **
  - **Description:** Grants permission to return a list of phone numbers that are opted out, meaning you cannot send SMS messages to them
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPlatformApplications](https://docs.aws.amazon.com/sns/latest/api/API_ListPlatformApplications.html)  **
  - **Description:** Grants permission to list the platform application objects for the supported push notification services, such as APNS and GCM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSMSSandboxPhoneNumbers](https://docs.aws.amazon.com/sns/latest/api/API_ListSMSSandboxPhoneNumbers.html)  **
  - **Description:** Grants permission to list the calling account's current pending and verified destination phone numbers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptions](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptions.html)  **
  - **Description:** Grants permission to return a list of the requester's subscriptions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSubscriptionsByTopic](https://docs.aws.amazon.com/sns/latest/api/API_ListSubscriptionsByTopic.html)  **
  - **Description:** Grants permission to return a list of the subscriptions to a specific topic
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/sns/latest/api/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list all tags added to the specified Amazon SNS topic
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html)  **
  - **Description:** Grants permission to return a list of the requester's topics
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [OptInPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_OptInPhoneNumber.html)  **
  - **Description:** Grants permission to opt in a phone number that is currently opted out, which enables you to resume sending SMS messages to the number
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [Publish](https://docs.aws.amazon.com/sns/latest/api/API_Publish.html)  **
  - **Description:** Grants permission to send a message to all of a topic's subscribed endpoints
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutDataProtectionPolicy](https://docs.aws.amazon.com/sns/latest/api/API_PutDataProtectionPolicy.html)  **
  - **Description:** Grants permission to allow a topic owner to set the data protection policy
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RemovePermission](https://docs.aws.amazon.com/sns/latest/api/API_RemovePermission.html)  **
  - **Description:** Grants permission to remove a statement from a topic's access control policy
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [SetEndpointAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetEndpointAttributes.html)  **
  - **Description:** Grants permission to set the attributes for an endpoint for a device on one of the supported push notification services, such as GCM and APNS
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetPlatformApplicationAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetPlatformApplicationAttributes.html)  **
  - **Description:** Grants permission to set the attributes of the platform application object for the supported push notification services, such as APNS and GCM
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html)  **
  - **Description:** Grants permission to set the default settings for sending SMS messages and receiving daily SMS usage reports
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [SetSubscriptionAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSubscriptionAttributes.html)  **
  - **Description:** Grants permission to allow a subscription owner to set an attribute of the topic to a new value
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SetTopicAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetTopicAttributes.html)  **
  - **Description:** Grants permission to allow a topic owner to set an attribute of the topic to a new value
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [Subscribe](https://docs.aws.amazon.com/sns/latest/api/API_Subscribe.html)  **
  - **Description:** Grants permission to prepare to subscribe an endpoint by sending the endpoint a confirmation message
  - **Resource types (\*required):** [topic\*](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)<br />[sns:Endpoint](#list_sns-sns_Endpoint)<br />[sns:Protocol](#list_sns-sns_Protocol)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/sns/latest/api/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified Amazon SNS topic
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_sns-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sns-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [Unsubscribe](https://docs.aws.amazon.com/sns/latest/api/API_Unsubscribe.html)  **
  - **Description:** Grants permission to delete a subscription
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UntagResource](https://docs.aws.amazon.com/sns/latest/api/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified Amazon SNS topic
  - **Resource types (\*required):** [topic](#list_sns-resource-topic)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_sns-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [VerifySMSSandboxPhoneNumber](https://docs.aws.amazon.com/sns/latest/api/API_VerifySMSSandboxPhoneNumber.html)  **
  - **Description:** Grants permission to verify a destination phone number with a one-time password (OTP) for an AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon SNS
<a name="list_sns-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [topic](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html)  | arn:${Partition}:sns:${Region}:${Account}:${TopicName} | [aws:ResourceTag/${TagKey}](#list_sns-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon SNS
<a name="list_sns-policy-keys"></a>

Amazon SNS defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags from request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys from request | ArrayOfString | 
|   [sns:Endpoint](https://docs.aws.amazon.com/sns/latest/dg/UsingIAMwithSNS.html#w2ab1c11c23c19)  | Filters access by the URL, email address, or ARN from a Subscribe request or a previously confirmed subscription | String | 
|   [sns:Protocol](https://docs.aws.amazon.com/sns/latest/dg/UsingIAMwithSNS.html#w2ab1c11c23c19)  | Filters access by the protocol value from a Subscribe request or a previously confirmed subscription | String | 