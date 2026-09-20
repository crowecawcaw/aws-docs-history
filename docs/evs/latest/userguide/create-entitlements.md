

# Creating Windows Server entitlements for your VMs
<a name="create-entitlements"></a>

After you create a vCenter connector, you create Windows Server entitlements for one or more virtual machines (VMs) running in your Amazon EVS environment. After you create an entitlement, Amazon EVS starts monitoring the corresponding VM’s Windows Server entitlement usage.

Note the following entitlement constraints:
+ The vCenter connector must be in an Active state, and its reachability checker must be in a Passed state. For more information about creating a connector, see [Creating a vCenter connector](create-vcenter-connector.md).
+ You can create entitlements for a maximum of 100 VMs in a single request.

You add each VM by its VM ID (Managed Object ID). To find a VM’s Managed Object ID, log in to vCenter and select the VM. The Managed Object ID appears in the browser address bar as part of the URL.

 **To create an Amazon EVS entitlement** 

**Example**  

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment containing the VMs.

1. Select the **Entitlements** tab.

1. Choose **Add**.

1. Product type defaults to **Windows server**.

1. Add the VMs you want to create entitlements for via text or by uploading a CSV file.
   + CSV format is a single column of only VM IDs.

1. Choose **Add entitlement**.

1. To verify completion, check that the entitlement **status** has changed to Created.

1. Open a new terminal session.

1. Create entitlements. See example command below for reference.

   ```
   aws evs create-entitlement \
       --environment-id env-abcde12345 \
       --connector-id cnctr-szgj87q6gi \
       --entitlement-type WINDOWS_SERVER \
       --vm-ids vm-001 vm-002 vm-003
   ```

1. To verify completion, list the environment VMs and check that the entitlement status is Created.

   ```
   aws evs list-vm-entitlements \
     --environment-id env-abcde12345 \
     --connector-id cnctr-szgj87q6gi \
     --entitlement-type WINDOWS_SERVER
   ```

## Reasons an entitlement can enter the `CREATE_FAILED` state
<a name="create-entitlement-failure-reasons"></a>

When you create an entitlement, Amazon EVS validates the configuration of each VM. Monitor the entitlement status to confirm that it succeeds. If a VM fails validation, its entitlement status is set to `CREATE_FAILED` with error details. After you fix the underlying issue for that VM, you must create the entitlement again.

**Note**  
Entitlements in the `CREATE_FAILED` state are automatically deleted after 90 days.

An entitlement can fail to create for the following reasons.

### VM not found
<a name="create-entitlement-failure-vm-not-found"></a>

The VM ID (Managed Object ID) that you specified is not present in the vCenter inventory that the connector targets.

Cause  
The VM ID is incorrect, or the VM does not exist in the vCenter appliance that the connector points to.

Resolution  

1. Verify that the VM ID is correct.

1. Confirm that the VM exists in the vCenter that the connector targets.

1. Create the entitlement again.

### VM is disconnected, orphaned, or inaccessible
<a name="create-entitlement-failure-vm-not-connected"></a>

The VM specified is in a disconnected, orphaned, or inaccessible state in the vCenter.

Cause  
This is typically caused by an underlying host or network issue.

Resolution  

1. Check the state of the VM in vCenter.

1. Resolve the host or network issue so that the VM is no longer disconnected, orphaned, or inaccessible.

1. Create the entitlement again.

### Unsupported guest operating system
<a name="create-entitlement-failure-unsupported-os"></a>

The guest operating system configured in the VM settings in vCenter must be Windows Server 2016 or later. Validation fails if it is not Windows, is a Windows client operating system such as Windows 10 or Windows 11 instead of Windows Server, or is a Windows Server version earlier than 2016.

Cause  
The guest operating system configured in the VM settings is not a supported Windows Server version.

Resolution  

1. Verify the guest operating system configured in the VM settings in vCenter.

1. Reconfigure the VM settings to specify a supported Windows Server version (2016 or later).

1. Create the entitlement again.

After you create entitlements for your Windows VMs, activate Windows Server on the entitled VMs. See [Activating Windows Server on entitled VMs](activate-windows-server.md).