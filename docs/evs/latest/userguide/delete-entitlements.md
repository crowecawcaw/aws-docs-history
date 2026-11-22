

# Delete Windows Server entitlements

When you no longer need Windows Server licensing from AWS for a VM in your Amazon Elastic VMware Service environment, delete its Windows Server entitlement. You can use the Amazon EVS console or the AWS CLI. You can delete up to 100 entitlements at a time.

**Important**  
When you delete an entitlement, Amazon EVS stops tracking Windows Server entitlement usage for that VM. After deletion, the VM no longer has a Windows Server entitlement through AWS. To cover the VM again, create a new entitlement.

## Delete entitlements
<a name="delete-entitlements-procedure"></a>

To delete entitlements in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the VMs.

1. Select the **Entitlements** tab.

1. Select the VMs whose entitlements you want to delete.

1. Choose **Delete**.

1. Confirm the deletion.

1. To verify, check that the entitlements for those VMs no longer appear in the list.

1. Open a terminal session.

1. Delete the entitlements. The following command is an example. Replace the values in angle brackets with your own values. Replace the example VM IDs with your own values.

   ```bash
   aws evs delete-entitlement \
       --environment-id <environment-id> \
       --connector-id <connector-id> \
       --entitlement-type WINDOWS_SERVER \
       --vm-ids vm-003 vm-001
   ```

1. To verify, list the entitlements and check that the deleted VMs no longer appear. Replace the values in angle brackets with your own values.

   ```bash
   aws evs list-vm-entitlements \
       --environment-id <environment-id> \
       --connector-id <connector-id> \
       --entitlement-type WINDOWS_SERVER
   ```

You have deleted the Windows Server entitlements for the selected VMs.

If you no longer need the vCenter connector, you can delete it. See [Delete a connector](evs-env-delete-connector.md).