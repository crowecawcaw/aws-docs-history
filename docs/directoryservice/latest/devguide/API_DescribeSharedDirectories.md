

# DescribeSharedDirectories
<a name="API_DescribeSharedDirectories"></a>

Returns the shared directories in your account. 

## Request Syntax
<a name="API_DescribeSharedDirectories_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "OwnerDirectoryId": "{{string}}",
   "SharedDirectoryIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeSharedDirectories_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribeSharedDirectories_RequestSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-request-Limit"></a>
The number of shared directories to return in the response object.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_DescribeSharedDirectories_RequestSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-request-NextToken"></a>
The `DescribeSharedDirectoriesResult.NextToken` value from a previous call to [DescribeSharedDirectories](#API_DescribeSharedDirectories). Pass null if this is the first call.   
Type: String  
Required: No

 ** [OwnerDirectoryId](#API_DescribeSharedDirectories_RequestSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-request-OwnerDirectoryId"></a>
Returns the identifier of the directory in the directory owner account.   
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [SharedDirectoryIds](#API_DescribeSharedDirectories_RequestSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-request-SharedDirectoryIds"></a>
A list of identifiers of all shared directories in your account.   
Type: Array of strings  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

## Response Syntax
<a name="API_DescribeSharedDirectories_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SharedDirectories": [ 
      { 
         "CreatedDateTime": number,
         "LastUpdatedDateTime": number,
         "OwnerAccountId": "string",
         "OwnerDirectoryId": "string",
         "SharedAccountId": "string",
         "SharedDirectoryId": "string",
         "ShareMethod": "string",
         "ShareNotes": "string",
         "ShareStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeSharedDirectories_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeSharedDirectories_ResponseSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-response-NextToken"></a>
If not null, token that indicates that more results are available. Pass this value for the `NextToken` parameter in a subsequent call to [DescribeSharedDirectories](#API_DescribeSharedDirectories) to retrieve the next set of items.  
Type: String

 ** [SharedDirectories](#API_DescribeSharedDirectories_ResponseSyntax) **   <a name="DirectoryService-DescribeSharedDirectories-response-SharedDirectories"></a>
A list of all shared directories in your account.  
Type: Array of [SharedDirectory](API_SharedDirectory.md) objects

## Errors
<a name="API_DescribeSharedDirectories_Errors"></a>

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

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## See Also
<a name="API_DescribeSharedDirectories_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeSharedDirectories) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeSharedDirectories) 