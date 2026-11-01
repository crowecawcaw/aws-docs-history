

# Manage source servers
<a name="server-list"></a>

The **Source servers** page lists all of the source servers that have been added to AWS Transform MGN (AWS MGN). The **Source servers** page allows you to manage your source servers and perform a variety of commands for one or more servers (such as controlling replication and launching test and cutover instances). The **Source servers** page is the main page of AWS MGN console and you will most likely interact with AWS Transform MGN predominantly through this page. 

## Interacting with the source servers page
<a name="interracting"></a>

The **Source servers** page shows a list of source servers. Each row on the list represents a single server. The table displays **Active source servers** by default. You can use the dropdown menu above the first row to choose to display: 
+ **Agentless discovered servers** - servers discovered by the agentless replication process, which are not yet replicating.
+ **Imported servers** - servers whose information was imported into MGN, but an agent is not yet installed on them.
+ **Archived source servers** - servers whose migration has completed, and the users archived their data.

The **Source servers** page provides key information for each source server under each of the columns on the page.

The columns include:
+ **Selector column** – This blank checkbox selector column allows you to select one or more source servers. When a server is selected, you can interact with the server through the **Actions**, **Replication**, and **Test and cutover** menus. Selected servers are highlighted. 
+ **Source server name** – This column shows the unique server name for each source server.
+ **Alerts** – This column shows whether any alerts exist for the server.
  + **No indication** – a healthy server for which a test or cutover instance has not been launched. 
  + **Launched** – a healthy server for which a test or cutover instance has been launched.
  + **A clock icon with a warning message** – a server that is experiencing a temporary issue such as lag or backlog
  + **A red x and message** – a server that is experiencing significant issues, such as a stall.
+ **Replication type** – This column identifies whether the server is being replicated through the default **Agent based** replication or through **Snapshot shipping**. [Learn more about agentless based snapshot shipping replication for vCenter.](agentless-mgn.md)
+ **Migration lifecycle** – This column shows the migration lifecycle state for each source server, so you can see which lifecycle step the server is undergoing. [Learn more about migration lifecycle states](migration-dashboard.md#lifecycle).
  + **Not ready**
  + **Ready for testing**
  + **Test in progress**
  + **Ready for cutover**
  + **Cutover in progress**
  + **Cutover complete**
  + **Disconnected**
  + **Stopped** – Data replication has been stopped for the server.
  + **Discovered** – The server was discovered by the agentless replication process and is not yet replicating.
+ **Data replication status** – This column shows the current status of data replication for the server. The information presented in this column changes based on the server's Migration lifecycle state and whether the server is experiencing any issues. 

   This column shows a variety of information, including:
  + **Not Started** – Data replication has not started. 
  + **Paused** – Data replication has been paused.
  + **Healthy** – The server is healthy and ready for Test or Cutover instance launch. 
  + **Done** – The server has been successfully cutover and data replication has been stopped as a result. 
  + **Percentage complete** – The percentage of the server's storage that was successfully replicated if the server is undergoing initial sync or a rescan. 
  + **Lag** – Whether server is experiencing any lag. If it is; the lag time is indicated. 
  + **Backlog** – Whether there is any backlog on the server (in MiB).
+ **Last snapshot** – This column shows the time the last consistent snapshot was taken of the source server. Servers that are still in the initial sync process and those that have been disconnected do not show any info in this field. Healthy servers show a recent snapshot. Unhealthy servers' last snapshot indicates the last time they were healthy.
+ **Next step** – This column shows the next step that needs to be undertaken in order to successfully complete a cutover for the server. The information presented in this column changes based on the server's Migration lifecycle state and whether the server is experiencing any issues.

  This column shows a variety of next steps, including:
  + **Wait for initial sync to complete** – Data replication is initiating for the server. Wait for the initial sync process to complete. 
  + **Start data replication** – Data replication has not been started or has been stopped. For a paused server, choose **Resume data replication** from the **Replication** menu.
  + **Launch test instance** – The server is ready to launch a test instance.
  + **Complete testing and mark as 'Ready for cutover'** – The server has launched a Test instance that needs to be reverted or finalized.
  + **Launch cutover instance** – The server had a Test instance launched and finalized and now is ready to launch a cutover instance.
  + **Finalize cutover** – The server has launched a cutover instance that needs to be finalized.
  + **Terminate launched instance, Launch cutover instance** – The server is ready for cutover. Terminate the launched Test instance and launch a cutover instance.
  + **Resolve cause of stalled data replication** – The server is experiencing significant issues such as a stall that need to be addressed.
  + **Wait for lag to disappear, then X.** – The server is experiencing a temporary lag. Wait for the lag to disappear and then perform the indicated action.
  + **Mark as archived** – The server has been successfully cut over and can now be archived.

## Managing source servers by migration phase
<a name="server-actions-by-phase"></a>

The following table summarizes the actions you can perform on source servers at each phase of the migration lifecycle, and the console menu where each action is located.


**Managing source servers by migration phase**  

<table>
<thead>
  <tr><th>Action</th><th>Location</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td colspan="3"><b>Before migration</b></td></tr>
  <tr><td><a href="replication-settings.md">Edit replication settings</a></td><td><b>Replication</b> menu</td><td>Configure how data is replicated to the staging area in AWS.</td></tr>
  <tr><td><a href="launch-settings-source.md">Edit launch settings</a></td><td><b>Test and cutover</b> menu</td><td>Configure how test and cutover instances are launched in AWS.</td></tr>
  <tr><td><a href="source-post-launch-settings.md">Edit post-launch settings</a></td><td><b>Test and cutover</b> menu</td><td>Configure actions that run automatically after a test or cutover instance is launched.</td></tr>
  <tr><td><a href="source-server-tags.md">Manage tags</a></td><td>Server details, <b>Tags</b> tab</td><td>Add or remove tags to organize and filter source servers.</td></tr>
  <tr><td><a href="add-server-server-page.md#server-actions-main">Add server to application</a></td><td><b>Actions</b> menu</td><td>Group related servers into an <a href="applications.md">application</a> to migrate them together.</td></tr>
  <tr><td colspan="3"><b>During migration</b></td></tr>
  <tr><td><a href="server-replication-main.md">Start, stop, pause, or resume data replication</a></td><td><b>Replication</b> menu</td><td>Control data replication from the source server to AWS.</td></tr>
  <tr><td><a href="launching-test-servers.md">Launch test instances</a></td><td><b>Test and cutover</b> menu</td><td>Launch a test instance to validate the migrated server. Data replication continues during the test.</td></tr>
  <tr><td><a href="finalizing-test.md">Mark as "Ready for cutover"</a></td><td><b>Test and cutover</b> menu</td><td>Finalize testing. You can choose to terminate the launched test instances.</td></tr>
  <tr><td><a href="revert-finalize-test.md">Revert to "ready for testing"</a></td><td><b>Test and cutover</b> menu</td><td>Revert a finalized test to run more tests.</td></tr>
  <tr><td><a href="launch-cutover.md">Launch cutover instances</a></td><td><b>Test and cutover</b> menu</td><td>Launch the cutover instance. Before you launch, confirm that there is no lag and stop all operational services on the source server.</td></tr>
  <tr><td><a href="server-test-cutover-main.md">Terminate launched instance</a></td><td><b>Test and cutover</b> menu</td><td>Delete a launched test or cutover instance.</td></tr>
  <tr><td colspan="3"><b>After migration</b></td></tr>
  <tr><td><a href="server-post-migration.md#server-post-migration-finalize-cutover">Finalize cutover</a></td><td><b>Test and cutover</b> menu</td><td>Complete the migration. This stops data replication and terminates the AWS resources used for replication. The AWS Replication Agent receives a command to uninstall itself (within 10 minutes).</td></tr>
  <tr><td><a href="server-test-cutover-main.md">Revert to "ready for cutover"</a></td><td><b>Test and cutover</b> menu</td><td>Revert a finalized cutover if you encounter issues.</td></tr>
  <tr><td><a href="server-post-migration.md#server-post-migration-disconnect">Disconnect from service</a></td><td><b>Actions</b> menu</td><td>Uninstall the AWS Replication Agent from the source server and stop data replication.</td></tr>
  <tr><td><a href="server-post-migration.md#server-post-migration-archive">Mark as archived</a></td><td><b>Actions</b> menu</td><td>Remove a cut-over server from the main <b>Source servers</b> list.</td></tr>
  <tr><td><a href="server-post-migration.md#server-post-migration-delete">Delete from service</a></td><td><b>Actions</b> menu</td><td>Remove the source server record from MGN. Only servers that are not actively replicating can be deleted.</td></tr>
</tbody>
</table>


**Topics**
+ [Interacting with the source servers page](#interracting)
+ [Managing source servers by migration phase](#server-actions-by-phase)
+ [Manage source server records](add-server-server-page.md)
+ [Manage data replication](server-replication-main.md)
+ [Manage test and cutover instances](server-test-cutover-main.md)
+ [Manage source servers after migration](server-post-migration.md)
+ [Source server migration metrics](source-server-migration-metrics.md)
+ [Filtering the source servers list](list-filtering.md)