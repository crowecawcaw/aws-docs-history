

# CreateSolution
<a name="API_CreateSolution"></a>

**Important**  
By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. To avoid unnecessary costs, when you are finished you can [update the solution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html) to turn off automatic training. For information about training costs, see [Amazon Personalize pricing](https://aws.amazon.com/personalize/pricing/).

Creates the configuration for training a model (creating a solution version). This configuration includes the recipe to use for model training and optional training configuration, such as columns to use in training and feature transformation parameters. For more information about configuring a solution, see [Creating and configuring a solution](https://docs.aws.amazon.com/personalize/latest/dg/customizing-solution-config.html). 

 By default, new solutions use automatic training to create solution versions every 7 days. You can change the training frequency. Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training. For more information, see [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html).

 To turn off automatic training, set `performAutoTraining` to false. If you turn off automatic training, you must manually create a solution version by calling the [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html) operation.

After training starts, you can get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) API operation. To get its status, use the [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html). 

After training completes you can evaluate model accuracy by calling [GetSolutionMetrics](https://docs.aws.amazon.com/personalize/latest/dg/API_GetSolutionMetrics.html). When you are satisfied with the solution version, you deploy it using [CreateCampaign](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateCampaign.html). The campaign provides recommendations to a client through the [GetRecommendations](https://docs.aws.amazon.com/personalize/latest/dg/API_RS_GetRecommendations.html) API.

**Note**  
Amazon Personalize doesn't support configuring the `hpoObjective` for solution hyperparameter optimization at this time.

 **Status** 

A solution can be in one of the following states:
+ CREATE PENDING > CREATE IN\_PROGRESS > ACTIVE -or- CREATE FAILED
+ DELETE PENDING > DELETE IN\_PROGRESS

To get the status of the solution, call [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html). If you use manual training, the status must be ACTIVE before you call `CreateSolutionVersion`.

**Related APIs**
+  [UpdateSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_UpdateSolution.html) 
+  [ListSolutions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutions.html) 
+  [CreateSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_CreateSolutionVersion.html) 
+  [DescribeSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolution.html) 
+  [DeleteSolution](https://docs.aws.amazon.com/personalize/latest/dg/API_DeleteSolution.html) 
+  [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) 
+  [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html) 

## Request Syntax
<a name="API_CreateSolution_RequestSyntax"></a>

```
{
   "datasetGroupArn": "{{string}}",
   "eventType": "{{string}}",
   "name": "{{string}}",
   "performAutoML": {{boolean}},
   "performAutoTraining": {{boolean}},
   "performHPO": {{boolean}},
   "performIncrementalUpdate": {{boolean}},
   "recipeArn": "{{string}}",
   "solutionConfig": { 
      "algorithmHyperParameters": { 
         "{{string}}" : "{{string}}" 
      },
      "autoMLConfig": { 
         "metricName": "{{string}}",
         "recipeList": [ "{{string}}" ]
      },
      "autoTrainingConfig": { 
         "schedulingExpression": "{{string}}"
      },
      "eventsConfig": { 
         "eventParametersList": [ 
            { 
               "eventType": "{{string}}",
               "eventValueThreshold": {{number}},
               "weight": {{number}}
            }
         ]
      },
      "eventValueThreshold": "{{string}}",
      "featureTransformationParameters": { 
         "{{string}}" : "{{string}}" 
      },
      "hpoConfig": { 
         "algorithmHyperParameterRanges": { 
            "categoricalHyperParameterRanges": [ 
               { 
                  "name": "{{string}}",
                  "values": [ "{{string}}" ]
               }
            ],
            "continuousHyperParameterRanges": [ 
               { 
                  "maxValue": {{number}},
                  "minValue": {{number}},
                  "name": "{{string}}"
               }
            ],
            "integerHyperParameterRanges": [ 
               { 
                  "maxValue": {{number}},
                  "minValue": {{number}},
                  "name": "{{string}}"
               }
            ]
         },
         "hpoObjective": { 
            "metricName": "{{string}}",
            "metricRegex": "{{string}}",
            "type": "{{string}}"
         },
         "hpoResourceConfig": { 
            "maxNumberOfTrainingJobs": "{{string}}",
            "maxParallelTrainingJobs": "{{string}}"
         }
      },
      "optimizationObjective": { 
         "itemAttribute": "{{string}}",
         "objectiveSensitivity": "{{string}}"
      },
      "trainingDataConfig": { 
         "excludedDatasetColumns": { 
            "{{string}}" : [ "{{string}}" ]
         },
         "includedDatasetColumns": { 
            "{{string}}" : [ "{{string}}" ]
         }
      }
   },
   "tags": [ 
      { 
         "tagKey": "{{string}}",
         "tagValue": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateSolution_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [datasetGroupArn](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-datasetGroupArn"></a>
The Amazon Resource Name (ARN) of the dataset group that provides the training data.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: Yes

 ** [eventType](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-eventType"></a>
When your have multiple event types (using an `EVENT_TYPE` schema field), this parameter specifies which event type (for example, 'click' or 'like') is used for training the model.  
If you do not provide an `eventType`, Amazon Personalize will use all interactions for training with equal weight regardless of type.  
Type: String  
Length Constraints: Maximum length of 256.  
Required: No

 ** [name](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-name"></a>
The name for the solution.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 63.  
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9\-_]*`   
Required: Yes

 ** [performAutoML](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-performAutoML"></a>
We don't recommend enabling automated machine learning. Instead, match your use case to the available Amazon Personalize recipes. For more information, see [Choosing a recipe](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html).
Whether to perform automated machine learning (AutoML). The default is `false`. For this case, you must specify `recipeArn`.  
When set to `true`, Amazon Personalize analyzes your training data and selects the optimal USER\_PERSONALIZATION recipe and hyperparameters. In this case, you must omit `recipeArn`. Amazon Personalize determines the optimal recipe by running tests with different values for the hyperparameters. AutoML lengthens the training process as compared to selecting a specific recipe.  
Type: Boolean  
Required: No

 ** [performAutoTraining](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-performAutoTraining"></a>
Whether the solution uses automatic training to create new solution versions (trained models). The default is `True` and the solution automatically creates new solution versions every 7 days. You can change the training frequency by specifying a `schedulingExpression` in the `AutoTrainingConfig` as part of solution configuration. For more information about automatic training, see [Configuring automatic training](https://docs.aws.amazon.com/personalize/latest/dg/solution-config-auto-training.html).  
 Automatic solution version creation starts within one hour after the solution is ACTIVE. If you manually create a solution version within the hour, the solution skips the first automatic training.   
 After training starts, you can get the solution version's Amazon Resource Name (ARN) with the [ListSolutionVersions](https://docs.aws.amazon.com/personalize/latest/dg/API_ListSolutionVersions.html) API operation. To get its status, use the [DescribeSolutionVersion](https://docs.aws.amazon.com/personalize/latest/dg/API_DescribeSolutionVersion.html).   
Type: Boolean  
Required: No

 ** [performHPO](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-performHPO"></a>
Whether to perform hyperparameter optimization (HPO) on the specified or selected recipe. The default is `false`.  
When performing AutoML, this parameter is always `true` and you should not set it to `false`.  
Type: Boolean  
Required: No

 ** [performIncrementalUpdate](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-performIncrementalUpdate"></a>
Whether to perform incremental training updates on your model. When enabled, this allows the model to learn from new data more frequently without requiring full retraining, which enables near real-time personalization. This parameter is supported only for solutions that use the semantic-similarity recipe.  
Type: Boolean  
Required: No

 ** [recipeArn](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-recipeArn"></a>
The Amazon Resource Name (ARN) of the recipe to use for model training. This is required when `performAutoML` is false. For information about different Amazon Personalize recipes and their ARNs, see [Choosing a recipe](https://docs.aws.amazon.com/personalize/latest/dg/working-with-predefined-recipes.html).   
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`   
Required: No

 ** [solutionConfig](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-solutionConfig"></a>
The configuration properties for the solution. When `performAutoML` is set to true, Amazon Personalize only evaluates the `autoMLConfig` section of the solution configuration.  
Amazon Personalize doesn't support configuring the `hpoObjective` at this time.
Type: [SolutionConfig](API_SolutionConfig.md) object  
Required: No

 ** [tags](#API_CreateSolution_RequestSyntax) **   <a name="personalize-CreateSolution-request-tags"></a>
A list of [tags](https://docs.aws.amazon.com/personalize/latest/dg/tagging-resources.html) to apply to the solution.  
Type: Array of [Tag](API_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_CreateSolution_ResponseSyntax"></a>

```
{
   "solutionArn": "string"
}
```

## Response Elements
<a name="API_CreateSolution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [solutionArn](#API_CreateSolution_ResponseSyntax) **   <a name="personalize-CreateSolution-response-solutionArn"></a>
The ARN of the solution.  
Type: String  
Length Constraints: Maximum length of 256.  
Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+` 

## Errors
<a name="API_CreateSolution_Errors"></a>

 ** InvalidInputException **   
Provide a valid value for the field or parameter.  
HTTP Status Code: 400

 ** LimitExceededException **   
The limit on the number of requests per second has been exceeded.  
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **   
The specified resource already exists.  
HTTP Status Code: 400

 ** ResourceInUseException **   
The specified resource is in use.  
HTTP Status Code: 400

 ** ResourceNotFoundException **   
Could not find the specified resource.  
HTTP Status Code: 400

 ** TooManyTagsException **   
You have exceeded the maximum number of tags you can apply to this resource.   
HTTP Status Code: 400

## See Also
<a name="API_CreateSolution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/personalize-2018-05-22/CreateSolution) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/personalize-2018-05-22/CreateSolution) 