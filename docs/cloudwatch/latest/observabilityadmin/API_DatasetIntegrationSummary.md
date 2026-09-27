

# DatasetIntegrationSummary
<a name="API_DatasetIntegrationSummary"></a>

Contains summary information about a dataset integration, including its ARN, associated IAM role, and creation and update timestamps, as returned by `ListDatasetIntegrations`.

## Contents
<a name="API_DatasetIntegrationSummary_Contents"></a>

 ** Arn **   <a name="cwoa-Type-DatasetIntegrationSummary-Arn"></a>
The Amazon Resource Name (ARN) of the dataset integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: Yes

 ** CreatedAt **   <a name="cwoa-Type-DatasetIntegrationSummary-CreatedAt"></a>
The timestamp when the dataset integration was created.  
Type: Timestamp  
Required: No

 ** RoleArn **   <a name="cwoa-Type-DatasetIntegrationSummary-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role associated with the dataset integration.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 1011.  
Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`   
Required: No

 ** UpdatedAt **   <a name="cwoa-Type-DatasetIntegrationSummary-UpdatedAt"></a>
The timestamp when the dataset integration was last updated.  
Type: Timestamp  
Required: No

## See Also
<a name="API_DatasetIntegrationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/observabilityadmin-2018-05-10/DatasetIntegrationSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/observabilityadmin-2018-05-10/DatasetIntegrationSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/observabilityadmin-2018-05-10/DatasetIntegrationSummary) 