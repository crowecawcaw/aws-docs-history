# CreateMicrosoftAD

Creates a Microsoft AD directory in the AWS Cloud. For more information, see [AWS Managed Microsoft AD](../admin-guide/directory_microsoft_ad.md "../admin-guide/directory_microsoft_ad.md") in the _AWS Directory Service Admin Guide_.

Before you call _CreateMicrosoftAD_, ensure that all of the required
permissions have been explicitly granted through a policy. For details about what permissions
are required to run the _CreateMicrosoftAD_ operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](../admin-guide/UsingWithDS_IAM_ResourcePermissions.md "../admin-guide/UsingWithDS_IAM_ResourcePermissions.md").

## Request Syntax

```
{
   "Description": "`string`",
   "Edition": "`string`",
   "Name": "`string`",
   "NetworkType": "`string`",
   "Password": "`string`",
   "ShortName": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "VpcSettings": {
      "SubnetIds": [ "`string`" ],
      "VpcId": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Description](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

A description for the directory. This label will appear on the AWS console
`Directory Details` page after the directory is created.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**[Edition](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

AWS Managed Microsoft AD is available in two editions: `Standard` and
`Enterprise`. `Enterprise` is the default.

Type: String

Valid Values: `Enterprise | Standard | Hybrid`

Required: No

**[Name](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

The fully qualified domain name for the AWS Managed Microsoft AD directory, such as
`corp.example.com`. This name will resolve inside your VPC only. It does not need
to be publicly resolvable.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: Yes

**[NetworkType](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

The network type for your domain. The default value is `IPv4` or `IPv6`
based on the provided subnet capabilities.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

**[Password](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

The password for the default administrative user named `Admin`.

If you need to change the password for the administrator account, you can use the [ResetUserPassword](API_ResetUserPassword.md "API_ResetUserPassword.md") API call.

Type: String

Pattern: `(?=^.{8,64}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])|(?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]))^.*`

Required: Yes

**[ShortName](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

The NetBIOS name for your domain, such as `CORP`. If you don't specify a
NetBIOS name, it will default to the first part of your directory DNS. For example,
`CORP` for the directory DNS `corp.example.com`.

Type: String

Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`

Required: No

**[Tags](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

The tags to be assigned to the AWS Managed Microsoft AD directory.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

**[VpcSettings](#API_CreateMicrosoftAD_RequestSyntax "#API_CreateMicrosoftAD_RequestSyntax")**

Contains VPC information for the [CreateDirectory](API_CreateDirectory.md "API_CreateDirectory.md") or [CreateMicrosoftAD](API_CreateMicrosoftAD.md "API_CreateMicrosoftAD.md") operation.

Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object

Required: Yes

## Response Syntax

```
{
   "DirectoryId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryId](#API_CreateMicrosoftAD_ResponseSyntax "#API_CreateMicrosoftAD_ResponseSyntax")**

The identifier of the directory that was created.

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

This example illustrates one usage of CreateMicrosoftAD.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 207
X-Amz-Target: DirectoryService_20150416.CreateMicrosoftAD
X-Amz-Date: 20161213T231510Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=5a73aaebf6dd7db4a17ffa5a0a5af7f8e134ad03034cb0b3e05e4f1a999d9e0a

 {
   "ShortName":"ad",
   "Password":"Str0ngP@ssw0rd",
   "Name":"ad.example.com",
   "Description":"Corporate AD directory",
   "VpcSettings":{
      "SubnetIds":[
         "subnet-ba0146de",
         "subnet-bef46bc8"
      ],
      "VpcId":"vpc-45025421"
   }
 }
```

### Example Response

This example illustrates one usage of CreateMicrosoftAD.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 00019586-c18a-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Tue, 13 Dec 2016 23:15:12 GMT

{
   "DirectoryId":"d-926example"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/cli2/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/DotNetSDKV3/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/boto3/ds-2015-04-16/CreateMicrosoftAD.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateMicrosoftAD.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateMicrosoftAD.md")
