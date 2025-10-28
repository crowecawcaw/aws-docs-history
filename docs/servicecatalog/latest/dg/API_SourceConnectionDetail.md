# SourceConnectionDetail

Provides details about the configured `SourceConnection`.

## Contents

**ConnectionParameters**

The connection details based on the connection `Type`.

Type: [SourceConnectionParameters](API_SourceConnectionParameters.md "API_SourceConnectionParameters.md") object

Required: No

**LastSync**

Provides details about the product's connection sync and contains the following sub-fields.

- `LastSyncTime`
- `LastSyncStatus`
- `LastSyncStatusMessage`
- `LastSuccessfulSyncTime`
- `LastSuccessfulSyncProvisioningArtifactID`

Type: [LastSync](API_LastSync.md "API_LastSync.md") object

Required: No

**Type**

The only supported `SourceConnection` type is Codestar.

Type: String

Valid Values: `CODESTAR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnectionDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/SourceConnectionDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnectionDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/SourceConnectionDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnectionDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/SourceConnectionDetail.md")
