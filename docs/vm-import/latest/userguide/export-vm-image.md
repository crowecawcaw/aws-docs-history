# Export your VM from its virtualization environment

After you have prepared your VM for export, you can export it from your virtualization
environment. When importing a VM as an image, you can import disks in the following
formats: Open Virtualization Archive (OVA), Virtual Machine Disk (VMDK), Virtual Hard
Disk (VHD/VHDX), and raw. With some virtualization environments, you would export to
Open Virtualization Format (OVF), which typically includes one or more VMDK, VHD, or
VHDX files, and then package the files into an OVA file.

For more information, see the documentation for your virtualization environment.
For example:

- VMware — Search for
  "Export an OVF Template" on the [VMware Docs](https://docs.vmware.com/ "https://docs.vmware.com/") site. Follow the instructions to export an OVA.
- Citrix — [Importing and Exporting VMs](https://docs.citrix.com/en-us/xencenter/current-release/vms-exportimport.html "https://docs.citrix.com/en-us/xencenter/current-release/vms-exportimport.html") on the Citrix website.
- Microsoft Hyper-V — [Overview of
  exporting and importing a virtual machine](https://technet.microsoft.com/en-us/library/hh831535.aspx "https://technet.microsoft.com/en-us/library/hh831535.aspx") on the Microsoft
  website.
- Microsoft Azure — [Download a Windows VHD from Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/download-vhd "https://docs.microsoft.com/en-us/azure/virtual-machines/windows/download-vhd") or [Download a Linux VHD from Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/download-vhd "https://docs.microsoft.com/en-us/azure/virtual-machines/linux/download-vhd") on the Microsoft website.
  From the Azure Portal, choose the VM to migrate, and then choose
  **Disks**. Select each disk (either OS or data) and
  choose **Create Snapshot**. On the completed snapshot
  resource, choose **Export**. This creates a URL that
  you can use to download the virtual image.
