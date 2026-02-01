# ListProvisioningArtifacts

Lists all provisioning artifacts (also known as versions) for the specified product.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "ProductId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListProvisioningArtifacts_RequestSyntax "#API_ListProvisioningArtifacts_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[ProductId](#API_ListProvisioningArtifacts_RequestSyntax "#API_ListProvisioningArtifacts_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "ProvisioningArtifactDetails": [
      {
         "Active": ***boolean***,
         "CreatedTime": ***number***,
         "Description": "***string***",
         "Guidance": "***string***",
         "Id": "***string***",
         "Name": "***string***",
         "SourceRevision": "***string***",
         "Type": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ListProvisioningArtifacts_ResponseSyntax "#API_ListProvisioningArtifacts_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProvisioningArtifactDetails](#API_ListProvisioningArtifacts_ResponseSyntax "#API_ListProvisioningArtifacts_ResponseSyntax")**

Information about the provisioning artifacts.

Type: Array of [ProvisioningArtifactDetail](API_ProvisioningArtifactDetail.md "API_ProvisioningArtifactDetail.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/cli2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/boto3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisioningArtifacts.md")
