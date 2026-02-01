# Schedule jobs in Deadline Cloud

After a job is created, AWS Deadline Cloud schedules it to be processed on one or more of the
fleets associated with a queue. The fleet that processes a particular task is chosen based on
the capabilities configured for the fleet and the host requirements of a specific step.

Jobs in a queue are scheduled in a best-effort priority order, highest to lowest. When two
jobs have the same priority, the oldest job is scheduled first.

The following sections provide details of the process of scheduling a job.

## Determine fleet compatibility

After a job is created, Deadline Cloud checks the host requirements for each step in the job
against the capabilities of the fleets associated with the queue the job was submitted to.
If a fleet meets the host requirements, the job is put into the `READY`
state.

If any step in the job has requirements that can't be met by a fleet associated with the
queue, the step's status is set to `NOT_COMPATIBLE`. In addition, the rest of the
steps in the job are canceled.

Capabilities for a fleet are set at the fleet level. Even if a worker in a fleet meets
the job's requirements, it won't be assigned tasks from the job if its fleet doesn't meet
the job's requirements.

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
