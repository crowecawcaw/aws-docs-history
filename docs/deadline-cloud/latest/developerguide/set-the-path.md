# Set the path in a queue environment

Use OpenJD environments to provide new commands in an environment. First you create a
 directory containing script files, and then add that directory to the `PATH`
 environment variables so that executables in your script can run them without needing to
 specify the directory path each time. The list of variables in an environment definition
 doesn’t provide a way to modify the variable, so you do this by running a script instead.
 After the script sets things up and modifies the `PATH`, it exports the variable to
 the OpenJD runtime with the command `echo "openjd_env: PATH=$PATH"`. 


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

## Run the path sample



1. Use the Deadline Cloud CLI to submit the `job_env_with_new_command`
 sample.



```
 $ deadline bundle submit job_env_with_new_command
 Submitting to Queue: MySampleQueue
 ...
```
2. In the Deadline Cloud monitor, you will see the new job and can monitor its progress. Once
 the Linux fleet associated with the queue has a worker available to run the job’s
 task, the job completes in a few seconds. Select the task, then choose the
 **View logs** option in the top right menu of the tasks panel. 


 On the right are two session actions, **Launch
 RandomSleepCommand** and **Task run**. The log viewer in the
 center of the window corresponds to the selected session action on the right.

## Compare session actions with their definitions


In this section you use the Deadline Cloud monitor to compare the session actions with where they
 are defined in the job template. It continues from the previous section. 


Open the file [job\_env\_with\_new\_command/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_with_new_command/template.yaml") in a text editor. Compare the session
 actions to where they are defined in the job template. 



1. Select the **Launch RandomSleepCommand** session action in the
 Deadline Cloud monitor. You will see log output as follows.



```
 2024/07/16 17:25:32-07:00
 2024/07/16 17:25:32-07:00 ==============================================
 2024/07/16 17:25:32-07:00 --------- Entering Environment: RandomSleepCommand
 2024/07/16 17:25:32-07:00 ==============================================
 2024/07/16 17:25:32-07:00 ----------------------------------------------
 2024/07/16 17:25:32-07:00 Phase: Setup
 2024/07/16 17:25:32-07:00 ----------------------------------------------
 2024/07/16 17:25:32-07:00 Writing embedded files for Environment to disk.
 2024/07/16 17:25:32-07:00 Mapping: Env.File.Enter -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmpbt8j_c3f
 2024/07/16 17:25:32-07:00 Mapping: Env.File.SleepScript -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmperastlp4
 2024/07/16 17:25:32-07:00 Wrote: Enter -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmpbt8j_c3f
 2024/07/16 17:25:32-07:00 Wrote: SleepScript -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmperastlp4
 2024/07/16 17:25:32-07:00 ----------------------------------------------
 2024/07/16 17:25:32-07:00 Phase: Running action
 2024/07/16 17:25:32-07:00 ----------------------------------------------
 2024/07/16 17:25:32-07:00 Running command sudo -u job-user -i setsid -w /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/tmpbwrquq5u.sh
 2024/07/16 17:25:32-07:00 Command started as pid: 2205
 2024/07/16 17:25:32-07:00 Output:
 2024/07/16 17:25:33-07:00 openjd_env: PATH=/sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/bin:/opt/conda/condabin:/home/job-user/.local/bin:/home/job-user/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/var/lib/snapd/snap/bin
 No newer logs at this moment.
```

 The following lines from the job template specified this action.



```
 jobEnvironments:
 - name: RandomSleepCommand
   description: Adds a command 'random-sleep' to the environment.
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

         # Make a bin directory inside the session's working directory for providing new commands
         mkdir -p '{{Session.WorkingDirectory}}/bin'

         # If this bin directory is not already in the PATH, then add it
         if ! [[ ":$PATH:" == *':{{Session.WorkingDirectory}}/bin:'* ]]; then
           export "PATH={{Session.WorkingDirectory}}/bin:$PATH"

           # This message to Open Job Description exports the new PATH value to the environment
           echo "openjd_env: PATH=$PATH"
         fi

         # Copy the SleepScript embedded file into the bin directory
         cp '{{Env.File.SleepScript}}' '{{Session.WorkingDirectory}}/bin/random-sleep'
         chmod u+x '{{Session.WorkingDirectory}}/bin/random-sleep'
     - name: SleepScript
       type: TEXT
       runnable: true
       data: |
         ...
```
2. Select the **Launch StepEnv** session action in the Deadline Cloud monitor.
 You see log output as follows. 



```
 2024/07/16 17:25:33-07:00
 2024/07/16 17:25:33-07:00 ==============================================
 2024/07/16 17:25:33-07:00 --------- Running Task
 2024/07/16 17:25:33-07:00 ==============================================
 2024/07/16 17:25:33-07:00 ----------------------------------------------
 2024/07/16 17:25:33-07:00 Phase: Setup
 2024/07/16 17:25:33-07:00 ----------------------------------------------
 2024/07/16 17:25:33-07:00 Writing embedded files for Task to disk.
 2024/07/16 17:25:33-07:00 Mapping: Task.File.Run -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmpdrwuehjf
 2024/07/16 17:25:33-07:00 Wrote: Run -> /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/embedded_filesf3tq_1os/tmpdrwuehjf
 2024/07/16 17:25:33-07:00 ----------------------------------------------
 2024/07/16 17:25:33-07:00 Phase: Running action
 2024/07/16 17:25:33-07:00 ----------------------------------------------
 2024/07/16 17:25:33-07:00 Running command sudo -u job-user -i setsid -w /sessions/session-ab132a51b9b54d5da22cbe839dd946baaw1c8hk5/tmpz81iaqfw.sh
 2024/07/16 17:25:33-07:00 Command started as pid: 2256
 2024/07/16 17:25:33-07:00 Output:
 2024/07/16 17:25:34-07:00 + random-sleep 12.5 27.5
 2024/07/16 17:26:00-07:00 Sleeping for duration 26.90
 2024/07/16 17:26:00-07:00 ----------------------------------------------
 2024/07/16 17:26:00-07:00 Uploading output files to Job Attachments
 2024/07/16 17:26:00-07:00 ----------------------------------------------
```
3. The following lines from the job template specified this action.



```
 steps:
 - name: EnvWithCommand
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
         set -xeuo pipefail

         # Run the script installed into PATH by the job environment
         random-sleep 12.5 27.5
   hostRequirements:
     attributes:
     - name: attr.worker.os.family
       anyOf:
       - linux
```
