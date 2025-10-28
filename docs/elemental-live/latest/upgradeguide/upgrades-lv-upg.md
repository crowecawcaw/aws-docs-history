# Upgrades in Elemental Live

This section describes how to upgrade to AWS Elemental Live software version to a higher
version.

###### Upgrade rules

The following rules apply when you're upgrading Elemental Live software.

- Your system must be in a working state prior to the upgrade. If it's in a degraded state
  (such as not accepting events or not responding through the web interface), the upgrade
  fails.
- You can upgrade to a version that's a maximum of two major versions above your current
  version. For example, from 2.23.5 to 2.25.4. (The number of minor
  versions between the two major versions is irrelevant.)
- To upgrade over a bigger span, you must perform the upgrade in several steps. For
  example, you might upgrade from version 2.22.5 to 2.23.5, then to
  2.25.4.

###### Important

Plan to upgrade during a maintenance window. All activity on the nodes stops during
upgrade.

###### Note

In this procedure, we show how to upgrade Elemental Live
from version 2.23.5 to version 2.25.4. Modify your commands to specify the
version that you are upgrading to.

###### Topics

- [Step A: Get ready to upgrade](upgrades-lv-upg-single-ver-version.md "upgrades-lv-upg-single-ver-version.md")
- [Step B: Kickstart the operating system
  software](upgrades-lv-step-kickstart.md "upgrades-lv-step-kickstart.md")
- [Step C: Copy the AWS Elemental Live
  installer](upgrades-lv-upg-single-locate-sw.md "upgrades-lv-upg-single-locate-sw.md")
- [Step D: Upgrade the Elemental Live software](upgrades-lv-upg-single-up-cond.md "upgrades-lv-upg-single-up-cond.md")
- [Step E: Restore the database](upgrades-lv-restore-database.md "upgrades-lv-restore-database.md")
- [Step F: Upgrade the license](upgrades-lv-upg-lic.md "upgrades-lv-upg-lic.md")
