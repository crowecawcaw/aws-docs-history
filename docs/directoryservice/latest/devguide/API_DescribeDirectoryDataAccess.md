

# DescribeDirectoryDataAccess
<a name="API_DescribeDirectoryDataAccess"></a>

Obtains status of directory data access enablement through the Directory Service Data API for the specified directory.

## Request Syntax
<a name="API_DescribeDirectoryDataAccess_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeDirectoryDataAccess_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeDirectoryDataAccess_RequestSyntax) **   <a name="DirectoryService-DescribeDirectoryDataAccess-request-DirectoryId"></a>
The directory identifier.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

## Response Syntax
<a name="API_DescribeDirectoryDataAccess_ResponseSyntax"></a>

```
{
   "DataAccessStatus": "string"
}
```

## Response Elements
<a name="API_DescribeDirectoryDataAccess_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DataAccessStatus](#API_DescribeDirectoryDataAccess_ResponseSyntax) **   <a name="DirectoryService-DescribeDirectoryDataAccess-response-DataAccessStatus"></a>
The current status of data access through the Directory Service Data API.  
Type: String  
Valid Values: `Disabled | Disabling | Enabled | Enabling | Failed` 

## Errors
<a name="API_DescribeDirectoryDataAccess_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
You do not have sufficient access to perform this action.    
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
<a name="API_DescribeDirectoryDataAccess_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeDirectoryDataAccess_Example_1"></a>

This example illustrates one usage of DescribeDirectoryDataAccess.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 98
X-Amz-Target: DirectoryService_20150416.DescribeDirectoryDataAccess
X-Amz-Date: 20161212T212029Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=477f3a2802dcc303f69499723eb2e29a455fe3d1b646df0dacfd7c005a3a9509

 {
   "DirectoryId":"d-926example"
 }
```

### Example Response
<a name="API_DescribeDirectoryDataAccess_Example_2"></a>

This example illustrates one usage of DescribeDirectoryDataAccess.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 21:20:31 GMT

  {
    "DataAccessStatus": "Enabled"
  }
```

## See Also
<a name="API_DescribeDirectoryDataAccess_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeDirectoryDataAccess) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeDirectoryDataAccess) 