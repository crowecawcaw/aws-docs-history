

After careful consideration, we have decided to discontinue Amazon Kinesis Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md).

# ApplicationUpdate
<a name="API_ApplicationUpdate"></a>

Describes updates to apply to an existing Amazon Kinesis Analytics application.

## Contents
<a name="API_ApplicationUpdate_Contents"></a>

 ** ApplicationCodeUpdate **   <a name="analytics-Type-ApplicationUpdate-ApplicationCodeUpdate"></a>
Describes application code updates.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 102400.  
Required: No

 ** CloudWatchLoggingOptionUpdates **   <a name="analytics-Type-ApplicationUpdate-CloudWatchLoggingOptionUpdates"></a>
Describes application CloudWatch logging option updates.  
Type: Array of [CloudWatchLoggingOptionUpdate](API_CloudWatchLoggingOptionUpdate.md) objects  
Required: No

 ** InputUpdates **   <a name="analytics-Type-ApplicationUpdate-InputUpdates"></a>
Describes application input configuration updates.  
Type: Array of [InputUpdate](API_InputUpdate.md) objects  
Required: No

 ** OutputUpdates **   <a name="analytics-Type-ApplicationUpdate-OutputUpdates"></a>
Describes application output configuration updates.  
Type: Array of [OutputUpdate](API_OutputUpdate.md) objects  
Required: No

 ** ReferenceDataSourceUpdates **   <a name="analytics-Type-ApplicationUpdate-ReferenceDataSourceUpdates"></a>
Describes application reference data source updates.  
Type: Array of [ReferenceDataSourceUpdate](API_ReferenceDataSourceUpdate.md) objects  
Required: No

## See Also
<a name="API_ApplicationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalytics-2015-08-14/ApplicationUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalytics-2015-08-14/ApplicationUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalytics-2015-08-14/ApplicationUpdate) 