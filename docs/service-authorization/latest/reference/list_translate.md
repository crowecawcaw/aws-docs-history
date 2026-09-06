

# Actions, resources, and condition keys for Amazon Translate
<a name="list_translate"></a>

Amazon Translate (service prefix: `translate`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/translate/latest/dg/getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/translate/latest/APIReference/API_Operations.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/translate/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/translate/translate.json) for this service.

**Topics**
+ [API operations defined by Amazon Translate](#list_translate-operations)
+ [Actions defined by Amazon Translate](#list_translate-actions-as-permissions)
+ [Resource types defined by Amazon Translate](#list_translate-resources-for-iam-policies)
+ [Condition keys for Amazon Translate](#list_translate-policy-keys)

## API operations defined by Amazon Translate
<a name="list_translate-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_translate-actions-as-permissions).




- **   CreateParallelData  **
  - **IAM action:**  [translate:CreateParallelData](#list_translate-action-CreateParallelData)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [translate:TagResource](#list_translate-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteParallelData  **
  - **IAM action:**  [translate:DeleteParallelData](#list_translate-action-DeleteParallelData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTerminology  **
  - **IAM action:**  [translate:DeleteTerminology](#list_translate-action-DeleteTerminology) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeTextTranslationJob  **
  - **IAM action:**  [translate:DescribeTextTranslationJob](#list_translate-action-DescribeTextTranslationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetParallelData  **
  - **IAM action:**  [translate:GetParallelData](#list_translate-action-GetParallelData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTerminology  **
  - **IAM action:**  [translate:GetTerminology](#list_translate-action-GetTerminology) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportTerminology  **
  - **IAM action:**  [translate:ImportTerminology](#list_translate-action-ImportTerminology)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [translate:TagResource](#list_translate-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   ListLanguages  **
  - **IAM action:**  [translate:ListLanguages](#list_translate-action-ListLanguages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListParallelData  **
  - **IAM action:**  [translate:ListParallelData](#list_translate-action-ListParallelData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [translate:ListTagsForResource](#list_translate-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTerminologies  **
  - **IAM action:**  [translate:ListTerminologies](#list_translate-action-ListTerminologies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTextTranslationJobs  **
  - **IAM action:**  [translate:ListTextTranslationJobs](#list_translate-action-ListTextTranslationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartTextTranslationJob  **
  - **IAM action:**  [translate:StartTextTranslationJob](#list_translate-action-StartTextTranslationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** translate.amazonaws.com / **Access level:** Write

- **   StopTextTranslationJob  **
  - **IAM action:**  [translate:StopTextTranslationJob](#list_translate-action-StopTextTranslationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [translate:TagResource](#list_translate-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   TranslateDocument  **
  - **IAM action:**  [translate:TranslateDocument](#list_translate-action-TranslateDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   TranslateText  **
  - **IAM action:**  [translate:TranslateText](#list_translate-action-TranslateText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   UntagResource  **
  - **IAM action:**  [translate:UntagResource](#list_translate-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateParallelData  **
  - **IAM action:**  [translate:UpdateParallelData](#list_translate-action-UpdateParallelData) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Translate
<a name="list_translate-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_CreateParallelData.html)  **
  - **Description:** Grants permission to create a Parallel Data
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_translate-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_DeleteParallelData.html)  **
  - **Description:** Grants permission to delete a Parallel Data
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_DeleteTerminology.html)  **
  - **Description:** Grants permission to delete a terminology
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_DescribeTextTranslationJob.html)  **
  - **Description:** Grants permission to get the properties associated with an asynchronous batch translation job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_GetParallelData.html)  **
  - **Description:** Grants permission to get a Parallel Data
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_GetTerminology.html)  **
  - **Description:** Grants permission to retrieve a terminology
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ImportTerminology](https://docs.aws.amazon.com/translate/latest/APIReference/API_ImportTerminology.html)  **
  - **Description:** Grants permission to create or update a terminology, depending on whether or not one already exists for the given terminology name
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_translate-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Access level:** Write

- **   [ListLanguages](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListLanguages.html)  **
  - **Description:** Grants permission to list supported languages
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListParallelData.html)  **
  - **Description:** Grants permission to list Parallel Data associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTerminologies](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTerminologies.html)  **
  - **Description:** Grants permission to list terminologies associated with your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTextTranslationJobs](https://docs.aws.amazon.com/translate/latest/APIReference/API_ListTextTranslationJobs.html)  **
  - **Description:** Grants permission to list batch translation jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_StartTextTranslationJob.html)  **
  - **Description:** Grants permission to start an asynchronous batch translation job. Batch translation jobs can be used to translate large volumes of text across multiple documents at once
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTextTranslationJob](https://docs.aws.amazon.com/translate/latest/APIReference/API_StopTextTranslationJob.html)  **
  - **Description:** Grants permission to stop an asynchronous batch translation job that is in progress
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_translate-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_translate-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [TranslateDocument](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateDocument.html)  **
  - **Description:** Grants permission to translate a document from a source language to a target language
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [TranslateText](https://docs.aws.amazon.com/translate/latest/APIReference/API_TranslateText.html)  **
  - **Description:** Grants permission to translate text from a source language to a target language
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [UntagResource](https://docs.aws.amazon.com/translate/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource with given key
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Resource types (\*required):** [terminology](#list_translate-resource-terminology) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_translate-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateParallelData](https://docs.aws.amazon.com/translate/latest/APIReference/API_UpdateParallelData.html)  **
  - **Description:** Grants permission to update an existing Parallel Data
  - **Resource types (\*required):** [parallel-data](#list_translate-resource-parallel-data)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Translate
<a name="list_translate-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [parallel-data](https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-parallel-data.html)  | arn:${Partition}:translate:${Region}:${Account}:parallel-data/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_) | 
|  [terminology](https://docs.aws.amazon.com/translate/latest/dg/how-custom-terminology.html)  | arn:${Partition}:translate:${Region}:${Account}:terminology/${ResourceName} | [aws:ResourceTag/${TagKey}](#list_translate-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Translate
<a name="list_translate-policy-keys"></a>

Amazon Translate defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag values present in a resource creation request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring the presence of mandatory tags in the request | ArrayOfString | 