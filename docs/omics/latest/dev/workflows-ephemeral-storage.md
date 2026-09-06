

# Ephemeral storage for HealthOmics workflow tasks
<a name="workflows-ephemeral-storage"></a>

HealthOmics provides ephemeral storage for workflow tasks using the `/tmp` directory. This storage is temporary and unique to each task in a workflow. HealthOmics allocates 16 GiB of ephemeral storage to each task instance by default. You can increase the amount of ephemeral storage allocated to individual tasks in your workflow definition, up to a maximum of 3,072 GiB per task. All data stored in `/tmp` is encrypted at rest.

**Topics**
+ [Key benefits](#ephemeral-storage-key-benefits)
+ [How ephemeral storage works](#ephemeral-storage-how-it-works)
+ [Enabling ephemeral storage](#ephemeral-storage-enable)
+ [Default storage allocation](#ephemeral-storage-default-allocation)
+ [Configuring ephemeral storage size](#ephemeral-storage-configure-size)
+ [Monitoring ephemeral storage](#ephemeral-storage-monitoring)
+ [How ephemeral storage is billed](#ephemeral-storage-billing)
+ [Considerations and limitations](#ephemeral-storage-considerations)
+ [Troubleshooting ephemeral storage](#ephemeral-storage-troubleshooting)

## Key benefits
<a name="ephemeral-storage-key-benefits"></a>
+ **Faster task execution:** Ephemeral storage may improve run performance by reducing shared file system I/O.
+ **Predictable performance:** Tasks do not compete with other concurrently running tasks for I/O bandwidth, reducing the variability and throttling associated with a shared network filesystem.
+ **Lower costs:** Faster task execution directly reduces compute time and cost for I/O bound tasks that make use of `/tmp`. For runs using Static run storage, this can reduce the amount of provisioned run storage you need. Dynamic runs require no changes.

## How ephemeral storage works
<a name="ephemeral-storage-how-it-works"></a>

When you enable ephemeral storage, HealthOmics mounts a dedicated local storage volume at `/tmp` for each workflow task instance. Ephemeral storage is intended for temporary files generated during task execution. Ephemeral storage volumes are always deleted when the task terminates. Data written to `/tmp` is not persisted, exported, or accessible to other tasks or subsequent runs.

### Where workflows write temporary files
<a name="ephemeral-storage-tmp-writes"></a>

Workflows benefit from ephemeral storage when task processes direct scratch I/O to `/tmp`. Bioinformatics workflow languages use the `/tmp` directory (and the `$TMP`, `$TMPDIR` environment variables) for temporary, short-lived intermediate files during task execution. Ensure your task commands have not mapped `$TMPDIR` to another location.

Workflow task processes that write to `/tmp` automatically use ephemeral storage when enabled, requiring no workflow changes. Workflows that do not explicitly direct scratch processes to `/tmp` will write scratch data to the working directory on the shared file system used for run storage, although tools used might take advantage of `/tmp` on ephemeral storage.

### Encryption at rest
<a name="ephemeral-storage-encryption"></a>

All ephemeral storage is encrypted at rest using a service-managed AWS KMS key. Accelerated computing instances are hardware-encrypted with a unique per-volume key that is destroyed when the instance terminates.

### Permissions
<a name="ephemeral-storage-permissions"></a>

HealthOmics manages the attachment and lifecycle of ephemeral storage volumes on your behalf. No additional IAM permissions are required in your task execution role.

## Enabling ephemeral storage
<a name="ephemeral-storage-enable"></a>

You can redirect scratch I/O to local storage by setting `scratchStorageMode` in the `StartRun` API. The `scratchStorageMode` setting applies to CPU instances only and applies to all tasks in that run.

`scratchStorageMode` determines where your workflow writes scratch data. Possible values:
+ `LOCAL` — Ephemeral storage is placed on local disk. Scratch I/O has dedicated IOPS and throughput.
+ `SHARED` — The shared filesystem is used (default). Scratch I/O contends with the working directory.

For more information, see [Start a run in HealthOmics](starting-a-run.md).

**Note**  
GPU tasks always use local NVMe ephemeral storage for scratch data, and `scratchStorageMode` is always `LOCAL` for GPU tasks.

### Opt in to ephemeral storage
<a name="ephemeral-storage-opt-in"></a>

To enable ephemeral storage for a run, set `scratchStorageMode` to `LOCAL` when you start the run.

```
aws omics start-run \
    --workflow-id {{workflow-id}} \
    --role-arn {{arn:aws:iam::123456789012:role/OmicsServiceRole}} \
    --output-uri s3://{{amzn-s3-demo-bucket}}/{{output-folder}}/ \
    --parameters file://{{/path/to/parameters.json}} \
    --scratch-storage-mode LOCAL
```

For batch runs, pass `scratchStorageMode` in `defaultRunSetting`. The setting applies to every run in the batch.

```
aws omics start-run-batch \
    --batch-name "{{my-batch}}" \
    --default-run-setting '{
      "workflowId": "{{workflow-id}}",
      "roleArn": "arn:aws:iam::{{123456789012}}:role/{{OmicsServiceRole}}",
      "outputUri": "s3://{{amzn-s3-demo-bucket}}/{{output-folder}}/",
      "storageType": "DYNAMIC",
      "parameters": {"{{referenceUri}}": "s3://{{amzn-s3-demo-bucket}}/{{reference.fasta}}"},
      "scratchStorageMode": "LOCAL"
    }' \
    --batch-run-settings '{
      "inlineSettings": [
        {
          "runSettingId": "{{sample-A}}",
          "parameters": {"{{inputUri}}": "s3://{{amzn-s3-demo-bucket}}/{{sampleA.fastq}}"}
        },
        {
          "runSettingId": "{{sample-B}}",
          "parameters": {"{{inputUri}}": "s3://{{amzn-s3-demo-bucket}}/{{sampleB.fastq}}"}
        }
      ]
    }'
```

### Opt out of ephemeral storage
<a name="ephemeral-storage-opt-out"></a>

To disable ephemeral storage for a specific run (for example, to isolate a failure), set `scratchStorageMode` to `SHARED`.

```
aws omics start-run \
     --workflow-id {{workflow-id}} \
     --role-arn {{arn:aws:iam::123456789012:role/OmicsServiceRole}} \
     --output-uri s3://{{amzn-s3-demo-bucket}}/{{output-folder}}/ \
     --scratch-storage-mode SHARED
```

When `scratchStorageMode` is `SHARED`, all `disk` and equivalent directives in the workflow definition are ignored and `/tmp` is backed by the shared filesystem. This setting applies to CPU instances only. GPU tasks always use local NVMe ephemeral storage and cannot be opted out.

### Check the effective mode
<a name="ephemeral-storage-check-mode"></a>

Ephemeral storage is off by default. When `scratchStorageMode` is omitted from a `StartRun` request, `scratchStorageMode` is set to `SHARED` (default).

`scratchStorageMode` is only returned in the `GetRun` response if it was explicitly passed in the `StartRun` request. `SHARED` is the default value if omitted. Call `GetRun` to confirm the effective storage mode for a run.

```
aws omics get-run --id {{run-id}}
```

## Default storage allocation
<a name="ephemeral-storage-default-allocation"></a>

The default ephemeral storage allocation is 16 GiB per task for all Standard, Compute- and Memory-optimized instance types. You do not need to specify a `disk` directive to receive this default. To configure additional storage, use the `disk` directive. You can increase the amount of ephemeral storage allocated to individual tasks in your workflow definition, up to a maximum of 3,072 GiB per task. You are billed for storage above the default 16 GiB.

Ephemeral storage can be configured in increments of 16 GiB. For more information, see [Supported sizes](#ephemeral-storage-supported-sizes).

### Ephemeral storage for accelerated computing instances
<a name="ephemeral-storage-gpu-defaults"></a>

GPU instance storage capacity is fixed per instance type and is provided at no additional cost.

GPU tasks always use local NVMe ephemeral storage. The `scratchStorageMode` setting on `StartRun` does not apply to GPU tasks and setting this value to `SHARED` will have no effect on GPU instances. Capacity is fixed per instance type and cannot be customized using the `disk` directive. The NVMe capacity is pre-determined by the instance type selected for the task's `cpu`, `memory`, and `acceleratorType` requirements.


| Size | GPUs | vCPU | Memory (GiB) | G4dn NVMe (T4) | G5 NVMe (A10G) | G6 NVMe (L4) | G6e NVMe (L40S) | 
| --- | --- | --- | --- | --- | --- | --- | --- | 
| xlarge | 1 | 4 | 16 | 125 GiB | 250 GiB | 250 GiB | 250 GiB | 
| 2xlarge | 1 | 8 | 32 | 225 GiB | 450 GiB | 450 GiB | 450 GiB | 
| 4xlarge | 1 | 16 | 64 | 225 GiB | 600 GiB | 600 GiB | 600 GiB | 
| 8xlarge | 1 | 32 | 128 | 900 GiB | 900 GiB | 900 GiB | 900 GiB | 
| 12xlarge | 4 | 48 | 192 | 900 GiB | 3,800 GiB | 3,760 GiB | 3,800 GiB | 
| 16xlarge | 1 | 64 | 256 | 900 GiB | 1,900 GiB | 1,880 GiB | 1,900 GiB | 
| 24xlarge | 4 | 96 | 384 | — | 3,800 GiB | 3,760 GiB | 3,800 GiB | 

## Configuring ephemeral storage size
<a name="ephemeral-storage-configure-size"></a>

When `scratchStorageMode` is set to `LOCAL`, you can request increased per-task ephemeral storage using the `disk` directive (or equivalent) in your workflow definition. HealthOmics treats the `disk` directive as a hint and provisions a volume rounded to the next 16 GiB. The use of the `disk` directive does not affect instance type selection. Instance type is selected based solely on `cpu`, `memory`, and `acceleratorType`. For more information, see [Task resources in a HealthOmics workflow definition](task-resources.md).

If no `disk` directive is present, the task receives the default 16 GiB. Tasks cannot have less than the default ephemeral storage.

You do not need to size your ephemeral storage for pulled container images, which are accounted for separately. For more information, see [Container images for private workflows](workflows-ecr.md).

### When to use the disk directive
<a name="ephemeral-storage-when-to-use-disk"></a>

Use the `disk` directive in your task definition when the default ephemeral storage for your chosen instance type is not sufficient for your task requirements. For example, when a task writes large volumes of data to `/tmp`.

### Common use cases for increased ephemeral storage
<a name="ephemeral-storage-use-cases"></a>

1. **RNA-Seq Fusion Detection:** RNA-seq workflows generate large intermediate BAMs and task processes often require both the raw FASTQs and aligned outputs to be present concurrently, requiring large scratch disks (for example, 512 GiB per task).

1. **De Novo Genome Assembly:** Long-read assembly workflows need large scratch volumes to process raw reads and temporary assembly artifacts that are repeatedly rewritten and reorganized before output. These tasks are memory- and disk-intensive, sometimes requiring multiple TiB of ephemeral storage.

1. **Variant calling / BAM processing:** Variant calling workflows require substantial scratch storage for alignment and sorting steps that repeatedly read and rewrite large BAM or CRAM files. Ephemeral storage needs are typically hundreds of GiB.

### Directive syntax by engine
<a name="ephemeral-storage-disk-directive-syntax"></a>

The following table shows the equivalent directive for each workflow language.


| Engine | Directive | Example | 
| --- | --- | --- | 
| WDL 1.1 | disks | disks: "/tmp 700 GiB" | 
| Nextflow | disk | disk '700 GB' | 
| CWL | tmpdirMin | tmpdirMin: 716800 (value in MiB) | 

The following examples show how to configure a task that requests 700 GiB of ephemeral storage. HealthOmics rounds this up to the 704 GiB tier.

------
#### [ WDL ]

```
task sort_bam {
    runtime {
        cpu:  16
        disks: "700 GiB"
    }
    command <<<
        samtools sort -T /tmp/sort_buffer ~{input_bam} -o ~{output_bam}
    >>>
}
```

------
#### [ Nextflow ]

```
process sort_bam {
    disk '700 GB'
    script:
    """
    samtools sort -T /tmp/sort_buffer ${input} -o ${output}
    """
}
```

------
#### [ CWL ]

```
requirements:
  ResourceRequirement:
    tmpdirMin: 716800   # 700 GiB expressed in MiB
```

------

For more information on supported directive syntax, see [WDL workflow definition specifics](workflow-languages-wdl.md) and [Nextflow workflow definition specifics](workflow-definition-nextflow.md).

### Example: expression-based disk sizing
<a name="ephemeral-storage-expression-disk"></a>

Instead of a fixed size, you can set the `disk` directive to an expression that the workflow engine evaluates for each task at runtime. The following Nextflow process uses a closure that scales the request with the task attempt number. If the task fails for any reason and Nextflow retries it, the retry requests a larger volume.

```
process sort_bam {
    disk { 200.GB * task.attempt }
    errorStrategy 'retry'
    maxRetries 2

    script:
    """
    samtools sort -T /tmp/sort_buffer ${input} -o ${output}
    """
}
// First attempt requests 200 GiB (provisioned at the 208 GiB tier)
// Second attempt requests 400 GiB (provisioned at the 400 GiB tier)
```

The workflow engine evaluates the expression for each task attempt. HealthOmics then rounds the resolved size up to the next 16 GiB increment.

**Note**  
Because the engine resolves the expression at runtime, HealthOmics cannot check the size at `CreateWorkflow`. HealthOmics caps an evaluated size above 3,072 GiB when the task starts. For more information, see [Supported sizes](#ephemeral-storage-supported-sizes).

### Common bioinformatics tools and ephemeral storage
<a name="ephemeral-storage-tool-examples"></a>

Many bioinformatics tools write large temporary files during execution. When `scratchStorageMode` is set to `LOCAL`, redirect these tools to use `/tmp` so that scratch I/O goes to the fast local volume instead of the shared run filesystem. The following examples show the relevant flags for commonly used tools.

------
#### [ WDL ]

```
task sort_bam {
    runtime {
        cpu:   16
        disks: "700 GiB"
    }
    command <<<
        # samtools: -T sets the temp-file prefix
        samtools sort -T /tmp/sort_buffer ~{input_bam} -o ~{sorted_bam}

        # GATK / Picard: --TMP_DIR flag (older Picard uses TMP_DIR=/tmp)
        gatk MarkDuplicates -I ~{sorted_bam} -O ~{output_bam} --TMP_DIR /tmp

        # STAR: --outTmpDir (path must not pre-exist; STAR creates it)
        STAR --runThreadN 16 --readFilesIn ~{reads} --outTmpDir /tmp/star_tmp --outFileNamePrefix out_

        # bcftools sort: -T / --temp-dir
        bcftools sort -T /tmp ~{vcf} -o ~{output_vcf}

        # GNU sort: -T / --temporary-directory
        sort -T /tmp ~{big_table} -o ~{sorted_table}
    >>>
}
# HealthOmics rounds 700 GiB up to the 704 GiB tier
```

------
#### [ Nextflow ]

```
process sort_bam {
    disk '700 GB'
    script:
    """
    # samtools: -T sets the temp-file prefix
    samtools sort -T /tmp/sort_buffer input.bam -o sorted.bam

    # GATK / Picard: --TMP_DIR flag (older Picard uses TMP_DIR=/tmp)
    gatk MarkDuplicates -I sorted.bam -O dedup.bam --TMP_DIR /tmp

    # STAR: --outTmpDir (path must not pre-exist; STAR creates it)
    STAR --runThreadN 16 --readFilesIn reads.fastq --outTmpDir /tmp/star_tmp --outFileNamePrefix out_

    # bcftools sort: -T / --temp-dir
    bcftools sort -T /tmp input.vcf -o sorted.vcf

    # GNU sort: -T / --temporary-directory
    sort -T /tmp big_table.tsv -o sorted_table.tsv
    """
}
// HealthOmics rounds 700 GB up to the 704 GiB tier
```

------
#### [ CWL ]

```
class: CommandLineTool
cwlVersion: v1.2
requirements:
  ResourceRequirement:
    coresMin: 16
    tmpdirMin: 716800          # 700 GiB expressed in MiB
baseCommand: [bash, -c]
arguments:
  - |
    set -euo pipefail

    # samtools: -T sets the temp-file prefix
    samtools sort -T /tmp/sort_buffer input.bam -o sorted.bam

    # GATK / Picard: --TMP_DIR flag (older Picard uses TMP_DIR=/tmp)
    gatk MarkDuplicates -I sorted.bam -O dedup.bam --TMP_DIR /tmp

    # STAR: --outTmpDir (path must not pre-exist; STAR creates it)
    STAR --runThreadN 16 --readFilesIn reads.fastq --outTmpDir /tmp/star_tmp --outFileNamePrefix out_

    # bcftools sort: -T / --temp-dir
    bcftools sort -T /tmp input.vcf -o sorted.vcf

    # GNU sort: -T / --temporary-directory
    sort -T /tmp big_table.tsv -o sorted_table.tsv
```

------

### Supported sizes
<a name="ephemeral-storage-supported-sizes"></a>

Requested sizes are rounded up to the nearest 16 GiB increment, starting from the default of 16 GiB (16, 32, 48, 64, ... up to 3,072 GiB). The maximum supported size is 3,072 GiB per task.

If a requested size exceeds 3,072 GiB, HealthOmics provisions 3,072 GiB and writes a warning to the run log. The task is not automatically failed.

**Note**  
For expression-based `disk` directives — such as Nextflow closures or WDL expressions like `disks: ceil(size(input_bam, "GiB") * 2.5)` — the value is evaluated at runtime, not at `CreateWorkflow`. If the evaluated size exceeds 3,072 GiB, the task fails at runtime and any compute costs incurred up to that point are charged. For an example, see [Example: expression-based disk sizing](#ephemeral-storage-expression-disk).

### Supported WDL `disks` forms
<a name="ephemeral-storage-wdl-disks"></a>

For the full list of accepted WDL `disks` forms, see [Supported WDL `disks` forms](workflow-languages-wdl.md#workflow-wdl-disks-forms).

### Using the Nextflow scratch directive
<a name="ephemeral-storage-nextflow-scratch"></a>

For Nextflow workflows, you can use the `scratch` directive to control where processes write temporary working files. For information about supported values and recommended usage with ephemeral storage, see [Using scratch storage efficiently in Nextflow](workflow-definition-nextflow.md#nextflow-scratch-storage).

## Monitoring ephemeral storage
<a name="ephemeral-storage-monitoring"></a>

HealthOmics writes per-task ephemeral storage metrics to CloudWatch manifest logs. Metrics include per-task ephemeral storage data of provisioned volume size (as `scratchStorageReservedGiB`) and usage (as `scratchStorageUtilizedGiB`) for each task. Review the manifest log to determine whether tasks were over- or under-provisioned without querying CloudWatch directly. For details on manifest logs, see [Monitoring HealthOmics with CloudWatch Logs](monitoring-cloudwatch-logs.md).

## How ephemeral storage is billed
<a name="ephemeral-storage-billing"></a>

You are billed only for the ephemeral storage provisioned above the default allocation. Requests above the default in your `disk` directive are rounded up to the nearest supported tier.

GPU instances have ephemeral storage already accounted for in instance pricing. There is no additional charge for ephemeral storage on GPU tasks.

## Considerations and limitations
<a name="ephemeral-storage-considerations"></a>


| Consideration | Detail | 
| --- | --- | 
| Ephemeral storage is not persistent | Ephemeral storage volumes are always deleted when the task terminates. Data in /tmp is not saved, exported, or available to subsequent tasks or runs. Data in /tmp on ephemeral storage cannot be a task output or a workflow output; this will result in a failure at runtime. | 
| Ephemeral storage is not shared across tasks | Each task receives its own isolated ephemeral storage volume. Tasks cannot access each other's /tmp directories. Data that must be shared between tasks must be written to the shared run filesystem. | 
| Storage cannot be resized mid-task | The storage size is fixed at task start. You cannot increase or decrease allocated storage while a task is running. | 
| Working-directory scratch is not automatically redirected | Workflows that write scratch to the working directory — for example, input/, ./, or out/ — do not benefit automatically. Update your workflow to redirect scratch I/O to /tmp or $TMPDIR. | 
| Scratch data is not being written to /tmp as expected | Ensure your task processes explicitly write to /tmp and that your task commands have not mapped $TMPDIR to another location. | 
| GPU instances always use ephemeral storage | GPU tasks always mount /tmp on the local NVMe instance store. Setting scratchStorageMode to SHARED does not disable ephemeral storage for GPU tasks. | 
| GPU instances: NVMe capacity is fixed | Custom disk sizing is not supported on GPU instances. HealthOmics ignores disk directives and provides the default NVMe capacity for the instance type. | 
| Maximum 3,072 GiB per task (CPU) | Requests exceeding 3,072 GiB are provisioned at 3,072 GiB with a run log warning. Tasks are not failed. | 
| Supported tiers only (CPU) | Requested sizes are rounded up to the nearest 16 GiB increment (16, 32, 48, 64, ... up to 3,072 GiB). | 
| Expression-based directives evaluated at runtime | disk values computed from expressions are validated at task start, not at CreateWorkflow. Compute costs up to that point are charged if the task fails at runtime. | 
| SHARED mode ignores all disk directives (CPU only) | When scratchStorageMode is SHARED, disk, tmpdirMin, and equivalent directives are ignored for CPU tasks. No local storage volume is provisioned. GPU tasks are unaffected, they always use local NVMe. | 

## Troubleshooting ephemeral storage
<a name="ephemeral-storage-troubleshooting"></a>

### Task fails with exhausted ephemeral storage
<a name="ephemeral-storage-ts-exhausted"></a>

A task fails when ephemeral storage reaches capacity. Review your CloudWatch manifest logs to determine how much storage your task actually used, then add or increase the `disk` directive to request a larger tier.

```
# Before: 4-vCPU task using the 16 GiB default
runtime { cpu: 4 }

# After: explicitly request 400 GiB
runtime { cpu: 4, disks: "400 GiB" }
```

### Ephemeral storage does not appear to be utilized
<a name="ephemeral-storage-ts-not-used"></a>

Call `GetRun` and check the `scratchStorageMode` field. If the value is `SHARED`, ephemeral storage is not enabled for that run. Set `--scratch-storage-mode LOCAL` on your next `start-run` call.

```
aws omics get-run --id {{run-id}}
```