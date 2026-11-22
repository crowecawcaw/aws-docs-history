

# Update and upgrade

You’re responsible for patching, updating, and upgrading the VMware Cloud Foundation (VCF) software in your Amazon Elastic VMware Service environment. This includes ESX, vCenter Server, vSAN, NSX, SDDC Manager, and VCF Operations, and any third-party integrations that you add, such as data protection solutions. For the full split of responsibilities, see [Shared responsibility and support](plan-shared-responsibility.md).

You have full control over your VCF software stack, so you can tune it for your applications.

## Who updates what
<a name="evs-lifecycle-who-updates"></a>

The following table lists each part of the environment and who maintains it after deployment. The two mode columns name the owner, either AWS or you.


| Part of the environment | VCF 9.x (Self-deployed) | VCF 5.2.x (EVS-deployed) | Notes | 
| --- | --- | --- | --- | 
| EC2 bare metal hosts and their firmware |  AWS  |  AWS  |  AWS performs scheduled maintenance on the underlying EC2 instances. For more information, see [Host maintenance and retirement events](evs-host-maintenance.md). | 
|  AWS networking that Amazon EVS uses (VPC route tables, security groups, network ACLs, VPC Route Server, internet gateways, NAT gateways, transit gateways) | You | You |  AWS deploys the environment with the network settings that you provide. You maintain them afterward. | 
| Initial VCF installation | You |  AWS  | In Self-deployed environments, you install VCF yourself with the VCF Installer. In EVS-deployed environments, Amazon EVS installs VCF when it creates the environment. | 
| Patches, updates, and upgrades of VCF software (ESX, vCenter Server, vSAN, NSX, SDDC Manager, and other components) | You | You | See [VMware software updates](#vmware-updates). | 
| NSX configuration (segments, distributed firewall rules, load balancers, added Tier-1 gateways) and integrated solutions such as VMware HCX | You | You | In EVS-deployed environments, Amazon EVS creates the first Tier-0 and Tier-1 gateways. See the note after this table. | 
| Health monitoring and remediation of ESX hosts | You | You | For more information, see [Manage hosts](host-management.md). | 
| External storage for diskless hosts, including its capacity, availability, backups, and patching | You | Not available | For more information, see [External storage options for diskless hosts](external-storage-diskless.md). | 

**Note**  
In EVS-deployed environments, Amazon EVS creates and configures a Tier-0 gateway and a Tier-1 gateway when it deploys the environment. Amazon EVS supports a single Tier-0 gateway. Don’t modify these gateways or the NSX Edge node VMs, because changes can affect connectivity.

## Software depots
<a name="evs-lifecycle-depots"></a>

You get VCF software and the Amazon EVS custom vendor add-on from different software depots. Each depot serves a different purpose, and you can’t use one in place of another.


| Depot | Who runs it | What it provides | Where you use it | Access | 
| --- | --- | --- | --- | --- | 
| Broadcom online depot | Broadcom | VCF software for installation, patches, and upgrades. | The VCF Installer when you install VCF 9.x. For Day 2 updates, see the Broadcom documentation for your VCF version. | A Broadcom credential with a valid VCF entitlement, and outbound internet access. For the install steps, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md). | 
| Amazon EVS custom add-on depot |  AWS  | The add-on that ESX hosts need to run on Amazon EC2. | vSphere Lifecycle Manager (vLCM), as a download source for cluster images. | A URL with an access token that you get with the `GetDepotUrl` API action. For the steps, see [Use the Amazon EVS custom add-on depot](addon-depot.md). | 

The Amazon EVS custom add-on depot doesn’t provide VCF software. The Broadcom online depot doesn’t provide the add-on.

## VMware software updates
<a name="vmware-updates"></a>

**Note**  
In EVS-deployed environments, if you update the ESX version after the environment deploys, SDDC Manager can fail during VCF host validation in the commission hosts step. For the steps to fix this issue, see [Troubleshoot hosts](troubleshoot-hosts.md).

For the VCF and ESX versions that Amazon EVS provides, see [Supported VCF versions and instance types](versions-provided.md). When you add a host, you can choose any available ESX version. After you add a host, you change its ESX version only with vSphere Lifecycle Manager.

Review the VCF software version after deployment, and update it as needed. Follow a regular maintenance schedule for updates and patches. You can get VCF updates through the [Broadcom support portal](https://support.broadcom.com/web/ecx).

Some patches, updates, and upgrades can affect the workloads in your environment. Before you change your VCF software, we recommend that you take the following steps:
+ Check software compatibility in the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1) and hardware compatibility with EC2 instances in the [Broadcom Compatibility Guide](https://compatibilityguide.broadcom.com/).
+ Read the VCF lifecycle documentation for your version, so that you understand how the change affects your environment. For VCF 9.x, see the [Broadcom documentation for VCF 9.0](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0.html). For VCF 5.2.x, see [VCF Lifecycle Management Guide](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vmware-cloud-foundation-lifecycle-management.html) and [VCF 5.2.x release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html) in the Broadcom documentation.
+ Test the change in a staging environment before you apply it to production.
+ When you update an ESX cluster image in vLCM, include the add-on from the Amazon EVS custom add-on depot. For the steps, see [Use the Amazon EVS custom add-on depot](addon-depot.md).

### Updates in EVS-deployed environments
<a name="evs-lifecycle-5x-updates"></a>

Amazon EVS deploys a recent bundled version of VCF 5.2.x that might not include individual product updates, known as async patches. After deployment, we recommend that you review and update individual products with the Broadcom Async Patch Tool (AP Tool) or the SDDC Manager lifecycle management automation. You must upgrade NSX outside of SDDC Manager.

vSAN disk prechecks can fail during a cluster upgrade, because Amazon EVS uses vSAN Express Storage Architecture (ESA) and those prechecks don’t apply to vSAN ESA. For more information, see [article 369423](https://knowledge.broadcom.com/external/article/369423/upgrade-prechecks-fails-with-esxi-cluste.html) in the Broadcom knowledge base.

## ESX host lifecycle and maintenance
<a name="esxi-host-updates"></a>

You are responsible for ESX host lifecycle management and maintenance, including monitoring host health and fixing host issues. For more information, see [Manage hosts](host-management.md).

 AWS performs scheduled maintenance on the underlying EC2 bare metal instances for reliability, availability, and performance. For more information, see [Host maintenance and retirement events](evs-host-maintenance.md).

**Topics**