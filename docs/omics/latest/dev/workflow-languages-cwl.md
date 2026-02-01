# CWL workflow definition specifics

Workflows written in Common Workflow Language, or CWL, offer similar functionality to workflows written in
WDL and Nextflow. You can use Amazon S3 or HealthOmics storage URIs as input parameters.

If you define input in a secondaryFile in a sub workflow, add the same definition in the main
workflow.

HealthOmics workflows don't support operation processes. To learn more about operations processes in CWL workflows,
see the [CWL
documentation](https://www.commonwl.org/user_guide/topics/operations.html "https://www.commonwl.org/user_guide/topics/operations.html").

Best practice is to define a separate CWL workflow for each container that you use. We recommend that you don't
hardcode the dockerPull entry with a fixed Amazon ECR URI.

###### Topics

- [Convert CWL workflows to use HealthOmics](#workflow-cwl-convert "#workflow-cwl-convert")
- [Opt out of task retry using omicsRetryOn5xx](#workflow-cwl-retry-5xx "#workflow-cwl-retry-5xx")
- [Loop a workflow step](#workflow-cwl-loop "#workflow-cwl-loop")
- [Retry tasks with increased memory](#workflow-cwl-out-of-memory-retry "#workflow-cwl-out-of-memory-retry")
- [Examples](#workflow-cwl-examples "#workflow-cwl-examples")

## Convert CWL workflows to use HealthOmics

To convert an existing CWL workflow definition to use HealthOmics, make the following changes:

- Replace all Docker container URIs with Amazon ECR URIs.
- Make sure that all the workflow files are declared in the main workflow as input, and all
  variables are explicitly defined.
- Make sure that all JavaScript code is strict-mode complaint.

## Opt out of task retry using `omicsRetryOn5xx`

HealthOmics supports task retries if the task failed because of service errors (5XX HTTP status codes). By default,
HealthOmics attempts up to two retries of a failed task. For more information about task retry in HealthOmics, see [Task Retries](monitoring-runs.md#run-status-task-retries "monitoring-runs.md#run-status-task-retries").

To opt out of task retry for service errors, configure the `omicsRetryOn5xx` directive in the
workflow definition. You can define this directive under requirements or hints. We recommend adding the directive
as a hint for portability.

```
requirements:
  ResourceRequirement:
    omicsRetryOn5xx: false

hints:
  ResourceRequirement:
    omicsRetryOn5xx: false
```

Requirements override hints. If a task implementation provides a resource requirement in hints that is also
provided by requirements in an enclosing workflow, the enclosing requirements takes precedence.

If the same task requirement appears at different levels of the workflow, HealthOmics uses the most specific
entry from `requirements` (or `hints`, if there are no entries in `requirements`).
The following list shows the order of precedence that HealthOmics uses to apply configuration settings, from
lowest to highest priority:

- Workflow level
- Step level
- Task section of the workflow definition

The following example shows how to configure the `omicsRetryOn5xx` directive at different levels of
the workflow. In this example, the workflow-level requirement overrides the workflow level hints. The requirements
configurations at the task and step levels override the hints configurations.

```
class: Workflow
# Workflow-level requirement and hint
requirements:
  ResourceRequirement:
    omicsRetryOn5xx: false

hints:
  ResourceRequirement:
    omicsRetryOn5xx: false  # The value in requirements overrides this value

steps:
  task_step:
    # Step-level requirement
    requirements:
      ResourceRequirement:
        omicsRetryOn5xx: false
    # Step-level hint
    hints:
      ResourceRequirement:
        omicsRetryOn5xx: false
    run:
      class: CommandLineTool
      # Task-level requirement
      requirements:
        ResourceRequirement:
          omicsRetryOn5xx: false
      # Task-level hint
      hints:
        ResourceRequirement:
          omicsRetryOn5xx: false

```

## Loop a workflow step

HealthOmics supports looping a workflow step. You can use loops to run workflow steps repeatedly until a specified condition is met. This is useful for iterative processes where you need to repeat a task multiple times or until a certain result is achieved.

**Note:** Loop functionality requires CWL version 1.2 or later. Workflows using CWL versions earlier than 1.2 do not support loop operations.

To use loops in your CWL workflow, define a Loop requirement. The following example shows the loop requirement configuration:

```
requirements:
  - class: "http://commonwl.org/cwltool#Loop"
    loopWhen: $(inputs.counter < inputs.max)
    loop:
      counter:
        loopSource: result
        valueFrom: $(self)
    outputMethod: last
```

The `loopWhen` field controls when the loop terminates. In this example, the loop continues as long as the counter is less than the maximum value. The `loop` field defines how input parameters are updated between iterations. The `loopSource` specifies which output from the previous iteration feeds into the next iteration. The `outputMethod` field set to `last` returns only the final iteration's output.

## Retry tasks with increased memory

HealthOmics supports automatic retry of out-of-memory task failures. When a task exits with code 137 (out-of-memory), HealthOmics creates a new task with increased memory allocation based on the specified multiplier.

###### Note

HealthOmics retries out-of-memory failures up to 3 times or until the memory allocation reaches 1536 GiB, whichever limit is reached first.

The following example shows how to configure out-of-memory retry:

```
hints:
  ResourceRequirement:
    ramMin: 4096
  http://arvados.org/cwl#OutOfMemoryRetry:
    memoryRetryMultiplier: 2.5
```

When a task fails due to out-of-memory, HealthOmics calculates the retry memory allocation using the formula: `previous_run_memory × memoryRetryMultiplier`. In the example above, if the task with 4096 MB of memory fails, the retry attempt uses 4096 × 2.5 = 10,240 MB of memory.

The `memoryRetryMultiplier` parameter controls how much additional memory to allocate for retry attempts:

- **Default value:** If you don't specify a value, it defaults to `2` (doubles the memory)
- **Valid range:** Must be a positive number greater than `1`. Invalid values result in a 4XX validation error
- **Minimum effective value:** Values between `1` and `1.5` are automatically increased to `1.5` to ensure meaningful memory increases and prevent excessive retry attempts

## Examples

The following is an example of a workflow written in CWL.

```

cwlVersion: v1.2
class: Workflow

inputs:
in_file:
type: File
secondaryFiles: [.fai]

out_filename: string
docker_image: string


outputs:
copied_file:
type: File
outputSource: copy_step/copied_file

steps:
copy_step:
in:
  in_file: in_file
  out_filename: out_filename
  docker_image: docker_image
out: [copied_file]
run: copy.cwl

```

The following file defines the `copy.cwl` task.

```

cwlVersion: v1.2
class: CommandLineTool
baseCommand: cp

inputs:
in_file:
type: File
secondaryFiles: [.fai]
inputBinding:
  position: 1

out_filename:
type: string
inputBinding:
  position: 2
docker_image:
type: string

outputs:
copied_file:
type: File
outputBinding:
    glob: $(inputs.out_filename)

requirements:
InlineJavascriptRequirement: {}
DockerRequirement:
dockerPull: "$(inputs.docker_image)"
```

The following is an example of a workflow written in CWL with a GPU
requirement.

```
cwlVersion: v1.2
class: CommandLineTool
baseCommand: ["/bin/bash", "docm_haplotypeCaller.sh"]
$namespaces:
cwltool: http://commonwl.org/cwltool#
requirements:
cwltool:CUDARequirement:
cudaDeviceCountMin: 1
cudaComputeCapability: "nvidia-tesla-t4"
cudaVersionMin: "1.0"
InlineJavascriptRequirement: {}
InitialWorkDirRequirement:
listing:
- entryname: 'docm_haplotypeCaller.sh'
  entry: |
          nvidia-smi --query-gpu=gpu_name,gpu_bus_id,vbios_version --format=csv

inputs: []
outputs: []
```
