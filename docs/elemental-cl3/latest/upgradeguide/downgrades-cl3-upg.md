# Cluster downgrades in

Conductor Live

In a AWS Elemental Conductor Live cluster, downgrade the Conductor Live nodes first, and then downgrade each of the
Elemental Live worker nodes.

###### Downgrade rules

The following rules apply when you're downgrading Conductor Live
software.

- Your system must be in a working state prior to the downgrade. If
  it's in a degraded state (for example, it is failing to successfully
  create events or channels, or it isn't responding through the web interface), the
  downgrade does not work.
- You can downgrade to a version that's a maximum of two major versions below your current
  version. For example, for Conductor Live, you can downgrade from 3.25.5 to
  3.23.5. (The number of minor versions between the two versions is irrelevant.)
- We recommend that you always downgrade to the highest minor version in the series you're
  downgrading to. For example, downgrade to 3.23.5.
- To downgrade over a bigger span than two major versions, you must perform the downgrade
  in several steps. For example, downgrade from 3.25.5 to 3.23.5, then
  to 3.22.5.

###### Important

Plan to downgrade during a maintenance window. All activity on the
nodes stops during downgrade.

In this procedure, we show how to downgrade from version 3.25.5 to version
3.23.5(for Conductor Live ) and from version 2.25.5 to 2.23.5 (for
worker nodes). Modify your commands to specify the version that you are downgrading to.

###### Topics

- [Step A: Get ready](downgrades-cl3-upg-locate-res-dn.md "downgrades-cl3-upg-locate-res-dn.md")
- [Step B: Copy the AWS
  Elemental installers](downgrades-cl3-upg-locate-sw-dn.md "downgrades-cl3-upg-locate-sw-dn.md")
- [Step C: Stop the running
  channels](downgrades-cl3-upg-stop-chan.md "downgrades-cl3-upg-stop-chan.md")
- [Step D: Disable high availability on the
  Conductor nodes](downgrades-cl3-upg-ha-disable-ha.md "downgrades-cl3-upg-ha-disable-ha.md")
- [Step E: Remove the secondary
  Conductor node](downgrades-rem-sec.md "downgrades-rem-sec.md")
- [Step F: Downgrade the nodes](downgrades-cl3-upg-dg-cond.md "downgrades-cl3-upg-dg-cond.md")
- [Step G: Add the secondary
  Conductor Live node](downgrades-add-sec.md "downgrades-add-sec.md")
- [Step H: Start channels](downgrades-start.md "downgrades-start.md")
- [Step I: Re-enable high availability](downgrades-reenable.md "downgrades-reenable.md")
