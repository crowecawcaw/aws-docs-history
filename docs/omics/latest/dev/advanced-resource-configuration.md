

# Advanced resource configuration
<a name="advanced-resource-configuration"></a>

With the **omicsResourceFallbackOrder** directive you can declare an ordered list of resource (for example, accelerator and CPU) profiles for a task within your workflow. You specify this directive at the task level in WDL, or at the process or config level in Nextflow. HealthOmics searches for each profile in the order you specify for availability to reserve. If capacity isn't available within the wait timeout, HealthOmics moves to the next resource profile in the list.

This is useful when your preferred accelerator capacity (for example, G6e with `nvidia-l40s`) isn't available and you'd rather fall back to a different accelerator type or to a CPU instead of failing the run. Resource fallback is one of several strategies for improving GPU acquisition success. For more information about these best practices, see [Mitigating INSTANCE\_RESERVATION\_FAILED errors](workflows-run-errors.md#workflows-mitigate-instance-reservation-failed).

## How it works
<a name="advanced-resource-configuration-how-it-works"></a>

1. You define an ordered list of resource profiles in the **omicsResourceFallbackOrder** directive.

1. At run time, HealthOmics tries to reserve capacity for the first profile in the list.

1. If capacity isn't available within the wait timeout period, HealthOmics moves to the next profile.

1. The task runs on whichever profile succeeds first.

1. If all profiles in the list fail, the task fails with reason `ALL_PROFILES_INSTANCE_RESERVATION_FAILED`. In WDL, no engine retries are applied when all profiles are unavailable. In Nextflow, **errorStrategy** and **maxRetries** decide whether the task is retried.

**Note**  
In WDL, use **omicsResourceFallbackOrder** instead of the task's usual **acceleratorType**, **acceleratorCount**, **cpu**, **memory**, and **omicsResourceWaitTimeoutInMin** fields. These must not be set at the top level when the directive is present. In Nextflow, a process's **cpus** and **memory** directives apply to every profile that omits them. For details, see [Configure resource fallback with **omicsResourceFallbackOrder**](workflow-definition-nextflow.md#workflow-nextflow-directive-fallback).

## Use cases
<a name="advanced-resource-configuration-use-cases"></a>


| Scenario | Description | 
| --- | --- | 
| GPU to GPU fallback | List accelerator (or GPU) types in priority order. For example, try nvidia-l40s first, then fall back to nvidia-l4. No command changes are needed if the workload is the same across accelerator types. | 
| GPU to CPU fallback | Add a final profile that omits acceleratorType for CPU-only fallback. Use the AWS\_HEALTHOMICS\_RESOURCE\_TYPE environment variable to branch the command by resource type. | 

## Task-level runtime fields
<a name="advanced-resource-configuration-runtime-fields"></a>

**Note**  
On this page, *profile* refers to an individual accelerator or CPU resource configuration declared within **omicsResourceFallbackOrder** that consists of the 5 per-profile fields.

When using **omicsResourceFallbackOrder**, task-level runtime fields split into two sets:
+ **Per-profile fields** (**acceleratorType**, **acceleratorCount**, **cpu**, **memory**, **omicsResourceWaitTimeoutInMin**) — configurable independently for each profile in the list.
+ **Shared fields** (all other runtime fields, such as **docker**, **maxRetries**) — set once at the top level and apply the same way to every profile.

In WDL, the CPU field is **cpu**. In Nextflow, it is **cpus**, and **memory** is written as for the Nextflow **memory** directive, for example `'32 GB'`. The shared fields in Nextflow are the process's other directives, such as **container**, **errorStrategy**, and **maxRetries**.

## Examples
<a name="advanced-resource-configuration-examples"></a>

------
#### [ WDL ]

The following WDL task searches for `nvidia-l40s` first (waiting up to 45 minutes for capacity), then `nvidia-l4` (default wait window), then falls back to a CPU-only profile (32 vCPUs, 128 GiB) if neither accelerator type is available.

```
task align {
  command <<<
    # Branch based on which resource type was allocated
    if [ "$AWS_HEALTHOMICS_RESOURCE_TYPE" = "cpu" ]; then
      sentieon bwa mem -t 32 ~{reference} ~{fastq}
    else
      pbrun fq2bam --ref ~{reference} --in-fq ~{fastq}
    fi
  >>>

  runtime {
    docker: "my-registry/align-multi-arch:latest"
    maxRetries: 2

    omicsResourceFallbackOrder: [
      {"acceleratorType": "nvidia-l40s", "acceleratorCount": 1,
       "cpu": 8, "memory": "32 GiB",
       "omicsResourceWaitTimeoutInMin": 45},

      {"acceleratorType": "nvidia-l4", "acceleratorCount": 1,
       "cpu": 8, "memory": "32 GiB"},

      {"cpu": 32, "memory": "128 GiB"}
    ]
  }
}
```

------
#### [ Nextflow ]

The following Nextflow process searches for `nvidia-l40s` first (waiting up to 45 minutes for capacity), then `nvidia-l4` (default wait window), then falls back to a CPU-only profile (32 vCPUs, 128 GB) if neither accelerator type is available. In a process body, write the directive as a method call with parentheses.

```
process ALIGN {
    container 'my-registry/align-multi-arch:latest'
    errorStrategy 'retry'
    maxRetries 2

    omicsResourceFallbackOrder([
        [acceleratorType: 'nvidia-l40s', acceleratorCount: 1, cpus: 8, memory: '32 GB',
         omicsResourceWaitTimeoutInMin: 45],
        [acceleratorType: 'nvidia-l4', acceleratorCount: 1, cpus: 8, memory: '32 GB'],
        [cpus: 32, memory: '128 GB']
    ])

    script:
    """
    # Branch based on which resource type was allocated
    if [ "\$AWS_HEALTHOMICS_RESOURCE_TYPE" = "cpu" ]; then
      sentieon bwa mem -t \$(nproc) ${reference} ${fastq}
    else
      pbrun fq2bam --ref ${reference} --in-fq ${fastq}
    fi
    """
}
```

You can also set the directive in `nextflow.config`, either in the `process` scope for every process or with a process selector. In a config file, assign the list with `=`:

```
process {
    withLabel: 'gpu_align' {
        omicsResourceFallbackOrder = [
            [acceleratorType: 'nvidia-l40s', acceleratorCount: 1, cpus: 8, memory: '32 GB'],
            [cpus: 32, memory: '128 GB']
        ]
    }
}
```

------

In these examples, **AWS\_HEALTHOMICS\_RESOURCE\_TYPE** tells the command which resource path was selected (for example, `"nvidia-l40s"` or `"cpu"`).

**Note**  
The Docker image must support both accelerator and CPU code paths if your fallback order contains a CPU profile. Ensure your container includes the required tooling for all resource profiles in the list.

## Per-profile field reference
<a name="advanced-resource-configuration-field-reference"></a>

Each entry in the **omicsResourceFallbackOrder** list is a map describing one resource profile. All fields are optional; a profile can be a partial specification. Each profile must use quoted (string) keys. The **cpu** and **memory** fields differ between WDL and Nextflow, so the following table lists a separate row for each.


| Field | Type | Default when omitted | Notes | 
| --- | --- | --- | --- | 
| acceleratorType | String | When not specified, the profile is considered as CPU | Must be one of the 7 supported accelerator types. See [Task accelerators in a HealthOmics workflow definition](task-accelerators.md). Omit this field to specify a CPU-only profile. For CPU profile, do not set it to "". | 
| acceleratorCount | Integer | Field absent when acceleratorType is also absent | Must be specified together with acceleratorType. A profile cannot have one without the other. | 
| cpu (WDL) | Integer or Float | 1 vCPU, or the GPU instance-type default for a GPU profile | Rounded up to a whole vCPU, minimum 1. Same fractional support as the top-level runtime.cpu. | 
| cpus (Nextflow) | Integer, Float, or a String holding a whole number (for example, '8') | The process's cpus, if set. Otherwise the GPU instance-type default for a GPU profile. | Truncated to a whole vCPU, as the cpus directive does. A value below 1 runs with 1 vCPU. A negative value is rejected. | 
| memory (WDL) | String, for example "32 GiB" | 1 GiB, or the GPU instance-type default for a GPU profile | Same format as the top-level runtime.memory. Rounded up to a whole GiB. | 
| memory (Nextflow) | String or Nextflow memory value, for example '32 GB' or 32.GB | The process's memory, if set. Otherwise the GPU instance-type default for a GPU profile. | Same format as the memory directive: B, KB, MB, GB or TB. Rounded down to a whole GB. A value below 1 GB runs with 1 GB. | 
| omicsResourceWaitTimeoutInMin | Integer | 20 minutes for Single GPU accelerator bundle and 30 minutes for multi-GPU accelerator bundles. These are also recommended minimum values. | There is no upper bound. Controls how long HealthOmics searches for one profile before moving to the next profile. See [Timeout behavior](#advanced-resource-configuration-timeout-behavior). | 

**Note**  
Omitted fields take default value, not values inherited from an earlier profile in the list. A field left out of a profile takes its documented default (as given in the table above), not a value copied from an earlier profile in the list.

## Timeout behavior
<a name="advanced-resource-configuration-timeout-behavior"></a>

**omicsResourceWaitTimeoutInMin** controls how long HealthOmics waits for accelerator capacity on a given profile before advancing to the next one.
+ **Per-profile, not global.** Each accelerator profile can specify its own timeout. Configure a longer wait for a preferred high-end accelerator and a shorter wait for a fallback type.
+ **20-minute recommended minimum.** Values below 20 minutes (30 for multi-GPU bundles) are accepted but generate a validation warning.
+ **Timeout advances, not fails.** When the timeout elapses, HealthOmics moves to the next profile — the task does not fail. Failure only occurs after all profiles are exhausted.
+ **Not applicable to CPU-only profiles.** A CPU profile has no capacity limitations. Omit **omicsResourceWaitTimeoutInMin** on the final CPU profile.
+ **Retries receive a fresh timeout window.** Each OOM or service-error retry starts its own full **omicsResourceWaitTimeoutInMin** window on the same profile, rather than inheriting time already spent by a prior attempt.

## Environment variables
<a name="advanced-resource-configuration-environment-variables"></a>

HealthOmics sets the following environment variable in the task container so your command can branch based on which resource profile was allocated:


| Variable | Value | Example values | 
| --- | --- | --- | 
| AWS\_HEALTHOMICS\_RESOURCE\_TYPE | The acceleratorType of the active profile, or "cpu" for a CPU-only profile. | "nvidia-l40s", "nvidia-l4", "cpu" | 

## Validation criteria
<a name="advanced-resource-configuration-validation"></a>

HealthOmics validates the following at workflow creation time and re-checks at task runtime. All rules reject the workflow or task unless noted otherwise.

1. **Cannot mix with individual resource directives.** If **omicsResourceFallbackOrder** is specified, the top-level **acceleratorType**, **acceleratorCount**, **cpu**, **memory**, and **omicsResourceWaitTimeoutInMin** must not be specified in the same task.

1. **Must be a list.** **omicsResourceFallbackOrder** must be written as an array of profiles.

1. **Cannot be empty.** The list must contain at least one profile.

1. **Quoted keys required.** Each field name must be a quoted string, for example `{"acceleratorType": "nvidia-l4", "acceleratorCount": 1}`. Bareword keys fail validation.

1. **Non-empty profiles.** An empty profile (`{}`) is not allowed.

1. ****acceleratorType** and **acceleratorCount** go together.** A profile that sets one must set the other. A CPU profile must omit both.

1. **Supported accelerator types only.** **acceleratorType** must be a supported accelerator type or omitted (CPU profile). Empty string `""` is not accepted.

1. **Accelerator type unavailable in the Region (warning only).** If an accelerator type isn't supported in the workflow's AWS Region, HealthOmics skips that profile at task scheduling time. You get a warning in the runtime logs when an accelerator is skipped because it's not supported (or not offered) in that Region.

1. **Minimum wait timeout.** **omicsResourceWaitTimeoutInMin** recommended value is ≥ 20 minutes (≥ 30 for multi-GPU bundles).

1. **Duplicate profiles (warning only).** Duplicate profiles are allowed but produce a warning. Consider increasing **omicsResourceWaitTimeoutInMin** on the earlier profile instead.

1. **Unrecognized fields rejected.** Only the 5 per-profile fields listed above are allowed.

1. **Correct types.** For example, **acceleratorCount** must be a number, not a string.

1. **Maximum resource values.** **cpu**, **memory**, and **acceleratorCount** each have a maximum — 192, 1536 GiB, and 4 respectively, matching the largest instance HealthOmics supports. Values above these are rejected at workflow creation time and at task run time. For supported instance maximum values, see [Compute and memory](memory-and-compute-tasks.md).

1. **At most one CPU profile.** Only one profile that omits **acceleratorType** is allowed.

1. **CPU profile must be last.** A CPU profile, if present, must be the last profile in the list. You should provide all accelerator options you would like before specifying a CPU profile in the priority order.

1. **Maximum 10 profiles per task.**

**Nextflow-specific criteria:** For Nextflow, workflow creation does not reject the workflow. Instead, it reports each finding in the workflow's status message, and an invalid value fails the task when it runs. Rule 1 is a warning rather than a rejection. Rule 4 does not apply because profile keys are written as Groovy map keys. Values that are only known at run time are checked when the task runs. For details, see [Configure resource fallback with **omicsResourceFallbackOrder**](workflow-definition-nextflow.md#workflow-nextflow-directive-fallback).

## Interaction with retries
<a name="advanced-resource-configuration-retries"></a>

For Out-of-Memory (OOM) and service errors (5xx excluding `ALL_PROFILES_INSTANCE_RESERVATION_FAILED`), HealthOmics retries the task as follows:
+ Retries occur within the currently active profile that was previously successfully reserved.
+ Retries never advance to the next profile in the fallback order.
+ A retry that exhausts **maxRetries** fails the task.

For more information about task retries in HealthOmics, see [Task Retries](monitoring-runs.md#run-status-task-retries).

**Warning**  
In WDL, if all profiles are exhausted on the first engine attempt with no instance reservation, the task and run fail with status `ALL_PROFILES_INSTANCE_RESERVATION_FAILED`. Even if you configure retries, HealthOmics does not retry for this error code. We recommend adjusting your **omicsResourceWaitTimeoutInMin** appropriately. Nextflow retries work differently; see [Configure resource fallback with **omicsResourceFallbackOrder**](workflow-definition-nextflow.md#workflow-nextflow-directive-fallback).

## Best practices
<a name="advanced-resource-configuration-best-practices"></a>

Follow these best practices when you configure resource fallback:
+ **Avoid multi-GPU bundle types in fallback order.** Accelerator types that span multiple instance families (for example, `nvidia-t4-a10g-l4`) are not recommended inside **omicsResourceFallbackOrder**. Use single-family types instead. For details on available accelerator types, see [Task accelerators in a HealthOmics workflow definition](task-accelerators.md).
+ **Set appropriate wait timeouts.** For high-priority accelerator profiles, increase **omicsResourceWaitTimeoutInMin** to give HealthOmics more time to find capacity.
+ **Place CPU profiles last.** If you include a CPU-only fallback, it must be the last entry so accelerators are preferred when available.
+ **Use multi-architecture container images.** When using GPU to CPU fallback, ensure your Docker image supports both GPU-accelerated and CPU-only code paths.

## Limitations
<a name="advanced-resource-configuration-limitations"></a>

The following limitations apply:
+ In WDL, **omicsResourceFallbackOrder** is not supported within **scatter** blocks. It is available only at the task level.
+ The directive is supported for WDL and Nextflow. CWL support is planned.
+ Instance-type names (for example, `omics.g6e.4xlarge`) are not accepted as resource values. You must use the per-profile field syntax described on this page.