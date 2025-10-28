This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Downgrades in AWS Elemental Statmux

This section describes how to downgrade from AWS Elemental Statmux version
2.20.x.

###### Downgrade rules

The following rules apply when you're downgrading AWS Elemental Statmux software.

- Your system must be in a working state prior to the downgrade. If it's in a
  degraded state (such as not creating MPTSs or not responding through the web
  interface), the downgrade does not work.
- You can downgrade to a version that's a maximum of two major versions below your
  current version, such as from 2.20.x to 2.17.x. The number of
  patches between the two versions is irrelevant. We do recommend, however, that you always use the
  latest patch release of the major version that you're downgrading to, for example, 2.17.6.
  To downgrade over a larger span, you must
  perform several downgrades, such as from 2.20.3 to 2.17.4,
  then 2.15.3.

###### Important

Plan to downgrade during a maintenance window. All activity on the nodes stops during downgrade.

###### Topics

- [Step A: Get Ready](downgrades-sm-upg-ready-dn.md "downgrades-sm-upg-ready-dn.md")
- [Step B: Copy the AWS Elemental Installer](downgrades-sm-upg-locate-sw-dn.md "downgrades-sm-upg-locate-sw-dn.md")
- [Step C: Downgrade the Node](downgrades-sm-upg-dg-node.md "downgrades-sm-upg-dg-node.md")
