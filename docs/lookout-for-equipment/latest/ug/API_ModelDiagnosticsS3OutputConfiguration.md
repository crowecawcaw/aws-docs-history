On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# ModelDiagnosticsS3OutputConfiguration

The Amazon S3 location for the pointwise model diagnostics for an Amazon Lookout for Equipment model.

## Contents

**Bucket**

The name of the Amazon S3 bucket where the pointwise model diagnostics are located. You must be the owner of the Amazon S3 bucket.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 63.

Pattern: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`

Required: Yes

**Prefix**

The Amazon S3 prefix for the location of the pointwise model diagnostics. The
prefix specifies the folder and evaluation result file name.
(`bucket`).

When you call `CreateModel` or `UpdateModel`, specify the path
within the bucket that you want Lookout for Equipment to save the model to. During training, Lookout for Equipment creates the model evaluation model
as a compressed JSON file with the name `model_diagnostics_results.json.gz`.

When you call `DescribeModel` or `DescribeModelVersion`, `prefix` contains
the file path and filename of the model evaluation file.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1024.

Pattern: `(^$)|([\u0009\u000A\u000D\u0020-\u00FF]{1,1023}/$)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md "../../../goto/SdkForCpp/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md "../../../goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md "../../../goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelDiagnosticsS3OutputConfiguration.md")
