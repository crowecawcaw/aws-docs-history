# Set environment variables in a queue

environment

[Open Job Description (OpenJD) environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment "https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment") can set environment variables that every
task command within their scope uses. Many applications and frameworks check for environment
variables to control feature settings, logging level, and more.

For example, the [Qt Framework](https://www.qt.io/product/framework "https://www.qt.io/product/framework")
provides GUI functionality for many desktop applications. When you run these applications on a
worker host without an interactive display, you may need to set the environment variable
`QT_QPA_PLATFORM` to `offscreen` so the worker doesn’t look for a
display.

In this example, you'll use a sample job bundle from the Deadline Cloud samples directory to set
and view the environment variables for a job.

## Prerequisites

Perform the following steps to run the [sample job bundle with environment variables](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml") from the Deadline Cloud samples github
repository.

1. If you do not have a Deadline Cloud farm with a queue and associated Linux fleet, follow the
   guided onboarding experience in the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home") to
   create one with default settings.
2. If you do not have the Deadline Cloud CLI and Deadline Cloud monitor on your workstation, follow the
   steps in [Set
   up Deadline Cloud submitters](../userguide/submitter.md "../userguide/submitter.md") from the user guide.
3. Use `git` to clone the [Deadline Cloud samples GitHub
   repository](https://github.com/aws-deadline/deadline-cloud-samples "https://github.com/aws-deadline/deadline-cloud-samples").

```
git clone https://github.com/aws-deadline/deadline-cloud-samples.git
 `Cloning into 'deadline-cloud-samples'...
 ...`
cd deadline-cloud-samples/job_bundles
```

## Run the environment variable sample

1. Use the Deadline Cloud CLI to submit the `job_env_vars` sample.

```
deadline bundle submit job_env_vars
 `Submitting to Queue: MySampleQueue
 ...`
```

2. In the Deadline Cloud monitor, you can see the new job and monitor its progress. After the
   Linux fleet associated with the queue has a worker available to run the job’s task,
   the job completes in a few seconds. Select the task, then choose the **View
   logs** option in the top right menu of the tasks panel.

On the right are three session actions, **Launch JobEnv**,
**Launch StepEnv**, and **Task run**. The log view
in the center of the window corresponds to the selected session action on the right.

## Compare the session actions with their

definitions

In this section you use the Deadline Cloud monitor to compare the session actions with where they
are defined in the job template. It continues from the previous section.

Open the file [job_env_vars/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml") in a text editor. This is the job template that
defines the session actions.

1. Select the **Launch JobEnv** session action in Deadline Cloud monitor. You
   will see the following log output.

```
 024/07/16 16:18:27-07:00
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 --------- Entering Environment: JobEnv
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 Setting: JOB_VERBOSITY=MEDIUM
 2024/07/16 16:18:27-07:00 Setting: JOB_EXAMPLE_PARAM=An example parameter value
 2024/07/16 16:18:27-07:00 Setting: JOB_PROJECT_ID=project-12
 2024/07/16 16:18:27-07:00 Setting: JOB_ENDPOINT_URL=https://internal-host-name/some/path
 2024/07/16 16:18:27-07:00 Setting: QT_QPA_PLATFORM=offscreen
```

The following lines from the job template specified this action.

```
jobEnvironments:
 - name: JobEnv
   description: Job environments apply to everything in the job.
   variables:
     # When applications have options as environment variables, you can set them here.
     JOB_VERBOSITY: MEDIUM
     # You can use the value of job parameters when setting environment variables.
     JOB_EXAMPLE_PARAM: "{{Param.ExampleParam}}"
     # Some more ideas.
     JOB_PROJECT_ID: project-12
     JOB_ENDPOINT_URL: https://internal-host-name/some/path
     # This variable lets applications using the Qt Framework run without a display
     QT_QPA_PLATFORM: offscreen
```

2. Select the **Launch StepEnv** session action in Deadline Cloud monitor. You
   will see the following log output.

```
 2024/07/16 16:18:27-07:00
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 --------- Entering Environment: StepEnv
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 Setting: STEP_VERBOSITY=HIGH
 2024/07/16 16:18:27-07:00 Setting: JOB_PROJECT_ID=step-project-12
```

The following lines from the job template specified this action.

```
   stepEnvironments:
   - name: StepEnv
     description: Step environments apply to all the tasks in the step.
     variables:
       # These environment variables are only set within this step, not other steps.
       STEP_VERBOSITY: HIGH
       # Replace a variable value defined at the job level.
       JOB_PROJECT_ID: step-project-12
```

3. Select the **Task run** session action in Deadline Cloud monitor. You will
   see the following output.

```
 2024/07/16 16:18:27-07:00
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 --------- Running Task
 2024/07/16 16:18:27-07:00 ==============================================
 2024/07/16 16:18:27-07:00 ----------------------------------------------
 2024/07/16 16:18:27-07:00 Phase: Setup
 2024/07/16 16:18:27-07:00 ----------------------------------------------
 2024/07/16 16:18:27-07:00 Writing embedded files for Task to disk.
 2024/07/16 16:18:27-07:00 Mapping: Task.File.Run -> /sessions/session-b4bd451784674c0987be82c5f7d5642deupf6tk9/embedded_files08cdnuyt/tmpmdiajwvh
 2024/07/16 16:18:27-07:00 Wrote: Run -> /sessions/session-b4bd451784674c0987be82c5f7d5642deupf6tk9/embedded_files08cdnuyt/tmpmdiajwvh
 2024/07/16 16:18:27-07:00 ----------------------------------------------
 2024/07/16 16:18:27-07:00 Phase: Running action
 2024/07/16 16:18:27-07:00 ----------------------------------------------
 2024/07/16 16:18:27-07:00 Running command sudo -u job-user -i setsid -w /sessions/session-b4bd451784674c0987be82c5f7d5642deupf6tk9/tmpiqbrsby4.sh
 2024/07/16 16:18:27-07:00 Command started as pid: 2176
 2024/07/16 16:18:27-07:00 Output:
 2024/07/16 16:18:28-07:00 Running the task
 2024/07/16 16:18:28-07:00
 2024/07/16 16:18:28-07:00 Environment variables starting with JOB_*:
 2024/07/16 16:18:28-07:00 JOB_ENDPOINT_URL=https://internal-host-name/some/path
 2024/07/16 16:18:28-07:00 JOB_EXAMPLE_PARAM='An example parameter value'
 2024/07/16 16:18:28-07:00 JOB_PROJECT_ID=step-project-12
 2024/07/16 16:18:28-07:00 JOB_VERBOSITY=MEDIUM
 2024/07/16 16:18:28-07:00
 2024/07/16 16:18:28-07:00 Environment variables starting with STEP_*:
 2024/07/16 16:18:28-07:00 STEP_VERBOSITY=HIGH
 2024/07/16 16:18:28-07:00
 2024/07/16 16:18:28-07:00 Done running the task
 2024/07/16 16:18:28-07:00 ----------------------------------------------
 2024/07/16 16:18:28-07:00 Uploading output files to Job Attachments
 2024/07/16 16:18:28-07:00 ----------------------------------------------
```

The following lines from the job template specified this action.

```
   script:
     actions:
       onRun:
         command: bash
         args:
         - '{{Task.File.Run}}'
     embeddedFiles:
     - name: Run
       type: TEXT
       data: |
         echo Running the task
         echo ""

         echo Environment variables starting with JOB_*:
         set | grep ^JOB_
         echo ""

         echo Environment variables starting with STEP_*:
         set | grep ^STEP_
         echo ""

         echo Done running the task

```
