

# Manage data workflows
<a name="sd-workflows"></a>

## Important data pipeline concepts in Scenario Discovery
<a name="sd-pipeline-concepts"></a>

This section covers important concepts related to data pipelines within Scenario Discovery. Data pipelines provide a managed orchestration and compute layer for workloads such as data processing, simulation, data ingestion, and enrichment jobs. You focus on writing your business logic as containerized tasks, and Scenario Discovery provisions and manages the underlying infrastructure. You bind pipelines and tasks to a workspace and define them there. Understanding these concepts enables you to use the system more efficiently.

This section describes concepts only. For setup and step-by-step instructions, see [Configure and run data pipelines](#sd-configure-run).

### Pipelines
<a name="sd-pipelines-concept"></a>

A pipeline is a series of data tasks you assemble in a directed acyclic graph (DAG). Tasks, represented as nodes in the graph, are individual units of logic. Each task performs some kind of processing on its input data and can provide output data or metadata for use by subsequent nodes. A pipeline can contain one or many nodes. You can assemble nodes in parallel, in series, or in combinations of both. Execution proceeds level by level: all tasks at a single level run until they reach a terminal state before the system proceeds to the next layer in the DAG. If any single node fails in a level, execution for the complete DAG stops.

### Enrichment
<a name="sd-enrichment-concept"></a>

Enrichment is the process by which Scenario Discovery analyzes your onboarded video data using domain-appropriate AI models to automatically extract meaningful behaviors and objects. During enrichment, Scenario Discovery recognizes common industry video data formats and applies AI-powered understanding to identify objects, events, environmental conditions, and relationships within your data. After enrichment is complete, your data becomes fully searchable and discoverable. You can then run natural-language queries, receive proactive recommendations, and use the full suite of Scenario Discovery curation capabilities.

### Pipeline execution storage
<a name="sd-pipeline-storage"></a>

Pipeline tasks can use two types of storage: shared storage and task ephemeral storage. Tasks can also read data directly from Amazon S3 through S3 mounts. Each option is exposed to the task container as a file system path, so your application can access data by using standard file system operations.

#### Shared storage
<a name="sd-ephemeral-storage"></a>

Pipeline tasks have access to shared ephemeral storage, mounted at `/var/tmp/data`. The path is also available in the `AWS_PIPELINE_SHARED_STORAGE_ROOT` environment variable. This storage is available during pipeline execution and provides shared access between tasks in the same pipeline. Data in shared storage is temporary and does not persist after the pipeline execution reaches a terminal state (succeeded, failed, or canceled).

#### Task ephemeral storage
<a name="sd-task-ephemeral-storage"></a>

Task ephemeral storage is dedicated, high-throughput local storage for intermediate processing within a single compute node. It is attached to the compute node for the duration of that compute node run. You specify the volume size and a storage class, which determines the IOPS and throughput of the volume. Scenario Discovery mounts the volume at `/var/tmp/scratch` and sets the `AWS_TASK_LOCAL_STORAGE_ROOT` environment variable. The volume is encrypted, is provisioned empty for each compute node run, and is deleted when the compute node completes. For configuration steps, see [Configure task ephemeral storage](#sd-configure-task-ephemeral).

#### S3 mounts
<a name="sd-s3-mounts-concept"></a>

An S3 mount makes the objects in an Amazon S3 access point accessible as read-only files in the task container, at `$AWS_PIPELINE_SHARED_STORAGE_ROOT/<relativePath>`. An S3 mount isn't a storage layer: data remains in Amazon S3 and is retrieved as your application reads it. You can optionally restrict the mount to a key prefix. For configuration steps, see [Mount Amazon S3 data into tasks](#sd-mount-s3).

#### Comparison
<a name="sd-storage-comparison"></a>

The following table compares the three ways a task can access data.


| Characteristic | Shared storage | Task ephemeral storage | S3 mount | 
| --- | --- | --- | --- | 
| Path in container | $AWS\_PIPELINE\_SHARED\_STORAGE\_ROOT (/var/tmp/data) | $AWS\_TASK\_LOCAL\_STORAGE\_ROOT (/var/tmp/scratch) | $AWS\_PIPELINE\_SHARED\_STORAGE\_ROOT/<relativePath> | 
| Scope | Shared by all compute nodes in a pipeline execution | Dedicated to a single compute node | The compute nodes for which the mount is configured | 
| Access | Read/write | Read/write | Read-only | 
| Configuration | Provided automatically | Optional; configured on the task | Optional; configured on the task, or on individual compute nodes when you start a pipeline execution | 
| Lifecycle | Deleted when the pipeline execution reaches a terminal state | Deleted when the compute node completes | Unmounted when the compute node completes. The source objects in Amazon S3 are unchanged. | 
| Recommended use | Exchanging data between compute nodes in a pipeline execution | High-performance temporary storage for a single compute node | Read-only access to source data in Amazon S3 without copying it | 

### Tasks
<a name="sd-tasks-concept"></a>

Tasks are the base functional unit of a Scenario Discovery data pipeline. A task is containerized software logic you use to process, retrieve, or otherwise interact with Scenario Discovery functions. You package tasks as container images, and Scenario Discovery requires the images to be accessible from Amazon Elastic Container Registry (Amazon ECR) ([https://aws.amazon.com/ecr/](https://aws.amazon.com/ecr/)).

### Environment variables
<a name="sd-environment-variables"></a>

You use environment variables in tasks and pipelines to pass parameters to containerized images upon execution. You can define environment variables at creation time and optionally modify them at execution time. You can define reusable atomic tasks with templatized runtime inputs that you can further compose into templatized pipelines. The goal is to define a series of useful processing actions once and reuse them repeatedly. Environment variables in Scenario Discovery work the same way as in traditional containerized applications.

Environment variable names must start with a letter or underscore and contain only letters, digits, and underscores (maximum 255 characters). Values can be up to 1,024 characters. Each environment variable map can contain up to 20 entries. Names that begin with `AWS_` are reserved for service-defined environment variables.

#### Service-defined environment variables
<a name="sd-service-env-vars"></a>

Scenario Discovery sets the following environment variables in every task container. We recommend that you reference storage locations through these variables rather than through hard-coded paths.


| Variable | Value | Availability | 
| --- | --- | --- | 
| AWS\_PIPELINE\_SHARED\_STORAGE\_ROOT | Path to shared storage (/var/tmp/data) | Always | 
| AWS\_TASK\_LOCAL\_STORAGE\_ROOT | Path to task ephemeral storage (/var/tmp/scratch) | Only when the task configuration includes ephemeralStorageConfiguration | 
| AWS\_PIPELINE\_EXECUTION\_ID | ID of the current pipeline execution | Always | 
| AWS\_PIPELINE\_NAME | Name of the pipeline | Always | 
| AWS\_WORKSPACE\_NAME | Name of the workspace | Always | 
| AWS\_TASK\_NAME | Name of the task that the compute node runs | Always | 
| AWS\_COMPUTE\_NODE\_NAME | Name of the compute node in the pipeline definition | Always | 

Scenario Discovery rejects any task, pipeline, or execution environment variable whose name begins with `AWS_` (case-insensitive). This ensures that the environment variables you define don't conflict with service-defined environment variables.

### Environment variable precedence
<a name="sd-env-var-precedence"></a>

The system resolves environment variables at runtime and records them in the execution instance. Precedence follows this pattern: pipeline environment variables take precedence over task environment variables, and execution-time changes take precedence over creation-time definitions. For example, suppose you define a variable called `S3_PATH` in a task called "load\_data." Next you define a pipeline called "ingest\_processing" that contains this task and defines the same `S3_PATH` environment variable. The final value used at runtime is the value from the pipeline's `S3_PATH`, not the task's `S3_PATH` value. If at execution time you change the task's `S3_PATH`, this takes precedence over the original pipeline's `S3_PATH`. And if you modify `S3_PATH` at the pipeline level at execution time, this takes precedence over any other definition of this environment variable. Service-defined environment variables are always set by Scenario Discovery and can't be overridden.

## Configure and run data pipelines
<a name="sd-configure-run"></a>

This section describes how to set up and run data pipelines. It covers the prerequisites, the configuration of S3 mounts and task ephemeral storage, and the steps to create and run tasks and pipelines in the AWS IoT SiteWise console.

### Prerequisites to using containers, tasks and pipelines
<a name="sd-pipeline-prereqs"></a>

Complete the following prerequisites before you process and ingest data with tasks and pipelines.

#### Ingest your data from Amazon S3 into AWS IoT SiteWise
<a name="sd-ingest-from-s3"></a>

You use the `CreateBulkImportJob` API to ingest MP4 video, Parquet telemetry, and OpenLABEL annotation files from Amazon S3 into AWS IoT SiteWise for Scenario Discovery. Before you can call this API, you must enable the warm tier on your account (a one-time setup per account and Region) and configure two IAM roles. AWS IoT SiteWise assumes the first role to read your S3 objects and write error reports. Your calling identity uses the second role to invoke the API and pass the service role. You define consistent aliases for each file type so Scenario Discovery can correlate video, telemetry, and annotations from the same event. You can invoke the API through the AWS CLI, the boto3 Python SDK, or raw HTTPS (signed with SigV4), and then verify job completion by polling `DescribeBulkImportJob` for a terminal status. For step-by-step instructions, IAM policy examples, request payloads, and code samples, see [CreateBulkImportJob for Scenario Discovery](sd-bulk-import.md).

#### Enrich videos for search
<a name="sd-enrich-videos"></a>

You use the `CreateEnrichmentJob` API to analyze video time-series data already ingested into AWS IoT SiteWise and generate embeddings that enable semantic (natural-language) search over events in that video. This is the natural follow-on to `CreateBulkImportJob`: after you land MP4 video in a Scenario Discovery dataset, you call `CreateEnrichmentJob` to make that video queryable. Before you submit the job, you need an active Scenario Discovery workspace and dataset containing the target video, and your calling identity must have AWS IoT SiteWise enrichment-job permissions (plus AWS KMS decrypt access if the workspace uses a customer managed key). You scope each job to a single video time series — identified by its property alias — and define a time window to process. You can invoke the API through the AWS CLI, the boto3 Python SDK, or raw HTTPS (signed with SigV4), and then verify completion by polling `DescribeEnrichmentJob` until it reaches a terminal status. For step-by-step instructions, IAM policy examples, request payloads, and code samples, see [CreateEnrichmentJob for Scenario Discovery](sd-enrichment.md).

### Mount Amazon S3 data into tasks
<a name="sd-mount-s3"></a>

An S3 mount makes the contents of an Amazon S3 access point accessible in the task container. The mount path is the shared storage root followed by the `relativePath` that you specify:

```
<mount path> = $AWS_PIPELINE_SHARED_STORAGE_ROOT/<relativePath>
```

For example, with `relativePath` set to `inputs/raw-data`, the data appears at `$AWS_PIPELINE_SHARED_STORAGE_ROOT/inputs/raw-data` (`/var/tmp/data/inputs/raw-data`). Your application reads the objects by using standard file operations, without calling Amazon S3 APIs. Scenario Discovery establishes all mounts before the container starts.

**Note**  
S3 mounts are currently available only through the Scenario Discovery API. You can't configure S3 mounts in the AWS IoT SiteWise console.

#### Where you configure mounts
<a name="sd-mount-where"></a>


| Level | Operation | Field | Accessible to | 
| --- | --- | --- | --- | 
| Task | CreateTask, UpdateTask | taskConfiguration.containerTaskConfiguration.mounts | Compute nodes that run the task | 
| Compute node, per execution | StartPipelineExecution | executionMountOverrides.computeNodes.<computeNodeName> | The specified compute node, for that execution only | 

You can't configure mounts in the pipeline definition, and you can't define a single execution-level mount that applies to all compute nodes. Execution-time mounts are specified for individual compute nodes.

Scenario Discovery matches execution overrides to task-defined mounts by name:
+ An execution override with the same name as a task-defined mount overrides that mount for that compute node and execution.
+ An execution override with a different name is added as a separate mount.

For example, suppose a task defines a mount named `rawdata`. When you start an execution, you specify two mounts for the compute node that runs this task: `rawdata`, which points to a different prefix, and `sensordata`. For that execution, the compute node uses your `rawdata` mount instead of the task-defined mount, and also has the `sensordata` mount.

Compute nodes that aren't specified in `executionMountOverrides` use their task-defined mounts without changes. Each key under `computeNodes` must match a `computeNodeName` in the pipeline definition, not a task name.

#### Mount parameters
<a name="sd-mount-parameters"></a>


| Parameter | Required | Description | Constraints | 
| --- | --- | --- | --- | 
| name | Yes | A name that identifies the mount. Scenario Discovery also uses this value to match an execution override to a task-defined mount. | Maximum 64 characters. Must be unique within the list. | 
| relativePath | Yes | The path at which the data is mounted, relative to the shared storage root ($AWS\_PIPELINE\_SHARED\_STORAGE\_ROOT). | Maximum 1,024 characters. Must be a relative path: it can't begin or end with /, contain //, or contain . or .. segments. Must be unique within the list. | 
| source.s3AccessPoint.accessPointArn | Yes | The Amazon Resource Name (ARN) of the Amazon S3 access point to mount. | Must be an S3 access point ARN. Bucket names and bucket ARNs aren't accepted. | 
| source.s3AccessPoint.prefix | No | An object key prefix. If specified, only objects whose keys begin with this prefix are accessible. To mount all objects in the access point, omit this parameter. | 1–1,024 characters | 
| storageType | Yes | The storage in which the mount is created. Currently, mounts can be created only in shared storage. | Must be SHARED\_STORAGE. | 

Each compute node supports a maximum of 5 mounts, after task-defined mounts and execution overrides are combined.

#### Behavior
<a name="sd-mount-behavior"></a>
+ **Read-only access.** The container can't create, modify, or delete files in a mount. Write output to shared storage, task ephemeral storage, or Amazon S3.
+ **On-demand retrieval.** Objects are retrieved from Amazon S3 when your application reads them. Data isn't copied in advance.
+ **Scope.** A mount is accessible only to the compute nodes for which it is configured. To make the same data available to multiple compute nodes, configure the mount in each corresponding task, or specify it for each compute node in `executionMountOverrides`.
+ **Pricing.** Scenario Discovery doesn't charge for S3 mounts. Standard Amazon S3 charges for requests and data transfer apply when your tasks read mounted objects.

#### Permissions
<a name="sd-mount-permissions"></a>

Scenario Discovery assumes the task's `taskExecutionRole` to read the mounted data. For the trust policy that this role requires, see [Step 3: Configure the container image and execution role](#sd-step3-configure-container). In addition, the role must meet these requirements:

1. Its permissions policy allows `s3:ListBucket` and `s3:GetObject` through the access point.

1. The access point policy and bucket policy, if any, also allow the role.

1. If the bucket uses SSE-KMS, the role has `kms:Decrypt` on the key.

#### Troubleshooting S3 mounts
<a name="sd-mount-troubleshooting"></a>

If an S3 mount can't be set up, the compute node fails. In the `DescribePipelineExecution` response, the compute node's `stateDetails.code` is `EXECUTION_ERROR`, and `stateDetails.message` describes the cause. The following table describes these messages.


| Message begins with | Cause and resolution | 
| --- | --- | 
| S3 mount setup could not assume the task role. | Scenario Discovery couldn't assume the taskExecutionRole. Verify that the role's trust policy allows AWS IoT SiteWise to assume it. For more information, see [Step 3: Configure the container image and execution role](#sd-step3-configure-container). | 
| S3 denied access to the access point. | The role doesn't have permission to read from the access point. Grant the s3:GetObject and s3:ListBucket permissions, and verify the access point policy, bucket policy, and AWS KMS key policy. | 
| The specified S3 bucket or access point does not exist | The specified access point or its bucket doesn't exist, or the ARN isn't valid. | 

### Configure task ephemeral storage
<a name="sd-configure-task-ephemeral"></a>

Task ephemeral storage provides a dedicated, high-performance volume for the duration of a single compute node run. Use it for intermediate data that doesn't need to persist after the compute node completes, such as decompressed archives, extracted video frames, or temporary model files.

#### Configuration
<a name="sd-ephemeral-config"></a>

To configure task ephemeral storage, specify `ephemeralStorageConfiguration` in `taskConfiguration.containerTaskConfiguration` when you call `CreateTask` or `UpdateTask`.


| Parameter | Required | Description | 
| --- | --- | --- | 
| storageClass | Yes | The performance tier of the volume, which determines its IOPS and throughput. | 
| storageSizeInGiB | Yes | The size of the volume, in GiB. Valid values range from the minimum size for the storage class to 16,384. | 

#### Storage classes
<a name="sd-ephemeral-classes"></a>


| Storage class | IOPS | Throughput | File system | Minimum size | Generic compute | Hardware-accelerated (GPU) | 
| --- | --- | --- | --- | --- | --- | --- | 
| STANDARD\_1 | 8,000 | 500 MiB/s | ext4 | 16 GiB | Yes | Yes | 
| STANDARD\_2 | 16,000 | 1,000 MiB/s | ext4 | 32 GiB | Yes | No | 
| THROUGHPUT\_1 | 2,000 | 500 MiB/s | XFS | 4 GiB | Yes | Yes | 
| THROUGHPUT\_2 | 4,000 | 1,000 MiB/s | XFS | 8 GiB | Yes | No | 

We recommend `STANDARD_*` storage classes for mixed or random I/O workloads, and `THROUGHPUT_*` storage classes for large sequential read and write workloads, such as video decoding or frame extraction.

#### Behavior
<a name="sd-ephemeral-behavior"></a>
+ **Location.** The volume is mounted at `/var/tmp/scratch`, and the path is available in the `AWS_TASK_LOCAL_STORAGE_ROOT` environment variable. This variable is set only when the task configuration includes ephemeral storage.
+ **Isolation and lifecycle.** The volume is accessible only to the compute node for which it is provisioned. A new, empty volume is provisioned for each compute node run, including retries, and the volume is deleted when the compute node completes. If multiple compute nodes run the same task, each compute node gets its own volume.
+ **Encryption.** Volumes are encrypted at rest.
+ **Sizing.** Specify a size that accommodates the peak temporary storage requirement of the task.

### Process and ingest data using tasks and pipelines
<a name="sd-process-ingest-tasks-pipelines"></a>

A task runs a container (your custom code) on managed compute. A pipeline chains multiple tasks together into an automated workflow. You can use pipelines for any containerized workload, such as data processing, simulation, or data ingestion. This section uses data processing and ingestion as an example use case, and walks you through creating tasks, building a pipeline, running it, and verifying that your data was ingested.

#### Step 1: Navigate to the Tasks tab
<a name="sd-step1-tasks-tab"></a>

From your workspace, choose the **Tasks** tab. This is where you manage all your container tasks. If you haven't created any tasks yet, the list is empty.

#### Step 2: Create a new task
<a name="sd-step2-create-task"></a>

Choose **Create task** and fill in the basic details: give your task a name (for example, `transfer-s3-data`), add an optional description, and select "Container" as the task type.

#### Step 3: Configure the container image and execution role
<a name="sd-step3-configure-container"></a>

Point the task to your container image by entering its Amazon ECR URI (your image address in Amazon Elastic Container Registry). Then select the IAM role for the task. Scenario Discovery assumes this role to provide credentials to your container and to read data from S3 mounts. The role must meet these requirements:
+ Its trust policy allows the AWS IoT SiteWise service principal (`iotsitewise.amazonaws.com`) to call `sts:AssumeRole`.
+ Its permissions policy grants access to the AWS resources that your container uses, such as Amazon S3 buckets.

Example trust policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": { "Service": "iotsitewise.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

#### Step 4: Set processing parameters
<a name="sd-step4-processing-params"></a>

Choose how much compute your task needs. Select "Generic compute" for standard CPU workloads or "Hardware accelerated" for GPU tasks. Pick a processing unit size (for example, 16 units), set the startup command (for example, "python main.py"), and specify a timeout in seconds (for example, 3600 for one hour).

#### Step 5: Add environment variables
<a name="sd-step5-env-vars"></a>

Add any environment variables your container needs at runtime, such as S3 bucket paths or processing parameters. These are key-value pairs that configure how your container behaves. Variable names can't begin with `AWS_`. Scenario Discovery automatically sets service-defined variables, such as `AWS_WORKSPACE_NAME` and `AWS_PIPELINE_SHARED_STORAGE_ROOT`. For naming rules, limits, and the full list, see [Environment variables](#sd-environment-variables) and [Service-defined environment variables](#sd-service-env-vars).

#### Step 6: Review the created task
<a name="sd-step6-review-task"></a>

Choose **Create task** to finish. A green banner confirms that the task was created successfully. You can review all your settings on the task details page and use the Edit or Delete buttons if you need to make changes.

#### Step 7: Create additional tasks
<a name="sd-step7-additional-tasks"></a>

Create additional tasks as needed for your pipeline. For example, you might create a separate "ingest" task that handles data ingestion into Scenario Discovery. Each task can use a different container image and configuration.

#### Step 8: Navigate to the Pipelines tab
<a name="sd-step8-pipelines-tab"></a>

Go back to your workspace and choose the **Pipelines** tab. Choose **Create pipeline** to start building a multi-step workflow. Give your pipeline a name (for example, "ingestdatapipeline") and an optional description.

#### Step 9: Add compute nodes to the pipeline
<a name="sd-step9-add-nodes"></a>

Choose **\+ Add node** to add processing steps to your pipeline. For each node, enter a name and select the task that it runs. Compute node names must be unique within the pipeline, can be up to 64 characters, and can contain only letters, digits, hyphens (-), and underscores (\_). The task must already exist in the workspace, and multiple nodes can run the same task. A pipeline can contain up to 50 compute nodes. The compute node name is available to the container in the `AWS_COMPUTE_NODE_NAME` environment variable, and you use it to specify execution-time S3 mounts (see [Mount Amazon S3 data into tasks](#sd-mount-s3)). You can add multiple nodes to chain tasks together (for example, first process data from an S3 mount, then ingest it into Scenario Discovery).

#### Step 10: Define the pipeline graph and dependencies
<a name="sd-step10-define-dag"></a>

The visual editor shows your pipeline as a flowchart. Connect nodes with arrows to define the execution order. For example, the processing node runs first, and the ingestion node starts only after it completes. Choose **Create pipeline** when your graph looks correct.

#### Step 11: Review the created pipeline
<a name="sd-step11-review-pipeline"></a>

After you create the pipeline, the pipeline details page confirms that it is active and shows its structure. You can see the node graph, execution history, and use the buttons at the top to edit, delete, monitor, or execute the pipeline.

#### Step 12: Monitor pipeline execution
<a name="sd-step12-monitor-execution"></a>

The monitoring screen shows your pipeline's progress in real time. Each node is color-coded: blue means running, green means completed, and red means failed. Choose any node to see its details and access logs for troubleshooting.

You can monitor the data pipeline by choosing **Monitor**. The Monitor tab shows the execution history of the particular pipeline over time. You can see how long different nodes in the pipeline take to execute, the number of successful executions, failed executions, and when the pipeline was last executed. Additionally, the monitor window gives you an indication of average execution time per node over many runs throughout the pipeline usage.

#### Step 13: Verify pipeline completion
<a name="sd-step13-verify-pipeline"></a>

After the pipeline finishes, go back to the Pipelines tab to confirm that it ran successfully. Your pipeline is listed with its status, and you can re-run it anytime.

#### Step 14: Verify session datasets
<a name="sd-step14-verify-session-datasets"></a>

After ingestion completes, check the **Session datasets** tab in your workspace to confirm your data is now available. You should see your recordings listed with an ACTIVE status.