

# DescribeConditionalForwarders
<a name="API_DescribeConditionalForwarders"></a>

Obtains information about the conditional forwarders for this account.

If no input parameters are provided for RemoteDomainNames, this request describes all conditional forwarders for the specified directory ID.

## Request Syntax
<a name="API_DescribeConditionalForwarders_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "RemoteDomainNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeConditionalForwarders_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeConditionalForwarders_RequestSyntax) **   <a name="DirectoryService-DescribeConditionalForwarders-request-DirectoryId"></a>
The directory ID for which to get the list of associated conditional forwarders.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [RemoteDomainNames](#API_DescribeConditionalForwarders_RequestSyntax) **   <a name="DirectoryService-DescribeConditionalForwarders-request-RemoteDomainNames"></a>
The fully qualified domain names (FQDN) of the remote domains for which to get the list of associated conditional forwarders. If this member is null, all conditional forwarders are returned.  
Type: Array of strings  
Length Constraints: Maximum length of 1024.  
Pattern: `^([a-zA-Z0-9]+[\\.-])+([a-zA-Z0-9])+[.]?$`   
Required: No

## Response Syntax
<a name="API_DescribeConditionalForwarders_ResponseSyntax"></a>

```
{
   "ConditionalForwarders": [ 
      { 
         "DnsIpAddrs": [ "string" ],
         "DnsIpv6Addrs": [ "string" ],
         "RemoteDomainName": "string",
         "ReplicationScope": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeConditionalForwarders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConditionalForwarders](#API_DescribeConditionalForwarders_ResponseSyntax) **   <a name="DirectoryService-DescribeConditionalForwarders-response-ConditionalForwarders"></a>
The list of conditional forwarders that have been created.  
Type: Array of [ConditionalForwarder](API_ConditionalForwarder.md) objects

## Errors
<a name="API_DescribeConditionalForwarders_Errors"></a>

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
<a name="API_DescribeConditionalForwarders_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeConditionalForwarders_Example_1"></a>

This example illustrates one usage of DescribeConditionalForwarders.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 79
X-Amz-Target: DirectoryService_20150416.DescribeConditionalForwarders
X-Amz-Date: 20161214T020215Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=d8f7ff4237b393b4734bbf5d96713dff3deff651b4ab348f64bd776606147f9d

 {
   "DirectoryId": "d-926example",
   "RemoteDomainNames": ["sales.example.com"]
 }
```

### Example Response
<a name="API_DescribeConditionalForwarders_Example_2"></a>

This example illustrates one usage of DescribeConditionalForwarders.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 56d08425-c1a1-11e6-a132-e5016ac609f4
Content-Type: application/x-amz-json-1.1
Content-Length: 28
Date: Wed, 14 Dec 2016 02:02:18 GMT

{
    "ConditionalForwarders": [
        {
            "RemoteDomainName": "sales.example.com",
            "DnsIpAddrs": [
                "172.30.21.228"
            ],
            "ReplicationScope": "Domain"
        }
    ]
}
```

## See Also
<a name="API_DescribeConditionalForwarders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeConditionalForwarders) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeConditionalForwarders) 