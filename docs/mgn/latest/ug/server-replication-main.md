

# Manage data replication
<a name="server-replication-main"></a>

You can manage data replication for the source server through these actions on the **Replication** drop-down menu:
+ **Start data replication** – Restarts data replication for a source server on which data replication has been stopped. If you are using agent-based replication you don't necessarily have to reinstall the agent. 
+ **Stop data replication** – Stops data replication for a source server. Stopping the replication stops billing, deletes existing snapshots and storage volumes (Amazon EBS volumes or FSx for ONTAP volumes), and terminates replication servers. Configuration is retained, and if you are using agent-based replication the agent is not uninstalled. 
+ **Pause data replication** – Pauses data replication for a source server. Pausing the replication does not stop billing or delete existing snapshots or storage volumes. Replication servers are not terminated and if you are using agent-based replication the agent is not uninstalled from the source server. 
+ **Resume data replication** – Resume data replication for a paused source server. This syncs any changes since the last synchronization and completes the data replication flow. 
+ **Edit replication settings** – Edit the replication settings for the selected source servers. [Learn more about editing replication settings](replication-settings-template.md#edit-replication-settings).

Data replication begins automatically after the AWS Replication Agent is installed on the source server. Use the following procedures to start, stop, pause, or resume replication manually. You can select one or more source servers for each procedure.

To start data replication:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers on which data replication has been stopped.

1. Choose **Replication**, then choose **Start data replication**.

To stop data replication:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Replication**, then choose **Stop data replication**.

To pause data replication:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more source servers.

1. Choose **Replication**, then choose **Pause data replication**.

**Important**  
While replication is paused, changes made on the source server are not replicated to AWS, so replication lag accumulates. When you resume replication, MGN syncs the changes made since the last synchronization. Allow time for this sync to complete before you launch test or cutover instances.

To resume data replication:

1. Open the AWS Transform MGN console and navigate to the **Source servers** page.

1. Select the checkbox next to one or more paused source servers.

1. Choose **Replication**, then choose **Resume data replication**.