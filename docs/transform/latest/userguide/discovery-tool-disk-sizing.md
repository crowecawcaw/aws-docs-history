

# Disk sizing and management
<a name="discovery-tool-disk-sizing"></a>

The discovery tool stores its data in an internal database on the root volume. The database grows with the number of servers in scope. Network collection increases disk usage further, especially when private IP address collection is enabled. The discovery tool prunes data older than 30 days, so disk usage plateaus after the first month.

The following table shows the recommended disk size for each environment size, based on how many servers you monitor and whether network collection is enabled.


| Environment | Servers | Network collection | Recommended volume | 
| --- | --- | --- | --- | 
| Any size | Any | Disabled | 35 GB (default) | 
| Small | Fewer than 500 | Enabled | 50 GB | 
| Medium | 500–2,000 | Enabled, no private addresses | 100 GB | 
| Medium | 500–2,000 | Enabled, private addresses on | 150–200 GB | 
| Large | 2,000 or more | Enabled | 200 GB | 

When in doubt, provision more disk than you expect to need. Resizing a running discovery tool requires downtime.

Choose the procedure that matches how you deployed the discovery tool. On the OVA and VHD appliances, cloud-init automatically expands the root partition on the first boot after you increase the disk. You do not need to partition the disk manually. On a Linux installer deployment, you manage the host yourself. You might also need to extend the partition and file system.

**To increase the disk on a VMware OVA deployment**

1. Deploy the Open Virtualization Format (OVF) template. Before you power on the virtual machine, open the vSphere Client, right-click the virtual machine, and choose **Edit Settings**.

1. Increase **Hard disk 1** to the size you want, and then save. The OVF deployment wizard does not expose the disk size, so you set it here.

1. Power on the virtual machine. If the virtual machine is already running, power it off first, increase **Hard disk 1** in **Edit Settings**, and then power it on.

**To increase the disk on a Hyper-V VHD deployment**

1. Before you start the virtual machine, in Hyper-V Manager, open the virtual machine **Settings**.

1. Select **Hard Drive**, choose **Edit**, choose **Expand**, and set the new size. The disk size cannot be set during import, so you set it here.

1. Start the virtual machine. If the virtual machine is already running, shut it down first, expand the hard drive in **Settings**, and then start it.

**To size the disk for a Linux installer deployment**

1. Provision a larger root disk on the host before you run the installer. The installer does not enforce a disk size.

1. If you increase the disk after you install, extend the partition and file system on the host by using the tools for your distribution. The discovery tool uses whatever space is available on the file system that holds its data directory.

To check current disk usage on the discovery tool virtual machine, run `df -h /`.

If the discovery tool is already out of disk space, see [Internal database disk space management in the AWS Transform discovery tool](https://repost.aws/articles/ARERZHOS-URGeds3VImdjzsg/internal-database-disk-space-management-in-the-aws-transform-discovery-tool) on the AWS re:Post website.