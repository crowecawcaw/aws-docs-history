# Troubleshooting assessment and evidence

collection issues

You can use the information on this page to resolve common assessment and evidence
collection issues in Audit Manager.

###### Evidence collection issues

- [I created an
  assessment but I can’t see any evidence yet](#no-evidence-yet "#no-evidence-yet")
- [My assessment isn’t collecting compliance check evidence
  from AWS Security Hub CSPM](#no-evidence-from-security-hub "#no-evidence-from-security-hub")
- [My
  assessment isn’t collecting compliance check evidence from AWS Config](#no-evidence-from-config "#no-evidence-from-config")
- [My assessment isn’t collecting user activity evidence from
  AWS CloudTrail](#no-evidence-from-cloudtrail "#no-evidence-from-cloudtrail")
- [My assessment isn’t collecting configuration data
  evidence for an AWS API call](#no-evidence-from-aws-api-calls "#no-evidence-from-aws-api-calls")
- [A
  common control isn’t collecting any automated evidence](#manual-common-control "#manual-common-control")
- [My evidence is generated at different intervals, and I'm
  not sure how often it’s being collected](#evidence-collection-frequency "#evidence-collection-frequency")
- [I disabled and then re-enabled Audit Manager,
  and now my pre-existing assessments are no longer collecting evidence](#no-evidence-from-preexisting-assessments-after-reregistering "#no-evidence-from-preexisting-assessments-after-reregistering")
- [On my assessment details page, I’m prompted to recreate
  my assessment](#recreate-assessment-post-common-controls "#recreate-assessment-post-common-controls")
- [What’s the
  difference between a data source and an evidence source?](#data-source-vs-evidence-source "#data-source-vs-evidence-source")

###### Assessment issues

- [My assessment
  creation failed](#assessment-creation-failed "#assessment-creation-failed")
- [What
  happens if I remove an in-scope account from my organization?](#what-happens-if-account-is-removed "#what-happens-if-account-is-removed")
- [I can't see the
  services in scope for my assessment](#unable-to-view-services "#unable-to-view-services")
- [I can't edit the
  services in scope for my assessment](#unable-to-edit-services "#unable-to-edit-services")
- [What's the
  difference between a service in scope and a data source type?](#data-source-vs-service-in-scope "#data-source-vs-service-in-scope")

## I created an

assessment but I can’t see any evidence yet

If you can't see any evidence, it's likely that you either didn't wait at least 24
hours after you created the assessment or that there's a configuration error.

We recommend that you check the following:

1. Make sure that 24 hours passed since you created the assessment. Automated
   evidence becomes available 24 hours after you create the assessment.
2. Make sure that you’re using Audit Manager in the same AWS Region as the
   AWS service that you’re expecting to see evidence for.
3. If you expect to see compliance check evidence from AWS Config and
   AWS Security Hub CSPM, make sure that both the AWS Config and Security Hub CSPM consoles display results
   for these checks. The AWS Config and Security Hub CSPM results should display in the same
   AWS Region that you use Audit Manager in.

If you still can't see evidence in your assessment and it's not due to one of
these issues, check the other potential causes that are described on this page.

## My assessment isn’t collecting compliance check evidence

from AWS Security Hub CSPM

If you don't see compliance check evidence for an AWS Security Hub CSPM control, this could be
due to one of the following issues.

**Missing configuration in AWS Security Hub CSPM**

This issue can be caused if you missed some configuration steps when
you enabled AWS Security Hub CSPM.

To fix this issue, make sure that you enabled Security Hub CSPM with the required
settings for Audit Manager. For instructions, see [Enable and set up AWS Security Hub CSPM](setup-recommendations.md#securityhub-recommendations "setup-recommendations.md#securityhub-recommendations").

**A Security Hub CSPM control name was entered incorrectly in your
`ControlMappingSource`**

When you use the Audit Manager API to create a custom control, you can specify
a Security Hub CSPM control as a [data source mapping](../APIReference/API_ControlMappingSource.md "../APIReference/API_ControlMappingSource.md") for evidence collection. To do this,
you enter a control ID as the [`keywordValue`](../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue "../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue").

If you don't see compliance check evidence for a Security Hub CSPM control, it
could be that the `keywordValue` was entered incorrectly in
your `ControlMappingSource`. The `keywordValue` is
case sensitive. If you enter it incorrectly, Audit Manager might not recognize
that rule. As a result, you might not collect compliance check evidence
for that control as expected.

To fix this issue, [update the custom control](../APIReference/API_UpdateControl.md "../APIReference/API_UpdateControl.md") and revise the
`keywordValue`. The correct format of a Security Hub CSPM keyword
varies. For accuracy, reference the list of [Supported Security Hub CSPM
controls](control-data-sources-ash.md#security-hub-controls-for-custom-control-data-sources "control-data-sources-ash.md#security-hub-controls-for-custom-control-data-sources") .

**`AuditManagerSecurityHubFindingsReceiver`
Amazon EventBridge rule is missing**

When you enable Audit Manager, a rule named
`AuditManagerSecurityHubFindingsReceiver` is
automatically created and enabled in Amazon EventBridge. This rule enables Audit Manager to
collect Security Hub CSPM findings as evidence.

If this rule isn't listed and enabled in the AWS Region where you
use Security Hub CSPM, Audit Manager can't collect Security Hub CSPM findings for that Region.

To resolve this issue, go to the [EventBridge console](https://console.aws.amazon.com/events "https://console.aws.amazon.com/events") and confirm that the
`AuditManagerSecurityHubFindingsReceiver` rule exists in
your AWS account. If the rule doesn't exist, we recommend that you
[disable
Audit Manager](disable.md "disable.md") and then re-enable the service. If this action doesn’t
resolve the issue, or if disabling Audit Manager isn’t an option, [contact Support](https://aws.amazon.com/contact-us "https://aws.amazon.com/contact-us") for
assistance.

**Service-linked AWS Config rules created by
Security Hub CSPM**

Keep in mind that Audit Manager doesn’t collect evidence from the [service-linked AWS Config rules that
Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md "../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md") creates. This is a specific type of managed AWS Config rule
that's enabled and controlled by the Security Hub CSPM service. Security Hub CSPM creates
instances of these service-linked rules in your AWS environment, even
if other instances of the same rules already exist. As a result, to
prevent evidence duplication, Audit Manager doesn’t support evidence collection
from the service-linked rules.

## I disabled a security

control in Security Hub CSPM. Does Audit Manager collect compliance check evidence for that security
control?

Audit Manager doesn't collect evidence for disabled security controls.

If you set the status of a security control to [disabled](../../../securityhub/latest/userguide/controls-overall-status.md#controls-overall-status-values "../../../securityhub/latest/userguide/controls-overall-status.md#controls-overall-status-values") in Security Hub CSPM, no security checks are performed for that control in
the current account and Region. As a result, no security findings are available in
Security Hub CSPM, and no related evidence is collected by Audit Manager.

By respecting the disabled status that you set in Security Hub CSPM, Audit Manager ensures that your
assessment accurately reflects the active security controls and findings that are
relevant to your environment, excluding any controls that you intentionally
disabled.

## I set the status of

a finding to `Suppressed` in Security Hub CSPM. Does Audit Manager collect compliance
check evidence about that finding?

Audit Manager collects evidence for security controls that have suppressed findings.

If you set the workflow status of a finding to [suppressed](../../../securityhub/latest/userguide/finding-workflow-status.md "../../../securityhub/latest/userguide/finding-workflow-status.md") in Security Hub CSPM, this means that you reviewed the finding and do not believe that
any action is needed. In Audit Manager, these suppressed findings are collected as evidence
and attached to your assessment. The evidence details show the evaluation status of
`SUPPRESSED` reported directly from Security Hub CSPM.

This approach ensures that your Audit Manager assessment accurately represents the findings
from Security Hub CSPM, while also providing visibility into any suppressed findings that may
require further review or consideration in an audit.

## My

assessment isn’t collecting compliance check evidence from AWS Config

If you don't see compliance check evidence for an AWS Config rule, this could be due
to one of the following issues.

**The rule identifier was entered incorrectly in your
`ControlMappingSource`**

When you use the Audit Manager API to create a custom control, you can specify
an AWS Config rule as a [data source mapping](../APIReference/API_ControlMappingSource.md "../APIReference/API_ControlMappingSource.md") for evidence collection. The [`keywordValue`](../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue "../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue") that you specify depends on
the type of rule.

If you don't see compliance check evidence for an AWS Config rule, it
could be that the `keywordValue` was entered incorrectly in
your `ControlMappingSource`. The `keywordValue` is
case sensitive. If you enter it incorrectly, Audit Manager might not recognize
the rule. As a result, you might not collect compliance check evidence
for that rule as intended.

To fix this issue, [update the custom control](../APIReference/API_UpdateControl.md "../APIReference/API_UpdateControl.md") and revise the
`keywordValue`.

- For custom rules, make sure that the `keywordValue`
  has the `Custom_` prefix followed by the custom rule
  name. The format of the custom rule name may vary. For accuracy,
  visit the [AWS Config
  console](https://console.aws.amazon.com/config/ "https://console.aws.amazon.com/config/") to verify your custom rule names.
- For managed rules, make sure that the
  `keywordValue` is the rule identifier in
  `ALL_CAPS_WITH_UNDERSCORES`. For example,
  `CLOUDWATCH_LOG_GROUP_ENCRYPTED`. For accuracy,
  reference the list of [supported managed rule keywords](control-data-sources-config.md#aws-config-managed-rules "control-data-sources-config.md#aws-config-managed-rules").

###### Note

For some managed rules, the rule identifier is different
from the rule name. For example, the rule identifier for
[restricted-ssh](../../../config/latest/developerguide/restricted-ssh.md "../../../config/latest/developerguide/restricted-ssh.md") is
`INCOMING_SSH_DISABLED`. Make sure to use the
rule identifier, not the rule name. To find a rule
identifier, choose a rule from the [list of managed rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") and look for its
**Identifier** value.

**The rule is a service-linked AWS Config
rule**

You can use [managed rules](control-data-sources-config.md#aws-config-managed-rules "control-data-sources-config.md#aws-config-managed-rules") and [custom rules](control-data-sources-config.md#aws-config-custom-rules "control-data-sources-config.md#aws-config-custom-rules") as a data source mapping for evidence
collection. However, Audit Manager doesn’t collect evidence from most [service-linked rules](../../../config/latest/developerguide/service-linked-awsconfig-rules.md "../../../config/latest/developerguide/service-linked-awsconfig-rules.md").

There are only two types of service-linked rule that Audit Manager collects
evidence from:

- Service-linked rules from Conformance Packs
- Service-linked rules from AWS Organizations

Audit Manager doesn't collect evidence from other service-linked rules,
specifically any rules with an Amazon Resource Name (ARN) that contains
the following prefix:
`arn:aws:config:*:*:config-rule/aws-service-rule/...`

The reason that Audit Manager doesn't collect evidence from most service-linked
AWS Config rules is to prevent duplicate evidence in your assessments. A
service-linked rule is a specific type of managed rule that enables
other AWS services to create AWS Config rules in your account. For
example, [some Security Hub CSPM controls use an AWS Config service-linked rule to run
security checks](../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md "../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md"). For each Security Hub CSPM control that uses a
service-linked AWS Config rule, Security Hub CSPM creates an instance of the required
AWS Config rule in your AWS environment. This happens even if the
original rule already exists in your account. Therefore, to avoid
collecting the same evidence from the same rule twice, Audit Manager ignores the
service-linked rule and doesn't collect evidence from it.

**AWS Config isn't enabled**

AWS Config must be enabled in your AWS account. After you've set up
AWS Config in this way, Audit Manager collects evidence each time the evaluation of
an AWS Config rule occurs. Make sure that you enabled AWS Config in your
AWS account. For instructions, see [Enable and set up AWS Config](setup-recommendations.md#config-recommendations "setup-recommendations.md#config-recommendations").

**The AWS Config rule evaluated a resource configuration
before you set up your assessment**

If your AWS Config rule is set up to evaluate configuration changes for
a specific resource, you might see a mismatch between the evaluation in
AWS Config and the evidence in Audit Manager. This happens if the rule evaluation
occurred before you set up the control in your Audit Manager assessment. In this
case, Audit Manager doesn't generate evidence until the underlying resource
changes state again and triggers a re-evaluation of the rule.

As a workaround, you can navigate to the rule in the AWS Config console
and [manually re-evaluate the rule](../../../config/latest/developerguide/evaluating-your-resources.md#evaluating-your-resources-console "../../../config/latest/developerguide/evaluating-your-resources.md#evaluating-your-resources-console"). This invokes a new
evaluation of all of the resources that pertain to that rule.

## My assessment isn’t collecting user activity evidence from

AWS CloudTrail

When you use the Audit Manager API to create a custom control, you can specify a CloudTrail event
name as a [data
source mapping](../APIReference/API_ControlMappingSource.md "../APIReference/API_ControlMappingSource.md") for evidence collection. To do so, you enter the event
name as the [`keywordValue`](../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue "../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue").

If you don't see user activity evidence for a CloudTrail event, it could be that the
`keywordValue` was entered incorrectly in your
`ControlMappingSource`. The `keywordValue` is case
sensitive. If you enter it incorrectly, Audit Manager might not recognize the event name. As
a result, you might not collect user activity evidence for that event as
intended.

To fix this issue, [update the custom
control](../APIReference/API_UpdateControl.md "../APIReference/API_UpdateControl.md") and revise the `keywordValue`. Make sure that the
event is written as `serviceprefix_ActionName`. For example,
`cloudtrail_StartLogging`. For accuracy, review the AWS service
prefix and action names in the [Service Authorization Reference](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md").

## My assessment isn’t collecting configuration data

evidence for an AWS API call

When you use the Audit Manager API to create a custom control, you can specify an AWS API
call as a [data
source mapping](../APIReference/API_ControlMappingSource.md "../APIReference/API_ControlMappingSource.md") for evidence collection. To do so, you enter the API
call as the [`keywordValue`](../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue "../APIReference/API_SourceKeyword.md#auditmanager-Type-SourceKeyword-keywordValue").

If you don't see configuration data evidence for an AWS API call, it could be
that the `keywordValue` was entered incorrectly in your
`ControlMappingSource`. The `keywordValue` case sensitive.
If you enter it incorrectly, Audit Manager might not recognize the API call. As a result, you
might not collect configuration data evidence for that API call as intended.

To fix this issue, [update the custom
control](../APIReference/API_UpdateControl.md "../APIReference/API_UpdateControl.md") and revise the `keywordValue`. Make sure that the API
call is written as `serviceprefix_ActionName`. For example,
`iam_ListGroups`. For accuracy, reference the list of [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md "control-data-sources-api.md").

## A

common control isn’t collecting any automated evidence

When you review a common control, you might see the following message:
**This common control doesn’t collect automated evidence from core
controls**.

This means that no AWS managed evidence sources can currently support this
common control. As a result, the **Evidence sources** tab is empty
and no core controls are displayed.

When a common control doesn’t collect automated evidence, it’s referred to as a
_manual common control_. Manual common controls
typically require the provision of physical records and signatures, or details about
events that occur outside of your AWS environment. For this reason, there are
often no AWS data sources that can produce evidence to support the control’s
requirements.

If a common control is manual, you can still use it as an evidence source for a
custom control. The only difference is that the common control won’t collect any
evidence automatically. Instead, you’ll need to manually upload your own evidence to
support the requirements of the common control.

###### To add evidence to a manual common control

1. **Create a custom control**
   - Follow the steps to [create](create-controls.md "create-controls.md") or [edit](edit-controls.md "edit-controls.md") a custom control.
   - When you specify evidence sources in step 2, choose the manual
     common control as an evidence source.

2. **Create a custom framework**
   - Follow the steps to [create](custom-frameworks.md "custom-frameworks.md") or [edit](edit-custom-frameworks.md "edit-custom-frameworks.md") a custom framework.
   - When you specify a control set in step 2, include your new custom
     control.

3. **Create an assessment**
   - Follow the steps to [create an assessment](create-assessments.md "create-assessments.md") from your custom framework.
   - At this point, the manual common control is now an evidence source
     in an active assessment control.

4. **Upload manual evidence**
   - Follow the steps to [add manual evidence](upload-evidence.md#how-to-upload-manual-evidence-files "upload-evidence.md#how-to-upload-manual-evidence-files") to the control in your
     assessment.

###### Note

As more AWS data sources become available in the future, it’s possible that
AWS might update the common control to include core controls as evidence
sources. In this case, if the common control is an evidence source in one or
more of your active assessment controls, you’ll benefit from these updates
automatically. No further set up is needed from your side, and you’ll start to
collect automated evidence that supports the common control.

## My evidence is generated at different intervals, and I'm

not sure how often it’s being collected

The controls in Audit Manager assessments are mapped to various data sources. Each data
source has a different evidence collection frequency. As a result, there’s no
one-size-fits-all answer for how often evidence is collected. Some data sources
evaluate compliance, whereas others only capture resource state and change data
without a compliance determination.

The following is a summary of the different data source types and how often they
collect evidence.

| Data source type      | Description                                                                                                   | Evidence collection frequency                                                             | When this control is active in an assessment                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS CloudTrail        | Tracks a specific user activity.                                                                              | Continual                                                                                 | Audit Manager filters your CloudTrail logs based on the keyword that you<br>choose. The processed logs are imported as \*_User<br>activity_<br>• evidence. |
| AWS Security Hub CSPM | Captures a snapshot of your resource security posture by<br>reporting findings from Security Hub CSPM.        | Based on the schedule of the Security Hub CSPM check (typically around every<br>12 hours) | Audit Manager retrieves the security finding directly from Security Hub CSPM. The<br>finding is imported as \*_Compliance<br>check_<br>• evidence.         |
| AWS Config            | Captures a snapshot of your resource security posture by<br>reporting findings from AWS Config.               | Based on the settings that are defined in the AWS Config rule                             | Audit Manager retrieves the rule evaluation directly from AWS Config. The<br>evaluation is imported as **Compliance check**<br>evidence.                   |
| AWS API calls         | Takes a snapshot of your resource configuration directly<br>through an API call to the specified AWS service. | Daily, weekly, or monthly                                                                 | Audit Manager makes the API call based on the frequency that you specify.<br>The response is imported as **Configuration data**<br>evidence.               |

Regardless of the evidence collection frequency, new evidence is collected
automatically for as long as the assessment is active. For more information, see
[Evidence collection frequency](how-evidence-is-collected.md#frequency "how-evidence-is-collected.md#frequency").

To learn more, see [Supported data source types for automated
evidence](control-data-sources.md "control-data-sources.md") and [Changing how often a control collects
evidence](change-evidence-collection-frequency.md "change-evidence-collection-frequency.md").

## I disabled and then re-enabled Audit Manager,

and now my pre-existing assessments are no longer collecting evidence

When you disable Audit Manager and choose not to delete your data, your existing
assessments move into a dormant state and stop collecting evidence. This means that
when you re-enable Audit Manager, the assessments that you previously created remain
available. However, they don't automatically resume evidence collection.

To start collecting evidence again for a pre-existing assessment, [edit the assessment](edit-assessment.md "edit-assessment.md") and choose **Save**
without making any changes.

## On my assessment details page, I’m prompted to recreate

my assessment

![Screenshot of the pop-up message that prompts you to recreate your assessment.](images/troubleshooting-recreate-assessment-post-common-controls-console.png)

If you see a message that says **Create new assessment to collect more
comprehensive evidence**, this indicates that Audit Manager now provides a new
definition of the standard framework that your assessment was created from.

In the new framework definition, all of the framework’s standard controls can now
collect evidence from [AWS
managed sources](concepts.md#aws-managed-source "concepts.md#aws-managed-source"). This means that whenever there’s an update to the
underlying data sources for a common or core control, Audit Manager automatically applies the
same update to all related standard controls.

To benefit from these AWS managed sources, we recommend that you [create a new
assessment](create-assessments.md "create-assessments.md") from the updated framework. After you do this, you can then
[change the old assessment status to inactive](change-assessment-status-to-inactive.md "change-assessment-status-to-inactive.md"). This action helps to
ensure that your new assessment collects the most accurate and comprehensive
evidence that’s available from AWS managed sources. If you take no action, your
assessment continues to use the old framework and control definitions to collect
evidence exactly as it did before.

## What’s the

difference between a data source and an evidence source?

An _evidence source_ determines where evidence is
collected from. This can be an individual data source, or a predefined grouping of
data sources that maps to a core control or a common control.

A _data source_ is the most granular type of
evidence source. A data source includes the following details that tell Audit Manager where
exactly to collect evidence data from:

- [Data
  source type](control-data-sources.md "control-data-sources.md") (for example, AWS Config)
- [Data source mapping](concepts.md#control-data-source "concepts.md#control-data-source") (for example, a specific AWS Config rule such
  as `s3-bucket-public-write-prohibited`)

## My assessment

creation failed

If your assessment creation fails, this could be due to one of the following issues.

**You selected too many AWS accounts in your assessment scope**

If you're using AWS Organizations, Audit Manager can support up to 200 member accounts in the scope of a single assessment. If you exceed this number, the assessment creation will fail.

As a workaround, you can run multiple assessments with different accounts in scope for each assessment up to 250 unique member accounts across all assessments.

**An account in your scope is already being assessed by another active assessment**

If you try to create an assessment that includes an account that's already in scope for another active assessment, the assessment creation fails. This can happen when multiple teams or organizations are trying to assess the same account simultaneously.

You might see an error message similar to: `Scope: AWS Account [account-id] has assessments in progress`.

To resolve this issue, you can take one of the following actions:

- **Coordinate with other teams** - Contact other teams in your organization to determine which assessments are currently using the account in question. You can then coordinate to avoid overlapping assessment scopes.
- **Modify your assessment scope** - Remove the conflicting account from your assessment scope and create the assessment with the remaining accounts. You can assess the conflicting account separately once the other assessment is complete.
- **Wait for the other assessment to complete** - If the other assessment is temporary or nearing completion, you can wait for it to finish before creating your assessment with the desired scope.

###### Note

This restriction helps ensure that evidence collection doesn't conflict between multiple assessments and that audit results remain accurate and consistent.

## What

happens if I remove an in-scope account from my organization?

When an in-scope account is removed from your organization, Audit Manager no longer
collects evidence for that account and it will be removed from all assessments where
the account is in scope. Removing a member account from all assessments will also
reduce the total number of unique accounts in scope, allowing you to add a new
account from your organization.

## I can't see the

services in scope for my assessment

If you don't see the **AWS services** tab, this means that the
services in scope are managed for you by Audit Manager. When you create a new assessment,
Audit Manager manages the services in scope for you from that point onwards.

If you have an older assessment, it’s possible that you saw this tab previously in
your assessment. However, Audit Manager automatically removes this tab from your assessment
and takes over the management of services in scope when either of the following
events occur:

- You edit your assessment
- You edit one of the custom controls that’s used in your assessment

Audit Manager infers the services in scope by examining your assessment controls and their
data sources, and then mapping this information to the corresponding AWS services.
If an underlying data source changes for your assessment, we automatically update
the scope as needed to reflect the correct services. This ensures that your
assessment collects accurate and comprehensive evidence about all of the relevant
services in your AWS environment.

## I can't edit the

services in scope for my assessment

The [Editing an assessment in AWS Audit Manager](edit-assessment.md "edit-assessment.md") workflow no
longer has an **Edit services** step. This is because Audit Manager now
manages which AWS services are in scope for your assessment.

If you have an older assessment, it’s possible that you manually defined the
services in scope when you created that assessment. However, you can’t edit these
services moving forward. Audit Manager automatically takes over the management of services in
scope for your assessment when either of the following events occur:

- You edit your assessment
- You edit one of the custom controls that’s used in your assessment

Audit Manager infers the services in scope by examining your assessment controls and their
data sources, and then mapping this information to the corresponding AWS services.
If an underlying data source changes for your assessment, we automatically update
the scope as needed to reflect the correct services. This ensures that your
assessment collects accurate and comprehensive evidence about all of the relevant
services in your AWS environment.

## What's the

difference between a service in scope and a data source type?

A [service in scope](concepts.md#service-in-scope "concepts.md#service-in-scope") is an
AWS service that's included in the scope of your assessment. When a service is in
scope, Audit Manager collects evidence about your usage of that service and its
resources.

###### Note

Audit Manager manages which AWS services are in scope for your assessments. If you
have an older assessment, it’s possible that you manually specified the services
in scope in the past. Moving forward, you can’t specify or edit services in
scope.

A [data source
type](control-data-sources.md "control-data-sources.md") indicates where exactly the evidence is collected from. If you
upload your own evidence, the data source type is _Manual_. If Audit Manager collects the evidence, the data source can be one of
four types.

1. AWS Security Hub CSPM – Captures a snapshot of your resource security posture
   by reporting findings from Security Hub CSPM.
2. AWS Config – Captures a snapshot of your resource security posture by
   reporting findings from AWS Config.
3. AWS CloudTrail – Tracks a specific user activity for a resource.
4. AWS API calls – Takes a snapshot of your resource configuration
   directly through an API call to a specific AWS service.

Here are two examples to illustrate the difference between a service in scope and
a data source type.

###### Example 1

Let's say that you want to collect evidence for a control that's named
_4.1.2 - Disallow public write access to S3
buckets_. This control checks the access levels of your S3 bucket
policies. For this control, Audit Manager uses a specific AWS Config rule ([s3-bucket-public-write-prohibited](../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md "../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md")) to look for an evaluation of
your S3 buckets. In this example, the following is true:

- The [service in scope](concepts.md#service-in-scope "concepts.md#service-in-scope") is
  Amazon S3
- The [resources](concepts.md#resource "concepts.md#resource") that are being assessed are your S3 buckets
- The [data
  source type](control-data-sources.md "control-data-sources.md") is AWS Config
- The [data source mapping](concepts.md#control-data-source "concepts.md#control-data-source") is a specific AWS Config rule
  (`s3-bucket-public-write-prohibited`)

###### Example 2

Let's say that you want to collect evidence for a HIPAA control that's named
_164.308(a)(5)(ii)(C)_. This control
requires a monitoring procedure for detecting inappropriate sign-ins. For this
control, Audit Manager uses CloudTrail logs to look for all [AWS Management Console sign-in events](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-aws-console-sign-in-events.md"). In this example, the
following is true:

- The [service in scope](concepts.md#service-in-scope "concepts.md#service-in-scope") is
  IAM
- The [resources](concepts.md#resource "concepts.md#resource") that are being assessed are your users
- The [data
  source type](control-data-sources.md "control-data-sources.md") is CloudTrail
- The [data source mapping](concepts.md#control-data-source "concepts.md#control-data-source") is a specific CloudTrail event
  (`ConsoleLogin`)
