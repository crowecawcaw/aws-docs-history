# TagResource

Applies a _tag_ to an AWS resource. Tags are
key-value pairs that can help you manage, filter, and search for your resources.

These include AWS DataSync resources, such as locations, tasks, and task
executions.

## Request Syntax

```
{
   "ResourceArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ResourceArn](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

Specifies the Amazon Resource Name (ARN) of the resource to apply the tag to.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:(agent|task|location|system)/((agent|task|loc)-[a-f0-9]{17}|storage-system-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})(/execution/exec-[a-f0-9]{17})?$`

Required: Yes

**[Tags](#API_TagResource_RequestSyntax "#API_TagResource_RequestSyntax")**

Specifies the tags that you want to apply to the resource.

Type: Array of [TagListEntry](API_TagListEntry.md "API_TagListEntry.md") objects

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

- [AWS Command Line Interface V2](../../../goto/cli2/datasync-2018-11-09/TagResource.md "../../../goto/cli2/datasync-2018-11-09/TagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/datasync-2018-11-09/TagResource.md "../../../goto/DotNetSDKV3/datasync-2018-11-09/TagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TagResource.md "../../../goto/SdkForCpp/datasync-2018-11-09/TagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/datasync-2018-11-09/TagResource.md "../../../goto/SdkForGoV2/datasync-2018-11-09/TagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TagResource.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/TagResource.md "../../../goto/SdkForJavaScriptV3/datasync-2018-11-09/TagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/datasync-2018-11-09/TagResource.md "../../../goto/SdkForKotlin/datasync-2018-11-09/TagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/datasync-2018-11-09/TagResource.md "../../../goto/SdkForPHPV3/datasync-2018-11-09/TagResource.md")
- [AWS SDK for Python](../../../goto/boto3/datasync-2018-11-09/TagResource.md "../../../goto/boto3/datasync-2018-11-09/TagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TagResource.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TagResource.md")
