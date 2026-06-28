NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Does MGN work with...?

This section contains answers to questions about what AWS Transform MGN works with.

## Does MGN work with Microsoft Windows Failover Clustering?

Yes.

## Does MGN work with Bitlocker encryption?

AWS Transform MGN does not support OS-based disk encryption features such as BitLocker. These should
be deactivated before using MGN.

## Does MGN work with FSx for ONTAP?

Yes. MGN can replicate data volumes to an FSx for ONTAP file system. The following
describes how data flows during replication and launch:

- **During replication**: The AWS Replication Agent on
  your source servers sends data to MGN replication servers. When FSx for ONTAP is configured
  as the target storage type, MGN writes the replicated data volumes to the FSx for ONTAP
  file system via iSCSI.
- **At launch and cutover**: The target EC2 instances
  connect to the FSx for ONTAP file system via iSCSI to access their data volumes. The boot
  volume always remains on Amazon EBS.
- **Network**: Security groups must allow iSCSI traffic
  (port 3260) between MGN instances and the FSx for ONTAP file system.
- **Authentication**: Communication is secured using
  certificate-based authentication. You store the certificates in AWS Secrets Manager, and MGN
  uses them to authenticate with the FSx for ONTAP file system.

**Key points:**

- Agent-based replication only – FSx for ONTAP is supported only with agent-based
  replication.
- Per-server configuration – You can use FSx for ONTAP for some servers and Amazon EBS
  for others in the same wave.
- Boot volume – Always stored on Amazon EBS regardless of target storage type.
- Up to 5 FSx for ONTAP file systems per account concurrently.

For full setup instructions, see
[FSx for ONTAP configuration guide](fsx-ontap.md "fsx-ontap.md").
