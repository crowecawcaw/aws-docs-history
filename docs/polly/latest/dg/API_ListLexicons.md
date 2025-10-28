# ListLexicons

Returns a list of pronunciation lexicons stored in an AWS Region. For more information, see [Managing Lexicons](managing-lexicons.md "managing-lexicons.md").

## Request Syntax

```
GET /v1/lexicons?NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[NextToken](#API_ListLexicons_RequestSyntax "#API_ListLexicons_RequestSyntax")**

An opaque pagination token returned from previous
`ListLexicons` operation. If present, indicates where to
continue the list of lexicons.

Length Constraints: Minimum length of 0. Maximum length of 4096.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Lexicons": [
      {
         "Attributes": {
            "Alphabet": "***string***",
            "LanguageCode": "***string***",
            "LastModified": ***number***,
            "LexemesCount": ***number***,
            "LexiconArn": "***string***",
            "Size": ***number***
         },
         "Name": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Lexicons](#API_ListLexicons_ResponseSyntax "#API_ListLexicons_ResponseSyntax")**

A list of lexicon names and attributes.

Type: Array of [LexiconDescription](API_LexiconDescription.md "API_LexiconDescription.md") objects

**[NextToken](#API_ListLexicons_ResponseSyntax "#API_ListLexicons_ResponseSyntax")**

The pagination token to use in the next request to continue the
listing of lexicons. `NextToken` is returned only if the
response is truncated.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 4096.

## Errors

**InvalidNextTokenException**

The NextToken is invalid. Verify that it's spelled correctly, and
then try again.

HTTP Status Code: 400

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/ListLexicons.md "../../../goto/cli2/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/polly-2016-06-10/ListLexicons.md "../../../goto/DotNetSDKV3/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForCpp/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForGoV2/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForJavaV2/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForKotlin/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForPHPV3/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/ListLexicons.md "../../../goto/boto3/polly-2016-06-10/ListLexicons.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/ListLexicons.md "../../../goto/SdkForRubyV3/polly-2016-06-10/ListLexicons.md")
