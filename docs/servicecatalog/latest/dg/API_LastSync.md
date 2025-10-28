# LastSync

Provides details about the product's connection sync and contains the following sub-fields.

- `LastSyncTime`
- `LastSyncStatus`
- `LastSyncStatusMessage`
- `LastSuccessfulSyncTime`
- `LastSuccessfulSyncProvisioningArtifactID`

## Contents

**LastSuccessfulSyncProvisioningArtifactId**

The ProvisioningArtifactID of the ProvisioningArtifact created from the latest successful sync.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**LastSuccessfulSyncTime**

The time of the latest successful sync from the source repo artifact to the AWS Service Catalog product.

Type: Timestamp

Required: No

**LastSyncStatus**

The current status of the sync. Responses include `SUCCEEDED` or `FAILED`.

Type: String

Valid Values: `SUCCEEDED | FAILED`

Required: No

**LastSyncStatusMessage**

The sync's status message.

Type: String

Required: No

**LastSyncTime**

The time of the last attempted sync from the repository to the AWS Service Catalog product.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/LastSync.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/LastSync.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/LastSync.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/LastSync.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/LastSync.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/LastSync.md")
