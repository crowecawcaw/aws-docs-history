# Parameter values elements for job

bundles

You can use the parameters file to set the values of some of the job parameters in the job
template or [CreateJob](../APIReference/API_CreateJob.md "../APIReference/API_CreateJob.md") operation
request arguments in the job bundle so that you don't need to set values when submitting a
job. The UI for job submission enables you to modify these values.

You can define the job template in either YAML format (`parameter_values.yaml`)
or JSON format (`parameter_values.json`). The examples in this section are shown in
YAML format.

In YAML, the format of the file is:

```
parameterValues:
- name: <string>
  value: <integer>, <float>, or <string>
- name: <string>
  value: <integer>, <float>, or <string>ab
... `repeating as necessary`
```

Each element of the `parameterValues` list must be one of the following:

- A job parameter defined in the job template.
- A job parameter defined in a queue environment for the queue that you submit the job
  to..
- A special parameter passed to the `CreateJob` operation when creating a
  job.

      + `deadline:priority` – The value must be an integer. It is passed
       to the `CreateJob` operation as the [priority](../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-priority "../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-priority") parameter.
      + `deadline:targetTaskRunStatus` – The value must be a string. It
       is passed to the `CreateJob` operation as the [targetTaskRunStatus](../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-targetTaskRunStatus "../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-targetTaskRunStatus") parameter.
      + `deadline:maxFailedTasksCount` – The value must be an integer. It
       is passed to the `CreateJob` operation as the [maxFailedTasksCount](../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxFailedTasksCount "../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxFailedTasksCount") parameter.
      + `deadline:maxRetriesPerTask` – The value must be an integer. It
       is passed to the `CreateJob` operation as the [maxRetriesPerTask](../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxRetriesPerTask "../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxRetriesPerTask") parameter.
      + `deadline:maxWorkercount` – The value must be an integer. It is
       passed to the `CreateJob` operation as the [maxWorkerCount](../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxRetriesPerTask "../APIReference/API_CreateJob.md#deadlinecloud-CreateJob-request-maxRetriesPerTask") parameter.

  A job template is always a template rather than a specific job to run. A parameter values
  file enables a job bundle to either act as a template if some parameters don't have values
  defined in this file, or as a specific job submission if all parameters have values.

For example, the [blender_render sample](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_render "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/blender_render") doesn't have a parameters file and its job template defines
parameters with no default values. This template must be used as a template to create jobs.
After you create a job using this job bundle, Deadline Cloud writes a new job bundle to the job history
directory.

For example, when you submit a job with the following command:

```
deadline bundle gui-submit blender_render/
```

The new job bundle contains a `parameter_values.yaml` file that contains the
specified parameters:

```
% cat ~/.deadline/job_history/\(default\)/2024-06/2024-06-20-01-JobBundle-Demo/parameter_values.yaml
parameterValues:
- name: deadline:targetTaskRunStatus
  value: READY
- name: deadline:maxFailedTasksCount
  value: 10
- name: deadline:maxRetriesPerTask
  value: 5
- name: deadline:priority
  value: 75
- name: BlenderSceneFile
  value: /private/tmp/bundle_demo/bmw27_cpu.blend
- name: Frames
  value: 1-10
- name: OutputDir
  value: /private/tmp/bundle_demo/output
- name: OutputPattern
  value: output_####
- name: Format
  value: PNG
- name: CondaPackages
  value: blender
- name: RezPackages
  value: blender
```

You can create the same job with the following command:

```
deadline bundle submit ~/.deadline/job_history/\(default\)/2024-06/2024-06-20-01-JobBundle-Demo/
```

###### Note

The job bundle that you submit is saved to your job history directory. You can find the
location of that directory with the following command:

```
deadline config get settings.job_history_dir
```
