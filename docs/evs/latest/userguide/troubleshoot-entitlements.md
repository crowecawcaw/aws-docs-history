

# Troubleshooting Windows Server entitlements
<a name="troubleshoot-entitlements"></a>

This topic describes common issues you might encounter with Windows Server entitlements and how to resolve them.

## Entitlement status is `AT_RISK`
<a name="troubleshoot-entitlement-at-risk"></a>

An entitlement enters the `AT_RISK` status when the associated vCenter connector fails its reachability check (that is, the vCenter connector reachability check status shows as Failed). This failure affects the entitlements for all Windows Server virtual machines (VMs) under the affected vCenter Server appliance.

You have 8 hours from the point the vCenter reachability check starts failing to restore the connection:
+ If you restore the connection within the 8-hour grace period, Amazon EVS recovers all transpiring events and maintains your Windows Server VM entitlements without further action.
+ If the connection is not restored within the 8-hour grace period, Amazon EVS removes the entitlements, changes their status to `ENTITLEMENT_REMOVED`, and sends you a Personal Health Dashboard notification. Windows Server license usage tracking stops as of the time the connection was lost.

To resolve this issue, check the following:
+ Verify the connector state is Active and its reachability check status is Failed.
+ Verify that the appliance credentials stored in AWS Secrets Manager are current and correct. If the credentials have changed, update them. For more information, see [Rotating vCenter connector credentials](rotate-vcenter-credentials.md).
+ Ensure that your DNS servers are reachable from the service access subnet, DNS records for the appliance FQDN are valid, and no duplicate hostnames or IP addresses exist.
+ Verify that firewall rules allow HTTPS/SSH access to the management VM VLAN subnet and TCP/UDP access to DNS servers.
+ Ensure that the appliance is running and accessible.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.

## Entitlement status is `ENTITLEMENT_REMOVED`
<a name="troubleshoot-entitlement-removed"></a>

An entitlement with the `ENTITLEMENT_REMOVED` status indicates that Amazon EVS has removed the entitlement for the VM. When an entitlement is removed, Amazon EVS stops tracking Windows Server license usage for the affected VM.

**Note**  
Entitlements that remain in the `ENTITLEMENT_REMOVED` status for 90 days are automatically deleted.

The `ENTITLEMENT_REMOVED` status can result from the following scenarios:
+ vCenter connector reachability failure remained unresolved beyond the 8-hour grace period, so the entitlement moved from `AT_RISK` to `ENTITLEMENT_REMOVED`. For more information, see [Entitlement status is `AT_RISK`](#troubleshoot-entitlement-at-risk).
+ The VM is disconnected, orphaned, or inaccessible typically indicates an underlying host or network issue.
+ The VM is no longer present in the vCenter inventory.
+ The VM guest OS was changed to an unsupported version. Amazon EVS supports Windows Server 2016 or later.

To restore an entitlement, first check the error details of the entitlement to identify the specific cause of the removal. Then, based on the cause, do the following:

1. If the entitlement was removed due to vCenter reachability failure that exceeded the grace period, restore the vCenter Server connection.

1. If the entitlement was removed because the VM is disconnected, orphaned, or inaccessible, check the connection state of the VM in vCenter and resolve the underlying issue so that the VM returns to a compliant state. A VM can become disconnected if its host loses connection to vCenter and vSphere HA fails to recover the VM on another host. A VM can become orphaned because of storage connectivity issues or interrupted migrations.

1. If the entitlement was removed because the VM is no longer present in the vCenter inventory, restore the VM in vCenter.

1. If the entitlement was removed because the VM has an unsupported guest OS, update the guest OS to a supported version. Amazon EVS supports Windows Server 2016 or later.

After you resolve the underlying issue in your VCF environment, Amazon EVS validates the affected entitlements and automatically restores them shortly afterward. Entitlements resume from the time when EVS successfully validates that VMs have restored their compliance.

If you are still unable to resolve the issue after following this guidance, we recommend that you reach out to AWS Support for further assistance.