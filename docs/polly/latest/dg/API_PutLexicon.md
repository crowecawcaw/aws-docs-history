# PutLexicon

Stores a pronunciation lexicon in an AWS Region. If
a lexicon with the same name already exists in the region, it is
overwritten by the new lexicon. Lexicon operations have eventual
consistency, therefore, it might take some time before the lexicon is
available to the SynthesizeSpeech operation.

For more information, see [Managing Lexicons](managing-lexicons.md "managing-lexicons.md").

## Request Syntax

```
PUT /v1/lexicons/`LexiconName` HTTP/1.1
Content-type: application/json

{
   "Content": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[LexiconName](#API_PutLexicon_RequestSyntax "#API_PutLexicon_RequestSyntax")**

Name of the lexicon. The name must follow the regular express
format [0-9A-Za-z]{1,20}. That is, the name is a case-sensitive
alphanumeric string up to 20 characters long.

Pattern: `[0-9A-Za-z]{1,20}`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Content](#API_PutLexicon_RequestSyntax "#API_PutLexicon_RequestSyntax")**

Content of the PLS lexicon as string data.

Type: String

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidLexiconException**

Amazon Polly can't find the specified lexicon. Verify that the lexicon's
name is spelled correctly, and then try again.

HTTP Status Code: 400

**LexiconSizeExceededException**

The maximum size of the specified lexicon would be exceeded by this
operation.

HTTP Status Code: 400

**MaxLexemeLengthExceededException**

The maximum size of the lexeme would be exceeded by this
operation.

HTTP Status Code: 400

**MaxLexiconsNumberExceededException**

The maximum number of lexicons would be exceeded by this
operation.

HTTP Status Code: 400

**ServiceFailureException**

An unknown condition has caused a service failure.

HTTP Status Code: 500

**UnsupportedPlsAlphabetException**

The alphabet specified by the lexicon is not a supported alphabet.
Valid values are `x-sampa` and `ipa`.

HTTP Status Code: 400

**UnsupportedPlsLanguageException**

The language specified in the lexicon is unsupported. For a list of
supported languages, see [Lexicon Attributes](API_LexiconAttributes.md "API_LexiconAttributes.md").

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/PutLexicon.md "../../../goto/cli2/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/polly-2016-06-10/PutLexicon.md "../../../goto/DotNetSDKV3/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForCpp/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForGoV2/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForJavaV2/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForKotlin/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForPHPV3/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/PutLexicon.md "../../../goto/boto3/polly-2016-06-10/PutLexicon.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/PutLexicon.md "../../../goto/SdkForRubyV3/polly-2016-06-10/PutLexicon.md")
