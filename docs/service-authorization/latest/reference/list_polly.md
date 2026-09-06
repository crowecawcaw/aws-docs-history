

# Actions, resources, and condition keys for Amazon Polly
<a name="list_polly"></a>

Amazon Polly (service prefix: `polly`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/polly/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/polly/latest/dg/API_Reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/polly/latest/dg/security_iam_service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/polly/polly.json) for this service.

**Topics**
+ [API operations defined by Amazon Polly](#list_polly-operations)
+ [Actions defined by Amazon Polly](#list_polly-actions-as-permissions)
+ [Resource types defined by Amazon Polly](#list_polly-resources-for-iam-policies)
+ [Condition keys for Amazon Polly](#list_polly-policy-keys)

## API operations defined by Amazon Polly
<a name="list_polly-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_polly-actions-as-permissions).




- **   DeleteLexicon  **
  - **IAM action:**  [polly:DeleteLexicon](#list_polly-action-DeleteLexicon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeVoices  **
  - **IAM action:**  [polly:DescribeVoices](#list_polly-action-DescribeVoices) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetLexicon  **
  - **IAM action:**  [polly:GetLexicon](#list_polly-action-GetLexicon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSpeechSynthesisTask  **
  - **IAM action:**  [polly:GetSpeechSynthesisTask](#list_polly-action-GetSpeechSynthesisTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListLexicons  **
  - **IAM action:**  [polly:ListLexicons](#list_polly-action-ListLexicons) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSpeechSynthesisTasks  **
  - **IAM action:**  [polly:ListSpeechSynthesisTasks](#list_polly-action-ListSpeechSynthesisTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutLexicon  **
  - **IAM action:**  [polly:PutLexicon](#list_polly-action-PutLexicon) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSpeechSynthesisStream  **
  - **IAM action:**  [polly:StartSpeechSynthesisStream](#list_polly-action-StartSpeechSynthesisStream) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartSpeechSynthesisTask  **
  - **IAM action:**  [polly:StartSpeechSynthesisTask](#list_polly-action-StartSpeechSynthesisTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   SynthesizeSpeech  **
  - **IAM action:**  [polly:SynthesizeSpeech](#list_polly-action-SynthesizeSpeech) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read



## Actions defined by Amazon Polly
<a name="list_polly-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [DeleteLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_DeleteLexicon.html)  **
  - **Description:** Grants permission to delete the specified pronunciation lexicon stored in an AWS Region
  - **Resource types (\*required):** [lexicon\*](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DescribeVoices](https://docs.aws.amazon.com/polly/latest/dg/API_DescribeVoices.html)  **
  - **Description:** Grants permission to describe the list of voices that are available for use when requesting speech synthesis
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [GetLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_GetLexicon.html)  **
  - **Description:** Grants permission to retrieve the content of the specified pronunciation lexicon stored in an AWS Region
  - **Resource types (\*required):** [lexicon\*](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_GetSpeechSynthesisTask.html)  **
  - **Description:** Grants permission to get information about specific speech synthesis task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListLexicons](https://docs.aws.amazon.com/polly/latest/dg/API_ListLexicons.html)  **
  - **Description:** Grants permission to list the pronunciation lexicons stored in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSpeechSynthesisTasks](https://docs.aws.amazon.com/polly/latest/dg/API_ListSpeechSynthesisTasks.html)  **
  - **Description:** Grants permission to list requested speech synthesis tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutLexicon](https://docs.aws.amazon.com/polly/latest/dg/API_PutLexicon.html)  **
  - **Description:** Grants permission to store a pronunciation lexicon in an AWS Region
  - **Resource types (\*required):** [lexicon\*](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartSpeechSynthesisStream](https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisStream.html)  **
  - **Description:** Grants permission to perform synthesis with bidirectional streaming
  - **Resource types (\*required):** [lexicon](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartSpeechSynthesisTask](https://docs.aws.amazon.com/polly/latest/dg/API_StartSpeechSynthesisTask.html)  **
  - **Description:** Grants permission to synthesize long inputs to the provided S3 location
  - **Resource types (\*required):** [lexicon](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SynthesizeSpeech](https://docs.aws.amazon.com/polly/latest/dg/API_SynthesizeSpeech.html)  **
  - **Description:** Grants permission to synthesize speech
  - **Resource types (\*required):** [lexicon](#list_polly-resource-lexicon)
  - **Condition keys:**  
  - **Access level:** Read



## Resource types defined by Amazon Polly
<a name="list_polly-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [lexicon](https://docs.aws.amazon.com/polly/latest/dg/managing-lexicons.html)  | arn:${Partition}:polly:${Region}:${Account}:lexicon/${LexiconName} |   | 

## Condition keys for Amazon Polly
<a name="list_polly-policy-keys"></a>

Amazon Polly has no service-specific condition keys that can be used in the `Condition` element of policy statements.