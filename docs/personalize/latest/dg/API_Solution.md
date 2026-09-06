

# Solution
<a name="API_Solution"></a>

**Important**  
By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html) to turn off automatic training. For information about training costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).

An object that provides information about a solution. A solution includes the custom recipe, customized parameters, and trained models (Solution Versions) that Amazon Personalize uses to generate recommendations. 

After you create a solution, you can’t change its configuration. If you need to make changes, you can [clone the solution](https://docs.aws.amazon.com/personalize/latest/dg/cloning-solution.html) with the Amazon Personalize console or create a new one.

## Contents
<a name="API_Solution_Contents"></a>

 ** autoMLResult **   <a name="personalize-Type-Solution-autoMLResult"></a>
When `performAutoML` is true, specifies the best recipe found.  
Type: [AutoMLResult](API_AutoMLResult.md) object  
Required: No

 ** creationDateTime **   <a name="personalize-Type-Solution-creationDateTime"></a>
The creation date and time (in Unix time) of the solution.  
Type: Timestamp  
Required: No

 ** datasetGroupArn **   <a name="personalize-Type-Solution-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group that provides the training data.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** eventType **   <a name="personalize-Type-Solution-eventType"></a>
The event type (for example, 'click' or 'like') that is used for training the model. If no `eventType` is provided, Amazon Personalize uses all interactions for training with equal weight regardless of type.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-Solution-lastUpdatedDateTime"></a>
The date and time (in Unix time) that the solution was last updated.  
Type: Timestamp  
Required: No

 ** latestSolutionUpdate **   <a name="personalize-Type-Solution-latestSolutionUpdate"></a>
Provides a summary of the latest updates to the solution.  
Type: [SolutionUpdateSummary](API_SolutionUpdateSummary.md) object  
Required: No

 ** latestSolutionVersion **   <a name="personalize-Type-Solution-latestSolutionVersion"></a>
Describes the latest version of the solution, including the status and the ARN.  
Type: [SolutionVersionSummary](API_SolutionVersionSummary.md) object  
Required: No

 ** name **   <a name="personalize-Type-Solution-name"></a>
The name of the solution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: No

 ** performAutoML **   <a name="personalize-Type-Solution-performAutoML"></a>
We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see [Determining your use case.](https://docs.aws.amazon.com/personalize/latest/dg/determining-use-case.html) 
When true, Amazon Personalize performs a search for the best USER\_PERSONALIZATION recipe from the list specified in the solution configuration (`recipeArn` must not be specified). When false (the default), Amazon Personalize uses `recipeArn` for training.  
Type: Boolean  
Required: No

 ** performAutoTraining **   <a name="personalize-Type-Solution-performAutoTraining"></a>
Specifies whether the solution automatically creates solution versions. The default is `True` and the solution automatically creates new solution versions every 7 days.  
For more information about auto training, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html).  
Type: Boolean  
Required: No

 ** performHPO **   <a name="personalize-Type-Solution-performHPO"></a>
Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is `false`.  
Type: Boolean  
Required: No

 ** performIncrementalUpdate **   <a name="personalize-Type-Solution-performIncrementalUpdate"></a>
A Boolean value that indicates whether incremental training updates are performed on the model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe  
Type: Boolean  
Required: No

 ** recipeArn **   <a name="personalize-Type-Solution-recipeArn"></a>
The ARN of the recipe used to create the solution. This is required when `performAutoML` is false.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** solutionArn **   <a name="personalize-Type-Solution-solutionArn"></a>
The ARN of the solution.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** solutionConfig **   <a name="personalize-Type-Solution-solutionConfig"></a>
Describes the configuration properties for the solution.  
Type: [SolutionConfig](API_SolutionConfig.md) object  
Required: No

 ** status **   <a name="personalize-Type-Solution-status"></a>
The status of the solution.  
A solution can be in one of the following states:  
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

## See Also
<a name="API_Solution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/Solution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/Solution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/Solution) 