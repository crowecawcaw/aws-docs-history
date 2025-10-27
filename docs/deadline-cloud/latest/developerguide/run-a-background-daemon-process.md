# Run a background daemon process from the

queue environment

In many rendering use cases, loading the application and scene data can take a
significant amount of time. If a job reloads them for every frame, it will spend most of its
time on overhead. It’s often possible to load the application once as a background daemon
process, have it load the scene data, and then send it commands via inter-process
communication (IPC) to perform the renders.

Many of the open source Deadline Cloud integrations use this pattern. The Open Job Description
project provides an [adaptor
runtime library](https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python "https://github.com/OpenJobDescription/openjd-adaptor-runtime-for-python") with robust IPC patterns on all supported operating systems.

To demonstrate this pattern, there is a [self-contained sample job bundle](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml") that uses Python and bash code to implement a
background daemon and the IPC for tasks to communicate with it. The daemon is implemented in
Python, and listens for a POSIX SIGUSR1 signal for when to process a task. The task details
are passed to the daemon in a specific JSON file, and the results of running the task are
returned as another JSON file.

## Prerequisites

Perform the following steps to run the [sample job bundle with a daemon process](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml") from the Deadline Cloud samples github repository.

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

## Run the daemon sample

1. Use the Deadline Cloud CLI to submit the `job_env_daemon_process` sample.

```
 git clone https://github.com/aws-deadline/deadline-cloud-samples.git
`Cloning into 'deadline-cloud-samples'...
 ...`
cd deadline-cloud-samples/job_bundles
```

2. In the Deadline Cloud monitor application, you will see the new job and can monitor its
   progress. Once the Linux fleet associated with the queue has a worker available to run
   the job’s task, it completes in about a minute. With one of the tasks selected, choose
   the **View logs** option in the top right menu of the tasks panel.

On the right there are two session actions, **Launch
DaemonProcess** and **Task run**. The log viewer in the
center of the window corresponds to the selected session action on the right.

Select the option **View logs for all tasks**. The timeline shows
the rest of the tasks that ran as part of the session, and the `Shut down
 DaemonProcess` action that exited the environment.

## View the daemon logs

1. In this section you use the Deadline Cloud monitor to compare the session actions with where
   they are defined in the job template. It continues from the previous section.

Open the file [job_env_daemon_process/template.yaml](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/job_env_daemon_process/template.yaml") in a text editor. Compare the session
actions to where they are defined in the job template. 2. Select the `Launch DaemonProcess` session action in Deadline Cloud monitor. You
will see log output as follows.

```
 2024/07/17 16:27:20-07:00
 2024/07/17 16:27:20-07:00 ==============================================
 2024/07/17 16:27:20-07:00 --------- Entering Environment: DaemonProcess
 2024/07/17 16:27:20-07:00 ==============================================
 2024/07/17 16:27:20-07:00 ----------------------------------------------
 2024/07/17 16:27:20-07:00 Phase: Setup
 2024/07/17 16:27:20-07:00 ----------------------------------------------
 2024/07/17 16:27:20-07:00 Writing embedded files for Environment to disk.
 2024/07/17 16:27:20-07:00 Mapping: Env.File.Enter -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/enter-daemon-process-env.sh
 2024/07/17 16:27:20-07:00 Mapping: Env.File.Exit -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/exit-daemon-process-env.sh
 2024/07/17 16:27:20-07:00 Mapping: Env.File.DaemonScript -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/daemon-script.py
 2024/07/17 16:27:20-07:00 Mapping: Env.File.DaemonHelperFunctions -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/daemon-helper-functions.sh
 2024/07/17 16:27:20-07:00 Wrote: Enter -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/enter-daemon-process-env.sh
 2024/07/17 16:27:20-07:00 Wrote: Exit -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/exit-daemon-process-env.sh
 2024/07/17 16:27:20-07:00 Wrote: DaemonScript -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/daemon-script.py
 2024/07/17 16:27:20-07:00 Wrote: DaemonHelperFunctions -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/daemon-helper-functions.sh
 2024/07/17 16:27:20-07:00 ----------------------------------------------
 2024/07/17 16:27:20-07:00 Phase: Running action
 2024/07/17 16:27:20-07:00 ----------------------------------------------
 2024/07/17 16:27:20-07:00 Running command sudo -u job-user -i setsid -w /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/tmp_u8slys3.sh
 2024/07/17 16:27:20-07:00 Command started as pid: 2187
 2024/07/17 16:27:20-07:00 Output:
 2024/07/17 16:27:21-07:00 openjd_env: DAEMON_LOG=/sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/daemon.log
 2024/07/17 16:27:21-07:00 openjd_env: DAEMON_PID=2223
 2024/07/17 16:27:21-07:00 openjd_env: DAEMON_BASH_HELPER_SCRIPT=/sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/daemon-helper-functions.sh
```

The following lines from the job template specified this action.

```
   stepEnvironments:
   - name: DaemonProcess
     description: Runs a daemon process for the step's tasks to share.
     script:
       actions:
         onEnter:
           command: bash
           args:
           - "{{Env.File.Enter}}"
         onExit:
           command: bash
           args:
           - "{{Env.File.Exit}}"
       embeddedFiles:
       - name: Enter
         filename: enter-daemon-process-env.sh
         type: TEXT
         data: |
           #!/bin/env bash
           set -euo pipefail

           DAEMON_LOG='{{Session.WorkingDirectory}}/daemon.log'
           echo "openjd_env: DAEMON_LOG=$DAEMON_LOG"
           nohup python {{Env.File.DaemonScript}} > $DAEMON_LOG 2>&1 &
           echo "openjd_env: DAEMON_PID=$!"
           echo "openjd_env: DAEMON_BASH_HELPER_SCRIPT={{Env.File.DaemonHelperFunctions}}"

           echo 0 > 'daemon_log_cursor.txt'
     ...
```

3. Select one of the Task run: N session action in Deadline Cloud monitor. You will see log
   output as follows.

```
2024/07/17 16:27:22-07:00
 2024/07/17 16:27:22-07:00 ==============================================
 2024/07/17 16:27:22-07:00 --------- Running Task
 2024/07/17 16:27:22-07:00 ==============================================
 2024/07/17 16:27:22-07:00 Parameter values:
 2024/07/17 16:27:22-07:00 Frame(INT) = 2
 2024/07/17 16:27:22-07:00 ----------------------------------------------
 2024/07/17 16:27:22-07:00 Phase: Setup
 2024/07/17 16:27:22-07:00 ----------------------------------------------
 2024/07/17 16:27:22-07:00 Writing embedded files for Task to disk.
 2024/07/17 16:27:22-07:00 Mapping: Task.File.Run -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/run-task.sh
 2024/07/17 16:27:22-07:00 Wrote: Run -> /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/embedded_fileswy00x5ra/run-task.sh
 2024/07/17 16:27:22-07:00 ----------------------------------------------
 2024/07/17 16:27:22-07:00 Phase: Running action
 2024/07/17 16:27:22-07:00 ----------------------------------------------
 2024/07/17 16:27:22-07:00 Running command sudo -u job-user -i setsid -w /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/tmpv4obfkhn.sh
 2024/07/17 16:27:22-07:00 Command started as pid: 2301
 2024/07/17 16:27:22-07:00 Output:
 2024/07/17 16:27:23-07:00 Daemon PID is 2223
 2024/07/17 16:27:23-07:00 Daemon log file is /sessions/session-972e21d98dde45e59c7153bd9258a64dohwg4yg1/daemon.log
 2024/07/17 16:27:23-07:00
 2024/07/17 16:27:23-07:00 === Previous output from daemon
 2024/07/17 16:27:23-07:00 ===
 2024/07/17 16:27:23-07:00
 2024/07/17 16:27:23-07:00 Sending command to daemon
 2024/07/17 16:27:23-07:00 Received task result:
 2024/07/17 16:27:23-07:00 {
 2024/07/17 16:27:23-07:00   "result": "SUCCESS",
 2024/07/17 16:27:23-07:00   "processedTaskCount": 1,
 2024/07/17 16:27:23-07:00   "randomValue": 0.2578537967668988,
 2024/07/17 16:27:23-07:00   "failureRate": 0.1
 2024/07/17 16:27:23-07:00 }
 2024/07/17 16:27:23-07:00
 2024/07/17 16:27:23-07:00 === Daemon log from running the task
 2024/07/17 16:27:23-07:00 Loading the task details file
 2024/07/17 16:27:23-07:00 Received task details:
 2024/07/17 16:27:23-07:00 {
 2024/07/17 16:27:23-07:00  "pid": 2329,
 2024/07/17 16:27:23-07:00  "frame": 2
 2024/07/17 16:27:23-07:00 }
 2024/07/17 16:27:23-07:00 Processing frame number 2
 2024/07/17 16:27:23-07:00 Writing result
 2024/07/17 16:27:23-07:00 Waiting until a USR1 signal is sent...
 2024/07/17 16:27:23-07:00 ===
 2024/07/17 16:27:23-07:00
 2024/07/17 16:27:23-07:00 ----------------------------------------------
 2024/07/17 16:27:23-07:00 Uploading output files to Job Attachments
 2024/07/17 16:27:23-07:00 ----------------------------------------------
```

The following lines from the job template are what specified this action. ```
steps:

```
 steps:
 - name: EnvWithDaemonProcess
   parameterSpace:
     taskParameterDefinitions:
     - name: Frame
       type: INT
       range: "{{Param.Frames}}"

   stepEnvironments:
     ...

   script:
     actions:
       onRun:
         timeout: 60
         command: bash
         args:
         - '{{Task.File.Run}}'
     embeddedFiles:
     - name: Run
       filename: run-task.sh
       type: TEXT
       data: |
         # This bash script sends a task to the background daemon process,
         # then waits for it to respond with the output result.

         set -euo pipefail

         source "$DAEMON_BASH_HELPER_SCRIPT"

         echo "Daemon PID is $DAEMON_PID"
         echo "Daemon log file is $DAEMON_LOG"

         print_daemon_log "Previous output from daemon"

         send_task_to_daemon "{\"pid\": $$, \"frame\": {{Task.Param.Frame}} }"
         wait_for_daemon_task_result

         echo Received task result:
         echo "$TASK_RESULT" | jq .

         print_daemon_log "Daemon log from running the task"

   hostRequirements:
     attributes:
     - name: attr.worker.os.family
       anyOf:
       - linux
```
