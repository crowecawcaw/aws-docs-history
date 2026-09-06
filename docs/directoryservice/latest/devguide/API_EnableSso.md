

# EnableSso
<a name="API_EnableSso"></a>

Enables single sign-on for a directory. Single sign-on allows users in your directory to access certain AWS services from a computer joined to the directory without having to enter their credentials separately.

## Request Syntax
<a name="API_EnableSso_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Password": "{{string}}",
   "UserName": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableSso_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_EnableSso_RequestSyntax) **   <a name="DirectoryService-EnableSso-request-DirectoryId"></a>
The identifier of the directory for which to enable single-sign on.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Password](#API_EnableSso_RequestSyntax) **   <a name="DirectoryService-EnableSso-request-Password"></a>
The password of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. For more information, see the *UserName* parameter.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: No

 ** [UserName](#API_EnableSso_RequestSyntax) **   <a name="DirectoryService-EnableSso-request-UserName"></a>
The username of an alternate account to use to enable single-sign on. This is only used for AD Connector directories. This account must have privileges to add a service principal name.  
If the AD Connector service account does not have privileges to add a service principal name, you can specify an alternate account with the *UserName* and *Password* parameters. These credentials are only used to enable single sign-on and are not stored by the service. The AD Connector service account is not changed.  
Type: String  
Length Constraints: Minimum length of 1.  
Pattern: `[a-zA-Z0-9._-]+`   
Required: No

## Response Elements
<a name="API_EnableSso_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableSso_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthenticationFailedException **   
An authentication error occurred.    
 ** Message **   
The textual message for the exception.  
 ** RequestId **   
The identifier of the request that caused the exception.
HTTP Status Code: 400

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** EntityDoesNotExistException **   
The specified entity could not be found.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InsufficientPermissionsException **   
The account does not have sufficient permission to perform the operation.    
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
<a name="API_EnableSso_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_EnableSso_Example_1"></a>

This example illustrates one usage of EnableSso.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 80
X-Amz-Target: DirectoryService_20150416.EnableSso
X-Amz-Date: 20161214T220301Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=88acc99818605aa438eb86b5be59daecce370c7db16e5e84311508e575ea0515

 {
   "UserName": "Admin",
   "DirectoryId": "d-926example",
   "Password": "Str0ngP@ssw0rd"
 }
```

### Example Response
<a name="API_EnableSso_Example_2"></a>

This example illustrates one usage of EnableSso.

```
HTTP/1.1 200 OK
x-amzn-RequestId: fcd40ac9-c247-11e6-a7ca-f9a52a6a0390
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 22:03:03 GMT

{  
  
}
```

## See Also
<a name="API_EnableSso_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/EnableSso) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/EnableSso) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/EnableSso) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/EnableSso) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/EnableSso) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/EnableSso) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/EnableSso) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/EnableSso) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/EnableSso) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/EnableSso) 