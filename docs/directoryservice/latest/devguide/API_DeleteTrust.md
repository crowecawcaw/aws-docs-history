

# DeleteTrust
<a name="API_DeleteTrust"></a>

Deletes an existing trust relationship between your AWS Managed Microsoft AD directory and an external domain.

## Request Syntax
<a name="API_DeleteTrust_RequestSyntax"></a>

```
{
   "DeleteAssociatedConditionalForwarder": {{boolean}},
   "TrustId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteTrust_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DeleteAssociatedConditionalForwarder](#API_DeleteTrust_RequestSyntax) **   <a name="DirectoryService-DeleteTrust-request-DeleteAssociatedConditionalForwarder"></a>
Delete a conditional forwarder as part of a DeleteTrustRequest.  
Type: Boolean  
Required: No

 ** [TrustId](#API_DeleteTrust_RequestSyntax) **   <a name="DirectoryService-DeleteTrust-request-TrustId"></a>
The Trust ID of the trust relationship to be deleted.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteTrust_ResponseSyntax"></a>

```
{
   "TrustId": "string"
}
```

## Response Elements
<a name="API_DeleteTrust_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrustId](#API_DeleteTrust_ResponseSyntax) **   <a name="DirectoryService-DeleteTrust-response-TrustId"></a>
The Trust ID of the trust relationship that was deleted.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$` 

## Errors
<a name="API_DeleteTrust_Errors"></a>

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
<a name="API_DeleteTrust_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DeleteTrust_Example_1"></a>

This example illustrates one usage of DeleteTrust.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 73
X-Amz-Target: DirectoryService_20150416.DeleteTrust
X-Amz-Date: 20161214T013332Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=ced49ef4329d015ebde09b7bc586eee4455b0b1e6608ade2fd6cd123440bbd6d

 {
   "TrustId": "t-9267353743",
   "DeleteAssociatedConditionalForwarder": true
 }
```

### Example Response
<a name="API_DeleteTrust_Example_2"></a>

This example illustrates one usage of DeleteTrust.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 54425c2e-c19d-11e6-b0d6-83af322c90cd
Content-Type: application/x-amz-json-1.1
Content-Length: 26
Date: Wed, 14 Dec 2016 01:33:37 GMT

{
   "TrustId":"t-9267353743"
}
```

## See Also
<a name="API_DeleteTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DeleteTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DeleteTrust) 