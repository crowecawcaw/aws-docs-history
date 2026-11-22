

# WorkerSetting

Details about worker setting of a connector

## Contents
<a name="API_WorkerSetting_Contents"></a>

 ** capacity **   <a name="MSKC-Type-WorkerSetting-capacity"></a>
Specifies the compute capacity settings of the connector.  
Type: [CapacityDescription](API_CapacityDescription.md) object  
Required: No

 ** plugins **   <a name="MSKC-Type-WorkerSetting-plugins"></a>
Specifies which plugins the connector uses.  
Type: Array of [PluginDescription](API_PluginDescription.md) objects  
Required: No

 ** useDefaultWorkerConfiguration **   <a name="MSKC-Type-WorkerSetting-useDefaultWorkerConfiguration"></a>
Specifies whether the connector uses the default worker configuration instead of a custom worker configuration.  
Type: Boolean  
Required: No

 ** workerConfiguration **   <a name="MSKC-Type-WorkerSetting-workerConfiguration"></a>
Specifies which worker configuration the connector uses.  
Type: [WorkerConfigurationDescription](API_WorkerConfigurationDescription.md) object  
Required: No

## See Also
<a name="API_WorkerSetting_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/WorkerSetting) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/WorkerSetting) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/WorkerSetting) 