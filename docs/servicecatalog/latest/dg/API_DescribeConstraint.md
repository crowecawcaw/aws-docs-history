# DescribeConstraint

Gets information about the specified constraint.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "Id": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_DescribeConstraint_RequestSyntax "#API_DescribeConstraint_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[Id](#API_DescribeConstraint_RequestSyntax "#API_DescribeConstraint_RequestSyntax")**

The identifier of the constraint.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "ConstraintDetail": {
      "ConstraintId": "***string***",
      "Description": "***string***",
      "Owner": "***string***",
      "PortfolioId": "***string***",
      "ProductId": "***string***",
      "Type": "***string***"
   },
   "ConstraintParameters": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ConstraintDetail](#API_DescribeConstraint_ResponseSyntax "#API_DescribeConstraint_ResponseSyntax")**

Information about the constraint.

Type: [ConstraintDetail](API_ConstraintDetail.md "API_ConstraintDetail.md") object

**[ConstraintParameters](#API_DescribeConstraint_ResponseSyntax "#API_DescribeConstraint_ResponseSyntax")**

The constraint parameters.

Type: String

**[Status](#API_DescribeConstraint_ResponseSyntax "#API_DescribeConstraint_ResponseSyntax")**

The status of the current request.

Type: String

Valid Values: `AVAILABLE | CREATING | FAILED`

## Errors

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/cli2/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/boto3/servicecatalog-2015-12-10/DescribeConstraint.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeConstraint.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeConstraint.md")
