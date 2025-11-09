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
