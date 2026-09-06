

# CreateConditionalForwarder
<a name="API_CreateConditionalForwarder"></a>

Creates a conditional forwarder associated with your AWS directory. Conditional forwarders are required in order to set up a trust relationship with another domain. The conditional forwarder points to the trusted domain.

## Request Syntax
<a name="API_CreateConditionalForwarder_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "DnsIpAddrs": [ "{{string}}" ],
   "DnsIpv6Addrs": [ "{{string}}" ],
   "RemoteDomainName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateConditionalForwarder_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_CreateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-CreateConditionalForwarder-request-DirectoryId"></a>
The directory ID of the AWS directory for which you are creating the conditional forwarder.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [DnsIpAddrs](#API_CreateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-CreateConditionalForwarder-request-DnsIpAddrs"></a>
The IP addresses of the remote DNS server associated with RemoteDomainName.  
Type: Array of strings  
Pattern: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$`   
Required: No

 ** [DnsIpv6Addrs](#API_CreateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-CreateConditionalForwarder-request-DnsIpv6Addrs"></a>
The IPv6 addresses of the remote DNS server associated with RemoteDomainName.  
Type: Array of strings  
Pattern: `^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))$`   
Required: No

 ** [RemoteDomainName](#API_CreateConditionalForwarder_RequestSyntax) **   <a name="DirectoryService-CreateConditionalForwarder-request-RemoteDomainName"></a>
The fully qualified domain name (FQDN) of the remote domain with which you will set up a trust relationship.  
Type: String  
Length Constraints: Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`   
Required: Yes

## Response Elements
<a name="API_CreateConditionalForwarder_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateConditionalForwarder_Errors"></a>

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

 ** EntityAlreadyExistsException **   
The specified entity already exists.    
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
<a name="API_CreateConditionalForwarder_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_CreateConditionalForwarder_Example_1"></a>

This example illustrates one usage of CreateConditionalForwarder.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 105
X-Amz-Target: DirectoryService_20150416.CreateConditionalForwarder
X-Amz-Date: 20161213T215543Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161213/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=717e381f0258731fe0197c68d1f5d2a0e96825119c15a6e0dcfa2d07063c6af6

 {
   "DirectoryId":"d-926example",
   "RemoteDomainName":"sales.example.com",
   "DnsIpAddrs":[
      "172.30.21.228"
   ]
 }
```

### Example Response
<a name="API_CreateConditionalForwarder_Example_2"></a>

This example illustrates one usage of CreateConditionalForwarder.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 68e74443-c180-11e6-91f4-6dbff6648f8a
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Tue, 13 Dec 2016 22:06:34 GMT

 {

 }
```

## See Also
<a name="API_CreateConditionalForwarder_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/CreateConditionalForwarder) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/CreateConditionalForwarder) 