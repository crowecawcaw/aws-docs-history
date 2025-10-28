End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetImport

Gets information about an import job started with the
`StartImport` operation.

## Request Syntax

```
GET /imports/`importId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[importId](#API_GetImport_RequestSyntax "#API_GetImport_RequestSyntax")**

The identifier of the import job information to return.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "createdDate": ***number***,
   "failureReason": [ "***string***" ],
   "importId": "***string***",
   "importStatus": "***string***",
   "mergeStrategy": "***string***",
   "name": "***string***",
   "resourceType": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[createdDate](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

A timestamp for the date and time that the import job was
created.

Type: Timestamp

**[failureReason](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

A string that describes why an import job failed to
complete.

Type: Array of strings

**[importId](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

The identifier for the specific import job.

Type: String

**[importStatus](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

The status of the import job. If the status is `FAILED`,
you can get the reason for the failure from the `failureReason`
field.

Type: String

Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

**[mergeStrategy](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

The action taken when there was a conflict between an existing
resource and a resource in the import file.

Type: String

Valid Values: `OVERWRITE_LATEST | FAIL_ON_CONFLICT`

**[name](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

The name given to the import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z_]+`

**[resourceType](#API_GetImport_ResponseSyntax "#API_GetImport_ResponseSyntax")**

The type of resource imported.

Type: String

Valid Values: `BOT | INTENT | SLOT_TYPE`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetImport.md "../../../goto/cli2/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetImport.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetImport.md "../../../goto/boto3/lex-models-2017-04-19/GetImport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetImport.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetImport.md")
