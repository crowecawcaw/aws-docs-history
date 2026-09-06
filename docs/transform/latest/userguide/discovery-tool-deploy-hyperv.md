# Deploy on Hyper-V

## Hyper-V virtual machine specifications

- **Operating System** – Amazon Linux 2023
- **RAM** – We recommend allocating at least 16 GB
- **CPU** – We recommend allocating at least 4 cores
- **Disks** – 35 GB minimum (included in the VHD). For larger inventories, see [Disk sizing and management](discovery-tool-disk-sizing.md "discovery-tool-disk-sizing.md").
- **Hyper-V requirements** – See [Hyper-V host requirements for running AL2023 on Hyper-V](../../../linux/al2023/ug/hyperv-supported-configurations.md#hyperv-host-requirements "../../../linux/al2023/ug/hyperv-supported-configurations.md#hyperv-host-requirements")

## Deploy the Hyper-V VHD

1. Download the VHD file from this URL: [https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.vhd](https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.vhd "https://s3.us-east-1.amazonaws.com/atx.discovery.collector.bundle/releases/latest/AWS-Transform-discovery-tool.vhd")
2. Copy the VHD file to the Windows Server machine that has the Hyper-V role enabled.
3. Open Hyper-V Manager.
4. Choose **New**, and then choose **Virtual Machine**.
5. Complete the setup wizard. On the **Specify Generation** page, select **Generation 1**. Generation 2 virtual machines do not support the VHD format. On the **Assign Memory** page, allocate at least 16384 MB. On the **Connect Virtual Hard Disk** page, choose **Use an existing virtual hard disk** and select the VHD file that you copied.
6. Start the VM. After a few minutes, check the **Networking** tab of the VM in Hyper-V Manager to find the IP address, or connect to the VM console and run `ip addr`. You use this IP address to connect to the discovery tool.
