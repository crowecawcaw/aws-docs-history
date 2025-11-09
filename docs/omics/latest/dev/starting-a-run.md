# Start a run in HealthOmics

When you start a run, you specify the resources that HealthOmics allocates for use during the run.

Specify the run storage type and storage amount (for static storage). To ensure data isolation and security,
HealthOmics provisions the storage at the start of each run, and deprovisions it at the end of the run. For additional
information, see [Run storage types in HealthOmics workflows](workflows-run-types.md "workflows-run-types.md").

Specify an Amazon S3 location for the output files. If you run a high volume of workflows concurrently, use separate
Amazon S3 output URIs for each workflow to avoid bucket throttling. For more information, see [Organizing objects using prefixes](../../../AmazonS3/latest/userguide/using-prefixes.md "../../../AmazonS3/latest/userguide/using-prefixes.md") in the _Amazon S3 User Guide_ and [Scale Storage Connections Horizontally](../../../whitepapers/latest/s3-optimizing-performance-best-practices/scale-storage-connections-horizontally.md "../../../whitepapers/latest/s3-optimizing-performance-best-practices/scale-storage-connections-horizontally.md") in the _Optimizing Amazon S3 Performance_
whitepaper.

You can also specify the run priority. How priority impacts the run depends on whether the run
is associated with a run group.
For additional information, see [Run priority](creating-run-groups.md#run-priority "creating-run-groups.md#run-priority").

If a workflow has one or more versions, you can specify a version when you start the run. If you don’t specify a
version, HealthOmics starts the [default workflow version](workflows-default-version.md "workflows-default-version.md").

When using the HealthOmics API, you can provide a unique request ID for each run. The request ID is an idempotency token that HealthOmics
uses to identify duplicate requests. and starts the run only once.

###### Note

You specify an IAM service role when you start a run. Optionally, the console can create the service role for you.
For more information, see [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md").

###### Topics

- [HealthOmics run parameters](#run-parameters "#run-parameters")
- [Starting a run using the console](#starting-a-run-console "#starting-a-run-console")
- [Starting a run using the API](#starting-a-run-api "#starting-a-run-api")
- [Get information about a run](#getinfo-about-runs "#getinfo-about-runs")

## HealthOmics run parameters

When you start a run, you specify run inputs in the run parameters JSON file or you can enter the parameter
values inline. For information about managing the
size of the run parameters JSON file, see [Managing run parameters size](workflows-run-inputs.md#run-input-file-options "workflows-run-inputs.md#run-input-file-options").

HealthOmics supports the following JSON types for parameter values.

| JSON type | Example key and value       | Notes                                                                                                            |
| --------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| boolean   | "b":true                    | Value is not in quotes, and all lowercase.                                                                       |
| integer   | "i":7                       | Value is not in quotes.                                                                                          |
| number    | "f":42.3                    | Value is not in quotes.                                                                                          |
| string    | "s":"characters"            | Value is in quotes. Use string type for text values and URIs.<br>The URI target must be the expected input type. |
| array     | "a":[1,2,3]                 | Value is not in quotes. Array members must each have the type defined by the input parameter.                    |
| object    | "o":{"left":"a", "right":1} | In WDL, object maps to WDL Pair, Map, or Struct                                                                  |

## Starting a run using the console

###### To start a run

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, choose **Start run**.
4. In the **Run details** panel, provide the following information
   - **Workflow source** - Choose **Owned workflow** or **Shared
     workflow**.
   - **Workflow ID** - The workflow ID associated
     with this run.
   - **Workflow version** (Optional) - Select a workflow version to use for this run. If
     you don't select a version, the run uses the workflow default version.
   - **Run name** - A distinctive name for this
     run.
   - **Run priority** (Optional) - The priority of this run. Higher numbers specify a
     higher priority, and the highest priority tasks are run first.
   - **Run storage type** - Specify the storage type here to override the default run
     storage type specified for the workflow. Static storage allocates a fixed amount of storage for the run.
     Dynamic storage scales up and down as required for each task in the run.
   - **Run storage capacity** - For static run storage, specify the amount of storage
     needed for the run. This entry overrides the default run storage amount specified for the workflow.
   - **Select S3 output destination** - The S3
     location where the run outputs will be saved.
   - **Output bucket owner's account ID** (Optional) - If your account doesn't own the
     output bucket, enter the bucket owner's AWS account ID. This information is required so that HealthOmics can
     verify the bucket ownership.
   - **Run metadata retention mode** - Choose whether to retain the metadata for all runs
     or have the system remove the oldest run metadata when your account reaches the maximum number of runs.
     For more information, see [Run retention mode for HealthOmics runs](run-retention.md "run-retention.md").

5. Under **Service role**, you can use an existing service role or create
   a new one.
6. (Optional) For **Tags**, you can assign up to 50 tags to the run.
7. Choose **Next**.
8. On the **Add parameter values** page, provide the run parameters. You can either upload a
   JSON file that specifies the parameters or manually enter the values.
9. Choose **Next**.
10. In the **Run group** panel, you can optionally specify a run group for this run. For more
    information, see [Using HealthOmics run groups](creating-run-groups.md "creating-run-groups.md").
11. In the **Run cache** panel, you can optionally specify a run cache for this run. For more
    information, see [Configuring a run with run cache using the console](workflow-cache-startrun.md#workflow-cache-startrun-console "workflow-cache-startrun.md#workflow-cache-startrun-console").
12. Choose **Review and start run**.
13. After you review the run configuration, choose **Start run**.

## Starting a run using the API

Use the **start-run** API operation to create and start a run.

The following example specifies the workflow ID and service role. This example sets the retention mode to
`REMOVE`. For more information about retention mode, see [Run retention mode for HealthOmics runs](run-retention.md "run-retention.md").

```
aws omics start-run
     --workflow-id ``workflow id`` \
     --role-arn arn:aws:iam::1234567892012:role/service-role/OmicsWorkflow-20221004T164236 \
     --name ``workflow name`` \
     --retention-mode REMOVE
```

In response, you get the following output. The `uuid` is unique to the run, and along with
`outputUri` can be used to track where output data is written.

```
{
    "arn": "arn:aws:omics:us-west-2:....:run/1234567",
    "id": "123456789",
    "uuid":"96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "outputUri":"s3://bucket/folder/8405154/96c57683-74bf-9d6d-ae7e-f09b097db14a"
    "status": "PENDING"
}
```

### Include a parameter file

If the parameter template for a workflow declares any required parameters, you can provide a local JSON file
of the inputs when you start a workflow run. The JSON file contains the exact name of each input parameter and a
value for the parameter.

Reference the input JSON file in the AWS CLI by adding `--parameters file://<input_file.json>` to
your `start-run` request. For more information about run parameters, see [HealthOmics run inputs](workflows-run-inputs.md "workflows-run-inputs.md").

### Provide a request ID

You can provide a unique `requestId` for each run. The request ID is an idempotency token that
HealthOmics uses to catch duplicate requests. It won't start a run if the request ID is a duplicate of a previous run.

If you use infrastructure (such as Lambda functions or step functions) for orchestrating run starts, best
practice is to provide a unique request ID for each StartRun request. This ensures that if your infrastructure
inadvertently starts a run that it already started, HealthOmics won't start the duplicate run. For example, if the
infrastructure is attemping to recover from an upstream error, it may rerun a script that tries to start runs
that are duplicate requests.

### Choose a workflow version

You can specify a workflow version for the run. If you don't specify a version, HealthOmics starts the run with the
default workflow version.

```
aws omics start-run
     --workflow-id ``workflow id`` \
      ...
     --workflow-version-name '1.2.1'
```

### Override the run storage type

You can override the default run storage type that was set in the workflow.

```
aws omics start-run
       --workflow-id ``workflow id`` \
        ...
       --storage-type STATIC
       --storage-capacity 2400
```

### Run a GPU workflow

You can also specify a GPU workflow ID, as shown in the following example:

```
aws omics start-run
       --workflow-id ``workflow id`` \
       --role-arn arn:aws:iam::1234567892012:role/service-role/OmicsWorkflow-20221004T164236 \
       --name GPUTestRunModel \
       --output-uri s3://amzn-s3-demo-bucket1
```

## Get information about a run

You can use the ID in the response with the **get-run** API
to check the status of a run, as shown.

```
aws omics get-run --id ``run id``
```

The response from this API operation tells you the status of the workflow run.
Possible statuses are `PENDING`, `STARTING`,
`RUNNING`, and `COMPLETED`. When a run is
`COMPLETED`, you can find an output file called
`outfile.txt` in your output Amazon S3 bucket, in a folder named
after the run ID.

The **get-run** API operation also returns other details, such as
whether the workflow is `Ready2Run` or `PRIVATE`, the workflow
engine, and accelerator details. The following example shows the response for
**get-run** for a run of a private workflow, described in WDL
with a GPU accelerator and no tags assigned to the run.

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/7830534",
    "id": "7830534",
    "uuid":"96c57683-74bf-9d6d-ae7e-f09b097db14a",
    "outputUri":"s3://bucket/folder/8405154/96c57683-74bf-9d6d-ae7e-f09b097db14a"
    "status": "COMPLETED",
    "workflowId": "4074992",
    "workflowType": "PRIVATE",
    "workflowVersionName": "3.0.0",
    "roleArn": "arn:aws:iam::123456789012:role/service-role/OmicsWorkflow-20221004T164236",
    "name": "RunGroupMaxGpuTest",
    "runGroupId": "9938959",
    "digest": "sha256:a23a6fc54040d36784206234c02147302ab8658bed89860a86976048f6cad5ac",
    "accelerators": "GPU",
    "outputUri": "s3://amzn-s3-demo-bucket1",
    "startedBy": "arn:aws:sts::123456789012:assumed-role/Admin/<role_name>",
    "creationTime": "2023-04-07T16:44:22.262471+00:00",
    "startTime": "2023-04-07T16:56:12.504000+00:00",
    "stopTime": "2023-04-07T17:22:29.908813+00:00",
    "tags": {}
}
```

You can see the status of all runs with the **list-runs** API
operation, as shown.

```
 aws omics list-runs
```

To see all the tasks completed for a specific run, use the
**list-run-tasks** API.

```
 aws omics list-run-tasks --id ``task ID``
```

To get the details of any specific task, use the get-run-task API.

```
 aws omics get-run-task --id <run_id> --task-id ``task ID``
```

After the run completes, the metadata is sent to CloudWatch under the stream
`**manifest/run/<run ID>/<run
 UUID>**`.

The following is an example of the manifest.

```
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
```

Run metadata isn't deleted if it's not present in the CloudWatch logs.
