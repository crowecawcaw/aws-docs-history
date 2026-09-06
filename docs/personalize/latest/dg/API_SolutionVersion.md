

# SolutionVersion
<a name="API_SolutionVersion"></a>

An object that provides information about a specific version of a [Solution](https://docs.aws.amazon.com/personalize/latest/dg/API_Solution.html) in a Custom dataset group.

## Contents
<a name="API_SolutionVersion_Contents"></a>

 ** creationDateTime **   <a name="personalize-Type-SolutionVersion-creationDateTime"></a>
The date and time (in Unix time) that this version of the solution was created.  
Type: Timestamp  
Required: No

 ** datasetGroupArn **   <a name="personalize-Type-SolutionVersion-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group providing the training data.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** eventType **   <a name="personalize-Type-SolutionVersion-eventType"></a>
The event type (for example, 'click' or 'like') that is used for training the model.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** failureReason **   <a name="personalize-Type-SolutionVersion-failureReason"></a>
If training a solution version fails, the reason for the failure.  
Type: String  
Required: No

 ** lastUpdatedDateTime **   <a name="personalize-Type-SolutionVersion-lastUpdatedDateTime"></a>
The date and time (in Unix time) that the solution was last updated.  
Type: Timestamp  
Required: No

 ** name **   <a name="personalize-Type-SolutionVersion-name"></a>
The name of the solution version.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: No

 ** performAutoML **   <a name="personalize-Type-SolutionVersion-performAutoML"></a>
When true, Amazon Personalize searches for the most optimal recipe according to the solution configuration. When false (the default), Amazon Personalize uses `recipeArn`.  
Type: Boolean  
Required: No

 ** performHPO **   <a name="personalize-Type-SolutionVersion-performHPO"></a>
Whether to perform hyperparameter optimization (HPO) on the chosen recipe. The default is `false`.  
Type: Boolean  
Required: No

 ** performIncrementalUpdate **   <a name="personalize-Type-SolutionVersion-performIncrementalUpdate"></a>
Whether the solution version should perform an incremental update. When set to true, the training will process only the data that has changed since the latest training, similar to when trainingMode is set to UPDATE. This can only be used with solution versions that use the User-Personalization recipe.  
Type: Boolean  
Required: No

 ** recipeArn **   <a name="personalize-Type-SolutionVersion-recipeArn"></a>
The ARN of the recipe used in the solution.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** solutionArn **   <a name="personalize-Type-SolutionVersion-solutionArn"></a>
The ARN of the solution.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** solutionConfig **   <a name="personalize-Type-SolutionVersion-solutionConfig"></a>
Describes the configuration properties for the solution.  
Type: [SolutionConfig](API_SolutionConfig.md) object  
Required: No

 ** solutionVersionArn **   <a name="personalize-Type-SolutionVersion-solutionVersionArn"></a>
The ARN of the solution version.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** status **   <a name="personalize-Type-SolutionVersion-status"></a>
The status of the solution version.  
A solution version can be in one of the following states:  
+ CREATE PENDING
+ CREATE IN\_PROGRESS
+ ACTIVE
+ CREATE FAILED
+ CREATE STOPPING
+ CREATE STOPPED
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** trainingHours **   <a name="personalize-Type-SolutionVersion-trainingHours"></a>
The time used to train the model. You are billed for the time it takes to train a model. This field is visible only after Amazon Personalize successfully trains a model.  
Type: Double  
Valid Range: Minimum value of 0.  
Required: No

 ** trainingMode **   <a name="personalize-Type-SolutionVersion-trainingMode"></a>
The scope of training to be performed when creating the solution version. A `FULL` training considers all of the data in your dataset group. An `UPDATE` processes only the data that has changed since the latest training. Only solution versions created with the User-Personalization recipe can use `UPDATE`.   
Type: String  
Valid Values: `FULL | UPDATE | AUTOTRAIN`   
Required: No

 ** trainingType **   <a name="personalize-Type-SolutionVersion-trainingType"></a>
Whether the solution version was created automatically or manually.  
Type: String  
Valid Values: `AUTOMATIC | MANUAL`   
Required: No

 ** tunedHPOParams **   <a name="personalize-Type-SolutionVersion-tunedHPOParams"></a>
If hyperparameter optimization was performed, contains the hyperparameter values of the best performing model.  
Type: [TunedHPOParams](API_TunedHPOParams.md) object  
Required: No

## See Also
<a name="API_SolutionVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/SolutionVersion) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/SolutionVersion) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/SolutionVersion) 