# Reduced downtime

Conductor Live upgrade

The process outlined in this section uses worker redundancy to limit the upgrade downtime.
This process applies when the following are true:

- The worker nodes are in a redundancy group.
- You are upgrading the worker nodes and the AWS Elemental Conductor Live node or nodes to the same
  major version. For example, 2.25.5 and 3.25.5.
- The cluster is in a working state. If any node is in a degraded state (not
  responding or not accepting jobs), the upgrade on that node won't work.
  If these conditions don't apply, see [Standard Conductor Live upgrade](upgrades-cl3-upg-std.md "upgrades-cl3-upg-std.md").

###### Note

In this procedure, we show how to upgrade from version 3.23.5 to version
3.25.5 (for Conductor Live ) and from version 2.23.5 to version
2.25.5(for worker nodes). Modify your commands to specify the version that you
are upgrading to.

###### To check the type of redundancy of your deployment

1.  On the web interface for the primary Conductor Live node, access **Conductor Live** > **Redundancy**.
2.  Look in the **Redundancy Group** task bar:

        * If you find any groups labeled as **Live**, your cluster
         is using worker redundancy and you can perform the
         reduced downtime upgrade.
        * If you find any groups labeled as **Conductor Live**,
         your cluster is using Conductor Live redundancy (high availability).

    The following procedure shows the comprehensive reduced downtime upgrade process. This process
    is valid whether or not you have Conductor Live redundancy. It will guide you to your next step
    based on your circumstances through the steps provided.

###### Topics

- [Step A: Get
  ready](upgrades-cl3-upg-red-single-ver-version.md "upgrades-cl3-upg-red-single-ver-version.md")
- [Step B: Copy the AWS Elemental installers](upg-red-copy-ins.md "upg-red-copy-ins.md")
- [Step C: Remove the backup worker
  nodes](upg-red-remove-bup.md "upg-red-remove-bup.md")
- [Step D: Upgrade the backup worker
  nodes](upg-red-b-wrker.md "upg-red-b-wrker.md")
- [Step E: Add back the backup worker
  nodes](upg-red-add-bup.md "upg-red-add-bup.md")
- [Step F: Fail over an active node](upg-red-fail.md "upg-red-fail.md")
- [Step G: Remove the failed worker
  node](upg-red-remove-failed.md "upg-red-remove-failed.md")
- [Step H: Upgrade the failed active
  node](upg-red-a-wrker.md "upg-red-a-wrker.md")
- [Step I: Add failed worker node](upg-red-add-failed.md "upg-red-add-failed.md")
- [Step J: Fail back the running channels](upg-red-back.md "upg-red-back.md")
- [Step K: Re-designate the backup worker
  node](upg-red-redesignate.md "upg-red-redesignate.md")
- [Step L: Disable high availability](upg-red-disable.md "upg-red-disable.md")
- [Step M: Remove the secondary Conductor Live
  node](upg-red-rem-sec.md "upg-red-rem-sec.md")
- [Step N: Upgrade the secondary
  Conductor Live node](upg-red-sec.md "upg-red-sec.md")
- [Step O: Upgrade the primary Conductor
  node](upg-red-pri.md "upg-red-pri.md")
- [Step P: Add the secondary Conductor Live
  node](upg-red-add-sec.md "upg-red-add-sec.md")
- [Step Q: Re-enable high
  availability](upg-red-reenable.md "upg-red-reenable.md")
