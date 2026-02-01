# CreatePortfolioShare

Shares the specified portfolio with the specified account or organization node.
Shares to an organization node can only be created by the management account of an
organization or by a delegated administrator. You can share portfolios to an organization,
an organizational unit, or a specific account.

Note that if a delegated admin is de-registered, they can no longer create portfolio shares.

`AWSOrganizationsAccess` must be enabled in order to create a portfolio share to an organization node.

You can't share a shared resource, including portfolios that contain a shared product.

If the portfolio share with the specified account or organization node already exists, this action will have no effect
and will not return an error. To update an existing share, you must use the `UpdatePortfolioShare` API instead.

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
   "AccountId": "`string`",
   "OrganizationNode": {
      "Type": "`string`",
      "Value": "`string`"
   },
   "PortfolioId": "`string`",
   "SharePrincipals": `boolean`,
   "ShareTagOptions": `boolean`
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AccountId](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

The AWS account ID. For example, `123456789012`.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**[OrganizationNode](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

The organization node to whom you are going to share. When you pass `OrganizationNode`, it creates `PortfolioShare` for all of the AWS accounts that are associated to the `OrganizationNode`.
The output returns a `PortfolioShareToken`, which enables the administrator to monitor the status of the `PortfolioShare` creation process.

Type: [OrganizationNode](API_OrganizationNode.md "API_OrganizationNode.md") object

Required: No

**[PortfolioId](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

The portfolio identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[SharePrincipals](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

This parameter is only supported for portfolios with an **OrganizationalNode**
Type of `ORGANIZATION` or `ORGANIZATIONAL_UNIT`.

Enables or disables `Principal` sharing when creating the portfolio share. If you do
**not** provide this flag, principal sharing is disabled.

When you enable Principal Name Sharing for a portfolio share, the share recipient
account end users with a principal that matches any of the associated IAM
patterns can provision products from the portfolio. Once
shared, the share recipient can view associations of `PrincipalType`:
`IAM_PATTERN` on their portfolio. You can create the principals in the recipient account before or
after creating the share.

Type: Boolean

Required: No

**[ShareTagOptions](#API_CreatePortfolioShare_RequestSyntax "#API_CreatePortfolioShare_RequestSyntax")**

Enables or disables `TagOptions` sharing when creating the portfolio share. If this flag is not
provided, TagOptions sharing is disabled.

Type: Boolean

Required: No

## Response Syntax

```
{
   "PortfolioShareToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PortfolioShareToken](#API_CreatePortfolioShare_ResponseSyntax "#API_CreatePortfolioShare_ResponseSyntax")**

The portfolio shares a unique identifier that only returns if the portfolio is shared to an organization node.

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

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

HTTP Status Code: 400

**OperationNotSupportedException**

The operation is not supported.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/cli2/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/boto3/servicecatalog-2015-12-10/CreatePortfolioShare.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreatePortfolioShare.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreatePortfolioShare.md")
