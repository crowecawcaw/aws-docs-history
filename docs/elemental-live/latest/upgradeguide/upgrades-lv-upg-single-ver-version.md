

# Step A: Get ready to upgrade
<a name="upgrades-lv-upg-single-ver-version"></a>

The following steps prepare you for upgrading. Perform these steps to ensure that you don't lose any data during the upgrade process.

## Check essential notes
<a name="ver-ess-notes"></a>

To identify changes in behavior with the upgrade, see the essential notes in the [ current Release Notes](https://docs.aws.amazon.com/elemental-live/). 

## Verify the worker type
<a name="ver-version-node"></a>

The software installer that you use for the nodes varies depending on whether you have GPU-accelerated software type or CPU-only. To determine the type of software, look at any web interface screen of the worker node. The top shows one or two icons as follows:
+ CPU and GPU icons: the software is *GPU-accelerated*.
+ CPU icon only: the software is *CPU-only*.