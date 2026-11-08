

# HealthOmics run outputs
<a name="workflows-run-outputs"></a>

When a run completes, HealthOmics exports the run outputs to the Amazon S3 output location (`outputUri`) that you specify when you start the run. By default, HealthOmics writes your workflow outputs under prefixes that it adds within the output URI you specify: a prefix named after the run ID, and for WDL and CWL workflows, an `out` prefix. These prefixes keep runs that use the same output URI from overwriting each other. You can choose to write the outputs directly under your output URI, without these prefixes.

WDL and CWL runs also produce an output summary file that lists the outputs of the run. For more information, see [Run output summary file](#run-output-summary-file).

**Topics**
+ [Run output location](#run-output-location)
+ [Avoid overwriting run outputs](#avoid-overwriting-run-outputs)
+ [Run output summary file](#run-output-summary-file)

## Run output location
<a name="run-output-location"></a>

You control the output location for a run with the `outputUriPrefixMode` parameter of the `StartRun` API operation. This parameter is optional. If you don't specify it, HealthOmics uses `SERVICE_DEFINED`. The parameter has the following values:
+ **`SERVICE_DEFINED`** – (Default) HealthOmics writes the outputs under a prefix named after the run ID. For WDL and CWL workflows, the outputs are also under an `out` prefix.
+ **`NONE_WITH_OVERWRITE`** – HealthOmics writes the outputs directly to the output location, with no run ID or `out` prefix. The output paths are the paths that your workflow definition specifies. If your run writes an output to an object key that already exists in the output location, HealthOmics overwrites the existing object. An object key is the object's full name in the bucket, such as `results/SAMPLES/SAMPLE1/metrics.txt`. For more information, see [Avoid overwriting run outputs](#avoid-overwriting-run-outputs).

Batch runs don't support `outputUriPrefixMode`. Runs that you start with `StartRunBatch` use `SERVICE_DEFINED`.

The following table shows where HealthOmics writes the outputs, the run logs, and the output summary file for each output URI prefix mode. In the table, `{outputUri}` is the output location (`outputUri`) that you specify when you start the run. For more information about the output location, see [Start a run in HealthOmics](starting-a-run.md).


| Item | `SERVICE_DEFINED` (default) | `NONE_WITH_OVERWRITE` | 
| --- | --- | --- | 
| WDL outputs | `{outputUri}/{runId}/out/` | `{outputUri}/` | 
| CWL outputs | `{outputUri}/{runId}/out/` | `{outputUri}/` | 
| Nextflow outputs | `{outputUri}/{runId}/` | `{outputUri}/` | 
| Run logs (all languages) | `{outputUri}/{runId}/logs/` | `{outputUri}/logs/{runId}/` | 
| Output summary file (WDL and CWL) | `{outputUri}/{runId}/logs/outputs.json` | `{outputUri}/logs/{runId}/outputs.json` | 

### Layout under the output location
<a name="run-output-layout"></a>

With `NONE_WITH_OVERWRITE`, HealthOmics doesn't add the run ID and `out` prefixes. The structure below those prefixes is the same with both output URI prefix modes. For example, a CWL workflow, or a WDL workflow that declares a `Directory` output, writes a file named `metrics.txt` to `SAMPLES/SAMPLE1/`, and the output location is `s3://amzn-s3-demo-bucket/results/`. The following example shows where the file is written with each mode.

```
SERVICE_DEFINED:      s3://amzn-s3-demo-bucket/results/1234567/out/SAMPLES/SAMPLE1/metrics.txt
NONE_WITH_OVERWRITE:  s3://amzn-s3-demo-bucket/results/SAMPLES/SAMPLE1/metrics.txt
```

### Set the output prefix mode
<a name="run-output-set-prefix-mode"></a>

To write the outputs directly to the output location, set the output prefix mode when you start the run.

**Console**

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/) and choose **Start run**.

1. On the **Specify run details** page, for **Output URI prefix mode**, choose **None, with overwrite**.

1. Complete the remaining steps and start the run.

To keep the default layout, leave **Service defined** selected. For the other settings on this page, see [Starting a run using the console](starting-a-run.md#starting-a-run-console).

**AWS CLI**

Set `outputUriPrefixMode` when you start the run. The following example uses the AWS CLI.

```
aws omics start-run \
  --workflow-id {{1234567}} \
  --role-arn arn:aws:iam::{{111122223333}}:role/{{OmicsWorkflowRole}} \
  --output-uri s3://{{amzn-s3-demo-bucket}}/{{results}}/ \
  --output-uri-prefix-mode NONE_WITH_OVERWRITE \
  --parameters file://parameters.json
```

To keep the default layout, omit `--output-uri-prefix-mode` or set it to `SERVICE_DEFINED`.

### Find the outputs of a completed run
<a name="run-output-find-outputs"></a>

To find the output location of a completed run, call `GetRun`. The `runOutputUri` field contains the location where HealthOmics wrote the outputs, and the `outputUriPrefixMode` field contains the value that the run used.

## Avoid overwriting run outputs
<a name="avoid-overwriting-run-outputs"></a>

When you use `NONE_WITH_OVERWRITE`, keeping output paths unique across runs is your responsibility. If two runs write an output to the same object key in the same output location, the output from the later run replaces the earlier one. To avoid losing outputs, follow these recommendations.
+ **Turn on S3 Versioning** – Turn on S3 Versioning for the output bucket. If a run overwrites an object, you can restore the previous version. Without versioning, you can't recover an overwritten object. For more information, see [Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) in the *Amazon S3 User Guide*.
+ **Include a value that is unique for every run in your output paths** – Add a value that changes for every run, such as a sample ID, batch ID, or timestamp, to the output paths that your workflow specifies. You can supply the value in any of the following ways:
  + **As a run parameter** – Define a workflow parameter and use it in your output paths. You pass a different value in each `StartRun` request, without changing the workflow definition.
  + **Built in your workflow** – Construct the value from your inputs, such as the sample name in an input file.
  + **From a HealthOmics environment variable** – Each run task can read environment variables that HealthOmics sets, such as `AWS_WORKFLOW_RUN_UUID`, which is unique for every run. For the full list, see [Environment variables for HealthOmics workflows](ecr-env-vars.md).

The following examples use a run parameter (`sample_id`) and the `AWS_WORKFLOW_RUN_UUID` environment variable to build a unique output path. Each example shows only the part of the task that builds the path. The examples use the output location `s3://amzn-s3-demo-bucket/results/` and set `sample_id` to `SAMPLE1`.

------
#### [ WDL ]

Declare a `Directory` output and create the path in the task command.

```
task Analyze {
  command <<<
    mkdir -p "~{sample_id}/$AWS_WORKFLOW_RUN_UUID"
    echo "done" > "~{sample_id}/$AWS_WORKFLOW_RUN_UUID/metrics.txt"
  >>>
  output {
    Directory sample_dir = "~{sample_id}"
  }
}

workflow Example {
  ...
  output {
    Directory SAMPLES = Analyze.sample_dir
  }
}
```

The run writes `s3://amzn-s3-demo-bucket/results/SAMPLES/SAMPLE1/{run-uuid}/metrics.txt`.

In WDL workflows, use a `Directory` output to write your own structure, such as `SAMPLES/SAMPLE1/`. The `Directory` type is not available in WDL 1.0 or 1.1. For more information, see [WDL workflow definition specifics](workflow-languages-wdl.md).

------
#### [ CWL ]

Declare a `Directory` output and create the path in the tool arguments.

```
arguments:
  - |
    mkdir -p "SAMPLES/$(inputs.sample_id)/$AWS_WORKFLOW_RUN_UUID"
    echo "done" > "SAMPLES/$(inputs.sample_id)/$AWS_WORKFLOW_RUN_UUID/metrics.txt"
outputs:
  samples:
    type: Directory
    outputBinding:
      glob: "SAMPLES"
```

The run writes `s3://amzn-s3-demo-bucket/results/SAMPLES/SAMPLE1/{run-uuid}/metrics.txt`.

------
#### [ Nextflow ]

Publish the output with the `output {}` block, and build the path from the run parameter and the environment variable.

```
workflow {
  main:
  Analyze()

  publish:
  metrics = Analyze.out
}

output {
  metrics {
    path "SAMPLES/${params.sample_id}/${System.getenv('AWS_WORKFLOW_RUN_UUID')}"
  }
}
```

The run writes `s3://amzn-s3-demo-bucket/results/SAMPLES/SAMPLE1/{run-uuid}/metrics.txt`.

------

## Run output summary file
<a name="run-output-summary-file"></a>

When a WDL or CWL run completes, the outputs include an output summary file (in JSON format) that lists all the outputs produced by the run. You can use the output summary file for these purposes:
+ Programmatically determine the output files that the run generated.
+ Validate that the run produced all the expected outputs.

For the location of the file, see the table in [Run output location](#run-output-location).

### Run output summary for WDL
<a name="run-outputs-wdl"></a>

When a WDL run completes, HealthOmics creates an output summary file named `outputs.json`.

For each output of the workflow, the file has a corresponding key/value pair. The key contains the workflow name and output name in the following format: `WorkflowName.output_name`. For a file output, the value is an S3 URI that points to the output location in S3 where the file is stored. For an Array[File] output, the value is an array of S3 URIs.

The following example shows the `outputs.json` file for a workflow named `BWAMappingWorkflow`:

```
{
  "BWAMappingWorkflow.bam_indexes": [
    "s3://omics-outputs/8886192/out/bam_indexes/0/pbmc8k_S1_L007_R1_001.sorted.bam.bai",
    "s3://omics-outputs/8886192/out/bam_indexes/1/pbmc8k_S1_L008_R1_001.sorted.bam.bai"
  ],
  "BWAMappingWorkflow.mapping_stats": "s3://omics-outputs/8886192/out/mapping_stats/genome_mapping_final_stats.txt",
  "BWAMappingWorkflow.merged_bam": "s3://omics-outputs/8886192/out/merged_bam/genome_mapping.merged.bam",
  "BWAMappingWorkflow.merged_bam_index": "s3://omics-outputs/8886192/out/merged_bam_index/genome_mapping.merged.bam.bai",
  "BWAMappingWorkflow.reference_index_tar": "s3://omics-outputs/8886192/out/reference_index_tar/reference_index.tar",
  "BWAMappingWorkflow.sorted_bams": [
    "s3://omics-outputs/8886192/out/sorted_bams/0/pbmc8k_S1_L007_R1_001.sorted.bam",
    "s3://omics-outputs/8886192/out/sorted_bams/1/pbmc8k_S1_L008_R1_001.sorted.bam"
  ],
  "BWAMappingWorkflow.unmapped_bams": [
    "s3://omics-outputs/8886192/out/unmapped_bams/0/pbmc8k_S1_L007_R1_001.unmapped.bam",
    "s3://omics-outputs/8886192/out/unmapped_bams/1/pbmc8k_S1_L008_R1_001.unmapped.bam"
  ]
}
```

The following example shows part of the outputs.json file for the same workflow when the run uses NONE\_WITH\_OVERWRITE with the output location s3://omics-outputs/project-a/:

```
{
  "BWAMappingWorkflow.mapping_stats": "s3://omics-outputs/project-a/mapping_stats/genome_mapping_final_stats.txt",
  "BWAMappingWorkflow.merged_bam": "s3://omics-outputs/project-a/merged_bam/genome_mapping.merged.bam",
  "BWAMappingWorkflow.sorted_bams": [
    "s3://omics-outputs/project-a/sorted_bams/0/pbmc8k_S1_L007_R1_001.sorted.bam",
    "s3://omics-outputs/project-a/sorted_bams/1/pbmc8k_S1_L008_R1_001.sorted.bam"
  ]
}
```

If the workflow produces outputs with non-file types (such as String, Int, Float, or Bool), the field value is a JSON primitive. For example:

```
{
  "MyWorkflow.my_int_output": 1,
  "MyWorkflow.my_bool_output": false,
    ...
}
```

### Run output summary for CWL
<a name="run-outputs-cwl"></a>

When a CWL run completes, HealthOmics creates an output summary file named `outputs.json`. For the location of the file, see the table in [Run output location](#run-output-location).

The output summary file includes a list of outputs. Each output is a key/value pair, where the key is the name of the output. The value is an object that includes the following properties:
+ location – The fully qualified path to the output file
+ basename – The filename portion of the path
+ class – The type of the output, which is typically File
+ size – The size of the file in bytes

In the following example, the outputs.json file has a list of two output files:

```
{
  "example_output": {
    "location": "{my-S3outputpath}/{runId}/out/output.txt",
    "basename": "output.txt",
    "class": "File",
    "size": 13
  },
  "another_output": {
    "location": "{my-S3outputpath}/{runId}/out/metrics.json",
    "basename": "metrics.json",
    "class": "File",
    "size": 256
  }
}
```

If the run uses NONE\_WITH\_OVERWRITE, the location property contains the path directly under the output location. For example, the location of example\_output is {my-S3outputpath}/output.txt.