

# Virtual machine backups
<a name="vm-backups"></a>

AWS Backup supports centralized and automated data protection for on-premises VMware virtual machines (VMs) along with VMs in the VMware Cloud™ (VMC) on AWS and VMware Cloud™ (VMC) on AWS Outposts. You can back up from your on-premises and VMC virtual machines to AWS Backup. Then, you can restore from AWS Backup to on-premises VMs, VMs in the VMC, or the VMC on AWS Outposts.

AWS Backup also provides you with fully-managed, AWS-native VM backup management capabilities, such as VM discovery, backup scheduling, retention management, a low-cost storage tier, cross-Region and cross-account copy, support for AWS Backup Vault Lock and AWS Backup Audit Manager, encryption that is independent from source data, and backup access policies. For a full list of capabilities and details, see the [Feature availability by resource](backup-feature-availability.md#features-by-resource) table.

You can use AWS Backup to protect your virtual machines on [VMware Cloud™ on AWS Outposts](https://aws.amazon.com/vmware/aws-services/). AWS Backup stores your VM backups in the AWS Region to which your VMware Cloud™ on AWS Outposts is connected. You can use AWS Backup to protect your VMware Cloud™ on AWS Backup VMs when you’re using VMware Cloud™ on AWS Outposts to meet your low-latency and local data-processing needs for your application data. Based on your data residency requirements, you may choose AWS Backup to store backups of your application data in the parent AWS Region to which your AWS Outposts is connected.

## Supported VMs
<a name="supported-vms"></a>

AWS Backup can back up and restore virtual machines managed by a VMware vCenter.

**Currently supported:**
+ vSphere 8, 7.0, and 6.7
+ Virtual disk sizes that are multiples of 1 KiB
+ NFS, VMFS, and VSAN datastores on premises and in VMC on AWS
+ SCSI Hot-Add and Network Block Device Secure Sockets Layer (NBDSSL) transport modes for copying data from source VMs to AWS for on-premises VMware
+ Hot-Add mode to protect VMs on VMware Cloud on AWS

**Not currently supported:**
+ RDM (raw disk mapping) disks or NVMe controllers and their disks
+ Independent-persistent and independent-non persistent disk modes

## Backup consistency
<a name="backup-consistency"></a>

AWS Backup, by default, captures application-consistent backups of VMs using the VMware Tools quiescence setting on the VM. Your backups are application consistent if your applications are compatible with VMware Tools. If the quiescence capability is not available, AWS Backup captures crash-consistent backups. Validate that your backups meet your organization’s needs by testing your restores.

## Backup gateway
<a name="backup-gateway"></a>

Backup gateway is downloadable AWS Backup software that you deploy to your VMware infrastructure to connect your VMware VMs to AWS Backup. The gateway connects to your VM management server to discover VMs, discovers your VMs, encrypts data, and efficiently transfers data to AWS Backup. The following diagram illustrates how Backup gateway connects to your VMs:

![A backup gateway is an OVF template the connects your VMware environment to AWS Backup.](http://docs.aws.amazon.com/aws-backup/latest/devguide/images/Horizon.png)


To download the Backup gateway software, follow the procedure for [Working with gateways](working-with-gateways.md).

### Download VM software
<a name="download-vm-software"></a>

Backup gateway is distributed as an OVF (Open Virtualization Format) template that you deploy to your VMware infrastructure. The gateway software connects your VMware VMs to AWS Backup by discovering VMs, encrypting data, and efficiently transferring data to AWS Backup.

To obtain the OVF template, use the AWS Backup console:

1. Sign in to the AWS Management Console and open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the left navigation pane, under **External resources**, choose **Gateways**.

1. Choose **Create gateway**.

1. In the **Set up gateway** section, download the OVF template and deploy it to your VMware environment.

For information on VPC (Virtual Private Cloud) endpoints, see [AWS Backup and AWS PrivateLink connectivity](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-network.html#backup-privatelink).

Backup gateway comes with its own API which is separately maintained from the AWS Backup API. To view a list of Backup gateway API actions, see [Backup gateway actions](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Operations_AWS_Backup_Gateway.html). To view a list of Backup gateway API data types, see [Backup gateway data types](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_Types_AWS_Backup_Gateway.html).

## Endpoints
<a name="backup-gateway-endpoints"></a>

Existing users who currently use a public endpoint and who wish to switch to a VPC (Virtual Private Cloud) endpoint can [ create a new gateway with a VPC endpoint](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-gateways.html#create-gateway) using [AWS PrivateLink](https://docs.aws.amazon.com/aws-backup/latest/devguide/backup-network.html#backup-privatelink), associate the existing hypervisor to the gateway, and then [ delete the gateway](https://docs.aws.amazon.com/aws-backup/latest/devguide/working-with-gateways.html#edit-gateway) containing the public endpoint.