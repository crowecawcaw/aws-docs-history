NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage source servers

The **Source servers** page lists all of the source servers
that have been added to AWS Application Migration Service (AWS MGN). The **Source servers**
page allows you to manage your source servers and perform a variety of commands for one or more
servers (such as controlling replication and launching test and cutover instances). The **Source servers** page is the main page of AWS MGN console and you will most
likely interact with AWS Application Migration Service predominantly through this page.

## Interacting with the source servers page

The **Source servers** page shows a list of source servers.
Each row on the list represents a single server. The table displays **Active source servers** by default. You can use the dropdown menu above the first row to choose to display:

- **Agentless discovered servers** - servers discovered by the agentless
  replication process, which are not yet replicating.
- **Imported servers** - servers whose information was imported into MGN, but
  an agent is not yet installed on them.
- **Archived source servers** - servers whose migration has completed, and the
  users archived their data.

The **Source servers** page provides key information for each
source server under each of the columns on the page.

The columns include:

- **Selector column** – This blank checkbox selector column
  allows you to select one or more source servers. When a server is selected, you can interact
  with the server through the **Actions**, **Replication**, and **Test and cutover** menus.
  Selected servers are highlighted.
- **Source server name** – This column shows the unique server
  name for each source server.
- **Alerts** – This column shows whether any alerts exist for
  the server.
  - **No indication** – a healthy server for which a test or
    cutover instance has not been launched.
  - **Launched** – a healthy server for which a test of
    cutover instance has been launched.
  - **A clock icon with a warning message** – a server that is
    experiencing a temporary issue such as lag or backlog
  - **A red x and message** – a server that is experiencing
    significant issues, such as a stall.

- **Replication type** – This column identifies whether the
  server is being replicated through the default **Agent based**
  replication or through **Snapshot shipping**. [Learn more about agentless based snapshot shipping replication for
  vCenter.](agentless-mgn.md "agentless-mgn.md")
- **Migration lifecycle** – This column shows the migration
  lifecycle state for each source server. This way you can easily know which lifecycle
  step the server is undergoing. Migration lifecycle steps include these: [Learn more about Migration lifecycle
  steps](migration-dashboard.md#initiation "migration-dashboard.md#initiation").
  - **Not ready**
  - **Ready for testing**
  - **Test in progress**
  - **Ready for cutover**
  - **Cutover in progress**
  - **Cutover complete**
  - **Disconnected**

- **Data replication status** – This column shows the current
  status of data replication for the server. The information presented in this column changes
  based on the server's Migration lifecycle state and whether the server is experiencing any
  issues.

This column shows a variety of information, including:

    + **Not Started** – Data replication has not started.
    + **Paused** – Data replication has been paused.
    + **Healthy** – The server is healthy and ready for Test or
     Cutover instance launch.
    + **Done** – The server has been successfully cutover and
     data replication has been stopped as a result.
    + **Percentage complete** – The percentage of the server's
     storage that was successfully replicated if the server is undergoing initial sync or a
     rescan.
    + **Lag** – Whether server is experiencing any lag. If it
     is; the lag time is indicated.
    + **Backlog** – Whether there is any backlog on the server
     (in MiB).

- **Last snapshot** – This column shows the time the last
  consistent snapshot was taken of the source server. Servers that are still in the initial sync
  process and those that have been disconnected do not show any info in this field. Healthy
  servers shows a recent snapshot. Unhealthy servers' last snapshot indicates the last time
  they were healthy.
- **Next step** – This column shows the next step that needs
  to be undertaken in order to successfully complete a cutover for the server. The information
  presented in this column changes based on the server's Migration lifecycle state and whether
  the server is experiencing any issues.

This column shows a variety of next steps, including:

    + **Wait for initial sync to complete** – Data replication
     is initiating for the server. Wait for the initial sync process to complete.
    + **Start data replication** – Data replication has not been
     started or is paused.
    + **Launch test instance** – The server is ready to launch a
     test instance.
    + **Complete testing and mark as 'ready for cutover'** – The
     server has launched a Test instance that needs to be reverted or finalized.
    + **Launch cutover instance** – The server had a Test
     instance launched and finalized and now is ready to launch a cutover instance.
    + **Finalize cutover** – The server has launched a cutover
     instance that needs to be finalized.
    + **Terminate launched instance, Launch cutover instance** –
     The server is ready for cutover. Terminate the launched Test instance and launch a cutover
     instance.
    + **Resolve cause of stalled data replication** – The server
     is experiencing significant issues such as a stall that need to be addressed.
    + **Wait for lag to disappear, then X.** – The server is
     experiencing a temporary lag. Wait for the lag to disappear and then perform the indicated
     action.
    + **Mark as archived** – The server has been successfully
     cut over and can now be archived.

###### Topics

- [Add a source server](add-server-server-page.md "add-server-server-page.md")
- [Manage data replication](server-replication-main.md "server-replication-main.md")
- [Manage test and cutover instances](server-test-cutover-main.md "server-test-cutover-main.md")
- [Source server migration metrics](source-server-migration-metrics.md "source-server-migration-metrics.md")
- [Filtering the source servers list](list-filtering.md "list-filtering.md")
