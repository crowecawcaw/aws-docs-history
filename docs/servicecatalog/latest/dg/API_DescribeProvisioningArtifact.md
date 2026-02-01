# DescribeProvisioningArtifact

Gets information about the specified provisioning artifact (also known as a version) for the specified product.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IncludeProvisioningArtifactParameters": `boolean`,
   "ProductId": "`string`",
   "ProductName": "`string`",
   "ProvisioningArtifactId": "`string`",
   "ProvisioningArtifactName": "`string`",
   "Verbose": `boolean`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IncludeProvisioningArtifactParameters](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

Indicates if the API call response does or does not include additional details about the provisioning parameters.

Type: Boolean

Required: No

**[ProductId](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProductName](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

The product name.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[ProvisioningArtifactId](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProvisioningArtifactName](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

The provisioning artifact name.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**[Verbose](#API_DescribeProvisioningArtifact_RequestSyntax "#API_DescribeProvisioningArtifact_RequestSyntax")**

Indicates whether a verbose level of detail is enabled.

Type: Boolean

Required: No

## Response Syntax

```
{
   "Info": {
      "***string***" : "***string***"
   },
   "ProvisioningArtifactDetail": {
      "Active": ***boolean***,
      "CreatedTime": ***number***,
      "Description": "***string***",
      "Guidance": "***string***",
      "Id": "***string***",
      "Name": "***string***",
      "SourceRevision": "***string***",
      "Type": "***string***"
   },
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
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Info](#API_DescribeProvisioningArtifact_ResponseSyntax "#API_DescribeProvisioningArtifact_ResponseSyntax")**

The URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.

Type: String to string map

Map Entries: Maximum number of 100 items.

**[ProvisioningArtifactDetail](#API_DescribeProvisioningArtifact_ResponseSyntax "#API_DescribeProvisioningArtifact_ResponseSyntax")**

Information about the provisioning artifact.

Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md "API_ProvisioningArtifactDetail.md") object

**[ProvisioningArtifactParameters](#API_DescribeProvisioningArtifact_ResponseSyntax "#API_DescribeProvisioningArtifact_ResponseSyntax")**

Information about the parameters used to provision the product.

Type: Array of [ProvisioningArtifactParameter](API_ProvisioningArtifactParameter.md "API_ProvisioningArtifactParameter.md") objects

**[Status](#API_DescribeProvisioningArtifact_ResponseSyntax "#API_DescribeProvisioningArtifact_ResponseSyntax")**

The status of the current request.

Type: String

Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeProvisioningArtifact.md")
