

# WorkerConfigurationSummary
<a name="API_WorkerConfigurationSummary"></a>

The summary of a worker configuration.

## Contents
<a name="API_WorkerConfigurationSummary_Contents"></a>

 ** creationTime **   <a name="MSKC-Type-WorkerConfigurationSummary-creationTime"></a>
The time that a worker configuration was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="MSKC-Type-WorkerConfigurationSummary-description"></a>
The description of a worker configuration.  
Type: String  
Required: No

 ** latestRevision **   <a name="MSKC-Type-WorkerConfigurationSummary-latestRevision"></a>
The latest revision of a worker configuration.  
Type: [WorkerConfigurationRevisionSummary](API_WorkerConfigurationRevisionSummary.md) object  
Required: No

 ** name **   <a name="MSKC-Type-WorkerConfigurationSummary-name"></a>
The name of the worker configuration.  
Type: String  
Required: No

 ** workerConfigurationArn **   <a name="MSKC-Type-WorkerConfigurationSummary-workerConfigurationArn"></a>
The Amazon Resource Name (ARN) of the worker configuration.  
Type: String  
Required: No

 ** workerConfigurationState **   <a name="MSKC-Type-WorkerConfigurationSummary-workerConfigurationState"></a>
The state of the worker configuration.  
Type: String  
Valid Values: `ACTIVE | DELETING`   
Required: No

## See Also
<a name="API_WorkerConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerConfigurationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerConfigurationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerConfigurationSummary) 