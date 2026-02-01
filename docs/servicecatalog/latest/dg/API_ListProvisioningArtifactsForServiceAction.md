# ListProvisioningArtifactsForServiceAction

Lists all provisioning artifacts (also known as versions) for the specified self-service action.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PageSize": `number`,
   "PageToken": "`string`",
   "ServiceActionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ListProvisioningArtifactsForServiceAction_RequestSyntax "#API_ListProvisioningArtifactsForServiceAction_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PageSize](#API_ListProvisioningArtifactsForServiceAction_RequestSyntax "#API_ListProvisioningArtifactsForServiceAction_RequestSyntax")**

The maximum number of items to return with this call.

Type: Integer

Valid Range: Minimum value of 0. Maximum value of 20.

Required: No

**[PageToken](#API_ListProvisioningArtifactsForServiceAction_RequestSyntax "#API_ListProvisioningArtifactsForServiceAction_RequestSyntax")**

The page token for the next set of results. To retrieve the first set of results, use null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**[ServiceActionId](#API_ListProvisioningArtifactsForServiceAction_RequestSyntax "#API_ListProvisioningArtifactsForServiceAction_RequestSyntax")**

The self-service action identifier. For example, `act-fs7abcd89wxyz`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "NextPageToken": "***string***",
   "ProvisioningArtifactViews": [
      {
         "ProductViewSummary": {
            "Distributor": "***string***",
            "HasDefaultPath": ***boolean***,
            "Id": "***string***",
            "Name": "***string***",
            "Owner": "***string***",
            "ProductId": "***string***",
            "ShortDescription": "***string***",
            "SupportDescription": "***string***",
            "SupportEmail": "***string***",
            "SupportUrl": "***string***",
            "Type": "***string***"
         },
         "ProvisioningArtifact": {
            "CreatedTime": ***number***,
            "Description": "***string***",
            "Guidance": "***string***",
            "Id": "***string***",
            "Name": "***string***"
         }
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[NextPageToken](#API_ListProvisioningArtifactsForServiceAction_ResponseSyntax "#API_ListProvisioningArtifactsForServiceAction_ResponseSyntax")**

The page token to use to retrieve the next set of results. If there are no additional results, this value is null.

Type: String

Length Constraints: Maximum length of 2024.

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

**[ProvisioningArtifactViews](#API_ListProvisioningArtifactsForServiceAction_ResponseSyntax "#API_ListProvisioningArtifactsForServiceAction_ResponseSyntax")**

An array of objects with information about product views and provisioning artifacts.

Type: Array of [ProvisioningArtifactView](API_ProvisioningArtifactView.md "API_ProvisioningArtifactView.md") objects

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/cli2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/boto3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ListProvisioningArtifactsForServiceAction.md")
