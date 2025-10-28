# ConnectorOperationSummary

Summary of a connector operation.

## Contents

**connectorOperationArn**

The Amazon Resource Name (ARN) of the connector operation.

Type: String

Required: No

**connectorOperationState**

The state of the connector operation.

Type: String

Valid Values: `PENDING | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE`

Required: No

**connectorOperationType**

The type of connector operation performed.

Type: String

Valid Values: `UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | ISOLATE_CONNECTOR | RESTORE_CONNECTOR`

Required: No

**creationTime**

The time when operation was created.

Type: Timestamp

Required: No

**endTime**

The time when operation ended.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorOperationSummary.md "../../../goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorOperationSummary.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorOperationSummary.md "../../../goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorOperationSummary.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorOperationSummary.md "../../../goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorOperationSummary.md")
