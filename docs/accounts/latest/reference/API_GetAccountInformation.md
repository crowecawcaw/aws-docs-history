# GetAccountInformation

Retrieves information about the specified account including its account name, account
ID, and account creation date and time. To use this API, an IAM user or role must have
the `account:GetAccountInformation` IAM permission.

## Request Syntax

```
POST /getAccountInformation HTTP/1.1
Content-type: application/json

{
   "AccountId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[AccountId](#API_GetAccountInformation_RequestSyntax "#API_GetAccountInformation_RequestSyntax")**

Specifies the 12 digit account ID number of the AWS account that
you want to access or modify with this operation.

If you do not specify this parameter, it defaults to the AWS account of the
identity used to call the operation.

To use this parameter, the caller must be an identity in the [organization's management account](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account") or a delegated administrator account, and
the specified account ID must be a member account in the same organization. The
organization must have [all features
enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"), and the organization must have [trusted access](../../../organizations/latest/userguide/services-that-can-integrate-account.md "../../../organizations/latest/userguide/services-that-can-integrate-account.md") enabled for the
Account Management service, and optionally a [delegated
administrator](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin") account
assigned.

###### Note

The management account can't specify its own `AccountId`; it must call
the operation in standalone context by not including the `AccountId`
parameter.

To call this operation on an account that is not a member of an organization, then
don't specify this parameter, and call the operation using an identity belonging to
the account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "AccountCreatedDate": "***string***",
   "AccountId": "***string***",
   "AccountName": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AccountCreatedDate](#API_GetAccountInformation_ResponseSyntax "#API_GetAccountInformation_ResponseSyntax")**

The date and time the account was created.

Type: Timestamp

**[AccountId](#API_GetAccountInformation_ResponseSyntax "#API_GetAccountInformation_ResponseSyntax")**

Specifies the 12-digit account ID number of the AWS account that you want to access
or modify with this operation. To use this parameter, the caller must be an identity in
the [organization's
management account](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account") or a delegated administrator account. The specified
account ID must be a member account in the same organization. The organization must have
[all features
enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"), and the organization must have [trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") enabled for
the Account Management service, and optionally a [delegated
admin](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin") account assigned.

This operation can only be called from the management account or the delegated
administrator account of an organization for a member account.

###### Note

The management account can't specify its own `AccountId`.

Type: String

Pattern: `\d{12}`

**[AccountName](#API_GetAccountInformation_ResponseSyntax "#API_GetAccountInformation_ResponseSyntax")**

The name of the account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[ -;=?-~]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

The operation failed because the calling identity doesn't have the minimum required
permissions.

**errorType**

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 403

**InternalServerException**

The operation failed because of an error internal to AWS. Try your operation again
later.

**errorType**

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 500

**TooManyRequestsException**

The operation failed because it was called too frequently and exceeded a throttle
limit.

**errorType**

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 429

**ValidationException**

The operation failed because one of the input parameters was invalid.

**fieldList**

The field where the invalid entry was detected.

**message**

The message that informs you about what was invalid about the request.

**reason**

The reason that validation failed.

HTTP Status Code: 400

## Examples

### Example 1

The following example retrieves the account information for the account whose
credentials are used to call the operation.

#### Sample Request

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.GetAccountInformation

{}
```

#### Sample Response

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "AccountId": "123456789012",
   "AccountName": "MyAccount",
   "AccountCreatedDate": "2020-11-30T17:44:37Z"
}
```

### Example 2

The following example retrieves the account information for the specified
member account in an organization. You must use credentials from either the
organization's management account or from the Account Management service's delegated admin
account.

#### Sample Request

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.GetAccountInformation

{
   "AccountId": "123456789012"
}
```

#### Sample Response

```
HTTP/1.1 200 OK
Content-Type: application/json

{
   "AccountId": "123456789012",
   "AccountName": "MyMemberAccount",
   "AccountCreatedDate": "2020-11-30T17:44:37Z"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/account-2021-02-01/GetAccountInformation.md "../../../goto/cli2/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/account-2021-02-01/GetAccountInformation.md "../../../goto/DotNetSDKV4/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForCpp/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForGoV2/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForJavaV2/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForJavaScriptV3/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForKotlin/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForPHPV3/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for Python](../../../goto/boto3/account-2021-02-01/GetAccountInformation.md "../../../goto/boto3/account-2021-02-01/GetAccountInformation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/GetAccountInformation.md "../../../goto/SdkForRubyV3/account-2021-02-01/GetAccountInformation.md")
