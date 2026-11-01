

# Migration workflow
<a name="migration-workflow-gs"></a>

The general process is:

1.  Initialize AWS Transform MGN in the target region. Refer to the [list ](what-is-mgn.md#supported-regions) of supported AWS regions.

1. Install the AWS Replication Agent on the source server. Learn more about [agent installation ](source-servers.md).

1. Wait until the initial sync is finished. After installing the agent, you need to wait for the initial synchronization process to complete. This process performs block level replication from the source server to the replication server in staging area. 

1. Launch test instances. Once the initial sync is finished, you can launch a target machine in Test Mode. This allows you to perform acceptance testing and verify that the migrated environment is functioning correctly. 

1. Perform acceptance tests on the servers. After the test instance is tested successfully, finalize the test and delete the test instance. 

1. Configure Post-launch actions (if needed). Learn more about [Post-launch settings ](post-launch-settings.md). 

1. Wait for the cutover window. 

1. Confirm that there is no lag.

1. Stop all operational services on the source server. 

1. Launch a cutover instance. Launch the target machine in Cutover Mode, which initiates the final migration process. 

1. Confirm that the cutover instance was launched successfully and then finalize the cutover. 

1. Archive the source server. 

For a checklist with the key actions, completion indicators, and links to detailed instructions for each step, see [Quick start guide for AWS Transform MGN](quick-start-guide-gs.md).