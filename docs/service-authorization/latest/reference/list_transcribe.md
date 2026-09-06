

# Actions, resources, and condition keys for Amazon Transcribe
<a name="list_transcribe"></a>

Amazon Transcribe (service prefix: `transcribe`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/transcribe/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/transcribe/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/transcribe/latest/dg/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/transcribe/transcribe.json) for this service.

**Topics**
+ [API operations defined by Amazon Transcribe](#list_transcribe-operations)
+ [Actions defined by Amazon Transcribe](#list_transcribe-actions-as-permissions)
+ [Resource types defined by Amazon Transcribe](#list_transcribe-resources-for-iam-policies)
+ [Condition keys for Amazon Transcribe](#list_transcribe-policy-keys)

## API operations defined by Amazon Transcribe
<a name="list_transcribe-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_transcribe-actions-as-permissions).




- **   CreateCallAnalyticsCategory  **
  - **IAM action:**  [transcribe:CreateCallAnalyticsCategory](#list_transcribe-action-CreateCallAnalyticsCategory)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLanguageModel  **
  - **IAM action:**  [transcribe:CreateLanguageModel](#list_transcribe-action-CreateLanguageModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   CreateMedicalVocabulary  **
  - **IAM action:**  [transcribe:CreateMedicalVocabulary](#list_transcribe-action-CreateMedicalVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateVocabulary  **
  - **IAM action:**  [transcribe:CreateVocabulary](#list_transcribe-action-CreateVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   CreateVocabularyFilter  **
  - **IAM action:**  [transcribe:CreateVocabularyFilter](#list_transcribe-action-CreateVocabularyFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   DeleteCallAnalyticsCategory  **
  - **IAM action:**  [transcribe:DeleteCallAnalyticsCategory](#list_transcribe-action-DeleteCallAnalyticsCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCallAnalyticsJob  **
  - **IAM action:**  [transcribe:DeleteCallAnalyticsJob](#list_transcribe-action-DeleteCallAnalyticsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLanguageModel  **
  - **IAM action:**  [transcribe:DeleteLanguageModel](#list_transcribe-action-DeleteLanguageModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMedicalScribeJob  **
  - **IAM action:**  [transcribe:DeleteMedicalScribeJob](#list_transcribe-action-DeleteMedicalScribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMedicalTranscriptionJob  **
  - **IAM action:**  [transcribe:DeleteMedicalTranscriptionJob](#list_transcribe-action-DeleteMedicalTranscriptionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMedicalVocabulary  **
  - **IAM action:**  [transcribe:DeleteMedicalVocabulary](#list_transcribe-action-DeleteMedicalVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteTranscriptionJob  **
  - **IAM action:**  [transcribe:DeleteTranscriptionJob](#list_transcribe-action-DeleteTranscriptionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVocabulary  **
  - **IAM action:**  [transcribe:DeleteVocabulary](#list_transcribe-action-DeleteVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVocabularyFilter  **
  - **IAM action:**  [transcribe:DeleteVocabularyFilter](#list_transcribe-action-DeleteVocabularyFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeLanguageModel  **
  - **IAM action:**  [transcribe:DescribeLanguageModel](#list_transcribe-action-DescribeLanguageModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCallAnalyticsCategory  **
  - **IAM action:**  [transcribe:GetCallAnalyticsCategory](#list_transcribe-action-GetCallAnalyticsCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCallAnalyticsJob  **
  - **IAM action:**  [transcribe:GetCallAnalyticsJob](#list_transcribe-action-GetCallAnalyticsJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMedicalScribeJob  **
  - **IAM action:**  [transcribe:GetMedicalScribeJob](#list_transcribe-action-GetMedicalScribeJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMedicalTranscriptionJob  **
  - **IAM action:**  [transcribe:GetMedicalTranscriptionJob](#list_transcribe-action-GetMedicalTranscriptionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMedicalVocabulary  **
  - **IAM action:**  [transcribe:GetMedicalVocabulary](#list_transcribe-action-GetMedicalVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTranscriptionJob  **
  - **IAM action:**  [transcribe:GetTranscriptionJob](#list_transcribe-action-GetTranscriptionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVocabulary  **
  - **IAM action:**  [transcribe:GetVocabulary](#list_transcribe-action-GetVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetVocabularyFilter  **
  - **IAM action:**  [transcribe:GetVocabularyFilter](#list_transcribe-action-GetVocabularyFilter) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListCallAnalyticsCategories  **
  - **IAM action:**  [transcribe:ListCallAnalyticsCategories](#list_transcribe-action-ListCallAnalyticsCategories) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCallAnalyticsJobs  **
  - **IAM action:**  [transcribe:ListCallAnalyticsJobs](#list_transcribe-action-ListCallAnalyticsJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLanguageModels  **
  - **IAM action:**  [transcribe:ListLanguageModels](#list_transcribe-action-ListLanguageModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMedicalScribeJobs  **
  - **IAM action:**  [transcribe:ListMedicalScribeJobs](#list_transcribe-action-ListMedicalScribeJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMedicalTranscriptionJobs  **
  - **IAM action:**  [transcribe:ListMedicalTranscriptionJobs](#list_transcribe-action-ListMedicalTranscriptionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMedicalVocabularies  **
  - **IAM action:**  [transcribe:ListMedicalVocabularies](#list_transcribe-action-ListMedicalVocabularies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [transcribe:ListTagsForResource](#list_transcribe-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTranscriptionJobs  **
  - **IAM action:**  [transcribe:ListTranscriptionJobs](#list_transcribe-action-ListTranscriptionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVocabularies  **
  - **IAM action:**  [transcribe:ListVocabularies](#list_transcribe-action-ListVocabularies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVocabularyFilters  **
  - **IAM action:**  [transcribe:ListVocabularyFilters](#list_transcribe-action-ListVocabularyFilters) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   StartCallAnalyticsJob  **
  - **IAM action:**  [transcribe:StartCallAnalyticsJob](#list_transcribe-action-StartCallAnalyticsJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   StartMedicalScribeJob  **
  - **IAM action:**  [transcribe:StartMedicalScribeJob](#list_transcribe-action-StartMedicalScribeJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   StartMedicalTranscriptionJob  **
  - **IAM action:**  [transcribe:StartMedicalTranscriptionJob](#list_transcribe-action-StartMedicalTranscriptionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartTranscriptionJob  **
  - **IAM action:**  [transcribe:StartTranscriptionJob](#list_transcribe-action-StartTranscriptionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [transcribe:TagResource](#list_transcribe-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [transcribe:UntagResource](#list_transcribe-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateCallAnalyticsCategory  **
  - **IAM action:**  [transcribe:UpdateCallAnalyticsCategory](#list_transcribe-action-UpdateCallAnalyticsCategory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateMedicalVocabulary  **
  - **IAM action:**  [transcribe:UpdateMedicalVocabulary](#list_transcribe-action-UpdateMedicalVocabulary) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVocabulary  **
  - **IAM action:**  [transcribe:UpdateVocabulary](#list_transcribe-action-UpdateVocabulary)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write

- **   UpdateVocabularyFilter  **
  - **IAM action:**  [transcribe:UpdateVocabularyFilter](#list_transcribe-action-UpdateVocabularyFilter)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** transcribe.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Transcribe
<a name="list_transcribe-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CreateCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateCallAnalyticsCategory.html)  **
  - **Description:** Grants permission to create an analytics category. Amazon Transcribe applies the conditions specified by your analytics categories to your call analytics jobs
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLanguageModel](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateLanguageModel.html)  **
  - **Description:** Grants permission to create a new custom language model
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Write

- **   [CreateMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateMedicalVocabulary.html)  **
  - **Description:** Grants permission to create a new custom vocabulary that you can use to change the way Amazon Transcribe Medical handles transcription of an audio file
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabulary.html)  **
  - **Description:** Grants permission to create a new custom vocabulary that you can use to change the way Amazon Transcribe handles transcription of an audio file
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Write

- **   [CreateVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabularyFilter.html)  **
  - **Description:** Grants permission to create a new vocabulary filter that you can use to filter out words from the transcription of an audio file generated by Amazon Transcribe
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteCallAnalyticsCategory.html)  **
  - **Description:** Grants permission to delete a call analytics category using its name from Amazon Transcribe
  - **Resource types (\*required):** [callanalyticscategory\*](#list_transcribe-resource-callanalyticscategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteCallAnalyticsJob.html)  **
  - **Description:** Grants permission to delete a previously submitted call analytics job along with any other generated results such as the transcription, models, and so on
  - **Resource types (\*required):** [callanalyticsjob\*](#list_transcribe-resource-callanalyticsjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLanguageModel](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteLanguageModel.html)  **
  - **Description:** Grants permission to delete a previously created custom language model
  - **Resource types (\*required):** [languagemodel\*](#list_transcribe-resource-languagemodel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteMedicalScribeJob.html)  **
  - **Description:** Grants permission to delete a previously submitted Medical Scribe job
  - **Resource types (\*required):** [medicalscribejob\*](#list_transcribe-resource-medicalscribejob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteMedicalTranscriptionJob.html)  **
  - **Description:** Grants permission to delete a previously submitted medical transcription job
  - **Resource types (\*required):** [medicaltranscriptionjob\*](#list_transcribe-resource-medicaltranscriptionjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteMedicalVocabulary.html)  **
  - **Description:** Grants permission to delete a medical vocabulary from Amazon Transcribe
  - **Resource types (\*required):** [medicalvocabulary\*](#list_transcribe-resource-medicalvocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteTranscriptionJob.html)  **
  - **Description:** Grants permission to delete a previously submitted transcription job along with any other generated results such as the transcription, models, and so on
  - **Resource types (\*required):** [transcriptionjob\*](#list_transcribe-resource-transcriptionjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteVocabulary.html)  **
  - **Description:** Grants permission to delete a vocabulary from Amazon Transcribe
  - **Resource types (\*required):** [vocabulary\*](#list_transcribe-resource-vocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_DeleteVocabularyFilter.html)  **
  - **Description:** Grants permission to delete a vocabulary filter from Amazon Transcribe
  - **Resource types (\*required):** [vocabularyfilter\*](#list_transcribe-resource-vocabularyfilter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeLanguageModel](https://docs.aws.amazon.com/transcribe/latest/dg/API_DescribeLanguageModel.html)  **
  - **Description:** Grants permission to return information about a custom language model
  - **Resource types (\*required):** [languagemodel\*](#list_transcribe-resource-languagemodel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetCallAnalyticsCategory.html)  **
  - **Description:** Grants permission to retrieve information about a call analytics category
  - **Resource types (\*required):** [callanalyticscategory\*](#list_transcribe-resource-callanalyticscategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetCallAnalyticsJob.html)  **
  - **Description:** Grants permission to return information about a call analytics job
  - **Resource types (\*required):** [callanalyticsjob\*](#list_transcribe-resource-callanalyticsjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetMedicalScribeJob.html)  **
  - **Description:** Grants permission to return information about a Medical Scribe job
  - **Resource types (\*required):** [medicalscribejob\*](#list_transcribe-resource-medicalscribejob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_GetMedicalScribeStream.html)  **
  - **Description:** Grants permission to get information about the specified AWS HealthScribe streaming session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetMedicalTranscriptionJob.html)  **
  - **Description:** Grants permission to return information about a medical transcription job
  - **Resource types (\*required):** [medicaltranscriptionjob\*](#list_transcribe-resource-medicaltranscriptionjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetMedicalVocabulary.html)  **
  - **Description:** Grants permission to get information about a medical vocabulary
  - **Resource types (\*required):** [medicalvocabulary\*](#list_transcribe-resource-medicalvocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetTranscriptionJob.html)  **
  - **Description:** Grants permission to return information about a transcription job
  - **Resource types (\*required):** [transcriptionjob\*](#list_transcribe-resource-transcriptionjob)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetVocabulary.html)  **
  - **Description:** Grants permission to to get information about a vocabulary
  - **Resource types (\*required):** [vocabulary\*](#list_transcribe-resource-vocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_GetVocabularyFilter.html)  **
  - **Description:** Grants permission to get information about a vocabulary filter
  - **Resource types (\*required):** [vocabularyfilter\*](#list_transcribe-resource-vocabularyfilter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListCallAnalyticsCategories](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListCallAnalyticsCategories.html)  **
  - **Description:** Grants permission to list call analytics categories that has been created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCallAnalyticsJobs](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListCallAnalyticsJobs.html)  **
  - **Description:** Grants permission to list call analytics jobs with the specified status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLanguageModels](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListLanguageModels.html)  **
  - **Description:** Grants permission to list custom language models
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMedicalScribeJobs](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListMedicalScribeJobs.html)  **
  - **Description:** Grants permission to list Medical Scribe jobs with the specified status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMedicalTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListMedicalTranscriptionJobs.html)  **
  - **Description:** Grants permission to list medical transcription jobs with the specified status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMedicalVocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListMedicalVocabularies.html)  **
  - **Description:** Grants permission to return a list of medical vocabularies that match the specified criteria. If no criteria are specified, returns the entire list of vocabularies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTranscriptionJobs](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListTranscriptionJobs.html)  **
  - **Description:** Grants permission to list transcription jobs with the specified status
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVocabularies](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListVocabularies.html)  **
  - **Description:** Grants permission to return a list of vocabularies that match the specified criteria. If no criteria are specified, returns the entire list of vocabularies
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVocabularyFilters](https://docs.aws.amazon.com/transcribe/latest/dg/API_ListVocabularyFilters.html)  **
  - **Description:** Grants permission to return a list of vocabulary filters that match the specified criteria. If no criteria are specified, returns the at most 5 vocabulary filters
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartCallAnalyticsJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_StartCallAnalyticsJob.html)  **
  - **Description:** Grants permission to start an asynchronous analytics job that not only transcribes the audio recording of a caller and agent, but also returns additional insights
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)<br />[transcribe:OutputEncryptionKMSKeyId](#list_transcribe-transcribe_OutputEncryptionKMSKeyId)<br />[transcribe:OutputLocation](#list_transcribe-transcribe_OutputLocation)
  - **Access level:** Write

- **   [StartCallAnalyticsStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartCallAnalyticsStreamTranscription.html)  **
  - **Description:** Grants permission to start a protocol where audio is streamed to Transcribe Call Analytics and the transcription results are streamed to your application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartCallAnalyticsStreamTranscriptionWebSocket](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartCallAnalyticsStreamTranscriptionWebSocket.html)  **
  - **Description:** Grants permission to start a WebSocket where audio is streamed to Transcribe Call Analytics and the transcription results are streamed to your application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_StartMedicalScribeJob.html)  **
  - **Description:** Grants permission to start an asynchronous job to transcribe patient-clinician conversations and generates clinical notes
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)<br />[transcribe:OutputBucketName](#list_transcribe-transcribe_OutputBucketName)<br />[transcribe:OutputEncryptionKMSKeyId](#list_transcribe-transcribe_OutputEncryptionKMSKeyId)
  - **Access level:** Write

- **   [StartMedicalScribeStream](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartMedicalScribeStream.html)  **
  - **Description:** Grants permission to start a bidirectional HTTP2 stream where audio is streamed to AWS HealthScribe and the transcription results are streamed to your application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMedicalStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartMedicalStreamTranscription.html)  **
  - **Description:** Grants permission to start a protocol where audio is streamed to Transcribe Medical and the transcription results are streamed to your application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMedicalStreamTranscriptionWebSocket](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartMedicalStreamTranscriptionWebSocket.html)  **
  - **Description:** Grants permission to start a WebSocket where audio is streamed to Transcribe Medical and the transcription results are streamed to your application
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMedicalTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_StartMedicalTranscriptionJob.html)  **
  - **Description:** Grants permission to start an asynchronous job to transcribe medical speech to text
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)<br />[transcribe:OutputBucketName](#list_transcribe-transcribe_OutputBucketName)<br />[transcribe:OutputEncryptionKMSKeyId](#list_transcribe-transcribe_OutputEncryptionKMSKeyId)<br />[transcribe:OutputKey](#list_transcribe-transcribe_OutputKey)
  - **Access level:** Write

- **   [StartStreamTranscription](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartStreamTranscription.html)  **
  - **Description:** Grants permission to start a bidirectional HTTP2 stream to transcribe speech to text in real time
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartStreamTranscriptionWebSocket](https://docs.aws.amazon.com/transcribe/latest/dg/API_streaming_StartStreamTranscriptionWebSocket.html)  **
  - **Description:** Grants permission to start a websocket stream to transcribe speech to text in real time
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartTranscriptionJob](https://docs.aws.amazon.com/transcribe/latest/dg/API_StartTranscriptionJob.html)  **
  - **Description:** Grants permission to start an asynchronous job to transcribe speech to text
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)<br />[transcribe:OutputBucketName](#list_transcribe-transcribe_OutputBucketName)<br />[transcribe:OutputEncryptionKMSKeyId](#list_transcribe-transcribe_OutputEncryptionKMSKeyId)<br />[transcribe:OutputKey](#list_transcribe-transcribe_OutputKey)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/transcribe/latest/dg/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_transcribe-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_transcribe-aws_TagKeys)<br />[transcribe:OutputBucketName](#list_transcribe-transcribe_OutputBucketName)<br />[transcribe:OutputEncryptionKMSKeyId](#list_transcribe-transcribe_OutputEncryptionKMSKeyId)<br />[transcribe:OutputKey](#list_transcribe-transcribe_OutputKey)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/transcribe/latest/dg/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource with given key
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:TagKeys](#list_transcribe-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateCallAnalyticsCategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_UpdateCallAnalyticsCategory.html)  **
  - **Description:** Grants permission to update the call analytics category with new values. The UpdateCallAnalyticsCategory operation overwrites all of the existing information with the values that you provide in the request
  - **Resource types (\*required):** [callanalyticscategory\*](#list_transcribe-resource-callanalyticscategory)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateMedicalVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_UpdateMedicalVocabulary.html)  **
  - **Description:** Grants permission to update an existing medical vocabulary with new values. The UpdateMedicalVocabulary operation overwrites all of the existing information with the values that you provide in the request
  - **Resource types (\*required):** [medicalvocabulary\*](#list_transcribe-resource-medicalvocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_UpdateVocabulary.html)  **
  - **Description:** Grants permission to update an existing vocabulary with new values. The UpdateVocabulary operation overwrites all of the existing information with the values that you provide in the request
  - **Resource types (\*required):** [vocabulary\*](#list_transcribe-resource-vocabulary)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVocabularyFilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_UpdateVocabularyFilter.html)  **
  - **Description:** Grants permission to update an existing vocabulary filter with new values. The UpdateVocabularyFilter operation overwrites all of the existing information with the values that you provide in the request
  - **Resource types (\*required):** [vocabularyfilter\*](#list_transcribe-resource-vocabularyfilter)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Transcribe
<a name="list_transcribe-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [callanalyticscategory](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateCallAnalyticsCategory.html)  | arn:${Partition}:transcribe:${Region}:${Account}:analytics-category/${CategoryName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [callanalyticsjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_CallAnalyticsJob.html)  | arn:${Partition}:transcribe:${Region}:${Account}:analytics/${JobName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [languagemodel](https://docs.aws.amazon.com/transcribe/latest/dg/API_LanguageModel.html)  | arn:${Partition}:transcribe:${Region}:${Account}:language-model/${ModelName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [medicalscribejob](https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalScribeJob.html)  | arn:${Partition}:transcribe:${Region}:${Account}:medical-scribe-job/${JobName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [medicaltranscriptionjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_MedicalTranscriptionJob.html)  | arn:${Partition}:transcribe:${Region}:${Account}:medical-transcription-job/${JobName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [medicalvocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateMedicalVocabulary.html)  | arn:${Partition}:transcribe:${Region}:${Account}:medical-vocabulary/${VocabularyName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [transcriptionjob](https://docs.aws.amazon.com/transcribe/latest/dg/API_TranscriptionJob.html)  | arn:${Partition}:transcribe:${Region}:${Account}:transcription-job/${JobName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [vocabulary](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabulary.html)  | arn:${Partition}:transcribe:${Region}:${Account}:vocabulary/${VocabularyName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 
|  [vocabularyfilter](https://docs.aws.amazon.com/transcribe/latest/dg/API_CreateVocabularyFilter.html)  | arn:${Partition}:transcribe:${Region}:${Account}:vocabulary-filter/${VocabularyFilterName} | [aws:ResourceTag/${TagKey}](#list_transcribe-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Transcribe
<a name="list_transcribe-policy-keys"></a>

Amazon Transcribe defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag values present in a resource creation request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring the presence of mandatory tags in the request | ArrayOfString | 
|   [transcribe:OutputBucketName](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazontranscribe.html#amazontranscribe-policy-keys)  | Filters access based on the output bucket name included in the request | String | 
|   [transcribe:OutputEncryptionKMSKeyId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazontranscribe.html#amazontranscribe-policy-keys)  | Filters access based on the KMS key id included in the request, provided in the form of a KMS key ARN | String | 
|   [transcribe:OutputKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazontranscribe.html#amazontranscribe-policy-keys)  | Filters access based on the output key included in the request | String | 
|   [transcribe:OutputLocation](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazontranscribe.html#amazontranscribe-policy-keys)  | Filters access based on the output location included in the request | String | 