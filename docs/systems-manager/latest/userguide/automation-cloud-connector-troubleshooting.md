

# Troubleshooting automations that use a Cloud Connector

Use the following information to troubleshoot problems when you run an automation against Microsoft Azure or Google Cloud resources through a Cloud Connector. For the target value fields referenced here, see [Cloud Connector target reference](automation-cloud-connector-target.md). Error messages name these fields in camelCase, for example `azureSubscriptions` for `AzureSubscriptions`. For the permissions referenced here, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

## TargetParameterName must be specified
<a name="automation-cloud-connector-troubleshooting-tpn"></a>

**Error message**: `TargetParameterName must be specified for rate control.`

A Cloud Connector target uses rate control, which requires a `TargetParameterName`. Set `TargetParameterName` to the runbook input that receives each resource ID.

## Only one target can be specified
<a name="automation-cloud-connector-troubleshooting-onetarget"></a>

**Error message**: `Only one target can be specified for rate control.`

A Cloud Connector target must be the only entry in `Targets`. Provide a single target whose `Key` is `CloudConnector`.

## Targets and TargetMaps can't both be specified
<a name="automation-cloud-connector-troubleshooting-targetmaps"></a>

**Error message**: `Both Targets and TargetMaps cannot be specified for rate control.`

A Cloud Connector target can't be combined with `TargetMaps`. Remove `TargetMaps` and use only the `CloudConnector` target.

## A single CloudConnector value must be provided
<a name="automation-cloud-connector-troubleshooting-singlevalue"></a>

**Error message**: `A single CloudConnector value must be provided`

The `CloudConnector` target's `Values` must contain exactly one string: either a connector ID or a JSON object as a string. Provide one value.

## An error occurred reading the provided CloudConnector
<a name="automation-cloud-connector-troubleshooting-reading"></a>

**Error message**: `An error occurred reading the provided CloudConnector: {{error-code}}: {{message}}`

Automation couldn't read the connector. Check the following causes:
+ The caller doesn't have `ssm:GetCloudConnector` permission.
+ The connector ID or the AWS Region is wrong.
+ The target value is malformed JSON, so Automation used the whole string as a connector ID. Correct the JSON, or provide only the connector ID.

## Unable to assume role for cloud connector
<a name="automation-cloud-connector-troubleshooting-assume"></a>

**Error message**: `Unable to assume role {{arn}} for cloud connector: {{message}}`

The role can't assume the connector's federation role, usually because the federation role doesn't trust the role. The federation role that connector setup creates trusts the roles that you chose under **Additional trusted roles** when you created the connector, and the roles that you add to its trust policy. It also trusts roles whose name starts with `SSM-AzureAssumeRole` or `SSM-GCPAssumeRole`, whose path is `/service-role/`, and that have the tag `caller=SSM`. Such a role must also allow `sts:AssumeRole` on the federation role. If the execution has no `AutomationAssumeRole`, the federation role must trust your own identity instead. A runbook that uses both an Azure connector and a Google Cloud connector fails this way unless both federation roles trust its role.

To create a role that meets the name, path, and tag conditions, see [Create the automation assume role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-create-role). To use another role, see [Use another role](automation-cloud-connector-permissions.md#automation-cloud-connector-permissions-other-role).

## A subscription isn't in the connector
<a name="automation-cloud-connector-troubleshooting-subscription"></a>

**Error message**: `A subscription in azureSubscriptions is not in the CloudConnector`

A value in `AzureSubscriptions` isn't one of the connector's subscriptions. When the connector lists subscriptions, each value must be one of them. Remove the value, or use a connector whose scope includes it.

## Invalid subscription IDs
<a name="automation-cloud-connector-troubleshooting-subid"></a>

**Error message**: `Invalid value found for azureSubscriptions. Use subscription ids`

A value in `AzureSubscriptions` isn't a valid subscription ID (GUID). Provide subscription IDs as GUIDs, for example `11111111-2222-3333-4444-555555555555`.

## A project isn't in the connector
<a name="automation-cloud-connector-troubleshooting-project"></a>

**Error message**: `A project in gcpProjects is not in the CloudConnector`

A value in `GcpProjects` isn't one of the connector's projects. Each value must be one of the connector's projects.

## GcpProjects with an organization connector
<a name="automation-cloud-connector-troubleshooting-gcpprojects"></a>

**Error message**: `gcpProjects can't be used with a CloudConnector that lists no projects`

The connector covers an organization and lists no projects, so you can't restrict it with `GcpProjects`. Remove `GcpProjects`, or use a connector that lists projects.

## Zones in CloudProviderRegions
<a name="automation-cloud-connector-troubleshooting-zones"></a>

**Error message**: `Specify GCP zones in zones only, not also in cloudProviderRegions`

For Google Cloud, specify zones in `Zones` and don't also send `CloudProviderRegions`. A region name such as `us-central1` matches nothing. Use a zone such as `us-central1-a`.

## OS policy orchestrator missing
<a name="automation-cloud-connector-troubleshooting-orchestrator"></a>

**Error message**: `osPolicyOrchestratorName or osPolicyOrchestratorId is required when osPolicyComplianceFilter is SKIP_COMPLIANT`

You set `OsPolicyComplianceFilter` to `SKIP_COMPLIANT` without an orchestrator. Provide `OsPolicyOrchestratorId` or `OsPolicyOrchestratorName`.

## Google Cloud tags are too large
<a name="automation-cloud-connector-troubleshooting-tags"></a>

**Error message**: `The tags on role {{arn}} are too large to include in a federation token. Reduce the number or length of tags on that role and retry: {{message}}`

The automation assume role has too many tags for the Google Cloud federation token. Remove tags from the role to keep its tags few.

## AuthorizationFailed in an Azure step
<a name="automation-cloud-connector-troubleshooting-authfailed"></a>

**Error message**: `AuthorizationFailed`

A step called an Azure operation that the connector's Azure application isn't allowed to perform. The connector's application has only the `AWSSSMVMExtensionRole-*` role, which reads VMs and runs commands. Assign another Azure role to the connector's Azure application. For more information, see [Permissions for automations that use a Cloud Connector](automation-cloud-connector-permissions.md).

## The automation started but ran no child automations
<a name="automation-cloud-connector-troubleshooting-nochildren"></a>

The target matched no resources, so the execution starts and runs no child automations. Check the following causes:
+ The target matches only running VMs by default. To include VMs in other states, set the VM state fields.
+ A field name is misspelled, so the target ignores the field and covers different resources than you intended. Check the spelling of each field name.
+ A Google Cloud target uses a region name, such as `us-central1`, where a zone is required. Use a zone, such as `us-central1-a`.
+ The filters are too narrow. Remove or widen filters until they match the resources that you want.

## Input validation fails for Azure IDs
<a name="automation-cloud-connector-troubleshooting-inputpattern"></a>

Automation passes Azure resource IDs to the runbook in lowercase, for example `/subscriptions/11111111-2222-3333-4444-555555555555/resourcegroups/my-resource-group/providers/microsoft.compute/virtualmachines/my-vm`. If the input's `allowedPattern` rejects lowercase, validation fails. Make the input's `allowedPattern` accept lowercase, for example by starting it with `(?i)`.

## Multi-account and Region isn't available
<a name="automation-cloud-connector-troubleshooting-mar"></a>

The **Multi-account and Region** execution mode supports AWS targets only, so the console hides it for a runbook whose cloud providers don't include AWS, or that has a Cloud Connector input. If a link opens it for such a runbook, the console switches to Simple execution and shows **Execution mode changed to Simple execution**. Use a Cloud Connector target in Simple execution, Rate control, or Manual execution instead.

## Parameter type is invalid
<a name="automation-cloud-connector-troubleshooting-paramtype"></a>

**Error message**: `Parameter type: {{type}} is invalid.`

A runbook declared a parameter type that doesn't match a supported type string. Type strings are matched exactly, including their mixed casing. Check the casing against [Parameter types for Azure and Google Cloud resources](automation-multicloud-parameter-types.md).