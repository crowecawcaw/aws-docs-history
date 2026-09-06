

 Amazon Forecast is no longer available to new customers. Existing customers of Amazon Forecast can continue to use the service as normal. [Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/)

# TimeSeriesIdentifiers
<a name="API_TimeSeriesIdentifiers"></a>

Details about the import file that contains the time series for which you want to create forecasts.

## Contents
<a name="API_TimeSeriesIdentifiers_Contents"></a>

 ** DataSource **   <a name="forecast-Type-TimeSeriesIdentifiers-DataSource"></a>
The source of your data, an AWS Identity and Access Management (IAM) role that allows Amazon Forecast to access the data and, optionally, an AWS Key Management Service (KMS) key.  
Type: [DataSource](API_DataSource.md) object  
Required: No

 ** Format **   <a name="forecast-Type-TimeSeriesIdentifiers-Format"></a>
The format of the data, either CSV or PARQUET.  
Type: String  
Length Constraints: Maximum length of 7.  
Pattern: `^CSV|PARQUET$`   
Required: No

 ** Schema **   <a name="forecast-Type-TimeSeriesIdentifiers-Schema"></a>
Defines the fields of a dataset.  
Type: [Schema](API_Schema.md) object  
Required: No

## See Also
<a name="API_TimeSeriesIdentifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/forecast-2018-06-26/TimeSeriesIdentifiers) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/forecast-2018-06-26/TimeSeriesIdentifiers) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/forecast-2018-06-26/TimeSeriesIdentifiers) 