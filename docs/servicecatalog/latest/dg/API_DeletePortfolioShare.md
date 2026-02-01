# DeletePortfolioShare

Stops sharing the specified portfolio with the specified account or organization
node. Shares to an organization node can only be deleted by the management account of an
organization or by a delegated administrator.

Note that if a delegated admin is de-registered, portfolio shares created from that account are removed.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "AccountId": "`string`",
   "OrganizationNode": {
      "Type": "`string`",
      "Value": "`string`"
   },
   "PortfolioId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DeletePortfolioShare_RequestSyntax "#API_DeletePortfolioShare_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AccountId](#API_DeletePortfolioShare_RequestSyntax "#API_DeletePortfolioShare_RequestSyntax")**

The AWS account ID.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**[OrganizationNode](#API_DeletePortfolioShare_RequestSyntax "#API_DeletePortfolioShare_RequestSyntax")**

The organization node to whom you are going to stop sharing.

Type: [OrganizationNode](API_OrganizationNode.md "API_OrganizationNode.md") object

Required: No

**[PortfolioId](#API_DeletePortfolioShare_RequestSyntax "#API_DeletePortfolioShare_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "PortfolioShareToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PortfolioShareToken](#API_DeletePortfolioShare_ResponseSyntax "#API_DeletePortfolioShare_ResponseSyntax")**

The portfolio share unique identifier. This will only be returned if delete is made to an organization node.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**InvalidStateException**

An attempt was made to modify a resource that is in a state that is not valid.
Check your resources to ensure that they are in valid states before retrying the operation.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/cli2/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/boto3/servicecatalog-2015-12-10/DeletePortfolioShare.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeletePortfolioShare.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeletePortfolioShare.md")
