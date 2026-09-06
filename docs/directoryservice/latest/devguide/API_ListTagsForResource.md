

# ListTagsForResource
<a name="API_ListTagsForResource"></a>

Lists all tags on a directory.

## Request Syntax
<a name="API_ListTagsForResource_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "ResourceId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTagsForResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_ListTagsForResource_RequestSyntax) **   <a name="DirectoryService-ListTagsForResource-request-Limit"></a>
Reserved for future use.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_ListTagsForResource_RequestSyntax) **   <a name="DirectoryService-ListTagsForResource-request-NextToken"></a>
Reserved for future use.  
Type: String  
Required: No

 ** [ResourceId](#API_ListTagsForResource_RequestSyntax) **   <a name="DirectoryService-ListTagsForResource-request-ResourceId"></a>
Identifier (ID) of the directory for which you want to retrieve tags.  
Type: String  
Pattern: `^[d]-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_ListTagsForResource_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Tags": [ 
      { 
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListTagsForResource_ResponseSyntax) **   <a name="DirectoryService-ListTagsForResource-response-NextToken"></a>
Reserved for future use.  
Type: String

 ** [Tags](#API_ListTagsForResource_ResponseSyntax) **   <a name="DirectoryService-ListTagsForResource-response-Tags"></a>
List of tags returned by the ListTagsForResource operation.  
Type: Array of [Tag](API_Tag.md) objects

## Errors
<a name="API_ListTagsForResource_Errors"></a>

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

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
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
<a name="API_ListTagsForResource_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 42
X-Amz-Target: DirectoryService_20150416.ListTagsForResource
X-Amz-Date: 20161214T231352Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=72d8e8988d5a206b4e218f406544b06cb4f6fd9d8927a270317509c9861b0826

 {  
   "ResourceId":"d-926example",
   "Limit": 0
 }
```

### Example Response
<a name="API_ListTagsForResource_Example_2"></a>

This example illustrates one usage of ListTagsForResource.

```
HTTP/1.1 200 OK
x-amzn-RequestId: fb7da12c-c252-11e6-a96d-2b0686697d23
Content-Type: application/x-amz-json-1.1
Content-Length: 53
Date: Wed, 14 Dec 2016 23:13:54 GMT

{
   "Tags":[
      {
         "Key":"environment",
         "Value":"production"
      }
   ]
}
```

## See Also
<a name="API_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/ListTagsForResource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ListTagsForResource) 