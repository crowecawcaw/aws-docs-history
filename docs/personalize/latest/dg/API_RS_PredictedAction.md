

# PredictedAction
<a name="API_RS_PredictedAction"></a>

An object that identifies an action.

The [GetActionRecommendations](API_RS_GetActionRecommendations.md) API returns a list of `PredictedAction`s.

## Contents
<a name="API_RS_PredictedAction_Contents"></a>

 ** actionId **   <a name="personalize-Type-RS_PredictedAction-actionId"></a>
The ID of the recommended action.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** score **   <a name="personalize-Type-RS_PredictedAction-score"></a>
The score of the recommended action. For information about action scores, see [How action recommendation scoring works](https://docs.aws.amazon.com/personalize/latest/dg/how-action-recommendation-scoring-works.html).  
Type: Double  
Required: No

## See Also
<a name="API_RS_PredictedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-runtime-2018-05-22/PredictedAction) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-runtime-2018-05-22/PredictedAction) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-runtime-2018-05-22/PredictedAction) 