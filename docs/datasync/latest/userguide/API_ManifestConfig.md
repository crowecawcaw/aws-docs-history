# ManifestConfig

Configures a manifest, which is a list of files or objects that you want AWS DataSync to transfer. For more information and configuration examples, see [Specifying what DataSync transfers by using a manifest](transferring-with-manifest.md "transferring-with-manifest.md").

## Contents

**Action**

Specifies what DataSync uses the manifest for.

Type: String

Valid Values: `TRANSFER`

Required: No

**Format**

Specifies the file format of your manifest. For more information, see [Creating a manifest](transferring-with-manifest.md#transferring-with-manifest-create "transferring-with-manifest.md#transferring-with-manifest-create").

Type: String

Valid Values: `CSV`

Required: No

**Source**

Specifies the manifest that you want DataSync to use and where it's
hosted.

###### Note

You must specify this parameter if you're configuring a new manifest on or after
February 7, 2024.

If you don't, you'll get a 400 status code and `ValidationException` error
stating that you're missing the IAM role for DataSync to access the
S3 bucket where you're hosting your manifest. For more information, see [Providing DataSync access to your manifest](transferring-with-manifest.md#transferring-with-manifest-access "transferring-with-manifest.md#transferring-with-manifest-access").

Type: [SourceManifestConfig](API_SourceManifestConfig.md "API_SourceManifestConfig.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/ManifestConfig.md "../../../goto/SdkForCpp/datasync-2018-11-09/ManifestConfig.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/ManifestConfig.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/ManifestConfig.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/ManifestConfig.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/ManifestConfig.md")
