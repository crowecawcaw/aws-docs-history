

# CreateSnapshot
<a name="API_CreateSnapshot"></a>

Creates a snapshot of a Simple AD or Microsoft AD directory in the AWS cloud.

**Note**  
You cannot take snapshots of AD Connector directories.

## Request Syntax
<a name="API_CreateSnapshot_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_CreateSnapshot_RequestSyntax) **   <a name="DirectoryService-CreateSnapshot-request-DirectoryId"></a>
The identifier of the directory of which to take a snapshot.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Name](#API_CreateSnapshot_RequestSyntax) **   <a name="DirectoryService-CreateSnapshot-request-Name"></a>
The descriptive name to apply to the snapshot.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]*$`   
Required: No

## Response Syntax
<a name="API_CreateSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotId": "string"
}
```

## Response Elements
<a name="API_CreateSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotId](#API_CreateSnapshot_ResponseSyntax) **   <a name="DirectoryService-CreateSnapshot-response-SnapshotId"></a>
The identifier of the snapshot that was created.  
Type: String  
Pattern: `^s-[0-9a-f]{10}$` 

## Errors
<a name="API_CreateSnapshot_Errors"></a>

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

 ** SnapshotLimitExceededException **   
The maximum number of manual snapshots for the directory has been reached. You can use the [GetSnapshotLimits](API_GetSnapshotLimits.md) operation to determine the snapshot limits for a directory.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_CreateSnapshot_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_CreateSnapshot_Example_1"></a>

This example illustrates one usage of CreateSnapshot.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 58
X-Amz-Target: DirectoryService_20150416.CreateSnapshot
X-Amz-Date: 20161213T233356Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=8789d87320d00e26fec4d745a34b3c5d898e4e89bf96b5f9c744ca612bed3d6d

 {
   "DirectoryId":"d-926example",
   "Name":"ad.example.com"
 }
```

### Example Response
<a name="API_CreateSnapshot_Example_2"></a>

This example illustrates one usage of CreateSnapshot.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 9eedb7ba-c18c-11e6-a099-03078e35561b
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Tue, 13 Dec 2016 23:33:58 GMT

{  
   "SnapshotId":"s-9267f8d3f0"
}
```

## See Also
<a name="API_CreateSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/CreateSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CreateSnapshot) 