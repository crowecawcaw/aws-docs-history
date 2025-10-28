# PutItems

Adds one or more items to an Items dataset. For more information see
[Importing items individually](importing-items.md "importing-items.md").

## Request Syntax

```
POST /items HTTP/1.1
Content-type: application/json

{
   "datasetArn": "`string`",
   "items": [
      {
         "itemId": "`string`",
         "properties": "`string`"
      }
   ]
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[datasetArn](#API_UBS_PutItems_RequestSyntax "#API_UBS_PutItems_RequestSyntax")**

The Amazon Resource Name (ARN) of the Items dataset you are adding the item or items to.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

**[items](#API_UBS_PutItems_RequestSyntax "#API_UBS_PutItems_RequestSyntax")**

A list of item data.

Type: Array of [Item](API_UBS_Item.md "API_UBS_Item.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 409

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-events-2018-03-22/PutItems.md "../../../goto/cli2/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-events-2018-03-22/PutItems.md "../../../goto/DotNetSDKV3/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-events-2018-03-22/PutItems.md "../../../goto/boto3/personalize-events-2018-03-22/PutItems.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutItems.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutItems.md")
