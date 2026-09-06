

# CreateMicrosoftAD
<a name="API_CreateMicrosoftAD"></a>

Creates a Microsoft AD directory in the AWS Cloud. For more information, see [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html) in the * AWS Directory Service Admin Guide*.

Before you call *CreateMicrosoftAD*, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the *CreateMicrosoftAD* operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html).

## Request Syntax
<a name="API_CreateMicrosoftAD_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "Edition": "{{string}}",
   "Name": "{{string}}",
   "NetworkType": "{{string}}",
   "Password": "{{string}}",
   "ShortName": "{{string}}",
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
<a name="API_CreateMicrosoftAD_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-Description"></a>
A description for the directory. This label will appear on the AWS console `Directory Details` page after the directory is created.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

 ** [Edition](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-Edition"></a>
 AWS Managed Microsoft AD is available in two editions: `Standard` and `Enterprise`. `Enterprise` is the default.  
Type: String  
Valid Values: `Enterprise | Standard | Hybrid`   
Required: No

 ** [Name](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-Name"></a>
The fully qualified domain name for the AWS Managed Microsoft AD directory, such as `corp.example.com`. This name will resolve inside your VPC only. It does not need to be publicly resolvable.  
Type: String  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+$`   
Required: Yes

 ** [NetworkType](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-NetworkType"></a>
 The network type for your domain. The default value is `IPv4` or `IPv6` based on the provided subnet capabilities.  
Type: String  
Valid Values: `Dual-stack | IPv4 | IPv6`   
Required: No

 ** [Password](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-Password"></a>
The password for the default administrative user named `Admin`.  
If you need to change the password for the administrator account, you can use the [ResetUserPassword](API_ResetUserPassword.md) API call.  
Type: String  
Pattern: `(?=^.{8,64}$)((?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9\s])(?=.*[a-z])|(?=.*[^A-Za-z0-9\s])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9\s]))^.*`   
Required: Yes

 ** [ShortName](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-ShortName"></a>
The NetBIOS name for your domain, such as `CORP`. If you don't specify a NetBIOS name, it will default to the first part of your directory DNS. For example, `CORP` for the directory DNS `corp.example.com`.   
Type: String  
Pattern: `^[^\\/:*?"<>|.]+[^\\/:*?"<>|]*$`   
Required: No

 ** [Tags](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-Tags"></a>
The tags to be assigned to the AWS Managed Microsoft AD directory.  
Type: Array of [Tag](API_Tag.md) objects  
Required: No

 ** [VpcSettings](#API_CreateMicrosoftAD_RequestSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-request-VpcSettings"></a>
Contains VPC information for the [CreateDirectory](API_CreateDirectory.md) or [CreateMicrosoftAD](#API_CreateMicrosoftAD) operation.  
Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md) object  
Required: Yes

## Response Syntax
<a name="API_CreateMicrosoftAD_ResponseSyntax"></a>

```
{
   "DirectoryId": "string"
}
```

## Response Elements
<a name="API_CreateMicrosoftAD_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_CreateMicrosoftAD_ResponseSyntax) **   <a name="DirectoryService-CreateMicrosoftAD-response-DirectoryId"></a>
The identifier of the directory that was created.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_CreateMicrosoftAD_Errors"></a>

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

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_CreateMicrosoftAD_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_CreateMicrosoftAD_Example_1"></a>

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
<a name="API_CreateMicrosoftAD_Example_2"></a>

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
<a name="API_CreateMicrosoftAD_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/CreateMicrosoftAD) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CreateMicrosoftAD) 