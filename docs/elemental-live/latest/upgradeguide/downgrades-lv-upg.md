# Downgrades in Elemental Live

This section describes how to downgrade the AWS Elemental Live software version.

###### Downgrade rules

The following rules apply when you're downgrading
AWS Elemental Live software.

- Your system must be in a working state prior to the downgrade. If
  it's in a degraded state (for example, it is failing to
  successfully craete events, or it isn't responding through the web
  interface), the downgrade does not work.
- You can downgrade to a version that's a maximum of two major versions below your current
  version. For example, from
  2.25.4 to 2.23.5
  (The number of minor versions between the two versions is irrelevant.)
- However, we recommend that you always downgrade to the highest minor version in the
  series you're downgrading to. For example, downgrade to 2.23.5. Don't downgrade
  to 2.23.1.
- To downgrade over a bigger span than two major versions, you must perform the downgrade
  in several steps. For example, downgrade from 2.25.4 to 2.23.5 and
  then to 2.22.5.

###### Important

Plan to downgrade during a maintenance window. All activity on the
nodes stops during downgrade.

###### Note

In this procedure, we show how to downgrade Elemental Live from version 2.25.4 to version 2.23.5. Modify your commands to specify the
version that you are downgrading to.

###### Topics

- [Step A: Get ready to
  downgrade](downgrades-lv-upg-ready-dn.md "downgrades-lv-upg-ready-dn.md")
- [Step B: Copy the AWS Elemental
  installer](downgrades-lv-upg-locate-sw-dn.md "downgrades-lv-upg-locate-sw-dn.md")
- [Step C: Downgrade the node](downgrades-lv-upg-dg-node.md "downgrades-lv-upg-dg-node.md")
