

# AddTagsToResource
<a name="API_AddTagsToResource"></a>

Adds or overwrites one or more tags for the specified directory. Each directory can have a maximum of 50 tags. Each tag consists of a key and optional value. Tag keys must be unique to each resource.

## Request Syntax
<a name="API_AddTagsToResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "Tags": [ 
      { 
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_AddTagsToResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_AddTagsToResource_RequestSyntax) **   <a name="DirectoryService-AddTagsToResource-request-ResourceId"></a>
Identifier (ID) for the directory to which to add the tag.  
Type: String  
Pattern: `^[d]-[0-9a-f]{10}$`   
Required: Yes

 ** [Tags](#API_AddTagsToResource_RequestSyntax) **   <a name="DirectoryService-AddTagsToResource-request-Tags"></a>
The tags to be assigned to the directory.  
Type: Array of [Tag](API_Tag.md) objects  
Required: Yes

## Response Elements
<a name="API_AddTagsToResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddTagsToResource_Errors"></a>

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

 ** TagLimitExceededException **   
The maximum allowed number of tags was exceeded.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_AddTagsToResource_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_AddTagsToResource_Example_1"></a>

This example illustrates one usage of AddTagsToResource.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 87
X-Amz-Target: DirectoryService_20150416.AddTagsToResource
X-Amz-Date: 20161212T222805Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=2756d8b256b5e6b3d74879557e4f421d21111510a78c6c3650a7a93809d533c4

 {  
   "ResourceId":"d-926example",
   "Tags":[  
      {  
         "Key":"environment",
         "Value":"production"
      }
   ]
 }
```

### Example Response
<a name="API_AddTagsToResource_Example_2"></a>

This example illustrates one usage of AddTagsToResource.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 419ff1d5-c0ba-11e6-9ed0-172b3469d361
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 22:28:07 GMT

 {
 }
```

## See Also
<a name="API_AddTagsToResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/AddTagsToResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AddTagsToResource) 