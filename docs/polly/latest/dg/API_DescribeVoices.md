# DescribeVoices

Returns the list of voices that are available for use when
requesting speech synthesis. Each voice speaks a specified language, is
either male or female, and is identified by an ID, which is the ASCII
version of the voice name.

When synthesizing speech ( `SynthesizeSpeech` ), you
provide the voice ID for the voice you want from the list of voices
returned by `DescribeVoices`.

For example, you want your news reader application to read news in
a specific language, but giving a user the option to choose the voice.
Using the `DescribeVoices` operation you can provide the user
with a list of available voices to select from.

You can optionally specify a language code to filter the available
voices. For example, if you specify `en-US`, the operation
returns a list of all available US English voices.

This operation requires permissions to perform the
`polly:DescribeVoices` action.

## Request Syntax

```
GET /v1/voices?Engine=`Engine`&IncludeAdditionalLanguageCodes=`IncludeAdditionalLanguageCodes`&LanguageCode=`LanguageCode`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[Engine](#API_DescribeVoices_RequestSyntax "#API_DescribeVoices_RequestSyntax")**

Specifies the engine (`standard`, `neural`,
`long-form` or `generative`) used by Amazon Polly when
processing input text for speech synthesis.

Valid Values: `standard | neural | long-form | generative`

**[IncludeAdditionalLanguageCodes](#API_DescribeVoices_RequestSyntax "#API_DescribeVoices_RequestSyntax")**

Boolean value indicating whether to return any bilingual voices that
use the specified language as an additional language. For instance, if you
request all languages that use US English (es-US), and there is an Italian
voice that speaks both Italian (it-IT) and US English, that voice will be
included if you specify `yes` but not if you specify
`no`.

**[LanguageCode](#API_DescribeVoices_RequestSyntax "#API_DescribeVoices_RequestSyntax")**

The language identification tag (ISO 639 code for the language
name-ISO 3166 country code) for filtering the list of voices returned. If
you don't specify this optional parameter, all available voices are
returned.

Valid Values: `arb | cmn-CN | cy-GB | da-DK | de-DE | en-AU | en-GB | en-GB-WLS | en-IN | en-US | es-ES | es-MX | es-US | fr-CA | fr-FR | is-IS | it-IT | ja-JP | hi-IN | ko-KR | nb-NO | nl-NL | pl-PL | pt-BR | pt-PT | ro-RO | ru-RU | sv-SE | tr-TR | en-NZ | en-ZA | ca-ES | de-AT | yue-CN | ar-AE | fi-FI | en-IE | nl-BE | fr-BE | cs-CZ | de-CH`

**[NextToken](#API_DescribeVoices_RequestSyntax "#API_DescribeVoices_RequestSyntax")**

An opaque pagination token returned from the previous
`DescribeVoices` operation. If present, this indicates where
to continue the listing.

Length Constraints: Minimum length of 0. Maximum length of 4096.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "***string***",
   "Voices": [
      {
         "AdditionalLanguageCodes": [ "***string***" ],
         "Gender": "***string***",
         "Id": "***string***",
         "LanguageCode": "***string***",
         "LanguageName": "***string***",
         "Name": "***string***",
         "SupportedEngines": [ "***string***" ]
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeVoices_ResponseSyntax "#API_DescribeVoices_ResponseSyntax")**

The pagination token to use in the next request to continue the
listing of voices. `NextToken` is returned only if the response
is truncated.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 4096.

**[Voices](#API_DescribeVoices_ResponseSyntax "#API_DescribeVoices_ResponseSyntax")**

A list of voices with their properties.

Type: Array of [Voice](API_Voice.md "API_Voice.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/polly-2016-06-10/DescribeVoices.md "../../../goto/cli2/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/polly-2016-06-10/DescribeVoices.md "../../../goto/DotNetSDKV4/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForCpp/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForGoV2/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForJavaV2/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForJavaScriptV3/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForKotlin/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForPHPV3/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for Python](../../../goto/boto3/polly-2016-06-10/DescribeVoices.md "../../../goto/boto3/polly-2016-06-10/DescribeVoices.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/DescribeVoices.md "../../../goto/SdkForRubyV3/polly-2016-06-10/DescribeVoices.md")
