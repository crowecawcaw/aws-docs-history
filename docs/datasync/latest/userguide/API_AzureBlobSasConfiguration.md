# AzureBlobSasConfiguration

The shared access signature (SAS) configuration that allows AWS DataSync to
access your Microsoft Azure Blob Storage.

For more information, see [SAS
tokens](creating-azure-blob-location.md#azure-blob-sas-tokens "creating-azure-blob-location.md#azure-blob-sas-tokens") for accessing your Azure Blob Storage.

## Contents

**Token**

Specifies a SAS token that provides permissions to access your Azure Blob Storage.

The token is part of the SAS URI string that comes after the storage resource URI and a
question mark. A token looks something like this:

`sp=r&st=2023-12-20T14:54:52Z&se=2023-12-20T22:54:52Z&spr=https&sv=2021-06-08&sr=c&sig=aBBKDWQvyuVcTPH9EBp%2FXTI9E%2F%2Fmq171%2BZU178wcwqU%3D`

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Pattern: `^.+$`

Required: Yes

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/AzureBlobSasConfiguration.md "../../../goto/SdkForCpp/datasync-2018-11-09/AzureBlobSasConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/AzureBlobSasConfiguration.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/AzureBlobSasConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/AzureBlobSasConfiguration.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/AzureBlobSasConfiguration.md")
