

# Step 3: Add hosts

Add enough hosts to serve the topology of your target VMware Cloud Foundation (VCF) version. Charges for the Amazon EC2 bare-metal instances begin when you add a host. For more information, see [Billing](getting-started-self-deployed.md#self-deployed-costs). You can add hosts with the Amazon Elastic VMware Service console or the AWS CLI.

For minimum host counts, including vSAN requirements, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).

Before you begin, make sure that the following are true.
+ The A and PTR records of each host resolve. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).
+ Your **Host count per EVS environment** quota is at least the number of hosts that the environment will have after you add hosts. Host creation fails if this quota is lower. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
+ You have an Amazon EC2 key pair. Amazon EVS requires the key pair name when you add a host.

## Choose the instance type and ESX version
<a name="self-deployed-host-choices"></a>

All hosts in a VCF cluster must use the same instance type. For the instance types and ESX versions available to your account, see [Supported VCF versions and instance types](versions-provided.md) or run `aws evs get-versions`.

If you don’t specify an ESX version, Amazon EVS uses the default ESX version for Self-deployed mode, which `aws evs get-versions` reports as `defaultEsxVersion`. We recommend that you specify the ESX version explicitly, so that it matches the VCF Installer build that you use. Confirm that the ESX version is compatible with your VCF release in the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1).

Diskless hosts require external storage that you prepare before you install VCF. For more information, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).

**Note**  
To add diskless hosts, specify a diskless instance type and an ESX 9.x version. Add only the first diskless host at this step. You add the other diskless hosts in [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md), while the VCF software downloads.

## Add a host
<a name="self-deployed-host-create"></a>

To add a host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then choose your environment.

1. Choose the **Hosts** tab, and then choose **Create host**.

1. Enter the host details. Use the short host name from your DNS records (such as `esx01`), the instance type, the ESX version, and your Amazon EC2 key pair.

1. Choose **Create host**.

1. Repeat these steps for each host that your VCF topology requires.

1. Run the `aws evs create-environment-host` command. The following example adds a host that runs ESX 9.0.2 to an Amazon EVS environment. Replace the values in angle brackets with your own values. Replace the example host name, key pair name, and instance type with your own values. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs create-environment-host \
       --environment-id <environment-id> \
       --esx-version ESXi-9.0.2.0.25148076 \
       --host '{
           "hostName": "esx01",
           "keyName": "my-ec2-key-pair",
           "instanceType": "i4i.metal"
       }' \
       --region <region-code>
   ```

1. Repeat this command for each host that your VCF topology requires. Don’t run the command again for a host that is in the `CREATING` state.

1. Check the host state with the following command.

   ```bash
   aws evs list-environment-hosts \
       --environment-id <environment-id> \
       --query 'environmentHosts[].[hostName,hostState,ipAddress]' \
       --output table \
       --region <region-code>
   ```

A host is ready when its state is `CREATED`. Confirm that the IP address of each host equals the address in its A record. If a host stays in `CREATING` or moves to `CREATE_FAILED`, check its DNS records first. For more information, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

**Important**  
Hosts that you add to this environment receive the tag `DoNotDelete-EVS-[<environmentId>]-[<hostname>]`. Don’t delete, stop, or shut down these hosts outside of Amazon EVS. Doing so causes Amazon EVS to lose visibility into the host and can put your environment into an impaired state.

Amazon EVS stores the ESX root password of each host in AWS Secrets Manager. Each host has its own secret. You need the root password to sign in to the VMware Host Client in the next step.

## Host networking settings
<a name="self-deployed-host-networking"></a>

Amazon EVS assigns a VLAN ID to each network function in your environment. To find the VLAN IDs, see the VLAN IDs step in [Prepare the VLAN subnets for VCF](self-deployed-create-env.md#self-deployed-create-env-after). When you install VCF, apply these host networking settings.

 **Host management**   
The host management port group `Management` must remain untagged with VLAN ID `0`. `aws evs list-environment-vlans` also lists a VLAN ID for `vmkManagement`. Don’t use that VLAN ID on the host.

 **VM management**   
On the host where you run the VCF Installer, set the `VM Network` port group to the VM management (`vmManagement`) VLAN ID. For instructions, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md) for hosts with local storage, and [Prepare the first host](getting-started-diskless.md#getting-started-diskless-prep-host) for diskless hosts.

 **Other networks**   
Use the Amazon EVS-assigned VLAN IDs for the vMotion, vSAN, host overlay (`vTep`), Edge overlay (`edgeVTep`), and NSX uplink networks in your deployment specification. For the MTU of each network, see [Amazon EVS network settings for VCF](self-deployed-install-vcf.md#sd-install-network).

 **Uplink teaming**   
Use a failover teaming policy (an active uplink with a standby uplink) for the distributed switch port groups, rather than a load-balancing policy. In NSX, set the teaming policy to `FAILOVER_ORDER`.

The VCF Installer migrates host networking to a distributed switch during bringup. You don’t need to enable SSH on the hosts.

Next step: For hosts with local storage, see [Step 4a (local storage): Prepare the VCF Installer](self-deployed-install-vcf.md). For diskless hosts, see [Step 4a (diskless): Prepare diskless hosts and the VCF Installer](getting-started-diskless.md).