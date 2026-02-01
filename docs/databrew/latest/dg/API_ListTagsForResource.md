# ListTagsForResource

Lists all the tags for a DataBrew resource.

## Request Syntax

```
GET /tags/`ResourceArn` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ResourceArn](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

The Amazon Resource Name (ARN) string that uniquely identifies the DataBrew resource.

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Tags": {
      "***string***" : "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

A list of tags associated with the DataBrew resource.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalServerException**

An internal service failure occurred.

HTTP Status Code: 500

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/ListTagsForResource.md "../../../goto/cli2/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/ListTagsForResource.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForCpp/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForGoV2/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForKotlin/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/ListTagsForResource.md "../../../goto/boto3/databrew-2017-07-25/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/ListTagsForResource.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/ListTagsForResource.md")
