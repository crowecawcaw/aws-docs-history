

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# ModelVersionSummary
<a name="API_ModelVersionSummary"></a>

Contains information about the specific model version.

## Contents
<a name="API_ModelVersionSummary_Contents"></a>

 ** CreatedAt **   <a name="LookoutForEquipment-Type-ModelVersionSummary-CreatedAt"></a>
The time when this model version was created.  
Type: Timestamp  
Required: No

 ** ModelArn **   <a name="LookoutForEquipment-Type-ModelVersionSummary-ModelArn"></a>
The Amazon Resource Name (ARN) of the model that this model version is a version of.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/.+`   
Required: No

 ** ModelName **   <a name="LookoutForEquipment-Type-ModelVersionSummary-ModelName"></a>
The name of the model that this model version is a version of.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** ModelQuality **   <a name="LookoutForEquipment-Type-ModelVersionSummary-ModelQuality"></a>
Provides a quality assessment for a model that uses labels. If Lookout for Equipment determines that the model quality is poor based on training metrics, the value is `POOR_QUALITY_DETECTED`. Otherwise, the value is `QUALITY_THRESHOLD_MET`.   
If the model is unlabeled, the model quality can't be assessed and the value of `ModelQuality` is `CANNOT_DETERMINE_QUALITY`. In this situation, you can get a model quality assessment by adding labels to the input dataset and retraining the model.  
For information about improving the quality of a model, see [Best practices with Amazon Lookout for Equipment](https://docs.aws.amazon.com/lookout-for-equipment/latest/ug/best-practices.html).  
Type: String  
Valid Values: `QUALITY_THRESHOLD_MET | CANNOT_DETERMINE_QUALITY | POOR_QUALITY_DETECTED`   
Required: No

 ** ModelVersion **   <a name="LookoutForEquipment-Type-ModelVersionSummary-ModelVersion"></a>
The version of the model.  
Type: Long  
Valid Range: Minimum value of 1.  
Required: No

 ** ModelVersionArn **   <a name="LookoutForEquipment-Type-ModelVersionSummary-ModelVersionArn"></a>
The Amazon Resource Name (ARN) of the model version.  
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `^arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:model\/[0-9a-zA-Z_-]{1,200}\/.+\/model-version\/[0-9]{1,}$`   
Required: No

 ** SourceType **   <a name="LookoutForEquipment-Type-ModelVersionSummary-SourceType"></a>
Indicates how this model version was generated.  
Type: String  
Valid Values: `TRAINING | RETRAINING | IMPORT`   
Required: No

 ** Status **   <a name="LookoutForEquipment-Type-ModelVersionSummary-Status"></a>
The current status of the model version.  
Type: String  
Valid Values: `IN_PROGRESS | SUCCESS | FAILED | IMPORT_IN_PROGRESS | CANCELED`   
Required: No

## See Also
<a name="API_ModelVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/ModelVersionSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/ModelVersionSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/ModelVersionSummary) 