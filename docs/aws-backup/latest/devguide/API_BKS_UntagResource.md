# UntagResource

This operation removes tags from the specified resource.

## Request Syntax

```
DELETE /tags/`ResourceArn`?tagKeys=`TagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[ResourceArn](#API_BKS_UntagResource_RequestSyntax "#API_BKS_UntagResource_RequestSyntax")**

The Amazon Resource Name (ARN) that uniquely identifies
the resource where you want to remove tags.

Required: Yes

**[TagKeys](#API_BKS_UntagResource_RequestSyntax "#API_BKS_UntagResource_RequestSyntax")**

This required parameter contains the tag keys you
want to remove from the source.

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

**AccessDeniedException**

You do not have sufficient access to perform this action.

**message**

User does not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**

An internal server error occurred. Retry your request.

**message**

Unexpected error during processing of request.

**retryAfterSeconds**

Retry the call after number of seconds.

HTTP Status Code: 500

**ResourceNotFoundException**

The resource was not found for this request.

Confirm the resource information, such as the ARN or type is correct
and exists, then retry the request.

**message**

Request references a resource which does not exist.

**resourceId**

Hypothetical identifier of the resource affected.

**resourceType**

Hypothetical type of the resource affected.

HTTP Status Code: 404

**ThrottlingException**

The request was denied due to request throttling.

**message**

Request was unsuccessful due to request throttling.

**quotaCode**

This is the code unique to the originating service with the quota.

**retryAfterSeconds**

Retry the call after number of seconds.

**serviceCode**

This is the code unique to the originating service.

HTTP Status Code: 429

**ValidationException**

The input fails to satisfy the constraints specified by a service.

**message**

The input fails to satisfy the constraints specified by an Amazon service.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backupsearch-2018-05-10/UntagResource.md "../../../goto/cli2/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backupsearch-2018-05-10/UntagResource.md "../../../goto/DotNetSDKV4/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForCpp/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForGoV2/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForJavaV2/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForJavaScriptV3/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForKotlin/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForPHPV3/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/backupsearch-2018-05-10/UntagResource.md "../../../goto/boto3/backupsearch-2018-05-10/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backupsearch-2018-05-10/UntagResource.md "../../../goto/SdkForRubyV3/backupsearch-2018-05-10/UntagResource.md")
