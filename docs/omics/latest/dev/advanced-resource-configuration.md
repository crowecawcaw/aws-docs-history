# Advanced resource configuration

With the **omicsResourceFallbackOrder** directive you can declare an ordered list of
resource (for example, accelerator and CPU) profiles for a task within your workflow. You specify this
directive at the task level. HealthOmics searches for each profile in the order you specify for availability to
reserve. If capacity isn't available within the wait timeout, HealthOmics moves to the next resource profile in the
list.

This is useful when your preferred accelerator capacity (for example, G6e with `nvidia-l40s`)
isn't available and you'd rather fall back to a different accelerator type or to a CPU instead of failing
the run.

## How it works

1. You define an ordered list of resource profiles in the **omicsResourceFallbackOrder**
   directive.
2. At run time, HealthOmics tries to reserve capacity for the first profile in the list.
3. If capacity isn't available within the wait timeout period, HealthOmics moves to the next profile.
4. The task runs on whichever profile succeeds first.
5. If all profiles in the list fail, the task fails with reason
   `ALL_PROFILES_INSTANCE_RESERVATION_FAILED`. No engine retries will be applied when all
   profiles are unavailable.

###### Note

**omicsResourceFallbackOrder** replaces the task's usual **acceleratorType**,
**acceleratorCount**, **cpu**, **memory**, and
**omicsResourceWaitTimeoutInMin** fields. These must not be set at the top level when
the directive is present.

## Use cases

| Scenario                | Description                                                                                                                                                                                                       |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **GPU to GPU fallback** | List accelerator (or GPU) types in priority order. For example, try `nvidia-l40s` first, then fall<br>back to `nvidia-l4`. No command changes are needed if the workload is the same across<br>accelerator types. |
| **GPU to CPU fallback** | Add a final profile that omits *_acceleratorType_<br>• for CPU-only fallback. Use the<br>*_AWS\_HEALTHOMICS\_RESOURCE\_TYPE_<br>• environment variable to branch the command by<br>resource type.                 |

## Task-level runtime fields

When using **omicsResourceFallbackOrder**, task-level runtime fields split into two
sets:

- **Per-profile fields** (**acceleratorType**,
  **acceleratorCount**, **cpu**, **memory**,
  **omicsResourceWaitTimeoutInMin**) — configurable independently for each profile in the
  list.
- **Shared fields** (all other runtime fields, such as
  **docker**, **maxRetries**) — set once at the top level and apply the
  same way to every profile.

## WDL example

The following WDL task searches for `nvidia-l40s` first (waiting up to 45 minutes for
capacity), then `nvidia-l4` (default wait window), then falls back to a CPU-only profile (32
vCPUs, 128 GiB) if neither accelerator type is available.

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

In this example, **AWS\_HEALTHOMICS\_RESOURCE\_TYPE** tells the command which resource path
was selected (for example, `"nvidia-l40s"` or `"cpu"`).

###### Note

The Docker image must support both accelerator and CPU code paths if your fallback order contains a
CPU profile. Ensure your container includes the required tooling for all resource profiles in the
list.

## Per-profile field reference

Each entry in the **omicsResourceFallbackOrder** list is a map describing one resource
profile. All fields are optional; a profile can be a partial specification. Each profile must use quoted
(string) keys.

| Field                           | Type                             | Default when omitted                                                                                                                         | Notes                                                                                                                                                                                                                                                  |
| ------------------------------- | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `acceleratorType`               | String                           | When not specified, the profile is considered as CPU                                                                                         | Must be one of the 7 supported accelerator types. See [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md"). Omit this field to specify a CPU-only profile. For CPU<br>profile, do not set it to `""`. |
| `acceleratorCount`              | Integer                          | Field absent when `acceleratorType` is also absent                                                                                           | Must be specified together with `acceleratorType`. A profile cannot have one without<br>the other.                                                                                                                                                     |
| `cpu`                           | Integer or Float                 | 1 vCPU, or GPU instance-type default if a GPU profile omits it                                                                               | Rounded up to nearest whole vCPU (minimum 1). Same fractional support as the<br>top-level *_runtime.cpu_<br>• directive.                                                                                                                               |
| `memory`                        | String (for example, `"32 GiB"`) | 1 GiB, or a GPU instance-type default if a GPU profile omits it                                                                              | Same format as the top-level *_runtime.memory_<br>• directive.                                                                                                                                                                                         |
| `omicsResourceWaitTimeoutInMin` | Integer                          | 20 minutes for Single GPU accelerator bundle and 30 minutes for multi-GPU accelerator bundles.<br>These are also recommended minimum values. | There is no upper bound. Controls how long HealthOmics searches for one profile before moving to<br>the next profile. See [Timeout behavior](#advanced-resource-configuration-timeout-behavior "#advanced-resource-configuration-timeout-behavior").   |

###### Note

Omitted fields take default value, not values inherited from an earlier profile in the list. A field
left out of a profile takes its documented default (as given in the table above), not a value copied
from an earlier profile in the list.

## Timeout behavior

**omicsResourceWaitTimeoutInMin** controls how long HealthOmics waits for accelerator capacity on a
given profile before advancing to the next one.

- **Per-profile, not global.** Each accelerator profile can specify its
  own timeout. Configure a longer wait for a preferred high-end accelerator and a shorter wait for a
  fallback type.
- **20-minute recommended minimum.** Values below 20 minutes (30 for
  multi-GPU bundles) are accepted but generate a validation warning.
- **Timeout advances, not fails.** When the timeout elapses, HealthOmics moves to
  the next profile — the task does not fail. Failure only occurs after all profiles are exhausted.
- **Not applicable to CPU-only profiles.** A CPU profile has no capacity
  limitations. Omit **omicsResourceWaitTimeoutInMin** on the final CPU profile.
- **Retries receive a fresh timeout window.** Each OOM or service-error
  retry starts its own full **omicsResourceWaitTimeoutInMin** window on the same profile,
  rather than inheriting time already spent by a prior attempt.

## Environment variables

HealthOmics sets the following environment variable in the task container so your command can branch based on
which resource profile was allocated:

| Variable                        | Value                                                                              | Example values                          |
| ------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------- |
| `AWS_HEALTHOMICS_RESOURCE_TYPE` | The `acceleratorType` of the active profile, or `"cpu"` for a<br>CPU-only profile. | `"nvidia-l40s"`, `"nvidia-l4"`, `"cpu"` |

## Validation criteria

HealthOmics validates the following at workflow creation time and re-checks at task runtime. All rules
reject the workflow or task unless noted otherwise.

1. **Cannot mix with individual resource directives.** If
   **omicsResourceFallbackOrder** is specified, the top-level
   **acceleratorType**, **acceleratorCount**, **cpu**,
   **memory**, and **omicsResourceWaitTimeoutInMin** must not be
   specified in the same task.
2. **Must be a list.** **omicsResourceFallbackOrder** must
   be written as an array of profiles.
3. **Cannot be empty.** The list must contain at least one profile.
4. **Quoted keys required.** Each field name must be a quoted string, for
   example `{"acceleratorType": "nvidia-l4", "acceleratorCount": 1}`. Bareword keys fail
   validation.
5. **Non-empty profiles.** An empty profile (`{}`) is not
   allowed.
6. ****acceleratorType** and **acceleratorCount** go
   together.** A profile that sets one must set the other. A CPU profile must omit both.
7. **Supported accelerator types only.** **acceleratorType** must be
   a supported accelerator type or omitted (CPU profile). Empty string `""` is not accepted.
8. **Minimum wait timeout.**
   **omicsResourceWaitTimeoutInMin** recommended value is ≥ 20 minutes (≥ 30 for
   multi-GPU bundles).
9. **Duplicate profiles (warning only).** Duplicate profiles are allowed
   but produce a warning. Consider increasing **omicsResourceWaitTimeoutInMin** on the
   earlier profile instead.
10. **Unrecognized fields rejected.** Only the five per-profile fields
    listed above are allowed.
11. **Correct types.** For example, **cpu** must be a
    number, not a string.
12. **At most one CPU profile.** Only one profile that omits
    **acceleratorType** is allowed.
13. **Maximum 10 profiles per task.**

## Interaction with retries

For Out-of-Memory (OOM) and service errors (5xx excluding
`ALL_PROFILES_INSTANCE_RESERVATION_FAILED`), HealthOmics retries the task as follows:

- Retries occur within the currently active profile that was previously successfully reserved.
- Retries never advance to the next profile in the fallback order.
- A retry that exhausts **maxRetries** fails the task.

For more information about task retries in HealthOmics, see [Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

###### Note

If all profiles are exhausted on the first engine attempt with no instance reservation, the engine
fails the task and subsequently the run with status `ALL_PROFILES_INSTANCE_RESERVATION_FAILED`.
Even if you have configured retries, HealthOmics does not retry for this error code. We recommend adjusting your
**omicsResourceWaitTimeoutInMin** appropriately.

## Best practices

- **Avoid multi-GPU bundle types in fallback order.** Accelerator types
  that span multiple instance families (for example, `nvidia-t4-a10g-l4`) are not recommended
  inside **omicsResourceFallbackOrder**. Use single-family types instead. For details on
  available accelerator types, see [Task accelerators in a HealthOmics workflow definition](task-accelerators.md "task-accelerators.md").
- **Set appropriate wait timeouts.** For high-priority accelerator profiles,
  increase **omicsResourceWaitTimeoutInMin** to give HealthOmics more time to find capacity.
- **Place CPU profiles last.** If you include a CPU-only fallback, it
  must be the last entry so accelerators are preferred when available.
- **Use multi-architecture container images.** When using GPU to CPU
  fallback, ensure your Docker image supports both GPU-accelerated and CPU-only code paths.

## Limitations

- **omicsResourceFallbackOrder** is not supported within **scatter**
  blocks. It is available only at the task level.
- Only WDL is supported as of the GA launch date. Nextflow and CWL support is planned.
- Instance-type names (for example, `omics.g6e.4xlarge`) are not accepted as resource
  values. You must use the per-profile field syntax described on this page.
