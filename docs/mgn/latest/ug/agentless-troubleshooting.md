NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Troubleshooting agentless replication issues

**Discovery** related troubleshooting

- No machines are discovered -

Verify vCenter client is still connected to the service and able to communicate with the required endpoints.

Verify vCenter user permissions, which you have configured the MGN Agentless client with, are correct by reviewing the [agentless snapshot based replication section](agentless-mgn.md "agentless-mgn.md").

- The same Machine is discovered twice -

Source Servers are identified by their vCenter UUID. If a server changes its UUID (which may happen in edge cases), the same guest can appear as two source servers, where only one of them is responsive (the new UUID). In this case, you may archive the previous source server, or use the API to delete it.

- Two machines with the same UUID -

Both replications are stalled, duplicate UUID reported to the service log. The workaround is to change the UUID of one of the machines. [Learn more about changing UUID](https://knowledge.broadcom.com/external/article?legacyId=1541 "https://knowledge.broadcom.com/external/article?legacyId=1541")
**Agentless Replication** related troubleshooting

- Replication state is STALLED -

Verify vCenter client is still connected to the service and able to communicate with the required endpoints.

- dataReplicationError is UNSUPPORTED_VM_CONFIGURATION -

Try to delete all VMWare snapshots on the guest, and wait for the next iteration. This usually works around snapshotting and CBT issues

- dataReplicationError is LAST_SNAPSHOT_JOB_FAILED

Check to see if the snapshots are successfully being created in vCenter. You can check this by clicking on the VM which is in the error state > Choosing Monitor tab > Tasks

Check the replication log which can be found at `/var/lib/aws-vcenter-client/active/tmp/*Unique-ID*/*snapshot-num*.log.0`
**Logs**

/var/lib/aws-vcenter-client/active/aws-vcenter-client-upgrader.log - This is the log for the upgrade process of the Agentless client software

/var/lib/aws-vcenter-client/active/vcenter_commands_client.log - This is the main agentless client log that will show the log of the agentless discovery process, etc.

/_installation-directory_/aws-vcenter-client-installer.log - This log will show any issues with the installation process of the MGN agentless client. This will be located in the directory that you have executed the installer from.

/var/lib/aws-vcenter-client/active/tmp/_Unique-ID_/_snapshot-num_.log.0 - When you start replication for a discovered server, it will create a snapshot in vCenter and generate this log which is similar to the agent log. For each snapshot, there is a different log. This will show a log of replication process for the snapshot.
