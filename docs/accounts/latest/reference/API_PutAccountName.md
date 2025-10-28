# PutAccountName

Updates the account name of the specified account. To use this API, IAM principals
must have the `account:PutAccountName` IAM permission.

## Request Syntax

```
POST /putAccountName HTTP/1.1
Content-type: application/json

{
   "AccountId": "`string`",
   "AccountName": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[AccountId](#API_PutAccountName_RequestSyntax "#API_PutAccountName_RequestSyntax")**

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

**[AccountName](#API_PutAccountName_RequestSyntax "#API_PutAccountName_RequestSyntax")**

The name of the account.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 50.

Pattern: `[ -;=?-~]+`

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

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

The following example updates the name for the account whose credentials are
used to call the operation.

#### Sample Request

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.PutAccountName

{
   "AccountName":"MyAccount"
}
```

#### Sample Response

```
HTTP/1.1 200 OK
Content-Type: application/json
```

### Example 2

The following example updates the account name for the specified member
account in an organization. You must use credentials from either the
organization's management account or from the Account Management service's delegated admin
account.

#### Sample Request

```
POST / HTTP/1.1
X-Amz-Target: AWSAccountV20210201.PutAccountName

{
   "AccountId": "123456789012",
   "AccountName": "MyMemberAccount"
}
```

#### Sample Response

```
HTTP/1.1 200 OK
Content-Type: application/json
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/account-2021-02-01/PutAccountName.md "../../../goto/cli2/account-2021-02-01/PutAccountName.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/account-2021-02-01/PutAccountName.md "../../../goto/DotNetSDKV3/account-2021-02-01/PutAccountName.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/PutAccountName.md "../../../goto/SdkForCpp/account-2021-02-01/PutAccountName.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/account-2021-02-01/PutAccountName.md "../../../goto/SdkForGoV2/account-2021-02-01/PutAccountName.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/PutAccountName.md "../../../goto/SdkForJavaV2/account-2021-02-01/PutAccountName.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/account-2021-02-01/PutAccountName.md "../../../goto/SdkForJavaScriptV3/account-2021-02-01/PutAccountName.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/account-2021-02-01/PutAccountName.md "../../../goto/SdkForKotlin/account-2021-02-01/PutAccountName.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/account-2021-02-01/PutAccountName.md "../../../goto/SdkForPHPV3/account-2021-02-01/PutAccountName.md")
- [AWS SDK for Python](../../../goto/boto3/account-2021-02-01/PutAccountName.md "../../../goto/boto3/account-2021-02-01/PutAccountName.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/PutAccountName.md "../../../goto/SdkForRubyV3/account-2021-02-01/PutAccountName.md")
