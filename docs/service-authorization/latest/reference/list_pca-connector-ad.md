

# Actions, resources, and condition keys for AWS Private CA Connector for Active Directory
<a name="list_pca-connector-ad"></a>

AWS Private CA Connector for Active Directory (service prefix: `pca-connector-ad`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/privateca/latest/userguide/connector-for-ad.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/privateca/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/pca-connector-ad/pca-connector-ad.json) for this service.

**Topics**
+ [API operations defined by AWS Private CA Connector for Active Directory](#list_pca-connector-ad-operations)
+ [Actions defined by AWS Private CA Connector for Active Directory](#list_pca-connector-ad-actions-as-permissions)
+ [Resource types defined by AWS Private CA Connector for Active Directory](#list_pca-connector-ad-resources-for-iam-policies)
+ [Condition keys for AWS Private CA Connector for Active Directory](#list_pca-connector-ad-policy-keys)

## API operations defined by AWS Private CA Connector for Active Directory
<a name="list_pca-connector-ad-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_pca-connector-ad-actions-as-permissions).




- **   CreateConnector  **
  - **IAM action:**  [pca-connector-ad:CreateConnector](#list_pca-connector-ad-action-CreateConnector)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pca-connector-ad:TagResource](#list_pca-connector-ad-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDirectoryRegistration  **
  - **IAM action:**  [pca-connector-ad:CreateDirectoryRegistration](#list_pca-connector-ad-action-CreateDirectoryRegistration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pca-connector-ad:TagResource](#list_pca-connector-ad-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateServicePrincipalName  **
  - **IAM action:**  [pca-connector-ad:CreateServicePrincipalName](#list_pca-connector-ad-action-CreateServicePrincipalName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTemplate  **
  - **IAM action:**  [pca-connector-ad:CreateTemplate](#list_pca-connector-ad-action-CreateTemplate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [pca-connector-ad:TagResource](#list_pca-connector-ad-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateTemplateGroupAccessControlEntry  **
  - **IAM action:**  [pca-connector-ad:CreateTemplateGroupAccessControlEntry](#list_pca-connector-ad-action-CreateTemplateGroupAccessControlEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteConnector  **
  - **IAM action:**  [pca-connector-ad:DeleteConnector](#list_pca-connector-ad-action-DeleteConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectoryRegistration  **
  - **IAM action:**  [pca-connector-ad:DeleteDirectoryRegistration](#list_pca-connector-ad-action-DeleteDirectoryRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteServicePrincipalName  **
  - **IAM action:**  [pca-connector-ad:DeleteServicePrincipalName](#list_pca-connector-ad-action-DeleteServicePrincipalName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplate  **
  - **IAM action:**  [pca-connector-ad:DeleteTemplate](#list_pca-connector-ad-action-DeleteTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplateGroupAccessControlEntry  **
  - **IAM action:**  [pca-connector-ad:DeleteTemplateGroupAccessControlEntry](#list_pca-connector-ad-action-DeleteTemplateGroupAccessControlEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetConnector  **
  - **IAM action:**  [pca-connector-ad:GetConnector](#list_pca-connector-ad-action-GetConnector) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDirectoryRegistration  **
  - **IAM action:**  [pca-connector-ad:GetDirectoryRegistration](#list_pca-connector-ad-action-GetDirectoryRegistration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServicePrincipalName  **
  - **IAM action:**  [pca-connector-ad:GetServicePrincipalName](#list_pca-connector-ad-action-GetServicePrincipalName) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplate  **
  - **IAM action:**  [pca-connector-ad:GetTemplate](#list_pca-connector-ad-action-GetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplateGroupAccessControlEntry  **
  - **IAM action:**  [pca-connector-ad:GetTemplateGroupAccessControlEntry](#list_pca-connector-ad-action-GetTemplateGroupAccessControlEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListConnectors  **
  - **IAM action:**  [pca-connector-ad:ListConnectors](#list_pca-connector-ad-action-ListConnectors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDirectoryRegistrations  **
  - **IAM action:**  [pca-connector-ad:ListDirectoryRegistrations](#list_pca-connector-ad-action-ListDirectoryRegistrations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListServicePrincipalNames  **
  - **IAM action:**  [pca-connector-ad:ListServicePrincipalNames](#list_pca-connector-ad-action-ListServicePrincipalNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [pca-connector-ad:ListTagsForResource](#list_pca-connector-ad-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplateGroupAccessControlEntries  **
  - **IAM action:**  [pca-connector-ad:ListTemplateGroupAccessControlEntries](#list_pca-connector-ad-action-ListTemplateGroupAccessControlEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTemplates  **
  - **IAM action:**  [pca-connector-ad:ListTemplates](#list_pca-connector-ad-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   TagResource  **
  - **IAM action:**  [pca-connector-ad:TagResource](#list_pca-connector-ad-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [pca-connector-ad:UntagResource](#list_pca-connector-ad-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateTemplate  **
  - **IAM action:**  [pca-connector-ad:UpdateTemplate](#list_pca-connector-ad-action-UpdateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplateGroupAccessControlEntry  **
  - **IAM action:**  [pca-connector-ad:UpdateTemplateGroupAccessControlEntry](#list_pca-connector-ad-action-UpdateTemplateGroupAccessControlEntry) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Private CA Connector for Active Directory
<a name="list_pca-connector-ad-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateConnector.html)  **
  - **Description:** Grants permission to create a Connector in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html)  **
  - **Description:** Grants permission to create a DirectoryRegistration in your account
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Access level:** Write

- **   [CreateServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateServicePrincipalName.html)  **
  - **Description:** Grants permission to create a ServicePrincipalName for a DirectoryRegistration
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplate.html)  **
  - **Description:** Grants permission to create a Template for a Connector
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-ad-resource-Connector)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Access level:** Write

- **   [CreateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateTemplateGroupAccessControlEntry.html)  **
  - **Description:** Grants permission to create a TemplateGroupAccessControlEntry for a Template
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteConnector.html)  **
  - **Description:** Grants permission to delete a Connector in your account
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-ad-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteDirectoryRegistration.html)  **
  - **Description:** Grants permission to delete a DirectoryRegistration in your account
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteServicePrincipalName.html)  **
  - **Description:** Grants permission to delete a ServicePrincipalName for a DirectoryRegistration
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteTemplate.html)  **
  - **Description:** Grants permission to delete a Template for a Connector
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_DeleteTemplateGroupAccessControlEntry.html)  **
  - **Description:** Grants permission to delete a TemplateGroupAccessControlEntry for a Template
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetConnector](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetConnector.html)  **
  - **Description:** Grants permission to get a Connector in your account
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-ad-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDirectoryRegistration](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetDirectoryRegistration.html)  **
  - **Description:** Grants permission to get a DirectoryRegistration in your account
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServicePrincipalName](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetServicePrincipalName.html)  **
  - **Description:** Grants permission to get a ServicePrincipalName for a DirectoryRegistration
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetTemplate.html)  **
  - **Description:** Grants permission to get a Template for a Connector
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_GetTemplateGroupAccessControlEntry.html)  **
  - **Description:** Grants permission to get a TemplateGroupAccessControlEntry for a Template
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListConnectors](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListConnectors.html)  **
  - **Description:** Grants permission to list the Connectors in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDirectoryRegistrations](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListDirectoryRegistrations.html)  **
  - **Description:** Grants permission to list the DirectoryRegistrations in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListServicePrincipalNames](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListServicePrincipalNames.html)  **
  - **Description:** Grants permission to list the ServicePrincipalNames for a DirectoryRegistration
  - **Resource types (\*required):** [DirectoryRegistration\*](#list_pca-connector-ad-resource-DirectoryRegistration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for a pca-connector-ad resource in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTemplateGroupAccessControlEntries](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTemplateGroupAccessControlEntries.html)  **
  - **Description:** Grants permission to list the TemplateGroupAccessControlEntries for a Template
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTemplates](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_ListTemplates.html)  **
  - **Description:** Grants permission to list the Templates for a Connector
  - **Resource types (\*required):** [Connector\*](#list_pca-connector-ad-resource-Connector)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [TagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a pca-connector-ad resource in your account
  - **Resource types (\*required):** [Connector](#list_pca-connector-ad-resource-Connector) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Resource types (\*required):** [DirectoryRegistration](#list_pca-connector-ad-resource-DirectoryRegistration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Resource types (\*required):** [Template](#list_pca-connector-ad-resource-Template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_pca-connector-ad-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a pca-connector-ad resource in your account
  - **Resource types (\*required):** [Connector](#list_pca-connector-ad-resource-Connector) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Resource types (\*required):** [DirectoryRegistration](#list_pca-connector-ad-resource-DirectoryRegistration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Resource types (\*required):** [Template](#list_pca-connector-ad-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_pca-connector-ad-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateTemplate](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplate.html)  **
  - **Description:** Grants permission to update a Template for a Connector
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateTemplateGroupAccessControlEntry](https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_UpdateTemplateGroupAccessControlEntry.html)  **
  - **Description:** Grants permission to update a TemplateGroupAccessControlEntry for a Template
  - **Resource types (\*required):** [Template\*](#list_pca-connector-ad-resource-Template)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Private CA Connector for Active Directory
<a name="list_pca-connector-ad-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Connector](${ActionsDocRoot}API_Connector.html)  | arn:${Partition}:pca-connector-ad:${Region}:${Account}:connector/${ConnectorId} | [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_) | 
|  [DirectoryRegistration](${ActionsDocRoot}API_DirectoryRegistration.html)  | arn:${Partition}:pca-connector-ad:${Region}:${Account}:directory-registration/${DirectoryId} | [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_) | 
|  [Template](${ActionsDocRoot}API_Template.html)  | arn:${Partition}:pca-connector-ad:${Region}:${Account}:connector/${ConnectorId}/template/${TemplateId} | [aws:ResourceTag/${TagKey}](#list_pca-connector-ad-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Private CA Connector for Active Directory
<a name="list_pca-connector-ad-policy-keys"></a>

AWS Private CA Connector for Active Directory defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecaconnectorforactivedirectory.html#condition-keys-requesttag)  | Filters access by on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecaconnectorforactivedirectory.html#condition-keys-resourcetag)  | Filters access by on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsprivatecaconnectorforactivedirectory.html#condition-keys-tagkeys)  | Filters access by on the tag keys that are passed in the request | ArrayOfString | 