

# Step 4a (diskless): Prepare diskless hosts and the VCF Installer

Diskless hosts have no local storage for VMware Cloud Foundation (VCF). They boot from an Amazon EBS volume, and vSAN and local VMFS datastores aren’t available, so you provide external storage for the management domain. For the instance types that are diskless, see [Supported VCF versions and instance types](versions-provided.md). In this step, you create the external storage, prepare the first host, deploy the VCF Installer appliance, download the VCF software, and add the remaining hosts. In [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md), you create the deployment specification and deploy VCF.

The example on this page deploys a VCF 9.x management domain on two r7i.metal-24xl hosts. It uses Amazon FSx for OpenZFS as the only storage, with a Network File System (NFS) v3 principal datastore and no vSAN. The VCF Installer accepts a management domain with two hosts and an NFS principal datastore.

**Note**  
You can use Amazon FSx for NetApp ONTAP or Everpure Cloud Dedicated instead. Follow the same sequence, and replace the storage creation and datastore mount steps with the procedures for your storage. For more information, see [External storage options for diskless hosts](external-storage-diskless.md).

## Before you begin
<a name="getting-started-diskless-prereqs"></a>

Make sure that you meet the following prerequisites.
+ You created an environment with `SELF_DEPLOYED` as the VCF version. For more information, see [Step 1: Create the environment](self-deployed-create-env.md).
+ You associated the Amazon Elastic VMware Service VLAN subnets with a route table that has a default route to your NAT gateway. The VCF Installer downloads software from the Broadcom online depot, so the VM management VLAN subnet needs outbound internet access. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).
+ You created and verified the forward (A) and reverse (PTR) DNS records for every host and VCF appliance. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).
+ You added the first diskless host, and it is in the `CREATING` or `CREATED` state. For more information, see [Step 3: Add hosts](self-deployed-add-hosts.md). You can add the remaining hosts later in this step, while the VCF software downloads.
+ You have a computer or an instance with a web browser that can reach the private IP addresses of your VPC. You use it to open the VMware Host Client and the VCF Installer. For more information, see [Launch an instance to reach the VPC](network-dhcp-dns-ntp.md#network-access-instance).
+ You have a Broadcom account with a VCF entitlement, and you downloaded the VCF Installer Open Virtualization Appliance (OVA) file for your VCF version from the [Broadcom Support Portal](https://support.broadcom.com/).
+ You chose the size and type of your external storage. For more information, see [External storage options for diskless hosts](external-storage-diskless.md) and [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).

The examples on this page and in Step 4b (diskless) use the following values. Replace the example addresses and names with your own values.


| Item | Example value | 
| --- | --- | 
| Instance type |  `r7i.metal-24xl`  | 
| VPC CIDR block | 10.10.0.0/16 | 
| Domain name in the DHCP option set |  `evs.example.com`  | 
| Service access subnet | 10.10.200.0/24 | 
| DNS servers in the DHCP option set | 10.10.200.100 and 10.10.200.101 | 
| Host management VLAN subnet | 10.10.0.0/24 | 
| VM management VLAN subnet | 10.10.1.0/24 | 
| Host names and addresses |  `esx01` (10.10.0.11) and `esx02` (10.10.0.12) | 
| VCF Installer, which becomes SDDC Manager |  `sddcm` (10.10.1.12) | 
| FSx for OpenZFS endpoint IP address | 10.10.200.50 | 

### DNS records for the example
<a name="getting-started-diskless-dns"></a>

Create an A record and a PTR record for each name in the following table before you add the first host. The example uses the `evs.example.com` zone. The specification in Step 4b (diskless) gives no IP addresses for the appliances, so the VCF Installer takes them from these records. For the record requirements and the verification steps, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).


| Name | IP address | Use | 
| --- | --- | --- | 
|  `esx01`  | 10.10.0.11 | First host | 
|  `esx02`  | 10.10.0.12 | Second host | 
|  `vc`  | 10.10.1.10 | vCenter Server | 
|  `nsx`  | 10.10.1.11 | NSX Manager virtual IP address | 
|  `sddcm`  | 10.10.1.12 | VCF Installer, which becomes SDDC Manager | 
|  `nsx01`  | 10.10.1.16 | NSX Manager node | 
|  `vcfops`  | 10.10.1.19 | VCF Operations | 
|  `vcfopscol`  | 10.10.1.23 | VCF Operations collector | 
|  `vsp-platform`  | 10.10.1.25 | VCF services platform | 
|  `vsp-instance`  | 10.10.1.26 | VCF services platform | 
|  `vsp-fleet`  | 10.10.1.27 | VCF services platform | 
|  `vcf-vidb`  | 10.10.1.28 | VCF identity database | 
|  `vcf-license`  | 10.10.1.29 | VCF license server | 

Keep these addresses outside the address ranges in the specification. In the example, the VCF services platform pool uses 10.10.1.100 to 10.10.1.113, and the NFS network range uses 10.10.0.20 to 10.10.0.29.

## Create the external storage
<a name="getting-started-diskless-storage"></a>

Create your external storage while the first host is created. A host reaches the `CREATED` state in about 9 minutes, and a file system becomes available in 10 to 25 minutes.

For Amazon FSx for OpenZFS, create a file system and two NFS volumes. Use `vcf-principal` as the principal datastore and `installer-staging` as the temporary datastore for the VCF Installer appliance. Note the endpoint IP address of the file system. For instructions, see [Configure FSx for OpenZFS as principal storage for diskless hosts](config-fsx-openzfs-datastore.md).

## Prepare the first host
<a name="getting-started-diskless-prep-host"></a>

The VCF Installer expects its appliance and the principal datastore on the first host. Diskless hosts have no local storage, so you use the two NFS volumes for both. This procedure replaces the Amazon EBS-backed temporary datastore that hosts with local storage use.

Amazon EVS stores the ESX root password of each host in AWS Secrets Manager. Each host has its own secret. To find the secret, search Secrets Manager for the environment ID. The value of the secret is a plain string and not JSON. The `credentials` list of the environment stays empty in Self-deployed mode.

In the VMware Host Client, do the following:

1. Open `https://esx01.evs.example.com` in your browser. The certificate is self-signed, so your browser shows a warning.

1. Sign in as `root` with the root password from Secrets Manager.

1. Set the `VM Network` port group to the VM management VLAN ID, and keep the host management port group untagged with VLAN ID `0`. Without this VLAN ID, the VCF Installer appliance can’t reach the VM management VLAN subnet. For how to find the VLAN ID, see [VLAN subnets, VLAN IDs, and IP addresses](vlan-subnet-reference.md).

1. Choose **Storage**, **Datastores**, and **New datastore**, and then choose **Mount NFS datastore**.

1. Enter the following values, and finish the wizard.
   + For **NFS server**, enter the endpoint IP address of the file system.
   + For **NFS share**, enter `/fsx/installer-staging`.
   + For **NFS version**, choose NFS 3.
   + For **Name**, enter a name such as `fsx-staging`.

1. Repeat the previous two steps to mount the principal datastore with the share `/fsx/vcf-principal` and a name such as `fsx-principal`.

You have mounted both datastores on the first host. Both datastores mount through the host management VMkernel adapter (`vmk0`). Don’t create a separate NFS VMkernel adapter.

Each datastore shows the capacity of the file system, or the volume quota if you set one. For example, a 7,168 GiB file system with no volume quota appears as a 7,168 GiB datastore. The VCF Installer checks this size during validation. For more information, see [Size the file system](config-fsx-openzfs-datastore.md#fsx-openzfs-sizing).

The principal datastore must be mounted on the first host before you validate the specification. Otherwise, the VCF Installer reports that it can’t find the datastore on the host. For more information, see [article 414088](https://knowledge.broadcom.com/external/article/414088) in the Broadcom knowledge base. If a mount fails, check the security group of the file system and the NFS export list. For more information, see [Security group rules](config-fsx-openzfs-datastore.md#fsx-openzfs-security-group) and [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

## Deploy the VCF Installer
<a name="getting-started-diskless-installer"></a>

Deploy the VCF Installer OVA file onto the first host, on the staging datastore.

In the VMware Host Client, do the following:

1. Choose **Virtual Machines**, and then choose **Create / Register VM**.

1. Choose **Deploy a virtual machine from an OVF or OVA file**, enter a name such as `sddcm`, and select the OVA file.

1. Choose the `fsx-staging` datastore.

1. On the deployment options page, map the network to `VM Network`, choose thin disk provisioning, and turn on **Power on automatically**.

1. On the additional settings page, enter the appliance values. The following table shows example values.


<table>
<thead>
  <tr><th>Setting</th><th>Example value</th></tr>
</thead>
<tbody>
  <tr><td>Host Name</td><td> <code>sddcm.evs.example.com</code> </td></tr>
  <tr><td>Network 1 IPv4 Address</td><td>10.10.1.12</td></tr>
  <tr><td>Network 1 Subnet Mask</td><td>255.255.255.0</td></tr>
  <tr><td>Network Default IPv4 Gateway</td><td>10.10.1.1</td></tr>
  <tr><td>DNS Domain Name</td><td> <code>evs.example.com</code> </td></tr>
  <tr><td>Domain Search Path</td><td> <code>evs.example.com</code> </td></tr>
  <tr><td>Domain Name Servers</td><td>10.10.200.100,10.10.200.101</td></tr>
  <tr><td>NTP Servers</td><td> <code>time.aws.com</code> </td></tr>
  <tr><td>Root user password and local user password</td><td>Your own passwords</td></tr>
</tbody>
</table>


1. Finish the wizard.

The VCF Installer appliance becomes SDDC Manager after deployment. Its IP address and host name must match the SDDC Manager record in your DNS plan. The passwords must be at least 15 characters long and contain an uppercase letter, a lowercase letter, a digit, and one of the special characters `! % @ $ ^ # ? *`. For more information, see [VCF Installer settings for Amazon EVS](vcf-installer-settings.md).

The import of the OVA file onto the NFS datastore takes about 2 minutes. The VCF Installer web service responds within a few minutes after the appliance starts. To verify, open `https://sddcm.evs.example.com` in your browser, and sign in as `admin@local` with the local user password that you entered in the wizard.

Right after the first start, the inventory page of the VCF Installer can show an error for more than 30 minutes. The error doesn’t stop you from connecting the Broadcom online depot or from validating the specification. Continue with the next section, and don’t wait for the inventory page.

## Connect the software depot
<a name="getting-started-diskless-depot"></a>

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

The catalog lists install and patch images of each component, and several builds of your VCF version. Download the install image of the newest build of each component within the VCF version that you selected. The VCF Installer downloads three bundles at a time.

## Add the remaining hosts
<a name="getting-started-diskless-host2"></a>

Add the other hosts while the downloads run. All hosts in a cluster must use the same instance type and the same ESX version. Before you add each host, verify its DNS records. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).

Diskless hosts support only ESX 9.x versions. Choose an ESX version that Amazon EVS provides for the instance type and that matches your VCF Installer build. To list the ESX versions for the instance type, run `aws evs get-versions`. For more information, see [Supported VCF versions and instance types](versions-provided.md).

You can add a host by using the Amazon EVS console or the AWS CLI.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then choose your environment.

1. Choose the **Hosts** tab, and then choose **Create host**.

1. Enter the short host name from your DNS records, such as `esx02`. Choose your Amazon EC2 key pair. Choose the same instance type and ESX version as for the first host.

1. Choose **Create host**.

1. Run the `aws evs create-environment-host` command.

   In the following command, replace `<esx-version>` with the ESX version of the first host, as listed in the `get-versions` response. Replace the example environment ID, host name, and key pair name with your own values. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs create-environment-host \
       --environment-id env-abcde12345 \
       --esx-version <esx-version> \
       --host '{
           "hostName": "esx02",
           "keyName": "my-ec2-key-pair",
           "instanceType": "r7i.metal-24xl"
       }' \
       --region <region-code>
   ```

1. Check the host state. The create command doesn’t return a host ID, so use the host name to find the host.

   Replace the example environment ID with your own value, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345 \
       --query 'environmentHosts[].[hostName,hostState,ipAddress]' \
       --output table \
       --region <region-code>
   ```

Don’t run the create command again for a host that is in the `CREATING` state. A host usually reaches `CREATED` in about 9 minutes. When a host is `CREATED`, confirm that its IP address equals the address in its A record. If a host stays in `CREATING`, check its DNS records first. For more information, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

You don’t prepare the other hosts. The VCF Installer mounts the datastores on them during deployment. Get the root password of each host from Secrets Manager, because you need it in the specification.

When every host is `CREATED` and every download shows success, you have prepared the diskless hosts and the VCF Installer.

Next step: [Step 4b (diskless): Create the specification and deploy](deploy-diskless-spec.md).

**Topics**