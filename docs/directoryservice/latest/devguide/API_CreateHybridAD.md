# CreateHybridAD

Creates a hybrid directory that connects your self-managed Active Directory (AD)
infrastructure and AWS.

You must have a successful directory assessment using [StartADAssessment](API_StartADAssessment.md "API_StartADAssessment.md") to validate your environment compatibility before you
use this operation.

Updates are applied asynchronously. Use [DescribeDirectories](API_DescribeDirectories.md "API_DescribeDirectories.md") to
monitor the progress of directory creation.

## Request Syntax

```
{
   "AssessmentId": "`string`",
   "SecretArn": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AssessmentId](#API_CreateHybridAD_RequestSyntax "#API_CreateHybridAD_RequestSyntax")**

The unique identifier of the successful directory assessment that validates your
self-managed AD environment. You must have a successful directory assessment before you
create a hybrid directory.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

Required: Yes

**[SecretArn](#API_CreateHybridAD_RequestSyntax "#API_CreateHybridAD_RequestSyntax")**

The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the
credentials for the service account used to join hybrid domain controllers to your
self-managed AD domain. This secret is used once and not stored.

The secret must contain key-value pairs with keys matching
`customerAdAdminDomainUsername` and
`customerAdAdminDomainPassword`. For example:
`{"customerAdAdminDomainUsername":"carlos_salazar","customerAdAdminDomainPassword":"ExamplePassword123!"}`.

Type: String

Pattern: `^arn:aws:secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+-[a-zA-Z0-9]{6}$`

Required: Yes

**[Tags](#API_CreateHybridAD_RequestSyntax "#API_CreateHybridAD_RequestSyntax")**

The tags to be assigned to the directory. Each tag consists of a key and value pair.
You can specify multiple tags as a list.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

## Response Syntax

```
{
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryId](#API_CreateHybridAD_ResponseSyntax "#API_CreateHybridAD_ResponseSyntax")**

The unique identifier of the newly created hybrid directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ADAssessmentLimitExceededException**

A directory assessment is automatically created when you create a hybrid directory.
There are two types of assessments: `CUSTOMER` and `SYSTEM`. Your
AWS account has a limit of 100 `CUSTOMER` directory assessments.

If you attempt to create a hybrid directory; and you already have 100
`CUSTOMER` directory assessments;, you will encounter an error. Delete
assessments to free up capacity before trying again.

You can request an increase to your `CUSTOMER` directory assessment quota
by contacting customer support or delete existing CUSTOMER directory assessments; to
free up capacity.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryLimitExceededException**

The maximum number of directories in the region has been reached. You can use the
[GetDirectoryLimits](API_GetDirectoryLimits.md "API_GetDirectoryLimits.md") operation to determine your directory limits in
the region.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of CreateHybridAD.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 298
X-Amz-Target: DirectoryService_20150416.CreateHybridAD
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAIOSFODNN7EXAMPLE/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
    "SecretArn": "arn:aws:secretsmanager:eu-west-1:111122223333:secret:CredExample-DZESji",
    "AssessmentId": "da-1234567890example1",
    "Tags": [{
        "Key": "Environment",
        "Value": "Production"
    }]
}
```

### Example Response

This example illustrates one usage of CreateHybridAD.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "DirectoryId": "d-926example"
}}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateHybridAD.md "../../../goto/cli2/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/CreateHybridAD.md "../../../goto/DotNetSDKV4/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateHybridAD.md "../../../goto/boto3/ds-2015-04-16/CreateHybridAD.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateHybridAD.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateHybridAD.md")
