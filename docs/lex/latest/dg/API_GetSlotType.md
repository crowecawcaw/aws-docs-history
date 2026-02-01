End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetSlotType

Returns information about a specific version of a slot type. In
addition to specifying the slot type name, you must specify the slot type
version.

This operation requires permissions for the
`lex:GetSlotType` action.

## Request Syntax

```
GET /slottypes/`name`/versions/`version` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_GetSlotType_RequestSyntax "#API_GetSlotType_RequestSyntax")**

The name of the slot type. The name is case sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[version](#API_GetSlotType_RequestSyntax "#API_GetSlotType_RequestSyntax")**

The version of the slot type.

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "checksum": "***string***",
   "createdDate": ***number***,
   "description": "***string***",
   "enumerationValues": [
      {
         "synonyms": [ "***string***" ],
         "value": "***string***"
      }
   ],
   "lastUpdatedDate": ***number***,
   "name": "***string***",
   "parentSlotTypeSignature": "***string***",
   "slotTypeConfigurations": [
      {
         "regexConfiguration": {
            "pattern": "***string***"
         }
      }
   ],
   "valueSelectionStrategy": "***string***",
   "version": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[checksum](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

Checksum of the `$LATEST` version of the slot
type.

Type: String

**[createdDate](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The date that the slot type was created.

Type: Timestamp

**[description](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

A description of the slot type.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 200.

**[enumerationValues](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

A list of `EnumerationValue` objects that defines the
values that the slot type can take.

Type: Array of [EnumerationValue](API_EnumerationValue.md "API_EnumerationValue.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10000 items.

**[lastUpdatedDate](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The date that the slot type was updated. When you create a
resource, the creation date and last update date are the same.

Type: Timestamp

**[name](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The name of the slot type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[parentSlotTypeSignature](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The built-in slot type used as a parent for the slot type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^((AMAZON\.)_?|[A-Za-z]_?)+`

**[slotTypeConfigurations](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

Configuration information that extends the parent built-in slot
type.

Type: Array of [SlotTypeConfiguration](API_SlotTypeConfiguration.md "API_SlotTypeConfiguration.md") objects

Array Members: Minimum number of 0 items. Maximum number of 10 items.

**[valueSelectionStrategy](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The strategy that Amazon Lex uses to determine the value of the slot.
For more information, see [PutSlotType](API_PutSlotType.md "API_PutSlotType.md").

Type: String

Valid Values: `ORIGINAL_VALUE | TOP_RESOLUTION`

**[version](#API_GetSlotType_ResponseSyntax "#API_GetSlotType_ResponseSyntax")**

The version of the slot type.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `\$LATEST|[0-9]+`

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetSlotType.md "../../../goto/cli2/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetSlotType.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetSlotType.md "../../../goto/boto3/lex-models-2017-04-19/GetSlotType.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotType.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotType.md")
