# ListIpRoutes

Lists the address blocks that you have added to a directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ListIpRoutes_RequestSyntax "#API_ListIpRoutes_RequestSyntax")**

Identifier (ID) of the directory for which you want to retrieve the IP addresses.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[Limit](#API_ListIpRoutes_RequestSyntax "#API_ListIpRoutes_RequestSyntax")**

Maximum number of items to return. If this value is zero, the maximum number of items is
specified by the limitations of the operation.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[NextToken](#API_ListIpRoutes_RequestSyntax "#API_ListIpRoutes_RequestSyntax")**

The _ListIpRoutes.NextToken_ value from a previous call to [ListIpRoutes](API_ListIpRoutes.md "API_ListIpRoutes.md"). Pass null if this is the first call.

Type: String

Required: No

## Response Syntax

```
{
   "IpRoutesInfo": [
      {
         "AddedDateTime": ***number***,
         "CidrIp": "***string***",
         "CidrIpv6": "***string***",
         "Description": "***string***",
         "DirectoryId": "***string***",
         "IpRouteStatusMsg": "***string***",
         "IpRouteStatusReason": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[IpRoutesInfo](#API_ListIpRoutes_ResponseSyntax "#API_ListIpRoutes_ResponseSyntax")**

A list of [IpRoute](API_IpRoute.md "API_IpRoute.md")s.

Type: Array of [IpRouteInfo](API_IpRouteInfo.md "API_IpRouteInfo.md") objects

**[NextToken](#API_ListIpRoutes_ResponseSyntax "#API_ListIpRoutes_ResponseSyntax")**

If not null, more results are available. Pass this value for the
_NextToken_ parameter in a subsequent call to [ListIpRoutes](API_ListIpRoutes.md "API_ListIpRoutes.md") to retrieve the next set of items.

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

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ListIpRoutes.md "../../../goto/cli2/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/ListIpRoutes.md "../../../goto/DotNetSDKV4/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForCpp/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForGoV2/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForKotlin/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ListIpRoutes.md "../../../goto/boto3/ds-2015-04-16/ListIpRoutes.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ListIpRoutes.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ListIpRoutes.md")
