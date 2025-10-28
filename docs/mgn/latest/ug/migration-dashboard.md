NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Monitor the server in the migration lifecycle

The **Migration dashboard** tab allows you to monitor the
server in relation to the migration lifecycle.

Here, you can see the lifecycle state the source server is currently on, a detailed view of
the data replication status, and any events that the source server has undergone (in AWS
CloudTrail). You can use the Migration dashboard to monitor the status of your source server and
to troubleshoot migration and data replication issues.

## Understand lifecycle states

The **Lifecycle** view shows the current state of each server
within the migration lifecycle.

Lifecycle states include:

- **Not ready** – The server is undergoing the Initial Sync
  process and is not yet ready for testing. Data replication can only commence once all of the
  Initial Sync steps have been completed.
- **Ready for testing** – The server has been successfully
  added to AWS Application Migration Service and data replication has started. Test or cutover instances can now be
  launched for this server.
- **Test in progress** – A test instance is currently being
  launched for this server.
- **Ready for cutover** – This server has been tested and is
  now ready for a cutover instance to be launched.
- **Cutover in progress** – A cutover instance is currently
  being launched for this server.
- **Cutover complete** – This server has been cutover. All of
  the data on this server has been migrated to the cutover instance.

The lifecycle always displays the **Launch status**,
**Last test**, and **Cutover
status** for each server that has undergone these stages.

###### Topics

- [Not ready](#not-ready "#not-ready")
- [Ready for testing](#ready-for-testing-1 "#ready-for-testing-1")
- [Test in progress](#test-in-progress "#test-in-progress")
- [Ready for cutover](#ready-for-cutover1 "#ready-for-cutover1")
- [Cutover in progress](#cutover-in-progress "#cutover-in-progress")
- [Cutover complete](#cutover-stage "#cutover-stage")

### Not ready

The **Not ready** lifecycle state represents several
possible scenarios:

###### Topics

- [Server undergoing initial sync](#initiation "#initiation")
- [Unable to complete initiation](#unable-to-initiate "#unable-to-initiate")

#### Server undergoing initial sync

A source server that has been added to AWS Application Migration Service automatically begins the initial sync
process after AWS Replication Agent installation.

Data replication can only commence after all of the initial sync steps have been
completed. The server is in the **Not ready** lifecycle
state until initial sync has been successfully completed.

Initial sync steps include:

- Initiation
  - Creating firewall rules
  - Creating replication server
  - Booting replication server
  - Resolving Service Manager address
  - Authenticating with the Service Manager
  - Downloading replication software
  - Creating staging disks
  - Pairing replication server with agent
  - Establishing communication between AWS Replication Agent and replication
    server

- Sync (0% to 100%)
- Flush backlog (if any)
- Create first launchable snapshot

You can review the overall progress of the Initial Sync process under the **Data replication status** view.

It provides the percentage of completion, the time left until initial sync is finished,
and whether there are any issues (such as a stall).

You can tell that a server has successfully completed the initial sync process through
several indicators on the main **Source servers** page as well
as on the **Migration dashboard** tab for an individual
server.

On the main **Source servers** page, a newly added server
that has completed initial sync for the first time shows **Ready for
testing** under the **Migration lifecycle** column and
**Healthy** under the **Data replication
status** column.

On the individual server view, under the **Migration
dashboard** tab, the **Lifecycle** section shows
the **Ready for testing** status. The **Data
replication status** section shows the **Healthy**
status.

###### Note

Servers automatically undergo initial sync every time there is a network
disconnect.

#### Unable to complete initiation

The server is in the **Not ready** Lifecycle state until
Initial Sync has been successfully completed.

If the Initial Sync process is stalled for any reason, the **Data
replication status** section indicates that replication has stalled.

Scroll down to the Replication initiation steps to see the step on which the error
occurred. The step on which initial sync failed is marked with a red "x".

You must fix the indicated issue before the initial sync process can continue. You are
not able to migrate your server and the server remains in the **Not ready** state until the issue is resolved.

Each step has troubleshooting methods.

### Ready for testing

Once the server has successfully completed the Initial Sync process, it enters the
**Ready for testing** lifecycle state.

The **Data replication status** box shows a **Healthy** state, indicating that the server is healthy.

You can now launch a test instance for this server. The server stays in the **Ready for testing** lifecycle state until you launch a Test
instance for the server.

### Test in progress

Once you have launched a Test instance for your server, the migration dashboard shows
the **Test in progress** lifecycle state.

Within the **Lifecycle** box, you can review the **Launch status** and **Last test**
information fields for the test instance.

- The **Launch status** field shows the time of the test
  instance launch. While the Testing instance is being launched, the **Launch status** field shows **Waiting**.
- Once the test instance has been launched, the Launch status shows **Launched**. Wait for the instance to boot and then choose **View in EC2 console** link to open the EC2 console in a new tab, in
  order to view and monitor your launched test instance.
- The AWS EC2 console opens in a new tab and automatically searches for and displays your
  test instance.
- The **Last test** field shows the date of the last
  test. To review the test launch details, click **Job ID**,
  which opens the job within the **Launch History** page in a
  new tab.
- On the main **Source servers** page, the **Migration lifecycle** column shows **Ready for
  testing** and the **Next step** column shows
  **Launch test instance**.
- The server stays in the **Test in progress** Lifecycle
  state until you finalize your testing and mark the server as **Ready for cutover**.

You can use these indicators to verify that your test instance was successfully
launched::

- On the **Server Details > Lifecycle** pane, the Launch
  status states **Launched**.
- On the main **Source servers** page, the **Alerts** column shows the **Launched** status.

### Ready for cutover

After you have finalized your testing, the Migration dashboard shows the **Ready for cutover** lifecycle state.

- The **Launch status** field shows the time of the last
  test instance launch. Click on the **View in EC2 console** link
  to open the EC2 console in a new tab in order to view and monitor your launched Test
  instance.
- The **Last test** field shows the date the last test
  was started. You can review the test launch details by clicking on the **Job ID**. This opens the relevant Job.
- The **Cutover** field shows the date of the last
  cutover instance launch, if applicable. You can review the cutover launch details by
  clicking on the **Job ID**. This opens the relevant Job.
- On the **Source servers** page, the **Migration lifecycle** column shows **Ready for
  cutover** and the **Next step** column shows
  **Terminate test instance; Launch cutover instance**.

The server stays in the **Ready for cutover** Lifecycle
state until you launch a cutover instance.

### Cutover in progress

Once you have launched a cutover instance for your server, the Migration dashboard shows the **Cutover in progress** Lifecycle state.

- The **Launch status** field shows the last time of
  cutover launch. Click on the **View in EC2 console** link to
  open the EC2 console in a new tab in order to view and monitor your launched cutover
  instance.
- The **Last test** field shows the date the last test
  was started. You can review the test launch details by clicking on the **Job ID**. This opens the Job.
- The **Cutover** field shows the date of the last
  cutover instance launch. You can review the cutover launch details by clicking on the
  **Job ID**. This opens the Job.
- On the **Source servers** page, the **Migration lifecycle** column shows **Cutover in
  progress** and the **Next step** column shows
  **Complete the cutover**.

The server stays in the **Cutover in progress** Lifecycle
state until you complete the cutover.

### Cutover complete

Once you have completed your cutover instance launch for your server, the Migration
dashboard shows the **Cutover complete** lifecycle state.
This is the final state in the migration lifecycle. This state indicates that you have
successfully migrated your source server to AWS.

- The **Launch status** field shows **Launched**. Click on the **View in EC2
  console** link to open the EC2 console in a new tab in order to view and monitor
  your launched cutover instance.
- The **Last test** field shows the date the last test
  was started. You can review the test launch details by clicking on the **Job ID**. This opens the Job.
- The **Cutover** field shows the date you finalized
  your Cutover instance launch. You can review the cutover launch details by clicking on the
  **Job ID**. This opens the Job.
- The AWS Application Migration Service console automatically stops data replication for the source servers that
  were cutover in order to save resource costs.
- On the **Source servers** page, the selected source
  servers' **Migration lifecycle** column shows the **Cutover complete** status, the **Data replication
  status** column shows **Disconnected** and the
  **Next step** column shows **Mark as
  archived**.

The lifecycle also shows the status of any post-launch actions for the server. [Learn more about post-launch actions.](source-post-launch-settings.md "source-post-launch-settings.md")

## Understand data replication states

The **Data replication status** section provides an overview
of the overall source server status, including:

- **Replication progress** – The percentage of the server's
  storage that was successfully replicated.
- **Rescan progress** – The percentage of the server's
  storage that was rescanned (in the event of a rescan)
- **Total replicated storage** – The total amount of storage
  replicated (in GiB).
- **Lag** – Whether the server is experiencing any lag. If it
  is - the lag time is indicated.
- **Backlog** – Whether there is any backlog on the server
  (in MiB)
- **Elapsed replication time** – Time elapsed since
  replication first began on the server.
- **Last seen** – The last time the server successfully
  connected to AWS Application Migration Service.
- **Replication start time** – The date and time replication
  first began on the server.

Data replication can be in one of several states, as indicated in the panel title:

- **Initial sync**: initial copying of data from external
  servers is not done. Progress bar and **Total replicated
  storage** fields indicate how far along the process is.
- **Healthy:** all data has been copied and any changes at
  the source are continuously being replicated (data is flowing).
- **Rescan**: an event happened that forced the agent on the
  external server to rescan all of the blocks on all of the replicated disks. This is
  similar to the initial sync but faster because only changed blocks are copied. A
  rescan progress bar is displayed.
- **Stalled**: data is not flowing. You may need to
  intervene. When stalled, either the initial sync never completes, or the difference
  between the state of the replicated data and that of the source server continues to
  grow. When the state is stalled, then the replication initiation checklist is shown
  and indicates where the error occurred that caused the stall.

This panel also shows:

- **Total replicated storage:** size of all disks being
  replicated for this source server, and how much has been copied to AWS (once initial sync is
  complete)
- **Lag**: if you launch a recovery instance now, how far
  behind it will be from the state at the source. Normally this should be none.
- **Backlog**: how much data has been written at source but
  has not yet been copied to AWS. Normally this should be none.
- **Last**
  **seen**: when is the last time the AWS Replication Agent
  communicated with the AWS DRS service or the replication server.

If everything is working as it should and replication has finished initializing, the Data
replication progress section shows a **Healthy** status.

If there are initialization, replication, or connectivity errors, the **Data replication status** section shows the cause of the issue (for
example, a stall).

If the error occurred during the initialization process, then the exact step during which
the error occurred is marked with a red "x" under **Replication
initiation steps**.

## Understand the state of post-launch actions

The **Post-launch actions** view shows the current execution
status of post-launch actions.

The status includes:

- Name – the name of the action is a link to the detailed execution status in the [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/") console.
- Execution status – provides the current action status.
- Start time – the start time of the execution of the action script. This column is empty
  for actions that have not yet started execution.
- End time – the end time of the execution of the action script. This column is empty for
  actions that have not yet completed execution.
- Details – error messages are shown in this column.
- Link – used by the “DR after migration” action. Provides a link to the replicated server
  in the [AWS Elastic Disaster
  Recovery](https://aws.amazon.com/disaster-recovery/ "https://aws.amazon.com/disaster-recovery/") console.

## Review events and metrics in AWS CloudTrail

You can review AWS Application Migration Service events and metrics in AWS CloudTrail. Click on **View CloudTrail Event** History to openAWS CloudTrail in a new tab.

Learn more about [monitoring AWS MGN.](monitoring-overview.md "monitoring-overview.md")

Learn more about AWS CloudTrail events in the [AWS
CloudTrail user guide](../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md "../../../awscloudtrail/latest/userguide/cloudtrail-concepts.md").

## Understand server actions and replication control

You can perform a variety of actions, control data replication, and manage your testing
and cutover for an individual server from the server details view.

###### Topics

- [Actions menu](#server-actions "#server-actions")
- [Replication menu](#server-replication "#server-replication")
- [Test and cutover menu](#server-test-cutover "#server-test-cutover")
- [Alerts and errors](#server-test-cutover-alert "#server-test-cutover-alert")

### Actions menu

The **Actions** menu allows you to perform these
actions:

- **Add servers** – Choosing the **Add
  servers** option opens the Add servers prompt, through which you can construct
  a custom installation command to use when adding Linux or Windows source servers.

To construct a custom installation command, take these steps:

    1. Select your operating system. The installation command is different for Windows and
     Linux.


    ###### Note

    If you want to install the AWS Replication Agent on a legacy Windows OS (Windows
     Server 2003, Windows Server 2008 or Windows Server 2008 R2), you must choose
     the **Legacy OS: Windows Server 2003 or Windows Server
     2008** box. This downloads a unique version of the AWS Replication
     Agent installer that is only valid for legacy Windows OSs
     (`AwsReplicationWindowsLegacyInstaller.exe`). **Do not** use this installer file to install the agent
     on any other OS types.
    2. Select your replication preferences for the source server. The selected preferences
     are added as installation prompts to the custom installation command that are
     generated by this form.


    Choose the **Replicate all disks** option to replicate
     all of the disks of the source server. This is the default option. This option adds the
     `--no-prompt` prompt to the installation command.


    Select the **Choose which disks to replicate** option to
     choose which specific disks you want to replicate. You are prompted to select which
     disks to replicate during agent installation.
    3. Enter the credentials that [you previously generated for
     AWS Replication Agent installation](credentials.md "credentials.md"). The form does not send the secret, but does
     add it to the installation command.
    4. If you have not yet obtained the necessary credentials, [follow these instructions](credentials.md "credentials.md").
    5. If you are adding a Windows source server to AWS MGN, download the installer onto the
     source server. The installer is downloaded from the AWS Region of your account. If
     you're adding a Linux source server, skip this step.
    6. Copy the generated custom installation command and either input it into the command
     line on your source server. Proceed with [AWS
     Replication Agent installation as instructed in the documentation](agent-installation.md "agent-installation.md").

- **View server details** – Choosing this option to open the
  server details view for the selected server. This option is only available when a single
  server is selected.
- **Disconnect from service** – Choose this option to
  disconnect the selected server from Application Migration Service and AWS. This option disconnects the source
  server and should be used when data replication is complete.

On the **Disconnect X server/s from service** dialog,
choose **Disconnect**.

###### Important

This uninstalls the AWS Replication Agent from the source server and data
replication stops for the source server. If you need to restart data replication for
this server, you need to reinstall the agent. This action does not affect any test or
cutover instances that have been launched for this source server, but you are no longer
able to identify which source servers your Amazon EC2 instances correspond to.

- **Mark as archived** – Choose this option to archive the
  server. You should only archive servers for which you have already performed a cutover.
  Archived servers are removed from the main **Source
  servers** page, but can still be accessed through filtering options.

On the **Archive X servers** dialog, select **Archive**.

To see your archived servers, open the **Preferences**
menu by clicking the gear button. Select the **Show only archived
servers** option and click **Confirm**. You can now
see all of your archived servers. Unselect this option to see your non-archived
servers.

### Replication menu

The Replication menu allows you to manage data replication for your source servers
through these actions:

- **Edit replication settings** – Choose this option to be
  redirected to the **Edit replication settings** page, where you
  can edit specific replication settings for the selected source server. [Learn more about editing replication
  settings.](replication-settings-template.md "replication-settings-template.md")

### Test and cutover menu

The **Test and cutover menu** allows you to manage your test
and cutover instances.

- **Launch test instances** – Choose this option to launch a
  test instance for this server.

When the **Launch test instances for X** servers dialog
appears, click **Launch** to begin the test.

The AWS Application Migration Service console indicates **1 launch job
complete** after the test has been completed successfully.

- **Finalize testing** – Choose the **Mark as "Ready for cutover"** option to finalize testing for this server after
  you have completed all of the necessary tests in preparation for cutover.

When the **Mark X servers as "Ready for cutover"** dialog
appears, select whether you want to terminate the launched instances used for testing. We recommend that you terminate these instances, as you will be charged for them
even though you no longer need them. Check the **Yes, terminate launched instances
(recommended)** box and click **Continue**.

The AWS Application Migration Service console indicates that testing has been finalized. The selected
source servers' **Migration lifecycle** column shows the
**Ready for cutover** status and the launched test instances
are deleted if that option was selected.

- **Revert to "ready for testing"** – Choose this option to
  revert a finalized test for this server if you want to run further tests prior to initiating
  a cutover.

When the **Revert testing for X servers** dialog appears,
select whether you want to terminate the launched instances used for testing. We recommend that you terminate these instances, as you will be charged for them
even though you no longer need them. Check the **Yes, terminate launched instances
(recommended)** box and choose **Revert**.

The AWS Application Migration Service console indicates that testing has been reverted. The selected source
servers' **Migration lifecycle** column shows the **Ready for testing** status and the launched test instances are
deleted if that option was selected.

- **Launch cutover instances** – Choose this option to
  launch a cutover instance for this server after you have finalized all of your testing and
  are ready to initiate a cutover.

When the **Launch cutover instances for X**
**servers** dialog appears, click **Launch** to begin the cutover.

The AWS Application Migration Service console indicates **1 launch job
complete** after the cutover has been completed successfully.

This changes your source servers' **Migration
lifecycle** status to **Cutover in progress**,
indicating that the cutover is in progress but has not yet been finalized.

- **Finalize cutover** – Choose this option to finalize the
  cutover for this server after you have successfully performed a cutover.

This changes your source servers' **Migration
lifecycle** status to **Cutover complete**,
indicating that the cutover is complete and that the migration has been performed
successfully. In addition, this stops data replication and cause all replicated data to
be discarded. All AWS resources used for data replication are terminated.

When the **Finalize cutover for X servers** dialog
appears, click **Finalize**.

The AWS Application Migration Service console indicates **X servers cutover. Data
replication has been stopped for servers** once the cutover has been completed
successfully. The AWS Application Migration Service console automatically stops data replication for the cutover
source servers to save resource costs. The selected source servers' **Migration lifecycle** column shows the **Cutover** status, the **Data replication** column
shows **Disconnected** and the **Next
step** column states **Mark as archived**. The
source servers have now been successfully migrated into AWS and can be archived.

###### Note

This action does not uninstall the AWS Replication Agent from the source server. Use
the **Disconnect from service** option under the **Actions** menu when you have completed the migration and want to
uninstall the agent from your source server.

- **Revert to "ready for cutover"** – Choose this option to
  revert a finalized cutover for this server if you encounter any issues or want to reverse
  the cutover for any reason.

This reverts your source servers' **Migration
lifecycle** to the **Ready for cutover** status,
indicating that these servers have not undergone cutover.

When the **Revert cutover for X servers** dialog appears,
click **Revert**.

- **Edit launch settings** – Use this option to edit the
  launch settings for this server. This redirects you to the **Launch
  settings** tab. [Learn more about Launch
  settings.](launching-target-servers.md "launching-target-servers.md")
- **Terminate launched instance** – Choose this option if
  you want to delete your test or cutover instance for any reason at any time. This option can
  only be selected for a server that has a launched test or cutover instance.

When the **Terminate launched instance** dialog appears,
click **Terminate**.

- **Edit post-launch settings** – Choose this option to edit
  the post-launch settings for the selected source server or group of source servers. [Learn more about post-launch settings.](source-post-launch-settings.md "source-post-launch-settings.md")

### Alerts and errors

You can easily distinguish between healthy servers and servers that are experiencing
issues on the **Migration dashboard**.

The AWS Application Migration Service console is color-coded for ease of use.

- Healthy servers with no errors are characterized by the color blue in both the **Lifecycle** and **Data replication**
  **status** boxes.
- Servers that are experiencing temporary issues such as lagging or rescanning, are characterized by the color yellow.
  These issues do not halt the replication, but
  may delay it or indicate a bigger problem.
- Servers that are experiencing serious issues such as a loss of connection or a stall are characterized by the color red.
  You have to fix
  these issues for data replication to resume. The **Next actions** box provides additional information.

For example, if a stall occurred during initiation, you would scroll down to **Replication
initiation steps**, where the problematic step is marked with a red 'x'.
