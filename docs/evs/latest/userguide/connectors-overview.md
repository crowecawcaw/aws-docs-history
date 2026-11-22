

# Manage connectors and credentials

An Amazon Elastic VMware Service connector lets Amazon EVS communicate with one VMware Cloud Foundation (VCF) management appliance in your environment. Amazon EVS uses connectors to stay in sync with your VCF deployment and to track Windows Server entitlements. A connector that stops working affects your environment health.

Each connector uses the fully qualified domain name (FQDN) of the appliance and credentials that you store in an AWS Secrets Manager secret. For a short definition, see [Amazon EVS connectors](concepts.md#concepts-connector).

## Connector types
<a name="connectors-overview-types"></a>

The following table lists the connector types and the deployment mode that uses each one.


| Connector type | VCF 9.x (Self-deployed) | VCF 5.2.x (EVS-deployed) | What Amazon EVS uses it for | 
| --- | --- | --- | --- | 
| Operations Manager (`OPERATIONS_MANAGER`) | Required | Not available | Connects to VCF Operations to stay in sync with your VMware deployment and to monitor vSAN capacity. | 
| SDDC Manager (`SDDC_MANAGER`) | Not available | Required | Connects to SDDC Manager to validate host counts and license key coverage, and to monitor vSAN capacity. | 
| vCenter (`VCENTER`) | Optional | Optional | Connects to vCenter Server to monitor VM lifecycle events for entitled VMs. You need it for Windows Server entitlements. For more information, see [Windows Server entitlements](entitlements.md). | 

The VCF Operations and SDDC Manager connectors are the management connectors. Each environment needs the management connector for its mode.

## Reachability checks and environment health
<a name="connectors-overview-health"></a>

Amazon EVS runs a reachability check against each appliance through its connector. The check runs every 10 minutes after the connector becomes `ACTIVE`, and its status is `PASSED`, `FAILED`, or `UNKNOWN`.
+ If the management connector isn’t created or loses reachability, Amazon EVS reports impaired environment health through AWS Health notifications. For the SDDC Manager connector (VCF 5.2.x), Amazon EVS also can’t validate host counts and license key coverage. For more information, see [Monitor environment status](evs-env-status-check.md).
+ If the vCenter connector loses reachability, the Windows Server entitlements that depend on it enter the `AT_RISK` status. If you don’t restore reachability within 8 hours, Amazon EVS removes the entitlements. For more information, see [Troubleshoot Windows Server entitlements](troubleshoot-entitlements.md).

A reachability check can fail when the password of the connector user changes or expires in VCF but the secret still holds the old password. To avoid this, update the secret whenever you change the credentials of the connector user. For the steps, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).

## Connector and credential tasks
<a name="connectors-overview-tasks"></a>
+ To create a connector of any type, see [Create a connector](evs-env-create-connector.md).
+ To change the appliance FQDN or the secret of a connector, see [Update a connector](evs-env-update-connector.md).
+ To delete a connector, see [Delete a connector](evs-env-delete-connector.md).
+ To give a vCenter connector new credentials after you rotate them in vCenter Server, see [Rotate vCenter connector credentials](rotate-vcenter-credentials.md).
+ To learn which secrets Amazon EVS creates and who rotates them, see [Manage secrets](evs-env-secret-rotation.md).

**Topics**