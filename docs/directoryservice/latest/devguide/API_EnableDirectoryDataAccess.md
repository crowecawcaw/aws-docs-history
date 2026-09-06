

# EnableDirectoryDataAccess
<a name="API_EnableDirectoryDataAccess"></a>

Enables access to directory data via the Directory Service Data API for the specified directory. For more information, see [Directory Service Data API Reference](https://docs.aws.amazon.com/directoryservicedata/latest/DirectoryServiceDataAPIReference/Welcome.html).

## Request Syntax
<a name="API_EnableDirectoryDataAccess_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_EnableDirectoryDataAccess_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_EnableDirectoryDataAccess_RequestSyntax) **   <a name="DirectoryService-EnableDirectoryDataAccess-request-DirectoryId"></a>
The directory identifier.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Elements
<a name="API_EnableDirectoryDataAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableDirectoryDataAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryDoesNotExistException **   
The specified directory does not exist in the system.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryInDesiredStateException **   
 The directory is already updated to desired update type settings.     
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryUnavailableException **   
The specified directory is unavailable.    
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
<a name="API_EnableDirectoryDataAccess_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_EnableDirectoryDataAccess_Example_1"></a>

This example illustrates one usage of EnableDirectoryDataAccess.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 98
X-Amz-Target: DirectoryService_20150416.EnableDirectoryDataAccess
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
<a name="API_EnableDirectoryDataAccess_Example_2"></a>

This example illustrates one usage of EnableDirectoryDataAccess.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 21:20:31 GMT

 {
 }
```

## See Also
<a name="API_EnableDirectoryDataAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/EnableDirectoryDataAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/EnableDirectoryDataAccess) 