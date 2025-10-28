# CreateDirectory

Creates a Simple AD directory. For more information, see [Simple Active Directory](../admin-guide/directory_simple_ad.md "../admin-guide/directory_simple_ad.md") in the _AWS Directory Service Admin Guide_.

Before you call `CreateDirectory`, ensure that all of the required permissions
have been explicitly granted through a policy. For details about what permissions are required
to run the `CreateDirectory` operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](../admin-guide/UsingWithDS_IAM_ResourcePermissions.md "../admin-guide/UsingWithDS_IAM_ResourcePermissions.md").

## Request Syntax

```
{
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
   ],
   "VpcSettings": {
      "SubnetIds": [ "`string`" ],
      "VpcId": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Description](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

A description for the directory.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 128.

Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`

Required: No

**[Name](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The fully qualified name for the directory, such as `corp.example.com`.

Type: String

Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`

Required: Yes

**[NetworkType](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The network type for your directory. Simple AD supports IPv4 and Dual-stack only.

Type: String

Valid Values: `Dual-stack | IPv4 | IPv6`

Required: No

**[Password](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The password for the directory administrator. The directory creation process creates a
directory administrator account with the user name `Administrator` and this
password.

If you need to change the password for the administrator account, you can use the [ResetUserPassword](API_ResetUserPassword.md "API_ResetUserPassword.md") API call.

The regex pattern for this string is made up of the following conditions:

- Length (?=^.{8,64}$) – Must be between 8 and 64 characters

AND any 3 of the following password complexity rules required by Active Directory:

- Numbers and upper case and lowercase (?=.\*\d)(?=.\*[A-Z])(?=.\*[a-z])
- Numbers and special characters and lower case
  (?=.\*\d)(?=.\*[^A-Za-z0-9\s])(?=.\*[a-z])
- Special characters and upper case and lower case
  (?=.\*[^A-Za-z0-9\s])(?=.\*[A-Z])(?=.\*[a-z])
- Numbers and upper case and special characters
  (?=.\*\d)(?=.\*[A-Z])(?=.\*[^A-Za-z0-9\s])

For additional information about how Active Directory passwords are enforced, see [Password must meet complexity requirements](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements "https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements") on the Microsoft website.

Type: String

Pattern: `(?=^.{8,64}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])|(?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]))^.*`

Required: Yes

**[ShortName](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The NetBIOS name of the directory, such as `CORP`.

Type: String

Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`

Required: No

**[Size](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The size of the directory.

Type: String

Valid Values: `Small | Large`

Required: Yes

**[Tags](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

The tags to be assigned to the Simple AD directory.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Required: No

**[VpcSettings](#API_CreateDirectory_RequestSyntax "#API_CreateDirectory_RequestSyntax")**

A [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object that contains additional information for
the operation.

Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object

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

**[DirectoryId](#API_CreateDirectory_ResponseSyntax "#API_CreateDirectory_ResponseSyntax")**

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

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of CreateDirectory.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 245
X-Amz-Target: DirectoryService_20150416.CreateDirectory
X-Amz-Date: 20161213T222613Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e0bf599277231d294b0ebb1c7ad7a68aafdfc49db016adbee32a167954c53d54

 {
   "Description":"Regional directory for example.com",
   "VpcSettings":{
      "SubnetIds":[
         "subnet-ba0146de",
         "subnet-bef46bc8"
      ],
      "VpcId":"vpc-45025421"
   },
   "Name":"seattle.example.com",
   "ShortName":"seattle",
   "Password":"Str0ngP@ssw0rd",
   "Size":"Small"
 }
```

### Example Response

This example illustrates one usage of CreateDirectory.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 298112b6-c183-11e6-9b49-eff49203d13b
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Tue, 13 Dec 2016 22:26:17 GMT

{
   "DirectoryId":"d-926example"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/CreateDirectory.md "../../../goto/cli2/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/CreateDirectory.md "../../../goto/DotNetSDKV3/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForCpp/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForGoV2/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForJavaV2/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForKotlin/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForPHPV3/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/CreateDirectory.md "../../../goto/boto3/ds-2015-04-16/CreateDirectory.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/CreateDirectory.md "../../../goto/SdkForRubyV3/ds-2015-04-16/CreateDirectory.md")
