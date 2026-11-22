

# Monitoring source action execution

Monitor execution jobs and view detailed results from the AWS Transform MGN console or through the API.

## Viewing execution jobs
<a name="source-actions-monitor-jobs"></a>

Source action execution jobs appear on the **Launch history** page of the account where the AWS Transform MGN connector is deployed (the MGN connector account), together with the other jobs in that account.

To view source action execution jobs:

1. Sign in to the MGN connector account and open the AWS Transform MGN console

1. Choose **Launch history** in the left navigation menu

1. Find the source action execution jobs in the list. You can sort by any column, or search by job type or another property

1. Choose the **Job ID** of a job to view its details

The job detail view shows:
+ **Job ID** — Unique identifier for the execution
+ **Action name** — The executed action
+ **Job status** — Overall status (In Progress, Completed, Completed with Errors)
+ **Started at** — Execution start timestamp
+ **Completed at** — Execution end timestamp (if complete)
+ **Invocation summary** — Count of passed, failed, and in-progress invocations

[Learn more about launch history](jobs.md).

## Viewing invocation results
<a name="source-actions-monitor-invocations"></a>

AWS Transform MGN doesn't store or show script output. The job details list each invocation's status, start time, and duration, with a link to the command in SSM Run Command. You view the script output and exit code in Run Command.

To view results for individual machine invocations:

1. Open a source action execution job from the **Launch history** page

1. View the **Invocations** table showing each targeted machine

1. Check the status for each invocation (Passed, Failed, In Progress, or Timeout)

1. To see the script output and exit code, choose the SSM command link to open the command in SSM Run Command

For each invocation, the job details show:
+ **Machine name** — On-premises machine that executed the action
+ **Status** — Invocation result (Passed, Failed, Timeout)
+ **Start time** — When the invocation started
+ **Duration** — Script execution time in seconds
+ **SSM command link** — Opens the command in SSM Run Command, where you can view the standard output, standard error, and exit code

**Note**  
The link to the SSM execution log is available only in the account where the AWS Transform MGN connector is deployed. In a member account that doesn't own the connector, open the log from the connector account.

## Viewing source actions on a source server
<a name="source-actions-monitor-server"></a>

The **Migration dashboard** tab of each source server includes a table that summarizes the source actions that ran on that server.

To view the source actions that ran on a source server:

1. Navigate to the **Source servers** page

1. Choose the source server name to open the server details view

1. Choose the **Migration dashboard** tab and review the source actions table

The table includes these columns:
+ **Name** — The name of the source action
+ **Description** — The description of the source action
+ **Start time** — When the execution started
+ **End time** — When the execution ended
+ **Execution status** — The status of the execution. See [Status indicators](#source-actions-status-indicators)
+ **MGN connector account** — The account where the AWS Transform MGN connector that ran the source action is deployed
+ **Debug link** — A link to the SSM execution log. The link appears only in the account where the AWS Transform MGN connector is deployed. In other accounts, this column shows `Link can be provided only from the account the MGN connector is implemented in`

## Status indicators
<a name="source-actions-status-indicators"></a>

Source action execution status is indicated throughout the console:

**Source action status (Settings page):**
+ **✔ Completed** (green) — All actions passed on this server
+ **◷ In progress** (gray) — Actions are currently running
+ **✕ Failed** (red) — One or more actions failed

**Invocation status (Job detail view):**
+ **Passed** (green) — Script executed successfully with exit code 0. On Windows, a script with only non-terminating PowerShell errors can also report exit code 0. For more information, see [Windows script requirements and behaviors](source-actions-intro.md#source-actions-windows-scripts)
+ **Failed** (red) — The script returned a non-zero exit code, or the script didn't run, for example because the connector couldn't connect to the machine. When the script didn't run, there is no exit code
+ **Timeout** (red) — Script did not complete within the specified timeout
+ **In Progress** (gray) — Script is currently executing

## Troubleshooting execution failures
<a name="source-actions-troubleshooting"></a>

If a source action execution fails, follow these steps:

1. Check the invocation status in the job details, and the exit code in SSM Run Command

1. Review the standard error output in SSM Run Command for error messages

1. Verify the script in SSM Parameter Store is correct and matches the target platform

1. Ensure the connector has network access to the machine: SSH on port 22 (Linux), or WinRM on port 5986 for HTTPS or 5985 for HTTP (Windows)

1. Check that the timeout is sufficient for the script duration

1. Verify that the connector role has the required IAM permissions and access to SSM. If the result includes a warning that AWS Transform MGN couldn't send logs or metrics, add the `mgn:SendClientLogsForMgn` and `mgn:SendClientMetricsForMgn` actions to the connector role, as described in [Prerequisites](source-actions-intro.md#source-actions-prerequisites). The source server doesn't need access to AWS

### Reviewing the execution in SSM
<a name="source-actions-troubleshooting-ssm"></a>

Each source action execution runs through the `RunSourceServerAction` SSM document. You can review the execution in the SSM console to confirm whether a source action succeeded and to investigate failures. The link to the SSM execution log is available only in the account where the AWS Transform MGN connector is deployed.

To review a source action execution in SSM:

1. In the account where the AWS Transform MGN connector is deployed, open the invocation details, or the **Migration dashboard** tab of the source server, and choose the link to the SSM execution log

1. Review the overall command status and the status for the target

1. Review the output and error output of each step to find where the execution stopped and why

Use the results to tell apart the main types of failures:
+ **Script errors** — The script ran but returned a non-zero exit code. Review the script's standard error, and see [Supported operating systems and script limitations](source-actions-intro.md#source-actions-supported) for common causes such as missing interpreters, line endings, or sudo configuration
+ **Connection errors** — The connector could not reach the machine over SSH (Linux) or WinRM (Windows), or authentication failed. The script didn't run, so the result has no exit code, and the error message shows the reason. If the address in **FQDN for Action Framework** isn't reachable, the error is:
  + Linux: `SSH connection to the source server failed: Unable to get the SSH connection to host due to "{{reason}}"`
  + Windows: `WinRM connection to the source server failed: Unable to get the WinRM connection to host due to "{{reason}}"`

  Verify the network connectivity and credentials described in [Prerequisites](source-actions-intro.md#source-actions-prerequisites)
+ **Timeouts** — The script did not finish within the source action timeout. Increase the timeout or shorten the script