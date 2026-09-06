

# Actions, resources, and condition keys for AWS End User Messaging Social
<a name="list_socialmessaging"></a>

AWS End User Messaging Social (service prefix: `social-messaging`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/social-messaging/latest/userguide/what-is-service.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/social-messaging/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/social-messaging/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/social-messaging/social-messaging.json) for this service.

**Topics**
+ [API operations defined by AWS End User Messaging Social](#list_socialmessaging-operations)
+ [Actions defined by AWS End User Messaging Social](#list_socialmessaging-actions-as-permissions)
+ [Resource types defined by AWS End User Messaging Social](#list_socialmessaging-resources-for-iam-policies)
+ [Condition keys for AWS End User Messaging Social](#list_socialmessaging-policy-keys)

## API operations defined by AWS End User Messaging Social
<a name="list_socialmessaging-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_socialmessaging-actions-as-permissions).




- **   AssociateWhatsAppBusinessAccount  **
  - **IAM action:**  [social-messaging:AssociateWhatsAppBusinessAccount](#list_socialmessaging-action-AssociateWhatsAppBusinessAccount)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [social-messaging:TagResource](#list_socialmessaging-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** social-messaging.amazonaws.com / **Access level:** Write

- **   CreateWhatsAppFlow  **
  - **IAM action:**  [social-messaging:CreateWhatsAppFlow](#list_socialmessaging-action-CreateWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWhatsAppMessageTemplate  **
  - **IAM action:**  [social-messaging:CreateWhatsAppMessageTemplate](#list_socialmessaging-action-CreateWhatsAppMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWhatsAppMessageTemplateFromLibrary  **
  - **IAM action:**  [social-messaging:CreateWhatsAppMessageTemplateFromLibrary](#list_socialmessaging-action-CreateWhatsAppMessageTemplateFromLibrary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateWhatsAppMessageTemplateMedia  **
  - **IAM action:**  [social-messaging:CreateWhatsAppMessageTemplateMedia](#list_socialmessaging-action-CreateWhatsAppMessageTemplateMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWhatsAppFlow  **
  - **IAM action:**  [social-messaging:DeleteWhatsAppFlow](#list_socialmessaging-action-DeleteWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWhatsAppMessageMedia  **
  - **IAM action:**  [social-messaging:DeleteWhatsAppMessageMedia](#list_socialmessaging-action-DeleteWhatsAppMessageMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteWhatsAppMessageTemplate  **
  - **IAM action:**  [social-messaging:DeleteWhatsAppMessageTemplate](#list_socialmessaging-action-DeleteWhatsAppMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeprecateWhatsAppFlow  **
  - **IAM action:**  [social-messaging:DeprecateWhatsAppFlow](#list_socialmessaging-action-DeprecateWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateWhatsAppBusinessAccount  **
  - **IAM action:**  [social-messaging:DisassociateWhatsAppBusinessAccount](#list_socialmessaging-action-DisassociateWhatsAppBusinessAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetLinkedWhatsAppBusinessAccount  **
  - **IAM action:**  [social-messaging:GetLinkedWhatsAppBusinessAccount](#list_socialmessaging-action-GetLinkedWhatsAppBusinessAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLinkedWhatsAppBusinessAccountPhoneNumber  **
  - **IAM action:**  [social-messaging:GetLinkedWhatsAppBusinessAccountPhoneNumber](#list_socialmessaging-action-GetLinkedWhatsAppBusinessAccountPhoneNumber) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWhatsAppFlow  **
  - **IAM action:**  [social-messaging:GetWhatsAppFlow](#list_socialmessaging-action-GetWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWhatsAppFlowPreview  **
  - **IAM action:**  [social-messaging:GetWhatsAppFlowPreview](#list_socialmessaging-action-GetWhatsAppFlowPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetWhatsAppMessageMedia  **
  - **IAM action:**  [social-messaging:GetWhatsAppMessageMedia](#list_socialmessaging-action-GetWhatsAppMessageMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetWhatsAppMessageTemplate  **
  - **IAM action:**  [social-messaging:GetWhatsAppMessageTemplate](#list_socialmessaging-action-GetWhatsAppMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLinkedWhatsAppBusinessAccounts  **
  - **IAM action:**  [social-messaging:ListLinkedWhatsAppBusinessAccounts](#list_socialmessaging-action-ListLinkedWhatsAppBusinessAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [social-messaging:ListTagsForResource](#list_socialmessaging-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListWhatsAppFlowAssets  **
  - **IAM action:**  [social-messaging:ListWhatsAppFlowAssets](#list_socialmessaging-action-ListWhatsAppFlowAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWhatsAppFlows  **
  - **IAM action:**  [social-messaging:ListWhatsAppFlows](#list_socialmessaging-action-ListWhatsAppFlows) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWhatsAppMessageTemplates  **
  - **IAM action:**  [social-messaging:ListWhatsAppMessageTemplates](#list_socialmessaging-action-ListWhatsAppMessageTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListWhatsAppTemplateLibrary  **
  - **IAM action:**  [social-messaging:ListWhatsAppTemplateLibrary](#list_socialmessaging-action-ListWhatsAppTemplateLibrary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PostWhatsAppMessageMedia  **
  - **IAM action:**  [social-messaging:PostWhatsAppMessageMedia](#list_socialmessaging-action-PostWhatsAppMessageMedia) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PublishWhatsAppFlow  **
  - **IAM action:**  [social-messaging:PublishWhatsAppFlow](#list_socialmessaging-action-PublishWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutWhatsAppBusinessAccountEventDestinations  **
  - **IAM action:**  [social-messaging:PutWhatsAppBusinessAccountEventDestinations](#list_socialmessaging-action-PutWhatsAppBusinessAccountEventDestinations)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** social-messaging.amazonaws.com / **Access level:** Write

- **   SendWhatsAppMessage  **
  - **IAM action:**  [social-messaging:SendWhatsAppMessage](#list_socialmessaging-action-SendWhatsAppMessage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [social-messaging:TagResource](#list_socialmessaging-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [social-messaging:UntagResource](#list_socialmessaging-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateWhatsAppFlow  **
  - **IAM action:**  [social-messaging:UpdateWhatsAppFlow](#list_socialmessaging-action-UpdateWhatsAppFlow) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWhatsAppFlowAssets  **
  - **IAM action:**  [social-messaging:UpdateWhatsAppFlowAssets](#list_socialmessaging-action-UpdateWhatsAppFlowAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateWhatsAppMessageTemplate  **
  - **IAM action:**  [social-messaging:UpdateWhatsAppMessageTemplate](#list_socialmessaging-action-UpdateWhatsAppMessageTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS End User Messaging Social
<a name="list_socialmessaging-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_AssociateWhatsAppBusinessAccount.html)  **
  - **Description:** Grants permission to associate a WhatsApp Business Account with your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_socialmessaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_socialmessaging-aws_TagKeys)
  - **Access level:** Write

- **   [CreateWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppFlow.html)  **
  - **Description:** Grants permission to create a new WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplate.html)  **
  - **Description:** Grants permission to create a WhatsApp message template
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWhatsAppMessageTemplateFromLibrary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplateFromLibrary.html)  **
  - **Description:** Grants permission to create a WhatsApp message template from Meta's template library
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateWhatsAppMessageTemplateMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_CreateWhatsAppMessageTemplateMedia.html)  **
  - **Description:** Grants permission to create media for WhatsApp message templates
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppFlow.html)  **
  - **Description:** Grants permission to delete a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageMedia.html)  **
  - **Description:** Grants permission to delete a media object from WhatsApp
  - **Resource types (\*required):** [phone-number-id\*](#list_socialmessaging-resource-phone-number-id)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeleteWhatsAppMessageTemplate.html)  **
  - **Description:** Grants permission to delete a WhatsApp message template
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeprecateWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DeprecateWhatsAppFlow.html)  **
  - **Description:** Grants permission to deprecate a published WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_DisassociateWhatsAppBusinessAccount.html)  **
  - **Description:** Grants permission to disassociate a WhatsApp Business Account from your AWS account
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html)  **
  - **Description:** Grants permission to view the details of a WhatsApp Business Account
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLinkedWhatsAppBusinessAccountPhoneNumber](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccountPhoneNumber.html)  **
  - **Description:** Grants permission to view the details of a phone number
  - **Resource types (\*required):** [phone-number-id\*](#list_socialmessaging-resource-phone-number-id)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppFlow.html)  **
  - **Description:** Grants permission to retrieve the metadata and status of a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWhatsAppFlowPreview](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppFlowPreview.html)  **
  - **Description:** Grants permission to generate a web preview URL for testing a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageMedia.html)  **
  - **Description:** Grants permission to get a media object from WhatsApp
  - **Resource types (\*required):** [phone-number-id\*](#list_socialmessaging-resource-phone-number-id)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppMessageTemplate.html)  **
  - **Description:** Grants permission to get details of a WhatsApp message template
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListLinkedWhatsAppBusinessAccounts](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html)  **
  - **Description:** Grants permission to view all of your WhatsApp Business Accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [phone-number-id](#list_socialmessaging-resource-phone-number-id) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [waba](#list_socialmessaging-resource-waba) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListWhatsAppFlowAssets](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppFlowAssets.html)  **
  - **Description:** Grants permission to list the assets of a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWhatsAppFlows](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppFlows.html)  **
  - **Description:** Grants permission to list all WhatsApp Flows for a WhatsApp Business Account
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWhatsAppMessageTemplates](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppMessageTemplates.html)  **
  - **Description:** Grants permission to list WhatsApp message templates
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListWhatsAppTemplateLibrary](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListWhatsAppTemplateLibrary.html)  **
  - **Description:** Grants permission to list available templates from Meta's template library
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PostWhatsAppMessageMedia](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PostWhatsAppMessageMedia.html)  **
  - **Description:** Grants permission to upload a media object to WhatsApp
  - **Resource types (\*required):** [phone-number-id\*](#list_socialmessaging-resource-phone-number-id)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PublishWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PublishWhatsAppFlow.html)  **
  - **Description:** Grants permission to publish a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [PutWhatsAppBusinessAccountEventDestinations](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_PutWhatsAppBusinessAccountEventDestinations.html)  **
  - **Description:** Grants permission to update a WhatsApp Business Accounts event destination
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendWhatsAppMessage](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_SendWhatsAppMessage.html)  **
  - **Description:** Grants permission to send a message through WhatsApp
  - **Resource types (\*required):** [phone-number-id\*](#list_socialmessaging-resource-phone-number-id)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a tag to a resource
  - **Resource types (\*required):** [phone-number-id](#list_socialmessaging-resource-phone-number-id) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_socialmessaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_socialmessaging-aws_TagKeys)
  - **Resource types (\*required):** [waba](#list_socialmessaging-resource-waba) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_socialmessaging-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_socialmessaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a tag from a resource
  - **Resource types (\*required):** [phone-number-id](#list_socialmessaging-resource-phone-number-id) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_socialmessaging-aws_TagKeys)
  - **Resource types (\*required):** [waba](#list_socialmessaging-resource-waba) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_socialmessaging-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateWhatsAppFlow](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlow.html)  **
  - **Description:** Grants permission to update the metadata of a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWhatsAppFlowAssets](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppFlowAssets.html)  **
  - **Description:** Grants permission to update the Flow JSON definition of a WhatsApp Flow
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateWhatsAppMessageTemplate](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_UpdateWhatsAppMessageTemplate.html)  **
  - **Description:** Grants permission to update a WhatsApp message template
  - **Resource types (\*required):** [waba\*](#list_socialmessaging-resource-waba)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS End User Messaging Social
<a name="list_socialmessaging-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [phone-number-id](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_WhatsAppPhoneNumberDetail.html)  | arn:${Partition}:social-messaging:${Region}:${Account}:phone-number-id/${OriginationPhoneNumberId} | [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_) | 
|  [waba](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_LinkedWhatsAppBusinessAccountSummary.html)  | arn:${Partition}:social-messaging:${Region}:${Account}:waba/${WabaId} | [aws:ResourceTag/${TagKey}](#list_socialmessaging-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS End User Messaging Social
<a name="list_socialmessaging-policy-keys"></a>

AWS End User Messaging Social defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 