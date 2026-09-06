

# CreateDirectory
<a name="API_CreateDirectory"></a>

**Note**  
Simple AD is no longer open to new customers. For capabilities similar to Simple AD, explore Directory Service Managed Microsoft AD or AD Connector. For more information, see [Simple AD availability changes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple-ad-availability-change.html).

Creates a Simple AD directory. For more information, see [Simple Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html) in the * AWS Directory Service Admin Guide*.

Before you call `CreateDirectory`, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the `CreateDirectory` operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html).

## Request Syntax
<a name="API_CreateDirectory_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Name": "{{string}}",
   "NetworkType": "{{string}}",
   "Password": "{{string}}",
   "ShortName": "{{string}}",
   "Size": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "VpcSettings": { 
      "SubnetIds": [ "{{string}}" ],
      "VpcId": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-Description"></a>
A description for the directory.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** [Name](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-Name"></a>
The fully qualified name for the directory, such as `corp.example.com`.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: Yes

 ** [NetworkType](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-NetworkType"></a>
The network type for your directory. Simple AD supports IPv4 and Dual-stack only.  
Type: String  
Valid Values: `Dual-stack | IPv4 | IPv6`   
Required: No

 ** [Password](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-Password"></a>
The password for the directory administrator. The directory creation process creates a directory administrator account with the user name `Administrator` and this password.  
If you need to change the password for the administrator account, you can use the [ResetUserPassword](API_ResetUserPassword.md) API call.  
The regex pattern for this string is made up of the following conditions:  
+ Length (?=^.{8,64}$) – Must be between 8 and 64 characters
AND any 3 of the following password complexity rules required by Active Directory:  
+ Numbers and upper case and lowercase (?=.\*\\d)(?=.\*[A-Z])(?=.\*[a-z])
+ Numbers and special characters and lower case (?=.\*\\d)(?=.\*[^A-Za-z0-9\\s])(?=.\*[a-z])
+ Special characters and upper case and lower case (?=.\*[^A-Za-z0-9\\s])(?=.\*[A-Z])(?=.\*[a-z])
+ Numbers and upper case and special characters (?=.\*\\d)(?=.\*[A-Z])(?=.\*[^A-Za-z0-9\\s])
For additional information about how Active Directory passwords are enforced, see [Password must meet complexity requirements](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements) on the Microsoft website.  
Type: String  
Pattern: `(?=^.{8,64}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])|(?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]))^.*`   
Required: Yes

 ** [ShortName](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-ShortName"></a>
The NetBIOS name of the directory, such as `CORP`.  
Type: String  
Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`   
Required: No

 ** [Size](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-Size"></a>
The size of the directory.  
Type: String  
Valid Values: `Small | Large`   
Required: Yes

 ** [Tags](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-Tags"></a>
The tags to be assigned to the Simple AD directory.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VpcSettings](#API_CreateDirectory_RequestSyntax) **   <a name="DirectoryService-CreateDirectory-request-VpcSettings"></a>
A [DirectoryVpcSettings](API_DirectoryVpcSettings.md) object that contains additional information for the operation.  
Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md) object  
Required: No

## Response Syntax
<a name="API_CreateDirectory_ResponseSyntax"></a>

```
{
   "DirectoryId": "string"
}
```

## Response Elements
<a name="API_CreateDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_CreateDirectory_ResponseSyntax) **   <a name="DirectoryService-CreateDirectory-response-DirectoryId"></a>
The identifier of the directory that was created.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_CreateDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryLimitExceededException **   
The maximum number of directories in the region has been reached. You can use the [GetDirectoryLimits](API_GetDirectoryLimits.md) operation to determine your directory limits in the region.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidParameterException **   
One or more parameters are not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

## Examples
<a name="API_CreateDirectory_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_CreateDirectory_Example_1"></a>

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
<a name="API_CreateDirectory_Example_2"></a>

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
<a name="API_CreateDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/CreateDirectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CreateDirectory) 