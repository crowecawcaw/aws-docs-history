# Use `DeleteVocabulary` with an AWS SDK or CLI

The following code examples show how to use `DeleteVocabulary`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in
context in the following code example:

- [Create and refine a custom vocabulary](example_transcribe_Scenario_CustomVocabulary_section.md "example_transcribe_Scenario_CustomVocabulary_section.md")

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/Transcribe#code-examples").

```

    /// <summary>
    /// Delete an existing custom vocabulary.
    /// </summary>
    /// <param name="vocabularyName">Name of the vocabulary to delete.</param>
    /// <returns>True if successful.</returns>
    public async Task<bool> DeleteCustomVocabulary(string vocabularyName)
    {
        var response = await _amazonTranscribeService.DeleteVocabularyAsync(
            new DeleteVocabularyRequest
            {
                VocabularyName = vocabularyName
            });
        return response.HttpStatusCode == HttpStatusCode.OK;
    }



```

- For API details, see
  [DeleteVocabulary](../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteVocabulary.md "../../../goto/DotNetSDKV3/transcribe-2017-10-26/DeleteVocabulary.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To delete a custom vocabulary**

The following `delete-vocabulary` example deletes a custom vocabulary.

```
`aws transcribe delete-vocabulary \
 --`vocabulary-name` vocabulary-name`

```

This command produces no output.

For more information, see [Custom Vocabularies](how-vocabulary.md "how-vocabulary.md") in the _Amazon Transcribe Developer Guide_.

- For API details, see
  [DeleteVocabulary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/delete-vocabulary.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples").

```
def delete_vocabulary(vocabulary_name, transcribe_client):
    """
    Deletes a custom vocabulary.

    :param vocabulary_name: The name of the vocabulary to delete.
    :param transcribe_client: The Boto3 Transcribe client.
    """
    try:
        transcribe_client.delete_vocabulary(VocabularyName=vocabulary_name)
        logger.info("Deleted vocabulary %s.", vocabulary_name)
    except ClientError:
        logger.exception("Couldn't delete vocabulary %s.", vocabulary_name)
        raise




```

- For API details, see
  [DeleteVocabulary](../../../goto/boto3/transcribe-2017-10-26/DeleteVocabulary.md "../../../goto/boto3/transcribe-2017-10-26/DeleteVocabulary.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](getting-started-sdk.md#sdk-general-information-section "getting-started-sdk.md#sdk-general-information-section").
This topic also includes information about getting started and details about previous SDK versions.
