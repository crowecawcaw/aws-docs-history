# DeleteConditionalForwarder

Deletes a conditional forwarder that has been set up for your AWS
directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "RemoteDomainName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DeleteConditionalForwarder_RequestSyntax "#API_DeleteConditionalForwarder_RequestSyntax")**

The directory ID for which you are deleting the conditional forwarder.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[RemoteDomainName](#API_DeleteConditionalForwarder_RequestSyntax "#API_DeleteConditionalForwarder_RequestSyntax")**

The fully qualified domain name (FQDN) of the remote domain with which you are deleting
the conditional forwarder.

Type: String

Length Constraints: Maximum length of 1024.

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryUnavailableException**

The specified directory is unavailable.

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

This example illustrates one usage of DeleteConditionalForwarder.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 76
X-Amz-Target: DirectoryService_20150416.DeleteConditionalForwarder
X-Amz-Date: 20161214T001055Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=ffc3c3d6feac461a9b093cab94dd8957b252f2936b51f14a1ad8499a8b401d4a

 {
   "DirectoryId":"d-926example",
   "RemoteDomainName":"sales.example.com"
 }
```

### Example Response

This example illustrates one usage of DeleteConditionalForwarder.

```
HTTP/1.1 200 OK
x-amzn-RequestId: ca119fd0-c191-11e6-8f8e-ed61d076c15a
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 00:11:00 GMT

 {

 }
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/cli2/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForCpp/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/boto3/ds-2015-04-16/DeleteConditionalForwarder.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteConditionalForwarder.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteConditionalForwarder.md")
