# AMS Patch Orchestrator: a tag-based patching model

If you have been onboarded to the new AMS Patch Orchestrator tag-based patching
model, you can use tags to apply your patch configuration to a precise set of resources,
called a _patch group_, ranging from one instance to
all of your instances. For information about AMS tags, see
[Using tags](ex-using-tags.md "ex-using-tags.md").
Instructions on setting up Patch Orchestrator tags are provided in the following section.

Patches are installed during the patch windows you define with the
[SSM Patch Window | Create](../ctref/deployment-patching-ssm-patch-window-create.md "../ctref/deployment-patching-ssm-patch-window-create.md").
Each patch window is an AWS Systems Manager maintenance window that runs on a schedule
of your choice, has a configured duration, and applies to one patch group. Instances
that are not part of an explicit patch window are patched during the default maintenance
window that you define when you onboard to Patch Orchestrator.

###### Important

If multiple patch maintenance windows are scheduled to run at the same time, they
must have fewer than 1001 instances being processed at any given time. This is an
AWS Systems Manager limitation. AMS recommends at least one hour per every fifty instances.

By default, all operating system (OS) vendor-provided patches are installed during a maintenance window
or an on-demand patch. This is called the _default patch baseline_.
If you would like to restrict which patches are installed, you can define a custom patch baseline with one of the patch baseline create CTs (per OSes), see
[Patching subcategory](edeployment-patching-section.md "edeployment-patching-section.md").
For example, you can use a custom patch baseline so that only critical and important security
updates are installed for one or more patch groups.

After patches are installed on an instance, the instance is rebooted. Patch
notifications are sent before and after patching, and an additional reminder is sent
within 96 hours before the scheduled start. In addition, AMS applies updates to
infrastructure management tools (such as the AWS SSM agent) during the selected maintenance window.

###### Important

AMS is deprecating the monthly patch compliance reporting of instances with
missing patches, and will not be sending monthly reports. This change has been made in view of the recently
released self-serve operational reports that refresh every 24 hours and are available to you on demand
and provide the most recent and granular data. To learn more about the reports, see Self-service reporting.
To learn more about the reports, see
[Self-service reports](self-service-reporting.md "self-service-reporting.md").

For more information on the notifications, see
[Patch notifications](patch-notifications.md "patch-notifications.md").
