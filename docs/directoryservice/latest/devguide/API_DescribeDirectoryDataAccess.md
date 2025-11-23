# DescribeDirectoryDataAccess

Obtains status of directory data access enablement through the Directory Service Data API for the
specified directory.

## Request Syntax

```
{
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DescribeDirectoryDataAccess_RequestSyntax "#API_DescribeDirectoryDataAccess_RequestSyntax")**

The directory identifier.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "DataAccessStatus": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DataAccessStatus](#API_DescribeDirectoryDataAccess_ResponseSyntax "#API_DescribeDirectoryDataAccess_ResponseSyntax")**

The current status of data access through the Directory Service Data API.

Type: String

Valid Values: `Disabled | Disabling | Enabled | Enabling | Failed`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

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

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

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

This example illustrates one usage of DescribeDirectoryDataAccess.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 98
X-Amz-Target: DirectoryService_20150416.DescribeDirectoryDataAccess
X-Amz-Date: 20161212T212029Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=477f3a2802dcc303f69499723eb2e29a455fe3d1b646df0dacfd7c005a3a9509

 {
   "DirectoryId":"d-926example"
 }
```

### Example Response

This example illustrates one usage of DescribeDirectoryDataAccess.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 21:20:31 GMT

  {
    "DataAccessStatus": "Enabled"
  }

```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/cli2/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/boto3/ds-2015-04-16/DescribeDirectoryDataAccess.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDirectoryDataAccess.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDirectoryDataAccess.md")
