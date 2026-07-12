# Actions, resources, and condition keys for Amazon Polly

Amazon Polly (service prefix: `polly`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../polly/latest/dg.md "../../../polly/latest/dg.md").
- View a list of the [API operations available for
  this service](../../../polly/latest/dg/API_Reference.md "../../../polly/latest/dg/API_Reference.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../polly/latest/dg/security_iam_service-with-iam.md "../../../polly/latest/dg/security_iam_service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/polly/polly.json "https://servicereference.us-east-1.amazonaws.com/v1/polly/polly.json") for this service.

###### Topics

- [API operations defined by Amazon Polly](#list_polly-operations "#list_polly-operations")
- [Actions defined by Amazon Polly](#list_polly-actions-as-permissions "#list_polly-actions-as-permissions")
- [Resource types defined by Amazon Polly](#list_polly-resources-for-iam-policies "#list_polly-resources-for-iam-policies")
- [Condition keys for Amazon Polly](#list_polly-policy-keys "#list_polly-policy-keys")

## API operations defined by Amazon Polly

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_polly-actions-as-permissions "#list_polly-actions-as-permissions").

| Operation                  | IAM action                                                                                                                        | Condition key | Possible value(s) | Access level |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| DeleteLexicon              | [polly:DeleteLexicon](#list_polly-action-DeleteLexicon "#list_polly-action-DeleteLexicon")                                        |               |                   | Write        |
| DescribeVoices             | [polly:DescribeVoices](#list_polly-action-DescribeVoices "#list_polly-action-DescribeVoices")                                     |               |                   | List         |
| GetLexicon                 | [polly:GetLexicon](#list_polly-action-GetLexicon "#list_polly-action-GetLexicon")                                                 |               |                   | Read         |
| GetSpeechSynthesisTask     | [polly:GetSpeechSynthesisTask](#list_polly-action-GetSpeechSynthesisTask "#list_polly-action-GetSpeechSynthesisTask")             |               |                   | Read         |
| ListLexicons               | [polly:ListLexicons](#list_polly-action-ListLexicons "#list_polly-action-ListLexicons")                                           |               |                   | List         |
| ListSpeechSynthesisTasks   | [polly:ListSpeechSynthesisTasks](#list_polly-action-ListSpeechSynthesisTasks "#list_polly-action-ListSpeechSynthesisTasks")       |               |                   | List         |
| PutLexicon                 | [polly:PutLexicon](#list_polly-action-PutLexicon "#list_polly-action-PutLexicon")                                                 |               |                   | Write        |
| StartSpeechSynthesisStream | [polly:StartSpeechSynthesisStream](#list_polly-action-StartSpeechSynthesisStream "#list_polly-action-StartSpeechSynthesisStream") |               |                   | Read         |
| StartSpeechSynthesisTask   | [polly:StartSpeechSynthesisTask](#list_polly-action-StartSpeechSynthesisTask "#list_polly-action-StartSpeechSynthesisTask")       |               |                   | Write        |
| SynthesizeSpeech           | [polly:SynthesizeSpeech](#list_polly-action-SynthesizeSpeech "#list_polly-action-SynthesizeSpeech")                               |               |                   | Read         |

## Actions defined by Amazon Polly

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                               | Description                                                                                                  | Resource types (\*required)                                              | Condition keys | Access level |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | -------------- | ------------ |
| [DeleteLexicon](../../../polly/latest/dg/API_DeleteLexicon.md "../../../polly/latest/dg/API_DeleteLexicon.md")                                        | Grants permission to delete the specified pronunciation lexicon stored in an AWS Region                      | [lexicon\*](#list_polly-resource-lexicon "#list_polly-resource-lexicon") |                | Write        |
| [DescribeVoices](../../../polly/latest/dg/API_DescribeVoices.md "../../../polly/latest/dg/API_DescribeVoices.md")                                     | Grants permission to describe the list of voices that are available for use when requesting speech synthesis |                                                                          |                | List         |
| [GetLexicon](../../../polly/latest/dg/API_GetLexicon.md "../../../polly/latest/dg/API_GetLexicon.md")                                                 | Grants permission to retrieve the content of the specified pronunciation lexicon stored in an AWS Region     | [lexicon\*](#list_polly-resource-lexicon "#list_polly-resource-lexicon") |                | Read         |
| [GetSpeechSynthesisTask](../../../polly/latest/dg/API_GetSpeechSynthesisTask.md "../../../polly/latest/dg/API_GetSpeechSynthesisTask.md")             | Grants permission to get information about specific speech synthesis task                                    |                                                                          |                | Read         |
| [ListLexicons](../../../polly/latest/dg/API_ListLexicons.md "../../../polly/latest/dg/API_ListLexicons.md")                                           | Grants permission to list the pronunciation lexicons stored in an AWS Region                                 |                                                                          |                | List         |
| [ListSpeechSynthesisTasks](../../../polly/latest/dg/API_ListSpeechSynthesisTasks.md "../../../polly/latest/dg/API_ListSpeechSynthesisTasks.md")       | Grants permission to list requested speech synthesis tasks                                                   |                                                                          |                | List         |
| [PutLexicon](../../../polly/latest/dg/API_PutLexicon.md "../../../polly/latest/dg/API_PutLexicon.md")                                                 | Grants permission to store a pronunciation lexicon in an AWS Region                                          | [lexicon\*](#list_polly-resource-lexicon "#list_polly-resource-lexicon") |                | Write        |
| [StartSpeechSynthesisStream](../../../polly/latest/dg/API_StartSpeechSynthesisStream.md "../../../polly/latest/dg/API_StartSpeechSynthesisStream.md") | Grants permission to perform synthesis with bidirectional streaming                                          | [lexicon](#list_polly-resource-lexicon "#list_polly-resource-lexicon")   |                | Read         |
| [StartSpeechSynthesisTask](../../../polly/latest/dg/API_StartSpeechSynthesisTask.md "../../../polly/latest/dg/API_StartSpeechSynthesisTask.md")       | Grants permission to synthesize long inputs to the provided S3 location                                      | [lexicon](#list_polly-resource-lexicon "#list_polly-resource-lexicon")   |                | Write        |
| [SynthesizeSpeech](../../../polly/latest/dg/API_SynthesizeSpeech.md "../../../polly/latest/dg/API_SynthesizeSpeech.md")                               | Grants permission to synthesize speech                                                                       | [lexicon](#list_polly-resource-lexicon "#list_polly-resource-lexicon")   |                | Read         |

## Resource types defined by Amazon Polly

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                           | ARN                                                                | Condition keys |
| -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------- |
| [lexicon](../../../polly/latest/dg/managing-lexicons.md "../../../polly/latest/dg/managing-lexicons.md") | arn:${Partition}:polly:${Region}:${Account}:lexicon/${LexiconName} |                |

## Condition keys for Amazon Polly

Amazon Polly has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
