

# DisableCAEnrollmentPolicy
<a name="API_DisableCAEnrollmentPolicy"></a>

Disables the certificate authority (CA) enrollment policy for the specified directory. This stops automatic certificate enrollment and management for domain-joined clients, but does not affect existing certificates.

**Important**  
Disabling the CA enrollment policy prevents new certificates from being automatically enrolled, but existing certificates remain valid and functional until they expire.

## Request Syntax
<a name="API_DisableCAEnrollmentPolicy_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisableCAEnrollmentPolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DisableCAEnrollmentPolicy_RequestSyntax) **   <a name="DirectoryService-DisableCAEnrollmentPolicy-request-DirectoryId"></a>
The identifier of the directory for which to disable the CA enrollment policy.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Elements
<a name="API_DisableCAEnrollmentPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DisableCAEnrollmentPolicy_Errors"></a>

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

 ** DirectoryUnavailableException **   
The specified directory is unavailable.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DisableAlreadyInProgressException **   
A disable operation for CA enrollment policy is already in progress for this directory.    
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

## Examples
<a name="API_DisableCAEnrollmentPolicy_Examples"></a>

The following examples are formatted for legibility.

### Disable CA enrollment policy
<a name="API_DisableCAEnrollmentPolicy_Example_1"></a>

The following example disables the CA enrollment policy for a directory.

#### Sample Request
<a name="API_DisableCAEnrollmentPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: DirectoryService_20150416.DisableCAEnrollmentPolicy
X-Amz-Date: 20230815T143000Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Authorization: AWS4-HMAC-SHA256
  Credential=AKIAIOSFODNN7EXAMPLE/20230815/us-west-2/ds/aws4_request,
  SignedHeaders=host;x-amz-date;x-amz-target,
  Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
  "DirectoryId": "d-926example"
}
```

#### Sample Response
<a name="API_DisableCAEnrollmentPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 Aug 2023 14:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 2
x-amzn-RequestId: 12345678-1234-1234-1234-123456789012

{}
```

## See Also
<a name="API_DisableCAEnrollmentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DisableCAEnrollmentPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DisableCAEnrollmentPolicy) 