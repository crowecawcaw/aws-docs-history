

# Replace a failed host (Self-deployed)

Replace a host in a Self-deployed environment when it fails, or before an EC2 `system-maintenance` or `instance-retirement` event occurs. You add a new host with the Amazon Elastic VMware Service console or the AWS CLI. You then move the cluster workloads to it with VMware Cloud Foundation (VCF) 9.x tools and delete the old host. For when to replace a host, see [Host maintenance and retirement events](evs-host-maintenance.md). For EVS-deployed environments (VCF 5.2.x), see [Replace a host (EVS-deployed)](host-replace-evs-deployed.md).

**Warning**  
Replace a host with local storage before the scheduled event occurs. If EC2 reboots the instance during the event, you lose the vSAN data that’s stored on its instance store volumes.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API.

Diskless hosts have no instance store volumes, and your data stays on your external storage.

## Before you begin
<a name="host-replace-prereqs"></a>

Before you begin, make sure that the following are true.
+ Your **Host count per EVS environment** quota allows one more host than the environment has. You might need to request a quota increase for maintenance that requires host replacement. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md).
+ You created the A and PTR DNS records for the new host. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).
+ You know the instance type and ESX version of the hosts in the cluster. The new host must use the same instance type and ESX version.
+ Any spare host or Capacity Reservation that you keep for replacements is available. For more information, see [Reserve capacity for hosts](plan-capacity.md).

## Step 1: Add the new host
<a name="host-replace-add"></a>

Create the new host, and for a diskless host, connect it to the external storage of the cluster. For the steps, see [Step 1: Create the host](host-add.md#host-add-create) and [Step 2: Connect a diskless host to external storage](host-add.md#diskless-host-add-storage). Get the ESX root password of the new host from AWS Secrets Manager.

## Step 2: Move the workloads and remove the old host from VCF
<a name="host-replace-vcf"></a>

 **In VCF** 

1. Add the new host to the cluster that contains the host to be replaced.

1. If the old host still runs, place it in maintenance mode in the vSphere Client and migrate its VMs to the other hosts.

1. Remove the old host from the cluster and from the VCF inventory.

For the procedures, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).

## Step 3: Delete the old host
<a name="host-replace-delete"></a>

To delete the old host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then choose your environment.

1. Choose the **Hosts** tab.

1. Select the old host and choose **Delete** > **Delete host**.

1. To verify completion, check that the old host no longer appears in the **Hosts** tab, or that its **Host state** is **Deleted**.

1. Run the `delete-environment-host` command. Replace the example environment ID and host name with your own values. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs delete-environment-host \
       --environment-id env-abcde12345 \
       --host-name esx01 \
       --region <region-code>
   ```

1. To verify completion, list the hosts and confirm that the old host is no longer listed or that its state is `DELETED`. Replace the example environment ID with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345 \
       --query 'environmentHosts[].[hostName,hostState]' \
       --output table \
       --region <region-code>
   ```

You have replaced the host. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md). If a step fails, see [Troubleshoot hosts](troubleshoot-hosts.md).