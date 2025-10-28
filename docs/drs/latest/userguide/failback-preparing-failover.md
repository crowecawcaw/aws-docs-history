# Performing a failover with Elastic Disaster Recovery

A failover is the redirection of traffic from a primary system to a secondary system. It's
a network operation that's performed outside of AWS Elastic Disaster Recovery. AWS Elastic Disaster Recovery helps you perform a failover by launching recovery instances in AWS. Once the Recovery
instances are launched, you will need to redirect the traffic from your primary systems to the
launched recovery instances.

###### Note

These instructions also apply to the cross-Region or cross-AZ failover process.

## Launching recovery instances

### Ready for launch indicators

Prior to launching a Recovery instance, ensure that your source servers are
ready for testing by looking for these indicators on the **Source Servers** page:

1. Under the **Ready for recovery** column, the server should
   show
   **Ready**
2. Under the **Data replication status**
   column, the server should show the **Healthy** status.
3. Under the **Last recovery result**
   column, there should be an indication of a successful Drill instance
   launch sometime in the past. The column should state **Successful** and show when the last successful
   launch occurred. This column may be empty if a significant amount of
   time passed since your last drill instance launch.

### Launching recovery instances

To launch a recovery instance for a single source server or multiple source
servers:

1. Go to the **Source servers** page and
   select each server for which you want to launch a recovery instance.
2. Open
   the **Initiate recovery job** menu and select
   **Initiate recovery**.
3. Select the Point in time snapshot from which to launch the recovery instance for the selected
   source server. You can either select the **Use most
   recent data** option to use the latest snapshot available
   or select an earlier specific Point-in-time snapshot. You may opt to
   select an earlier snapshot in case you wish to return to a specific
   server configuration before a disaster occurred.
4. Choose **Initiate recovery**.

[Learn more about Point in Time
snapshots.](CloudEndure-Concepts.md#point-in-time-faq "CloudEndure-Concepts.md#point-in-time-faq")

The AWS Elastic Disaster Recovery Console will indicate **Recovery job is creating drill instance for X source servers**
when the drill has started.

Click **View job details** on the dialog to view
the specific job for the test launch in the **Recovery job
history** tab.

### Successful recovery instance launch

indicators

You can tell that the recovery instance launch started successfully through
several indicators on the **Source servers** page.

1. The **Last recovery result** column will show the status of
   the recovery launch and the time of the launch. A successful recovery instance launch will
   show the **Successful** status. A launch that is still in
   progress will show the **Pending** status.
2. The launched recovery instance will appear on the **Recovery instances** page. [Learn more about the Recovery instances
   page.](recovery-instances.md "recovery-instances.md")
3. You can now redirect traffic from your primary systems to the launched
   recovery instances.

###### Note

Launch of a new recovery instance from the same source server will clean up all the previous recovery instances, regardless if they have been disconnected and deleted from DRS
