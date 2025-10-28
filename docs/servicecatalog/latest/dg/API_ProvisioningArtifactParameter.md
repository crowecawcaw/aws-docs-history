# ProvisioningArtifactParameter

Information about a parameter used to provision a product.

## Contents

**DefaultValue**

The default value.

Type: String

Required: No

**Description**

The description of the parameter.

Type: String

Required: No

**IsNoEcho**

If this value is true, the value for this parameter is obfuscated from view when the
parameter is retrieved. This parameter is used to hide sensitive information.

Type: Boolean

Required: No

**ParameterConstraints**

Constraints that the administrator has put on a parameter.

Type: [ParameterConstraints](API_ParameterConstraints.md "API_ParameterConstraints.md") object

Required: No

**ParameterKey**

The parameter key.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1000.

Required: No

**ParameterType**

The parameter type.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactParameter.md")
