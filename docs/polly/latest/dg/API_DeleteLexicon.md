# DeleteLexicon

Deletes the specified pronunciation lexicon stored in an AWS Region. A lexicon which has been deleted is not available for
speech synthesis, nor is it possible to retrieve it using either the
`GetLexicon` or `ListLexicon` APIs.

For more information, see [Managing Lexicons](managing-lexicons.md "managing-lexicons.md").

## Request Syntax

```
DELETE /v1/lexicons/`LexiconName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[LexiconName](#API_DeleteLexicon_RequestSyntax "#API_DeleteLexicon_RequestSyntax")**

The name of the lexicon to delete. Must be an existing lexicon in
the region.

Pattern: `[0-9A-Za-z]{1,20}`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**LexiconNotFoundException**

Amazon Polly can't find the specified lexicon. This could be caused by a
lexicon that is missing, its name is misspelled or specifying a lexicon
that is in a different region.

Verify that the lexicon exists, is in the region (see [ListLexicons](API_ListLexicons.md "API_ListLexicons.md")) and that you spelled its name is spelled
correctly. Then try again.

HTTP Status Code: 404

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/DeleteLexicon.md "../../../goto/cli2/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/polly-2016-06-10/DeleteLexicon.md "../../../goto/DotNetSDKV4/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForCpp/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForGoV2/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForJavaV2/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForKotlin/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForPHPV3/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/DeleteLexicon.md "../../../goto/boto3/polly-2016-06-10/DeleteLexicon.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/DeleteLexicon.md "../../../goto/SdkForRubyV3/polly-2016-06-10/DeleteLexicon.md")
