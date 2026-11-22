

# Differences between deployment modes

Amazon Elastic VMware Service (Amazon EVS) offers two deployment modes for VMware Cloud Foundation (VCF):
+ In **Self-deployed** mode, Amazon EVS creates the VLAN subnets when you create the environment. You add the hosts and install VCF yourself. You can deploy VCF 5.x or VCF 9.x in this mode.
+ In **EVS-deployed** mode, Amazon EVS creates the VLAN subnets and four hosts, and installs VCF 5.2.x for you. EVS-deployed mode doesn’t support VCF 9.x deployments. To automate a VCF 9.x deployment, use the [EVS Deployment Orchestrator (EDO)](https://github.com/aws/solutions-for-amazon-evs) in the Solutions for Amazon EVS repository on GitHub.

Choose Self-deployed mode to install VCF yourself, to deploy VCF 9.x, or to use diskless hosts. Choose EVS-deployed mode to have Amazon EVS install VCF 5.2.x for you.

You choose the mode when you create the environment. In the console, the version list includes a **Self-deployed** option. In the API, the values are `SELF_DEPLOYED`, `VCF-5.2.2`, and `VCF-5.2.1`.

## Comparison table
<a name="deployment-mode-comparison"></a>

Each row covers one topic. The second and third columns give the behavior in each mode. The value `Not available` means that the mode doesn’t support the item.


| Topic | Self-deployed | EVS-deployed | 
| --- | --- | --- | 
| Who installs VCF | You install VCF yourself. For VCF 9.x, you can use the VCF Installer, or the EVS Deployment Orchestrator (EDO) from the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub. For instructions, see [Deploy in Self-deployed mode](getting-started-self-deployed.md). | Amazon EVS installs VCF during environment creation. For instructions, see [Deploy in EVS-deployed mode](evs-deployed-overview.md). | 
| VCF versions and API value | VCF 5.x or VCF 9.x. Amazon EVS provides VCF 9.0 and VCF 9.1 as the VCF 9.x versions. The API value is `SELF_DEPLOYED`. | VCF 5.2.2 (`VCF-5.2.2`) and VCF 5.2.1 (`VCF-5.2.1`). VCF 5.2.1 is restricted, and you request access through AWS Support. | 
| ESX version | You can choose an ESX version when you add a host. If you don’t choose one, Amazon EVS uses the default that `get-versions` reports as `defaultEsxVersion`. | Each VCF release has a default ESX version. For the values, see [Supported VCF versions and instance types](versions-provided.md). | 
| VCF license keys | You don’t provide license keys when you create the environment. You add them in your VCF management appliance after you install VCF. For more information, see [VCF licensing](vcf-license-mgmt.md). | You provide a VCF solution key and a vSAN license key when you create the environment. You must keep valid keys in SDDC Manager. | 
| Hosts at environment creation | None. Environment creation provisions the VLAN subnets only. You add hosts after the environment is created. | Four hosts. Amazon EVS environments in this mode require four hosts for initial deployment. | 
| Route server peers | You don’t select peers when you create the environment. You configure BGP peering between the NSX Tier-0 gateway and Amazon VPC Route Server after you install VCF. | You choose two route server peer IDs when you create the environment. The route server, its endpoints, and its peers must exist before you create the environment. | 
| NSX setup | You configure the NSX Edge cluster, the Tier-0 gateway, and routing to your VPC after VCF bringup. For instructions, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md). | Amazon EVS deploys an Active/Standby NSX Edge cluster with two NSX Edge nodes and configures the NSX routing and uplinks for you. | 
| Management connector | VCF Operations connector (`OPERATIONS_MANAGER`). You can also create a vCenter connector (`VCENTER`). | SDDC Manager connector (`SDDC_MANAGER`). You can also create a vCenter connector (`VCENTER`). | 
| Principal storage | vSAN on hosts with local NVMe instance store volumes, or external storage on diskless hosts. For the choice, see [Choose storage](plan-storage.md). | vSAN on hosts with local NVMe instance store volumes. | 
| Diskless hosts (for example, r7i instance types) | Available with VCF 9.x. For instructions, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md). | Not available | 
| Supplemental storage with AWS services | Amazon FSx for NetApp ONTAP as an NFS, iSCSI, or NVMe/TCP datastore. For more information, see [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md). | Amazon FSx for NetApp ONTAP as an NFS, iSCSI, or NVMe/TCP datastore. For more information, see [Use Amazon FSx for NetApp ONTAP with Amazon EVS](fsx-ontap.md). | 
| Tools in the Solutions for Amazon EVS repository |  [Deploy with the EVS Deployment Orchestrator](deploy-with-edo.md) (EDO) in the [Solutions for Amazon EVS GitHub repository](https://github.com/aws/solutions-for-amazon-evs). | Not available | 
| Who installs, upgrades, and patches VCF | You install, upgrade, and patch the VCF stack. | Amazon EVS does the initial VCF installation. You upgrade and patch the VCF stack. | 
| Support |  AWS Support covers Amazon EVS and its associated infrastructure services, including VCF. For more information, see [Get help from AWS Support and Broadcom](get-help.md). |  AWS Support covers Amazon EVS and its associated infrastructure services, including VCF. For more information, see [Get help from AWS Support and Broadcom](get-help.md). | 

In both modes, AWS manages the AWS resources that Amazon EVS provisions, the bare metal hosts and their firmware. For the full split of responsibilities, see [Shared responsibility and support](plan-shared-responsibility.md).

## Related topics
<a name="deployment-mode-related"></a>

For more information about the modes, see the following topics.
+ For the VCF and ESX versions that each mode supports, see [Supported VCF versions and instance types](versions-provided.md).
+ For the VCF features that you can use in each mode, see [VCF feature support on Amazon EVS](vcf-feature-support.md).