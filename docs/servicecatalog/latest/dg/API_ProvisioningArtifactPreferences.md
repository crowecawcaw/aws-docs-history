# ProvisioningArtifactPreferences

The user-defined preferences that will be applied during product provisioning, unless overridden by `ProvisioningPreferences` or `UpdateProvisioningPreferences`.

For more information on maximum concurrent accounts and failure tolerance, see [Stack set operation options](../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options "../../../AWSCloudFormation/latest/UserGuide/stacksets-concepts.md#stackset-ops-options") in the _AWS CloudFormation User Guide_.

## Contents

**StackSetAccounts**

One or more AWS accounts where stack instances are deployed from the stack set. These accounts can be scoped in `ProvisioningPreferences$StackSetAccounts` and `UpdateProvisioningPreferences$StackSetAccounts`.

Applicable only to a `CFN_STACKSET` provisioned product type.

Type: Array of strings

Pattern: `^[0-9]{12}$`

Required: No

**StackSetRegions**

One or more AWS Regions where stack instances are deployed from the stack set. These Regions can be scoped in `ProvisioningPreferences$StackSetRegions` and `UpdateProvisioningPreferences$StackSetRegions`.

Applicable only to a `CFN_STACKSET` provisioned product type.

Type: Array of strings

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisioningArtifactPreferences.md")
