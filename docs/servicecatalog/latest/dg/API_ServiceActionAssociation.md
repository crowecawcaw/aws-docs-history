# ServiceActionAssociation

A self-service action association consisting of the Action ID, the Product ID, and the Provisioning Artifact ID.

## Contents

**ProductId**

The product identifier. For example, `prod-abcdzk7xy33qa`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**ProvisioningArtifactId**

The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**ServiceActionId**

The self-service action identifier. For example, `act-fs7abcd89wxyz`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ServiceActionAssociation.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ServiceActionAssociation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ServiceActionAssociation.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ServiceActionAssociation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ServiceActionAssociation.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ServiceActionAssociation.md")
