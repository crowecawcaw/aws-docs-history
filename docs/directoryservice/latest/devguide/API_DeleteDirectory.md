

# DeleteDirectory
<a name="API_DeleteDirectory"></a>

Deletes an AWS Directory Service directory.

Before you call `DeleteDirectory`, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the `DeleteDirectory` operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html).

## Request Syntax
<a name="API_DeleteDirectory_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteDirectory_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DeleteDirectory_RequestSyntax) **   <a name="DirectoryService-DeleteDirectory-request-DirectoryId"></a>
The identifier of the directory to delete.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteDirectory_ResponseSyntax"></a>

```
{
   "DirectoryId": "string"
}
```

## Response Elements
<a name="API_DeleteDirectory_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DirectoryId](#API_DeleteDirectory_ResponseSyntax) **   <a name="DirectoryService-DeleteDirectory-response-DirectoryId"></a>
The directory identifier.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

## Errors
<a name="API_DeleteDirectory_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

## Examples
<a name="API_DeleteDirectory_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DeleteDirectory_Example_1"></a>

This example illustrates one usage of DeleteDirectory.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: DirectoryService_20150416.DeleteDirectory
X-Amz-Date: 20161214T002424Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=b542aa77381528e27afcf08b229252606fa79723695fb2d19b81b51d66d7f92d

 {
   "DirectoryId": "d-926example"
 }
```

### Example Response
<a name="API_DeleteDirectory_Example_2"></a>

This example illustrates one usage of DeleteDirectory.

```
HTTP/1.1 200 OK
x-amzn-RequestId: abcbeb82-c193-11e6-bf9e-272b6602bf9f
Content-Type: application/x-amz-json-1.1
Content-Length: 30
Date: Wed, 14 Dec 2016 00:24:26 GMT

{
   "DirectoryId":"d-926example"
}
```

## See Also
<a name="API_DeleteDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DeleteDirectory) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DeleteDirectory) 