

# Cloud Connector target reference

A Cloud Connector target has exactly one entry. Its `Key` is `CloudConnector` (case-sensitive), and its `Values` list has one string. Use this reference to build that string and to understand how Automation matches Microsoft Azure and Google Cloud resources.

## Target value formats
<a name="automation-cloud-connector-target-formats"></a>

The target value is one of the following:
+ A connector ID alone, for example `a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`. Automation finds the default resources that the connector covers.
+ A JSON object, as a string, with the fields in the following table. If the string isn't valid JSON, Automation uses the whole string as the connector ID.

## Target value fields
<a name="automation-cloud-connector-target-fields"></a>

Write the field names in PascalCase, as shown. The following table lists every field.


| Field | Cloud | Values | Default | 
| --- | --- | --- | --- | 
| `CloudConnectorId` | Both | The connector ID. Required. | None | 
| `SsmManagedNodeFilter` | Both, VMs only | `ALL`, `MANAGED`, or `UNMANAGED`. `MANAGED` matches VMs that are registered with Systems Manager and online. `UNMANAGED` matches VMs that aren't registered, or are registered but not online. | `ALL` | 
| `CloudProviderRegions` | Azure | Azure region names, letters and numbers only, for example `eastus`. Case-insensitive. | All regions | 
| `Zones` | Google Cloud, VMs only | Zone names, for example `us-central1-a`. A region name such as `us-central1` matches nothing. Letters, numbers, and hyphens. | All zones | 
| `AzureSubscriptions` | Azure | Subscription IDs (GUIDs). If the connector lists subscriptions, each must be one of them. | The connector's scope | 
| `AzureResourceGroups` | Azure | Resource group names, case-insensitive. Each name has up to 90 letters, numbers, `_`, `-`, `.`, `(`, and `)`, and can't end with `.`. | All | 
| `AzureResourceType` | Azure | One Azure resource type, for example `Microsoft.Compute/virtualMachines` or `Microsoft.Storage/storageAccounts`. Case-insensitive match. | `Microsoft.Compute/virtualMachines` | 
| `AzureTag` | Azure | One object `{"Key": "Env", "Value": "prod"}`. Omit `Value` to match any value. Key and value case-insensitive. Key up to 512 characters, value up to 256. | None | 
| `AzureVmPowerStates` | Azure, VMs only | List of `STARTING`, `RUNNING`, `STOPPING`, `STOPPED`, `DEALLOCATING`, `DEALLOCATED` (any case) | `["RUNNING"]` | 
| `GcpProjects` | Google Cloud | Project IDs. Each must be one of the connector's projects. You can't use this field for a connector that lists no projects. | The connector's scope | 
| `GcpAssetType` | Google Cloud | One asset type, for example `compute.googleapis.com/Disk` (lowercase service name, then a kind that starts with an uppercase letter) | `compute.googleapis.com/Instance` | 
| `GcpInstanceStates` | Google Cloud, VMs only | List of `PROVISIONING`, `STAGING`, `RUNNING`, `STOPPING`, `SUSPENDING`, `SUSPENDED`, `REPAIRING`, `TERMINATED` (any case) | `["RUNNING"]` | 
| `IncludesLabels` | Google Cloud | Object of label key to value, for example `{"env": "prod"}`. `""` or `"*"` means the key only has to be present. All entries must match. Keys and values up to 63 lowercase letters, numbers, `_`, `-`. | None | 
| `ExcludesLabels` | Google Cloud | List of label keys. A resource with any of them is skipped. | None | 
| `OsPolicyComplianceFilter` | Google Cloud, VMs only | `ALL` or `SKIP_COMPLIANT` (skip VMs where every OS policy assignment report is compliant) | `ALL` | 
| `OsPolicyOrchestratorId` | Google Cloud | Required with `SKIP_COMPLIANT` (or `OsPolicyOrchestratorName`). 1 to 63 lowercase letters, numbers, and hyphens. The orchestrator is looked up under the connector's organization, or its home project. | None | 
| `OsPolicyOrchestratorName` | Google Cloud | Alternative to the ID: `organizations/<id>/locations/global/policyOrchestrators/<id>` or `projects/<number>/locations/global/policyOrchestrators/<id>`. Takes precedence over the ID. | None | 

## Matching rules
<a name="automation-cloud-connector-target-matching"></a>
+ The VM-only filters (`SsmManagedNodeFilter` other than `ALL`, the VM state fields, `Zones`, and `OsPolicyComplianceFilter`) are rejected for non-VM resource types.
+ Misspelled field names are ignored. The run then covers more resources than you intended.
+ Fields for the other cloud are ignored.
+ Automation also accepts each field name in camelCase, for example `cloudConnectorId`. The Automation console writes this form, and error messages use it. Don't use other capitalizations.

The console's **VM state** options map to these values:
+ For Azure, **Running** is `RUNNING`. **Stopped** is `STOPPED` and `DEALLOCATED`, so it includes deallocated VMs. **Running and stopped** is all three.
+ For Google Cloud, **Stopped** is `TERMINATED` and `SUSPENDED`, so it includes suspended VMs.

## Examples
<a name="automation-cloud-connector-target-examples"></a>

The following target value finds managed, running, and stopped VMs in one Azure subscription and resource group that have the tag `Env=prod`.

```json
{
    "CloudConnectorId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "AzureSubscriptions": ["11111111-2222-3333-4444-555555555555"],
    "AzureResourceGroups": ["my-resource-group"],
    "AzureResourceType": "Microsoft.Compute/virtualMachines",
    "AzureTag": { "Key": "Env", "Value": "prod" },
    "AzureVmPowerStates": ["RUNNING", "STOPPED"],
    "SsmManagedNodeFilter": "MANAGED",
    "CloudProviderRegions": ["eastus"]
}
```

The following target value finds running VMs in one Google Cloud project and zone that have the label `env=prod`, and skips VMs that are already OS policy compliant.

```json
{
    "CloudConnectorId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "GcpProjects": ["my-project"],
    "Zones": ["us-central1-a"],
    "GcpInstanceStates": ["RUNNING"],
    "IncludesLabels": { "env": "prod" },
    "ExcludesLabels": ["temp"],
    "OsPolicyComplianceFilter": "SKIP_COMPLIANT",
    "OsPolicyOrchestratorId": "my-orchestrator"
}
```

## Validation errors
<a name="automation-cloud-connector-target-errors"></a>

If the target or its value is invalid, the `StartAutomationExecution` request fails with one of the following messages. The messages name the fields in camelCase, for example `cloudProviderRegions` for `CloudProviderRegions`.


| Error message | How to fix it | 
| --- | --- | 
| TargetParameterName must be specified for rate control. | Add the --target-parameter-name option. Rate control requires it. | 
| Only one target can be specified for rate control. | Use a single target whose Key is CloudConnector. | 
| Both Targets and TargetMaps cannot be specified for rate control. | Remove TargetMaps. A Cloud Connector target uses Targets only. | 
| Specify GCP zones in zones only, not also in cloudProviderRegions | For Google Cloud, remove CloudProviderRegions and use Zones. | 
| gcpProjects can't be used with a CloudConnector that lists no projects | Remove GcpProjects. The connector already covers its whole organization. | 