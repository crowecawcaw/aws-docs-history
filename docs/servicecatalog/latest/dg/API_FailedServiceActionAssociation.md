# FailedServiceActionAssociation

An object containing information about the error, along with identifying information about the self-service action and its associations.

## Contents

**ErrorCode**

The error code. Valid values are listed below.

Type: String

Valid Values: `DUPLICATE_RESOURCE | INTERNAL_FAILURE | LIMIT_EXCEEDED | RESOURCE_NOT_FOUND | THROTTLING | INVALID_PARAMETER`

Required: No

**ErrorMessage**

A text description of the error.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1024.

Required: No

**ProductId**

The product identifier. For example, `prod-abcdzk7xy33qa`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisioningArtifactId**

The identifier of the provisioning artifact. For example, `pa-4abcdjnxjj6ne`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ServiceActionId**

The self-service action identifier. For example, `act-fs7abcd89wxyz`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/FailedServiceActionAssociation.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/FailedServiceActionAssociation.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/FailedServiceActionAssociation.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/FailedServiceActionAssociation.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/FailedServiceActionAssociation.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/FailedServiceActionAssociation.md")
