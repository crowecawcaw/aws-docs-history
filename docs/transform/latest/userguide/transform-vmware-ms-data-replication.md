

# Step 4: Data replication
<a name="transform-vmware-ms-data-replication"></a>

After the replication agents are installed, data replication begins automatically. AWS Transform uses continuous block-level replication to synchronize data from source servers to AWS.

The replication process consists of two phases:
+ **Initial sync** – A complete copy of the source server data to AWS. Data is stored as Amazon Elastic Block Store (Amazon EBS) snapshots or on Amazon FSx for NetApp ONTAP (FSx for ONTAP) volumes in the target account, depending on your configured target storage type. For more information, see [Target storage type](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html#ebs-volume) in the *MGN User Guide*. Duration depends on data volume and network bandwidth.
+ **Continuous replication** – Ongoing synchronization of changed blocks with minimal impact on source server performance. Maintains an up-to-date copy in AWS.

Replication servers are temporary Amazon EC2 instances deployed in the staging area subnet. They receive replicated data from source servers and are automatically managed by MGN. For more information, see [Replication server settings](https://docs.aws.amazon.com/mgn/latest/ug/replication-server-settings.html) in the *MGN User Guide*.

AWS Transform monitors the replication progress and provides status updates, including replication status, replication lag (the time difference between source and replicated data), and bandwidth usage.

During replication, each server progresses through the following states:
+ **Not ready** – The server is undergoing the initial sync process and is not yet ready for testing.
+ **Ready for testing** – The server has been successfully added and data replication has started. Test or cutover instances can now be launched.

After all servers in the wave have progressed beyond the `NOT_READY` state, the data replication phase is complete and you can proceed to testing.

You can control replication for individual servers or the entire wave at any time:
+ **Pause replication** – Temporarily pause replication for specific servers or the entire wave.
+ **Resume replication** – Resume previously paused replication.
+ **Stop replication** – Permanently stop replication. Stopped replication can be restarted, but it begins from the initial sync.