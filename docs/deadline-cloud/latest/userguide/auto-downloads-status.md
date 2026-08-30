# View output download status in Deadline Cloud

The **Download status** column in the AWS Deadline Cloud monitor shows, for each job and
each task, whether automatic downloads copied the output files to the download location. A job's
render status and its download status answer different questions. A status of
`SUCCEEDED` means the tasks rendered. The **Download status** column
tells you whether the resulting files are on your file system yet.

The column reports one specific transfer: the automatic downloads that the
`deadline queue sync-output` command performs for a queue. A studio administrator
usually schedules that command once for the whole queue, so finished output lands on the shared
storage everyone works from without anyone downloading files by hand. Deadline Cloud moves output files
in two other ways, and the column doesn't report either of them.

Ways output files move, and where each one is reported| Transfer | What it moves | Who sets it up | Where you see it |
| --- | --- | --- | --- |
| Automatic downloads | Output from every job that finished in a queue, to the shared download<br>location. | A studio administrator, once per queue. | The *_Download status_<br>• column, described on this page. |
| Download finished output | Output from one job you pick, to the computer you're sitting at, when you ask for<br>it. | Nobody. The action is in the monitor. | The download progress in the monitor. See [Download finished output in Deadline Cloud](download-finished-output.md "download-finished-output.md"). |
| Job attachment transfer during a session | Input files onto the worker before a task runs, and output files back to Amazon S3 when it<br>finishes. | Nobody. The transfer is part of any job that uses job attachments. | The session actions in the job's logs. See [View session and worker logs in Deadline Cloud](view-logs.md "view-logs.md"). |

Because the two other transfers are reported elsewhere, a job can show
**Downloaded** in the column while a task's output is still uploading to Amazon S3 in
a session, or show a dash after you already downloaded the output to your own computer.

If you watch jobs in the monitor, you don't set up anything to see the column. You need the
Deadline Cloud monitor desktop application and access to the location where the download command records the
status, which is the shared storage that holds your outputs. If you administer the queue,
scheduling the download command is what makes the column work for everyone who watches the
queue. For more information, see [Set up scheduled downloads](auto-downloads.md#set-up-scheduled-downloads "auto-downloads.md#set-up-scheduled-downloads").

## Availability and prerequisites

The **Download status** column is available in the Deadline Cloud monitor desktop
application version 1.2.0 or later. It doesn't appear in the web
version of the monitor. There is no setting to turn the feature on. The column shows data
when the following are in place:

- Automatic downloads are running for the queue with the
  `deadline queue sync-output` command, using version 0.60.4 or later of the
  Deadline CLI. That version started recording the download status that the monitor reads. For more
  information, see
  [Set up scheduled downloads](auto-downloads.md#set-up-scheduled-downloads "auto-downloads.md#set-up-scheduled-downloads") and
  [Configuring AWS credentials](auto-downloads.md#credentials "auto-downloads.md#credentials").
- Jobs in the queue use job attachments to record their output files. For more
  information, see [Job attachments in Deadline Cloud](storage-job-attachments.md "storage-job-attachments.md").
- The download command knows where output files belong on the machine that runs it. Most
  studios run the command on one machine that writes to shared storage, which needs a storage
  profile to map the paths from the submitting machine to the downloading one. If you run the
  command on the machine you submit jobs from, the submitted paths are already correct there,
  so you can pass `--ignore-storage-profiles` instead of configuring a profile.
  Download status is recorded either way. For more information, see [Storage
  profiles for job attachments](storage-profile.md "storage-profile.md").
- The machine running the monitor can reach the location where the download command
  recorded the status. With a storage profile, the `deadline queue sync-output`
  command writes the status file into the profile's file system location, in a
  `.deadline` subfolder on the same shared storage that holds the downloaded
  output. That location must be mounted on the monitor's machine, and the column shows
  **Unavailable from this machine** when it isn't. With
  `--ignore-storage-profiles`, the command records the status on its own machine,
  where the monitor reads it without a shared mount.

The column fills in after the `deadline queue sync-output` command completes
its first run for the queue. Until then, jobs show a dash.

The column is shown by default on both the jobs table and the tasks table. To hide or show
it, open the table preferences and select **Download status** under
**Column preferences**. Each table remembers the setting separately.

## Download status for a job

Each job in the jobs table shows one of the following download statuses:

**Downloaded**

Every available output for the job is in the download location.

**In progress**

A progress bar, such as 3/4, showing that outputs for some tasks are downloaded and
more are still to come. The remaining outputs arrive on a later download run. A job whose
tasks are done can also show a bar when some of its tasks had problems: a red segment marks
tasks that failed to render, or whose download failed. Open the job's tasks table to see
which.

An error name, such as **Permission denied**

The download failed. The tasks rendered, but copying the files to the download
location didn't complete. The cell names the reason: **Permission
denied**, **Disk full**, **Path not found**, or
**Network error**. A failure the monitor can't classify shows
**Failed**. For the full list of reasons and how to resolve them, see
[Download error codes](auto-downloads.md#download-error-codes "auto-downloads.md#download-error-codes").

**No attachments** or **Missing storage profile**

The downloader skipped the job, and the cell names the reason. A job without job
attachments has no output to download and needs no action. A job that is missing a storage
profile downloads nothing until the profile is configured, so that reason is actionable.
For more information, see
[Why was my job skipped?](auto-downloads.md#download-skip-reasons "auto-downloads.md#download-skip-reasons").

**-** (a dash)

There is no download information for the job yet. The most common cause is timing: the
job finished after the last download run, so the downloader hasn't seen it yet. The status
fills in on the next run. A job where no task succeeded also shows a dash, because it
produced no output to download. The job's own status column already reports that
failure.

**Unavailable from this machine**

A download status record exists, but the monitor can't read it from your computer.
Check that the shared drive that holds your outputs is mounted. For where the status
record lives and why the mount matters, see
[Availability and prerequisites](#auto-downloads-status-prerequisites "#auto-downloads-status-prerequisites").

## Download status for a task

Open a job to see the same column for each task in the tasks table. The per-task view
shows which outputs landed. Each task shows one of the following:

**Downloaded**

The task's output is in the download location.

An error name, such as **Permission denied**

The download of the task's files failed. Choose the status to see the error detail and
a **Troubleshoot with AI** button. For more information, see
[Download error codes](auto-downloads.md#download-error-codes "auto-downloads.md#download-error-codes").

**No outputs**

The task produced no file to download. The task either finished successfully without
writing any files, which is normal for setup or validation work, or it failed to render on
the farm. The task's own run status column tells you which. For more information, see
[Is it a download problem or a render problem?](auto-downloads.md#download-failure-vs-render-failure "auto-downloads.md#download-failure-vs-render-failure").

**No attachments** or **Missing storage profile**

The job was skipped, and the reason shows on each task as well.
**No attachments** means the job isn't set up to produce downloadable
output, so none of its tasks have anything to download, even tasks that rendered
successfully. Every task in the job shows the label, and it needs no action. In the tasks
table, **Missing storage profile** is a link that opens an explanation, a
link to the storage profile documentation, and a
**Troubleshoot with AI** button.

**-** (a dash)

The download run hasn't looked at the task yet, or nothing is recorded for it. The
task's output may still be coming down. Wait for the next run.

A task that was requeued while its earlier output is still on disk keeps showing
**Downloaded** with a blue info icon. Choose the icon to see the explanation:
the files in the download location are from the previous run, and a newer run is in flight.
The icon clears after the task finishes and the next download run completes.

## Outputs last synced indicator

Every value in the **Download status** column is a snapshot from the last
time the download command ran. The **Outputs last synced** indicator in the
page header tells you when that was, so you know how current the column is. Check the indicator
before acting on a download status.

Green, such as "Outputs last synced 5 minutes ago"

The last download run succeeded recently. The column is current.

Yellow, "Outputs may be stale"

No download run has completed in over 30 minutes, so the statuses in the column may be
out of date. Select the indicator for details. The usual cause is that the scheduled
download command stopped running on the machine that syncs the queue.

Red, "Output sync failed"

The last download run failed. Select the indicator to see the failures grouped by
reason, along with a **Troubleshoot with AI** button that helps you
diagnose the specific failure. For more information, see
[Troubleshoot with AI](auto-downloads.md#download-troubleshoot-with-ai "auto-downloads.md#download-troubleshoot-with-ai").

The column refreshes on its own about every 60 seconds. It also refreshes as soon as you
return focus to the monitor window, so clicking away and back pulls the latest download run
immediately. You don't need to restart the monitor to pick up a new run. Refreshing rereads
what the download command already recorded. If the indicator shows the outputs may be stale,
the download command isn't running, and refreshing won't change the column.
