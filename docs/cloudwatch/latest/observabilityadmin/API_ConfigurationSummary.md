

# ConfigurationSummary
<a name="API_ConfigurationSummary"></a>

Provides a summary of pipeline configuration components including sources, processors, and destinations.

## Contents
<a name="API_ConfigurationSummary_Contents"></a>

 ** DataSources **   <a name="cwoa-Type-ConfigurationSummary-DataSources"></a>
The list of data sources that provide telemetry data to the pipeline.  
Type: Array of [DataSource](API_DataSource.md) objects  
Required: No

 ** ProcessorCount **   <a name="cwoa-Type-ConfigurationSummary-ProcessorCount"></a>
The total number of processors configured in the pipeline.  
Type: Integer  
Required: No

 ** Processors **   <a name="cwoa-Type-ConfigurationSummary-Processors"></a>
The list of processors configured in the pipeline for data transformation.  
Type: Array of strings  
Required: No

 ** Sinks **   <a name="cwoa-Type-ConfigurationSummary-Sinks"></a>
The list of destinations where processed data is sent.  
Type: Array of strings  
Required: No

 ** Sources **   <a name="cwoa-Type-ConfigurationSummary-Sources"></a>
The list of data sources configured in the pipeline.  
Type: Array of [Source](API_Source.md) objects  
Required: No

## See Also
<a name="API_ConfigurationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/ConfigurationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/ConfigurationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/ConfigurationSummary) 