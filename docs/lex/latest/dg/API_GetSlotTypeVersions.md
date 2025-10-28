End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GetSlotTypeVersions

Gets information about all versions of a slot type.

The `GetSlotTypeVersions` operation returns a
`SlotTypeMetadata` object for each version of a slot type.
For example, if a slot type has three numbered versions, the
`GetSlotTypeVersions` operation returns four
`SlotTypeMetadata` objects in the response, one for each
numbered version and one for the `$LATEST` version.

The `GetSlotTypeVersions` operation always returns at
least one version, the `$LATEST` version.

This operation requires permissions for the
`lex:GetSlotTypeVersions` action.

## Request Syntax

```
GET /slottypes/`name`/versions/?maxResults=`maxResults`&nextToken=`nextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[maxResults](#API_GetSlotTypeVersions_RequestSyntax "#API_GetSlotTypeVersions_RequestSyntax")**

The maximum number of slot type versions to return in the response.
The default is 10.

Valid Range: Minimum value of 1. Maximum value of 50.

**[name](#API_GetSlotTypeVersions_RequestSyntax "#API_GetSlotTypeVersions_RequestSyntax")**

The name of the slot type for which versions should be
returned.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

**[nextToken](#API_GetSlotTypeVersions_RequestSyntax "#API_GetSlotTypeVersions_RequestSyntax")**

A pagination token for fetching the next page of slot type
versions. If the response to this call is truncated, Amazon Lex returns a
pagination token in the response. To fetch the next page of versions,
specify the pagination token in the next request.

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

**[nextToken](#API_GetSlotTypeVersions_ResponseSyntax "#API_GetSlotTypeVersions_ResponseSyntax")**

A pagination token for fetching the next page of slot type
versions. If the response to this call is truncated, Amazon Lex returns a
pagination token in the response. To fetch the next page of versions,
specify the pagination token in the next request.

Type: String

**[slotTypes](#API_GetSlotTypeVersions_ResponseSyntax "#API_GetSlotTypeVersions_ResponseSyntax")**

An array of `SlotTypeMetadata` objects, one for each
numbered version of the slot type plus one for the `$LATEST`
version.

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

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/cli2/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/DotNetSDKV3/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForCpp/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/boto3/lex-models-2017-04-19/GetSlotTypeVersions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotTypeVersions.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/GetSlotTypeVersions.md")
