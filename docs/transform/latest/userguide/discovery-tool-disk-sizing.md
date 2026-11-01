

# Disk and memory sizing
<a name="discovery-tool-disk-sizing"></a>

The discovery tool stores its data in an internal database on the root volume. The database grows with the number of servers in scope. Network collection increases disk usage further, especially when private IP address collection is enabled. The discovery tool prunes data older than 30 days, so disk usage plateaus after the first month. This page also covers virtual machine (VM) memory and the discovery tool service memory limit.

The following table shows the recommended disk size for each environment size, based on how many servers you monitor and whether network collection is enabled.


| Environment | Servers | Network collection | Recommended volume | 
| --- | --- | --- | --- | 
| Any size | Any | Disabled | 100 GB (the appliance default) | 
| Small | Fewer than 500 | Enabled | 100 GB (the appliance default) | 
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

The discovery tool service is limited to 14 GB of memory by default, regardless of how much memory the VM has. The recommended 16 GB VM leaves 2 GB for the operating system. If you monitor a large environment, increase the VM's memory and then raise the service memory limit. The discovery tool doesn't start an export that needs more memory than the service can use. For more information, see [Incomplete or failed export](discovery-tool-troubleshooting.md#discovery-tool-export-troubleshooting).

**To increase memory on a VMware OVA deployment**

1. Power off the virtual machine. In the vSphere Client, right-click the virtual machine, and choose **Edit Settings**.

1. Increase **Memory** to the size you want, and then save. If the virtual machine is in a resource pool with a memory limit, ask your vSphere administrator to raise the pool limit as well.

1. Power on the virtual machine.

**To increase memory on a Hyper-V VHD deployment**

1. Shut down the virtual machine. In Hyper-V Manager, open the virtual machine **Settings**.

1. Choose **Memory**, clear **Enable Dynamic Memory**, and set **Startup RAM** to the size you want. Use a fixed amount of memory. With Dynamic Memory, the amount of memory the VM has changes while it runs, so the total that you check in the next procedure, and the service memory limit that you base on it, might not match the memory that is available later.

1. In the **Settings** dialog box, choose **OK**, and then start the virtual machine.

**To raise the service memory limit**

1. On the discovery tool VM, check how much memory the operating system has by running `free -g`. Choose a new limit that is at least 2 GB less than the total, to leave memory for the operating system. For example, use `28G` on a VM with 32 GB of memory. systemd uses `G` as its unit for gigabytes, with no space. If a VMware memory limit or a resource pool limit applies to the VM, the operating system can use less memory than `free -g` reports. In that case, base the new limit on the hypervisor limit instead.

1. On the discovery tool VM, run the following commands. Replace {{28G}} with the limit that you chose.

   ```
   sudo mkdir -p /etc/systemd/system/discovery-tool.service.d
   printf '[Service]\nMemoryMax=28G\nMemoryLimit=28G\n' | sudo tee /etc/systemd/system/discovery-tool.service.d/memory.conf
   sudo systemctl daemon-reload
   sudo systemctl restart discovery-tool
   ```

1. Verify the new limit.

   ```
   systemctl show discovery-tool -p MemoryMax -p MemoryLimit
   ```

   The output shows the new limit in bytes, for example `MemoryMax=30064771072` for `28G`. If the service does not start, check its status with `systemctl status discovery-tool` and its log with `journalctl -u discovery-tool`.

The service memory limit persists across restarts and in-place updates. On a Linux installer deployment, you manage the host's memory yourself; raise the service memory limit the same way.