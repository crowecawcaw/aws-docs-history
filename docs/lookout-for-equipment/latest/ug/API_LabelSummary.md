

 On October 7, 2026, AWS will discontinue support for Amazon Lookout for Equipment. After October 7, 2026, you will no longer be able to access the Lookout for Equipment console or resources. For more information, [see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/). 

# LabelSummary
<a name="API_LabelSummary"></a>

 Information about the label. 

## Contents
<a name="API_LabelSummary_Contents"></a>

 ** CreatedAt **   <a name="LookoutForEquipment-Type-LabelSummary-CreatedAt"></a>
 The time at which the label was created.   
Type: Timestamp  
Required: No

 ** EndTime **   <a name="LookoutForEquipment-Type-LabelSummary-EndTime"></a>
 The timestamp indicating the end of the label.   
Type: Timestamp  
Required: No

 ** Equipment **   <a name="LookoutForEquipment-Type-LabelSummary-Equipment"></a>
 Indicates that a label pertains to a particular piece of equipment.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `[\P{M}\p{M}]{1,200}`   
Required: No

 ** FaultCode **   <a name="LookoutForEquipment-Type-LabelSummary-FaultCode"></a>
 Indicates the type of anomaly associated with the label.   
Data in this field will be retained for service usage. Follow best practices for the security of your data.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100.  
Pattern: `[\P{M}\p{M}]{1,100}`   
Required: No

 ** LabelGroupArn **   <a name="LookoutForEquipment-Type-LabelSummary-LabelGroupArn"></a>
 The Amazon Resource Name (ARN) of the label group.   
Type: String  
Length Constraints: Minimum length of 20. Maximum length of 2048.  
Pattern: `arn:aws(-[^:]+)?:lookoutequipment:[a-zA-Z0-9\-]*:[0-9]{12}:label-group\/.+`   
Required: No

 ** LabelGroupName **   <a name="LookoutForEquipment-Type-LabelSummary-LabelGroupName"></a>
 The name of the label group.   
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 200.  
Pattern: `^[0-9a-zA-Z_-]{1,200}$`   
Required: No

 ** LabelId **   <a name="LookoutForEquipment-Type-LabelSummary-LabelId"></a>
 The ID of the label.   
Type: String  
Length Constraints: Maximum length of 32.  
Pattern: `[A-Fa-f0-9]{0,32}`   
Required: No

 ** Rating **   <a name="LookoutForEquipment-Type-LabelSummary-Rating"></a>
 Indicates whether a labeled event represents an anomaly.   
Type: String  
Valid Values: `ANOMALY | NO_ANOMALY | NEUTRAL`   
Required: No

 ** StartTime **   <a name="LookoutForEquipment-Type-LabelSummary-StartTime"></a>
 The timestamp indicating the start of the label.   
Type: Timestamp  
Required: No

## See Also
<a name="API_LabelSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lookoutequipment-2020-12-15/LabelSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lookoutequipment-2020-12-15/LabelSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lookoutequipment-2020-12-15/LabelSummary) 