# AssociatePrincipalWithPortfolio

Associates the specified principal ARN with the specified portfolio.

If you share the portfolio with principal name sharing enabled, the `PrincipalARN` association is
included in the share.

The `PortfolioID`, `PrincipalARN`, and `PrincipalType` parameters are
required.

You can associate a maximum of 10 Principals with a portfolio using `PrincipalType` as `IAM_PATTERN`.

###### Note

When you associate a principal with portfolio, a potential privilege escalation path may occur when that portfolio is
then shared with other accounts. For a user in a recipient account who is _not_ an Service Catalog Admin,
but still has the ability to create Principals (Users/Groups/Roles), that user could create a role that matches a principal
name association for the portfolio. Although this user may not know which principal names are associated through
Service Catalog, they may be able to guess the user. If this potential escalation path is a concern, then
Service Catalog recommends using `PrincipalType` as `IAM`. With this configuration,
the `PrincipalARN` must already exist in the recipient account before it can be associated.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "PortfolioId": "`string`",
   "PrincipalARN": "`string`",
   "PrincipalType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_AssociatePrincipalWithPortfolio_RequestSyntax "#API_AssociatePrincipalWithPortfolio_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[PortfolioId](#API_AssociatePrincipalWithPortfolio_RequestSyntax "#API_AssociatePrincipalWithPortfolio_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[PrincipalARN](#API_AssociatePrincipalWithPortfolio_RequestSyntax "#API_AssociatePrincipalWithPortfolio_RequestSyntax")**

The ARN of the principal (user, role, or group). If the `PrincipalType` is `IAM`, the supported value is a
fully defined
[IAM Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns").
If the `PrincipalType` is `IAM_PATTERN`,
the supported value is an `IAM` ARN _without an AccountID_ in the following format:

_arn:partition:iam:::resource-type/resource-id_

The ARN resource-id can be either:

- A fully formed resource-id. For example, _arn:aws:iam:::role/resource-name_ or
  _arn:aws:iam:::role/resource-path/resource-name_
- A wildcard ARN. The wildcard ARN accepts `IAM_PATTERN` values with a
  "\*" or "?" in the resource-id segment of the ARN. For example _arn:partition:service:::resource-type/resource-path/resource-name_.
  The new symbols are exclusive to the **resource-path** and **resource-name**
  and cannot replace the **resource-type** or other
  ARN values.

The ARN path and principal name allow unlimited wildcard characters.

Examples of an **acceptable** wildcard ARN:

- arn:aws:iam:::role/ResourceName\_\*
- arn:aws:iam:::role/\*/ResourceName\_?

Examples of an **unacceptable** wildcard ARN:

- arn:aws:iam:::\*/ResourceName

You can associate multiple `IAM_PATTERN`s even if the account has no principal
with that name.

The "?" wildcard character matches zero or one of any character. This is similar to ".?" in regular
regex context. The "\*" wildcard character matches any number of any characters.
This is similar to ".\*" in regular regex context.

In the IAM Principal ARN format (_arn:partition:iam:::resource-type/resource-path/resource-name_),
valid resource-type values include **user/**, **group/**,
or **role/**. The "?" and "\*" characters
are allowed only after the resource-type in the resource-id segment.
You can use special characters anywhere within the resource-id.

The "\*" character also matches the "/" character, allowing paths to be formed _within_ the
resource-id. For example, _arn:aws:iam:::role/**\***/ResourceName\_?_
matches both _arn:aws:iam:::role/pathA/pathB/ResourceName_1_
and
_arn:aws:iam:::role/pathA/ResourceName_1_.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: Yes

**[PrincipalType](#API_AssociatePrincipalWithPortfolio_RequestSyntax "#API_AssociatePrincipalWithPortfolio_RequestSyntax")**

The principal type. The supported value is `IAM` if you use a fully defined Amazon Resource Name
(ARN), or `IAM_PATTERN` if you use an ARN with no `accountID`,
with or without wildcard characters.

Type: String

Valid Values: `IAM | IAM_PATTERN`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/cli2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/boto3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociatePrincipalWithPortfolio.md")
