

# Actions, resources, and condition keys for Amazon Textract
<a name="list_textract"></a>

Amazon Textract (service prefix: `textract`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/textract/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/textract/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/textract/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/textract/textract.json) for this service.

**Topics**
+ [API operations defined by Amazon Textract](#list_textract-operations)
+ [Actions defined by Amazon Textract](#list_textract-actions-as-permissions)
+ [Resource types defined by Amazon Textract](#list_textract-resources-for-iam-policies)
+ [Condition keys for Amazon Textract](#list_textract-policy-keys)

## API operations defined by Amazon Textract
<a name="list_textract-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_textract-actions-as-permissions).




- **   AnalyzeDocument  **
  - **IAM action:**  [textract:AnalyzeDocument](#list_textract-action-AnalyzeDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AnalyzeExpense  **
  - **IAM action:**  [textract:AnalyzeExpense](#list_textract-action-AnalyzeExpense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   AnalyzeID  **
  - **IAM action:**  [textract:AnalyzeID](#list_textract-action-AnalyzeID) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateAdapter  **
  - **IAM action:**  [textract:CreateAdapter](#list_textract-action-CreateAdapter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [textract:TagResource](#list_textract-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateAdapterVersion  **
  - **IAM action:**  [textract:CreateAdapterVersion](#list_textract-action-CreateAdapterVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [textract:TagResource](#list_textract-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteAdapter  **
  - **IAM action:**  [textract:DeleteAdapter](#list_textract-action-DeleteAdapter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAdapterVersion  **
  - **IAM action:**  [textract:DeleteAdapterVersion](#list_textract-action-DeleteAdapterVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DetectDocumentText  **
  - **IAM action:**  [textract:DetectDocumentText](#list_textract-action-DetectDocumentText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAdapter  **
  - **IAM action:**  [textract:GetAdapter](#list_textract-action-GetAdapter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAdapterVersion  **
  - **IAM action:**  [textract:GetAdapterVersion](#list_textract-action-GetAdapterVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentAnalysis  **
  - **IAM action:**  [textract:GetDocumentAnalysis](#list_textract-action-GetDocumentAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDocumentTextDetection  **
  - **IAM action:**  [textract:GetDocumentTextDetection](#list_textract-action-GetDocumentTextDetection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetExpenseAnalysis  **
  - **IAM action:**  [textract:GetExpenseAnalysis](#list_textract-action-GetExpenseAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLendingAnalysis  **
  - **IAM action:**  [textract:GetLendingAnalysis](#list_textract-action-GetLendingAnalysis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLendingAnalysisSummary  **
  - **IAM action:**  [textract:GetLendingAnalysisSummary](#list_textract-action-GetLendingAnalysisSummary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAdapterVersions  **
  - **IAM action:**  [textract:ListAdapterVersions](#list_textract-action-ListAdapterVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAdapters  **
  - **IAM action:**  [textract:ListAdapters](#list_textract-action-ListAdapters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [textract:ListTagsForResource](#list_textract-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartDocumentAnalysis  **
  - **IAM action:**  [textract:StartDocumentAnalysis](#list_textract-action-StartDocumentAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** textract.amazonaws.com / **Access level:** Write

- **   StartDocumentTextDetection  **
  - **IAM action:**  [textract:StartDocumentTextDetection](#list_textract-action-StartDocumentTextDetection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** textract.amazonaws.com / **Access level:** Write

- **   StartExpenseAnalysis  **
  - **IAM action:**  [textract:StartExpenseAnalysis](#list_textract-action-StartExpenseAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** textract.amazonaws.com / **Access level:** Write

- **   StartLendingAnalysis  **
  - **IAM action:**  [textract:StartLendingAnalysis](#list_textract-action-StartLendingAnalysis)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** textract.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [textract:TagResource](#list_textract-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [textract:UntagResource](#list_textract-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateAdapter  **
  - **IAM action:**  [textract:UpdateAdapter](#list_textract-action-UpdateAdapter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Textract
<a name="list_textract-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AnalyzeDocument](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeDocument.html)  **
  - **Description:** Grants permission to detect instances of real-world document entities within an image provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [AnalyzeExpense](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeExpense.html)  **
  - **Description:** Grants permission to detect instances of real-world document entities within an image provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [AnalyzeID](https://docs.aws.amazon.com/textract/latest/dg/API_AnalyzeID.html)  **
  - **Description:** Grants permission to detect relevant information from identity documents provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_CreateAdapter.html)  **
  - **Description:** Grants permission to create an Amazon Textract adapter
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_textract-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Access level:** Write

- **   [CreateAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_CreateAdapterVersion.html)  **
  - **Description:** Grants permission to create an Amazon Textract adapter version
  - **Resource types (\*required):** [adapter\*](#list_textract-resource-adapter)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_textract-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_DeleteAdapter.html)  **
  - **Description:** Grants permission to delete an Amazon Textract adapter
  - **Resource types (\*required):** [adapter\*](#list_textract-resource-adapter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_DeleteAdapterVersion.html)  **
  - **Description:** Grants permission to delete an Amazon Textract adapter version
  - **Resource types (\*required):** [adapterversion\*](#list_textract-resource-adapterversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DetectDocumentText](https://docs.aws.amazon.com/textract/latest/dg/API_DetectDocumentText.html)  **
  - **Description:** Grants permission to detect text in document images
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_GetAdapter.html)  **
  - **Description:** Grants permission to get an Amazon Textract adapter
  - **Resource types (\*required):** [adapter\*](#list_textract-resource-adapter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetAdapterVersion](https://docs.aws.amazon.com/textract/latest/dg/API_GetAdapterVersion.html)  **
  - **Description:** Grants permission to get an Amazon Textract adapter version
  - **Resource types (\*required):** [adapterversion\*](#list_textract-resource-adapterversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetDocumentAnalysis.html)  **
  - **Description:** Grants permission to return information about a document analysis job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/dg/API_GetDocumentTextDetection.html)  **
  - **Description:** Grants permission to return information about a document text detection job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetExpenseAnalysis.html)  **
  - **Description:** Grants permission to return information about an expense analysis job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLendingAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_GetLendingAnalysis.html)  **
  - **Description:** Grants permission to retrieve page-level information regarding a lending analysis job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLendingAnalysisSummary](https://docs.aws.amazon.com/textract/latest/dg/API_GetLendingAnalysisSummary.html)  **
  - **Description:** Grants permission to retrieve summarized information regarding a lending analysis job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAdapterVersions](https://docs.aws.amazon.com/textract/latest/dg/API_ListAdapterVersions.html)  **
  - **Description:** Grants permission to list Amazon Textract adapter versions
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAdapters](https://docs.aws.amazon.com/textract/latest/dg/API_ListAdapters.html)  **
  - **Description:** Grants permission to list Amazon Textract adapters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/textract/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags associated with a resource
  - **Resource types (\*required):** [adapter](#list_textract-resource-adapter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [adapterversion](#list_textract-resource-adapterversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartDocumentAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentAnalysis.html)  **
  - **Description:** Grants permission to start an asynchronous job to detect instances of real-world document entities within an image or pdf provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartDocumentTextDetection](https://docs.aws.amazon.com/textract/latest/dg/API_StartDocumentTextDetection.html)  **
  - **Description:** Grants permission to start an asynchronous job to detect text in document images or pdfs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartExpenseAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartExpenseAnalysis.html)  **
  - **Description:** Grants permission to start an asynchronous job to detect instances of invoices or receipts within an image or pdf provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartLendingAnalysis](https://docs.aws.amazon.com/textract/latest/dg/API_StartLendingAnalysis.html)  **
  - **Description:** Grants permission to start an asynchronous job for detection of entities in a lending document, takes a provided image or PDF as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/textract/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [adapter](#list_textract-resource-adapter) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_textract-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Resource types (\*required):** [adapterversion](#list_textract-resource-adapterversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_textract-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/textract/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [adapter](#list_textract-resource-adapter) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Resource types (\*required):** [adapterversion](#list_textract-resource-adapterversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_textract-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateAdapter](https://docs.aws.amazon.com/textract/latest/dg/API_UpdateAdapter.html)  **
  - **Description:** Grants permission to update Amazon Textract adapter
  - **Resource types (\*required):** [adapter\*](#list_textract-resource-adapter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Textract
<a name="list_textract-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [adapter](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterOverview.html)  | arn:${Partition}:textract:${Region}:${Account}:/adapters/${AdapterId} | [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_) | 
|  [adapterversion](https://docs.aws.amazon.com/textract/latest/dg/API_AdapterVersionOverview.html)  | arn:${Partition}:textract:${Region}:${Account}:/adapters/${AdapterId}/versions/${AdapterVersion} | [aws:ResourceTag/${TagKey}](#list_textract-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Textract
<a name="list_textract-policy-keys"></a>

Amazon Textract defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 