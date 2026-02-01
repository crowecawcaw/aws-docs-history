# UntagResource

Removes metadata tags from a DataBrew resource.

## Request Syntax

```
DELETE /tags/`ResourceArn`?tagKeys=`TagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ResourceArn](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

A DataBrew resource from which you want to remove a tag or tags. The value for this
parameter is an Amazon Resource Name (ARN).

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**[TagKeys](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The tag keys (names) of one or more tags to be removed.

Array Members: Minimum number of 1 item. Maximum number of 200 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

## Request Body

The request does not have a request body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UntagResource.md "../../../goto/cli2/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/databrew-2017-07-25/UntagResource.md "../../../goto/DotNetSDKV4/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForCpp/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UntagResource.md "../../../goto/boto3/databrew-2017-07-25/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UntagResource.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UntagResource.md")
