# DescribeDomainControllers

Provides information about any domain controllers in your directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "DomainControllerIds": [ "`string`" ],
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DescribeDomainControllers_RequestSyntax "#API_DescribeDomainControllers_RequestSyntax")**

Identifier of the directory for which to retrieve the domain controller
information.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[DomainControllerIds](#API_DescribeDomainControllers_RequestSyntax "#API_DescribeDomainControllers_RequestSyntax")**

A list of identifiers for the domain controllers whose information will be
provided.

Type: Array of strings

Pattern: `^dc-[0-9a-f]{10}$`

Required: No

**[Limit](#API_DescribeDomainControllers_RequestSyntax "#API_DescribeDomainControllers_RequestSyntax")**

The maximum number of items to return.

Type: Integer

Valid Range: Minimum value of 0.

Required: No

**[NextToken](#API_DescribeDomainControllers_RequestSyntax "#API_DescribeDomainControllers_RequestSyntax")**

The _DescribeDomainControllers.NextToken_ value from a previous call
to [DescribeDomainControllers](API_DescribeDomainControllers.md "API_DescribeDomainControllers.md"). Pass null if this is the first call.

Type: String

Required: No

## Response Syntax

```
{
   "DomainControllers": [
      {
         "AvailabilityZone": "***string***",
         "DirectoryId": "***string***",
         "DnsIpAddr": "***string***",
         "DnsIpv6Addr": "***string***",
         "DomainControllerId": "***string***",
         "LaunchTime": ***number***,
         "Status": "***string***",
         "StatusLastUpdatedDateTime": ***number***,
         "StatusReason": "***string***",
         "SubnetId": "***string***",
         "VpcId": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[DomainControllers](#API_DescribeDomainControllers_ResponseSyntax "#API_DescribeDomainControllers_ResponseSyntax")**

List of the [DomainController](API_DomainController.md "API_DomainController.md") objects that were retrieved.

Type: Array of [DomainController](API_DomainController.md "API_DomainController.md") objects

**[NextToken](#API_DescribeDomainControllers_ResponseSyntax "#API_DescribeDomainControllers_ResponseSyntax")**

If not null, more results are available. Pass this value for the `NextToken`
parameter in a subsequent call to [DescribeDomainControllers](API_DescribeDomainControllers.md "API_DescribeDomainControllers.md") retrieve the
next set of items.

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

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/cli2/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/boto3/ds-2015-04-16/DescribeDomainControllers.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDomainControllers.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeDomainControllers.md")
