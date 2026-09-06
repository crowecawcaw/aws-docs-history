

# ListSchemaExtensions
<a name="API_ListSchemaExtensions"></a>

Lists all schema extensions applied to a Microsoft AD Directory.

## Request Syntax
<a name="API_ListSchemaExtensions_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSchemaExtensions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_ListSchemaExtensions_RequestSyntax) **   <a name="DirectoryService-ListSchemaExtensions-request-DirectoryId"></a>
The identifier of the directory from which to retrieve the schema extension information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Limit](#API_ListSchemaExtensions_RequestSyntax) **   <a name="DirectoryService-ListSchemaExtensions-request-Limit"></a>
The maximum number of items to return.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_ListSchemaExtensions_RequestSyntax) **   <a name="DirectoryService-ListSchemaExtensions-request-NextToken"></a>
The `ListSchemaExtensions.NextToken` value from a previous call to `ListSchemaExtensions`. Pass null if this is the first call.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListSchemaExtensions_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SchemaExtensionsInfo": [ 
      { 
         "Description": "string",
         "DirectoryId": "string",
         "EndDateTime": number,
         "SchemaExtensionId": "string",
         "SchemaExtensionStatus": "string",
         "SchemaExtensionStatusReason": "string",
         "StartDateTime": number
      }
   ]
}
```

## Response Elements
<a name="API_ListSchemaExtensions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSchemaExtensions_ResponseSyntax) **   <a name="DirectoryService-ListSchemaExtensions-response-NextToken"></a>
If not null, more results are available. Pass this value for the `NextToken` parameter in a subsequent call to `ListSchemaExtensions` to retrieve the next set of items.  
Type: String

 ** [SchemaExtensionsInfo](#API_ListSchemaExtensions_ResponseSyntax) **   <a name="DirectoryService-ListSchemaExtensions-response-SchemaExtensionsInfo"></a>
Information about the schema extensions applied to the directory.  
Type: Array of [SchemaExtensionInfo](API_SchemaExtensionInfo.md) objects

## Errors
<a name="API_ListSchemaExtensions_Errors"></a>

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

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

## Examples
<a name="API_ListSchemaExtensions_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListSchemaExtensions_Example_1"></a>

This example illustrates one usage of ListSchemaExtensions.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 43
X-Amz-Target: DirectoryService_20150416.ListSchemaExtensions
X-Amz-Date: 20161214T230332Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=39aa3aec95444a9bf6dff7fc57d3178c9364b5d2fd560380e8fbc6eee13b3cf1

 {
   "DirectoryId": "d-926example", 
   "Limit": 0
 }
```

### Example Response
<a name="API_ListSchemaExtensions_Example_2"></a>

This example illustrates one usage of ListSchemaExtensions.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 89f9aea0-c251-11e6-b0d6-83af322c90cd
Content-Type: application/x-amz-json-1.1
Content-Length: 333
Date: Wed, 14 Dec 2016 23:03:34 GMT

{
   "SchemaExtensionsInfo":[
      {
         "Description":"example text",
         "DirectoryId":"d-926example",
         "EndDateTime":1.481586088301E9,
         "SchemaExtensionId":"e-926731d2a0",
         "SchemaExtensionStatus":"Cancelled",
         "SchemaExtensionStatusReason":"Cancellation is complete. No schema updates were applied to your directory.",
         "StartDateTime":1.481584463548E9
      }
   ]
}
```

## See Also
<a name="API_ListSchemaExtensions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/ListSchemaExtensions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ListSchemaExtensions) 