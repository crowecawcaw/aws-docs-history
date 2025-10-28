# Standard Conductor Live upgrade

The process outlined in this section is for a standard upgrade of the AWS Elemental Conductor Live software,
where all nodes are taken offline and upgraded within a maintenance window. If your worker
nodes are in a redundancy group and you want to limit downtime outside of a maintenance
window, see [Reduced downtime
Conductor Live upgrade](upgrades-cl3-upg-red.md "upgrades-cl3-upg-red.md").

This process applies when the following are true:

- You're upgrading to Conductor Live to a specific version, and you're upgrading all the
  worker nodes to the matching version. For example 3.25.5 (for Conductor Live) and
  2.25.5 (for worker nodes).
- The cluster is in a working state. If any nodes are in a degraded state (not
  responding or not accepting jobs), any upgrades you might make to that node won't
  work.
  This comprehensive upgrade process is valid regardless of the type of redundancy you're
  using and whether or not you're upgrading worker nodes.

###### Note

In this procedure, we show how to upgrade from version 3.23.5 to version
3.25.5. Modify the commands to specify the version that you are upgrading to.

###### Topics

- [Step A: Get ready](upgrades-cl3-upg-single-ver-version.md "upgrades-cl3-upg-single-ver-version.md")
- [Step B: Copy the AWS Elemental installers](upg-std-copy-ins.md "upg-std-copy-ins.md")
- [Step C: Disable high availability](upg-std-disable.md "upg-std-disable.md")
- [Step D: Remove the secondary Conductor Live node](upg-std-rem-sec.md "upg-std-rem-sec.md")
- [Step E: Stop the running channels](upg-std-stop.md "upg-std-stop.md")
- [Step F: Remove worker nodes](upg-std-remove-w.md "upg-std-remove-w.md")
- [Step G: Upgrade worker nodes](upg-std-all.md "upg-std-all.md")
- [Step I: Add worker nodes](upg-std-add-w.md "upg-std-add-w.md")
- [Step J: Add the secondary Conductor Live node](upg-std-add-sec.md "upg-std-add-sec.md")
- [Step K: Start channels](upg-std-start.md "upg-std-start.md")
- [Step L: Re-enable high availability](upg-std-reenable.md "upg-std-reenable.md")
