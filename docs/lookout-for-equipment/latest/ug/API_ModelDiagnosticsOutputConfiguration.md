On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ModelDiagnosticsOutputConfiguration

Output configuration information for the pointwise model diagnostics for an Amazon Lookout for Equipment model.

## Contents

**S3OutputConfiguration**

The Amazon S3 location for the pointwise model diagnostics.

Type: [ModelDiagnosticsS3OutputConfiguration](API_ModelDiagnosticsS3OutputConfiguration.md "API_ModelDiagnosticsS3OutputConfiguration.md") object

Required: Yes

**KmsKeyId**

The AWS Key Management Service (KMS) key identifier to encrypt the pointwise model diagnostics files.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelDiagnosticsOutputConfiguration.md")
