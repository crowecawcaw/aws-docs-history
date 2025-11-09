# Using Patch Orchestrator

Enable AMS Patch Orchestrator for your account by submitting a service request that includes the following details:

- **Category**: Other
- **Subject**: Onboard to Patch Orchestrator
- **CC Emails**: CC email addresses receive notifications when the status of this onboarding RFC changes
- **Details**: Paste the following information into the
  email and provide your values. Note that the ThirdTagKey is optional. For
  recommendations and examples, see the following table.

```
Default maintenance window Schedule:
Default Maintenance Window Schedule TimeZone:
Default Maintenance Window Duration:
Default Maintenance Window Cutoff:
Default Patch Backup Retention In Days:
Default Maintenance Window Notification Emails:
First Tag Key:
Second Tag Key:
Third Tag Key:
```

The following table describes the format and recommendations for your provided
values.

| Patch orchestrator tag-based patching configurations | Name of parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Information                                                                                                                  | Recommendation or example |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Default Maintenance Window Schedule                  | The schedule of the default maintenance window in the form of a cron or rate expression. For example:<br>• `cron(0 3 ? * 6L *)`: 03:00 am on the last Friday of every month<br>• `rate(7 days)`: Every seven days<br>For more information about creating cron expressions, and links to cron and rate expression resources, see<br>[Cron and rate expressions for maintenance windows](../../../systems-manager/latest/userguide/reference-cron-and-rate-expressions.md#reference-cron-and-rate-expressions-maintenance-window "../../../systems-manager/latest/userguide/reference-cron-and-rate-expressions.md#reference-cron-and-rate-expressions-maintenance-window"). | We recommend having the window run at least once per month on a consistent weekday.                                          |
| Default Maintenance Window Schedule Time Zone        | The time zone that the default maintenance window runs<br>are based on, in Internet Assigned Numbers Authority (IANA) format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | For example:<br>• America/Los_Angeles<br>• etc/UTC                                                                           |
| Default Maintenance Window Duration                  | The duration of the default maintenance window in hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | At least 1 hour per every 50 instances, plus 2 hours for cutoff.                                                             |
| Default Maintenance Window Cutoff                    | The number of hours before the end of the Default Maintenance<br>Window in which no new patching commands are started. This<br>interval exists to allow enough time for patching to complete<br>before the window ends.                                                                                                                                                                                                                                                                                                                                                                                                                                                    | At least 2 hours.                                                                                                            |
| Default Patch Backup Retention In Days (optional)    | The default time in days to keep the EBS restore points created before patching<br>instances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | We recommend keeping the default, which is 60.                                                                               |
| Default Maintenance Window Notification Emails       | One to five email addresses or distribution lists to receive<br>notifications about default maintenance window patching status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | We recommend using group distribution lists instead of individual emails.                                                    |
| First Tag Key                                        | The first tag-key to use for creating your Patch Group tag values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | For example, AppId. Specify \*_null_<br>• if you already have defined your own patch<br>groups with a Patch Group tag.       |
| Second Tag Key                                       | The second tag-key to use for creating your Patch Group tag values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | For example, Environment. Specify \*_null_<br>• if you have already defined your own patch<br>groups with a Patch Group tag. |
| Third Tag Key (optional)                             | The optional third tag-key to use for creating your Patch Group tag values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | For example, Group.                                                                                                          |

After you're onboarded to the new Patch Orchestrator patching service model, all
appropriately tagged instances in your account belong to a patch group with a Patch
Group tag. Patch Orchestrator uses either your existing Patch Group tag, or an
AMS-created tag consisting of the two or three concatenated tag values that you
specified during Patch Orchestrator onboarding. For example, {`Tag Value
 1`}-{`Tag Value 2`}-{`Tag
 Value 3`}. AMS updates these AMS-applied Patch Group tags
every 12 hours. If needed, you can update your Patch Group tag values with the
[Tag | Update (Managed automation)](../ctref/management-advanced-tag-update-review-required.md "../ctref/management-advanced-tag-update-review-required.md") or
[Tag | Update (Managed automation)](../ctref/management-advanced-tag-update-review-required.md "../ctref/management-advanced-tag-update-review-required.md") change types.

For example, if your Amazon EC2 instance has the following tag key:value pairs:

- `AppId:MyApplication`
- `Environment:Production`
- `Group:1`
  During onboarding you specified the following tag keys:

- `First Tag Key = AppId`
- `Second Tag Key = Environment`
- `Third Tag Key = Group`
  AMS creates the following Patch Group tag and applies it to your instances:
  `Patch Group:MyApplication-Production-1`.

###### Note

Patch failure alerts aren't created for instances that have unsupported operating systems, or that are stopped during the maintenance window.

## Patch Orchestrator prerequisites

Patch Orchestrator workflow targets Amazon EC2 instances that are patched by latest version of
System Manager Automation Document: AWSManagedServices-PatchInstanceFromMaintenanceWindow.

As part of the document workflow, the run command document "AWS-RunPatchBaseline" is run
against each of the Amazon EC2 instances out of patch group members. To learn more, see
[About the SSM document AWS-RunPatchBaseline](../../../systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.md "../../../systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.md").

**Requirements**:

- Amazon EC2 instance deployed from AMS-provided Amazon Machine Image (AMI), or on an AMI through the
  "Stack from migration partner migrated instance" CT
  (ct-257p9zjk14ija).
- Egress internet connection enabled. For firewall/proxy solutions the requirement is to allow
  Windows update endpoint and/or Linux repository mirror endpoints, AWS
  system manager proxy settings, and metadata proxy configuration. For more information, see
  [Configure SSM Agent to use a proxy](../../../systems-manager/latest/userguide/sysman-proxy-with-ssm-agent.md "../../../systems-manager/latest/userguide/sysman-proxy-with-ssm-agent.md") and
  [Using an HTTP proxy](../../../cli/latest/userguide/cli-configure-proxy.md "../../../cli/latest/userguide/cli-configure-proxy.md")
- IAM role matching minimum permissive access for the SSM service of
  `customer-mc-ec2-instance-profile` IAM role.
- We recommend 10 GB available root partition space. For Linux OS, at least 2 GB available in the
  `/var` partition.
- Working and valid Certificate Authority for update downloads.
- Windows Server Update Services (WSUS) - Registry including but not limited to:
  DisableWindowsUpdateAccess, NoWindowsUpdate; Automatic Updates must not impair operation of
  Windows Update process.

**Validation**:

- For Linux OS instances using yum package manager you can validate availability
  of updates by running `#yum check-update`
- For Linux OS RedHat 5.7 and newer, 6.1 and newer, and 7.0 and newer;
  Amazon EC2 instances migrated to your AMS account via the "Stack from migration partner migrated instance"
  CT (ct-257p9zjk14ija), you need to validate subscription manager status for
  update performance.
- On Windows OS, enable Windows Server Update Services (WSUS).
  No local policy should block WSUS ability to scan or install updates. Once logged as
  administrator you can validate it by performing a scan for available updates from
  Windows Update Service console. Windows Server OS releases including 2012R2, 2016 and 2019 have
  default Windows Update settings to download and install. You can configure desired
  settings prior to scan. On later releases of OS, this operation can trigger installation;
  configure desired behavior beforehand.
- Request validation from the AMS Operations team by submitting a service request:
  "AWSManagedServices-CheckPatchingPrerequisites Automation document to run against Amazon EC2 instance
  for assessment of patch readiness."

###### Note

Patch failure alerts aren't created for instances that have unsupported operating systems, or that are stopped during the maintenance window.

## Patch Orchestrator reserved tags

Patch Orchestrator also generates the following tags that can't be
modified:

- **AMSPatchGroup** – This tag is used for Patch
  Group tag value generation. You shouldn't modify the AMSPatchGroup. You
  can modify the "Patch Group" tag if you want to use a custom "Patch
  Group" value. Patch Orchestrator continues generating a value for
  AMSPatchGroup based on the tag-keys provided during onboarding, but
  won't modify the "Patch Group" tag value if it has been set to a custom
  value by you. To stop using a custom "Patch Group" value, you can set
  the value of "Patch Group" to match the AMSPatchGroup tag value.
- **AMSDefaultPatchGroup** – This tag indicates
  whether an instance is part of the default maintenance window, with a
  value of either True or False. If an instance's Patch Group is not
  assigned to a maintenance window this value is set to True.
