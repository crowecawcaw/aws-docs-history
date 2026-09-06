

# Deploy on VMware
<a name="discovery-tool-deploy-vmware"></a>

## VMware virtual machine specifications
<a name="discovery-tool-vmware-vm-specs"></a>
+ **Operating System** – Amazon Linux 2023
+ **RAM** – 16 GB
+ **CPU** – 4 cores
+ **Disks** – 35 GB minimum (default). For larger inventories, see [Disk sizing and management](discovery-tool-disk-sizing.md).
+ **VMware requirements** – See [VMware host requirements for running AL2023 on VMware](https://docs.aws.amazon.com/linux/al2023/ug/vmware-supported-configurations.html#vmware-host-requirements)

## Deploy the VMware OVA
<a name="discovery-tool-vmware-deploy-steps"></a>

1. Download the OVA file from this URL: [https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.ova](https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.ova)

1. Sign in to vCenter as a VMware administrator.

1. Use one of these ways to install the OVA file:

   1. **Use the UI:** Choose **File**, choose **Deploy OVF Template**, select the discovery tool OVA file you downloaded in step 1, and then complete the wizard. Ensure the proxy settings in the server management dashboard are configured correctly.

   1. **Use the command line:** To install the discovery tool OVA file from the command line, download and use the VMware Open Virtualization Format Tool (ovftool). To download ovftool, select a release from the [OVF Tool Documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/ovf-tool-user-s-guide/using-ovf-tool-commands/command-line-options.html) page. This is an example of using the ovftool command line tool to install the discovery tool OVA file.

      ```
      ovftool --acceptAllEulas --name='discovery tool' --datastore=datastore1 -dm=thin AWS-Transform-discovery-tool.ova 'vi://username:password@vcenterurl/Datacenter/host/esxi/'
      ```

      Descriptions of the replaceable values in the example:
      + The name is the name that you want to use for your discovery tool VM.
      + The datastore is the name of the datastore in your vCenter.
      + The OVA file name is the name of the downloaded discovery tool OVA file.
      + The username/password are your vCenter credentials.
      + The vcenterurl is the URL of your vCenter.
      + The vi path is the path to your VMware ESXi host.

1. Locate the deployed discovery tool in your vCenter. Right-click the VM, and then choose **Power**, **Power On**.

1. After a few minutes, the IP address of the discovery tool displays in vCenter. You use this IP address to connect to the discovery tool.