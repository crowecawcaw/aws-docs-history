# UntagResource

Removes metadata tags from an elastic cluster resource

## Request Syntax

```
DELETE /tags/`resourceArn`?tagKeys=`tagKeys` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[resourceArn](#API_elastic_UntagResource_RequestSyntax "#API_elastic_UntagResource_RequestSyntax")**

The ARN identifier of the elastic cluster resource.

Length Constraints: Minimum length of 1. Maximum length of 1011.

Required: Yes

**[tagKeys](#API_elastic_UntagResource_RequestSyntax "#API_elastic_UntagResource_RequestSyntax")**

The tag keys to be removed from the elastic cluster resource.

Array Members: Minimum number of 0 items. Maximum number of 50 items.

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`

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

There was an internal server error.

HTTP Status Code: 500

**ResourceNotFoundException**

The specified resource could not be located.

**message**

An error message describing the failure.

**resourceId**

The ID of the resource that could not be located.

**resourceType**

The type of the resource that could not be found.

HTTP Status Code: 404

**ThrottlingException**

ThrottlingException will be thrown when request was denied due to request throttling.

**retryAfterSeconds**

The number of seconds to wait before retrying the operation.

HTTP Status Code: 429

**ValidationException**

A structure defining a validation exception.

**fieldList**

A list of the fields in which the validation exception occurred.

**message**

An error message describing the validation exception.

**reason**

The reason why the validation exception occurred (one of `unknownOperation`,
`cannotParse`, `fieldValidationFailed`, or `other`).

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/cli2/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/DotNetSDKV4/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForCpp/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForGoV2/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForJavaV2/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForJavaScriptV3/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForKotlin/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForPHPV3/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for Python](../../../goto/boto3/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/boto3/docdb-elastic-2022-11-28/UntagResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/UntagResource.md "../../../goto/SdkForRubyV3/docdb-elastic-2022-11-28/UntagResource.md")
