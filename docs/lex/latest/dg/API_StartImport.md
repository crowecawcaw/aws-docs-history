End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# StartImport

Starts a job to import a resource to Amazon Lex.

## Request Syntax

```
POST /imports/ HTTP/1.1
Content-type: application/json

{
   "mergeStrategy": "`string`",
   "payload": `blob`,
   "resourceType": "`string`",
   "tags": [
      {
         "key": "`string`",
         "value": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[mergeStrategy](#API_StartImport_RequestSyntax "#API_StartImport_RequestSyntax")**

Specifies the action that the `StartImport` operation
should take when there is an existing resource with the same
name.

- FAIL_ON_CONFLICT - The import operation is stopped on the first
  conflict between a resource in the import file and an existing
  resource. The name of the resource causing the conflict is in the
  `failureReason` field of the response to the
  `GetImport` operation.

OVERWRITE_LATEST - The import operation proceeds even if there
is a conflict with an existing resource. The $LASTEST version of the
existing resource is overwritten with the data from the import
file.

Type: String

Valid Values: `OVERWRITE_LATEST | FAIL_ON_CONFLICT`

Required: Yes

**[payload](#API_StartImport_RequestSyntax "#API_StartImport_RequestSyntax")**

A zip archive in binary format. The archive should contain one file, a
JSON file containing the resource to import. The resource should match the
type specified in the `resourceType` field.

Type: Base64-encoded binary data object

Required: Yes

**[resourceType](#API_StartImport_RequestSyntax "#API_StartImport_RequestSyntax")**

Specifies the type of resource to export. Each resource also
exports any resources that it depends on.

- A bot exports dependent intents.
- An intent exports dependent slot types.

Type: String

Valid Values: `BOT | INTENT | SLOT_TYPE`

Required: Yes

**[tags](#API_StartImport_RequestSyntax "#API_StartImport_RequestSyntax")**

A list of tags to add to the imported bot. You can only add tags when
you import a bot, you can't add tags to an intent or slot type.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

Required: No

## Response Syntax

```
HTTP/1.1 201
Content-type: application/json

{
   "createdDate": ***number***,
   "importId": "***string***",
   "importStatus": "***string***",
   "mergeStrategy": "***string***",
   "name": "***string***",
   "resourceType": "***string***",
   "tags": [
      {
         "key": "***string***",
         "value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

**[createdDate](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

A timestamp for the date and time that the import job was
requested.

Type: Timestamp

**[importId](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

The identifier for the specific import job.

Type: String

**[importStatus](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

The status of the import job. If the status is `FAILED`,
you can get the reason for the failure using the `GetImport`
operation.

Type: String

Valid Values: `IN_PROGRESS | COMPLETE | FAILED`

**[mergeStrategy](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

The action to take when there is a merge conflict.

Type: String

Valid Values: `OVERWRITE_LATEST | FAIL_ON_CONFLICT`

**[name](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

The name given to the import job.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z_]+`

**[resourceType](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

The type of resource to import.

Type: String

Valid Values: `BOT | INTENT | SLOT_TYPE`

**[tags](#API_StartImport_ResponseSyntax "#API_StartImport_ResponseSyntax")**

A list of tags added to the imported bot.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Minimum number of 0 items. Maximum number of 200 items.

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/StartImport.md "../../../goto/cli2/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/StartImport.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForCpp/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/StartImport.md "../../../goto/boto3/lex-models-2017-04-19/StartImport.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/StartImport.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/StartImport.md")
