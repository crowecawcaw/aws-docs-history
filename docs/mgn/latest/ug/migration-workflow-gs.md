

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Migration workflow
<a name="migration-workflow-gs"></a>

The general process is:

1.  Initialize AWS Transform MGN in the target region. Refer to the [list ](https://docs.aws.amazon.com/mgn/latest/ug/supported-regions.html) of supported AWS regions.

1. Install the AWS Replication Agent on the source server. Learn more about [agent installation ](https://docs.aws.amazon.com/mgn/latest/ug/source-servers.html).
**Note**  
If you are using the agentless replication for vCenter feature, then you will need to add your source servers by installing the MGN vCenter Client. [Learn more about agentless replication.](agentless-mgn.md)

1. Wait until the initial sync is finished. After installing the agent, you need to wait for the initial synchronization process to complete. This process performs block level replication from the source server to the replication server in staging area. 

1. Launch test instances. Once the initial sync is finished, you can launch a target machine in Test Mode. This allows you to perform acceptance testing and verify that the migrated environment is functioning correctly. 

1. Perform acceptance tests on the servers. After the test instance is tested successfully, finalize the test and delete the test instance. 

1. Configure Post-launch actions (if needed). Learn more about [Post-launch settings ](https://docs.aws.amazon.com/mgn/latest/ug/post-launch-settings.html). 

1. Wait for the cutover window. 

1. Confirm that there is no lag.

1. Stop all operational services on the source server. 

1. Launch a cutover instance. Launch the target machine in Cutover Mode, which initiates the final migration process. 

1. Confirm that the cutover instance was launched successfully and then finalize the cutover. 

1. Archive the source server. 