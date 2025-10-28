AWS Systems Manager Incident Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Incident Manager,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Incident Manager availability change](incident-manager-availability-change.md "incident-manager-availability-change.md").

# AWS Systems Manager Incident Manager availability

change

After careful consideration, AWS has made the decision to stop accepting new customers to
AWS Systems Manager Incident Manager beginning on November 7, 2025, and will no longer be adding any new
features or capabilities to Incident Manager going forward. AWS will continue investing in the
security and availability of Incident Manager, and existing Incident Manager customers will be able to
continue using the service as normal in accounts where Incident Manager is already enabled.

As Incident Manager will no longer be adding new features or capabilities, it’s important for you
to understand your alternatives for incident management. For managing operational issues on your
AWS infrastructure, we recommend you use [AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md"). For
automated paging and response capabilities, we recommend solutions offered by our AWS Partner
Network partners. AWS Solution Architects and Technical Account Managers will be able to guide
you to the most suitable option based on your specific requirements. The following sections
provide guidance on how you can migrate your incident management from Incident Manager to
OpsCenter.

## Migrating Amazon CloudWatch Alarms and EventBridge Rules to AWS Systems Manager

OpsCenter

[AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md"), a capability of AWS Systems Manager, provides a central location where
operations engineers and IT professionals can view, investigate, and resolve operational work
items (OpsItems) related to AWS resources. OpsCenter is designed to reduce mean time to
resolution (MTTR) for issues impacting AWS resources. OpsCenter aggregates and standardizes
OpsItems across services while providing contextual investigation data about each OpsItem,
related OpsItems, and related resources. OpsCenter integrates with Systems Manager Automation, allowing
you to use Automation runbooks to investigate and resolve issues. You can view
automatically-generated summary reports about OpsItems by status and source. You can also use
[OpsCenter’s
cross-account](../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md "../../../systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.md") capability to centrally manage OpsItems across accounts. Note that
there are charges associated with the OpsCenter use. Please refer to the [AWS Systems Manager pricing page](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/") for more
details.

Similar to Incident Manager, OpsCenter has integrations with Amazon CloudWatch and Amazon EventBridge. This means
you can configure these services to automatically create an OpsItem in OpsCenter when a CloudWatch
alarm enters the `ALARM` state or when EventBridge processes an event from any
AWS service that publishes events. Configuring CloudWatch alarms and EventBridge events to automatically
create OpsItems allows you to quickly diagnose and remediate issues with AWS resources from
a single console. If you have existing CloudWatch Alarms and EventBridge Rules integrated with Incident Manager,
we recommend updating your CloudWatch Alarms and EventBridge Rules to integrate with OpsCenter. Please
visit our technical documentation for detailed instructions on [integrating CloudWatch alarms with OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") or [integrating EventBridge events with OpsCenter](../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md "../../../systems-manager/latest/userguide/OpsCenter-automatically-create-OpsItems-2.md").

For additional support, you can contact your Technical Account Manager or [create a support case
in the Support Center](../../../awssupport/latest/user/case-management.md "../../../awssupport/latest/user/case-management.md") of the AWS Management Console.
