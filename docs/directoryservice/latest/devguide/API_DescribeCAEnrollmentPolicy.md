

# DescribeCAEnrollmentPolicy
<a name="API_DescribeCAEnrollmentPolicy"></a>

Retrieves detailed information about the certificate authority (CA) enrollment policy for the specified directory. This policy determines how client certificates are automatically enrolled and managed through AWS Private Certificate Authority. 

## Request Syntax
<a name="API_DescribeCAEnrollmentPolicy_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeCAEnrollmentPolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeCAEnrollmentPolicy_RequestSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-request-DirectoryId"></a>
The identifier of the directory for which to retrieve the CA enrollment policy information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DescribeCAEnrollmentPolicy_ResponseSyntax"></a>

```
{
   "CaEnrollmentPolicyStatus": "string",
   "CaEnrollmentPolicyStatusReason": "string",
   "DirectoryId": "string",
   "LastUpdatedDateTime": number,
   "PcaConnectorArn": "string"
}
```

## Response Elements
<a name="API_DescribeCAEnrollmentPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CaEnrollmentPolicyStatus](#API_DescribeCAEnrollmentPolicy_ResponseSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-response-CaEnrollmentPolicyStatus"></a>
The current status of the CA enrollment policy. This indicates if automatic certificate enrollment is currently active, inactive, or in a transitional state.  
Valid values:  
+  `IN_PROGRESS` - The policy is being activated T
+  `SUCCESS` - The policy is active and automatic certificate enrollment is operational
+  `FAILED` - The policy activation or deactivation failed
+  `DISABLING` - The policy is being deactivated
+  `DISABLED` - The policy is inactive and automatic certificate enrollment is not available
+  `IMPAIRED` - Network connectivity is impaired.
Type: String  
Valid Values: `InProgress | Success | Failed | Disabling | Disabled | Impaired` 

 ** [CaEnrollmentPolicyStatusReason](#API_DescribeCAEnrollmentPolicy_ResponseSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-response-CaEnrollmentPolicyStatusReason"></a>
Additional information explaining the current status of the CA enrollment policy, particularly useful when the policy is in an error or transitional state.  
Type: String

 ** [DirectoryId](#API_DescribeCAEnrollmentPolicy_ResponseSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-response-DirectoryId"></a>
The identifier of the directory associated with this CA enrollment policy.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$` 

 ** [LastUpdatedDateTime](#API_DescribeCAEnrollmentPolicy_ResponseSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-response-LastUpdatedDateTime"></a>
The date and time when the CA enrollment policy was last modified or updated.  
Type: Timestamp

 ** [PcaConnectorArn](#API_DescribeCAEnrollmentPolicy_ResponseSyntax) **   <a name="DirectoryService-DescribeCAEnrollmentPolicy-response-PcaConnectorArn"></a>
The Amazon Resource Name (ARN) of the AWS Private Certificate Authority (PCA) connector that is configured for automatic certificate enrollment in this directory.  
Type: String  
Pattern: `^arn:[\w-]+:pca-connector-ad:[\w-]+:[0-9]+:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}$` 

## Errors
<a name="API_DescribeCAEnrollmentPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeCAEnrollmentPolicy_Examples"></a>

The following examples are formatted for legibility.

### Describe CA enrollment policy
<a name="API_DescribeCAEnrollmentPolicy_Example_1"></a>

The following example describes the CA enrollment policy for a directory.

#### Sample Request
<a name="API_DescribeCAEnrollmentPolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: DirectoryService_20150416.DescribeCAEnrollmentPolicy
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
<a name="API_DescribeCAEnrollmentPolicy_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: Tue, 15 Aug 2023 14:30:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 245
x-amzn-RequestId: 12345678-1234-1234-1234-123456789012

{
  "DirectoryId": "d-926example",
  "PcaConnectorArn": "arn:aws:pca-connector-ad:us-east-1:123456789012:connector/c-123456789abcdef01",
  "CaEnrollmentPolicyStatus": "SUCCESS",
  "LastUpdatedDateTime": "2023-08-15T14:30:00.000Z",
  "CaEnrollmentPolicyStatusReason": "Policy successfully activated and operational"
}
```

### Response when CA enrollment is disabled
<a name="API_DescribeCAEnrollmentPolicy_Example_2"></a>

If CA enrollment is disabled, this returns an empty response. 

#### Sample Request
<a name="API_DescribeCAEnrollmentPolicy_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: DirectoryService_20150416.DescribeCAEnrollmentPolicy
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
<a name="API_DescribeCAEnrollmentPolicy_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: Thu, 10 Aug 2023 09:15:00 GMT
Content-Type: application/x-amz-json-1.1
Content-Length: 156
x-amzn-RequestId: 87654321-4321-4321-4321-210987654321

{}
```

## See Also
<a name="API_DescribeCAEnrollmentPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeCAEnrollmentPolicy) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeCAEnrollmentPolicy) 