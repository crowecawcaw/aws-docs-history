# DescribeRegions

Provides information about the Regions that are configured for multi-Region
replication.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "NextToken": "`string`",
   "RegionName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_DescribeRegions_RequestSyntax "#API_DescribeRegions_RequestSyntax")**

The identifier of the directory.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[NextToken](#API_DescribeRegions_RequestSyntax "#API_DescribeRegions_RequestSyntax")**

The `DescribeRegionsResult.NextToken` value from a previous call to [DescribeRegions](API_DescribeRegions.md "API_DescribeRegions.md"). Pass null if this is the first call.

Type: String

Required: No

**[RegionName](#API_DescribeRegions_RequestSyntax "#API_DescribeRegions_RequestSyntax")**

The name of the Region. For example, `us-east-1`.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 32.

Required: No

## Response Syntax

```
{
   "NextToken": "***string***",
   "RegionsDescription": [
      {
         "DesiredNumberOfDomainControllers": ***number***,
         "DirectoryId": "***string***",
         "LastUpdatedDateTime": ***number***,
         "LaunchTime": ***number***,
         "RegionName": "***string***",
         "RegionType": "***string***",
         "Status": "***string***",
         "StatusLastUpdatedDateTime": ***number***,
         "VpcSettings": {
            "SubnetIds": [ "***string***" ],
            "VpcId": "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextToken](#API_DescribeRegions_ResponseSyntax "#API_DescribeRegions_ResponseSyntax")**

If not null, more results are available. Pass this value for the `NextToken`
parameter in a subsequent call to [DescribeRegions](API_DescribeRegions.md "API_DescribeRegions.md") to retrieve the next set
of items.

Type: String

**[RegionsDescription](#API_DescribeRegions_ResponseSyntax "#API_DescribeRegions_ResponseSyntax")**

List of Region information related to the directory for each replicated Region.

Type: Array of [RegionDescription](API_RegionDescription.md "API_RegionDescription.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeRegions.md "../../../goto/cli2/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeRegions.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeRegions.md "../../../goto/boto3/ds-2015-04-16/DescribeRegions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeRegions.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeRegions.md")
