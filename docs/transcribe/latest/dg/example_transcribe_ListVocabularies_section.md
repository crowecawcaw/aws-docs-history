# Use `ListVocabularies` with an AWS SDK or CLI

The following code examples show how to use `ListVocabularies`.

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
    /// List custom vocabularies for the current account. Optionally specify a name
    /// filter and a specific state to filter the vocabularies list.
    /// </summary>
    /// <param name="nameContains">Optional string the vocabulary name must contain.</param>
    /// <param name="stateEquals">Optional state of the vocabulary.</param>
    /// <returns>List of information about the vocabularies.</returns>
    public async Task<List<VocabularyInfo>> ListCustomVocabularies(string? nameContains = null,
        VocabularyState? stateEquals = null)
    {
        var response = await _amazonTranscribeService.ListVocabulariesAsync(
            new ListVocabulariesRequest()
            {
                NameContains = nameContains,
                StateEquals = stateEquals
            });
        return response.Vocabularies;
    }



```

- For API details, see
  [ListVocabularies](../../../goto/DotNetSDKV3/transcribe-2017-10-26/ListVocabularies.md "../../../goto/DotNetSDKV3/transcribe-2017-10-26/ListVocabularies.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

**To list your custom vocabularies**

The following `list-vocabularies` example lists the custom vocabularies associated with your AWS account and Region.

```
`aws transcribe list-vocabularies`

```

Output:

```
{
    "NextToken": "NextToken",
    "Vocabularies": [
        {
            "VocabularyName": "ards-test-1",
            "LanguageCode": "language-code",
            "LastModifiedTime": "2020-04-27T22:00:27.330000+00:00",
            "VocabularyState": "READY"
        },
        {
            "VocabularyName": "sample-test",
            "LanguageCode": "language-code",
            "LastModifiedTime": "2020-04-24T23:04:11.044000+00:00",
            "VocabularyState": "READY"
        },
        {
            "VocabularyName": "CRLF-to-LF-test-3-1",
            "LanguageCode": "language-code",
            "LastModifiedTime": "2020-04-24T22:12:22.277000+00:00",
            "VocabularyState": "READY"
        },
        {
            "VocabularyName": "CRLF-to-LF-test-2",
            "LanguageCode": "language-code",
            "LastModifiedTime": "2020-04-24T21:53:50.455000+00:00",
            "VocabularyState": "READY"
        },
        {
            "VocabularyName": "CRLF-to-LF-1-1",
            "LanguageCode": "language-code",
            "LastModifiedTime": "2020-04-24T21:39:33.356000+00:00",
            "VocabularyState": "READY"
        }
    ]
}
```

For more information, see [Custom Vocabularies](how-vocabulary.md "how-vocabulary.md") in the _Amazon Transcribe Developer Guide_.

- For API details, see
  [ListVocabularies](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabularies.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-vocabularies.html")
  in _AWS CLI Command Reference_.

Python

**SDK for Python (Boto3)**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/transcribe#code-examples").

```
def list_vocabularies(vocabulary_filter, transcribe_client):
    """
    Lists the custom vocabularies created for this AWS account.

    :param vocabulary_filter: The returned vocabularies must contain this string in
                              their names.
    :param transcribe_client: The Boto3 Transcribe client.
    :return: The list of retrieved vocabularies.
    """
    try:
        response = transcribe_client.list_vocabularies(NameContains=vocabulary_filter)
        vocabs = response["Vocabularies"]
        next_token = response.get("NextToken")
        while next_token is not None:
            response = transcribe_client.list_vocabularies(
                NameContains=vocabulary_filter, NextToken=next_token
            )
            vocabs += response["Vocabularies"]
            next_token = response.get("NextToken")
        logger.info(
            "Got %s vocabularies with filter %s.", len(vocabs), vocabulary_filter
        )
    except ClientError:
        logger.exception(
            "Couldn't list vocabularies with filter %s.", vocabulary_filter
        )
        raise
    else:
        return vocabs




```

- For API details, see
  [ListVocabularies](../../../goto/boto3/transcribe-2017-10-26/ListVocabularies.md "../../../goto/boto3/transcribe-2017-10-26/ListVocabularies.md")
  in _AWS SDK for Python (Boto3) API Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](getting-started-sdk.md#sdk-general-information-section "getting-started-sdk.md#sdk-general-information-section").
This topic also includes information about getting started and details about previous SDK versions.
