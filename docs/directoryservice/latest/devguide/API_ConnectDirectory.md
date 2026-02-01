# ConnectDirectory

Creates an AD Connector to connect to a self-managed directory.

Before you call `ConnectDirectory`, ensure that all of the required permissions
have been explicitly granted through a policy. For details about what permissions are required
to run the `ConnectDirectory` operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](../admin-guide/UsingWithDS_IAM_ResourcePermissions.md "../admin-guide/UsingWithDS_IAM_ResourcePermissions.md").

## Request Syntax

```
{
   "ConnectSettings": {
      "CustomerDnsIps": [ "`string`" ],
      "CustomerDnsIpsV6": [ "`string`" ],
      "CustomerUserName": "`string`",
      "SubnetIds": [ "`string`" ],
      "VpcId": "`string`"
   },
   "Description": "`string`",
   "Name": "`string`",
   "NetworkType": "`string`",
   "Password": "`string`",
   "ShortName": "`string`",
   "Size": "`string`",
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

**[ConnectSettings](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

A [DirectoryConnectSettings](API_DirectoryConnectSettings.md "API_DirectoryConnectSettings.md") object that contains additional information
for the operation.

Type: [DirectoryConnectSettings](API_DirectoryConnectSettings.md "API_DirectoryConnectSettings.md") object

Required: Yes

**[Description](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

A description for the directory.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**[Name](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The fully qualified name of your self-managed directory, such as
`corp.example.com`.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: Yes

**[NetworkType](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The network type for your directory. The default value is `IPv4` or
`IPv6` based on the provided subnet capabilities.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

**[Password](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The password for your self-managed user account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Required: Yes

**[ShortName](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The NetBIOS name of your self-managed directory, such as `CORP`.

Type: String

Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`

Required: No

**[Size](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The size of the directory.

Type: String

Valid Values: `Small | Large`

Required: Yes

**[Tags](#API_ConnectDirectory_RequestSyntax "#API_ConnectDirectory_RequestSyntax")**

The tags to be assigned to AD Connector.

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

**[DirectoryId](#API_ConnectDirectory_ResponseSyntax "#API_ConnectDirectory_ResponseSyntax")**

The identifier of the new directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of ConnectDirectory.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 295
X-Amz-Target: DirectoryService_20150416.ConnectDirectory
X-Amz-Date: 20161212T233740Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=60ddfa4a90d91327ef8cb510563d6f031eab1b092d5b1034fab7b157733bf86b

 {
   "Name":"corp.example.com",
   "ConnectSettings":{
      "CustomerUserName":"Administrator",
      "VpcId":"vpc-45025421",
      "SubnetIds":[
         "subnet-ba0146de",
         "subnet-bef46bc8"
      ],
      "CustomerDnsIps":[
         "172.30.21.228"
      ]
   },
   "Description":"Connector to corp",
   "ShortName":"corp",
   "Password":"Str0ngP@ssw0rd",
   "Size":"Small"
 }
```

### Example Response

This example illustrates one usage of ConnectDirectory.

```
HTTP/1.1 200 OK
x-amzn-RequestId: fa22d0f1-c0c3-11e6-9ed0-172b3469d361
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Mon, 12 Dec 2016 23:37:43 GMT

{
   "DirectoryId":"d-926example"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ConnectDirectory.md "../../../goto/cli2/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/ConnectDirectory.md "../../../goto/DotNetSDKV4/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ConnectDirectory.md "../../../goto/boto3/ds-2015-04-16/ConnectDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ConnectDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ConnectDirectory.md")
