# GetLexicon

Returns the content of the specified pronunciation lexicon stored
in an AWS Region. For more information, see [Managing Lexicons](managing-lexicons.md "managing-lexicons.md").

## Request Syntax

```
GET /v1/lexicons/`LexiconName` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[LexiconName](#API_GetLexicon_RequestSyntax "#API_GetLexicon_RequestSyntax")**

Name of the lexicon.

Pattern: `[0-9A-Za-z]{1,20}`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Lexicon": {
      "Content": "***string***",
      "Name": "***string***"
   },
   "LexiconAttributes": {
      "Alphabet": "***string***",
      "LanguageCode": "***string***",
      "LastModified": ***number***,
      "LexemesCount": ***number***,
      "LexiconArn": "***string***",
      "Size": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Lexicon](#API_GetLexicon_ResponseSyntax "#API_GetLexicon_ResponseSyntax")**

Lexicon object that provides name and the string content of the
lexicon.

Type: [Lexicon](API_Lexicon.md "API_Lexicon.md") object

**[LexiconAttributes](#API_GetLexicon_ResponseSyntax "#API_GetLexicon_ResponseSyntax")**

Metadata of the lexicon, including phonetic alphabetic used,
language code, lexicon ARN, number of lexemes defined in the lexicon, and
size of lexicon in bytes.

Type: [LexiconAttributes](API_LexiconAttributes.md "API_LexiconAttributes.md") object

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

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/GetLexicon.md "../../../goto/cli2/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/polly-2016-06-10/GetLexicon.md "../../../goto/DotNetSDKV3/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForCpp/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForGoV2/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForJavaV2/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForKotlin/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForPHPV3/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/GetLexicon.md "../../../goto/boto3/polly-2016-06-10/GetLexicon.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/GetLexicon.md "../../../goto/SdkForRubyV3/polly-2016-06-10/GetLexicon.md")
