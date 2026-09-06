

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# LabelGroupSummary
<a name="API_LabelGroupSummary"></a>

 Contains information about the label group. 

## Contents
<a name="API_LabelGroupSummary_Contents"></a>

 ** CreatedAt **   <a name="LookoutForEquipment-Type-LabelGroupSummary-CreatedAt"></a>
 The time at which the label group was created.   
Type: Timestamp  
Required: No

 ** LabelGroupArn **   <a name="LookoutForEquipment-Type-LabelGroupSummary-LabelGroupArn"></a>
 The Amazon Resource Name (ARN) of the label group.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`   
Required: No

 ** LabelGroupName **   <a name="LookoutForEquipment-Type-LabelGroupSummary-LabelGroupName"></a>
 The name of the label group.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** UpdatedAt **   <a name="LookoutForEquipment-Type-LabelGroupSummary-UpdatedAt"></a>
 The time at which the label group was updated.   
Type: Timestamp  
Required: No

## See Also
<a name="API_LabelGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/LabelGroupSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelGroupSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelGroupSummary) 