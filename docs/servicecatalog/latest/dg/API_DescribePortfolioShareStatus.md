# DescribePortfolioShareStatus

Gets the status of the specified portfolio share operation. This API can only be called
by the management account in the organization or by a delegated admin.

## Request Syntax

```
{
   "PortfolioShareToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[PortfolioShareToken](#API_DescribePortfolioShareStatus_RequestSyntax "#API_DescribePortfolioShareStatus_RequestSyntax")**

The token for the portfolio share operation. This token is returned either by CreatePortfolioShare or by DeletePortfolioShare.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "OrganizationNodeValue": "***string***",
   "PortfolioId": "***string***",
   "PortfolioShareToken": "***string***",
   "ShareDetails": {
      "ShareErrors": [
         {
            "Accounts": [ "***string***" ],
            "Error": "***string***",
            "Message": "***string***"
         }
      ],
      "SuccessfulShares": [ "***string***" ]
   },
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[OrganizationNodeValue](#API_DescribePortfolioShareStatus_ResponseSyntax "#API_DescribePortfolioShareStatus_ResponseSyntax")**

Organization node identifier. It can be either account id, organizational unit id or organization id.

Type: String

Pattern: `(^[0-9]{12}$)|(^arn:aws:organizations::\d{12}:organization\/o-[a-z0-9]{10,32})|(^o-[a-z0-9]{10,32}$)|(^arn:aws:organizations::\d{12}:ou\/o-[a-z0-9]{10,32}\/ou-[0-9a-z]{4,32}-[0-9a-z]{8,32}$)|(^ou-[0-9a-z]{4,32}-[a-z0-9]{8,32}$)`

**[PortfolioId](#API_DescribePortfolioShareStatus_ResponseSyntax "#API_DescribePortfolioShareStatus_ResponseSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[PortfolioShareToken](#API_DescribePortfolioShareStatus_ResponseSyntax "#API_DescribePortfolioShareStatus_ResponseSyntax")**

The token for the portfolio share operation. For example, `share-6v24abcdefghi`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[ShareDetails](#API_DescribePortfolioShareStatus_ResponseSyntax "#API_DescribePortfolioShareStatus_ResponseSyntax")**

Information about the portfolio share operation.

Type: [ShareDetails](API_ShareDetails.md "API_ShareDetails.md") object

**[Status](#API_DescribePortfolioShareStatus_ResponseSyntax "#API_DescribePortfolioShareStatus_ResponseSyntax")**

Status of the portfolio share operation.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribePortfolioShareStatus.md")
