

# DeleteConditionalForwarder
<a name="API_DeleteConditionalForwarder"></a>

Deletes a conditional forwarder that has been set up for your AWS directory.

## Request Syntax
<a name="API_DeleteConditionalForwarder_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "RemoteDomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteConditionalForwarder_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DeleteConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-DeleteConditionalForwarder-request-DirectoryId"></a>
The directory ID for which you are deleting the conditional forwarder.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [RemoteDomainName](#API_DeleteConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-DeleteConditionalForwarder-request-RemoteDomainName"></a>
The fully qualified domain name (FQDN) of the remote domain with which you are deleting the conditional forwarder.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`   
Required: Yes

## Response Elements
<a name="API_DeleteConditionalForwarder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteConditionalForwarder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
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

 ** EntityDoesNotExistException **   
The specified entity could not be found.    
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
<a name="API_DeleteConditionalForwarder_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DeleteConditionalForwarder_Example_1"></a>

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
<a name="API_DeleteConditionalForwarder_Example_2"></a>

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
<a name="API_DeleteConditionalForwarder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DeleteConditionalForwarder) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DeleteConditionalForwarder) 