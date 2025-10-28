# Interacting with the Source Servers page

The **Source servers** page shows a list of source servers.
Each row on the list represents a single server.

The **Source servers** page provides key information for each
source server under each of the columns on the page.

The columns include:

- **Selector column** – This blank checkbox selector column
  allows you to select one or more source servers. When you select a server you can
  interact with it through the **Actions**, **Replication**, and **Initiate recovery
  job** menus. Selected servers are highlighted.
- **Hostname** – This column shows the unique server hostname
  for each source server.
- - **Ready for recovery** – This column shows whether the
    server is ready for recovery. You can use this column to easily tell whether a server is
    ready or not and the server's exact status. You can learn more about the server's status
    by reviewing the **Data replication status** column.
  - A server that is ready shows the green checkmark and **Ready**.
  - A server that is ready, but is experiencing a non-critical issue such as lag shows the
    blue info sign and **Ready** and displays the lag
    duration to the right.
  - A server that is still undergoing initial sync shows a gray circle with three dots and
    **Initial sync**.
  - A server that is disconnected shows the gray warning sign and **Disconnected**.
  - A server that is not ready due to a significant error, such as a stall, shows a red
    **X** and **Not Ready**.
    Servers that have one or more marketplace licenses assigned to them may not be able to
    launch if there was an error reading their license information.
- **Data replication status** – This column shows the current
  status of data replication for the server :
  - **Initiating** – The server has just been added to AWS Elastic Disaster Recovery and replication is being initiated.
  - **Initial sync** – The server is undergoing the initial
    sync process. The console displays the percentage of the server data that has been synced
    and the step the server is undergoing in the initial sync process. You can learn
    more about the exact state of the server in the server info view.
  - **Rescanning** – The server is undergoing a rescan. The
    console displays the percentage of the server data that has been rescanned successfully.
  - **Healthy** – The server is healthy and is ready to
    initiate a recovery job.
  - **Lag** – The server is experiencing lag. The console
    displays the amount of lag time. You can learn more about the exact state of the
    server in the server info view.
  - **Stalled** – The server is stalled due to a replication
    error. You can learn more about the specific cause of the stall in the server info
    view.
  - **Disconnected** – The server has been disconnected from
    AWS Elastic Disaster Recovery.

- **Last recovery result** – This column shows the result of
  the last recovery job launch. The column is empty if no recovery job has ever been
  launched for the server:
  - **Successful** - Recovery launch job was completed
    successfully. The console indicates how long ago the job was completed.
  - **Failed** – Recovery launch job failed. The console
    indicates how long ago the job failed. You can learn more about why the job failed
    in the job history.
  - **Pending** – Recovery launch job is pending. The console
    indicates how long ago the job was initiated.

- **Pending actions** – This column shows any pending actions
  that need to be performed on the server. This column appears empty unless there is an
  actionable pending action. Actions include:
  - **Initiate drill** – The source server is healthy, but no
    drill instances have been launched for the source server. Initiate a drill by
    launching a drill instance.
  - **Resolve cause of stall** – The source server is stalled.
    Resolve the cause of the stall for the server to return to healthy function.
  - **Reinstall AWS Replication Agent** – The AWS Replication
    Agent was removed from the source server. Reinstall the agent for replication to
    resume.
  - **Error: Missing permissions to retrieve marketplace licenses from the source account, cannot launch this server** –
    The marketplace license belongs to a different AWS account, permissions to get information about this marketplace license are missing.
    [Create a Failback and in-AWS right-sizing role for trusted account](adding-trusted-account.md#trusted-accounts-failback-role "adding-trusted-account.md#trusted-accounts-failback-role")
    using the target account AWS account ID.
  - **Warning: server uses marketplace product, drill recommended** –
    This source server uses one or multiple marketplace licenses.
    Doing a drill is strongly recommended as some marketplace incompatibilities can only be identified during launch.
    [Learn more here.](marketplace-license-requirements.md "marketplace-license-requirements.md")
