# AddIpRoutes

If the DNS server for your self-managed domain uses a publicly addressable IP address,
you must add a CIDR address block to correctly route traffic to and from your Microsoft AD
on Amazon Web Services. _AddIpRoutes_ adds this address block. You can
also use _AddIpRoutes_ to facilitate routing traffic that uses public IP
ranges from your Microsoft AD on AWS to a peer VPC.

Before you call _AddIpRoutes_, ensure that all of the required
permissions have been explicitly granted through a policy. For details about what
permissions are required to run the _AddIpRoutes_ operation, see [AWS Directory Service API Permissions: Actions, Resources, and Conditions Reference](../admin-guide/UsingWithDS_IAM_ResourcePermissions.md "../admin-guide/UsingWithDS_IAM_ResourcePermissions.md").

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "IpRoutes": [
      {
         "CidrIp": "`string`",
         "CidrIpv6": "`string`",
         "Description": "`string`"
      }
   ],
   "UpdateSecurityGroupForDirectoryControllers": `boolean`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_AddIpRoutes_RequestSyntax "#API_AddIpRoutes_RequestSyntax")**

Identifier (ID) of the directory to which to add the address block.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[IpRoutes](#API_AddIpRoutes_RequestSyntax "#API_AddIpRoutes_RequestSyntax")**

IP address blocks, using CIDR format, of the traffic to route. This is often the IP
address block of the DNS server used for your self-managed domain.

Type: Array of [IpRoute](API_IpRoute.md "API_IpRoute.md") objects

Required: Yes

**[UpdateSecurityGroupForDirectoryControllers](#API_AddIpRoutes_RequestSyntax "#API_AddIpRoutes_RequestSyntax")**

If set to true, updates the inbound and outbound rules of the security group that has
the description: "AWS created security group for _directory ID_
directory controllers." Following are the new rules:

Inbound:

- Type: Custom UDP Rule, Protocol: UDP, Range: 88, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom UDP Rule, Protocol: UDP, Range: 123, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom UDP Rule, Protocol: UDP, Range: 138, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom UDP Rule, Protocol: UDP, Range: 389, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom UDP Rule, Protocol: UDP, Range: 464, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom UDP Rule, Protocol: UDP, Range: 445, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 88, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 135, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 445, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 464, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 636, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 1024-65535, Source: AWS Managed Microsoft AD VPC
  IPv4 CIDR
- Type: Custom TCP Rule, Protocol: TCP, Range: 3268-33269, Source: AWS Managed Microsoft AD VPC
  IPv4 CIDR
- Type: DNS (UDP), Protocol: UDP, Range: 53, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: DNS (TCP), Protocol: TCP, Range: 53, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR
- Type: LDAP, Protocol: TCP, Range: 389, Source: AWS Managed Microsoft AD VPC IPv4 CIDR
- Type: All ICMP, Protocol: All, Range: N/A, Source: AWS Managed Microsoft AD VPC IPv4
  CIDR

Outbound:

- Type: All traffic, Protocol: All, Range: All, Destination: 0.0.0.0/0

These security rules impact an internal network interface that is not exposed
publicly.

Type: Boolean

Required: No

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryUnavailableException**

The specified directory is unavailable.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityAlreadyExistsException**

The specified entity already exists.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**IpRouteLimitExceededException**

The maximum allowed number of IP addresses was exceeded. The default limit is 100 IP
address blocks.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## Examples

The following examples are formatted for legibility.

### Example Request

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

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/AddIpRoutes.md "../../../goto/cli2/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/AddIpRoutes.md "../../../goto/DotNetSDKV3/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForCpp/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForGoV2/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForKotlin/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForPHPV3/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/AddIpRoutes.md "../../../goto/boto3/ds-2015-04-16/AddIpRoutes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AddIpRoutes.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AddIpRoutes.md")
