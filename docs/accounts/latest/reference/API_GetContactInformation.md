# GetContactInformation

Retrieves the primary contact information of an AWS account.

For complete details about how to use the primary contact operations, see [Update the primary contact for your AWS account](manage-acct-update-contact-primary.md "manage-acct-update-contact-primary.md").

## Request Syntax

```
POST /getContactInformation HTTP/1.1
Content-type: application/json

{
   "AccountId": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[AccountId](#API_GetContactInformation_RequestSyntax "#API_GetContactInformation_RequestSyntax")**

Specifies the 12-digit account ID number of the AWS account that you want to access
or modify with this operation. If you don't specify this parameter, it defaults to the
Amazon Web Services account of the identity used to call the operation. To use this
parameter, the caller must be an identity in the [organization's
management account](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#account") or a delegated administrator account. The specified
account ID must be a member account in the same organization. The organization must have
[all features
enabled](../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md "../../../organizations/latest/userguide/orgs_manage_org_support-all-features.md"), and the organization must have [trusted access](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") enabled for
the Account Management service, and optionally a [delegated
admin](../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin "../../../organizations/latest/userguide/orgs_getting-started_concepts.md#delegated-admin") account assigned.

###### Note

The management account can't specify its own `AccountId`. It must call
the operation in standalone context by not including the `AccountId`
parameter.

To call this operation on an account that is not a member of an organization, don't
specify this parameter. Instead, call the operation using an identity belonging to the
account whose contacts you wish to retrieve or modify.

Type: String

Pattern: `\d{12}`

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "ContactInformation": {
      "AddressLine1": "***string***",
      "AddressLine2": "***string***",
      "AddressLine3": "***string***",
      "City": "***string***",
      "CompanyName": "***string***",
      "CountryCode": "***string***",
      "DistrictOrCounty": "***string***",
      "FullName": "***string***",
      "PhoneNumber": "***string***",
      "PostalCode": "***string***",
      "StateOrRegion": "***string***",
      "WebsiteUrl": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ContactInformation](#API_GetContactInformation_ResponseSyntax "#API_GetContactInformation_ResponseSyntax")**

Contains the details of the primary contact information associated with an
AWS account.

Type: [ContactInformation](API_ContactInformation.md "API_ContactInformation.md") object

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

**ResourceNotFoundException**

The operation failed because it specified a resource that can't be found.

**errorType**

The value populated to the `x-amzn-ErrorType` response header by API Gateway.

HTTP Status Code: 404

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/account-2021-02-01/GetContactInformation.md "../../../goto/cli2/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/account-2021-02-01/GetContactInformation.md "../../../goto/DotNetSDKV4/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForCpp/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForGoV2/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForJavaV2/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForJavaScriptV3/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForKotlin/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForPHPV3/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for Python](../../../goto/boto3/account-2021-02-01/GetContactInformation.md "../../../goto/boto3/account-2021-02-01/GetContactInformation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/account-2021-02-01/GetContactInformation.md "../../../goto/SdkForRubyV3/account-2021-02-01/GetContactInformation.md")
