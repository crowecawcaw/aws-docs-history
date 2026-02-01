# UpdateProvisionedProductProperties

Requests updates to the properties of the specified provisioned product.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IdempotencyToken": "`string`",
   "ProvisionedProductId": "`string`",
   "ProvisionedProductProperties": {
      "`string`" : "`string`"
   }
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_UpdateProvisionedProductProperties_RequestSyntax "#API_UpdateProvisionedProductProperties_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IdempotencyToken](#API_UpdateProvisionedProductProperties_RequestSyntax "#API_UpdateProvisionedProductProperties_RequestSyntax")**

The idempotency token that uniquely identifies the provisioning product update request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[ProvisionedProductId](#API_UpdateProvisionedProductProperties_RequestSyntax "#API_UpdateProvisionedProductProperties_RequestSyntax")**

The identifier of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisionedProductProperties](#API_UpdateProvisionedProductProperties_RequestSyntax "#API_UpdateProvisionedProductProperties_RequestSyntax")**

A map that contains the provisioned product properties to be updated.

The `LAUNCH_ROLE` key accepts role ARNs. This key allows an
administrator to call `UpdateProvisionedProductProperties` to update the launch
role that is associated with a provisioned product. This role is used when an end user
calls a provisioning operation such as `UpdateProvisionedProduct`,
`TerminateProvisionedProduct`, or
`ExecuteProvisionedProductServiceAction`. Only a role ARN is valid. A user ARN is invalid.

The `OWNER` key accepts user ARNs, IAM role ARNs, and STS
assumed-role ARNs. The owner is the user that has permission to see, update, terminate, and
execute service actions in the provisioned product.

The administrator can change the owner of a provisioned product to another IAM or STS entity within the
same account. Both end user owners and administrators can see ownership history of the provisioned
product using the `ListRecordHistory` API. The new owner can describe all past records
for the provisioned product using the `DescribeRecord` API. The previous owner can no
longer use `DescribeRecord`, but can still see the product's history from when he was
an owner using `ListRecordHistory`.

If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or
AWS Service Catalog console such as update, terminate, and execute service actions.
If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through
API or the AWS Service Catalog console on that provisioned product.

Type: String to string map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Valid Keys: `OWNER | LAUNCH_ROLE`

Value Length Constraints: Minimum length of 0. Maximum length of 1024.

Required: Yes

## Response Syntax

```
{
   "ProvisionedProductId": "***string***",
   "ProvisionedProductProperties": {
      "***string***" : "***string***"
   },
   "RecordId": "***string***",
   "Status": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ProvisionedProductId](#API_UpdateProvisionedProductProperties_ResponseSyntax "#API_UpdateProvisionedProductProperties_ResponseSyntax")**

The provisioned product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[ProvisionedProductProperties](#API_UpdateProvisionedProductProperties_ResponseSyntax "#API_UpdateProvisionedProductProperties_ResponseSyntax")**

A map that contains the properties updated.

Type: String to string map

Map Entries: Maximum number of 100 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Valid Keys: `OWNER | LAUNCH_ROLE`

Value Length Constraints: Minimum length of 0. Maximum length of 1024.

**[RecordId](#API_UpdateProvisionedProductProperties_ResponseSyntax "#API_UpdateProvisionedProductProperties_ResponseSyntax")**

The identifier of the record.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[Status](#API_UpdateProvisionedProductProperties_ResponseSyntax "#API_UpdateProvisionedProductProperties_ResponseSyntax")**

The status of the request.

Type: String

Valid Values: `CREATED | IN_PROGRESS | IN_PROGRESS_IN_ERROR | SUCCEEDED | FAILED`

## Errors

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**InvalidStateException**

An attempt was made to modify a resource that is in a state that is not valid.
Check your resources to ensure that they are in valid states before retrying the operation.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties.md")
