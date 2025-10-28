# IAM actions for data access in Amazon Neptune

Note that Neptune data-access actions have the prefix `neptune-db:`,
whereas administrative actions in Neptune have the prefix `rds:`.

The Amazon Resource Name (ARN) for a data resource in IAM is not the same as the
ARN assigned to a cluster on creation. You must construct the ARN as shown in [Specifying data resources](iam-data-resources.md "iam-data-resources.md"). Such data resource ARNs
can use wildcards to include multiple resources.

Data-access policy statements can also include the [neptune-db:QueryLanguage](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys") condition key to
restrict access by query language.

Starting with [Release: 1.2.0.0 (2022-07-21)](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
Neptune supports restricting permissions to one or more [specific Neptune actions](../../../service-authorization/latest/reference/list_amazonneptune.md "../../../service-authorization/latest/reference/list_amazonneptune.md"). This provides
more granular access control than was previously possible.

###### Important

- Changes to an IAM policy take up to 10 minutes to apply to the specified Neptune
  resources.
- IAM policies that are applied to a Neptune DB cluster apply to all instances in
  that cluster.

## _Query-based data-access actions_

###### Note

It isn't always obvious what permissions are needed to run a given query,
because queries can potentially take more than one action depending on the data that
they process. See [Using query actions](iam-data-access-policies.md#iam-data-query-actions "iam-data-access-policies.md#iam-data-query-actions") for more information.

## `neptune-db:ReadDataViaQuery`

`ReadDataViaQuery` allows the user to read data from the Neptune
database by submitting queries.

_Action groups:_ read-only, read-write.

_Action context keys:_ `neptune-db:QueryLanguage`.

_Required resources:_ database.

## `neptune-db:WriteDataViaQuery`

`WriteDataViaQuery` allows the user to write data to the Neptune
database by submitting queries.

_Action groups:_ read-write.

_Action context keys:_ `neptune-db:QueryLanguage`.

_Required resources:_ database.

## `neptune-db:DeleteDataViaQuery`

`DeleteDataViaQuery` allows the user to delete data from the Neptune
database by submitting queries.

_Action groups:_ read-write.

_Action context keys:_ `neptune-db:QueryLanguage`.

_Required resources:_ database.

## `neptune-db:GetQueryStatus`

`GetQueryStatus` allows the user to check the status of all active queries.

_Action groups:_ read-only, read-write.

_Action context keys:_ `neptune-db:QueryLanguage`.

_Required resources:_ database.

## `neptune-db:GetStreamRecords`

`GetStreamRecords` allows the user to fetch stream records from Neptune.

_Action groups:_ read-write.

_Action context keys:_ `neptune-db:QueryLanguage`.

_Required resources:_ database.

## `neptune-db:CancelQuery`

`CancelQuery` allows the user to to cancel a query.

_Action groups:_ read-write.

_Required resources:_ database.

## _General data-access actions_

## `neptune-db:GetEngineStatus`

`GetEngineStatus` allows the user to check the status of the Neptune
engine.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:GetStatisticsStatus`

`GetStatisticsStatus` allows the user to check the status of statistics
being collected for the database.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:GetGraphSummary`

`GetGraphSummary` The graph summary API enables you to retrieve a
read-only summary of your graph.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:ManageStatistics`

`ManageStatistics` allows the user to to manage the collection of
statistics for the database.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:DeleteStatistics`

`DeleteStatistics` allows the user to delete all the statistics in the database.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:ResetDatabase`

`ResetDatabase` allows the user to get the token needed for a reset and
to reset the Neptune database.

_Action groups:_ read-write.

_Required resources:_ database.

## _Bulk-loader data-access actions_

## `neptune-db:StartLoaderJob`

`StartLoaderJob` allows the user to start a bulk-loader job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:GetLoaderJobStatus`

`GetLoaderJobStatus` allows the user to check the status of a
bulk-loader job.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:ListLoaderJobs`

`ListLoaderJobs` allows the user to list all the bulk-loader jobs.

_Action groups:_ list-only, read-only, read-write.

_Required resources:_ database.

## `neptune-db:CancelLoaderJob`

`CancelLoaderJob` allows the user to cancel a loader job.

_Action groups:_ read-write.

_Required resources:_ database.

## _Machine-learning data-access actions_

## `neptune-db:StartMLDataProcessingJob`

`StartMLDataProcessingJob` allows a user to start a Neptune ML data
processing job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:StartMLModelTrainingJob`

`StartMLModelTrainingJob` allows a user to start an ML model training job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:StartMLModelTransformJob`

`StartMLModelTransformJob` allows a user to start an ML model transform job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:CreateMLEndpoint`

`CreateMLEndpoint` allows a user to create a Neptune ML endpoint.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:GetMLDataProcessingJobStatus`

`GetMLDataProcessingJobStatus` allows a user to check the status of a
Neptune ML data processing job.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:GetMLModelTrainingJobStatus`

`GetMLModelTrainingJobStatus` allows a user to check the status of a
Neptune ML model training job.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:GetMLModelTransformJobStatus`

`GetMLModelTransformJobStatus` allows a user to check the status of a
Neptune ML model transform job.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:GetMLEndpointStatus`

`GetMLEndpointStatus` allows a user to check the status of a Neptune
ML endpoint.

_Action groups:_ read-only, read-write.

_Required resources:_ database.

## `neptune-db:ListMLDataProcessingJobs`

`ListMLDataProcessingJobs` allows a user to list all the Neptune ML data processing jobs.

_Action groups:_ list-only, read-only, read-write.

_Required resources:_ database.

## `neptune-db:ListMLModelTrainingJobs`

`ListMLModelTrainingJobs` allows a user to list all the Neptune ML model training jobs.

_Action groups:_ list-only, read-only, read-write.

_Required resources:_ database.

## `neptune-db:ListMLModelTransformJobs`

`ListMLModelTransformJobs` allows a user to list all the ML model transform jobs.

_Action groups:_ list-only, read-only, read-write.

_Required resources:_ database.

## `neptune-db:ListMLEndpoints`

`ListMLEndpoints` allows a user to list all the Neptune ML endpoints.

_Action groups:_ list-only, read-only, read-write.

_Required resources:_ database.

## `neptune-db:CancelMLDataProcessingJob`

`CancelMLDataProcessingJob` allows a user to cancel a Neptune ML
data processing job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:CancelMLModelTrainingJob`

`CancelMLModelTrainingJob` allows a user to cancel a Neptune ML model
training job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:CancelMLModelTransformJob`

`CancelMLModelTransformJob` allows a user to cancel a Neptune ML
model transform job.

_Action groups:_ read-write.

_Required resources:_ database.

## `neptune-db:DeleteMLEndpoint`

`DeleteMLEndpoint` allows a user to delete a Neptune ML endpoint.

_Action groups:_ read-write.

_Required resources:_ database.
