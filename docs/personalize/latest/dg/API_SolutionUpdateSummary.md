

# SolutionUpdateSummary
<a name="API_SolutionUpdateSummary"></a>

Provides a summary of the properties of a solution update. For a complete listing, call the [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html) API.

## Contents
<a name="API_SolutionUpdateSummary_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-SolutionUpdateSummary-creationDateTime"></a>
The date and time (in Unix format) that the solution update was created.  
Type: Timestamp  
Required: No

 ** failureReason **   <a name="personalize-Type-SolutionUpdateSummary-failureReason"></a>
If a solution update fails, the reason behind the failure.  
Type: String  
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-SolutionUpdateSummary-lastUpdatedDateTime"></a>
The date and time (in Unix time) that the solution update was last updated.  
Type: Timestamp  
Required: No

 ** performAutoTraining **   <a name="personalize-Type-SolutionUpdateSummary-performAutoTraining"></a>
Whether the solution automatically creates solution versions.  
Type: Boolean  
Required: No

 ** performIncrementalUpdate **   <a name="personalize-Type-SolutionUpdateSummary-performIncrementalUpdate"></a>
A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, incremental training is performed for solution versions with active campaigns and allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe. The default is `true`.  
Note that certain scores and attributes (like updates to item popularity and freshness used for ranking influence with aws-semantic-similarity recipe) may not update until the next full training occurs.   
Type: Boolean  
Required: No

 ** solutionUpdateConfig **   <a name="personalize-Type-SolutionUpdateSummary-solutionUpdateConfig"></a>
The configuration details of the solution.  
Type: [SolutionUpdateConfig](API_SolutionUpdateConfig.md) object  
Required: No

 ** status **   <a name="personalize-Type-SolutionUpdateSummary-status"></a>
The status of the solution update. A solution update can be in one of the following states:  
CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_SolutionUpdateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/SolutionUpdateSummary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/SolutionUpdateSummary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/SolutionUpdateSummary) 