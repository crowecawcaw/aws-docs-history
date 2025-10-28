# Cluster Upgrades in Conductor Live

There are two types of upgrade that you can perform on an AWS Elemental Conductor Live cluster:

- **Standard upgrade**: Use this for any type of cluster and
  redundancy configuration. Do this type of upgrade in a maintenance window since all nodes
  are offline for the duration of the upgrade process.
- **Reduced downtime upgrade**: Use this for clusters that
  have worker redundancy. This type of upgrade leverages worker node redundancy. Therefore the
  downtime is typically less than 30 seconds.
  This document describes both upgrade processes.

###### Topics

- [Standard Conductor Live upgrade](upgrades-cl3-upg-std.md "upgrades-cl3-upg-std.md")
- [Reduced downtime
  Conductor Live upgrade](upgrades-cl3-upg-red.md "upgrades-cl3-upg-red.md")
- [Sample Upgrade](sample-upg-cl3-upg.md "sample-upg-cl3-upg.md")
