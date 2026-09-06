

# Install Adobe After Effects with Red Giant on Deadline Cloud Windows workers
<a name="examples-host-config-aftereffects"></a>

The [aftereffects\_redgiant](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects/aftereffects_redgiant) host configuration script on the GitHub website installs Adobe After Effects 2025 with Red Giant and Universe plugins on Windows GPU service-managed fleet workers. The script fetches installers from Amazon S3 and runs each one in silent mode on each worker launch.

**Important**  
This script can add about 15-20 minutes to worker launch time because of the software installation. The duration decreases as you vertically scale your instance size up. For example, a `g6.xlarge` with 4 vCPUs and 16 GiB of memory adds about 20 minutes, while a `g6.4xlarge` with 16 vCPUs and 64 GiB of memory adds about 15 minutes. To reduce the impact, keep a warm worker alive during peak usage hours, or use one fleet for After Effects renders through conda and a separate fleet for After Effects with Red Giant through this host configuration script.

The script uses a persistent volume automatically when your fleet has one configured. The first worker installs the software once to the persistent volume; subsequent worker boots restore it in seconds instead of reinstalling. If no persistent volume is attached, the script performs a normal install. No separate script or flag is required. Configure a persistent volume if your fleets scale up and down frequently. For more information about how the script uses persistent volumes, see [Persistent Volumes (Automatic)](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/host_configuration_scripts/aftereffects/aftereffects_redgiant#persistent-volumes-automatic) in the `aftereffects_redgiant` README on the GitHub website. For more information about configuring persistent volumes on a fleet, see [Persistent storage for service-managed fleets](smf-persistent-storage-dev.md).

To use this script, you need:
+ An enterprise Adobe account with Admin access to download the After Effects 2025 installer package from the Adobe Admin Console.
+ A Maxon account to download the Red Giant and Universe installers.
+ An Amazon S3 bucket where you upload the installers, and IAM permissions for the fleet to read them.
+ A Windows GPU service-managed fleet with the latest GPU driver.

For an After Effects job bundle that uses this fleet configuration, see [Render Adobe After Effects projects on Deadline Cloud](examples-jb-aftereffects.md).