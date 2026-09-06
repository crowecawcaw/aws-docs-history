

# CustomPluginRevisionSummary
<a name="API_CustomPluginRevisionSummary"></a>

Details about the revision of a custom plugin.

## Contents
<a name="API_CustomPluginRevisionSummary_Contents"></a>

 ** contentType **   <a name="MSKC-Type-CustomPluginRevisionSummary-contentType"></a>
The format of the plugin file.  
Type: String  
Valid Values: `JAR | ZIP`   
Required: No

 ** creationTime **   <a name="MSKC-Type-CustomPluginRevisionSummary-creationTime"></a>
The time that the custom plugin was created.  
Type: Timestamp  
Required: No

 ** description **   <a name="MSKC-Type-CustomPluginRevisionSummary-description"></a>
The description of the custom plugin.  
Type: String  
Required: No

 ** fileDescription **   <a name="MSKC-Type-CustomPluginRevisionSummary-fileDescription"></a>
Details about the custom plugin file.  
Type: [CustomPluginFileDescription](API_CustomPluginFileDescription.md) object  
Required: No

 ** location **   <a name="MSKC-Type-CustomPluginRevisionSummary-location"></a>
Information about the location of the custom plugin.  
Type: [CustomPluginLocationDescription](API_CustomPluginLocationDescription.md) object  
Required: No

 ** revision **   <a name="MSKC-Type-CustomPluginRevisionSummary-revision"></a>
The revision of the custom plugin.  
Type: Long  
Required: No

## See Also
<a name="API_CustomPluginRevisionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/CustomPluginRevisionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/CustomPluginRevisionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/CustomPluginRevisionSummary) 