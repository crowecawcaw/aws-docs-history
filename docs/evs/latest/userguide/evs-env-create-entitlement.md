# Create an Amazon EVS entitlement

You can create Windows Server entitlements for one or more virtual machines (VMs) running in your Amazon EVS environment.
After you have created an entitlement and the VM is powered on, Amazon EVS starts monitoring the corresponding VM’s Windows Server entitlement usage, allowing you to consume Windows Server licenses directly through AWS on a pay-as-you-go basis.

More info on entitlements can be found under [Concepts and components of Amazon EVS](concepts.md#concepts-windows-server-license-entitlement "concepts.md#concepts-windows-server-license-entitlement").

###### Note

Only 100 entitlements can be created at a single time.

###### Note

You must create a vCenter connector before creating entitlements.
The connector must be in an Active state and the reachability checker must be in a Passed state.

###### Note

Validation happens asynchronously.
If a VM fails validation (for example, unsupported guest OS or VM not found), its entitlement status is set to create failed with error details.
You can fix the underlying issue, then create the entitlement again.

###### Note

In vCenter you can use PowerCLI or other tooling to get the VM Managed Object ID.

**To create an Amazon EVS entitlement**

Follow these steps to create an Amazon EVS entitlement.

###### Example

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. In the navigation pane, choose **Environments**.
3. Select the environment containing the VMs.
4. Select the **Entitlements** tab.
5. Choose **Add**.
6. Product type defaults to **Windows server**.
7. Add the VMs you want to create entitlements for via text or by uploading a CSV file.

   - CSV format is a single column of only VM IDs.

8. Choose **Add entitlement**.
9. To verify completion, check that the entitlement **status** has changed to Created.

AWS CLI

1. Open a new terminal session.
2. Create entitlements.
   See example command below for reference.

```
aws evs create-entitlement \
    --environment-id env-abcde12345 \
    --connector-id cnctr-szgj87q6gi \
    --entitlement-type WINDOWS_SERVER \
    --vm-ids vm-001 vm-002 vm-003
```

3. To verify completion, list the VM entitlements and check that the entitlement status is Created.

```
aws evs list-vm-entitlements \
  --environment-id env-abcde12345 \
  --connector-id cnctr-szgj87q6gi \
  --entitlement-type WINDOWS_SERVER
```
