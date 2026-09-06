

# EventParameters
<a name="API_EventParameters"></a>

Describes the parameters of events, which are used in solution creation.

## Contents
<a name="API_EventParameters_Contents"></a>

 ** eventType **   <a name="personalize-Type-EventParameters-eventType"></a>
The name of the event type to be considered for solution creation.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** eventValueThreshold **   <a name="personalize-Type-EventParameters-eventValueThreshold"></a>
The threshold of the event type. Only events with a value greater or equal to this threshold will be considered for solution creation.  
Type: Double  
Required: No

 ** weight **   <a name="personalize-Type-EventParameters-weight"></a>
The weight of the event type. A higher weight means higher importance of the event type for the created solution.  
Type: Double  
Valid Range: Minimum value of 0. Maximum value of 1.  
Required: No

## See Also
<a name="API_EventParameters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/EventParameters) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/EventParameters) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/EventParameters) 