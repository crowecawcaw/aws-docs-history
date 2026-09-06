

# ConnectorOperationSummary
<a name="API_ConnectorOperationSummary"></a>

Summary of a connector operation.

## Contents
<a name="API_ConnectorOperationSummary_Contents"></a>

 ** connectorOperationArn **   <a name="MSKC-Type-ConnectorOperationSummary-connectorOperationArn"></a>
The Amazon Resource Name (ARN) of the connector operation.  
Type: String  
Required: No

 ** connectorOperationState **   <a name="MSKC-Type-ConnectorOperationSummary-connectorOperationState"></a>
The state of the connector operation.  
Type: String  
Valid Values: `PENDING | UPDATE_IN_PROGRESS | UPDATE_COMPLETE | UPDATE_FAILED | ROLLBACK_IN_PROGRESS | ROLLBACK_FAILED | ROLLBACK_COMPLETE`   
Required: No

 ** connectorOperationType **   <a name="MSKC-Type-ConnectorOperationSummary-connectorOperationType"></a>
The type of connector operation performed.  
Type: String  
Valid Values: `UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | ISOLATE_CONNECTOR | RESTORE_CONNECTOR`   
Required: No

 ** creationTime **   <a name="MSKC-Type-ConnectorOperationSummary-creationTime"></a>
The time when operation was created.  
Type: Timestamp  
Required: No

 ** endTime **   <a name="MSKC-Type-ConnectorOperationSummary-endTime"></a>
The time when operation ended.  
Type: Timestamp  
Required: No

## See Also
<a name="API_ConnectorOperationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorOperationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorOperationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorOperationSummary) 