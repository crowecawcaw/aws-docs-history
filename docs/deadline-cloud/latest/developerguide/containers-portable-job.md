

# Run a portable job locally and in a container
<a name="containers-portable-job"></a>

A portable job template defines the application command and arguments without selecting the runtime. The following example requires `bash`. It doesn't contain Docker commands, an image URI, or Amazon ECR authentication.

## Prerequisites
<a name="containers-portable-prerequisites"></a>

Install the OpenJD CLI and the Deadline Cloud CLI. Complete [Set up container support in the console](containers-console-setup.md) and use an image that provides `bash`.

## Run the job template
<a name="containers-portable-procedure"></a>

**To run a portable job locally and on Deadline Cloud**

1. Create a directory named `portable-container-job` and save the following content as `template.yaml` in that directory.

   ```
   specificationVersion: jobtemplate-2023-09
   name: Portable container job
   parameterDefinitions:
     - name: Message
       type: STRING
       default: Hello from a portable OpenJD job
   steps:
     - name: PrintMessage
       script:
         actions:
           onRun:
             command: bash
             args:
               - "{{Task.File.Run}}"
               - "{{Param.Message}}"
         embeddedFiles:
           - name: Run
             filename: run.sh
             type: TEXT
             data: |
               #!/usr/bin/env bash
               set -euo pipefail
               printf '%s\n' "$1"
   ```

1. Validate the job template.

   ```
   openjd check portable-container-job/template.yaml
   ```

1. Run the job directly on your workstation.

   ```
   openjd run portable-container-job/template.yaml \
       -p Message="Local execution"
   ```

   Verify that the output contains `Local execution`.

1. Configure the Deadline Cloud CLI to use the Docker-enabled queue, and submit the unchanged job bundle.

   ```
   deadline bundle submit portable-container-job \
       -p Message="Container execution"
   ```

1. Open the job in the Deadline Cloud monitor, select the task, and view its session log. Confirm that the log contains `Container execution`.

The queue environment selects the Docker image and redirects the action into its session container. If you remove the wrapping environment, the same command runs directly on a compatible worker.