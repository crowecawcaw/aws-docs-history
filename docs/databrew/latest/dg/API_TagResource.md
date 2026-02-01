# TagResource

Adds metadata tags to a DataBrew resource, such as a dataset, project, recipe, job, or
schedule.

## Request Syntax

```
POST /tags/`ResourceArn` HTTP/1.1
Content-type: application/json

{
   "Tags": {
      "`string`" : "`string`"
   }
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[ResourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

The DataBrew resource to which tags should be added. The value for this parameter is
an Amazon Resource Name (ARN). For DataBrew, you can tag a dataset, a job, a project, or
a recipe.

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

One or more tags to be assigned to the resource.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/TagResource.md "../../../goto/cli2/databrew-2017-07-25/TagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/TagResource.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/TagResource.md "../../../goto/SdkForCpp/databrew-2017-07-25/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/TagResource.md "../../../goto/SdkForGoV2/databrew-2017-07-25/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/TagResource.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/TagResource.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/TagResource.md "../../../goto/SdkForKotlin/databrew-2017-07-25/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/TagResource.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/TagResource.md "../../../goto/boto3/databrew-2017-07-25/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/TagResource.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/TagResource.md")
