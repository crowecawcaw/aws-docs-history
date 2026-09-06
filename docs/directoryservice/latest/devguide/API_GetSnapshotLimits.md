

# GetSnapshotLimits
<a name="API_GetSnapshotLimits"></a>

Obtains the manual snapshot limits for a directory.

## Request Syntax
<a name="API_GetSnapshotLimits_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetSnapshotLimits_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_GetSnapshotLimits_RequestSyntax) **   <a name="DirectoryService-GetSnapshotLimits-request-DirectoryId"></a>
Contains the identifier of the directory to obtain the limits for.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_GetSnapshotLimits_ResponseSyntax"></a>

```
{
   "SnapshotLimits": { 
      "ManualSnapshotsCurrentCount": number,
      "ManualSnapshotsLimit": number,
      "ManualSnapshotsLimitReached": boolean
   }
}
```

## Response Elements
<a name="API_GetSnapshotLimits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotLimits](#API_GetSnapshotLimits_ResponseSyntax) **   <a name="DirectoryService-GetSnapshotLimits-response-SnapshotLimits"></a>
A [SnapshotLimits](API_SnapshotLimits.md) object that contains the manual snapshot limits for the specified directory.  
Type: [SnapshotLimits](API_SnapshotLimits.md) object

## Errors
<a name="API_GetSnapshotLimits_Errors"></a>

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
<a name="API_GetSnapshotLimits_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_GetSnapshotLimits_Example_1"></a>

This example illustrates one usage of GetSnapshotLimits.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 31
X-Amz-Target: DirectoryService_20150416.GetSnapshotLimits
X-Amz-Date: 20161214T224507Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=f9ba790cf905e14fa97fd1ed6a961c72d83a23f3e54ab126d8e4a30ec14d3cdb

 {
   "DirectoryId": "d-926example"
 }
```

### Example Response
<a name="API_GetSnapshotLimits_Example_2"></a>

This example illustrates one usage of GetSnapshotLimits.

```
HTTP/1.1 200 OK
x-amzn-RequestId: f7895979-c24e-11e6-a0ba-6bb2a89ebc49
Content-Type: application/x-amz-json-1.1
Content-Length: 113
Date: Wed, 14 Dec 2016 22:45:09 GMT

{
   "SnapshotLimits":{
      "ManualSnapshotsCurrentCount":1,
      "ManualSnapshotsLimit":5,
      "ManualSnapshotsLimitReached":false
   }
}
```

## See Also
<a name="API_GetSnapshotLimits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/GetSnapshotLimits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/GetSnapshotLimits) 