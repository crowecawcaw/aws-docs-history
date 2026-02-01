# UpdateProvisioningArtifact

Updates the specified provisioning artifact (also known as a version) for the specified product.

You cannot update a provisioning artifact for a product that was shared with you.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Active": `boolean`,
   "Description": "`string`",
   "Guidance": "`string`",
   "Name": "`string`",
   "ProductId": "`string`",
   "ProvisioningArtifactId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Active](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

Indicates whether the product version is active.

Inactive provisioning artifacts are invisible to end users. End users cannot launch or update a provisioned product from an inactive provisioning artifact.

Type: Boolean

Required: No

**[Description](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

The updated description of the provisioning artifact.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**[Guidance](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.

The `DEFAULT` value indicates that the product version is active.

The administrator can set the guidance to `DEPRECATED` to inform
users that the product version is deprecated. Users are able to make updates to a provisioned product
of a deprecated version but cannot launch new provisioned products using a deprecated version.

Type: String

Valid Values: `DEFAULT | DEPRECATED`

Required: No

**[Name](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

The updated name of the provisioning artifact.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**[ProductId](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisioningArtifactId](#API_UpdateProvisioningArtifact_RequestSyntax "#API_UpdateProvisioningArtifact_RequestSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

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
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Info](#API_UpdateProvisioningArtifact_ResponseSyntax "#API_UpdateProvisioningArtifact_ResponseSyntax")**

The URL of the AWS CloudFormation template in Amazon S3 or GitHub in JSON format.

Type: String to string map

Map Entries: Maximum number of 100 items.

**[ProvisioningArtifactDetail](#API_UpdateProvisioningArtifact_ResponseSyntax "#API_UpdateProvisioningArtifact_ResponseSyntax")**

Information about the provisioning artifact.

Type: [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md "API_ProvisioningArtifactDetail.md") object

**[Status](#API_UpdateProvisioningArtifact_ResponseSyntax "#API_UpdateProvisioningArtifact_ResponseSyntax")**

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisioningArtifact.md")
