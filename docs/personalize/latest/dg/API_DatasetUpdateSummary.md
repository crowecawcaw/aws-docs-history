

# DatasetUpdateSummary
<a name="API_DatasetUpdateSummary"></a>

Describes an update to a dataset.

## Contents
<a name="API_DatasetUpdateSummary_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-DatasetUpdateSummary-creationDateTime"></a>
The creation date and time (in Unix time) of the dataset update.  
Type: Timestamp  
Required: No

 ** failureReason **   <a name="personalize-Type-DatasetUpdateSummary-failureReason"></a>
If updating a dataset fails, provides the reason why.  
Type: String  
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-DatasetUpdateSummary-lastUpdatedDateTime"></a>
The last update date and time (in Unix time) of the dataset.  
Type: Timestamp  
Required: No

 ** schemaArn **   <a name="personalize-Type-DatasetUpdateSummary-schemaArn"></a>
The Amazon Resource Name (ARN) of the schema that replaced the previous schema of the dataset.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** status **   <a name="personalize-Type-DatasetUpdateSummary-status"></a>
The status of the dataset update.   
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_DatasetUpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/DatasetUpdateSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/DatasetUpdateSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/DatasetUpdateSummary) 