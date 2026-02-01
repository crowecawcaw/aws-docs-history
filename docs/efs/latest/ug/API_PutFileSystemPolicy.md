# PutFileSystemPolicy

Applies an Amazon EFS
`FileSystemPolicy` to an Amazon EFS file system. A file system policy is an
IAM resource-based policy and can contain multiple policy statements. A file system always has
exactly one file system policy, which can be the default policy or an explicit policy set or
updated using this API operation. EFS file system policies have a 20,000 character
limit. When an explicit policy is set, it overrides the default policy. For more information
about the default file system policy, see [Default EFS file system policy](iam-access-control-nfs-efs.md#default-filesystempolicy "iam-access-control-nfs-efs.md#default-filesystempolicy").

###### Note

EFS file system policies have a 20,000 character limit.

This operation requires permissions for the `elasticfilesystem:PutFileSystemPolicy` action.

## Request Syntax

```
PUT /2015-02-01/file-systems/`FileSystemId`/policy HTTP/1.1
Content-type: application/json

{
   "BypassPolicyLockoutSafetyCheck": `boolean`,
   "Policy": "`string`"
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[FileSystemId](#API_PutFileSystemPolicy_RequestSyntax "#API_PutFileSystemPolicy_RequestSyntax")**

The ID of the EFS file system that you want to create or update the
`FileSystemPolicy` for.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[BypassPolicyLockoutSafetyCheck](#API_PutFileSystemPolicy_RequestSyntax "#API_PutFileSystemPolicy_RequestSyntax")**

(Optional) A boolean that specifies whether or not to bypass the `FileSystemPolicy` lockout safety check. The lockout safety check
determines whether the policy in the request will lock out, or prevent, the IAM principal that is making the request from making future `PutFileSystemPolicy` requests on this file system.
Set `BypassPolicyLockoutSafetyCheck` to `True` only when you intend to prevent
the IAM principal that is making the request from making subsequent `PutFileSystemPolicy` requests on this file system.
The default value is `False`.

Type: Boolean

Required: No

**[Policy](#API_PutFileSystemPolicy_RequestSyntax "#API_PutFileSystemPolicy_RequestSyntax")**

The `FileSystemPolicy` that you're creating. Accepts a JSON formatted
policy definition. EFS file system policies have a 20,000 character limit. To find
out more about the elements that make up a file system policy, see [Resource-based policies within Amazon EFS](security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies "security_iam_service-with-iam.md#security_iam_service-with-iam-resource-based-policies").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20000.

Pattern: `[\s\S]+`

Required: Yes

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "FileSystemId": "***string***",
   "Policy": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[FileSystemId](#API_PutFileSystemPolicy_ResponseSyntax "#API_PutFileSystemPolicy_ResponseSyntax")**

Specifies the EFS file system to which the `FileSystemPolicy`
applies.

Type: String

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:file-system/fs-[0-9a-f]{8,40}|fs-[0-9a-f]{8,40})$`

**[Policy](#API_PutFileSystemPolicy_ResponseSyntax "#API_PutFileSystemPolicy_ResponseSyntax")**

The JSON formatted `FileSystemPolicy` for the EFS file
system.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 20000.

Pattern: `[\s\S]+`

## Errors

**BadRequest**

Returned if the request is malformed or contains an error such as an invalid
parameter value or a missing required parameter.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

**FileSystemNotFound**

Returned if the specified `FileSystemId` value doesn't exist in the
requester's AWS account.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 404

**IncorrectFileSystemLifeCycleState**

Returned if the file system's lifecycle state is not "available".

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 409

**InternalServerError**

Returned if an error occurred on the server side.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 500

**InvalidPolicyException**

Returned if the `FileSystemPolicy` is malformed or contains an error such
as a parameter value that is not valid or a missing required parameter. Returned in the
case of a policy lockout safety check error.

**ErrorCode**

The error code is a string that uniquely identifies an error condition.
It is meant to be read and understood by programs that detect and handle errors by type.

**Message**

The error message contains a generic description of the error
condition in English. It is intended for a human audience. Simple programs display the message directly
to the end user if they encounter an error condition they don't know how or don't care to handle.
Sophisticated programs with more exhaustive error handling and proper internationalization are
more likely to ignore the error message.

HTTP Status Code: 400

## Examples

### Create an EFS FileSystemPolicy

The following request creates a `FileSystemPolicy` that allows all AWS principals to mount the specified EFS file system with read and
write permissions.

#### Sample Request

```
PUT /2015-02-01/file-systems/fs-01234567/file-system-policy HTTP/1.1
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:ClientMount",
                "elasticfilesystem:ClientWrite"
            ],
            "Principal": {
                "AWS": ["*"]
            },
        }
    ]
}
```

#### Sample Response

```
{
    "Version": "2012-10-17",
    "Id": "1",
    "Statement": [
        {
            "Sid": "efs-statement-abcdef01-1111-bbbb-2222-111122224444",
            "Effect": "Allow",
            "Action": [
                "elasticfilesystem:ClientMount",
                "elasticfilesystem:ClientWrite"
            ],
            "Principal": {
                "AWS": ["*"]
            },
            "Resource":"arn:aws:elasticfilesystem:us-east-1:1111222233334444:file-system/fs-01234567"
        }
    ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/cli2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/boto3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/PutFileSystemPolicy.md")
