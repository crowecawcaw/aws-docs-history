

# Troubleshoot hosts

Host problems might occur when you create, add, upgrade, or connect to ESX hosts in an Amazon Elastic VMware Service environment. This page applies to both deployment modes. For host creation problems during a Self-deployed deployment, see [Troubleshoot Self-deployed deployments](troubleshoot-self-deployed.md).

## Host creation fails with a vCPU limit error
<a name="troubleshoot-vcpu-limit"></a>

When you create an environment or add a host, the host creation fails with an error such as `VcpuLimitExceeded`.

 **Cause** 

Your Amazon EC2 Running On-Demand Standard Instances quota is measured in vCPUs, and it doesn’t cover the vCPUs of all the EC2 instances that you use. Host creation also fails when the host count per Amazon EVS environment quota is lower than the number of hosts that you create.

 **Solution** 

1. Check both quotas, and compare them with the hosts that you plan to run. For the quotas and the vCPUs of each instance type, see [Service quotas for Amazon EVS](service-quotas-evs.md) and [Supported VCF versions and instance types](versions-provided.md).

1. Request an increase for the quota that is too low. For more information, see [Request an increase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html#request-increase) in the *Amazon EC2 User Guide*.

1. Create the host again after the increase is approved.

## vSphere HA agent on this host could not reach isolation address
<a name="troubleshoot-vsphere-ha-agent-ipv6"></a>

In the vSphere Client, with the ESX host selected, you see the message "vSphere HA agent on this host could not reach isolation address <IPv6 address>". The host can show a yellow warning status while the cluster stays healthy.

 **Cause** 

The vSphere HA agent on the host can’t reach the default IPv6 isolation address that vSphere HA uses for heartbeat checks. The message occurs because Amazon EVS doesn’t support IPv6.

 **Solution** 

No action is needed. The message doesn’t indicate a problem, and the absence of IPv6 support doesn’t affect the core functions of vSphere HA.

## vSAN upgrade prechecks fail for the ESX host cluster
<a name="troubleshoot-vsan-precheck-fail"></a>

This section applies to hosts with local storage, which use vSAN.

When you upgrade the ESX host cluster with SDDC Manager, vSAN disk-related prechecks can fail.

 **Cause** 

Amazon EVS uses vSAN Express Storage Architecture (ESA), and these upgrade prechecks don’t apply to vSAN ESA.

 **Solution** 

Follow the guidance in [article 369423](https://knowledge.broadcom.com/external/article/369423/upgrade-prechecks-fails-with-esxi-cluste.html) in the Broadcom knowledge base. For how to update and upgrade your environment, see [Update and upgrade](evs-lifecycle-mgmt.md).

## vSAN capacity warning received in AWS Health
<a name="troubleshoot-vsan-capacity"></a>

This section applies to hosts with local storage, which use vSAN.

You received an AWS Health notification with the event type `AWS_EVS_VSAN_CAPACITY_WARNING`. You can view the notification in the [AWS Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/aws-health-account-views.html). To receive these notifications automatically, use Amazon EventBridge. For more information, see [Monitoring events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html).

Amazon EVS checks the vSAN utilization of each cluster once an hour. Amazon EVS sends this notification when a cluster reaches 70% utilization or more, or when it can’t read a cluster’s capacity.

Amazon EVS closes the notification automatically after the issue is resolved. These warnings appear only in AWS Health and don’t affect your environment status or connector check results.

Act on this notification promptly. vSAN needs free capacity to rebuild data after a host or device failure and to complete operations such as rebalancing and storage policy changes. If vSAN can’t rebuild data in a timely manner, you run the risk of cascading VM failures. A vSAN capacity warning might indicate one of the following issues:
+ A cluster’s vSAN utilization is 70% or more. To reduce utilization, do one or more of the following:
  + In the vSphere Client, choose your cluster, and then choose **Monitor**, **vSAN**, **Capacity** to see what is using the space.
  + Delete virtual machines and snapshots that you no longer need.
  + Provision additional external storage, such as [Amazon FSx for NetApp ONTAP](fsx-ontap.md), and move virtual machines to it.
  + Add hosts to your environment to increase capacity. For more information, see [Add a host (VCF 5.x)](evs-env-create-host.md).
+ The credentials in your environment connector don’t have permission to read cluster capacity. Amazon EVS reports a permission problem when the appliance denies the request, or when the appliance returns no clusters because the account can’t see them. If this is the issue, verify the access of the account that the connector uses. If you create a new user or API key, update the credentials in AWS Secrets Manager as described in [Update a connector](evs-env-update-connector.md).
  + For an SDDC Manager connector, verify that the API key belongs to a service user with the `VIEWER` role.
  + For a VCF Operations connector, verify that the user has a read-only role, such as `ReadOnly`, with a scope that includes your clusters, such as `All Objects`.
+ Amazon EVS can’t read a cluster’s capacity. Amazon EVS can reach the appliance and has permission, but the appliance doesn’t return valid capacity values for a cluster. If this is the issue, in SDDC Manager or VCF Operations, verify that the cluster is listed and reports its vSAN capacity.

If you are still unable to resolve the issue after following this guidance, contact AWS Support for further assistance.

## Adding a host fails because the cluster image is incompatible
<a name="troubleshoot-cluster-image"></a>

Adding a host to your environment fails with an error that the new host isn’t compatible with your cluster image.

<a name="troubleshoot-add-host-failure-cluster-image"></a> **Cause** 

A new host has the latest available version of the Amazon EVS custom vendor add-on. If the other hosts in your cluster use an older add-on version, the new host doesn’t match the cluster image.

 **Solution** 

Use vSphere Lifecycle Manager (vLCM) to extract the latest add-on version from the new host, and update the cluster image.

**Important**  
Updating the cluster hosts to the latest add-on version requires host reboots.

 **In the vSphere Client** 

1. Go to the **Hosts and Clusters** inventory in vCenter Server.

1. To extract the add-on from the new host, create a temporary empty cluster.

1. Under **Basics**, select **Import image from an existing host in the vCenter Inventory**, and create the cluster. Leave all other settings at their defaults.

1. After the temporary cluster is created with the extracted image, delete the temporary cluster. The add-on is now available in your vLCM depot.

1. Go to your environment cluster, and choose the **Updates** tab.

1. Edit your cluster image, and change the add-on version to the version that you extracted.

1. Choose **Save**.

 **In SDDC Manager** 

1. Retry the failed add host task. The task remediates your cluster hosts and updates all of them to the latest add-on version.

For where to get the add-on, see [Use the Amazon EVS custom add-on depot](addon-depot.md).

## SDDC Manager fails VCF host validation during host commissioning
<a name="troubleshoot-sddc-failure-host-commission"></a>

This section applies to EVS-deployed environments that run VMware Cloud Foundation (VCF) 5.2.x.

SDDC Manager fails during VCF host validation in the commission hosts step.

 **Cause** 

You updated the ESX version of your cluster after the Amazon EVS environment was deployed, and the new host runs a different ESX version.

 **Solution** 

Use vLCM to upgrade ESX on the new host to the ESX version of your cluster.

These steps require that you add the host to vCenter Server temporarily, outside of SDDC Manager.

**Warning**  
If you use vLCM for any operation other than an ESX upgrade on this host, the host might become unusable. If that happens, you must delete the host and create a new Amazon EVS host.

 **In the vSphere Client** 

1. Go to the **Hosts and Clusters** inventory in vCenter Server.

1. Add the host temporarily to your virtual data center, and select **manage host with an image**. You remove the host in a later step. For more information, see [How to Add a Host to Your vSphere Data Center or Folder](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/organizing-your-inventory/add-a-host-to-a-folder-or-a-data-center.html) in the Broadcom documentation.

1. On the **Updates** tab of the host, edit the host image to match the ESX version of your cluster, and upgrade the host.

1. After the upgrade completes, remove the host from your vCenter Server inventory. For more information, see [How to Remove an ESX Host from Your vCenter Server Instance](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/managing-hosts-in-the-vsphere-client/remove-a-host-from-vcenter-server.html) in the Broadcom documentation.

 **In SDDC Manager** 

1. Commission the host. For more information, see [Commission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/commission-hosts-admin.html) in the Broadcom documentation.

1. After the host is commissioned, add the host to your cluster.

For the full procedure, see [Add a host (VCF 5.x)](evs-env-create-host.md).

## Hosts can’t mount an FSx for ONTAP NFS datastore
<a name="troubleshoot-nfs-ontap"></a>

 **Cause** 

A security group rule or a route between the service access subnet and the VMkernel management VLAN subnet is missing.

 **Solution** 

Check the security group rules of the Amazon FSx for NetApp ONTAP file system. Also check the routes between the service access subnet and the VMkernel management VLAN subnet. For the configuration, see [Configure FSx for ONTAP as an NFS datastore](config-fsx-nfs-datastore.md). For diskless hosts (VCF 9.x) with FSx for OpenZFS, see [The NFS datastore doesn’t mount](troubleshoot-self-deployed.md#troubleshoot-diskless-mount).

## You can’t reach an ESX host over the network
<a name="access-ec2-serial-console"></a>

A host has a boot problem, a network configuration problem, or another issue, and you can’t reach the host over the network.

 **Cause** 

The host has lost its network configuration or doesn’t boot correctly. Amazon EVS disables remote SSH by default.

 **Solution** 

Use the Amazon EC2 serial console. By default, Amazon EVS enables the ESX Shell on newly deployed hosts, so that you can access the serial port of the EC2 instance through the EC2 serial console. The serial console doesn’t require your instance to have network connectivity. You enter commands as if your keyboard and monitor were attached directly to the serial port of the instance.

**Note**  
The EC2 serial console is the only mechanism that Amazon EVS supports to access the Direct Console User Interface (DCUI) of an ESX host locally.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API. For more information, see [Manage hosts](host-management.md).

Before you begin, complete the prerequisites for the EC2 serial console. For more information, see [Prerequisites for the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.html) in the *Amazon EC2 User Guide*.

To connect to the serial console, do the following.

1. Grant serial console access at the account level, and configure IAM policies that grant access to your users. For more information, see [Configure access to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html) in the *Amazon EC2 User Guide*.

1. Make sure that the instance state is `running`. You can’t connect to the serial console when the instance is in the `pending`, `stopping`, `stopped`, `shutting-down`, or `terminated` state. For more information, see [Amazon EC2 instance state change](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.

1. Connect to the serial console with the EC2 console or the AWS CLI. For more information, see [Connect to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-serial-console.html) in the *Amazon EC2 User Guide*.

To use the remote ESX Shell over SSH instead, see [Remote ESX Shell Access with SSH](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/getting-started-with-esxcli/running-host-management-commands-in-the-esxi-shell/remote-esxi-shell-access-with-ssh.html) in the Broadcom documentation.

If these steps don’t resolve the problem, see [Get help from AWS Support and Broadcom](get-help.md) for who to contact and what to include in a case.