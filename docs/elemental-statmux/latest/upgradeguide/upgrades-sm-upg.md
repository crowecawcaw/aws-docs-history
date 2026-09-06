

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Upgrades in AWS Elemental Statmux
<a name="upgrades-sm-upg"></a>

This section describes how to upgrade to AWS Elemental Statmux version 2.20.x.

**Upgrade rules**  
The following rules apply when you're upgrading AWS Elemental Statmux software.
+ Your system must be in a working state prior to the upgrade. If it's in a degraded state (such as not accepting MPTSs or not responding through the web interface), the upgrade fails.
+ You can upgrade to a version that's a maximum of two major versions above your current version, such as from 2.17.x to 2.20.x. The number of patches between the two versions is irrelevant. To upgrade over a bigger span, you must perform several upgrades, such as from 2.15.2 to 2.17.4, then to 2.20.0.

**Important**  
Plan to upgrade during a maintenance window. All activity on the nodes stops during upgrade.

**Topics**
+ [Step A: Get Ready](upgrades-sm-upg-single-ver-version.md)
+ [Step B: Copy the AWS Elemental Statmux Installer](upgrades-sm-upg-single-locate-sw.md)
+ [Step D: Upgrade the Node](upgrades-sm-upg-single-up-cond.md)