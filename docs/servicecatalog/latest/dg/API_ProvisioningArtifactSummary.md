# ProvisioningArtifactSummary

Summary information about a provisioning artifact (also known as a version) for a product.

## Contents

**CreatedTime**

The UTC time stamp of the creation time.

Type: Timestamp

Required: No

**Description**

The description of the provisioning artifact.

Type: String

Length Constraints: Maximum length of 8192.

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

**ProvisioningArtifactMetadata**

The metadata for the provisioning artifact. This is used with AWS Marketplace products.

Type: String to string map

Map Entries: Maximum number of 100 items.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactSummary.md")
