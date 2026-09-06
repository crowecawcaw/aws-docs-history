

# Get run information
<a name="getinfo-about-runs"></a>

After you start a run, you can retrieve its status, configuration, and task-level details using the HealthOmics API. This page describes how to:

**Topics**
+ [Get run status and details](#get-run)
+ [List all runs](#list-runs)
+ [List tasks in a run](#list-tasks)
+ [Get task details](#get-task)
+ [Run metadata in CloudWatch](#run-metadata)

## Get run status and details
<a name="get-run"></a>

Use the **GetRun** API operation to check the status and retrieve details of a specific run. You need the run ID, which is returned when you start a run.

```
aws omics get-run --id {{run_id}}
```

**Finding the run ID**  
You can find the run ID in the following ways:  
From the [**StartRun** API response](starting-a-run.md#start-run-api-basic) – the `id` field is returned when you start a run.
From the HealthOmics console – on the **Runs** page, the run ID is displayed in the first column of the runs list.
From the **ListRuns** API – lists all runs in your account with their IDs.

The response includes the run status, workflow details, accelerator information, and timestamps. Possible run statuses are:


| Status | Description | 
| --- | --- | 
| PENDING | The run has been submitted and is waiting to start. | 
| STARTING | HealthOmics is provisioning resources for the run. | 
| RUNNING | The run is actively executing tasks. | 
| COMPLETED | The run finished successfully. Output files are available in the Amazon S3 output location. | 
| FAILED | The run encountered an error. See [Run failure reasons](workflows-run-errors.md). | 
| CANCELLED | The run was cancelled by the user. | 

When a run is `COMPLETED`, you can find the output files in your Amazon S3 output bucket, in a folder named after the run ID.

### Example response
<a name="get-run-example-response"></a>

The following example shows the response for a completed run of a private WDL workflow with a GPU accelerator:

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/7830534",
    "id": "7830534",
    "uuid": "96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "outputUri": "s3://amzn-s3-demo-bucket/output",
    "status": "COMPLETED",
    "workflowId": "4074992",
    "workflowType": "PRIVATE",
    "workflowVersionName": "3.0.0",
    "roleArn": "arn:aws:iam::123456789012:role/OmicsRole",
    "name": "RunGroupMaxGpuTest",
    "runGroupId": "9938959",
    "digest": "sha256:a23a6fc54040d36784206234c02147302ab8658bed89860a...",
    "accelerators": "GPU",
    "startedBy": "arn:aws:sts::123456789012:assumed-role/Admin/role_name",
    "creationTime": "2023-04-07T16:44:22.262471+00:00",
    "startTime": "2023-04-07T16:56:12.504000+00:00",
    "stopTime": "2023-04-07T17:22:29.908813+00:00",
    "tags": {}
}
```

### Key fields in the response
<a name="get-run-key-fields"></a>


| Field | Description | 
| --- | --- | 
| uuid | Universally unique identifier for the run. Along with outputUri, can be used to track where output data is written. | 
| status | Current run status (see the preceding table). | 
| workflowType | Whether the workflow is PRIVATE or READY2RUN. | 
| accelerators | Accelerator type used (for example, GPU), if applicable. | 
| digest | SHA-256 digest of the workflow definition. | 
| creationTime | When the run was submitted. | 
| startTime | When the run began executing. | 
| stopTime | When the run finished or was cancelled. | 
| engineSettings | Engine settings applied to the run. This field is returned only for Nextflow workflows. If you specify engine settings for WDL or CWL workflows, they are silently ignored and this field is not present in the GetRun response. See [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings). | 

### Example response for a Nextflow run with engine settings
<a name="get-run-engine-settings-example"></a>

For Nextflow runs that were started with engine settings, the **GetRun** response includes an `engineSettings` map that reflects the values applied to the run. The following example shows a run that was started with a pinned engine version and two profiles.

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/9876543",
    "id": "9876543",
    "uuid": "1a2b3c4d-5e6f-7a8b-9c0d-1e2f3a4b5c6d",
    "status": "COMPLETED",
    "workflowId": "1122334",
    "workflowType": "PRIVATE",
    "workflowVersionName": "1.2.1",
    "roleArn": "arn:aws:iam::123456789012:role/OmicsRole",
    "name": "nextflow-rnaseq-run",
    "outputUri": "s3://amzn-s3-demo-bucket/output",
    "engineSettings": {
        "engineVersion": "26.04",
        "profile": "test,docker"
    },
    "creationTime": "2024-09-10T16:44:22.262471+00:00",
    "startTime": "2024-09-10T16:56:12.504000+00:00",
    "stopTime": "2024-09-10T17:22:29.908813+00:00",
    "tags": {}
}
```

The `engineSettings` field is returned only for Nextflow workflows. For WDL and CWL workflows, this field isn't present in the response. For more information, see [Specify Nextflow engine settings](starting-a-run.md#start-run-api-engine-settings).

## List all runs
<a name="list-runs"></a>

Use the **ListRuns** API operation to see all runs in your account:

```
aws omics list-runs
```

The response returns a paginated list of runs with summary information including run ID, name, status, and timestamps. Use the `--starting-token` parameter to retrieve additional pages.

## List tasks in a run
<a name="list-tasks"></a>

Use the **ListRunTasks** API operation to see all tasks completed within a specific run:

```
aws omics list-run-tasks --id {{run_id}}
```

The response returns a list of tasks with their status, resource allocation, and timing information.

## Get task details
<a name="get-task"></a>

Use the **GetRunTask** API operation to get detailed information about a specific task within a run:

```
aws omics get-run-task --id {{run_id}} --task-id {{task_id}}
```

The response includes task-level details such as CPU, memory allocation, container image, and task status.

## Run metadata in CloudWatch
<a name="run-metadata"></a>

After a run completes, HealthOmics sends the run metadata to CloudWatch Logs under the stream:

```
manifest/run/{{run_id}}/{{run_uuid}}
```

The manifest includes the complete run configuration, input parameters, resource digests, and task-level details. The following is an example of the manifest:

```
[
  {
    "arn": "arn:aws:omics:us-east-1:123456789012:run/1695324",
    "creationTime": "2022-08-24T19:53:55.284Z",
    "resourceDigests": {
      "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.dict": "etag:3884c62eb0e53fa92459ed9bff133ae6",
      "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.fasta": "etag:e307d81c605fb91b7720a08f00276842-388",
      "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.fasta.fai": "etag:f76371b113734a56cde236bc0372de0a",
      "s3://omics-data/intervals/hg38-mjs-whole-chr.500M.intervals": "etag:27fdd1341246896721ec49a46a575334",
      "s3://omics-data/workflow-input-lists/dragen-gvcf-list.txt": "etag:e22f5aeed0b350a66696d8ffae453227"
    },
    "digest": "sha256:a5baaff84dd54085eb03f78766b0a367e93439486bc3f67de42bb38b93304964",
    "engine": "WDL",
    "main": "gatk4-basic-joint-genotyping-v2.wdl",
    "name": "1044-gvcfs",
    "outputUri": "s3://omics-data/workflow-output",
    "parameters": {
      "callset_name": "cohort",
      "input_gvcf_uris": "s3://omics-data/workflow-input-lists/dragen-gvcf-list.txt",
      "interval_list": "s3://omics-data/intervals/hg38-mjs-whole-chr.500M.intervals",
      "ref_dict": "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.dict",
      "ref_fasta": "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.fasta",
      "ref_fasta_index": "s3://omics-data/broad-references/hg38/v0/Homo_sapiens_assembly38.fasta.fai"
    },
    "roleArn": "arn:aws:iam::123456789012:role/OmicsServiceRole",
    "startedBy": "arn:aws:sts::123456789012:assumed-role/admin/ahenroid-Isengard",
    "startTime": "2022-08-24T20:08:22.582Z",
    "status": "COMPLETED",
    "stopTime": "2022-08-24T20:08:22.582Z",
    "storageCapacity": 9600,
    "uuid": "a3b0ca7e-9597-4ecc-94a4-6ed45481aeab",
    "workflow": "arn:aws:omics:us-east-1:123456789012:workflow/1558364",
    "workflowType": "PRIVATE"
  },
  {
    "arn": "arn:aws:omics:us-east-1:123456789012:task/1245938",
    "cpus": 16,
    "creationTime": "2022-08-24T20:06:32.971290",
    "image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/gatk",
    "imageDigest": "sha256:8051adab0ff725e7e9c2af5997680346f3c3799b2df3785dd51d4abdd3da747b",
    "memory": 32,
    "name": "geno-123",
    "run": "arn:aws:omics:us-east-1:123456789012:run/1695324",
    "startTime": "2022-08-24T20:08:22.278Z",
    "status": "SUCCESS",
    "stopTime": "2022-08-24T20:08:22.278Z",
    "uuid": "44c1a30a-4eee-426d-88ea-1af403858f76"
  },
  ...
]
```

For more information about logs available in CloudWatch for HealthOmics runs, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md).

**Note**  
Run metadata is not deleted from CloudWatch Logs even when you remove the run from HealthOmics. You can use CloudWatch to access metadata for runs that are no longer available through the HealthOmics API.