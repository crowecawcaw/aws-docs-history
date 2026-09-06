

# Automatic downloads
<a name="auto-downloads"></a>

The Deadline CLI provides a command to download the output of all tasks in a queue that completed since the last time the same command ran. You can configure this as a cron job or scheduled task to run repeatedly. This configuration sets up automatic downloading of output on a continuous basis.

Before setting up automatic downloads, follow the steps in [Storage profiles for job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-profile.html) to configure all paths of asset data for upload and download. If a job uses an output path that is not in its storage profile, then the automatic download skips downloading that output and prints warning messages to summarize the files it did not download. Similarly, if a job is submitted without a storage profile, the automatic download skips that job and prints a warning message. By default, Deadline Cloud submitters display warning messages for paths that are outside of storage profiles to help ensure correct configuration.

## Configuring AWS credentials
<a name="credentials"></a>

Automatic downloads use the Deadline CLI to continuously download job outputs. To authenticate these downloads, you need long-term IAM credentials. Deadline Cloud monitor credentials expire, so you can't use them for this purpose. 

 Follow the steps below to set up long-term credentials. 

**Important**  
Heed the following warnings:  
**Do NOT** use your account's root credentials to access AWS resources. These credentials provide unrestricted account access and are difficult to revoke.
**Do NOT** put literal access keys or credential information in your application files. If you do, you create a risk of accidentally exposing your credentials if, for example, you upload the project to a public repository.
**Do NOT** include files that contain credentials in your project area.
Secure your access keys. Do not provide your access keys to unauthorized parties, even to help [find your account identifiers](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html). By doing this, you might give someone permanent access to your account.
Be aware that any credentials stored in the shared AWS credentials file are stored in plain text.
For more details, see [Best practices for managing AWS access keys in the *AWS General Reference*.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys)

**Create an IAM user**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane, select **Users** and then select **Create user**.

1. Name the user **deadline-output-downloader**. Clear the checkbox for **Provide user access to the AWS Management Console**, then choose **Next**.

1. Choose **Attach policies directly**.

1. Choose **Create policy** to create a custom policy with minimum required permissions.

1. In the JSON editor, specify the following permissions:

------
#### [ JSON ]

****  

   ```
   {
                      "Version":"2012-10-17",		 	 	 
                      "Statement": [
                          {
                              "Sid": "DeadlineCloudOutputDownload",
                              "Effect": "Allow",
                              "Action": [
                                  "deadline:AssumeQueueRoleForUser",
                                  "deadline:ListQueueEnvironments",
                                  "deadline:ListSessions",
                                  "deadline:ListSessionActions",
                                  "deadline:SearchJobs",
                                  "deadline:GetJob",
                                  "deadline:GetQueue",
                                  "deadline:GetStorageProfileForQueue"
                              ],
                              "Resource": "*"
                          }
                        ]
                     }
   ```

------

1. Name the policy **DeadlineCloudOutputDownloadPolicy** and choose **Create policy**.

1. Return to the user creation page, refresh the policy list, and select the **DeadlineCloudOutputDownloadPolicy** you just created, then choose **Next**.

1. Review the user details and then choose **Create user**.

**Create an access key**

1. From the user details page, select the **Security credentials** tab. In the **Access keys** section, choose **Create access key**. 

1. Indicate that you want to use the key for Other, then choose **Next**, then choose **Create access key**.

1. On the **Retrieve access keys** page, choose **Show** to reveal the value of your user's secret access key. You can copy the credentials or download a .csv file.

**Store the user access keys**
+ Store the user access keys in the AWS credentials file on your system:
  + On Linux, the file is located at `~/.aws/credentials`
  + On Windows, the file is located at `%USERPROFILE%\.aws\credentials`

  Replace the following keys:

  ```
  [deadline-downloader]
  aws_access_key_id={{ACCESS_KEY_ID}}
  aws_secret_access_key={{SECRET_ACCESS_KEY}}
  region={{YOUR_AWS_REGION}}
  ```

**Important**  
When you no longer need this IAM user, we recommend that you remove it to align with the [AWS security best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials). We recommend that you require your human users to use temporary credentials through [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/getting-started.html) when accessing AWS.

## Prerequisites
<a name="auto-downloads-prerequisites"></a>

Complete the following steps before creating a cron job or scheduled task for automatic download.

1. If you haven't already, install [Python](https://www.python.org/) from the Python website.

1. Install the Deadline CLI by running:

   ```
   python -m pip install deadline
   ```

1. Confirm the version of the Deadline CLI is 0.52.1 or newer with the following command.

   ```
   $ deadline --version
   deadline, version 0.52.1
   ```

   To see download status in the Deadline Cloud monitor, use version 0.60.4 or newer. That version started recording the download status that the monitor reads. For more information, see [View output download status in Deadline Cloud](auto-downloads-status.md).

## Test the output download command
<a name="test-output-command"></a>

**To verify the command works in your environment**

1. Get the path to Deadline

------
#### [ Linux and macOS ]

   ```
   $ which deadline
   ```

------
#### [ Windows ]

   ```
   C:\> where deadline
   ```

------
#### [ PowerShell ]

   ```
   PS C:\> Get-Command deadline
   ```

------

1. Run the sync-output command to bootstrap.

   ```
     /path/to/deadline queue sync-output \
     --profile deadline-downloader \
     --farm-id YOUR_FARM_ID \
     --queue-id YOUR_QUEUE_ID \
     --storage-profile-id YOUR_PROFILE_ID \
     --checkpoint-dir /path/to/checkpoint/directory \
   ```

1. You only need to do this step if your downloading machine is the same as submitting machine. Replace `--storage-profile-id YOUR_PROFILE_ID \` above with `--ignore-storage-profiles`. 

1. Submit a test job.

   1. Download the .zip file from GitHub.

      1. Open the [deadline-cloud-samples repository](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline) on the GitHub website.

      1. Choose **Code** and then, from the dropdown menu, select **Download ZIP**.

      1. Unzip the downloaded archive to a local directory.

   1. Run

      ```
       cd /path/to/unzipped/deadline-cloud-samples-mainline/job_bundles/job_attachments_devguide_output
      ```

   1. Run

      ```
      deadline bundle submit .
      ```

      1. If you don't have the default deadline config setup, you might need to supply the following in the command line.

        ```
        --farm-id {{YOUR-FARM-ID}} --queue-id {{YOUR-QUEUE-ID}}
        ```

   1. Wait for the job to complete before going to the next step. 

1. Run the sync-output command again.

   ```
    /path/to/deadline queue sync-output \
     --profile deadline-downloader \
     --farm-id YOUR_FARM_ID \
     --queue-id YOUR_QUEUE_ID \
     --storage-profile-id YOUR_PROFILE_ID \
     --checkpoint-dir /path/to/checkpoint/directory
   ```

1. Verify the following:
   + Your test job's outputs appear in the destination directory.
   + A checkpoint file is created in your specified checkpoint directory.

## Set up scheduled downloads
<a name="set-up-scheduled-downloads"></a>

Select the tab for your operating system to learn how to configure automatic downloads for every 5 minutes.

------
#### [ Linux ]

1. **Verify Deadline CLI Installation**

   Get the exact path to your deadline executable:

   ```
   $ which deadline
   ```

   Note this path (e.g., `/opt/homebrew/bin/deadline`) for use in the plist file.

1. **Create Checkpoint Directory**

   Create the directory where checkpoint files will be stored. Ensure proper permissions for your user to run the command.

   ```
   $ mkdir -p /path/to/checkpoint/directory
   ```

1. **Create Log Directory**

   Create a directory for cron job logs:

   ```
   $ mkdir -p /path/to/logs
   ```

   Consider setting up log rotate on the log file using https://www.redhat.com/en/blog/setting-logrotate

1. **Check Current Crontab**

   View your current crontab to see existing jobs:

   ```
   $ crontab -l
   ```

1. **Edit Crontab**

   Open your crontab file for editing:

   ```
   $ crontab -e
   ```

   The first time you run the command, you might be prompted to choose an editor (nano, vim, and so on).

1. **Add Cron Job Entry**

   Add the following line to run the job every 5 minutes (replace paths with actual values from steps 1 and 2):

   ```
   */5 * * * * /path/to/deadline queue sync-output --profile deadline-downloader --farm-id YOUR_FARM_ID --queue-id YOUR_QUEUE_ID --storage-profile-id YOUR_PROFILE_ID --checkpoint-dir /path/to/checkpoint/directory >> /path/to/logs/deadline_sync.log 2>&1
   ```

1. **Verify Cron Job Installation**

   After saving and exiting the editor, verify the cron job was added:

   ```
   $ crontab -l
   ```

   You should see your new job listed.

1. **Check Cron Service Status**

   Ensure the cron service is running:

   ```
   # For systemd systems (most modern Linux distributions)
   $ sudo systemctl status cron
   # or
   $ sudo systemctl status crond
   
   # For older systems
   $ sudo service cron status
   ```

   If not running, start it:

   ```
   $ sudo systemctl start cron
   $ sudo systemctl enable cron  # Enable auto-start on boot
   ```

------
#### [ macOS ]

1. **Verify Deadline CLI Installation**

   Get the exact path to your deadline executable:

   ```
   $ which deadline
   ```

   Note this path (e.g., `/opt/homebrew/bin/deadline`) for use in the plist file.

1. **Create Checkpoint Directory and Log Directory**

   Create the directory where checkpoint files will be stored:

   ```
   $ mkdir -p /path/to/checkpoint/directory
   $ mkdir -p /path/to/logs
   ```

   Consider setting up log rotate on the log file using https://formulae.brew.sh/formula/logrotate

1. **Create a Plist file**

   Create a configuration file at `~/Library/LaunchAgents/com.user.deadlinesync.plist` with the following content (replace `/path/to/deadline` with the actual path from step 1):

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.deadlinesync</string>
       <key>ProgramArguments</key>
       <array>
           <string>/path/to/deadline</string>
           <string>queue</string>
           <string>sync-output</string>
           <string>--profile</string>
           <string>deadline-downloader</string>
           <string>--farm-id</string>
           <string>YOUR_FARM_ID</string>
           <string>--queue-id</string>
           <string>YOUR_QUEUE_ID</string>
           <string>--storage-profile-id</string>
           <string>YOUR STORAGE PROFILE ID</string>
           <string>--checkpoint-dir</string>
           <string>/path/to/checkpoint/dir</string>
       </array>
       <key>RunAtLoad</key>
       <true/>
       <key>UserName</key>
       <string>YOUR_USER_NAME</string>
       <key>StandardOutPath</key>
       <string>/path/to/logs/deadline_sync.log</string>
       <key>StartInterval</key>
       <integer>300</integer>
   </dict>
   </plist>
   ```

   Replace `--storage-profile-id {{YOUR_PROFILE_ID}}` above with `--ignore-storage-profiles` if your downloading machine is the same as submitting machine.

1. **Validate Plist File**

   Validate the XML syntax of your plist file:

   ```
   $ plutil -lint ~/Library/LaunchAgents/com.user.deadlinesync.plist
   ```

   The command returns "OK" if the file is valid.

1. **Check for Existing Launch Agents or Launch Daemons**

   Check if a launch agent is already loaded:

   ```
   $ launchctl list | grep deadlinesync
   OR
   $ sudo launchctl list | grep deadlinesync
   ```

   If one exists, unload it first:

   ```
   $ launchctl bootout gui/$(id -u)/com.user.deadlinesync
   OR
   $ sudo launchctl bootout system/com.user.deadlinesync
   ```

1. **Create and bootstrap**

   To run this task while the user is logged in, run it as **LaunchAgent**. To run this task without a user being logged in every time the machine is running, run it as a **LaunchDaemon**.

   1. To run as **LaunchAgent:**

      1. Use the configuration created under `~/Library/LaunchAgents/com.user.deadlinesync.plist`

      1. Then load the configuration using the bootstrap command:

         ```
         $ launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.user.deadlinesync.plist
         ```

   1. To run as **LaunchDaemon**:

      1. Move the Pilst file and change permissions by running the following:

         ```
         $ sudo mv ~/Library/LaunchAgents/com.user.deadlinesync.plist /Library/LaunchDaemons/ 
         $ sudo chown root:wheel /Library/LaunchDaemons/com.user.deadlinesync.plist 
         $ sudo chmod 644 /Library/LaunchDaemons/com.user.deadlinesync.plist
         ```

      1. Load the launch agent using the modern bootstrap command:

         ```
         $ sudo launchctl bootstrap system /Library/LaunchDaemons/com.user.deadlinesync.plist
         ```

1. **Verify Status**

   If you bootstrapped a LaunchAgent run the following to confirm it's loaded:

   ```
   $ launchctl list | grep deadlinesync
   ```

   If you bootstrapped a LaunchDaemon, confirm it is loaded by running:

   ```
   $ sudo launchctl list | grep deadlinesync
   ```

   The output should look like

   ```
   SOME_PID_NUMBER 0 com.user.deadlinesync
   ```

   For detailed status information:

   ```
   $ launchctl print gui/$(id -u)/com.user.deadlinesync
   ```

   This shows the current state, program arguments, environment variables, run interval, and execution history.

------
#### [ Windows ]

**Note**  
The scheduled task created using these instructions only work when the user is logged in.  
To set it up at system startup without requiring user login, see the official [Windows documentation](https://learn.microsoft.com/en-us/windows/win32/taskschd/using-the-task-scheduler) on the Microsoft website.

For all steps below use Command Prompt - run as Administrator:

1. **Verify Deadline CLI Installation**

   Find the deadline executable:

   ```
   C:\> where deadline
   ```

   Note the full path (e.g., `C:\Program Files\Amazon\DeadlineCloud\deadline.exe`) for use in the task.

1. **Create Checkpoint Directory**

   Create the directory where checkpoint files will be stored:

   ```
   C:\> mkdir "path\to\checkpoint\directory"
   ```

1. **Create Log Directory**

   Create a directory for task logs:

   ```
   C:\> mkdir "path\to\logs"
   ```

1. **Create Batch File Wrapper**

   Create the batch file with the following content:

   ```
   C:\> notepad C:\path\to\deadline_sync.bat
   ```

   ```
   YOUR_PATH_TO_DEADLINE.EXE queue sync-output --profile deadline-downloader --farm-id {{YOUR_FARM_ID}} --queue-id {{YOUR_QUEUE_ID}} --storage-profile-id {{YOUR_PROFILE_ID}} --checkpoint-dir path\to\checkpoint\checkpoints > path\to\logs\deadline.log 2>&1
   ```

1. **Test Batch File**

   Test the batch file manually:

   ```
   C:\> .\path\to\deadline_sync.bat
   ```

   Check the log file was created:

   ```
   C:\> notepad path\to\logs\deadline_sync.log
   ```

1. **Check Task Scheduler Service**

   Ensure Task Scheduler service is running:

   ```
   C:\> sc query "Schedule"
   ```

   If the service doesn't exist, try alternative names:

   ```
   C:\> sc query "TaskScheduler"
   C:\> sc query "Task Scheduler"
   ```

   If not running, start it:

   ```
   C:\> sc start "Schedule"
   ```

1. **Create Scheduled Task**

   Create the task to run every 5 minutes.

   ```
   C:\> schtasks /create /tn "DeadlineOutputSync" /tr "C:\path\to\deadline_sync.bat" /sc minute /mo 5
   ```

   Command breakdown:
   + `/tn` - Task name
   + `/tr` - Task to run (your batch file)
   + `/sc minute /mo 5` - Schedule: every 5 minutes

1. **Verify Task Creation**

   Check that the task was created successfully:

   ```
   schtasks /query /tn "DeadlineOutputSync" /v /fo LIST
   ```

   Look for:
   + **Task To Run**: Should show your batch file path
   + **Next Run Time**: Should show a time within 5 minutes

1. **Test Task Execution**

   Run the task manually to test:

   ```
   schtasks /run /tn "DeadlineOutputSync"
   ```

   Check task status:

   ```
   schtasks /query /tn "DeadlineOutputSync"
   ```

------

**Verify the setup**

To verify the automatic downloads setup was successful, complete the following steps.

1. Submit a new test job.

1. Wait for one scheduler interval to complete, which in this case is 5 minutes.

1. Verify that new outputs are downloaded automatically.

If the outputs do not download, check the Troubleshooting section for the process logs.

## Troubleshooting automatic downloads
<a name="auto-downloads-troubleshooting"></a>

If you encounter issues with the automatic downloads, check the following:

### Download error codes
<a name="download-error-codes"></a>

When a download fails, the **Download status** column in the Deadline Cloud monitor names the reason, and the `deadline queue sync-output` command records one of the following error codes. Most of these errors are resolved on the machine that runs the download command, which is often a different machine from the one you view the monitor on.

`PERMISSION_DENIED` (Permission denied)  
The downloader isn't allowed to write to the output location, or its AWS credentials were denied access. Grant the user that runs the download command write access to the output location, confirm the command's AWS profile has access to the queue, and run the command again.

`DISK_FULL` (Disk full)  
The machine running the download ran out of disk space. Free up space on the drive that holds the output location, then run the command again.

`PATH_NOT_FOUND` (Path not found)  
The output destination doesn't exist or isn't mounted on the machine running the download. Create the directory or mount the shared drive, then run the command again.

`NETWORK_ERROR` (Network error)  
A network interruption stopped the transfer. Network errors are usually transient. Run the command again, and check the machine's connectivity if the error repeats.

`UNKNOWN` (Failed)  
The downloader couldn't identify a specific cause. The monitor shows **Failed** for this code and for any code it doesn't recognize. Check the log output of the `deadline queue sync-output` command for the underlying error.

A job whose download fails is retried automatically on each later run. After five failed attempts, the downloader stops retrying the job and prints a warning. After you fix the cause, recover the job by running the download command with a lookback window that covers when the job finished:

```
deadline queue sync-output --farm-id {{FARM_ID}} --queue-id {{QUEUE_ID}} \
    --storage-profile-id {{STORAGE_PROFILE_ID}} \
    --force-bootstrap --bootstrap-lookback-minutes {{1440}}
```

Pass both flags together. The `--bootstrap-lookback-minutes` option defaults to 0, so `--force-bootstrap` on its own recovers nothing.

### Why was my job skipped?
<a name="download-skip-reasons"></a>

When the downloader skips a job, the **Download status** column names the reason directly in the cell:

**No attachments** (`no_attachments`)  
The job wasn't submitted with job attachments, so it has no recorded output files to download. Some jobs never produce downloadable output, so a skipped job with no attachments usually needs no action.

**Missing storage profile** (`missing_storage_profile`)  
The job was submitted without a storage profile while the download command uses one, so the downloader doesn't know where the job's files belong on each machine. Nothing downloads for the job until a storage profile is configured for it. A job's storage profile is set when the job is submitted, so submit the job with a storage profile and pass the same profile to the download command. In the tasks table, the **Missing storage profile** status is a link that opens an explanation, a documentation link, and a **Troubleshoot with AI** button. For more information, see [Storage profiles for job attachments](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-profile.html).

A skipped job with no reason shown was canceled or stopped before producing output. It needs no action.

### Is it a download problem or a render problem?
<a name="download-failure-vs-render-failure"></a>

A problem in a task's **Download status** column can mean two different things, and they have different fixes. The status text tells you which one you have:
+ **No outputs** on a task whose run status is `FAILED` means the task failed to render on the farm. No file was ever produced, so there was nothing to download. Your drive and your network are fine. Check the task's logs to find the render error, fix it, and requeue the task. A task can also show **No outputs** after finishing successfully without writing any files, which is normal and needs no action.
+ An error name, such as **Permission denied**, means the task rendered and its output exists, and copying the files to your file system failed. Resolve the error using [Download error codes](#download-error-codes).

In the jobs table, both problems appear as a red segment in the job's download progress bar. Open the job's tasks table to tell them apart. A job where every task failed shows a dash instead of a download error, because the job never produced output. The job's own status column reports that failure. Diagnosing the download in these render-failure cases wastes time, so always check the task's run status first.

### Troubleshoot with AI
<a name="download-troubleshoot-with-ai"></a>

The download failure messages in the Deadline Cloud monitor, including the red **Output sync failed** indicator, include a **Troubleshoot with AI** button. The button opens the Deadline Cloud assistant, which reads the download status record for your queue and walks you through your specific failure, including the commands to run to fix it.

Reach for it when a download keeps failing after you tried the fix for its error code, when you see an error you don't recognize, or when you aren't sure which machine the problem is on. The button appears when the Deadline Cloud assistant is enabled for your monitor. For more information, see [Deadline Cloud assistant](deadline-cloud-assistant.md).

### Storage profile issues
<a name="storage-profile-issues"></a>
+ An error like `[Errno 2] No such file or directory` or `[Errno 13] Permission denied` in the log file could be related to missing or misconfigured storage profiles.
+ See [ Storage profiles](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/storage-profile-job-attachments.html) for information about how to set up your storage profiles when the downloading machine is different from the submitting machine.
+ For same-machine downloads, try the `--ignore-storage-profiles` flag.

### Directory permissions
<a name="directory-permissions"></a>
+ Ensure the scheduler service user has:
  + Read/write access to the checkpoint directory
  + Write access to the output destination directory
+ For Linux and macOS, use `ls -la` to check permissions.
+ For Windows, review Security settings in the Properties folder.

### Checking scheduler logs
<a name="checking-scheduler-logs"></a>

------
#### [ Linux ]

1. Check if cron service is running:

   ```
   # For systemd systems
   $ sudo systemctl status cron
   # or
   $ sudo systemctl status crond
   
   # Check if your user has cron job correctly configured
   $ crontab -l
   ```

1. View cron execution logs:

   ```
   # Check system logs for cron activity (most common locations)
   $ sudo tail -f /var/log/syslog | grep CRON
   $ sudo tail -f /var/log/cron.log | grep deadline
   
   # View recent cron logs
   $ sudo journalctl -u cron -f
   $ sudo journalctl -u crond -f  # On some systems
   ```

1. Check your specific cron job logs:

   ```
   # View the log file specified in your cron job
   $ tail -100f /path/to/logs/deadline_sync.log
   ```

1. Search for cron job execution in system logs:

   ```
   # Look for your specific cron job executions
   $ sudo grep "deadline.*sync-output" /var/log/syslog
   
   # Check for cron job starts and completions
   $ sudo grep "$(whoami).*CMD.*deadline" /var/log/syslog
   ```

1. Check checkpoint file updates:

   ```
   # List checkpoint files with timestamps
   $ ls -la /path/to/checkpoint/directory/
   
   # Check when checkpoint was last modified
   $ stat /path/to/checkpoint/directory/queue-*_download_checkpoint.json
   ```

1. Check the log file:

   ```
   $ ls -la /path/to/log/deadline_sync.log
   ```

------
#### [ macOS ]

Viewing Launch Agent Execution Logs:

1. Check if the launch agent is running:

   ```
   $ sudo launchctl list | grep deadlinesync
   ```

   Output shows: `PID Status Label` (PID will be `-` when not currently running, which is normal for interval jobs)

1. View detailed launch agent status:

   ```
   $ sudo launchctl print system/com.user.deadlinesync
   ```

   This shows execution history, last exit code, number of runs, and current state.

1. View launch agent execution logs:

   ```
   # View recent logs (last hour)
   log show --predicate 'subsystem contains "com.user.deadlinesync"' --last 1h
   
   # View logs from a specific time period
   log show --predicate 'subsystem contains "com.user.deadlinesync"' --start '2024-08-27 09:00:00'
   ```

1. Force run the launch agent for immediate testing:

   ```
   $ sudo launchctl kickstart gui/$(id -u)/com.user.deadlinesync
   ```

   This immediately triggers the job regardless of the schedule, useful for testing.

1. Check checkpoint file updates:

   ```
   # List checkpoint files with timestamps
   $ ls -la /path/to/checkpoint/directory/
   ```

1. Check the log file:

   ```
   $ ls -la /path/to/log/deadline_sync.log
   ```

------
#### [ Windows ]

1. Check if Task Scheduler service is running:

   ```
   C:\> sc query "Schedule"
   ```

   If the service doesn't exist, try alternative names:

   ```
   C:\> sc query "TaskScheduler"
   C:\> sc query "Task Scheduler"
   ```

1. View your scheduled tasks:

   ```
   C:> schtasks /query /tn "DeadlineOutputSync"
   ```

1. Check your task's log file:

   ```
   # View the log file created by your batch script
   C:> notepad C:\path\to\logs\deadline_sync.log
   ```

1. Check checkpoint file updates:

   ```
   # List checkpoint files with timestamps
   C:> dir "C:\path\to\checkpoint\directory" /od
   ```

------