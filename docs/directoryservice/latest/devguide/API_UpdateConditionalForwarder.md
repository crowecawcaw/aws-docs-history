

# UpdateConditionalForwarder
<a name="API_UpdateConditionalForwarder"></a>

Updates a conditional forwarder that has been set up for your AWS directory.

## Request Syntax
<a name="API_UpdateConditionalForwarder_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "DnsIpAddrs": [ "{{string}}" ],
   "DnsIpv6Addrs": [ "{{string}}" ],
   "RemoteDomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateConditionalForwarder_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_UpdateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-UpdateConditionalForwarder-request-DirectoryId"></a>
The directory ID of the AWS directory for which to update the conditional forwarder.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [DnsIpAddrs](#API_UpdateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-UpdateConditionalForwarder-request-DnsIpAddrs"></a>
The updated IP addresses of the remote DNS server associated with the conditional forwarder.  
Type: Array of strings  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** [DnsIpv6Addrs](#API_UpdateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-UpdateConditionalForwarder-request-DnsIpv6Addrs"></a>
The updated IPv6 addresses of the remote DNS server associated with the conditional forwarder.  
Type: Array of strings  
Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`   
Required: No

 ** [RemoteDomainName](#API_UpdateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-UpdateConditionalForwarder-request-RemoteDomainName"></a>
The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`   
Required: Yes

## Response Elements
<a name="API_UpdateConditionalForwarder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateConditionalForwarder_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryUnavailableException **   
The specified directory is unavailable.    
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

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_UpdateConditionalForwarder_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_UpdateConditionalForwarder_Example_1"></a>

This example illustrates one usage of UpdateConditionalForwarder.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 107
X-Amz-Target: DirectoryService_20150416.UpdateConditionalForwarder
X-Amz-Date: 20161215T183823Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161215/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=84648cead858ef1efd7db75ce248aa3e22a78139b109eec6122dc3c495b71085

 {
   "DirectoryId":"d-926example",
   "RemoteDomainName":"sales.example.com",
   "DnsIpAddrs": ["172.168.101.11"]
 }
```

### Example Response
<a name="API_UpdateConditionalForwarder_Example_2"></a>

This example illustrates one usage of UpdateConditionalForwarder.

```
HTTP/1.1 200 OK
x-amzn-RequestId: aa015a05-c2f5-11e6-b3d3-bf8f15b8b2ee
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Thu, 15 Dec 2016 18:38:27 GMT

 {

 }
```

## See Also
<a name="API_UpdateConditionalForwarder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/UpdateConditionalForwarder) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/UpdateConditionalForwarder) 