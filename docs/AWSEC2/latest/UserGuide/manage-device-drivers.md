# Manage device drivers for your EC2 instance

Device drivers are software components that communicate with the virtualized hardware for
your Amazon EC2 instance. To prevent system errors, performance issues, and other unexpected
behavior, it's important to keep your drivers up-to-date. That's especially true for drivers
that can have a strong impact on system performance depending on your usage, such as networking,
graphics, and storage device drivers. New driver releases can include defect fixes or introduce
expanded functionality that you might want to take advantage of for instances that are currently
running.

## Network drivers

Linux distributions can incorporate networking features like Elastic Network Adapter (ENA)
or Elastic Fabric Adapter (EFA) within the kernel. However, the timing may vary for implementation
of kernel driver features within the different distributions.

ENA and EFA Linux kernel drivers are available from the Amazon Drivers GitHub repository.
For more information and links to the available drivers, see [Amazon Drivers](https://github.com/amzn/amzn-drivers/ "https://github.com/amzn/amzn-drivers/") on GitHub.

For more information about ENA drivers, see [Enable enhanced networking with ENA on your EC2 instances](enhanced-networking-ena.md "enhanced-networking-ena.md"). For more information about EFA
drivers, see **Getting started** topics in the
[Elastic Fabric Adapter for AI/ML and HPC workloads on Amazon EC2](efa.md "efa.md") section of this guide.

To install or update networking drivers on Windows instances, see the following topics:

- [Install the ENA driver on Windows](ena-adapter-driver-install-upgrade-win.md "ena-adapter-driver-install-upgrade-win.md")
- [Install the latest AWS PV drivers](xen-drivers-overview.md#aws-pv-download "xen-drivers-overview.md#aws-pv-download")

For more information, see [Paravirtual drivers for Windows instances](xen-drivers-overview.md "xen-drivers-overview.md").

###### Note

EFA is not supported on Windows instances.

## Graphics drivers

To install or update graphics drivers, see the following topics:

- [AMD drivers for your EC2 instance](install-amd-driver.md "install-amd-driver.md")
- [NVIDIA drivers for your Amazon EC2 instance](install-nvidia-driver.md "install-nvidia-driver.md")

## Storage device drivers

To install or update storage drivers, see the following topics:

- For Linux instances, see [Install
  or upgrade the NVMe driver](../../../ebs/latest/userguide/nvme-ebs-volumes.md#install-nvme-driver "../../../ebs/latest/userguide/nvme-ebs-volumes.md#install-nvme-driver") in the
  _Amazon EBS User Guide_.
- For Windows instances, see [AWS NVMe drivers](aws-nvme-drivers.md "aws-nvme-drivers.md").
