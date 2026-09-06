

# AutoTrainingConfig
<a name="API_AutoTrainingConfig"></a>

The automatic training configuration to use when `performAutoTraining` is true.

## Contents
<a name="API_AutoTrainingConfig_Contents"></a>

 ** schedulingExpression **   <a name="personalize-Type-AutoTrainingConfig-schedulingExpression"></a>
Specifies how often to automatically train new solution versions. Specify a rate expression in rate(*value* *unit*) format. For value, specify a number between 1 and 30. For unit, specify `day` or `days`. For example, to automatically create a new solution version every 5 days, specify `rate(5 days)`. The default is every 7 days.  
For more information about auto training, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html).  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 16.  
Pattern: `rate\(\d+ days?\)`   
Required: No

## See Also
<a name="API_AutoTrainingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/AutoTrainingConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/AutoTrainingConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/AutoTrainingConfig) 