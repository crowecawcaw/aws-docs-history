# ListTagsForResource

Returns all the tags associated with an AWS resource.

## Request Syntax

```
{
   "MaxResults": `number`,
   "NextToken": "`string`",
   "ResourceArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[MaxResults](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

Specifies how many results that you want in the response.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 100.

Required: No

**[NextToken](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

Specifies an opaque string that indicates the position to begin the next list of
results in the response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

Required: No

**[ResourceArn](#API_ListTagsForResource_RequestSyntax "#API_ListTagsForResource_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the resource that you want tag information
on.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:(((agent|task|location)/(agent|task|loc)-[a-z0-9]{17}(/execution/exec-[a-f0-9]{17})?)|(system/storage-system-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(/job/discovery-job-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})?))$`

Required: Yes

## Response Syntax

```
{
   "NextToken": "***string***",
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

The opaque string that indicates the position to begin the next list of results in the
response.

Type: String

Length Constraints: Maximum length of 65535.

Pattern: `[a-zA-Z0-9=_-]+`

**[Tags](#API_ListTagsForResource_ResponseSyntax "#API_ListTagsForResource_ResponseSyntax")**

An array of tags applied to the specified resource.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 55 items.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InternalException**

This exception is thrown when an error occurs in the AWS DataSync
service.

HTTP Status Code: 500

**InvalidRequestException**

This exception is thrown when the client submits a malformed request.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/ListTagsForResource.md "../../../goto/cli2/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/datasync-2018-11-09/ListTagsForResource.md "../../../goto/DotNetSDKV4/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForCpp/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForGoV2/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForKotlin/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/ListTagsForResource.md "../../../goto/boto3/datasync-2018-11-09/ListTagsForResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTagsForResource.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ListTagsForResource.md")
