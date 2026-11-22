

# Create Windows Server entitlements

After you create a vCenter connector, you can create Windows Server entitlements for one or more virtual machines (VMs) in your Amazon Elastic VMware Service environment. After you create an entitlement, Amazon EVS starts to monitor the Windows Server entitlement usage of that VM. You can create entitlements for up to 100 VMs in a single request. You can use the Amazon EVS console or the AWS CLI.

## Before you begin
<a name="create-entitlements-prereqs"></a>
+ You meet the requirements in [Before you begin](entitlements.md#entitlements-prerequisites) for [Windows Server entitlements](entitlements.md).
+ Make sure that the vCenter connector is in the `ACTIVE` state and its reachability check is `PASSED`. To create a connector, see [Create a connector](evs-env-create-connector.md).
+ You have the VM ID (Managed Object ID) of each VM. To find it, sign in to vCenter and select the VM. The ID appears in the URL in the browser address bar.

## Create entitlements
<a name="create-entitlements-procedure"></a>

To create entitlements in the Amazon EVS console or with the AWS CLI, choose the tab for the method that you use.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment that contains the VMs.

1. Select the **Entitlements** tab.

1. Choose **Add**.

1. For product type, keep the default, **Windows server**.

1. Add the VMs that you want to create entitlements for. You can enter the VM IDs as text or upload a CSV file. The CSV file has a single column that contains only VM IDs.

1. Choose **Add entitlement**.

1. To verify, check that the entitlement **Status** changes to **Created**.

1. Open a terminal session.

1. Create the entitlements. The following command is an example. Replace the values in angle brackets with your own values. Replace the example VM IDs with your own values.

   ```bash
   aws evs create-entitlement \
       --environment-id <environment-id> \
       --connector-id <connector-id> \
       --entitlement-type WINDOWS_SERVER \
       --vm-ids vm-001 vm-002 vm-003
   ```

1. To verify, list the entitlements of the environment and check that the entitlement status is Created. Replace the values in angle brackets with your own values.

   ```bash
   aws evs list-vm-entitlements \
       --environment-id <environment-id> \
       --connector-id <connector-id> \
       --entitlement-type WINDOWS_SERVER
   ```

You have created Windows Server entitlements for your VMs.

When you create an entitlement, Amazon EVS validates the configuration of each VM. If a VM fails validation, its entitlement status changes to `CREATE_FAILED` with error details. After you fix the cause, you must create the entitlement for that VM again. For causes and solutions, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

## Next step
<a name="create-entitlements-next"></a>

Activate Windows Server on the entitled VMs. For instructions, see [Activate Windows Server on entitled VMs](activate-windows-server.md).