AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# HealthOmics run outputs

When a WDL or CWL run completes, the outputs include an output summary file (in JSON format) that lists all the
outputs produced by the run. You can use the output summary file for these purposes:

- Programmatically determine the output files that the run generated.
- Validate that the run produced all the expected outputs.

###### Topics

- [Run output summary for WDL](#run-outputs-wdl "#run-outputs-wdl")
- [Run output summary for CWL](#run-outputs-cwl "#run-outputs-cwl")

## Run output summary for WDL

When a WDL run completes, HealthOmics creates an output summary file named **output.json**.

For each output of the workflow, there is a corresponding key/value pair in the file. The key contains the
workflow name and output name in the following format: `WorkflowName.output_name`. For a file output,
the value is an S3 URI pointing to the output location in S3 where the file is stored. For an Array[File] output,
the value is an array of S3 URIs.

The following example shows the **output.json** file for a workflow named **BWAMappingWorkflow**.

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

If the workflow produces outputs with non-file types (such as String, Int, Float, or Bool), the field value is
a JSON primitive. For example:

```
{
  "MyWorkflow.my_int_ouput": 1,
  "MyWorkflow.my_bool_output": false,
    ...
}
```

## Run output summary for CWL

When a CWL run completes, HealthOmics creates an output summary file named **outputs.json** at the
following location:

```
{my-S3outputpath}/{runId}/{run-uuid}/logs/outputs.json
```

The output summary file includes a list of outputs. Each output is a key/value pair, where the key is the name
of the output. The value is an object that includes the following properties:

- location – The fully qualified path to the output file
- basename – The filename portion of the path
- class – The type of the output, which is typically File
- size – The size of the file in bytes

In the following example, the output.json file has a list of two output files.

```
{
  "example_output": {
    "location": "{my-S3outputpath}/{runId}/{run-uuid}/out/output.txt",
    "basename": "output.txt",
    "class": "File",
    "size": 13
  },
  "another_output": {
    "location": "{my-S3outputpath}/{runId}/{run-uuid}/out/metrics.json",
    "basename": "metrics.json",
    "class": "File",
    "size": 256
  }
}
```
