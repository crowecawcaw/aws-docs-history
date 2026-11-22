

# Step 4a (local storage): Prepare the VCF Installer

After your hosts are in the `CREATED` state and your DNS records resolve, you install VMware Cloud Foundation (VCF) with the VCF Installer. This step prepares an ESX host and a temporary datastore for the VCF Installer appliance, deploys the appliance, and downloads the VCF software. In [Step 4b (local storage): Run VCF bringup](sd-install-bringup.md), you run bringup.

Use these steps for hosts with local storage that use vSAN. For diskless hosts, the datastore preparation, bringup storage, and reclaim steps differ. For instructions, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

The installation itself follows the standard Broadcom VCF process. For the installation guidance for your target VCF version, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html). In the VCF Installer, you also provide some settings that are specific to Amazon Elastic VMware Service.

**Tip**  
To run this installation end to end, including the Amazon EVS-specific settings, you can use the EVS Deployment Orchestrator (EDO), a tool in the [Solutions for Amazon EVS repository](https://github.com/aws/solutions-for-amazon-evs). For more information, see [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md).

Before you begin, make sure that you have the following.
+ A Broadcom account with a valid VCF entitlement.
+ The VCF Installer OVA file for your target VCF version, downloaded from the [Broadcom Support Portal](https://support.broadcom.com/).
+ A computer with a web browser that can reach the private IP addresses of your VPC, to open the VMware Host Client and the VCF Installer.

## Amazon EVS network settings for VCF
<a name="sd-install-network"></a>

To find the VLAN ID of each network function, see the VLAN IDs step in [Prepare the VLAN subnets for VCF](self-deployed-create-env.md#self-deployed-create-env-after). For how to apply the VLAN IDs on the hosts, see [Host networking settings](self-deployed-add-hosts.md#self-deployed-host-networking).

The following table lists the MTU and use of each network function.


| Network function | MTU | Used for | 
| --- | --- | --- | 
| Host management (`vmkManagement`) | 1500 | ESX host management | 
| VM management (`vmManagement`) | 1500 | VCF management appliances (vCenter Server, NSX Manager, SDDC Manager, and VCF Operations) | 
| vMotion | 8500 | vMotion traffic | 
| vSAN | 8500 | vSAN storage traffic | 
| Host overlay (`vTep`) | 8500 | Host overlay (Geneve) tunnel endpoints | 
| Edge overlay (`edgeVTep`) | 8500 | NSX Edge overlay tunnel endpoints | 
| NSX uplink (`nsxUplink`) | 1500 | Tier-0 gateway north-south uplink | 

**Important**  
Configure jumbo frames (MTU 8500) on the vMotion, vSAN, and overlay (TEP) networks. The management and uplink networks use MTU 1500. The MTU must be consistent across the network path, or vSAN and overlay traffic fails.

## Prepare the VCF Installer host
<a name="sd-install-hosts"></a>

On the ESX host where you run the VCF Installer appliance, set the `VM Network` port group to the Amazon EVS-assigned VM management VLAN ID. This setting lets the VCF Installer appliance communicate on the VM management VLAN.

1. Find the VLAN ID of the VM management (`vmManagement`) network. For instructions, see the VLAN IDs step in [Prepare the VLAN subnets for VCF](self-deployed-create-env.md#self-deployed-create-env-after).

1. Sign in to the VMware Host Client of the host at `https://<host-fqdn>` as `root`, with the root password from AWS Secrets Manager.

1. On the host, set the `VM Network` port group VLAN ID to the VM management VLAN ID. Leave the host management port group `Management` untagged with VLAN ID `0`.

## Prepare a temporary datastore for the VCF Installer
<a name="sd-install-datastore"></a>

The VCF Installer appliance needs a temporary datastore, because Amazon EVS hosts have no local VMFS datastores and the vSAN datastore doesn’t exist until bringup completes. Use the host that you prepared in the previous section.

1. In the Amazon EC2 console, create an encrypted General Purpose SSD (`gp3`) Amazon EBS volume in the same Availability Zone as the host. Size it to hold the VCF Installer appliance and the VCF installation bundles, at least 256 GB.

1. Attach the EBS volume to the ESX host. For instructions, see [Attach an Amazon EBS volume to an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html) in the *Amazon EBS User Guide*.

1. Using the VMware Host Client or the vSphere APIs, create a local VMFS datastore on the attached EBS volume.

The EBS volume accrues storage charges until you delete it in [Reclaim the temporary datastore](sd-install-bringup.md#sd-install-reclaim).

## Deploy the VCF Installer
<a name="sd-install-deploy"></a>

To deploy the VCF Installer, do the following.

1. Deploy the VCF Installer OVA onto the local VMFS datastore.

1. Attach the appliance to the `VM Network` port group.

1. Set its management IP address to the SDDC Manager address from your DNS plan, and set the appliance passwords and NTP servers. For the values to use, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

The VCF Installer appliance becomes SDDC Manager during bringup, so it uses the SDDC Manager address. On VCF 9.0 and 9.1, VCF Operations is a separate appliance.

## Connect the software depot
<a name="sd-install-depot"></a>

The VCF Installer downloads the VCF software from a software depot. Connect the VCF Installer to the Broadcom online depot, and then download the install binaries for your VCF version.

 **Broadcom online depot** 

1. Make sure that your Broadcom account has a valid VCF entitlement for the VCF version that you plan to deploy.

1. In the VCF Installer, open the depot settings, and configure the Broadcom online depot with your Broadcom credential. The credential depends on your VCF version.
   + For VCF 9.0, generate a Broadcom download token from the [Broadcom Support Portal](https://support.broadcom.com/), and enter the token in the VCF Installer.
   + For VCF 9.1, the VCF Installer authenticates to the Broadcom online depot with an activation code. Generate a software depot ID in the VCF Installer, and register it in the VCF Business Services console. Enter the activation code that the console returns in the VCF Installer, and then review and accept the certificate thumbprint. For more information, see [Broadcom knowledge base article 443647](https://knowledge.broadcom.com/external/article/443647).

1. Select the VCF version that you want, and download the install binaries. Downloading the binaries pulls that version of the VCF software into the local depot of the VCF Installer.

1. Wait until every download shows success before you validate the deployment specification.

**Note**  
Connecting to the Broadcom online depot and downloading software requires outbound internet access from the VCF Installer. The NAT gateway in your network foundation provides this access. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md).

If the depot connection succeeds but downloads fail with a 403 error, check that your Broadcom entitlement covers the VCF version that you selected. For more information, see [Broadcom knowledge base article 440278](https://knowledge.broadcom.com/external/article/440278).

The Amazon EVS custom add-on depot is a different depot. It provides the Amazon EVS add-on for ESX cluster images, and you don’t use it in this step. For more information, see [Use the Amazon EVS custom add-on depot](addon-depot.md).

When every download shows success, you have prepared the VCF Installer and downloaded the VCF software.

Next step: [Step 4b (local storage): Run VCF bringup](sd-install-bringup.md).