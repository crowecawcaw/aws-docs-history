

# IAM actions for data access in Amazon Neptune
<a name="iam-dp-actions"></a>

Note that Neptune data-access actions have the prefix `neptune-db:`, whereas administrative actions in Neptune have the prefix `rds:`.

The Amazon Resource Name (ARN) for a data resource in IAM is not the same as the ARN assigned to a cluster on creation. You must construct the ARN as shown in [Specifying data resources](iam-data-resources.md). Such data resource ARNs can use wildcards to include multiple resources.

Data-access policy statements can also include the [neptune-db:QueryLanguage](iam-data-condition-keys.md#iam-neptune-condition-keys) condition key to restrict access by query language.

Starting with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.0.md), Neptune supports restricting permissions to one or more [specific Neptune actions](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonneptune.html). This provides more granular access control than was previously possible.

**Important**  
Changes to an IAM policy take up to 10 minutes to apply to the specified Neptune resources.
IAM policies that are applied to a Neptune DB cluster apply to all instances in that cluster.

## *Query-based data-access actions*
<a name="iam-dp-actions-queries"></a>

**Note**  
It isn't always obvious what permissions are needed to run a given query, because queries can potentially take more than one action depending on the data that they process. See [Using query actions](iam-data-access-policies.md#iam-data-query-actions) for more information.

## `neptune-db:ReadDataViaQuery`
<a name="readdataviaquery"></a>

`ReadDataViaQuery` allows the user to read data from the Neptune database by submitting queries.

*Action groups:* read-only, read-write.

*Action context keys:* `neptune-db:QueryLanguage`.

*Required resources:* database.

## `neptune-db:WriteDataViaQuery`
<a name="writedataviaquery"></a>

`WriteDataViaQuery` allows the user to write data to the Neptune database by submitting queries.

*Action groups:* read-write.

*Action context keys:* `neptune-db:QueryLanguage`.

*Required resources:* database.

## `neptune-db:DeleteDataViaQuery`
<a name="deletedataviaquery"></a>

`DeleteDataViaQuery` allows the user to delete data from the Neptune database by submitting queries.

*Action groups:* read-write.

*Action context keys:* `neptune-db:QueryLanguage`.

*Required resources:* database.

## `neptune-db:GetQueryStatus`
<a name="getquerystatus"></a>

`GetQueryStatus` allows the user to check the status of all active queries.

*Action groups:* read-only, read-write.

*Action context keys:* `neptune-db:QueryLanguage`.

*Required resources:* database.

## `neptune-db:GetStreamRecords`
<a name="getstreamrecords"></a>

`GetStreamRecords` allows the user to fetch stream records from Neptune.

*Action groups:* read-write.

*Action context keys:* `neptune-db:QueryLanguage`.

*Required resources:* database.

## `neptune-db:CancelQuery`
<a name="cancelquery"></a>

`CancelQuery` allows the user to to cancel a query.

*Action groups:* read-write.

*Required resources:* database.

## *General data-access actions*
<a name="iam-dp-actions-general"></a>

## `neptune-db:GetEngineStatus`
<a name="getenginestatus"></a>

`GetEngineStatus` allows the user to check the status of the Neptune engine.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:GetStatisticsStatus`
<a name="getstatisticsstatus"></a>

`GetStatisticsStatus` allows the user to check the status of statistics being collected for the database.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:GetGraphSummary`
<a name="getgraphsummary"></a>

`GetGraphSummary` The graph summary API enables you to retrieve a read-only summary of your graph.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:ManageStatistics`
<a name="managestatistics"></a>

`ManageStatistics` allows the user to to manage the collection of statistics for the database.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:DeleteStatistics`
<a name="deletestatistics"></a>

`DeleteStatistics` allows the user to delete all the statistics in the database.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:ResetDatabase`
<a name="resetdatabase"></a>

`ResetDatabase` allows the user to get the token needed for a reset and to reset the Neptune database.

*Action groups:* read-write.

*Required resources:* database.

## *Bulk-loader data-access actions*
<a name="iam-dp-actions-loader"></a>

## `neptune-db:StartLoaderJob`
<a name="startloaderjob"></a>

`StartLoaderJob` allows the user to start a bulk-loader job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:GetLoaderJobStatus`
<a name="getloaderjobstatus"></a>

`GetLoaderJobStatus` allows the user to check the status of a bulk-loader job.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:ListLoaderJobs`
<a name="listloaderjobs"></a>

`ListLoaderJobs` allows the user to list all the bulk-loader jobs.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:CancelLoaderJob`
<a name="cancelloaderjob"></a>

`CancelLoaderJob` allows the user to cancel a loader job.

*Action groups:* read-write.

*Required resources:* database.

## *Machine-learning data-access actions*
<a name="iam-dp-actions-ml"></a>

## `neptune-db:StartMLDataProcessingJob`
<a name="startmldataprocessingjob"></a>

`StartMLDataProcessingJob` allows a user to start a Neptune ML data processing job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:StartMLModelTrainingJob`
<a name="startmlmodeltrainingjob"></a>

`StartMLModelTrainingJob` allows a user to start an ML model training job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:StartMLModelTransformJob`
<a name="startmlmodeltransformjob"></a>

`StartMLModelTransformJob` allows a user to start an ML model transform job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:CreateMLEndpoint`
<a name="createmlendpoint"></a>

`CreateMLEndpoint` allows a user to create a Neptune ML endpoint.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:GetMLDataProcessingJobStatus`
<a name="getmldataprocessingjobstatus"></a>

`GetMLDataProcessingJobStatus` allows a user to check the status of a Neptune ML data processing job.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:GetMLModelTrainingJobStatus`
<a name="getmlmodeltrainingjobstatus"></a>

`GetMLModelTrainingJobStatus` allows a user to check the status of a Neptune ML model training job.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:GetMLModelTransformJobStatus`
<a name="getmlmodeltransformjobstatus"></a>

`GetMLModelTransformJobStatus` allows a user to check the status of a Neptune ML model transform job.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:GetMLEndpointStatus`
<a name="getmlendpointstatus"></a>

`GetMLEndpointStatus` allows a user to check the status of a Neptune ML endpoint.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:ListMLDataProcessingJobs`
<a name="listmldataprocessingjobs"></a>

`ListMLDataProcessingJobs` allows a user to list all the Neptune ML data processing jobs.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:ListMLModelTrainingJobs`
<a name="listmlmodeltrainingjobs"></a>

`ListMLModelTrainingJobs` allows a user to list all the Neptune ML model training jobs.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:ListMLModelTransformJobs`
<a name="listmlmodeltransformjobs"></a>

`ListMLModelTransformJobs` allows a user to list all the ML model transform jobs.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:ListMLEndpoints`
<a name="listmlendpoints"></a>

`ListMLEndpoints` allows a user to list all the Neptune ML endpoints.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:CancelMLDataProcessingJob`
<a name="cancelmldataprocessingjob"></a>

`CancelMLDataProcessingJob` allows a user to cancel a Neptune ML data processing job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:CancelMLModelTrainingJob`
<a name="cancelmlmodeltrainingjob"></a>

`CancelMLModelTrainingJob` allows a user to cancel a Neptune ML model training job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:CancelMLModelTransformJob`
<a name="cancelmlmodeltransformjob"></a>

`CancelMLModelTransformJob` allows a user to cancel a Neptune ML model transform job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:DeleteMLEndpoint`
<a name="deletemlendpoint"></a>

`DeleteMLEndpoint` allows a user to delete a Neptune ML endpoint.

*Action groups:* read-write.

*Required resources:* database.

## *Export data-access actions*
<a name="iam-dp-actions-export"></a>

## `neptune-db:StartExportJob`
<a name="startexportjob"></a>

`StartExportJob` allows the user to start an export job.

*Action groups:* read-write.

*Required resources:* database.

## `neptune-db:GetExportJobStatus`
<a name="getexportjobstatus"></a>

`GetExportJobStatus` allows the user to get the status of an export job.

*Action groups:* read-only, read-write.

*Required resources:* database.

## `neptune-db:ListExportJobs`
<a name="listexportjobs"></a>

`ListExportJobs` allows the user to list all export jobs.

*Action groups:* list-only, read-only, read-write.

*Required resources:* database.

## `neptune-db:CancelExportJob`
<a name="cancelexportjob"></a>

`CancelExportJob` allows the user to cancel an export job.

*Action groups:* read-write.

*Required resources:* database.