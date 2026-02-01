End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetSlotTypes

Returns slot type information as follows:

- If you specify the `nameContains` field, returns the
  `$LATEST` version of all slot types that contain the
  specified string.
- If you don't specify the `nameContains` field,
  returns information about the `$LATEST` version of all slot
  types.
  The operation requires permission for the
  `lex:GetSlotTypes` action.

## Request Syntax

```
GET /slottypes/?maxResults=`maxResults`&nameContains=`nameContains`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_GetSlotTypes_RequestSyntax "#API_GetSlotTypes_RequestSyntax")**

The maximum number of slot types to return in the response. The
default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[nameContains](#API_GetSlotTypes_RequestSyntax "#API_GetSlotTypes_RequestSyntax")**

Substring to match in slot type names. A slot type will be returned
if any part of its name matches the substring. For example, "xyz" matches
both "xyzabc" and "abcxyz."

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

**[nextToken](#API_GetSlotTypes_RequestSyntax "#API_GetSlotTypes_RequestSyntax")**

A pagination token that fetches the next page of slot types. If the
response to this API call is truncated, Amazon Lex returns a pagination token
in the response. To fetch next page of slot types, specify the pagination
token in the next request.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "***string***",
   "slotTypes": [
      {
         "createdDate": ***number***,
         "description": "***string***",
         "lastUpdatedDate": ***number***,
         "name": "***string***",
         "version": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[nextToken](#API_GetSlotTypes_ResponseSyntax "#API_GetSlotTypes_ResponseSyntax")**

If the response is truncated, it includes a pagination token that
you can specify in your next request to fetch the next page of slot
types.

Type: String

**[slotTypes](#API_GetSlotTypes_ResponseSyntax "#API_GetSlotTypes_ResponseSyntax")**

An array of objects, one for each slot type, that provides
information such as the name of the slot type, the version, and a
description.

Type: Array of [SlotTypeMetadata](API_SlotTypeMetadata.md "API_SlotTypeMetadata.md") objects

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/cli2/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/boto3/lex-models-2017-04-19/GetSlotTypes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotTypes.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotTypes.md")
