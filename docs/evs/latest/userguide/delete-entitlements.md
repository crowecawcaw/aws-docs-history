

# Deleting Windows Server entitlements
<a name="delete-entitlements"></a>

When you no longer need AWS-offered Windows Server licensing for your VMs, delete their Windows Server entitlements. When you delete an entitlement, Amazon EVS stops tracking Windows Server entitlement usage for the specified VM. After deletion, the VM no longer has a Windows Server entitlement through AWS.

Note the following constraint: you can delete up to 100 entitlements at a time.

 **To delete an Amazon EVS entitlement** 

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

1. To verify completion, list the entitlement.

   ```
   aws evs list-vm-entitlements \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --entitlement-type WINDOWS_SERVER
   ```