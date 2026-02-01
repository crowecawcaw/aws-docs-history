# DescribeProvisioningParameters

Gets information about the configuration required to provision the specified product using
the specified provisioning artifact.

If the output contains a TagOption key with an empty list of values, there is a
TagOption conflict for that key. The end user cannot take action to fix the conflict, and
launch is not blocked. In subsequent calls to [ProvisionProduct](API_ProvisionProduct.md "API_ProvisionProduct.md"),
do not include conflicted TagOption keys as tags, or this causes the error
"Parameter validation failed: Missing required parameter in Tags[*N*]:_Value_".
Tag the provisioned product with the value `sc-tagoption-conflict-portfolioId-productId`.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PathId": "`string`",
   "PathName": "`string`",
   "ProductId": "`string`",
   "ProductName": "`string`",
   "ProvisioningArtifactId": "`string`",
   "ProvisioningArtifactName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PathId](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The path identifier of the product. This value is optional if the product
has a default path, and required if the product has more than one path.
To list the paths for a product, use [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md"). You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[PathName](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The name of the path. You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**[ProductId](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The product identifier. You must provide the product name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProductName](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The name of the product. You must provide the name or ID, but not both.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[ProvisioningArtifactId](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The identifier of the provisioning artifact. You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProvisioningArtifactName](#API_DescribeProvisioningParameters_RequestSyntax "#API_DescribeProvisioningParameters_RequestSyntax")**

The name of the provisioning artifact. You must provide the name or ID, but not both.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

## Response Syntax

```
{
   "ConstraintSummaries": [
      {
         "Description": "***string***",
         "Type": "***string***"
      }
   ],
   "ProvisioningArtifactOutputKeys": [
      {
         "Description": "***string***",
         "Key": "***string***"
      }
   ],
   "ProvisioningArtifactOutputs": [
      {
         "Description": "***string***",
         "Key": "***string***"
      }
   ],
   "ProvisioningArtifactParameters": [
      {
         "DefaultValue": "***string***",
         "Description": "***string***",
         "IsNoEcho": ***boolean***,
         "ParameterConstraints": {
            "AllowedPattern": "***string***",
            "AllowedValues": [ "***string***" ],
            "ConstraintDescription": "***string***",
            "MaxLength": "***string***",
            "MaxValue": "***string***",
            "MinLength": "***string***",
            "MinValue": "***string***"
         },
         "ParameterKey": "***string***",
         "ParameterType": "***string***"
      }
   ],
   "ProvisioningArtifactPreferences": {
      "StackSetAccounts": [ "***string***" ],
      "StackSetRegions": [ "***string***" ]
   },
   "TagOptions": [
      {
         "Key": "***string***",
         "Values": [ "***string***" ]
      }
   ],
   "UsageInstructions": [
      {
         "Type": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ConstraintSummaries](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

Information about the constraints used to provision the product.

Type: Array of [ConstraintSummary](API_ConstraintSummary.md "API_ConstraintSummary.md") objects

**[ProvisioningArtifactOutputKeys](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

A list of the keys and descriptions of the outputs. These outputs can be referenced from a provisioned product launched from this provisioning artifact.

Type: Array of [ProvisioningArtifactOutput](API_ProvisioningArtifactOutput.md "API_ProvisioningArtifactOutput.md") objects

Array Members: Maximum number of 60 items.

**[ProvisioningArtifactOutputs](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

_This parameter has been deprecated._

The output of the provisioning artifact.

Type: Array of [ProvisioningArtifactOutput](API_ProvisioningArtifactOutput.md "API_ProvisioningArtifactOutput.md") objects

Array Members: Maximum number of 60 items.

**[ProvisioningArtifactParameters](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

Information about the parameters used to provision the product.

Type: Array of [ProvisioningArtifactParameter](API_ProvisioningArtifactParameter.md "API_ProvisioningArtifactParameter.md") objects

**[ProvisioningArtifactPreferences](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

An object that contains information about preferences, such as Regions and accounts, for the provisioning artifact.

Type: [ProvisioningArtifactPreferences](API_ProvisioningArtifactPreferences.md "API_ProvisioningArtifactPreferences.md") object

**[TagOptions](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

Information about the TagOptions associated with the resource.

Type: Array of [TagOptionSummary](API_TagOptionSummary.md "API_TagOptionSummary.md") objects

**[UsageInstructions](#API_DescribeProvisioningParameters_ResponseSyntax "#API_DescribeProvisioningParameters_ResponseSyntax")**

Any additional metadata specifically related to the provisioning of the product. For
example, see the `Version` field of the AWS CloudFormation template.

Type: Array of [UsageInstruction](API_UsageInstruction.md "API_UsageInstruction.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisioningParameters.md")
