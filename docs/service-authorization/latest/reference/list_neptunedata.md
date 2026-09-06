

# Actions, resources, and condition keys for Amazon Neptune
<a name="list_neptunedata"></a>

Amazon Neptune (service prefix: `neptune-db`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/neptune/latest/userguide/api.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/neptune/latest/userguide/iam-auth.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/neptune-db/neptune-db.json) for this service.

**Topics**
+ [Actions defined by Amazon Neptune](#list_neptunedata-actions-as-permissions)
+ [Resource types defined by Amazon Neptune](#list_neptunedata-resources-for-iam-policies)
+ [Condition keys for Amazon Neptune](#list_neptunedata-policy-keys)

## Actions defined by Amazon Neptune
<a name="list_neptunedata-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelLoaderJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelloaderjob)  **
  - **Description:** Grants permission to cancel a loader job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmldataprocessingjob)  **
  - **Description:** Grants permission to cancel an ML data processing job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmlmodeltrainingjob)  **
  - **Description:** Grants permission to cancel an ML model training job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelmlmodeltransformjob)  **
  - **Description:** Grants permission to cancel an ML model transform job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery)  **
  - **Description:** Grants permission to cancel a query
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateMLEndpoint](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#createmlendpoint)  **
  - **Description:** Grants permission to create an ML endpoint
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery)  **
  - **Description:** Grants permission to run delete data via query APIs on database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:** [neptune-db:QueryLanguage](#list_neptunedata-neptune-db_QueryLanguage)
  - **Access level:** Write

- **   [DeleteMLEndpoint](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletemlendpoint)  **
  - **Description:** Grants permission to delete an ML endpoint
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletestatistics)  **
  - **Description:** Grants permission to delete all the statistics in the database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetEngineStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getenginestatus)  **
  - **Description:** Grants permission to check the status of the Neptune engine
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGraphSummary](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getgraphsummary)  **
  - **Description:** Grants permission to get the graph summary from the database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLoaderJobStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getloaderjobstatus)  **
  - **Description:** Grants permission to check the status of a loader job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMLDataProcessingJobStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmldataprocessingjobstatus)  **
  - **Description:** Grants permission to check the status of an ML data processing job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMLEndpointStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlendpointstatus)  **
  - **Description:** Grants permission to check the status of an ML endpoint
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMLModelTrainingJobStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlmodeltrainingjobstatus)  **
  - **Description:** Grants permission to check the status of an ML model training job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMLModelTransformJobStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getmlmodeltransformjobstatus)  **
  - **Description:** Grants permission to check the status of an ML model transform job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus)  **
  - **Description:** Grants permission to check the status of all active queries
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:** [neptune-db:QueryLanguage](#list_neptunedata-neptune-db_QueryLanguage)
  - **Access level:** Read

- **   [GetStatisticsStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstatisticsstatus)  **
  - **Description:** Grants permission to check the status of statistics of the database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetStreamRecords](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstreamrecords)  **
  - **Description:** Grants permission to fetch stream records from Neptune
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:** [neptune-db:QueryLanguage](#list_neptunedata-neptune-db_QueryLanguage)
  - **Access level:** Read

- **   [ListLoaderJobs](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listloaderjobs)  **
  - **Description:** Grants permission to list all the loader jobs
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMLDataProcessingJobs](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmldataprocessingjobs)  **
  - **Description:** Grants permission to list all the ML data processing jobs
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMLEndpoints](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmlendpoints)  **
  - **Description:** Grants permission to list all the ML endpoints
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMLModelTrainingJobs](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmlmodeltrainingjobs)  **
  - **Description:** Grants permission to list all the ML model training jobs
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMLModelTransformJobs](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#listmlmodeltransformjobs)  **
  - **Description:** Grants permission to list all the ML model transform jobs
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** List

- **   [ManageStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#managestatistics)  **
  - **Description:** Grants permission to manage statistics in the database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery)  **
  - **Description:** Grants permission to run read data via query APIs on database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:** [neptune-db:QueryLanguage](#list_neptunedata-neptune-db_QueryLanguage)
  - **Access level:** Read

- **   [ResetDatabase](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#resetdatabase)  **
  - **Description:** Grants permission to get the token needed for reset and resets the Neptune database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartLoaderJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startloaderjob)  **
  - **Description:** Grants permission to start a loader job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMLDataProcessingJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmldataprocessingjob)  **
  - **Description:** Grants permission to start an ML data processing job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMLModelTrainingJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmlmodeltrainingjob)  **
  - **Description:** Grants permission to start an ML model training job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMLModelTransformJob](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#startmlmodeltransformjob)  **
  - **Description:** Grants permission to start an ML model transform job
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write

- **   [WriteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery)  **
  - **Description:** Grants permission to run write data via query APIs on database
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:** [neptune-db:QueryLanguage](#list_neptunedata-neptune-db_QueryLanguage)
  - **Access level:** Write

- **   [connect](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html)  **
  - **Description:** Grants permission to all data-access actions in engine versions prior to 1.2.0.0
  - **Resource types (\*required):** [database\*](#list_neptunedata-resource-database)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by Amazon Neptune
<a name="list_neptunedata-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [database](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-resources.html)  | arn:${Partition}:neptune-db:${Region}:${Account}:${ClusterResourceId}/\* |   | 

## Condition keys for Amazon Neptune
<a name="list_neptunedata-policy-keys"></a>

Amazon Neptune defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [neptune-db:QueryLanguage](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys)  | Filters access by graph model | String | 