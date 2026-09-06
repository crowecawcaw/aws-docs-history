

# Task accelerators in a HealthOmics workflow definition
<a name="task-accelerators"></a>

In the workflow definition, you can optionally specify the GPU accelerator-spec for a task. HealthOmics supports the following accelerator-spec values, along with the supported instance types:


| Accelerator spec | Healthomics instance types | 
| --- | --- | 
| nvidia-tesla-t4 | G4 | 
| nvidia-tesla-t4-a10g | G4 and G5 | 
| nvidia-tesla-a10g | G5 | 
| nvidia-t4-a10g-l4 | G4, G5, and G6 | 
| nvidia-l4-a10g | G5 and G6 | 
| nvidia-l4 | G6 | 
| nvidia-l40s | G6e | 

If you specify an accelerator type that supports multiple instance types, HealthOmics selects the instance type based on available capacity. If both instance types are available, HealthOmics gives preference to the lower cost instance. The exception is for the nvidia-t4-a10g-l4 task accelerator which gives preference to the latest generation instance available.

For details about the instance types, see [Accelerated-computing instances](memory-and-compute-tasks.md#workflow-task-accelerated-computing-instances).

In the following example, the workflow definition specifies `nvidia-l4` as the accelerator:

------
#### [ WDL ]

```
task my_task {
 runtime {
    ...
    acceleratorCount: 1
    acceleratorType: "{{nvidia-l4}}"
 }
 ...
}
```

------
#### [ NextFlow ]

```
process my_task {
 ...
 accelerator 1, type: "{{nvidia-l4}}"
 ...
}
```

------
#### [ CWL ]

```
cwlVersion: v1.2
class: CommandLineTool
requirements:
  ...
  cwltool:CUDARequirement:
      cudaDeviceCountMin: 1
      cudaComputeCapability: "{{nvidia-l4}}"
      cudaVersionMin: "1.0"
```

------

## Advanced resource configuration
<a name="task-accelerators-fallback"></a>

You can also configure a task to reserve multiple accelerators in your preferred priority order using the **omicsResourceFallbackOrder** directive. This directive is currently available only for WDL. HealthOmics tries each accelerator profile in order you define until one succeeds, including an optional final CPU profile.

This is useful in the following scenarios:
+ **GPU to GPU fallback** – List GPU types in priority order (for example, try `nvidia-l40s` first, then fall back to `nvidia-l4`).
+ **GPU to CPU fallback** – Add a final CPU-only profile so the task completes even when no GPU capacity is available in the Region.

For full details about **omicsResourceFallbackOrder**, including per-profile field reference, validation rules, and a complete WDL example, see [Advanced resource configuration](advanced-resource-configuration.md).