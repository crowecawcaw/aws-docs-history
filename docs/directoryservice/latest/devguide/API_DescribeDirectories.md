# DescribeDirectories

Obtains information about the directories that belong to this account.

You can retrieve information about specific directories by passing the directory
identifiers in the `DirectoryIds` parameter. Otherwise, all directories that belong
to the current account are returned.

This operation supports pagination with the use of the `NextToken` request and
response parameters. If more results are available, the
`DescribeDirectoriesResult.NextToken` member contains a token that you pass in
the next call to DescribeDirectories to retrieve the next set of
items.

You can also specify a maximum number of return results with the `Limit`
parameter.

## Request Syntax

```
{
   "DirectoryIds": [ "`string`" ],
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryIds](#API_DescribeDirectories_RequestSyntax "#API_DescribeDirectories_RequestSyntax")**

A list of identifiers of the directories for which to obtain the information. If this
member is null, all directories that belong to the current account are returned.

An empty list results in an `InvalidParameterException` being thrown.

Type: Array of strings

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**[Limit](#API_DescribeDirectories_RequestSyntax "#API_DescribeDirectories_RequestSyntax")**

The maximum number of items to return. If this value is zero, the maximum number of items
is specified by the limitations of the operation.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[NextToken](#API_DescribeDirectories_RequestSyntax "#API_DescribeDirectories_RequestSyntax")**

The `DescribeDirectoriesResult.NextToken` value from a previous call to [DescribeDirectories](API_DescribeDirectories.md "API_DescribeDirectories.md"). Pass null if this is the first call.

Type: String

Required: No

## Response Syntax

```
{
   "DirectoryDescriptions": [
      {
         "AccessUrl": "***string***",
         "Alias": "***string***",
         "ConnectSettings": {
            "AvailabilityZones": [ "***string***" ],
            "ConnectIps": [ "***string***" ],
            "ConnectIpsV6": [ "***string***" ],
            "CustomerUserName": "***string***",
            "SecurityGroupId": "***string***",
            "SubnetIds": [ "***string***" ],
            "VpcId": "***string***"
         },
         "Description": "***string***",
         "DesiredNumberOfDomainControllers": ***number***,
         "DirectoryId": "***string***",
         "DnsIpAddrs": [ "***string***" ],
         "DnsIpv6Addrs": [ "***string***" ],
         "Edition": "***string***",
         "HybridSettings": {
            "SelfManagedDnsIpAddrs": [ "***string***" ],
            "SelfManagedInstanceIds": [ "***string***" ]
         },
         "LaunchTime": ***number***,
         "Name": "***string***",
         "NetworkType": "***string***",
         "OsVersion": "***string***",
         "OwnerDirectoryDescription": {
            "AccountId": "***string***",
            "DirectoryId": "***string***",
            "DnsIpAddrs": [ "***string***" ],
            "DnsIpv6Addrs": [ "***string***" ],
            "NetworkType": "***string***",
            "RadiusSettings": {
               "AuthenticationProtocol": "***string***",
               "DisplayLabel": "***string***",
               "RadiusPort": ***number***,
               "RadiusRetries": ***number***,
               "RadiusServers": [ "***string***" ],
               "RadiusServersIpv6": [ "***string***" ],
               "RadiusTimeout": ***number***,
               "SharedSecret": "***string***",
               "UseSameUsername": ***boolean***
            },
            "RadiusStatus": "***string***",
            "VpcSettings": {
               "AvailabilityZones": [ "***string***" ],
               "SecurityGroupId": "***string***",
               "SubnetIds": [ "***string***" ],
               "VpcId": "***string***"
            }
         },
         "RadiusSettings": {
            "AuthenticationProtocol": "***string***",
            "DisplayLabel": "***string***",
            "RadiusPort": ***number***,
            "RadiusRetries": ***number***,
            "RadiusServers": [ "***string***" ],
            "RadiusServersIpv6": [ "***string***" ],
            "RadiusTimeout": ***number***,
            "SharedSecret": "***string***",
            "UseSameUsername": ***boolean***
         },
         "RadiusStatus": "***string***",
         "RegionsInfo": {
            "AdditionalRegions": [ "***string***" ],
            "PrimaryRegion": "***string***"
         },
         "ShareMethod": "***string***",
         "ShareNotes": "***string***",
         "ShareStatus": "***string***",
         "ShortName": "***string***",
         "Size": "***string***",
         "SsoEnabled": ***boolean***,
         "Stage": "***string***",
         "StageLastUpdatedDateTime": ***number***,
         "StageReason": "***string***",
         "Type": "***string***",
         "VpcSettings": {
            "AvailabilityZones": [ "***string***" ],
            "SecurityGroupId": "***string***",
            "SubnetIds": [ "***string***" ],
            "VpcId": "***string***"
         }
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DirectoryDescriptions](#API_DescribeDirectories_ResponseSyntax "#API_DescribeDirectories_ResponseSyntax")**

The list of available [DirectoryDescription](API_DirectoryDescription.md "API_DirectoryDescription.md") objects that were
retrieved.

It is possible that this list contains less than the number of items specified in the
`Limit` member of the request. This occurs if there are less than the requested
number of items left to retrieve, or if the limitations of the operation have been
exceeded.

Type: Array of [DirectoryDescription](API_DirectoryDescription.md "API_DirectoryDescription.md") objects

**[NextToken](#API_DescribeDirectories_ResponseSyntax "#API_DescribeDirectories_ResponseSyntax")**

If not null, more results are available. Pass this value for the `NextToken`
parameter in a subsequent call to [DescribeDirectories](API_DescribeDirectories.md "API_DescribeDirectories.md") to retrieve the next
set of items.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

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

**InvalidNextTokenException**

The `NextToken` value is not valid.

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

This example illustrates one usage of DescribeDirectories.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 46
X-Amz-Target: DirectoryService_20150416.DescribeDirectories
X-Amz-Date: 20161214T022424Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=4e138f2c34fe61b203c621e69264a9347db842b944df2eb88fce7e2c337eab8c

 {
   "DirectoryIds": "d-926example",
   "Limit": 0
 }
```

### Example Response

This example illustrates one usage of DescribeDirectories.

```
HTTP/1.1 200 OK
x-amzn-RequestId: 6f884e4a-c1a4-11e6-a099-03078e35561b
Content-Type: application/x-amz-json-1.1
Content-Length: 470
Date: Wed, 14 Dec 2016 02:24:27 GMT

{
   "DirectoryDescriptions":[
      {
         "AccessUrl":"myaccess.awsapps.com",
         "Alias":"myaccess",
         "DirectoryId":"d-926example",
         "DnsIpAddrs":[
            "172.30.21.228",
            "172.30.9.82"
         ],
         "LaunchTime":1.469737584772E9,
         "Name":"corp.example.com",
         "ShortName":"example",
         "SsoEnabled":true,
         "Stage":"Active",
         "StageLastUpdatedDateTime":1.46973913171E9,
         "Type":"MicrosoftAD",
         "VpcSettings":{
            "AvailabilityZones":[
               "us-west-2a",
               "us-west-2b"
            ],
            "SubnetIds":[
               "subnet-ba0146de",
               "subnet-bef46bc8"
            ],
            "VpcId":"vpc-45025421"
         }
      }
   ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeDirectories.md "../../../goto/cli2/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeDirectories.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeDirectories.md "../../../goto/boto3/ds-2015-04-16/DescribeDirectories.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDirectories.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDirectories.md")
