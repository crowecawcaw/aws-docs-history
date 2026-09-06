

# Actions, resources, and condition keys for Amazon Machine Learning
<a name="list_machinelearning"></a>

Amazon Machine Learning (service prefix: `machinelearning`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/machine-learning/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/machine-learning/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/machine-learning/latest/dg/controlling-access-to-amazon-ml-resources-by-using-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/machinelearning/machinelearning.json) for this service.

**Topics**
+ [API operations defined by Amazon Machine Learning](#list_machinelearning-operations)
+ [Actions defined by Amazon Machine Learning](#list_machinelearning-actions-as-permissions)
+ [Resource types defined by Amazon Machine Learning](#list_machinelearning-resources-for-iam-policies)
+ [Condition keys for Amazon Machine Learning](#list_machinelearning-policy-keys)

## API operations defined by Amazon Machine Learning
<a name="list_machinelearning-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_machinelearning-actions-as-permissions).




- **   AddTags  **
  - **IAM action:**  [machinelearning:AddTags](#list_machinelearning-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   CreateBatchPrediction  **
  - **IAM action:**  [machinelearning:CreateBatchPrediction](#list_machinelearning-action-CreateBatchPrediction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateDataSourceFromRedshift  **
  - **IAM action:**  [machinelearning:CreateDataSourceFromRedshift](#list_machinelearning-action-CreateDataSourceFromRedshift)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDataSourceFromS3  **
  - **IAM action:**  [machinelearning:CreateDataSourceFromS3](#list_machinelearning-action-CreateDataSourceFromS3) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateEvaluation  **
  - **IAM action:**  [machinelearning:CreateEvaluation](#list_machinelearning-action-CreateEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateMLModel  **
  - **IAM action:**  [machinelearning:CreateMLModel](#list_machinelearning-action-CreateMLModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRealtimeEndpoint  **
  - **IAM action:**  [machinelearning:CreateRealtimeEndpoint](#list_machinelearning-action-CreateRealtimeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteBatchPrediction  **
  - **IAM action:**  [machinelearning:DeleteBatchPrediction](#list_machinelearning-action-DeleteBatchPrediction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [machinelearning:DeleteDataSource](#list_machinelearning-action-DeleteDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEvaluation  **
  - **IAM action:**  [machinelearning:DeleteEvaluation](#list_machinelearning-action-DeleteEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteMLModel  **
  - **IAM action:**  [machinelearning:DeleteMLModel](#list_machinelearning-action-DeleteMLModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteRealtimeEndpoint  **
  - **IAM action:**  [machinelearning:DeleteRealtimeEndpoint](#list_machinelearning-action-DeleteRealtimeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeBatchPredictions  **
  - **IAM action:**  [machinelearning:DescribeBatchPredictions](#list_machinelearning-action-DescribeBatchPredictions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeDataSources  **
  - **IAM action:**  [machinelearning:DescribeDataSources](#list_machinelearning-action-DescribeDataSources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeEvaluations  **
  - **IAM action:**  [machinelearning:DescribeEvaluations](#list_machinelearning-action-DescribeEvaluations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeMLModels  **
  - **IAM action:**  [machinelearning:DescribeMLModels](#list_machinelearning-action-DescribeMLModels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DescribeTags  **
  - **IAM action:**  [machinelearning:DescribeTags](#list_machinelearning-action-DescribeTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   GetBatchPrediction  **
  - **IAM action:**  [machinelearning:GetBatchPrediction](#list_machinelearning-action-GetBatchPrediction) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDataSource  **
  - **IAM action:**  [machinelearning:GetDataSource](#list_machinelearning-action-GetDataSource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetEvaluation  **
  - **IAM action:**  [machinelearning:GetEvaluation](#list_machinelearning-action-GetEvaluation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMLModel  **
  - **IAM action:**  [machinelearning:GetMLModel](#list_machinelearning-action-GetMLModel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   Predict  **
  - **IAM action:**  [machinelearning:Predict](#list_machinelearning-action-Predict) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Machine Learning
<a name="list_machinelearning-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AddTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_AddTags.html)  **
  - **Description:** Adds one or more tags to an object, up to a limit of 10. Each tag consists of a key and an optional value
  - **Resource types (\*required):** [batchprediction](#list_machinelearning-resource-batchprediction) / **Condition keys:**  
  - **Resource types (\*required):** [datasource](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [evaluation](#list_machinelearning-resource-evaluation) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [CreateBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateBatchPrediction.html)  **
  - **Description:** Generates predictions for a group of observations
  - **Resource types (\*required):** [batchprediction\*](#list_machinelearning-resource-batchprediction) / **Condition keys:**  
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataSourceFromRDS](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRDS.html)  **
  - **Description:** Creates a DataSource object from an Amazon RDS
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataSourceFromRedshift](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromRedshift.html)  **
  - **Description:** Creates a DataSource from a database hosted on an Amazon Redshift cluster
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateDataSourceFromS3](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateDataSourceFromS3.html)  **
  - **Description:** Creates a DataSource object from S3
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateEvaluation.html)  **
  - **Description:** Creates a new Evaluation of an MLModel
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [evaluation\*](#list_machinelearning-resource-evaluation) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateMLModel.html)  **
  - **Description:** Creates a new MLModel
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** Write

- **   [CreateRealtimeEndpoint](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_CreateRealtimeEndpoint.html)  **
  - **Description:** Creates a real-time endpoint for the MLModel
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteBatchPrediction.html)  **
  - **Description:** Assigns the DELETED status to a BatchPrediction, rendering it unusable
  - **Resource types (\*required):** [batchprediction\*](#list_machinelearning-resource-batchprediction)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteDataSource.html)  **
  - **Description:** Assigns the DELETED status to a DataSource, rendering it unusable
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteEvaluation.html)  **
  - **Description:** Assigns the DELETED status to an Evaluation, rendering it unusable
  - **Resource types (\*required):** [evaluation\*](#list_machinelearning-resource-evaluation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteMLModel.html)  **
  - **Description:** Assigns the DELETED status to an MLModel, rendering it unusable
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteRealtimeEndpoint](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteRealtimeEndpoint.html)  **
  - **Description:** Deletes a real time endpoint of an MLModel
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DeleteTags.html)  **
  - **Description:** Deletes the specified tags associated with an ML object. After this operation is complete, you can't recover deleted tags
  - **Resource types (\*required):** [batchprediction](#list_machinelearning-resource-batchprediction) / **Condition keys:**  
  - **Resource types (\*required):** [datasource](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [evaluation](#list_machinelearning-resource-evaluation) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** Tagging, Write

- **   [DescribeBatchPredictions](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeBatchPredictions.html)  **
  - **Description:** Returns a list of BatchPrediction operations that match the search criteria in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeDataSources](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeDataSources.html)  **
  - **Description:** Returns a list of DataSource that match the search criteria in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeEvaluations](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeEvaluations.html)  **
  - **Description:** Returns a list of DescribeEvaluations that match the search criteria in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeMLModels](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeMLModels.html)  **
  - **Description:** Returns a list of MLModel that match the search criteria in the request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeTags](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_DescribeTags.html)  **
  - **Description:** Describes one or more of the tags for your Amazon ML object
  - **Resource types (\*required):** [batchprediction](#list_machinelearning-resource-batchprediction) / **Condition keys:**  
  - **Resource types (\*required):** [datasource](#list_machinelearning-resource-datasource) / **Condition keys:**  
  - **Resource types (\*required):** [evaluation](#list_machinelearning-resource-evaluation) / **Condition keys:**  
  - **Resource types (\*required):** [mlmodel](#list_machinelearning-resource-mlmodel) / **Condition keys:**  
  - **Access level:** List

- **   [GetBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetBatchPrediction.html)  **
  - **Description:** Returns a BatchPrediction that includes detailed metadata, status, and data file information
  - **Resource types (\*required):** [batchprediction\*](#list_machinelearning-resource-batchprediction)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetDataSource.html)  **
  - **Description:** Returns a DataSource that includes metadata and data file information, as well as the current status of the DataSource
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetEvaluation.html)  **
  - **Description:** Returns an Evaluation that includes metadata as well as the current status of the Evaluation
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_GetMLModel.html)  **
  - **Description:** Returns an MLModel that includes detailed metadata, and data source information as well as the current status of the MLModel
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Read

- **   [Predict](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_Predict.html)  **
  - **Description:** Generates a prediction for the observation using the specified ML Model
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateBatchPrediction](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateBatchPrediction.html)  **
  - **Description:** Updates the BatchPredictionName of a BatchPrediction
  - **Resource types (\*required):** [batchprediction\*](#list_machinelearning-resource-batchprediction)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateDataSource.html)  **
  - **Description:** Updates the DataSourceName of a DataSource
  - **Resource types (\*required):** [datasource\*](#list_machinelearning-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateEvaluation](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateEvaluation.html)  **
  - **Description:** Updates the EvaluationName of an Evaluation
  - **Resource types (\*required):** [evaluation\*](#list_machinelearning-resource-evaluation)
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateMLModel](https://docs.aws.amazon.com/machine-learning/latest/APIReference/API_UpdateMLModel.html)  **
  - **Description:** Updates the MLModelName and the ScoreThreshold of an MLModel
  - **Resource types (\*required):** [mlmodel\*](#list_machinelearning-resource-mlmodel)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Machine Learning
<a name="list_machinelearning-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [batchprediction](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#batch-predictions)  | arn:${Partition}:machinelearning:${Region}:${Account}:batchprediction/${BatchPredictionId} |   | 
|  [datasource](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#datasources)  | arn:${Partition}:machinelearning:${Region}:${Account}:datasource/${DatasourceId} |   | 
|  [evaluation](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#evaluations)  | arn:${Partition}:machinelearning:${Region}:${Account}:evaluation/${EvaluationId} |   | 
|  [mlmodel](https://docs.aws.amazon.com/machine-learning/latest/dg/amazon-machine-learning-key-concepts.html#ml-models)  | arn:${Partition}:machinelearning:${Region}:${Account}:mlmodel/${MlModelId} |   | 

## Condition keys for Amazon Machine Learning
<a name="list_machinelearning-policy-keys"></a>

Amazon Machine Learning has no service-specific condition keys that can be used in the `Condition` element of policy statements.