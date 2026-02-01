End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetExport

Exports the contents of a Amazon Lex resource in a specified format.

## Request Syntax

```
GET /exports/?exportType=`exportType`&name=`name`&resourceType=`resourceType`&version=`version` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[exportType](#API_GetExport_RequestSyntax "#API_GetExport_RequestSyntax")**

The format of the exported data.

Valid Values: `ALEXA_SKILLS_KIT | LEX`

Required: Yes

**[name](#API_GetExport_RequestSyntax "#API_GetExport_RequestSyntax")**

The name of the bot to export.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z_]+`

Required: Yes

**[resourceType](#API_GetExport_RequestSyntax "#API_GetExport_RequestSyntax")**

The type of resource to export.

Valid Values: `BOT | INTENT | SLOT_TYPE`

Required: Yes

**[version](#API_GetExport_RequestSyntax "#API_GetExport_RequestSyntax")**

The version of the bot to export.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[0-9]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "exportStatus": "***string***",
   "exportType": "***string***",
   "failureReason": "***string***",
   "name": "***string***",
   "resourceType": "***string***",
   "url": "***string***",
   "version": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[exportStatus](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

The status of the export.

- `IN_PROGRESS` - The export is in progress.
- `READY` - The export is complete.
- `FAILED` - The export could not be
  completed.

Type: String

Valid Values: `IN_PROGRESS | READY | FAILED`

**[exportType](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

The format of the exported data.

Type: String

Valid Values: `ALEXA_SKILLS_KIT | LEX`

**[failureReason](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

If `status` is `FAILED`, Amazon Lex provides the
reason that it failed to export the resource.

Type: String

**[name](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

The name of the bot being exported.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z_]+`

**[resourceType](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

The type of the exported resource.

Type: String

Valid Values: `BOT | INTENT | SLOT_TYPE`

**[url](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

An S3 pre-signed URL that provides the location of the exported
resource. The exported resource is a ZIP archive that contains the
exported resource in JSON format. The structure of the archive may change.
Your code should not rely on the archive structure.

Type: String

**[version](#API_GetExport_ResponseSyntax "#API_GetExport_ResponseSyntax")**

The version of the bot being exported.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[0-9]+`

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetExport.md "../../../goto/cli2/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetExport.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetExport.md "../../../goto/boto3/lex-models-2017-04-19/GetExport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetExport.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetExport.md")
