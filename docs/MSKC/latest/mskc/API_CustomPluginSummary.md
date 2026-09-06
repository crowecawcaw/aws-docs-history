

# CustomPluginSummary
<a name="API_CustomPluginSummary"></a>

A summary of the custom plugin.

## Contents
<a name="API_CustomPluginSummary_Contents"></a>

 ** creationTime **   <a name="MSKC-Type-CustomPluginSummary-creationTime"></a>
The time that the custom plugin was created.  
Type: Timestamp  
Required: No

 ** customPluginArn **   <a name="MSKC-Type-CustomPluginSummary-customPluginArn"></a>
The Amazon Resource Name (ARN) of the custom plugin.  
Type: String  
Required: No

 ** customPluginState **   <a name="MSKC-Type-CustomPluginSummary-customPluginState"></a>
The state of the custom plugin.  
Type: String  
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | UPDATING | UPDATE_FAILED | DELETING`   
Required: No

 ** description **   <a name="MSKC-Type-CustomPluginSummary-description"></a>
A description of the custom plugin.  
Type: String  
Required: No

 ** latestRevision **   <a name="MSKC-Type-CustomPluginSummary-latestRevision"></a>
The latest revision of the custom plugin.  
Type: [CustomPluginRevisionSummary](API_CustomPluginRevisionSummary.md) object  
Required: No

 ** name **   <a name="MSKC-Type-CustomPluginSummary-name"></a>
The name of the custom plugin.  
Type: String  
Required: No

## See Also
<a name="API_CustomPluginSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/CustomPluginSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/CustomPluginSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/CustomPluginSummary) 