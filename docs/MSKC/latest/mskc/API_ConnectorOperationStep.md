

# ConnectorOperationStep
<a name="API_ConnectorOperationStep"></a>

Details of a step that is involved in a connector's operation.

## Contents
<a name="API_ConnectorOperationStep_Contents"></a>

 ** stepState **   <a name="MSKC-Type-ConnectorOperationStep-stepState"></a>
The step state of the operation.  
Type: String  
Valid Values: `PENDING | IN_PROGRESS | COMPLETED | FAILED | CANCELLED`   
Required: No

 ** stepType **   <a name="MSKC-Type-ConnectorOperationStep-stepType"></a>
The step type of the operation.  
Type: String  
Valid Values: `INITIALIZE_UPDATE | FINALIZE_UPDATE | UPDATE_WORKER_SETTING | UPDATE_CONNECTOR_CONFIGURATION | VALIDATE_UPDATE`   
Required: No

## See Also
<a name="API_ConnectorOperationStep_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ConnectorOperationStep) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ConnectorOperationStep) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ConnectorOperationStep) 