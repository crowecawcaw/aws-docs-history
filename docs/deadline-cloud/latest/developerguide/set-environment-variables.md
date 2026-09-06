

# Set environment variables in a queue environment
<a name="set-environment-variables"></a>

Many applications and frameworks use environment variables to control feature settings, logging levels, and display configuration. You can use Open Job Description (OpenJD) environments to set environment variables that every task command within their scope inherits. For more information, see [Environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment) on the GitHub website.

## Environment variable scope
<a name="set-env-vars-scope"></a>

AWS Deadline Cloud applies environment variables from queue environments that you attach to a queue. Within a job template, you can also define environment variables at the job and step levels using OpenJD environments. For more information, see [Environments](https://github.com/OpenJobDescription/openjd-specifications/wiki/2023-09-Template-Schemas#4-environment) on the GitHub website. Variables defined at a narrower scope override variables with the same name from a broader scope.
+ **Queue environment** – A template that you attach to a queue in Deadline Cloud. Variables apply to all jobs submitted to the queue. You can set variables with a `variables` map for fixed values, or use scripts for dynamic values.
+ **Job environment** – Defined under `jobEnvironments` in a job template. Variables apply to all steps and tasks in the job. A job-level variable overrides a queue-level variable with the same name.
+ **Step environment** – Defined under `stepEnvironments` in a job template. Variables apply only to the tasks in that step. A step-level variable overrides a job-level or queue-level variable with the same name.

## Setting variables in a queue environment
<a name="set-env-vars-queue-env"></a>

You can set environment variables in a queue environment using a `variables` map for fixed values, or using a `script` with an `onEnter` action for dynamic values.

The following queue environment template uses a `variables` map to set the `QT_QPA_PLATFORM` variable to `offscreen`, which allows applications that use the Qt Framework to run on worker hosts without an interactive display. For more information, see the [Qt Framework](https://www.qt.io/product/framework) on the Qt website.

```
specificationVersion: 'environment-2023-09'
environment:
  name: QtOffscreen
  variables:
    QT_QPA_PLATFORM: offscreen
```

For dynamic values, such as modifying `PATH` or activating virtual environments, use a script that prints lines in the format `openjd_env: {{VAR}}={{value}}` to stdout. The `openjd_env:` prefix is required. Using `echo`, `export`, or other shell mechanisms without the prefix does not propagate variables to jobs and tasks.

The following queue environment template sets the `QT_QPA_PLATFORM` variable using a script.

```
specificationVersion: 'environment-2023-09'
environment:
  name: QtOffscreen
  script:
    actions:
      onEnter:
        command: bash
        args:
        - "{{Env.File.Enter}}"
    embeddedFiles:
    - name: Enter
      type: TEXT
      data: |
        #!/bin/env bash
        set -euo pipefail
        echo "openjd_env: QT_QPA_PLATFORM=offscreen"
```

To attach a queue environment to your queue, use the Deadline Cloud console or the AWS CLI. For more information, see [Create a queue environment](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html) in the AWS Deadline Cloud User Guide. The following AWS CLI command creates a queue environment from a template file.

```
aws deadline create-queue-environment \
    --farm-id {{FARM_ID}} \
    --queue-id {{QUEUE_ID}} \
    --priority 1 \
    --template-type YAML \
    --template file://{{my-queue-env.yaml}}
```

For more complex examples, such as creating and activating conda virtual environments, see the [Deadline Cloud queue environment samples](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/queue_environments) on the GitHub website.

## Setting variables in a job template
<a name="set-env-vars-job-template"></a>

In a job template, add a `variables` map to a `jobEnvironments` or `stepEnvironments` entry. Each entry is a key-value pair where the key is the variable name and the value is the variable value.

The following job template sets the `QT_QPA_PLATFORM` environment variable to `offscreen`, which allows applications that use the Qt Framework to run on worker hosts without an interactive display. For more information, see the [Qt Framework](https://www.qt.io/product/framework) on the Qt website.

```
specificationVersion: 'jobtemplate-2023-09'
name: MyJob
jobEnvironments:
- name: JobEnv
  variables:
    QT_QPA_PLATFORM: offscreen
```

You can set multiple variables in a single environment definition.

```
jobEnvironments:
- name: JobEnv
  variables:
    JOB_VERBOSITY: MEDIUM
    JOB_PROJECT_ID: {{my-project-id}}
    JOB_ENDPOINT_URL: {{https://my-host-name/my/path}}
    QT_QPA_PLATFORM: offscreen
```

You can reference job parameters in variable values by using the `{{Param.{{ParameterName}}}}` syntax.

```
jobEnvironments:
- name: JobEnv
  variables:
    JOB_EXAMPLE_PARAM: "{{Param.ExampleParam}}"
```

To override a job-level variable for a specific step, define a `stepEnvironments` entry with the same variable name. The following example defines `JOB_PROJECT_ID` at the job level with the value `project-12`, and then overrides the value at the step level with `step-project-12`. Tasks in the step use the step-level value.

```
specificationVersion: 'jobtemplate-2023-09'
name: MyJob
jobEnvironments:
- name: JobEnv
  variables:
    JOB_PROJECT_ID: project-12
steps:
- name: MyStep
  stepEnvironments:
  - name: StepEnv
    variables:
      JOB_PROJECT_ID: step-project-12
```

## Try it: Running the environment variable sample
<a name="set-env-vars-example"></a>

The Deadline Cloud samples repository includes a [job bundle that demonstrates setting and viewing environment variables](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml) on the GitHub website. The sample job template defines variables at both the job and step levels, then runs a task that prints the merged result. Use the following procedure to run the sample and inspect the results.

### Prerequisites
<a name="set-prerequisites"></a>

1. If you do not have a Deadline Cloud farm with a queue and associated Linux fleet, follow the guided onboarding experience in the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home) to create one with default settings.

1. If you do not have the Deadline Cloud CLI and AWS Deadline Cloud monitor on your workstation, follow the steps in [Set up Deadline Cloud submitters](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/submitter.html).

1. Use `git` to clone the [Deadline Cloud samples GitHub repository](https://github.com/aws-deadline/deadline-cloud-samples) on the GitHub website.

   ```
   git clone https://github.com/aws-deadline/deadline-cloud-samples.git
   cd deadline-cloud-samples/job_bundles
   ```

### Running the sample
<a name="set-run-example"></a>

1. Use the Deadline Cloud CLI to submit the `job_env_vars` sample.

   ```
   deadline bundle submit job_env_vars
   ```

1. In the Deadline Cloud monitor, select the new job to monitor its progress. After the Linux fleet associated with the queue has a worker available, the job completes in a few seconds. Select the task, then choose **View logs** in the top right menu of the tasks panel.

### Comparing session actions with their definitions
<a name="set-compare-actions"></a>

The log view shows three session actions. Open the file [job\_env\_vars/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_vars/template.yaml) on the GitHub website in a text editor to compare each action with its definition in the job template.

1. Select the **Launch JobEnv** session action. The log output shows the job-level environment variables being set.

   ```
   Setting: JOB_VERBOSITY=MEDIUM
   Setting: JOB_EXAMPLE_PARAM=An example parameter value
   Setting: JOB_PROJECT_ID=project-12
   Setting: JOB_ENDPOINT_URL=https://internal-host-name/some/path
   Setting: QT_QPA_PLATFORM=offscreen
   ```

   The following lines from the job template define this environment.

   ```
   jobEnvironments:
   - name: JobEnv
     variables:
       JOB_VERBOSITY: MEDIUM
       JOB_EXAMPLE_PARAM: "{{Param.ExampleParam}}"
       JOB_PROJECT_ID: project-12
       JOB_ENDPOINT_URL: https://internal-host-name/some/path
       QT_QPA_PLATFORM: offscreen
   ```

1. Select the **Launch StepEnv** session action. The log output shows the step-level variables, including the overridden `JOB_PROJECT_ID`.

   ```
   Setting: STEP_VERBOSITY=HIGH
   Setting: JOB_PROJECT_ID=step-project-12
   ```

   The following lines from the job template define this environment.

   ```
   stepEnvironments:
   - name: StepEnv
     variables:
       STEP_VERBOSITY: HIGH
       JOB_PROJECT_ID: step-project-12
   ```

1. Select the **Task run** session action. The log output shows the merged environment variables available to the task. Notice that `JOB_PROJECT_ID` uses the step-level value `step-project-12`.

   ```
   Environment variables starting with JOB_*:
   JOB_ENDPOINT_URL=https://internal-host-name/some/path
   JOB_EXAMPLE_PARAM='An example parameter value'
   JOB_PROJECT_ID=step-project-12
   JOB_VERBOSITY=MEDIUM
   
   Environment variables starting with STEP_*:
   STEP_VERBOSITY=HIGH
   ```