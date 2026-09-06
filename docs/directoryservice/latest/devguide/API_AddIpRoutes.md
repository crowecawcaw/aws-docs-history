

# AddIpRoutes
<a name="API_AddIpRoutes"></a>

If the DNS server for your self-managed domain uses a publicly addressable IP address, you must add a CIDR address block to correctly route traffic to and from your Microsoft AD on Amazon Web Services. *AddIpRoutes* adds this address block. You can also use *AddIpRoutes* to facilitate routing traffic that uses public IP ranges from your Microsoft AD on AWS to a peer VPC. 

Before you call *AddIpRoutes*, ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the *AddIpRoutes* operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html).

## Request Syntax
<a name="API_AddIpRoutes_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "IpRoutes": [ 
      { 
         "CidrIp": "{{string}}",
         "CidrIpv6": "{{string}}",
         "Description": "{{string}}"
      }
   ],
   "UpdateSecurityGroupForDirectoryControllers": {{boolean}}
}
```

## Request Parameters
<a name="API_AddIpRoutes_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_AddIpRoutes_RequestSyntax) **   <a name="DirectoryService-AddIpRoutes-request-DirectoryId"></a>
Identifier (ID) of the directory to which to add the address block.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [IpRoutes](#API_AddIpRoutes_RequestSyntax) **   <a name="DirectoryService-AddIpRoutes-request-IpRoutes"></a>
IP address blocks, using CIDR format, of the traffic to route. This is often the IP address block of the DNS server used for your self-managed domain.  
Type: Array of [IpRoute](API_IpRoute.md) objects  
Required: Yes

 ** [UpdateSecurityGroupForDirectoryControllers](#API_AddIpRoutes_RequestSyntax) **   <a name="DirectoryService-AddIpRoutes-request-UpdateSecurityGroupForDirectoryControllers"></a>
If set to true, updates the inbound and outbound rules of the security group that has the description: "AWS created security group for *directory ID* directory controllers." Following are the new rules:   
Inbound:  
+ Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: DNS (UDP), Protocol: UDP, Range: 53, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: DNS (TCP), Protocol: TCP, Range: 53, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: LDAP, Protocol: TCP, Range: 389, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
+ Type: All ICMP, Protocol: All, Range: N/A, Source: AWS Managed Microsoft AD VPC IPv4 CIDR, or IPv6 CIDR
  
Outbound:  
+ Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0 or ::/0 if directory supports IPv6
These security rules impact an internal network interface that is not exposed publicly.  
Type: Boolean  
Required: No

## Response Elements
<a name="API_AddIpRoutes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AddIpRoutes_Errors"></a>

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

 ** IpRouteLimitExceededException **   
The maximum allowed number of IP addresses was exceeded. The default limit is 100 IP address blocks.    
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
<a name="API_AddIpRoutes_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_AddIpRoutes_Example_1"></a>

This example illustrates one usage of AddIpRoutes.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 98
X-Amz-Target: DirectoryService_20150416.AddIpRoutes
X-Amz-Date: 20161212T212029Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=477f3a2802dcc303f69499723eb2e29a455fe3d1b646df0dacfd7c005a3a9509

 {
   "DirectoryId":"d-926example",
   "IpRoutes":[
      {
         "Description":"my IpRoute",
         "CidrIp":"12.12.12.12/32"
      }
   ]
 }
```

### Example Response
<a name="API_AddIpRoutes_Example_2"></a>

This example illustrates one usage of AddIpRoutes.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Dec 2016 21:20:31 GMT

 {
 }
```

## See Also
<a name="API_AddIpRoutes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/AddIpRoutes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/AddIpRoutes) 