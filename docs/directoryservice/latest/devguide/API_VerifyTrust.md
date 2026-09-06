

# VerifyTrust
<a name="API_VerifyTrust"></a>

 AWS Directory Service for Microsoft Active Directory allows you to configure and verify trust relationships.

This action verifies a trust relationship between your AWS Managed Microsoft AD directory and an external domain.

## Request Syntax
<a name="API_VerifyTrust_RequestSyntax"></a>

```
{
   "TrustId": "{{string}}"
}
```

## Request Parameters
<a name="API_VerifyTrust_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [TrustId](#API_VerifyTrust_RequestSyntax) **   <a name="DirectoryService-VerifyTrust-request-TrustId"></a>
The unique Trust ID of the trust relationship to verify.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_VerifyTrust_ResponseSyntax"></a>

```
{
   "TrustId": "string"
}
```

## Response Elements
<a name="API_VerifyTrust_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TrustId](#API_VerifyTrust_ResponseSyntax) **   <a name="DirectoryService-VerifyTrust-response-TrustId"></a>
The unique Trust ID of the trust relationship that was verified.  
Type: String  
Pattern: `^t-[0-9a-f]{10}$` 

## Errors
<a name="API_VerifyTrust_Errors"></a>

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
<a name="API_VerifyTrust_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_VerifyTrust_Example_1"></a>

This example illustrates one usage of VerifyTrust.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 27
X-Amz-Target: DirectoryService_20150416.VerifyTrust
X-Amz-Date: 20161215T191010Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161215/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=249c3fb0ac94d57cc9abb43f6422fe237fce723ddd9462a4666712e46e3b5371

 {
   "TrustId": "t-9267353df0"
 }
```

### Example Response
<a name="API_VerifyTrust_Example_2"></a>

This example illustrates one usage of VerifyTrust.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 3343bc79-c18f-11e6-ba7f-e33ae22bc363
Content-Type: application/x-amz-json-1.1
Content-Length: 26
Date: Thu, 15 Dec 2016 19:10:12 GMT

{
   "TrustId": "t-9267353df0"
}
```

## See Also
<a name="API_VerifyTrust_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/VerifyTrust) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/VerifyTrust) 