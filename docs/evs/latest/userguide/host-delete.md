

# Delete a host (VCF 9.x)

You can delete a host from a Self-deployed environment when you no longer need it. You remove the host from its cluster with VMware Cloud Foundation (VCF) 9.x tools first, and then delete it with the Amazon Elastic VMware Service console or the AWS CLI. Before you delete a host, make sure that the cluster keeps enough hosts for your VCF topology.

For minimum host counts, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API. Deleting a host from the Amazon EC2 console can leave your environment in an inconsistent state.

To delete every host and the environment, see [Clean up a Self-deployed environment](self-deployed-cleanup.md) instead. For EVS-deployed environments (VCF 5.2.x), see [Delete a host (VCF 5.x)](evs-env-delete-host.md).

## Step 1: Remove the host from VCF
<a name="host-delete-vcf"></a>

 **In VCF** 

1. Place the host in maintenance mode in the vSphere Client, and migrate its VMs to the other hosts in the cluster.

1. Remove the host from its cluster and from the VCF inventory.

For the procedures, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1.html).

For a diskless host, the datastores of the cluster are on external storage, so removing the host doesn’t delete them.

## Step 2: Delete the host
<a name="host-delete-evs"></a>

To delete the host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**, and then choose your environment.

1. Choose the **Hosts** tab.

1. Select the host and choose **Delete** > **Delete host**. Repeat this step for each host that you want to delete.

1. To verify completion, check that the host no longer appears in the **Hosts** tab, or that its **Host state** is **Deleted**.

1. Run the `delete-environment-host` command. Replace the example environment ID and host name with your own values. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs delete-environment-host \
       --environment-id env-abcde12345 \
       --host-name esx05 \
       --region <region-code>
   ```

1. To verify completion, list the hosts and confirm that the host is no longer listed or that its state is `DELETED`. Replace the example environment ID with your own value. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345 \
       --query 'environmentHosts[].[hostName,hostState]' \
       --output table \
       --region <region-code>
   ```

You have deleted the host. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md).