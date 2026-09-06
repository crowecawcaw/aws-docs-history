

# Actions, resources, and condition keys for AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts"></a>

AWS Systems Manager Incident Manager Contacts (service prefix: `ssm-contacts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/incident-manager/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/incident-manager/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/ssm-contacts/ssm-contacts.json) for this service.

**Topics**
+ [API operations defined by AWS Systems Manager Incident Manager Contacts](#list_ssm-contacts-operations)
+ [Actions defined by AWS Systems Manager Incident Manager Contacts](#list_ssm-contacts-actions-as-permissions)
+ [Permission-only actions for AWS Systems Manager Incident Manager Contacts](#list_ssm-contacts-permission-only-actions)
+ [Resource types defined by AWS Systems Manager Incident Manager Contacts](#list_ssm-contacts-resources-for-iam-policies)
+ [Condition keys for AWS Systems Manager Incident Manager Contacts](#list_ssm-contacts-policy-keys)

## API operations defined by AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_ssm-contacts-actions-as-permissions).




- **   AcceptPage  **
  - **IAM action:**  [ssm-contacts:AcceptPage](#list_ssm-contacts-action-AcceptPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ActivateContactChannel  **
  - **IAM action:**  [ssm-contacts:ActivateContactChannel](#list_ssm-contacts-action-ActivateContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateContact  **
  - **IAM action:**  [ssm-contacts:AssociateContact](#list_ssm-contacts-action-AssociateContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [ssm-contacts:CreateContact](#list_ssm-contacts-action-CreateContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-contacts:TagResource](#list_ssm-contacts-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateContactChannel  **
  - **IAM action:**  [ssm-contacts:CreateContactChannel](#list_ssm-contacts-action-CreateContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRotation  **
  - **IAM action:**  [ssm-contacts:CreateRotation](#list_ssm-contacts-action-CreateRotation)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [ssm-contacts:TagResource](#list_ssm-contacts-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateRotationOverride  **
  - **IAM action:**  [ssm-contacts:CreateRotationOverride](#list_ssm-contacts-action-CreateRotationOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeactivateContactChannel  **
  - **IAM action:**  [ssm-contacts:DeactivateContactChannel](#list_ssm-contacts-action-DeactivateContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContact  **
  - **IAM action:**  [ssm-contacts:DeleteContact](#list_ssm-contacts-action-DeleteContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteContactChannel  **
  - **IAM action:**  [ssm-contacts:DeleteContactChannel](#list_ssm-contacts-action-DeleteContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRotation  **
  - **IAM action:**  [ssm-contacts:DeleteRotation](#list_ssm-contacts-action-DeleteRotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRotationOverride  **
  - **IAM action:**  [ssm-contacts:DeleteRotationOverride](#list_ssm-contacts-action-DeleteRotationOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeEngagement  **
  - **IAM action:**  [ssm-contacts:DescribeEngagement](#list_ssm-contacts-action-DescribeEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePage  **
  - **IAM action:**  [ssm-contacts:DescribePage](#list_ssm-contacts-action-DescribePage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContact  **
  - **IAM action:**  [ssm-contacts:GetContact](#list_ssm-contacts-action-GetContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContactChannel  **
  - **IAM action:**  [ssm-contacts:GetContactChannel](#list_ssm-contacts-action-GetContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContactPolicy  **
  - **IAM action:**  [ssm-contacts:GetContactPolicy](#list_ssm-contacts-action-GetContactPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRotation  **
  - **IAM action:**  [ssm-contacts:GetRotation](#list_ssm-contacts-action-GetRotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRotationOverride  **
  - **IAM action:**  [ssm-contacts:GetRotationOverride](#list_ssm-contacts-action-GetRotationOverride) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListContactChannels  **
  - **IAM action:**  [ssm-contacts:ListContactChannels](#list_ssm-contacts-action-ListContactChannels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListContacts  **
  - **IAM action:**  [ssm-contacts:ListContacts](#list_ssm-contacts-action-ListContacts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListEngagements  **
  - **IAM action:**  [ssm-contacts:ListEngagements](#list_ssm-contacts-action-ListEngagements) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPageReceipts  **
  - **IAM action:**  [ssm-contacts:ListPageReceipts](#list_ssm-contacts-action-ListPageReceipts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPageResolutions  **
  - **IAM action:**  [ssm-contacts:ListPageResolutions](#list_ssm-contacts-action-ListPageResolutions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPagesByContact  **
  - **IAM action:**  [ssm-contacts:ListPagesByContact](#list_ssm-contacts-action-ListPagesByContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPagesByEngagement  **
  - **IAM action:**  [ssm-contacts:ListPagesByEngagement](#list_ssm-contacts-action-ListPagesByEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPreviewRotationShifts  **
  - **IAM action:**  [ssm-contacts:ListPreviewRotationShifts](#list_ssm-contacts-action-ListPreviewRotationShifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRotationOverrides  **
  - **IAM action:**  [ssm-contacts:ListRotationOverrides](#list_ssm-contacts-action-ListRotationOverrides) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRotationShifts  **
  - **IAM action:**  [ssm-contacts:ListRotationShifts](#list_ssm-contacts-action-ListRotationShifts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListRotations  **
  - **IAM action:**  [ssm-contacts:ListRotations](#list_ssm-contacts-action-ListRotations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [ssm-contacts:ListTagsForResource](#list_ssm-contacts-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutContactPolicy  **
  - **IAM action:**  [ssm-contacts:PutContactPolicy](#list_ssm-contacts-action-PutContactPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SendActivationCode  **
  - **IAM action:**  [ssm-contacts:SendActivationCode](#list_ssm-contacts-action-SendActivationCode) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartEngagement  **
  - **IAM action:**  [ssm-contacts:StartEngagement](#list_ssm-contacts-action-StartEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopEngagement  **
  - **IAM action:**  [ssm-contacts:StopEngagement](#list_ssm-contacts-action-StopEngagement) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [ssm-contacts:TagResource](#list_ssm-contacts-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [ssm-contacts:UntagResource](#list_ssm-contacts-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateContact  **
  - **IAM action:**  [ssm-contacts:AssociateContact](#list_ssm-contacts-action-AssociateContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [ssm-contacts:UpdateContact](#list_ssm-contacts-action-UpdateContact)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateContactChannel  **
  - **IAM action:**  [ssm-contacts:UpdateContactChannel](#list_ssm-contacts-action-UpdateContactChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRotation  **
  - **IAM action:**  [ssm-contacts:UpdateRotation](#list_ssm-contacts-action-UpdateRotation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptPage](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_AcceptPage.html)  **
  - **Description:** Grants permission to accept a page
  - **Resource types (\*required):** [page\*](#list_ssm-contacts-resource-page)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ActivateContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ActivateContactChannel.html)  **
  - **Description:** Grants permission to activate a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateContact](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateContact.html)  **
  - **Description:** Grants permission to create a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-contacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Access level:** Write

- **   [CreateContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateContactChannel.html)  **
  - **Description:** Grants permission to create a contact channel for a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRotation](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateRotation.html)  **
  - **Description:** Grants permission to create a rotation in an on-call schedule
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-contacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Access level:** Write

- **   [CreateRotationOverride](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_CreateRotationOverride.html)  **
  - **Description:** Grants permission to create an override for a rotation in an on-call schedule
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeactivateContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeactivateContactChannel.html)  **
  - **Description:** Grants permission to deactivate a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteContact](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeleteContact.html)  **
  - **Description:** Grants permission to delete a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeleteContactChannel.html)  **
  - **Description:** Grants permission to delete a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRotation](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeleteRotation.html)  **
  - **Description:** Grants permission to delete a rotation
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRotationOverride](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DeleteRotationOverride.html)  **
  - **Description:** Grants permission to delete a rotation's rotation override
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeEngagement](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DescribeEngagement.html)  **
  - **Description:** Grants permission to describe an engagement
  - **Resource types (\*required):** [engagement\*](#list_ssm-contacts-resource-engagement)
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribePage](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_DescribePage.html)  **
  - **Description:** Grants permission to describe a page
  - **Resource types (\*required):** [page\*](#list_ssm-contacts-resource-page)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContact](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetContact.html)  **
  - **Description:** Grants permission to get a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetContactChannel.html)  **
  - **Description:** Grants permission to get a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContactPolicy](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetContactPolicy.html)  **
  - **Description:** Grants permission to get a contact's resource policy
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRotation](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetRotation.html)  **
  - **Description:** Grants permission to retrieve information about an on-call rotation
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetRotationOverride](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_GetRotationOverride.html)  **
  - **Description:** Grants permission to retrieve information about an override in an on-call rotation
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListContactChannels](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListContactChannels.html)  **
  - **Description:** Grants permission to list all of a contact's contact channels
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListContacts](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListContacts.html)  **
  - **Description:** Grants permission to list all contacts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListEngagements](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListEngagements.html)  **
  - **Description:** Grants permission to list all engagements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPageReceipts](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPageReceipts.html)  **
  - **Description:** Grants permission to list all receipts of a page
  - **Resource types (\*required):** [page\*](#list_ssm-contacts-resource-page)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPageResolutions](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPageResolutions.html)  **
  - **Description:** Grants permission to list the resolution path of an engagement
  - **Resource types (\*required):** [page\*](#list_ssm-contacts-resource-page)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPagesByContact](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPagesByContact.html)  **
  - **Description:** Grants permission to list all pages sent to a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPagesByEngagement](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPagesByEngagement.html)  **
  - **Description:** Grants permission to list all pages created in an engagement
  - **Resource types (\*required):** [engagement\*](#list_ssm-contacts-resource-engagement)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPreviewRotationShifts](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListPreviewRotationShifts.html)  **
  - **Description:** Grants permission to retrieve a list of shifts based on rotation configuration parameters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListRotationOverrides](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListRotationOverrides.html)  **
  - **Description:** Grants permission to retrieve a list of overrides currently specified for an on-call rotation
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRotationShifts](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListRotationShifts.html)  **
  - **Description:** Grants permission to retrieve a list of rotation shifts in an on-call schedule
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListRotations](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListRotations.html)  **
  - **Description:** Grants permission to retrieve a list of on-call rotations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ListTagsForResource.html)  **
  - **Description:** Grants permission to view a list of resource tags for a specified resource
  - **Resource types (\*required):** [contact](#list_ssm-contacts-resource-contact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [rotation](#list_ssm-contacts-resource-rotation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutContactPolicy](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_PutContactPolicy.html)  **
  - **Description:** Grants permission to add a resource policy to a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SendActivationCode](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_SendActivationCode.html)  **
  - **Description:** Grants permission to send the activation code of a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartEngagement](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_StartEngagement.html)  **
  - **Description:** Grants permission to start an engagement
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEngagement](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_StopEngagement.html)  **
  - **Description:** Grants permission to stop an engagement
  - **Resource types (\*required):** [engagement\*](#list_ssm-contacts-resource-engagement)
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_TagResource.html)  **
  - **Description:** Grants permission to add tags to the specified resource
  - **Resource types (\*required):** [contact](#list_ssm-contacts-resource-contact) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-contacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Resource types (\*required):** [rotation](#list_ssm-contacts-resource-rotation) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_ssm-contacts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from the specified resource
  - **Resource types (\*required):** [contact](#list_ssm-contacts-resource-contact) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Resource types (\*required):** [rotation](#list_ssm-contacts-resource-rotation) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_ssm-contacts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateContact](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateContact.html)  **
  - **Description:** Grants permission to update a contact
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateContactChannel](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateContactChannel.html)  **
  - **Description:** Grants permission to update a contact's contact channel
  - **Resource types (\*required):** [contactchannel\*](#list_ssm-contacts-resource-contactchannel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateRotation](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_UpdateRotation.html)  **
  - **Description:** Grants permission to update the information specified for an on-call rotation
  - **Resource types (\*required):** [rotation\*](#list_ssm-contacts-resource-rotation)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Permission-only actions for AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts-permission-only-actions"></a>

The following actions are defined by AWS Systems Manager Incident Manager Contacts but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [AssociateContact](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)  **
  - **Description:** Grants permission to use a contact in an escalation plan
  - **Resource types (\*required):** [contact\*](#list_ssm-contacts-resource-contact)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write



## Resource types defined by AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [contact](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)  | arn:${Partition}:ssm-contacts:${Region}:${Account}:contact/${ContactAlias} | [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_) | 
|  [contactchannel](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html)  | arn:${Partition}:ssm-contacts:${Region}:${Account}:contactchannel/${ContactAlias}/${ContactChannelId} |   | 
|  [engagement](https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html)  | arn:${Partition}:ssm-contacts:${Region}:${Account}:engagement/${ContactAlias}/${EngagementId} |   | 
|  [page](https://docs.aws.amazon.com/incident-manager/latest/userguide/escalation.html)  | arn:${Partition}:ssm-contacts:${Region}:${Account}:page/${ContactAlias}/${PageId} |   | 
|  [rotation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-on-call-schedule.html)  | arn:${Partition}:ssm-contacts:${Region}:${Account}:rotation/${RotationId} | [aws:ResourceTag/${TagKey}](#list_ssm-contacts-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Systems Manager Incident Manager Contacts
<a name="list_ssm-contacts-policy-keys"></a>

AWS Systems Manager Incident Manager Contacts defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 