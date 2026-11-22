

# Troubleshoot Windows Server entitlements

A Windows Server entitlement in an Amazon Elastic VMware Service environment might fail to create, enter the `AT_RISK` status, or be removed. This page applies to both deployment modes. For how entitlements work, see [Windows Server entitlements](entitlements.md).

## Entitlement status is `CREATE_FAILED`
<a name="create-entitlement-failure-reasons"></a>

When you create an entitlement, Amazon EVS validates the configuration of each virtual machine (VM). If a VM fails validation, its entitlement status is set to `CREATE_FAILED` with error details. After you fix the underlying issue for that VM, you must create the entitlement again. For the procedure, see [Create Windows Server entitlements](create-entitlements.md).

**Note**  
Amazon EVS deletes entitlements in the `CREATE_FAILED` state after 90 days.

Read the error details of the entitlement, and then find the cause in the following sections.

### VM not found
<a name="create-entitlement-failure-vm-not-found"></a>

The VM ID (Managed Object ID) that you specified isn’t in the vCenter inventory that the connector targets.

 **Cause** 

The VM ID is incorrect, or the VM doesn’t exist in the vCenter Server appliance that the connector points to.

 **Solution** 

1. Verify that the VM ID is correct. To find the Managed Object ID of a VM, sign in to vCenter Server and select the VM. The ID appears in the browser address bar as part of the URL.

1. Confirm that the VM exists in the vCenter Server that the connector targets.

1. Create the entitlement again.

### VM is disconnected, orphaned, or inaccessible
<a name="create-entitlement-failure-vm-not-connected"></a>

The VM is in a disconnected, orphaned, or inaccessible state in vCenter Server.

 **Cause** 

An underlying host or network issue typically causes this state.

 **Solution** 

1. Check the state of the VM in vCenter Server.

1. Resolve the host or network issue so that the VM is no longer disconnected, orphaned, or inaccessible.

1. Create the entitlement again.

### Unsupported guest operating system
<a name="create-entitlement-failure-unsupported-os"></a>

The guest operating system in the VM settings in vCenter Server must be Windows Server 2016 or later. Validation fails if the guest operating system is any of the following:
+ Not Windows.
+ A Windows client operating system, such as Windows 10 or Windows 11.
+ A Windows Server version earlier than 2016.

 **Cause** 

The guest operating system in the VM settings isn’t a supported Windows Server version.

 **Solution** 

1. Verify the guest operating system in the VM settings in vCenter Server.

1. Change the VM settings to a supported Windows Server version (2016 or later).

1. Create the entitlement again.

## Entitlement status is `AT_RISK`
<a name="troubleshoot-entitlement-at-risk"></a>

An entitlement enters the `AT_RISK` status when the reachability check of its vCenter connector fails. The failure affects the entitlements of all Windows Server VMs under the affected vCenter Server appliance.

You have 8 hours from the time the vCenter reachability check starts failing to restore the connection:
+ If you restore the connection within the 8-hour grace period, Amazon EVS recovers all events in that period and keeps your Windows Server VM entitlements with no further action.
+ If you don’t restore the connection within the 8-hour grace period, Amazon EVS removes the entitlements and changes their status to `ENTITLEMENT_REMOVED`. Amazon EVS also sends you a notification through the AWS Health Dashboard. Windows Server license usage tracking stops as of the time the connection was lost.

 **Cause** 

Amazon EVS can’t reach or sign in to the vCenter Server appliance through the connector.

 **Solution** 

1. Verify that the connector state is `ACTIVE` and that its reachability check status is `FAILED`.

1. Verify that the appliance credentials stored in AWS Secrets Manager are current and correct. If the credentials have changed, update them. For more information, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).

1. Fix the DNS records of the appliance FQDN, the reachability of your DNS servers, and your firewall rules, as described in [Amazon EVS can’t reach DNS servers or SDDC Manager](troubleshoot-networking.md#troubleshoot-dns-reachability).

1. Make sure that the appliance is running and accessible.

## Entitlement status is `ENTITLEMENT_REMOVED`
<a name="troubleshoot-entitlement-removed"></a>

The `ENTITLEMENT_REMOVED` status means that Amazon EVS has removed the entitlement for the VM and stopped tracking Windows Server license usage for it.

**Note**  
Amazon EVS deletes entitlements that remain in the `ENTITLEMENT_REMOVED` status for 90 days.

 **Cause** 

The status can result from one of the following:
+ The vCenter connector reachability failure lasted longer than the 8-hour grace period, so the entitlement moved from `AT_RISK` to `ENTITLEMENT_REMOVED`. For more information, see [Entitlement status is `AT_RISK`](#troubleshoot-entitlement-at-risk).
+ The VM is disconnected, orphaned, or inaccessible, which typically indicates an underlying host or network issue.
+ The VM is no longer in the vCenter inventory.
+ The guest operating system of the VM was changed to an unsupported version. Amazon EVS supports Windows Server 2016 or later.

 **Solution** 

Check the error details of the entitlement to find the specific cause. Then, based on the cause, do the following:

1. If the vCenter reachability failure exceeded the grace period, restore the vCenter Server connection.

1. If the VM is disconnected, orphaned or inaccessible, check the connection state of the VM in vCenter Server. Resolve the underlying issue so that the VM returns to a compliant state. A VM can become disconnected if its host loses its connection to vCenter Server and vSphere HA fails to recover the VM on another host. A VM can become orphaned because of storage connectivity issues or interrupted migrations.

1. If the VM is no longer in the vCenter inventory, restore the VM in vCenter Server.

1. If the VM has an unsupported guest operating system, update the guest operating system to a supported version.

After you resolve the underlying issue in your VMware Cloud Foundation (VCF) environment, Amazon EVS validates the affected entitlements and restores them automatically shortly afterward. Entitlements resume from the time when Amazon EVS validates that the VMs are compliant again.

If these steps don’t resolve the problem, see [Get help from AWS Support and Broadcom](get-help.md) for who to contact and what to include in a case.