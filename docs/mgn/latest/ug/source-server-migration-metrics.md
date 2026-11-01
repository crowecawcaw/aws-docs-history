

# Source server migration metrics
<a name="source-server-migration-metrics"></a>

The source server migration metrics present an aggregated overview of your source servers, focused on three topics: **Alerts**, **Data replication status**, and **Migration lifecycle**.

## Understand source server alerts
<a name="source-server-migration-metrics-alerts"></a>

The source server **Alerts** migration metric presents an aggregated overview of your source servers' alerts. You can look up an individual source server's **Alerts** in the **Source servers** table at the bottom of the page. 
+ A healthy server for which a test or cutover instance has not been launched displays a **Healthy** status. 
+ A healthy server for which a test or cutover instance has been launched displays a **Launched** status. 
+ A server that is experiencing a temporary issue such as lag or backlog displays a **Lagging** status. 
+ A server that is experiencing significant issues, such as a stall, displays a **Stalled** status. 

## Understand data replication status
<a name="source-server-migration-metrics-status"></a>

The source server **Data replication status** migration metric presents an aggregated overview of your source servers' data replication status. You can look up an individual source server's **Data replication status** status in the **Source servers** table at the bottom of the page. 

Source server **Data replication status** can have one of these values: 
+ **Not started** – Data replication has not started.
+ **Initiating** – MGN is performing the replication initiation steps. If an error occurs, the step in which it occurred is marked with a red "x" under **Replication initiation steps** in the server details view.
+ **Initial sync** – The initial copying of data from the source server to AWS is in progress. The progress bar and the **Total replicated storage** field indicate how far along the process is.
+ **Finalizing sync**
+ **Creating snapshot**
+ **Transferring snapshot**
+ **Healthy** – All data has been copied, and any changes on the source server are continuously being replicated.
+ **Lagging** – Replication is active, but the replicated data is behind the state of the source server, for example because of lag or backlog. This is usually a temporary issue that does not halt replication.
+ **Rescanning** – An event forced the agent on the source server to rescan all of the blocks on all of the replicated disks. This is similar to the initial sync, but faster, because only changed blocks are copied.
+ **Stalled** – Data is not flowing, and you may need to intervene. Either the initial sync never completes, or the difference between the replicated data and the source server continues to grow. Review the **Next actions** box and the replication initiation steps in the server details view to find the cause.
+ **Paused** – Data replication has been paused. [Learn more about managing data replication](server-replication-main.md).
+ **Disconnected** – Data replication has stopped and the server is no longer connected to MGN, for example after the cutover was finalized or the server was disconnected from service.

## Understand the migration lifecycle metric
<a name="source-server-migration-metrics-lifecycle"></a>

The source server **Migration lifecycle** metric shows an aggregated overview of your source servers' migration lifecycle. You can look up an individual source server's **Migration lifecycle** status in the **Source servers** table at the bottom of the page. 

From **Ready for testing** through **Cutover complete**, data replication to your staging area subnet continues as long as the source server is available. Source server **Migration lifecycle** can have one of these values:
+ **Not ready** – The AWS Replication Agent is installed, but the initial sync is not yet complete.
+ **Ready for testing** – The initial sync is complete and ongoing replication is in progress. You can launch test instances.
+ **Test in progress** – You launched test instances. Use them to confirm that your applications work as expected.
+ **Ready for cutover** – You completed application testing and can launch production cutover instances. We recommend that you shut down the source server before you launch cutover instances, so that the source environment and the target instances don't drift apart.
+ **Cutover in progress** – Production cutover instances are launching.
+ **Cutover complete** – Production cutover instances finished launching. A cutover instance doesn't receive changes that occur on the source server after the instance launches. If the source server changed, choose [Revert to "ready for cutover"](server-test-cutover-main.md), and then launch new cutover instances to pick up the latest data.
+ **Disconnected** – You disconnected the source server from MGN. Changes to the source server are no longer replicated to your staging area subnet.
+ **Stopped** – You chose **Stop data replication**. Replication and billing for the source server are stopped. For how to restart replication, and how stopping differs from pausing, see [Manage data replication](server-replication-main.md).
+ **Discovered** – The agentless replication process discovered the source server, but the initial sync to your staging area subnet hasn't started.