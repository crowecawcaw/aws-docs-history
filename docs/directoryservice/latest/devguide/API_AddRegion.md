# AddRegion

Adds two domain controllers in the specified Region for the specified directory.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "RegionName": "`string`",
   "VPCSettings": {
      "SubnetIds": [ "`string`" ],
      "VpcId": "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_AddRegion_RequestSyntax "#API_AddRegion_RequestSyntax")**

The identifier of the directory to which you want to add Region replication.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[RegionName](#API_AddRegion_RequestSyntax "#API_AddRegion_RequestSyntax")**

The name of the Region where you want to add domain controllers for replication. For
example, `us-east-1`.

Type: String

Length Constraints: Minimum length of 8. Maximum length of 32.

Required: Yes

**[VPCSettings](#API_AddRegion_RequestSyntax "#API_AddRegion_RequestSyntax")**

Contains VPC information for the [CreateDirectory](API_CreateDirectory.md "API_CreateDirectory.md"), [CreateMicrosoftAD](API_CreateMicrosoftAD.md "API_CreateMicrosoftAD.md"), or [CreateHybridAD](API_CreateHybridAD.md "API_CreateHybridAD.md") operation.

Type: [DirectoryVpcSettings](API_DirectoryVpcSettings.md "API_DirectoryVpcSettings.md") object

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

**DirectoryAlreadyInRegionException**

The Region you specified is the same Region where the AWS Managed Microsoft AD directory was created.
Specify a different Region and try again.

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

**DirectoryUnavailableException**

The specified directory is unavailable.

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

**RegionLimitExceededException**

You have reached the limit for maximum number of simultaneous Region replications per
directory.

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

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/AddRegion.md "../../../goto/cli2/ds-2015-04-16/AddRegion.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/AddRegion.md "../../../goto/DotNetSDKV4/ds-2015-04-16/AddRegion.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/AddRegion.md "../../../goto/SdkForCpp/ds-2015-04-16/AddRegion.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/AddRegion.md "../../../goto/SdkForGoV2/ds-2015-04-16/AddRegion.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/AddRegion.md "../../../goto/SdkForJavaV2/ds-2015-04-16/AddRegion.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AddRegion.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/AddRegion.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/AddRegion.md "../../../goto/SdkForKotlin/ds-2015-04-16/AddRegion.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/AddRegion.md "../../../goto/SdkForPHPV3/ds-2015-04-16/AddRegion.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/AddRegion.md "../../../goto/boto3/ds-2015-04-16/AddRegion.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/AddRegion.md "../../../goto/SdkForRubyV3/ds-2015-04-16/AddRegion.md")
