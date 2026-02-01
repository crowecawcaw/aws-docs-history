# UpdatePortfolioShare

Updates the specified portfolio share. You can use this API to enable or disable `TagOptions` sharing
or Principal sharing for an existing portfolio share.

The portfolio share cannot be updated if the `CreatePortfolioShare` operation is `IN_PROGRESS`, as the share is not available to recipient entities.
In this case, you must wait for the portfolio share to be completed.

You must provide the `accountId` or organization node in the input, but not both.

If the portfolio is shared to both an external account and an organization node, and both shares need to be updated, you must invoke `UpdatePortfolioShare` separately for each share type.

This API cannot be used for removing the portfolio share. You must use `DeletePortfolioShare` API for that action.

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

**[AcceptLanguage](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AccountId](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

The AWS account Id of the recipient account. This field is required when updating an external account to account type share.

Type: String

Pattern: `^[0-9]{12}$`

Required: No

**[OrganizationNode](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

Information about the organization node.

Type: [OrganizationNode](API_OrganizationNode.md "API_OrganizationNode.md") object

Required: No

**[PortfolioId](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

The unique identifier of the portfolio for which the share will be updated.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[SharePrincipals](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

A flag to enables or disables `Principals` sharing in the portfolio. If this field is not provided,
the current state of the `Principals` sharing on the portfolio share will not be modified.

Type: Boolean

Required: No

**[ShareTagOptions](#API_UpdatePortfolioShare_RequestSyntax "#API_UpdatePortfolioShare_RequestSyntax")**

Enables or disables `TagOptions` sharing for the portfolio share. If this field is not provided, the current state of
TagOptions sharing on the portfolio share will not be modified.

Type: Boolean

Required: No

## Response Syntax

```
{
   "PortfolioShareToken": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PortfolioShareToken](#API_UpdatePortfolioShare_ResponseSyntax "#API_UpdatePortfolioShare_ResponseSyntax")**

The token that tracks the status of the `UpdatePortfolioShare` operation for external account to account or organizational type sharing.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[Status](#API_UpdatePortfolioShare_ResponseSyntax "#API_UpdatePortfolioShare_ResponseSyntax")**

The status of `UpdatePortfolioShare` operation.
You can also obtain the operation status using `DescribePortfolioShareStatus` API.

Type: String

Valid Values: `NOT_STARTED | IN_PROGRESS | COMPLETED | COMPLETED_WITH_ERRORS | ERROR`

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdatePortfolioShare.md")
