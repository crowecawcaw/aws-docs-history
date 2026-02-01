# DeleteAccessPoint

Deletes the specified access point. After deletion is complete, new clients can no
longer connect to the access points. Clients connected to the access point at the time of
deletion will continue to function until they terminate their connection.

This operation requires permissions for the `elasticfilesystem:DeleteAccessPoint` action.

## Request Syntax

```
DELETE /2015-02-01/access-points/`AccessPointId` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[AccessPointId](#API_DeleteAccessPoint_RequestSyntax "#API_DeleteAccessPoint_RequestSyntax")**

The ID of the access point that you want to delete.

Length Constraints: Maximum length of 128.

Pattern: `^(arn:aws[-a-z]*:elasticfilesystem:[0-9a-z-:]+:access-point/fsap-[0-9a-f]{8,40}|fsap-[0-9a-f]{8,40})$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

**AccessPointNotFound**

Returned if the specified `AccessPointId` value doesn't exist in the
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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/cli2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/DotNetSDKV4/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForGoV2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForJavaScriptV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForKotlin/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForPHPV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for Python](../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/boto3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/DeleteAccessPoint.md")
