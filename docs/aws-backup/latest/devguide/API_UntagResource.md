# UntagResource

Removes a set of key-value pairs from a recovery point, backup plan, or backup vault
identified by an Amazon Resource Name (ARN)

This API is not supported for recovery points for resource types
including Aurora, Amazon DocumentDB. Amazon EBS,
Amazon FSx, Neptune, and Amazon RDS.

## Request Syntax

```
POST /untag/`resourceArn` HTTP/1.1
Content-type: application/json

{
   "TagKeyList": [ "`string`" ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

An ARN that uniquely identifies a resource. The format of the ARN depends on the type of
the tagged resource.

ARNs that do not include `backup` are incompatible with tagging.
`TagResource` and `UntagResource` with invalid ARNs will
result in an error. Acceptable ARN content can include
`arn:aws:backup:us-east`. Invalid ARN content may look like
`arn:aws:ec2:us-east`.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[TagKeyList](#API_UntagResource_RequestSyntax "#API_UntagResource_RequestSyntax")**

The keys to identify which key-value tags to remove from a resource.

Type: Array of strings

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ResourceNotFoundException**

A resource that is required for the action doesn't exist.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UntagResource.md "../../../goto/cli2/backup-2018-11-15/UntagResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-2018-11-15/UntagResource.md "../../../goto/DotNetSDKV3/backup-2018-11-15/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UntagResource.md "../../../goto/SdkForCpp/backup-2018-11-15/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UntagResource.md "../../../goto/SdkForGoV2/backup-2018-11-15/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UntagResource.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UntagResource.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UntagResource.md "../../../goto/SdkForKotlin/backup-2018-11-15/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UntagResource.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UntagResource.md "../../../goto/boto3/backup-2018-11-15/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UntagResource.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UntagResource.md")
