# RecordDetail

Information about a request operation.

## Contents

**CreatedTime**

The UTC time stamp of the creation time.

Type: Timestamp

Required: No

**LaunchRoleArn**

The ARN of the launch role associated with the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9-\.]{1,63}:iam::[a-z0-9-\.]{0,63}:role\/.{0,1023}`

Required: No

**PathId**

The path identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProductId**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisionedProductId**

The identifier of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisionedProductName**

The user-friendly name of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: No

**ProvisionedProductType**

The type of provisioned product. The supported values are `CFN_STACK`, `CFN_STACKSET`,
`TERRAFORM_OPEN_SOURCE`, `TERRAFORM_CLOUD`, and `EXTERNAL`.

Type: String

Required: No

**ProvisioningArtifactId**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**RecordErrors**

The errors that occurred.

Type: Array of [RecordError](API_RecordError.md "API_RecordError.md") objects

Required: No

**RecordId**

The identifier of the record.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**RecordTags**

One or more tags.

Type: Array of [RecordTag](API_RecordTag.md "API_RecordTag.md") objects

Array Members: Maximum number of 50 items.

Required: No

**RecordType**

The record type.

- `PROVISION_PRODUCT`
- `UPDATE_PROVISIONED_PRODUCT`
- `TERMINATE_PROVISIONED_PRODUCT`

Type: String

Required: No

**Status**

The status of the provisioned product.

- `CREATED` - The request was created but the operation has not started.
- `IN_PROGRESS` - The requested operation is in progress.
- `IN_PROGRESS_IN_ERROR` - The provisioned product is under change but the
  requested operation failed and some remediation is occurring. For example, a rollback.
- `SUCCEEDED` - The requested operation has successfully completed.
- `FAILED` - The requested operation has unsuccessfully completed.
  Investigate using the error messages returned.

Type: String

Valid Values: `CREATED | IN_PROGRESS | IN_PROGRESS_IN_ERROR | SUCCEEDED | FAILED`

Required: No

**UpdatedTime**

The time when the record was last updated.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/RecordDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/RecordDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/RecordDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/RecordDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/RecordDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/RecordDetail.md")
