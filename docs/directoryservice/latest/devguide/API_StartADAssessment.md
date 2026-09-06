

# StartADAssessment
<a name="API_StartADAssessment"></a>

Initiates a directory assessment to validate your self-managed AD environment for hybrid domain join. The assessment checks compatibility and connectivity of the self-managed AD environment.

A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: `CUSTOMER` and `SYSTEM`. Your AWS account has a limit of 100 `CUSTOMER` directory assessments.

The assessment process typically takes 30 minutes or more to complete. The assessment process is asynchronous and you can monitor it with `DescribeADAssessment`.

The `InstanceIds` must have a one-to-one correspondence with `CustomerDnsIps`, meaning that if the IP address for instance i-10243410 is 10.24.34.100 and the IP address for instance i-10243420 is 10.24.34.200, then the input arrays must maintain the same order relationship, either [10.24.34.100, 10.24.34.200] paired with [i-10243410, i-10243420] or [10.24.34.200, 10.24.34.100] paired with [i-10243420, i-10243410].

Note: You must provide exactly one `DirectoryId` or `AssessmentConfiguration`.

## Request Syntax
<a name="API_StartADAssessment_RequestSyntax"></a>

```
{
   "AssessmentConfiguration": { 
      "CustomerDnsIps": [ "{{string}}" ],
      "DnsName": "{{string}}",
      "InstanceIds": [ "{{string}}" ],
      "SecurityGroupIds": [ "{{string}}" ],
      "VpcSettings": { 
         "SubnetIds": [ "{{string}}" ],
         "VpcId": "{{string}}"
      }
   },
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartADAssessment_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AssessmentConfiguration](#API_StartADAssessment_RequestSyntax) **   <a name="DirectoryService-StartADAssessment-request-AssessmentConfiguration"></a>
Configuration parameters for the directory assessment, including DNS server information, domain name, Amazon VPC subnet, and AWS System Manager managed node details.  
Type: [AssessmentConfiguration](API_AssessmentConfiguration.md) object  
Required: No

 ** [DirectoryId](#API_StartADAssessment_RequestSyntax) **   <a name="DirectoryService-StartADAssessment-request-DirectoryId"></a>
The identifier of the directory for which to perform the assessment. This should be an existing directory. If the assessment is not for an existing directory, this parameter should be omitted.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

## Response Syntax
<a name="API_StartADAssessment_ResponseSyntax"></a>

```
{
   "AssessmentId": "string"
}
```

## Response Elements
<a name="API_StartADAssessment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssessmentId](#API_StartADAssessment_ResponseSyntax) **   <a name="DirectoryService-StartADAssessment-response-AssessmentId"></a>
The unique identifier of the newly started directory assessment. Use this identifier to monitor assessment progress and retrieve results.  
Type: String  
Pattern: `^da-[0-9a-f]{18}$` 

## Errors
<a name="API_StartADAssessment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ADAssessmentLimitExceededException **   
A directory assessment is automatically created when you create a hybrid directory. There are two types of assessments: `CUSTOMER` and `SYSTEM`. Your AWS account has a limit of 100 `CUSTOMER` directory assessments.  
If you attempt to create a hybrid directory; and you already have 100 `CUSTOMER` directory assessments;, you will encounter an error. Delete assessments to free up capacity before trying again.  
You can request an increase to your `CUSTOMER` directory assessment quota by contacting customer support or delete existing CUSTOMER directory assessments; to free up capacity.    
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
<a name="API_StartADAssessment_Examples"></a>

The following examples are formatted for legibility.

### Example Pre-join Request
<a name="API_StartADAssessment_Example_1"></a>

This example illustrates one usage of StartADAssessment.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 312
X-Amz-Target: DirectoryService_20150416.StartADAssessment
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
// Request - prejoin
{
    "AssessmentConfiguration": {
        "CustomerDnsIps": ["10.24.34.100", "10.24.34.200"],
        "DnsName": "ad.example.com",
        "VpcSettings": {
            "VpcId": "vpc-04c978example126f",
            "SubnetIds": ["subnet-0994bexampled9ea7", "subnet-095e06examplee7e7"]
        },
        "InstanceIds": ["i-10243410", "i-10243420"],
        "SecurityGroupIds": ["sg-0fbb77examplef199"]
    }
}
```

### Example Post-join Request
<a name="API_StartADAssessment_Example_2"></a>

This example illustrates one usage of StartADAssessment.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 312
X-Amz-Target: DirectoryService_20150416.StartADAssessment
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

// Request - postjoin
{
    "DirectoryId": "d-926example"
}
```

### Example Response
<a name="API_StartADAssessment_Example_3"></a>

This example illustrates one usage of StartADAssessment.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 45
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "AssessmentId": "da-1234567890example1"
}
```

## See Also
<a name="API_StartADAssessment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/StartADAssessment) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/StartADAssessment) 