

# ListIpRoutes
<a name="API_ListIpRoutes"></a>

Lists the address blocks that you have added to a directory.

## Request Syntax
<a name="API_ListIpRoutes_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListIpRoutes_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_ListIpRoutes_RequestSyntax) **   <a name="DirectoryService-ListIpRoutes-request-DirectoryId"></a>
Identifier (ID) of the directory for which you want to retrieve the IP addresses.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [Limit](#API_ListIpRoutes_RequestSyntax) **   <a name="DirectoryService-ListIpRoutes-request-Limit"></a>
Maximum number of items to return. If this value is zero, the maximum number of items is specified by the limitations of the operation.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_ListIpRoutes_RequestSyntax) **   <a name="DirectoryService-ListIpRoutes-request-NextToken"></a>
The *ListIpRoutes.NextToken* value from a previous call to [ListIpRoutes](#API_ListIpRoutes). Pass null if this is the first call.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListIpRoutes_ResponseSyntax"></a>

```
{
   "IpRoutesInfo": [ 
      { 
         "AddedDateTime": number,
         "CidrIp": "string",
         "CidrIpv6": "string",
         "Description": "string",
         "DirectoryId": "string",
         "IpRouteStatusMsg": "string",
         "IpRouteStatusReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListIpRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [IpRoutesInfo](#API_ListIpRoutes_ResponseSyntax) **   <a name="DirectoryService-ListIpRoutes-response-IpRoutesInfo"></a>
A list of [IpRoute](API_IpRoute.md)s.  
Type: Array of [IpRouteInfo](API_IpRouteInfo.md) objects

 ** [NextToken](#API_ListIpRoutes_ResponseSyntax) **   <a name="DirectoryService-ListIpRoutes-response-NextToken"></a>
If not null, more results are available. Pass this value for the *NextToken* parameter in a subsequent call to [ListIpRoutes](#API_ListIpRoutes) to retrieve the next set of items.  
Type: String

## Errors
<a name="API_ListIpRoutes_Errors"></a>

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
<a name="API_ListIpRoutes_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_ListIpRoutes_Example_1"></a>

This example illustrates one usage of ListIpRoutes.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 43
X-Amz-Target: DirectoryService_20150416.ListIpRoutes
X-Amz-Date: 20161214T225328Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=4dcb72aae179937790f5b061ceb1c697ac434b27891014b609671e49e52be1dd

 {
   "DirectoryId":"d-926example",
   "Limit": 0
 }
```

### Example Response
<a name="API_ListIpRoutes_Example_2"></a>

This example illustrates one usage of ListIpRoutes.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 2214ceaa-c250-11e6-a7ca-f9a52a6a0390
Content-Type: application/x-amz-json-1.1
Content-Length: 155
Date: Wed, 14 Dec 2016 22:53:30 GMT

{
   "IpRoutesInfo":[
      {
         "AddedDateTime":1.48157763163E9,
         "CidrIp":"12.12.12.12/32",
         "Description":"example",
         "DirectoryId":"d-926example",
         "IpRouteStatusMsg":"Added"
      }
   ]
}
```

## See Also
<a name="API_ListIpRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/ListIpRoutes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ListIpRoutes) 