# Workflows

The Workflows API describes the data types and API related to creating,
updating, or viewing workflows in AWS Glue. Job run history is accessible
for 90 days for your workflow and job run.

## Data types

- [JobNodeDetails structure](#aws-glue-api-workflow-JobNodeDetails "#aws-glue-api-workflow-JobNodeDetails")
- [CrawlerNodeDetails structure](#aws-glue-api-workflow-CrawlerNodeDetails "#aws-glue-api-workflow-CrawlerNodeDetails")
- [TriggerNodeDetails structure](#aws-glue-api-workflow-TriggerNodeDetails "#aws-glue-api-workflow-TriggerNodeDetails")
- [Crawl structure](#aws-glue-api-workflow-Crawl "#aws-glue-api-workflow-Crawl")
- [Node structure](#aws-glue-api-workflow-Node "#aws-glue-api-workflow-Node")
- [Edge structure](#aws-glue-api-workflow-Edge "#aws-glue-api-workflow-Edge")
- [Workflow structure](#aws-glue-api-workflow-Workflow "#aws-glue-api-workflow-Workflow")
- [WorkflowGraph structure](#aws-glue-api-workflow-WorkflowGraph "#aws-glue-api-workflow-WorkflowGraph")
- [WorkflowRun structure](#aws-glue-api-workflow-WorkflowRun "#aws-glue-api-workflow-WorkflowRun")
- [WorkflowRunStatistics structure](#aws-glue-api-workflow-WorkflowRunStatistics "#aws-glue-api-workflow-WorkflowRunStatistics")
- [StartingEventBatchCondition structure](#aws-glue-api-workflow-StartingEventBatchCondition "#aws-glue-api-workflow-StartingEventBatchCondition")
- [Blueprint structure](#aws-glue-api-workflow-Blueprint "#aws-glue-api-workflow-Blueprint")
- [BlueprintDetails structure](#aws-glue-api-workflow-BlueprintDetails "#aws-glue-api-workflow-BlueprintDetails")
- [LastActiveDefinition structure](#aws-glue-api-workflow-LastActiveDefinition "#aws-glue-api-workflow-LastActiveDefinition")
- [BlueprintRun structure](#aws-glue-api-workflow-BlueprintRun "#aws-glue-api-workflow-BlueprintRun")

## JobNodeDetails structure

The details of a Job node present in the workflow.

###### Fields

- `JobRuns` – An array of [JobRun](aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-JobRun "aws-glue-api-jobs-runs.md#aws-glue-api-jobs-runs-JobRun") objects.

The information for the job runs represented by the job node.

## CrawlerNodeDetails structure

The details of a Crawler node present in the workflow.

###### Fields

- `Crawls` – An array of [Crawl](#aws-glue-api-workflow-Crawl "#aws-glue-api-workflow-Crawl") objects.

A list of crawls represented by the crawl node.

## TriggerNodeDetails structure

The details of a Trigger node present in the workflow.

###### Fields

- `Trigger` – A [Trigger](aws-glue-api-jobs-trigger.md#aws-glue-api-jobs-trigger-Trigger "aws-glue-api-jobs-trigger.md#aws-glue-api-jobs-trigger-Trigger") object.

The information of the trigger represented by the trigger node.

## Crawl structure

The details of a crawl in the workflow.

###### Fields

- `State` – UTF-8 string (valid values: `RUNNING` | `CANCELLING` | `CANCELLED` | `SUCCEEDED` | `FAILED` | `ERROR`).

The state of the crawler.

- `StartedOn` – Timestamp.

The date and time on which the crawl started.

- `CompletedOn` – Timestamp.

The date and time on which the crawl completed.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-uri "aws-glue-api-common.md#aws-glue-api-regex-uri").

The error message associated with the crawl.

- `LogGroup` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log group string pattern](aws-glue-api-common.md#aws-glue-api-regex-logGroup-id "aws-glue-api-common.md#aws-glue-api-regex-logGroup-id").

The log group associated with the crawl.

- `LogStream` – UTF-8 string, not less than 1 or more than 512 bytes long, matching the [Log-stream string pattern](aws-glue-api-common.md#aws-glue-api-regex-logStream-id "aws-glue-api-common.md#aws-glue-api-regex-logStream-id").

The log stream associated with the crawl.

## Node structure

A node represents an AWS Glue component (trigger, crawler,
or job) on a workflow graph.

###### Fields

- `Type` – UTF-8 string (valid values: `CRAWLER` | `JOB` | `TRIGGER`).

The type of AWS Glue component represented by the node.

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the AWS Glue component represented by the node.

- `UniqueId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique Id assigned to the node within the workflow.

- `TriggerDetails` – A [TriggerNodeDetails](#aws-glue-api-workflow-TriggerNodeDetails "#aws-glue-api-workflow-TriggerNodeDetails") object.

Details of the Trigger when the node represents a Trigger.

- `JobDetails` – A [JobNodeDetails](#aws-glue-api-workflow-JobNodeDetails "#aws-glue-api-workflow-JobNodeDetails") object.

Details of the Job when the node represents a Job.

- `CrawlerDetails` – A [CrawlerNodeDetails](#aws-glue-api-workflow-CrawlerNodeDetails "#aws-glue-api-workflow-CrawlerNodeDetails") object.

Details of the crawler when the node represents a crawler.

## Edge structure

An edge represents a directed connection between two AWS Glue components that are part of the workflow the edge belongs to.

###### Fields

- `SourceId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique of the node within the workflow where the edge starts.

- `DestinationId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The unique of the node within the workflow where the edge ends.

## Workflow structure

A workflow is a collection of multiple dependent AWS Glue jobs
and crawlers that are run to complete a complex ETL task. A workflow manages the
execution and monitoring of all its jobs and crawlers.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow.

- `Description` – UTF-8 string.

A description of the workflow.

- `DefaultRunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

A collection of properties to be used as part of each execution of the workflow.
The run properties are made available to each job in the workflow. A job can modify
the properties for the next jobs in the flow.

- `CreatedOn` – Timestamp.

The date and time when the workflow was created.

- `LastModifiedOn` – Timestamp.

The date and time when the workflow was last modified.

- `LastRun` – A [WorkflowRun](#aws-glue-api-workflow-WorkflowRun "#aws-glue-api-workflow-WorkflowRun") object.

The information about the last execution of the workflow.

- `Graph` – A [WorkflowGraph](#aws-glue-api-workflow-WorkflowGraph "#aws-glue-api-workflow-WorkflowGraph") object.

The graph representing all the AWS Glue components that belong
to the workflow as nodes and directed connections between them as edges.

- `CreationStatus` – UTF-8 string (valid values: `CREATING` | `CREATED` | `CREATION_FAILED`).

The creation status of the workflow.

- `MaxConcurrentRuns` – Number (integer).

You can use this parameter to prevent unwanted multiple updates to data,
to control costs, or in some cases, to prevent exceeding the maximum number of
concurrent runs of any of the component jobs. If you leave this parameter blank,
there is no limit to the number of concurrent workflow runs.

- `BlueprintDetails` – A [BlueprintDetails](#aws-glue-api-workflow-BlueprintDetails "#aws-glue-api-workflow-BlueprintDetails") object.

This structure indicates the details of the blueprint that this particular
workflow is created from.

## WorkflowGraph structure

A workflow graph represents the complete workflow containing all the
AWS Glue components present in the workflow and all the directed connections
between them.

###### Fields

- `Nodes` – An array of [Node](#aws-glue-api-workflow-Node "#aws-glue-api-workflow-Node") objects.

A list of the the AWS Glue components belong to the workflow
represented as nodes.

- `Edges` – An array of [Edge](#aws-glue-api-workflow-Edge "#aws-glue-api-workflow-Edge") objects.

A list of all the directed connections between the nodes belonging to the
workflow.

## WorkflowRun structure

A workflow run is an execution of a workflow providing all the runtime information.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow that was run.

- `WorkflowRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of this workflow run.

- `PreviousRunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the previous workflow run.

- `WorkflowRunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

The workflow run properties which were set during the run.

- `StartedOn` – Timestamp.

The date and time when the workflow run was started.

- `CompletedOn` – Timestamp.

The date and time when the workflow run completed.

- `Status` – UTF-8 string (valid values: `RUNNING` | `COMPLETED` | `STOPPING` | `STOPPED` | `ERROR`).

The status of the workflow run.

- `ErrorMessage` – UTF-8 string.

This error message describes any error that may have occurred in starting
the workflow run. Currently the only error message is "Concurrent runs exceeded
for workflow: `foo`."

- `Statistics` – A [WorkflowRunStatistics](#aws-glue-api-workflow-WorkflowRunStatistics "#aws-glue-api-workflow-WorkflowRunStatistics") object.

The statistics of the run.

- `Graph` – A [WorkflowGraph](#aws-glue-api-workflow-WorkflowGraph "#aws-glue-api-workflow-WorkflowGraph") object.

The graph representing all the AWS Glue components that belong
to the workflow as nodes and directed connections between them as edges.

- `StartingEventBatchCondition` – A [StartingEventBatchCondition](#aws-glue-api-workflow-StartingEventBatchCondition "#aws-glue-api-workflow-StartingEventBatchCondition") object.

The batch condition that started the workflow run.

## WorkflowRunStatistics structure

Workflow run statistics provides statistics about the workflow run.

###### Fields

- `TotalActions` – Number (integer).

Total number of Actions in the workflow run.

- `TimeoutActions` – Number (integer).

Total number of Actions that timed out.

- `FailedActions` – Number (integer).

Total number of Actions that have failed.

- `StoppedActions` – Number (integer).

Total number of Actions that have stopped.

- `SucceededActions` – Number (integer).

Total number of Actions that have succeeded.

- `RunningActions` – Number (integer).

Total number Actions in running state.

- `ErroredActions` – Number (integer).

Indicates the count of job runs in the ERROR state in the workflow run.

- `WaitingActions` – Number (integer).

Indicates the count of job runs in WAITING state in the workflow run.

## StartingEventBatchCondition structure

The batch condition that started the workflow run. Either the number of
events in the batch size arrived, in which case the BatchSize member is non-zero,
or the batch window expired, in which case the BatchWindow member is non-zero.

###### Fields

- `BatchSize` – Number (integer).

Number of events in the batch.

- `BatchWindow` – Number (integer).

Duration of the batch window in seconds.

## Blueprint structure

The details of a blueprint.

###### Fields

- `Name` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `Description` – UTF-8 string, not less than 1 or more than 512 bytes long.

The description of the blueprint.

- `CreatedOn` – Timestamp.

The date and time the blueprint was registered.

- `LastModifiedOn` – Timestamp.

The date and time the blueprint was last modified.

- `ParameterSpec` – UTF-8 string, not less than 1 or more than 131072 bytes long.

A JSON string that indicates the list of parameter specifications for
the blueprint.

- `BlueprintLocation` – UTF-8 string.

Specifies the path in Amazon S3 where the blueprint is published.

- `BlueprintServiceLocation` – UTF-8 string.

Specifies a path in Amazon S3 where the blueprint is copied when you call
`CreateBlueprint/UpdateBlueprint` to register the blueprint
in AWS Glue.

- `Status` – UTF-8 string (valid values: `CREATING` | `ACTIVE` | `UPDATING` | `FAILED`).

The status of the blueprint registration.

    + Creating — The blueprint registration is in progress.
    + Active — The blueprint has been successfully registered.
    + Updating — An update to the blueprint registration is in progress.
    + Failed — The blueprint registration failed.

- `ErrorMessage` – UTF-8 string.

An error message.

- `LastActiveDefinition` – A [LastActiveDefinition](#aws-glue-api-workflow-LastActiveDefinition "#aws-glue-api-workflow-LastActiveDefinition") object.

When there are multiple versions of a blueprint and the latest version
has some errors, this attribute indicates the last successful blueprint definition
that is available with the service.

## BlueprintDetails structure

The details of a blueprint.

###### Fields

- `BlueprintName` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The run ID for this blueprint.

## LastActiveDefinition structure

When there are multiple versions of a blueprint and the latest version
has some errors, this attribute indicates the last successful blueprint definition
that is available with the service.

###### Fields

- `Description` – UTF-8 string, not less than 1 or more than 512 bytes long.

The description of the blueprint.

- `LastModifiedOn` – Timestamp.

The date and time the blueprint was last modified.

- `ParameterSpec` – UTF-8 string, not less than 1 or more than 131072 bytes long.

A JSON string specifying the parameters for the blueprint.

- `BlueprintLocation` – UTF-8 string.

Specifies a path in Amazon S3 where the blueprint is published by the AWS Glue developer.

- `BlueprintServiceLocation` – UTF-8 string.

Specifies a path in Amazon S3 where the blueprint is copied when you create
or update the blueprint.

## BlueprintRun structure

The details of a blueprint run.

###### Fields

- `BlueprintName` – UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The run ID for this blueprint run.

- `WorkflowName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of a workflow that is created as a result of a successful blueprint
run. If a blueprint run has an error, there will not be a workflow created.

- `State` – UTF-8 string (valid values: `RUNNING` | `SUCCEEDED` | `FAILED` | `ROLLING_BACK`).

The state of the blueprint run. Possible values are:

    + Running — The blueprint run is in progress.
    + Succeeded — The blueprint run completed successfully.
    + Failed — The blueprint run failed and rollback is complete.
    + Rolling Back — The blueprint run failed and rollback is in progress.

- `StartedOn` – Timestamp.

The date and time that the blueprint run started.

- `CompletedOn` – Timestamp.

The date and time that the blueprint run completed.

- `ErrorMessage` – UTF-8 string.

Indicates any errors that are seen while running the blueprint.

- `RollbackErrorMessage` – UTF-8 string.

If there are any errors while creating the entities of a workflow, we try
to roll back the created entities until that point and delete them. This attribute
indicates the errors seen while trying to delete the entities that are created.

- `Parameters` – UTF-8 string, not less than 1 or more than 131072 bytes long.

The blueprint parameters as a string. You will have to provide a value for
each key that is required from the parameter spec that is defined in the `Blueprint$ParameterSpec`.

- `RoleArn` – UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Custom string pattern #30](aws-glue-api-common.md#regex_30 "aws-glue-api-common.md#regex_30").

The role ARN. This role will be assumed by the AWS Glue service
and will be used to create the workflow and other entities of a workflow.

## Operations

- [CreateWorkflow action (Python: create_workflow)](#aws-glue-api-workflow-CreateWorkflow "#aws-glue-api-workflow-CreateWorkflow")
- [UpdateWorkflow action (Python: update_workflow)](#aws-glue-api-workflow-UpdateWorkflow "#aws-glue-api-workflow-UpdateWorkflow")
- [DeleteWorkflow action (Python: delete_workflow)](#aws-glue-api-workflow-DeleteWorkflow "#aws-glue-api-workflow-DeleteWorkflow")
- [GetWorkflow action (Python: get_workflow)](#aws-glue-api-workflow-GetWorkflow "#aws-glue-api-workflow-GetWorkflow")
- [ListWorkflows action (Python: list_workflows)](#aws-glue-api-workflow-ListWorkflows "#aws-glue-api-workflow-ListWorkflows")
- [BatchGetWorkflows action (Python: batch_get_workflows)](#aws-glue-api-workflow-BatchGetWorkflows "#aws-glue-api-workflow-BatchGetWorkflows")
- [GetWorkflowRun action (Python: get_workflow_run)](#aws-glue-api-workflow-GetWorkflowRun "#aws-glue-api-workflow-GetWorkflowRun")
- [GetWorkflowRuns action (Python: get_workflow_runs)](#aws-glue-api-workflow-GetWorkflowRuns "#aws-glue-api-workflow-GetWorkflowRuns")
- [GetWorkflowRunProperties action (Python: get_workflow_run_properties)](#aws-glue-api-workflow-GetWorkflowRunProperties "#aws-glue-api-workflow-GetWorkflowRunProperties")
- [PutWorkflowRunProperties action (Python: put_workflow_run_properties)](#aws-glue-api-workflow-PutWorkflowRunProperties "#aws-glue-api-workflow-PutWorkflowRunProperties")
- [CreateBlueprint action (Python: create_blueprint)](#aws-glue-api-workflow-CreateBlueprint "#aws-glue-api-workflow-CreateBlueprint")
- [UpdateBlueprint action (Python: update_blueprint)](#aws-glue-api-workflow-UpdateBlueprint "#aws-glue-api-workflow-UpdateBlueprint")
- [DeleteBlueprint action (Python: delete_blueprint)](#aws-glue-api-workflow-DeleteBlueprint "#aws-glue-api-workflow-DeleteBlueprint")
- [ListBlueprints action (Python: list_blueprints)](#aws-glue-api-workflow-ListBlueprints "#aws-glue-api-workflow-ListBlueprints")
- [BatchGetBlueprints action (Python: batch_get_blueprints)](#aws-glue-api-workflow-BatchGetBlueprints "#aws-glue-api-workflow-BatchGetBlueprints")
- [StartBlueprintRun action (Python: start_blueprint_run)](#aws-glue-api-workflow-StartBlueprintRun "#aws-glue-api-workflow-StartBlueprintRun")
- [GetBlueprintRun action (Python: get_blueprint_run)](#aws-glue-api-workflow-GetBlueprintRun "#aws-glue-api-workflow-GetBlueprintRun")
- [GetBlueprintRuns action (Python: get_blueprint_runs)](#aws-glue-api-workflow-GetBlueprintRuns "#aws-glue-api-workflow-GetBlueprintRuns")
- [StartWorkflowRun action (Python: start_workflow_run)](#aws-glue-api-workflow-StartWorkflowRun "#aws-glue-api-workflow-StartWorkflowRun")
- [StopWorkflowRun action (Python: stop_workflow_run)](#aws-glue-api-workflow-StopWorkflowRun "#aws-glue-api-workflow-StopWorkflowRun")
- [ResumeWorkflowRun action (Python: resume_workflow_run)](#aws-glue-api-workflow-ResumeWorkflowRun "#aws-glue-api-workflow-ResumeWorkflowRun")

## CreateWorkflow action (Python: create_workflow)

Creates a new workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name to be assigned to the workflow. It should be unique within your
account.

- `Description` – UTF-8 string, not more than 120000 bytes long.

A description of the workflow.

- `DefaultRunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

A collection of properties to be used as part of each execution of the workflow.

Run properties may be logged. Do not pass plaintext secrets as properties.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to use them
within the workflow run.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to be used with this workflow.

- `MaxConcurrentRuns` – Number (integer).

You can use this parameter to prevent unwanted multiple updates to data,
to control costs, or in some cases, to prevent exceeding the maximum number of
concurrent runs of any of the component jobs. If you leave this parameter blank,
there is no limit to the number of concurrent workflow runs.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow which was provided as part of the request.

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`

## UpdateWorkflow action (Python: update_workflow)

Updates an existing workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow to be updated.

- `Description` – UTF-8 string, not more than 120000 bytes long.

The description of the workflow.

- `DefaultRunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

A collection of properties to be used as part of each execution of the workflow.

Run properties may be logged. Do not pass plaintext secrets as properties.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to use them
within the workflow run.

- `MaxConcurrentRuns` – Number (integer).

You can use this parameter to prevent unwanted multiple updates to data,
to control costs, or in some cases, to prevent exceeding the maximum number of
concurrent runs of any of the component jobs. If you leave this parameter blank,
there is no limit to the number of concurrent workflow runs.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow which was specified in input.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## DeleteWorkflow action (Python: delete_workflow)

Deletes a workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow to be deleted.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow specified in input.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentModificationException`

## GetWorkflow action (Python: get_workflow)

Retrieves resource metadata for a workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow to retrieve.

- `IncludeGraph` – Boolean.

Specifies whether to include a graph when returning the workflow resource
metadata.

###### Response

- `Workflow` – A [Workflow](#aws-glue-api-workflow-Workflow "#aws-glue-api-workflow-Workflow") object.

The resource metadata for the workflow.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## ListWorkflows action (Python: list_workflows)

Lists names of workflows created in the account.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `MaxResults` – Number (integer), not less than 1 or more than 25.

The maximum size of a list to return.

###### Response

- `Workflows` – An array of UTF-8 strings, not less than 1 or more than 25 strings.

List of names of workflows in the account.

- `NextToken` – UTF-8 string.

A continuation token, if not all workflow names have been returned.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## BatchGetWorkflows action (Python: batch_get_workflows)

Returns a list of resource metadata for a given list of workflow names.
After calling the `ListWorkflows` operation, you can call this
operation to access the data to which you have been granted permissions. This
operation supports all IAM permissions, including permission conditions that
uses tags.

###### Request

- `Names` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 25 strings.

A list of workflow names, which may be the names returned from the `ListWorkflows`
operation.

- `IncludeGraph` – Boolean.

Specifies whether to include a graph when returning the workflow resource
metadata.

###### Response

- `Workflows` – An array of [Workflow](#aws-glue-api-workflow-Workflow "#aws-glue-api-workflow-Workflow") objects, not less than 1 or more than 25 structures.

A list of workflow resource metadata.

- `MissingWorkflows` – An array of UTF-8 strings, not less than 1 or more than 25 strings.

A list of names of workflows not found.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`

## GetWorkflowRun action (Python: get_workflow_run)

Retrieves the metadata for a given workflow run. Job run history is accessible
for 90 days for your workflow and job run.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow being run.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the workflow run.

- `IncludeGraph` – Boolean.

Specifies whether to include the workflow graph in response or not.

###### Response

- `Run` – A [WorkflowRun](#aws-glue-api-workflow-WorkflowRun "#aws-glue-api-workflow-WorkflowRun") object.

The requested workflow run metadata.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetWorkflowRuns action (Python: get_workflow_runs)

Retrieves metadata for all runs of a given workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow whose metadata of runs should be returned.

- `IncludeGraph` – Boolean.

Specifies whether to include the workflow graph in response or not.

- `NextToken` – UTF-8 string.

The maximum size of the response.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum number of workflow runs to be included in the response.

###### Response

- `Runs` – An array of [WorkflowRun](#aws-glue-api-workflow-WorkflowRun "#aws-glue-api-workflow-WorkflowRun") objects, not less than 1 or more than 1000 structures.

A list of workflow run metadata objects.

- `NextToken` – UTF-8 string.

A continuation token, if not all requested workflow runs have been returned.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetWorkflowRunProperties action (Python: get_workflow_run_properties)

Retrieves the workflow run properties which were set during the run.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow which was run.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the workflow run whose run properties should be returned.

###### Response

- `RunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

The workflow run properties which were set during the specified run.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## PutWorkflowRunProperties action (Python: put_workflow_run_properties)

Puts the specified workflow run properties for the given workflow run.
If a property already exists for the specified run, then it overrides the value
otherwise adds the property to existing properties.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Name of the workflow which was run.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the workflow run for which the run properties should be updated.

- `RunProperties` – _Required:_ A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

The properties to put for the specified run.

Run properties may be logged. Do not pass plaintext secrets as properties.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to use them
within the workflow run.

###### Response

- _No Response parameters._

###### Errors

- `AlreadyExistsException`
- `EntityNotFoundException`
- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentModificationException`

## CreateBlueprint action (Python: create_blueprint)

Registers a blueprint with AWS Glue.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `Description` – UTF-8 string, not less than 1 or more than 512 bytes long.

A description of the blueprint.

- `BlueprintLocation` – _Required:_ UTF-8 string, not less than 1 or more than 8192 bytes long, matching the [Custom string pattern #32](aws-glue-api-common.md#regex_32 "aws-glue-api-common.md#regex_32").

Specifies a path in Amazon S3 where the blueprint is published.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

The tags to be applied to this blueprint.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the name of the blueprint that was registered.

###### Errors

- `AlreadyExistsException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ResourceNumberLimitExceededException`

## UpdateBlueprint action (Python: update_blueprint)

Updates a registered blueprint.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `Description` – UTF-8 string, not less than 1 or more than 512 bytes long.

A description of the blueprint.

- `BlueprintLocation` – _Required:_ UTF-8 string, not less than 1 or more than 8192 bytes long, matching the [Custom string pattern #32](aws-glue-api-common.md#regex_32 "aws-glue-api-common.md#regex_32").

Specifies a path in Amazon S3 where the blueprint is published.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the name of the blueprint that was updated.

###### Errors

- `EntityNotFoundException`
- `ConcurrentModificationException`
- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `IllegalBlueprintStateException`

## DeleteBlueprint action (Python: delete_blueprint)

Deletes an existing blueprint.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the blueprint to delete.

###### Response

- `Name` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Returns the name of the blueprint that was deleted.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`

## ListBlueprints action (Python: list_blueprints)

Lists all the blueprint names in an account.

###### Request

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `MaxResults` – Number (integer), not less than 1 or more than 25.

The maximum size of a list to return.

- `Tags` – A map array of key-value pairs, not more than 50 pairs.

Each key is a UTF-8 string, not less than 1 or more than 128 bytes long.

Each value is a UTF-8 string, not more than 256 bytes long.

Filters the list by an AWS resource tag.

###### Response

- `Blueprints` – An array of UTF-8 strings.

List of names of blueprints in the account.

- `NextToken` – UTF-8 string.

A continuation token, if not all blueprint names have been returned.

###### Errors

- `InvalidInputException`
- `InternalServiceException`
- `OperationTimeoutException`

## BatchGetBlueprints action (Python: batch_get_blueprints)

Retrieves information about a list of blueprints.

###### Request

- `Names` – _Required:_ An array of UTF-8 strings, not less than 1 or more than 25 strings.

A list of blueprint names.

- `IncludeBlueprint` – Boolean.

Specifies whether or not to include the blueprint in the response.

- `IncludeParameterSpec` – Boolean.

Specifies whether or not to include the parameters, as a JSON string, for
the blueprint in the response.

###### Response

- `Blueprints` – An array of [Blueprint](#aws-glue-api-workflow-Blueprint "#aws-glue-api-workflow-Blueprint") objects.

Returns a list of blueprint as a `Blueprints` object.

- `MissingBlueprints` – An array of UTF-8 strings.

Returns a list of `BlueprintNames` that were not found.

###### Errors

- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`

## StartBlueprintRun action (Python: start_blueprint_run)

Starts a new run of the specified blueprint.

###### Request

- `BlueprintName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `Parameters` – UTF-8 string, not less than 1 or more than 131072 bytes long.

Specifies the parameters as a `BlueprintParameters` object.

- `RoleArn` – _Required:_ UTF-8 string, not less than 1 or more than 1024 bytes long, matching the [Custom string pattern #30](aws-glue-api-common.md#regex_30 "aws-glue-api-common.md#regex_30").

Specifies the IAM role used to create the workflow.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The run ID for this blueprint run.

###### Errors

- `InvalidInputException`
- `OperationTimeoutException`
- `InternalServiceException`
- `ResourceNumberLimitExceededException`
- `EntityNotFoundException`
- `IllegalBlueprintStateException`

## GetBlueprintRun action (Python: get_blueprint_run)

Retrieves the details of a blueprint run.

###### Request

- `BlueprintName` – _Required:_ UTF-8 string, not less than 1 or more than 128 bytes long, matching the [Custom string pattern #31](aws-glue-api-common.md#regex_31 "aws-glue-api-common.md#regex_31").

The name of the blueprint.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The run ID for the blueprint run you want to retrieve.

###### Response

- `BlueprintRun` – A [BlueprintRun](#aws-glue-api-workflow-BlueprintRun "#aws-glue-api-workflow-BlueprintRun") object.

Returns a `BlueprintRun` object.

###### Errors

- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`

## GetBlueprintRuns action (Python: get_blueprint_runs)

Retrieves the details of blueprint runs for a specified blueprint.

###### Request

- `BlueprintName` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the blueprint.

- `NextToken` – UTF-8 string.

A continuation token, if this is a continuation request.

- `MaxResults` – Number (integer), not less than 1 or more than 1000.

The maximum size of a list to return.

###### Response

- `BlueprintRuns` – An array of [BlueprintRun](#aws-glue-api-workflow-BlueprintRun "#aws-glue-api-workflow-BlueprintRun") objects.

Returns a list of `BlueprintRun` objects.

- `NextToken` – UTF-8 string.

A continuation token, if not all blueprint runs have been returned.

###### Errors

- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `InvalidInputException`

## StartWorkflowRun action (Python: start_workflow_run)

Starts a new run of the specified workflow.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow to start.

- `RunProperties` – A map array of key-value pairs.

Each key is a UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

Each value is a UTF-8 string.

The workflow run properties for the new workflow run.

Run properties may be logged. Do not pass plaintext secrets as properties.
Retrieve secrets from a AWS Glue Connection, AWS
Secrets Manager or other secret management mechanism if you intend to use them
within the workflow run.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

An Id for the new run.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ResourceNumberLimitExceededException`
- `ConcurrentRunsExceededException`

## StopWorkflowRun action (Python: stop_workflow_run)

Stops the execution of the specified workflow run.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow to stop.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the workflow run to stop.

###### Response

- _No Response parameters._

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `IllegalWorkflowStateException`

## ResumeWorkflowRun action (Python: resume_workflow_run)

Restarts selected nodes of a previous partially completed workflow run
and resumes the workflow run. The selected nodes and all nodes that are downstream
from the selected nodes are run.

###### Request

- `Name` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The name of the workflow to resume.

- `RunId` – _Required:_ UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The ID of the workflow run to resume.

- `NodeIds` – _Required:_ An array of UTF-8 strings.

A list of the node IDs for the nodes you want to restart. The nodes that are
to be restarted must have a run attempt in the original run.

###### Response

- `RunId` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine "aws-glue-api-common.md#aws-glue-api-regex-oneLine").

The new ID assigned to the resumed workflow run. Each resume of a workflow
run will have a new run ID.

- `NodeIds` – An array of UTF-8 strings.

A list of the node IDs for the nodes that were actually restarted.

###### Errors

- `InvalidInputException`
- `EntityNotFoundException`
- `InternalServiceException`
- `OperationTimeoutException`
- `ConcurrentRunsExceededException`
- `IllegalWorkflowStateException`
