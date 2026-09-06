

# DeleteSnapshot
<a name="API_DeleteSnapshot"></a>

Deletes a directory snapshot.

## Request Syntax
<a name="API_DeleteSnapshot_RequestSyntax"></a>

```
{
   "SnapshotId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteSnapshot_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [SnapshotId](#API_DeleteSnapshot_RequestSyntax) **   <a name="DirectoryService-DeleteSnapshot-request-SnapshotId"></a>
The identifier of the directory snapshot to be deleted.  
Type: String  
Pattern: `^s-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DeleteSnapshot_ResponseSyntax"></a>

```
{
   "SnapshotId": "string"
}
```

## Response Elements
<a name="API_DeleteSnapshot_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [SnapshotId](#API_DeleteSnapshot_ResponseSyntax) **   <a name="DirectoryService-DeleteSnapshot-response-SnapshotId"></a>
The identifier of the directory snapshot that was deleted.  
Type: String  
Pattern: `^s-[0-9a-f]{10}$` 

## Errors
<a name="API_DeleteSnapshot_Errors"></a>

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

## Examples
<a name="API_DeleteSnapshot_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DeleteSnapshot_Example_1"></a>

This example illustrates one usage of DeleteSnapshot.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 30
X-Amz-Target: DirectoryService_20150416.DeleteSnapshot
X-Amz-Date: 20161214T012131Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=685c5716e7e11b8d5b2ed5f413d6ff47fe179a1f215b83aa89d00d3b28827c1c

 {
   "SnapshotId": "s-9267f8d3f0"
 }
```

### Example Response
<a name="API_DeleteSnapshot_Example_2"></a>

This example illustrates one usage of DeleteSnapshot.

```
HTTP/1.1 200 OK
x-amzn-RequestId: a68a1e79-c19b-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Wed, 14 Dec 2016 01:21:34 GMT

{  
   "SnapshotId":"s-9267f8d3f0"
}
```

## See Also
<a name="API_DeleteSnapshot_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DeleteSnapshot) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DeleteSnapshot) 