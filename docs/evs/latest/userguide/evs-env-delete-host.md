

# Delete a host (VCF 5.x)

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Manage hosts](host-management.md).

You can delete an Amazon Elastic VMware Service host from your environment when you no longer need it. You decommission the host in SDDC Manager first, and then delete it with the Amazon EVS console or the AWS CLI. Before you delete a host, make sure that your environment keeps enough hosts for your VMware Cloud Foundation (VCF) deployment topology.

For minimum host counts, see the [Broadcom documentation for VCF](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2.html).

**Warning**  
If you delete a host without decommissioning it, stale data stays in vCenter Server and SDDC Manager, and you might need extra work to clean it up. Decommission the host before you delete it in the Amazon EVS console or with the Amazon EVS API.

**Warning**  
Don’t use the Amazon EC2 console to stop, start, or terminate Amazon EVS hosts. On hosts with local storage, these actions cause the loss of the vSAN data on the instance store volumes. To create, replace, or delete a host, use the Amazon EVS console, the AWS CLI, or the Amazon EVS API. Deleting a host from the Amazon EC2 console can leave your environment in an inconsistent state.

## Step 1: Decommission the host
<a name="evs-env-delete-host-sddc"></a>

 **In SDDC Manager** 

1. Remove the host from its cluster.

1. Decommission the host. For more information, see [Decommission Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/host-management-admin/decommission-hosts-admin.html) in the Broadcom documentation.

## Step 2: Delete the host
<a name="evs-env-delete-host-evs"></a>

To delete the host in the Amazon EVS console or with the AWS CLI, use the following steps.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the host to delete.

1. Choose the **Hosts** tab.

1. Select the host and choose **Delete** > **Delete host**. Repeat this step for each host that you want to delete.

1. To verify completion, check that the host no longer appears on the **Hosts** tab, or that its **Host state** is **Deleted**.

1. Run the `delete-environment-host` command. Replace the example environment ID and host name with your own values.

   ```bash
   aws evs delete-environment-host \
       --environment-id env-abcde12345 \
       --host-name esxi-host-05
   ```

1. To verify completion, list the hosts of the environment and confirm that the host is no longer listed or that its state is `DELETED`.

   ```bash
   aws evs list-environment-hosts \
       --environment-id env-abcde12345 \
       --query 'environmentHosts[].[hostName,hostState]' \
       --output table
   ```

You have deleted the host. In SDDC Manager, confirm that the host no longer appears in the host inventory. To check the environment after the change, see [Monitor environment status](evs-env-status-check.md).