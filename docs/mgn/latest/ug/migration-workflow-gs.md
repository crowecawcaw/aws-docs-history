NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Migration workflow

The general process is:

1. Initialize AWS Application Migration Service in the target region. Refer to the [list](supported-regions.md "supported-regions.md") of
   supported AWS regions.
2. Install the AWS Replication Agent on the source server. Learn more about [agent installation](source-servers.md "source-servers.md") .

###### Note

If you are using the agentless replication for vCenter feature, then you will need to add
your source servers by installing the AWS MGN vCenter Client. [Learn more about agentless replication.](agentless-mgn.md "agentless-mgn.md") 3. Wait until the initial sync is finished. After installing the agent, you need to wait for
the initial synchronization process to complete. This process performs block level replication
from the source server to the replication server in staging area. 4. Launch test instances. Once the initial sync is finished, you can launch a target machine
in Test Mode. This allows you to perform acceptance testing and verify that the migrated
environment is functioning correctly. 5. Perform acceptance tests on the servers. After the test instance is tested successfully,
finalize the test and delete the test instance. 6. Configure Post-launch actions (if needed). Learn more about [Post-launch settings](post-launch-settings.md "post-launch-settings.md") . 7. Wait for the cutover window. 8. Confirm that there is no lag. 9. Stop all operational services on the source server. 10. Launch a cutover instance. Launch the target machine in Cutover Mode, which initiates the
final migration process. 11. Confirm that the cutover instance was launched successfully and then finalize the cutover. 12. Archive the source server.
