# ProvisioningArtifactDetail

Information about a provisioning artifact (also known as a version) for a product.

## Contents

**Active**

Indicates whether the product version is active.

Type: Boolean

Required: No

**CreatedTime**

The UTC time stamp of the creation time.

Type: Timestamp

Required: No

**Description**

The description of the provisioning artifact.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**Guidance**

Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.

Type: String

Valid Values: `DEFAULT | DEPRECATED`

Required: No

**Id**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**Name**

The name of the provisioning artifact.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**SourceRevision**

Specifies the revision of the external artifact that was used to automatically sync the AWS Service Catalog product
and create the provisioning artifact. AWS Service Catalog includes this response parameter as a high level
field to the existing `ProvisioningArtifactDetail` type, which is returned as part of the
response for `CreateProduct`, `UpdateProduct`, `DescribeProductAsAdmin`,
`DescribeProvisioningArtifact`, `ListProvisioningArtifact`,
and `UpdateProvisioningArticat` APIs.

This field only exists for Repo-Synced products.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 512.

Required: No

**Type**

The type of provisioning artifact.

- `CLOUD_FORMATION_TEMPLATE` - AWS CloudFormation template
- `TERRAFORM_OPEN_SOURCE` - Terraform Open Source configuration file
- `TERRAFORM_CLOUD` - Terraform Cloud configuration file
- `EXTERNAL` - External configuration file

Type: String

Valid Values: `CLOUD_FORMATION_TEMPLATE | MARKETPLACE_AMI | MARKETPLACE_CAR | TERRAFORM_OPEN_SOURCE | EXTERNAL | TERRAFORM_CLOUD`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactDetail.md")
