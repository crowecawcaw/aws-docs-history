# Schedule jobs in Deadline Cloud

After you create a job, AWS Deadline Cloud schedules it to be processed on one or more of the
fleets associated with a queue. The fleet that processes a particular task is chosen
based on the scheduling configuration, the capabilities configured for the fleet, and
the host requirements of a specific step.

The following sections provide details of the process of scheduling a job.

## Scheduling configurations

You can configure how Deadline Cloud schedules jobs in a queue by setting a scheduling
configuration on the queue. The scheduling configuration controls how workers are
distributed across jobs.

You can set the scheduling configuration using the Deadline Cloud console or by calling the
[CreateQueue](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md") or
[UpdateQueue](../APIReference/API_UpdateQueue.md "../APIReference/API_UpdateQueue.md") APIs.

There are three available scheduling configurations:

- **Priority, first-in-first-out** (`priorityFifo`) –
  Schedules the highest priority, earliest submitted job first (default).
- **Priority, balanced**
  (`priorityBalanced`) – Distributes workers evenly across jobs at the
  highest priority.
- **Weighted, balanced**
  (`weightedBalanced`) – Uses a weighted formula to determine how
  workers are distributed across jobs.

In all scheduling configurations, in-progress tasks run to completion before a new
scheduling decision is made. If you change the scheduling configuration while tasks are
running, the change applies only when workers are assigned next. Running tasks
are not interrupted or reassigned.

### Priority, first-in-first-out

Priority, first-in-first-out (`priorityFifo`) is the default scheduling configuration
for new queues. Deadline Cloud assigns workers to the highest-priority job first. When multiple
jobs share the same priority, the oldest (earliest submitted) job receives all available
workers first.

Use priority FIFO when you want strict ordering of jobs. This configuration is
appropriate when jobs should complete one at a time in the order they were submitted,
such as sequential pipeline stages or batch processing where each job must finish
before the next one starts.

This configuration has no additional parameters.

### Priority, balanced

Priority, balanced (`priorityBalanced`) distributes workers evenly across
all jobs at the highest priority level. When only one job exists at the highest priority,
Deadline Cloud assigns all workers to that job. When multiple jobs share the highest priority,
workers are split evenly among them. If the workers cannot be evenly divided,
the extra workers are distributed among the highest priority jobs.

Use priority balanced when multiple artists or users submit jobs at the same priority
and each user needs immediate feedback. This configuration ensures that no single job
monopolizes all available workers, so that all users are allocated workers shortly after
submission.

If a job has fewer remaining tasks than its share of workers, the surplus workers are
redistributed to other jobs at the same priority level. If all jobs at the highest
priority are fully allocated, surplus workers cascade to jobs at the next highest
priority level.

This configuration has the following parameter:

`renderingTaskBuffer`

Controls worker stickiness. A worker switches from its current job to another
job at the same priority only if the difference in rendering tasks exceeds the
`renderingTaskBuffer` value. A higher value keeps workers on their
current jobs longer, reducing context switching. The default
value is `1`.

### Weighted, balanced

Weighted, balanced (`weightedBalanced`) uses a formula to calculate a
weight for each job. Deadline Cloud assigns workers to the highest-weight job first. If multiple
jobs have the same weight, workers are distributed among them.

Use weighted balanced when you need fine-grained control over how workers are
distributed across jobs with varying priorities, error rates, and submission times.
This configuration is appropriate for complex render farm environments where you want
to tune the balance between job priority, job age, error handling, and worker
stickiness.

The weight for each job is calculated as follows:

```
weight = (job.Priority * priorityWeight) +
         (job.Errors * errorWeight) +
         ((currentTimeInSeconds - job.SubmissionTime) * submissionTimeWeight) +
         ((job.RenderingTasks - renderingTaskBuffer) * renderingTaskWeight)
```

The `renderingTaskBuffer` component is applied only if the worker is
currently working on the job. The `renderingTaskWeight` is usually set
to a negative value so that jobs with assigned workers receive a lower weight,
bringing other jobs to the front of the queue. The
`errorWeight` is also usually negative so that jobs with errors are
deprioritized. You can use scheduling overrides for minimum and maximum priority
jobs.

This configuration has the following parameters:

`priorityWeight`

The weight applied to a job's priority. A positive value means higher-priority
jobs are scheduled first. The default value is `100.0`. Range:
`0` to `10000`.

`errorWeight`

The weight applied to a job's error count. A negative value means jobs without
errors are scheduled first. The default value is
`-10.0`. Range: `-10000` to `10000`.

`submissionTimeWeight`

The weight applied to a job's submission time (in seconds). A positive value
means earlier submitted jobs are scheduled first. The default value is
`3.0`. Range: `0` to `10000`.

`renderingTaskWeight`

The weight applied to the number of tasks currently rendering for a job. A
negative value means jobs with fewer workers are scheduled next. The
default value is `-100.0`. Range: `-10000` to
`10000`.

`renderingTaskBuffer`

The number of rendering tasks before the rendering task weight takes effect.
A positive value keeps workers on their current jobs. The default value is
`1`. Range: `0` to `1000`.

`maxPriorityOverride`

Optional. When set to `alwaysScheduleFirst`, jobs at the maximum
priority (100) are always scheduled before other jobs, regardless of the weighted
formula. When multiple jobs have the maximum priority, ties are broken using the
standard weighted formula. When the override is absent, maximum priority jobs use
the standard weighted formula with no special treatment.

`minPriorityOverride`

Optional. When set to `alwaysScheduleLast`, jobs at the minimum
priority (0) are always scheduled after other jobs, regardless of the weighted
formula. When multiple jobs have the minimum priority, ties are broken using the
standard weighted formula. When the override is absent, minimum priority jobs use
the standard weighted formula with no special treatment.

## Determine fleet compatibility

Queues and fleets divide the work of routing jobs. A queue organizes jobs and controls
who can submit and view them. Fleets and host requirements select which workers run
each step.

To dedicate specific workers to certain jobs, create a separate fleet for those
workers instead of a separate queue. For example, use a separate fleet for machines with
particular hardware or for machines reserved for sensitive content. One queue can be
associated with several fleets, and each step's host requirements select a compatible
fleet. If you're coming from Deadline 10, fleets and host requirements replace worker
groups. For the full concept mapping, see [Migrate from Deadline 10 to AWS Deadline Cloud](migrate-from-deadline-10.md "migrate-from-deadline-10.md").

After you create a job, Deadline Cloud checks the host requirements for each step in the job
against the capabilities of the fleets associated with the queue the job was submitted to.
If a fleet meets the host requirements, the job is put into the `READY`
state.

If any step in the job has requirements that can't be met by a fleet associated with the
queue, the step's status is set to `NOT_COMPATIBLE`. In addition, the rest of the
steps in the job are canceled. If you associate a compatible fleet with the queue later,
existing `NOT_COMPATIBLE` jobs don't automatically restart – to run them,
requeue them. For more information, see [Modify a job in Deadline Cloud](build-jobs-modifying.md "build-jobs-modifying.md").

Capabilities for a fleet are set at the fleet level. Even if a worker in a fleet meets
the job's requirements, it won't be assigned tasks from the job if its fleet doesn't meet
the job's requirements.

###### Important

The fleet-level `workerCapabilities` declaration is the scheduling
contract. The scheduler evaluates step compatibility exclusively against the fleet-level
capabilities – it does not inspect individual workers. If a step's
`hostRequirements` exceed the minimum values declared in the fleet's
`workerCapabilities`, the fleet is evaluated as not compatible, even
if some individual workers in the fleet would satisfy the requirements.

The following job template has a step that specifies host requirements for the
step:

```
name: Sample Job With Host Requirements
specificationVersion: jobtemplate-2023-09
steps:
- name: Step 1
  script:
    actions:
      onRun:
        args:
        - '1'
        command: /usr/bin/sleep
  hostRequirements:
    amounts:
    # Capabilities starting with "amount." are amount capabilities. If they start with "amount.worker.",
    # they are defined by the OpenJD specification. Other names are free for custom usage.
    - name: amount.worker.vcpu
      min: 4
      max: 8
    attributes:
    - name: attr.worker.os.family
      anyOf:
      - linux
```

This job can be scheduled to a fleet with the following capabilities:

```
{
    "vCpuCount": {"min": 4, "max": 8},
    "memoryMiB": {"min": 1024},
    "osFamily": "linux",
    "cpuArchitectureType": "x86_64"
}
```

This job can't be scheduled to a fleet with any of the following capabilities:

```
{
    "vCpuCount": {"min": 4},
    "memoryMiB": {"min": 1024},
    "osFamily": "linux",
    "cpuArchitectureType": "x86_64"
}
    The vCpuCount has no maximum, so it exceeds the maximum vCPU host requirement.

{
    "vCpuCount": {"max": 8},
    "memoryMiB": {"min": 1024},
    "osFamily": "linux",
    "cpuArchitectureType": "x86_64"
}
    The vCpuCount has no minimum, so it doesn't satisfy the minimum vCPU host requirement.

{
    "vCpuCount": {"min": 4, "max": 8},
    "memoryMiB": {"min": 1024},
    "osFamily": "windows",
    "cpuArchitectureType": "x86_64"
}
    The osFamily doesn't match.
```

### Fleet design best practices

Because the scheduler evaluates compatibility at the fleet level, design your
customer-managed fleets so that the declared `workerCapabilities` represent
the guaranteed minimum hardware characteristics of every worker in the fleet:

- Split workers into multiple fleets based on guaranteed minimum hardware
  characteristics (for example, GPU count, VRAM, or CPU count) rather than using one
  heterogeneous fleet with broad ranges.
- Ensure that each worker in a fleet meets or exceeds the declared minimums, even
  if the workers don't have identical hardware.
- Associate multiple fleets with a single queue so that the scheduler selects a
  compatible fleet based on each step's `hostRequirements`.

For example, if you have workers with 1 GPU (24 GiB VRAM) and workers
with 4 GPUs (96 GiB VRAM), create two separate fleets: one declaring a
minimum of 1 GPU and 24 GiB GPU memory, and another declaring a minimum of
4 GPUs and 96 GiB GPU memory. Then associate both fleets with the same queue.
Steps that require 4 GPUs are automatically routed to the high-GPU fleet.

For more information about creating a customer-managed fleet, see
[Create a customer-managed fleet](create-a-cmf.md "create-a-cmf.md").

### Custom capabilities

In addition to the built-in worker capabilities (vCPU, memory, GPU, operating system,
and CPU architecture), you can define custom amounts and custom attributes on a fleet to
express additional scheduling constraints:

- **Custom amounts** – Numeric values such as
  available disk space or specialized hardware counters.
- **Custom attributes** – String values such as
  installed software, solver versions, or site labels. For example, you can define
  `attr.sw.solvers` with values like `["vray-6", "arnold-7"]`
  to route jobs that require specific software.

At the fleet level, declare software or hardware combinations in custom capabilities
only if they are guaranteed to exist on all workers in that fleet.

Fleet-level custom capabilities have the following limits:

- Maximum of 15 custom amounts per fleet
- Maximum of 15 custom attributes per fleet

Names in the form `amount.worker.*` and `attr.worker.*` are
reserved by the service for built-in capabilities. Use other prefixes for your custom
capabilities.

For more information about configuring custom capabilities when creating a fleet, see
[Create a customer-managed fleet](create-a-cmf.md "create-a-cmf.md").

### GPU memory reporting

When you configure fleets for GPU-intensive workloads that require a specific per-GPU
VRAM threshold, understand how the worker agent reports GPU memory.

The Deadline Cloud worker agent reports the _minimum_ GPU memory across all
GPUs on the worker into `amount.worker.gpu.memory`, not the total sum. This
behavior ensures that jobs requiring a specific per-GPU VRAM amount are routed to workers
where every GPU meets that requirement.

For example, if a worker has two GPUs with 24 GiB and 48 GiB of VRAM
respectively, the worker agent reports 24 GiB as the GPU memory value.

At the fleet level, set the `acceleratorTotalMemoryMiB` minimum to the
lowest per-GPU VRAM that any worker in the fleet is guaranteed to have.

### Per-worker capabilities

When you need to track operational state for individual workers without affecting
scheduling decisions, use per-worker capabilities. For example, you might flag workers
for maintenance, track software rollout state, or record health check indicators.

You can set capabilities on individual workers using the
`UpdateWorker` API operation. Per-worker capabilities are
_not_ used as the scheduling contract. The scheduler evaluates
compatibility exclusively against the fleet-level `workerCapabilities`
declaration.

The `GetWorker` and `ListWorkers` operations don't return
worker capabilities that are set through `UpdateWorker`.

For more information, see [UpdateWorker](../APIReference/API_UpdateWorker.md "../APIReference/API_UpdateWorker.md") in
the _Deadline Cloud API Reference_.

## Fleet scaling

When a job is assigned to a compatible service-managed fleet, the fleet is auto scaled.
The number of workers in the fleet changes based on the number of tasks available for the
fleet to run.

When a job is assigned to a customer-managed fleet, workers might already exist or can
be created using event-based auto scaling. For more information, see [Use EventBridge
to handle auto scaling events](../../../autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.md "../../../autoscaling/ec2/userguide/automating-ec2-auto-scaling-with-eventbridge.md") in the _Amazon EC2 Auto Scaling User
Guide_.

## Sessions

The tasks in a job are divided into one or more sessions. Workers run the sessions to
set up the environment, run the tasks, and then tear down the environment. Each session is
composed of one or more actions that a worker must take.

As a worker completes section actions, additional session actions can be sent to the
worker. The worker reuses existing environments and job attachments in the session to
complete tasks more efficiently.

On service-managed fleet workers, session directories are deleted after the session ends,
but other directories are retained between sessions. This behavior allows you to implement caching strategies
for data that can be reused across multiple sessions. To cache data between sessions, store it
under the home directory of the user running the job. For example, conda packages are cached under
the job user's home directory at `C:\Users\job-user\.conda-pkgs` on Windows workers and
`/home/job-user/.conda-pkgs` on Linux workers. This data remains available until the
worker shuts down.

Job attachments are created by the submitter that you use as part of your Deadline Cloud CLI job
bundle. You can also create job attachments using the `--attachments` option for
the `create-job` AWS CLI command. Environments are defined in two places: queue
environments attached to a specific queue, and job and step environments defined in the job
template.

There are four session action types:

- `syncInputJobAttachments` – Downloads the input job attachments to
  the worker.
- `envEnter` – Performs the `onEnter` actions for an
  environment.
- `taskRun` – Performs the `onRun` actions for a
  task.
- `envExit` – Performs the `onExit` actions for an
  environment.

The following job template has a step environment. It has an `onEnter`
definition to set up the step environment, an `onRun` definition that defines the
task to run, and an `onExit` definition to tear down the step environment. The
sessions created for this job will include an `envEnter` action, one or more
`taskRun` actions, and then an `envExit` action.

```
name: Sample Job with Maya Environment
specificationVersion: jobtemplate-2023-09
steps:
- name: Maya Step
  stepEnvironments:
  - name: Maya
    description: Runs Maya in the background.
    script:
      embeddedFiles:
      - name: initData
        filename: init-data.yaml
        type: TEXT
        data: |
          scene_file: MyAwesomeSceneFile
          renderer: arnold
          camera: persp
      actions:
        onEnter:
          command: MayaAdaptor
          args:
          - daemon
          - start
          - --init-data
          - file://{{Env.File.initData}}
        onExit:
          command: MayaAdaptor
          args:
          - daemon
          - stop
  parameterSpace:
    taskParameterDefinitions:
    - name: Frame
      range: 1-5
      type: INT
  script:
    embeddedFiles:
    - name: runData
      filename: run-data.yaml
      type: TEXT
      data: |
        frame: {{Task.Param.Frame}}
    actions:
      onRun:
        command: MayaAdaptor
        args:
        - daemon
        - run
        - --run-data
        - file://{{ Task.File.runData }}
```

### Session actions pipelining

Session actions pipelining lets a scheduler pre-assign multiple session actions
to a worker. The worker can then run these actions sequentially, reducing or eliminating
idle time between tasks.

To create an initial assignment, the scheduler creates a session with one task, the
worker completes the task, and then the scheduler analyzes the task duration to determine
future assignments.

For the scheduler to be effective, there are task duration rules. For tasks under one
minute, the scheduler uses a power-of-2 growth pattern. For example, for a 1-second task,
the scheduler assigns 2 new tasks, then 4, then 8. For tasks over one minute, the
scheduler assigns only one new task and pipelining remains disabled.

To calculate pipeline size, the scheduler does the following:

- Uses average task duration from completed tasks
- Aims to keep the worker busy for one minute
- Considers only tasks within the same session
- Does not share duration data across workers

With session actions piplelining, workers start new tasks immediately and there's no
waiting time between scheduler requests. It also provides improved worker efficiency
and better task distribution for long-running processes.

Additionally, if there is a new higher priority job available, the worker will finish all
of its previously assigned work before its current session ends and a new session from a higher
priority job is assigned.

## Step dependencies

Deadline Cloud supports defining dependencies between steps so that one step waits until another
step is complete before starting. You can define more than one dependency for a step. A step
with a dependency isn't scheduled until all of its dependencies are complete.

If the job template defines a circular dependency, the job is rejected and the job
status is set to `CREATE_FAILED`.

The following job template creates a job with two steps. `StepB` depends on
`StepA`. `StepB` only runs after `StepA` completes
successfully.

After the job is created, `StepA` is in the `READY` state and
`StepB` is in the `PENDING` state. After `StepA`
finishes, `StepB` moves to the `READY` state. If `StepA`
fails, or if `StepA` is canceled, `StepB` moves to the
`CANCELED` state.

You can set a dependency on multiple steps. For example, if `StepC` depends
on both `StepA` and `StepB`, `StepC` won't start until the
other two steps finish.

Step dependencies have the following restrictions:

- **Dependencies per step** – A step can depend on a
  maximum of 128 other steps.
- **Consumers per step** – A maximum of 32 other steps
  can depend on a single step.

```
name: Step-Step Dependency Test
specificationVersion: 'jobtemplate-2023-09'
steps:
- name: A
  script:
    actions:
      onRun:
        command: bash
        args: ['{{ Task.File.run }}']
    embeddedFiles:
      - name: run
        type: TEXT
        data: |
          #!/bin/env bash

          set -euo pipefail

          sleep 1
          echo Task A Done!
- name: B
  dependencies:
  - dependsOn: A # This means Step B depends on Step A
  script:
    actions:
      onRun:
        command: bash
        args: ['{{ Task.File.run }}']
    embeddedFiles:
      - name: run
        type: TEXT
        data: |
          #!/bin/env bash

          set -euo pipefail

          sleep 1
          echo Task B Done!
```
