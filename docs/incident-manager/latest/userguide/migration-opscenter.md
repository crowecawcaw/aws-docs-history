AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# Migrating to AWS Systems Manager

OpsCenter

[AWS Systems Manager
OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md"), a capability of AWS Systems Manager, provides a central location where operations
engineers and IT professionals can view, investigate, and resolve operational work items
(OpsItems) related to AWS resources. OpsCenter is designed to reduce mean time to resolution
(MTTR) for issues impacting AWS resources. OpsCenter aggregates and standardizes OpsItems
across services while providing contextual investigation data about each OpsItem, related
OpsItems, and related resources. OpsCenter integrates with Systems Manager Automation, allowing you to use
Automation runbooks to investigate and resolve issues. You can view automatically-generated
summary reports about OpsItems by status and source. You can also use [OpsCenter's
cross-account](../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md "../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md") capability to centrally manage OpsItems across accounts. Note that there
are charges associated with the OpsCenter use. Please refer to the [AWS Systems Manager pricing page](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/") for more details.

Similar to Incident Manager, OpsCenter has integrations with Amazon CloudWatch and Amazon EventBridge. This means
you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch
alarm enters the `ALARM` state or when EventBridge processes an event from any
AWS service that publishes events. Configuring CloudWatch alarms and EventBridge events to automatically
create OpsItems allows you to quickly diagnose and remediate issues with AWS resources from a
single console. If you have existing CloudWatch Alarms and EventBridge Rules integrated with Incident Manager, we
recommend updating your CloudWatch Alarms and EventBridge Rules to integrate with OpsCenter. Please visit our
technical documentation for detailed instructions on [integrating CloudWatch alarms with OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") or [integrating EventBridge events with OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md "../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md").
