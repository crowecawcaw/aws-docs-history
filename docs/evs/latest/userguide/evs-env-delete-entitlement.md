

# Delete an Amazon EVS entitlement
<a name="evs-env-delete-entitlement"></a>

You can delete Windows Server entitlements for one or more virtual machines (VMs) in your Amazon EVS environment. When you delete an entitlement, Amazon EVS stops tracking Windows Server entitlement usage for the specified VM. After deletion, the VM no longer has a Windows Server entitlement through AWS.

More info on entitlements can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-windows-server-license-entitlement).

**Note**  
You can only delete up to 100 entitlements at a time.

**Note**  
You must specify the VM IDs to delete entitlements from.

**Note**  
After deletion, the VMs will no longer have Windows Server entitlements through AWS.

 **To delete an Amazon EVS entitlement** 

Follow these steps to delete an Amazon EVS entitlement.

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment containing the VMs.

1. Select the **Entitlements** tab.

1. Select the VMs you want to delete entitlements from.

1. Choose **Delete**.

1.  **Confirm** the removal.

1. To verify completion, check that the **Entitlements** for the specific VMs have been removed from the console list.

1. Open a new terminal session.

1. Delete an entitlement. See example command below for reference.

   ```
   aws evs delete-entitlement \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --entitlement-type WINDOWS_SERVER \
       --vm-ids vm-003 vm-001
   ```

1. To verify completion, list the entitlements and confirm the deleted VMs are no longer present.

   ```
   aws evs list-vm-entitlements \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --entitlement-type WINDOWS_SERVER
   ```