

# RemoveTagsFromResource
<a name="API_RemoveTagsFromResource"></a>

Removes tags from a directory.

## Request Syntax
<a name="API_RemoveTagsFromResource_RequestSyntax"></a>

```
{
   "ResourceId": "{{string}}",
   "TagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTagsFromResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceId](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="DirectoryService-RemoveTagsFromResource-request-ResourceId"></a>
Identifier (ID) of the directory from which to remove the tag.  
Type: String  
Pattern: `^[d]-[0-9a-f]{10}$`   
Required: Yes

 ** [TagKeys](#API_RemoveTagsFromResource_RequestSyntax) **   <a name="DirectoryService-RemoveTagsFromResource-request-TagKeys"></a>
The tag key (name) of the tag to be removed.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`   
Required: Yes

## Response Elements
<a name="API_RemoveTagsFromResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTagsFromResource_Errors"></a>

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
<a name="API_RemoveTagsFromResource_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_RemoveTagsFromResource_Example_1"></a>

This example illustrates one usage of RemoveTagsFromResource.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 58
X-Amz-Target: DirectoryService_20150416.RemoveTagsFromResource
X-Amz-Date: 20161214T234556Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=707f9d53696de7adc446b3bd54404571011febc29e9b76c6aed793767639bf47

 {  
   "ResourceId":"d-926example",
   "TagKeys": ["environment"]
 }
```

### Example Response
<a name="API_RemoveTagsFromResource_Example_2"></a>

This example illustrates one usage of RemoveTagsFromResource.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 767374a0-c257-11e6-ad7a-a9557d30f017
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Wed, 14 Dec 2016 23:45:58 GMT

{
   
}
```

## See Also
<a name="API_RemoveTagsFromResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/RemoveTagsFromResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/RemoveTagsFromResource) 