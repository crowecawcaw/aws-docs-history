

# Actions, resources, and condition keys for Amazon Connect Cases
<a name="list_connectcases"></a>

Amazon Connect Cases (service prefix: `cases`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/cases/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/connect/latest/adminguide/assign-security-profile-cases.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/cases/cases.json) for this service.

**Topics**
+ [API operations defined by Amazon Connect Cases](#list_connectcases-operations)
+ [Actions defined by Amazon Connect Cases](#list_connectcases-actions-as-permissions)
+ [Resource types defined by Amazon Connect Cases](#list_connectcases-resources-for-iam-policies)
+ [Condition keys for Amazon Connect Cases](#list_connectcases-policy-keys)

## API operations defined by Amazon Connect Cases
<a name="list_connectcases-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_connectcases-actions-as-permissions).




- **   BatchGetCaseRule  **
  - **IAM action:**  [cases:BatchGetCaseRule](#list_connectcases-action-BatchGetCaseRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchGetField  **
  - **IAM action:**  [cases:BatchGetField](#list_connectcases-action-BatchGetField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchPutFieldOptions  **
  - **IAM action:**  [cases:BatchPutFieldOptions](#list_connectcases-action-BatchPutFieldOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateCase  **
  - **IAM action:**  [cases:CreateCase](#list_connectcases-action-CreateCase)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [cases:TagResource](#list_connectcases-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCaseRule  **
  - **IAM action:**  [cases:CreateCaseRule](#list_connectcases-action-CreateCaseRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDomain  **
  - **IAM action:**  [cases:CreateDomain](#list_connectcases-action-CreateDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateField  **
  - **IAM action:**  [cases:CreateField](#list_connectcases-action-CreateField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLayout  **
  - **IAM action:**  [cases:CreateLayout](#list_connectcases-action-CreateLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRelatedItem  **
  - **IAM action:**  [cases:CreateRelatedItem](#list_connectcases-action-CreateRelatedItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateTemplate  **
  - **IAM action:**  [cases:CreateTemplate](#list_connectcases-action-CreateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCase  **
  - **IAM action:**  [cases:DeleteCase](#list_connectcases-action-DeleteCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCaseRule  **
  - **IAM action:**  [cases:DeleteCaseRule](#list_connectcases-action-DeleteCaseRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [cases:DeleteDomain](#list_connectcases-action-DeleteDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteField  **
  - **IAM action:**  [cases:DeleteField](#list_connectcases-action-DeleteField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLayout  **
  - **IAM action:**  [cases:DeleteLayout](#list_connectcases-action-DeleteLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRelatedItem  **
  - **IAM action:**  [cases:DeleteRelatedItem](#list_connectcases-action-DeleteRelatedItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTemplate  **
  - **IAM action:**  [cases:DeleteTemplate](#list_connectcases-action-DeleteTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCase  **
  - **IAM action:**  [cases:GetCase](#list_connectcases-action-GetCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCaseAuditEvents  **
  - **IAM action:**  [cases:GetCaseAuditEvents](#list_connectcases-action-GetCaseAuditEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCaseEventConfiguration  **
  - **IAM action:**  [cases:GetCaseEventConfiguration](#list_connectcases-action-GetCaseEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomain  **
  - **IAM action:**  [cases:GetDomain](#list_connectcases-action-GetDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLayout  **
  - **IAM action:**  [cases:GetLayout](#list_connectcases-action-GetLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTemplate  **
  - **IAM action:**  [cases:GetTemplate](#list_connectcases-action-GetTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCaseRules  **
  - **IAM action:**  [cases:ListCaseRules](#list_connectcases-action-ListCaseRules) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCasesForContact  **
  - **IAM action:**  [cases:ListCasesForContact](#list_connectcases-action-ListCasesForContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomains  **
  - **IAM action:**  [cases:ListDomains](#list_connectcases-action-ListDomains) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFieldOptions  **
  - **IAM action:**  [cases:ListFieldOptions](#list_connectcases-action-ListFieldOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFields  **
  - **IAM action:**  [cases:ListFields](#list_connectcases-action-ListFields) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLayouts  **
  - **IAM action:**  [cases:ListLayouts](#list_connectcases-action-ListLayouts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [cases:ListTagsForResource](#list_connectcases-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTemplates  **
  - **IAM action:**  [cases:ListTemplates](#list_connectcases-action-ListTemplates) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutCaseEventConfiguration  **
  - **IAM action:**  [cases:PutCaseEventConfiguration](#list_connectcases-action-PutCaseEventConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SearchAllRelatedItems  **
  - **IAM action:**  [cases:SearchAllRelatedItems](#list_connectcases-action-SearchAllRelatedItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchCases  **
  - **IAM action:**  [cases:SearchCases](#list_connectcases-action-SearchCases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchRelatedItems  **
  - **IAM action:**  [cases:SearchRelatedItems](#list_connectcases-action-SearchRelatedItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TagResource  **
  - **IAM action:**  [cases:TagResource](#list_connectcases-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [cases:UntagResource](#list_connectcases-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCase  **
  - **IAM action:**  [cases:UpdateCase](#list_connectcases-action-UpdateCase) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateCaseRule  **
  - **IAM action:**  [cases:UpdateCaseRule](#list_connectcases-action-UpdateCaseRule) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateField  **
  - **IAM action:**  [cases:UpdateField](#list_connectcases-action-UpdateField) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLayout  **
  - **IAM action:**  [cases:UpdateLayout](#list_connectcases-action-UpdateLayout) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateRelatedItem  **
  - **IAM action:**  [cases:UpdateRelatedItem](#list_connectcases-action-UpdateRelatedItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateTemplate  **
  - **IAM action:**  [cases:UpdateTemplate](#list_connectcases-action-UpdateTemplate) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Connect Cases
<a name="list_connectcases-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchGetCaseRule](https://docs.aws.amazon.com/cases/latest/APIReference/API_BatchGetCaseRule.html)  **
  - **Description:** Grants permission to retrieve information about the case rules in the case domain
  - **Resource types (\*required):** [CaseRule\*](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchGetField](https://docs.aws.amazon.com/cases/latest/APIReference/API_BatchGetField.html)  **
  - **Description:** Grants permission to retrieve information about the fields in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [BatchPutFieldOptions](https://docs.aws.amazon.com/cases/latest/APIReference/API_BatchPutFieldOptions.html)  **
  - **Description:** Grants permission to update the field options in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateCase](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateCase.html)  **
  - **Description:** Grants permission to create a case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Template\*](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Access level:** Write

- **   [CreateCaseRule](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateCaseRule.html)  **
  - **Description:** Grants permission to create a case rule in the case domain
  - **Resource types (\*required):** [CaseRule\*](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create a new case domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateField](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateField.html)  **
  - **Description:** Grants permission to create a field in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLayout](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateLayout.html)  **
  - **Description:** Grants permission to create a layout in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Layout\*](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateRelatedItem](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateRelatedItem.html)  **
  - **Description:** Grants permission to create a related item associated to a case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [RelatedItem\*](#list_connectcases-resource-RelatedItem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Access level:** Write

- **   [CreateTemplate](https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateTemplate.html)  **
  - **Description:** Grants permission to create a template in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Layout\*](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Template\*](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCase](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteCase.html)  **
  - **Description:** Grants permission to delete the case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCaseRule](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteCaseRule.html)  **
  - **Description:** Grants permission to delete the case rule in the case domain
  - **Resource types (\*required):** [CaseRule\*](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete the domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteField](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteField.html)  **
  - **Description:** Grants permission to delete the field in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLayout](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteLayout.html)  **
  - **Description:** Grants permission to delete the layout in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Layout\*](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteRelatedItem](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteRelatedItem.html)  **
  - **Description:** Grants permission to delete the related item associated to the case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RelatedItem\*](#list_connectcases-resource-RelatedItem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType)
  - **Access level:** Write

- **   [DeleteTemplate](https://docs.aws.amazon.com/cases/latest/APIReference/API_DeleteTemplate.html)  **
  - **Description:** Grants permission to delete the template in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Template\*](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCase](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetCase.html)  **
  - **Description:** Grants permission to retrieve information about a case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCaseAuditEvents](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetCaseAuditEvents.html)  **
  - **Description:** Grants permission to view audit history of a case
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCaseEventConfiguration](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetCaseEventConfiguration.html)  **
  - **Description:** Grants permission to retrieve information about the case event configuraton in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomain](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetDomain.html)  **
  - **Description:** Grants permission to retrieve information about the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLayout](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetLayout.html)  **
  - **Description:** Grants permission to retrieve information about the layout in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Layout\*](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTemplate](https://docs.aws.amazon.com/cases/latest/APIReference/API_GetTemplate.html)  **
  - **Description:** Grants permission to retrieve information about the template in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Template\*](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCaseRules](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListCaseRules.html)  **
  - **Description:** Grants permission to list case rules in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCasesForContact](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListCasesForContact.html)  **
  - **Description:** Grants permission to list cases for a specific contact in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomains](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListDomains.html)  **
  - **Description:** Grants permission to list all domains in the aws account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFieldOptions](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListFieldOptions.html)  **
  - **Description:** Grants permission to list field options for a single select field in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListFields](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListFields.html)  **
  - **Description:** Grants permission to list fields in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLayouts](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListLayouts.html)  **
  - **Description:** Grants permission to list layouts in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for the specified resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTemplates](https://docs.aws.amazon.com/cases/latest/APIReference/API_ListTemplates.html)  **
  - **Description:** Grants permission to list templates in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [PutCaseEventConfiguration](https://docs.aws.amazon.com/cases/latest/APIReference/API_PutCaseEventConfiguration.html)  **
  - **Description:** Grants permission to insert or update the case event configuration in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [SearchAllRelatedItems](https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchAllRelatedItems.html)  **
  - **Description:** Grants permission to search for related items in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchCases](https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchCases.html)  **
  - **Description:** Grants permission to search for cases in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchRelatedItems](https://docs.aws.amazon.com/cases/latest/APIReference/API_SearchRelatedItems.html)  **
  - **Description:** Grants permission to search for related items associated to the case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TagResource](https://docs.aws.amazon.com/cases/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add the specified tags to the specified resource
  - **Resource types (\*required):** [Case](#list_connectcases-resource-Case) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [CaseRule](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Domain](#list_connectcases-resource-Domain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Field](#list_connectcases-resource-Field) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Layout](#list_connectcases-resource-Layout) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [RelatedItem](#list_connectcases-resource-RelatedItem) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType)
  - **Resource types (\*required):** [Template](#list_connectcases-resource-Template) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_connectcases-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/cases/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove the specified tags from the specified resource
  - **Resource types (\*required):** [Case](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [CaseRule](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Domain](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Field](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [Layout](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Resource types (\*required):** [RelatedItem](#list_connectcases-resource-RelatedItem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType)
  - **Resource types (\*required):** [Template](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_connectcases-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCase](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCase.html)  **
  - **Description:** Grants permission to update the field values on the case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[connect:UserArn](#list_connectcases-connect_UserArn)
  - **Access level:** Write

- **   [UpdateCaseRule](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateCaseRule.html)  **
  - **Description:** Grants permission to update the case rule in the case domain
  - **Resource types (\*required):** [CaseRule\*](#list_connectcases-resource-CaseRule) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateField](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateField.html)  **
  - **Description:** Grants permission to update the field in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Field\*](#list_connectcases-resource-Field) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLayout](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateLayout.html)  **
  - **Description:** Grants permission to update the layout in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Layout\*](#list_connectcases-resource-Layout) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateRelatedItem](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateRelatedItem.html)  **
  - **Description:** Grants permission to update a related item associated to a case in the case domain
  - **Resource types (\*required):** [Case\*](#list_connectcases-resource-Case) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [RelatedItem\*](#list_connectcases-resource-RelatedItem) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType)
  - **Access level:** Write

- **   [UpdateTemplate](https://docs.aws.amazon.com/cases/latest/APIReference/API_UpdateTemplate.html)  **
  - **Description:** Grants permission to update the template in the case domain
  - **Resource types (\*required):** [Domain\*](#list_connectcases-resource-Domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Template\*](#list_connectcases-resource-Template) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Connect Cases
<a name="list_connectcases-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [Case](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/case/${CaseId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 
|  [CaseRule](https://docs.aws.amazon.com/connect/latest/adminguide/case-rules.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/case-rule/${CaseRuleId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 
|  [Domain](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 
|  [Field](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/field/${FieldId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 
|  [Layout](https://docs.aws.amazon.com/connect/latest/adminguide/case-layouts.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/layout/${LayoutId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 
|  [RelatedItem](https://docs.aws.amazon.com/connect/latest/adminguide/associatecontactandcase.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/case/${CaseId}/related-item/${RelatedItemId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_)<br />[cases:CreatedBy](#list_connectcases-cases_CreatedBy)<br />[cases:RelatedItemType](#list_connectcases-cases_RelatedItemType) | 
|  [Template](https://docs.aws.amazon.com/connect/latest/adminguide/case-templates.html)  | arn:${Partition}:cases:${Region}:${Account}:domain/${DomainId}/template/${TemplateId} | [aws:ResourceTag/${TagKey}](#list_connectcases-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Connect Cases
<a name="list_connectcases-policy-keys"></a>

Amazon Connect Cases defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 
|   [cases:CreatedBy](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_service-with-iam.html)  | Filters access by who created the the resource (user ARN or custom entity) | String | 
|   [cases:RelatedItemType](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_service-with-iam.html)  | Filters access by the type of related item. Possible values: Contact, Comment, File, Sla, ConnectCase, Custom | String | 
|   [connect:UserArn](https://docs.aws.amazon.com/connect/latest/APIReference/API_User.html)  | Filters access by connect's UserArn | ARN | 