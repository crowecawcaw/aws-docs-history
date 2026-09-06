

# DataSource
<a name="API_DataSource"></a>

Information about a data source associated with the telemetry pipeline. For CloudWatch Logs sources, this includes both a name and type extracted from the log event metadata. For third-party sources (such as S3), this includes only a name, with the type field left empty.

## Contents
<a name="API_DataSource_Contents"></a>

 ** Name **   <a name="cwoa-Type-DataSource-Name"></a>
The name of the data source. For CloudWatch Logs sources, this corresponds to the `data_source_name` from the log event metadata. For third-party sources, this is either the configured `data_source_name` or defaults to the plugin name if not specified.  
Type: String  
Required: No

 ** Type **   <a name="cwoa-Type-DataSource-Type"></a>
The type of the data source. For CloudWatch Logs sources, this corresponds to the `data_source_type` from the log event metadata. For third-party sources, this field is empty.  
Type: String  
Required: No

## See Also
<a name="API_DataSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/DataSource) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/DataSource) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/DataSource) 