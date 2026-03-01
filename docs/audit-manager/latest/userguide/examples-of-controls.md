# Examples of AWS Audit Manager controls

You can review the examples on this page to learn more about how controls work in
AWS Audit Manager.

In Audit Manager, controls can automatically collect evidence from four data source types:

1. **AWS CloudTrail** – Capture user activity from your
   CloudTrail logs and import it as user activity evidence
2. **AWS Security Hub CSPM** – Collect findings from Security Hub CSPM and
   import them as compliance check evidence
3. **AWS Config** – Collect rule evaluations from
   AWS Config and import them as compliance check evidence
4. **AWS API calls** – Capture a resource snapshot
   from an API call and import it as configuration data evidence
   Note that some controls collect evidence using predefined groupings of these data sources.
   These data source groupings are known as [AWS managed
   sources](concepts.md#aws-managed-source "concepts.md#aws-managed-source"). Each AWS managed source represents either a common control or a core
   control. These managed sources give you an efficient way to map your compliance requirements
   to a relevant group of underlying data sources that’s validated and maintained by [industry
   certified assessors](https://aws.amazon.com/professional-services/security-assurance-services/ "https://aws.amazon.com/professional-services/security-assurance-services/") in AWS.

The examples on this page show how controls collect evidence from each of the individual
data source types. They describe what a control looks like, how Audit Manager collects evidence from
the data source, and the next steps that you can take to demonstrate compliance.

###### Tip

We recommend that you enable AWS Config and Security Hub CSPM for an optimal experience in Audit Manager. When
you enable these services, Audit Manager can use Security Hub CSPM findings and AWS Config Rules to generate automated
evidence.

- After you [enable
  AWS Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-settingup.md "../../../securityhub/latest/userguide/securityhub-settingup.md"), make sure that you also [enable all security standards](../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console "../../../securityhub/latest/userguide/securityhub-standards-enable-disable.md#securityhub-standard-enable-console") and [turn on the consolidated control findings setting](../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings "../../../securityhub/latest/userguide/controls-findings-create-update.md#turn-on-consolidated-control-findings"). This step ensures that
  Audit Manager can import findings for all supported compliance standards.
- After you [enable AWS Config](../../../config/latest/developerguide/gs-console.md "../../../config/latest/developerguide/gs-console.md"), make sure
  that you also [enable the relevant AWS Config Rules](../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md "../../../config/latest/developerguide/setting-up-aws-config-rules-with-console.md") or [deploy a conformance
  pack](../../../config/latest/developerguide/conformance-pack-console.md "../../../config/latest/developerguide/conformance-pack-console.md") for the compliance standard that's related to your audit. This step
  ensures that Audit Manager can import findings for all the supported AWS Config Rules that you
  enabled.
  Examples are available for each of the following types of controls:

###### Topics

- [Automated controls that use AWS Security Hub CSPM as a data source type](#automated-security-hub "#automated-security-hub")
- [Automated controls that use AWS Config as a data source type](#automated-config "#automated-config")
- [Automated controls that use AWS API calls as a data source type](#automated-api "#automated-api")
- [Automated controls that use AWS CloudTrail as a data source type](#automated-cloudtrail "#automated-cloudtrail")
- [Manual controls](#manual "#manual")
- [Controls with mixed data source types (automated and manual)](#mixed "#mixed")

## Automated controls that use AWS Security Hub CSPM as a data source type

This example shows a control that uses AWS Security Hub CSPM as a data source type. This is a
standard control taken from the [AWS
Foundational Security Best Practices (FSBP) framework](aws-foundational-security-best-practices.md "aws-foundational-security-best-practices.md"). Audit Manager uses this control to
generate evidence that can help to bring your AWS environment in line with FSBP
requirements.

###### Example control details

- **Control name** – `FSBP1-012: AWS Config
should be enabled`
- **Control set** – `Config`. This is a
  framework-specific grouping of FSBP controls that relate to configuration
  management.
- **Evidence source** – Individual data
  sources
- **Data source type** – AWS Security Hub CSPM
- **Evidence type** – Compliance check

In the following example, this control appears in an Audit Manager assessment that was created
from the FSBP framework.

![Screenshot that shows the Security Hub CSPM control in an assessment.](images/control-example-automated_securityhub-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

This control requires that AWS Config is enabled in all AWS Regions where you use
Security Hub CSPM. Audit Manager can use this control to check whether you have enabled AWS Config.

###### How Audit Manager collects evidence for this control

Audit Manager takes the following steps to collect evidence for this control:

1. For each control, Audit Manager assesses your in-scope resources. It does this using the data
   source that’s specified in the control settings. In this example, your AWS Config settings are
   the resource, and Security Hub CSPM is the data source type. Audit Manager looks for the result of a specific
   Security Hub CSPM check ([[Config.1]](../../../securityhub/latest/userguide/config-controls.md#config-1 "../../../securityhub/latest/userguide/config-controls.md#config-1")).
2. The result of the resource assessment is saved and converted into auditor-friendly
   evidence. Audit Manager generates _compliance check_ evidence
   for controls that use Security Hub CSPM as a data source type. This evidence contains the result of
   the compliance check reported directly from Security Hub CSPM.
3. Audit Manager attaches the saved evidence to the control in your assessment that’s named
   `FSBP1-012: AWS Config should be enabled`.

###### How you can use Audit Manager to demonstrate compliance with this control

After the evidence is attached to the control, you—or a delegate of your
choice—can review the evidence to see if any remediation is necessary.

In this example, Audit Manager might display a _Fail_ ruling
from Security Hub CSPM. This can happen if you have not enabled AWS Config. In this case, you can take the
corrective action of enabling AWS Config, which helps to bring your AWS environment in line with
FSBP requirements.

When your AWS Config settings are in line with the control, mark the control as _Reviewed_ and add the evidence to your assessment report. You can
then share this report with auditors to demonstrate that the control is working as
intended.

## Automated controls that use AWS Config as a data source type

This example shows a control that uses AWS Config as a data source type. This is a
standard control taken from the [AWS Control Tower Guardrails
framework](controltower.md "controltower.md"). Audit Manager uses this control to generate evidence that helps bring your AWS
environment in line with AWS Control Tower Guardrails.

###### Example control details

- **Control name** – `CT-4.1.2: 4.1.2 -
Disallow public write access to S3 buckets`
- **Control set** – This control belongs to the
  `Disallow public access` control set. This is a grouping of controls that
  relate to access management.
- **Evidence source** – Individual data
  source
- **Data source type** – AWS Config
- **Evidence type** – Compliance check

In the following example, this control appears in an Audit Manager assessment that was created
from the AWS Control Tower Guardrails framework.

![Screenshot that shows the AWS Config control in an assessment.](images/control-example-automated_config-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

Audit Manager can use this control to check if the access levels of your S3 bucket policies are
too lenient to meet AWS Control Tower requirements. More specifically, it can check the Block
Public Access settings, the bucket policies, and the bucket access control lists (ACL) to
confirm that your buckets don’t allow public write access.

###### How Audit Manager collects evidence for this control

Audit Manager takes the following steps to collect evidence for this control:

1. For each control, Audit Manager assesses your in-scope resources using the data source that’s
   specified in the control settings. In this case, your S3 buckets are the resource, and
   AWS Config is the data source type. Audit Manager looks for the result of a specific AWS Config Rule
   ([s3-bucket-public-write-prohibited](../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md "../../../config/latest/developerguide/s3-bucket-public-write-prohibited.md")) to evaluate the settings, policy, and ACL
   of each of the S3 buckets that are in scope of your assessment.
2. The result of the resource assessment is saved and converted into auditor-friendly
   evidence. Audit Manager generates _compliance check_ evidence
   for controls that use AWS Config as a data source type. This evidence contains the result of
   the compliance check reported directly from AWS Config.
3. Audit Manager attaches the saved evidence to the control in your assessment that’s named
   `CT-4.1.2: 4.1.2 - Disallow public write access to S3 buckets`.

###### How you can use Audit Manager to demonstrate compliance with this control

After the evidence is attached to the control, you—or a delegate of your
choice—can review the evidence to see if any remediation is necessary.

In this example, Audit Manager might display a ruling from AWS Config stating that an S3 bucket is
_noncompliant_. This could happen if one of your S3
buckets has a Block Public Access setting that doesn’t restrict public policies, and the
policy that’s in use allows public write access. To remediate this, you can update the Block
Public Access setting to restrict public policies. Or, you can use a different bucket policy
that doesn’t allow public write access. This corrective action helps to bring your AWS
environment in line with AWS Control Tower requirements.

When you’re satisfied that your S3 bucket access levels are in line with the control,
you can mark the control as _Reviewed_ and add the evidence
to your assessment report. You can then share this report with auditors to demonstrate that
the control is working as intended.

## Automated controls that use AWS API calls as a data source type

This example shows a custom control that uses AWS API calls as a data source type.
Audit Manager uses this control to generate evidence that can help to bring your AWS environment in
line with your specific requirements.

###### Example control details

- **Control name** – `Password
Use`
- **Control set** – This control belongs to a
  control set that's called `Access Control`. This is a grouping of controls
  that relate to identity and access management.
- **Evidence source** – Individual data
  source
- **Data source type** – AWS API calls
- **Evidence type** – Configuration data

In the following example, this control appears in an Audit Manager assessment that was created
from a custom framework.

![Screenshot that shows the API control in an assessment.](images/control-example-automated_api-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

Audit Manager can use this custom control to help you ensure that you have sufficient access
control policies in place. This control requires that you follow good security practices
in the selection and use of passwords. Audit Manager can help you to validate this by retrieving a
list of all password policies for the IAM principals that are in the scope of your
assessment.

###### How Audit Manager collects evidence for this control

Audit Manager takes the following steps to collect evidence for this custom control:

1. For each control, Audit Manager assesses your in-scope resources using the data source that’s
   specified in the control settings. In this case, your IAM principals are the
   resources, and AWS API calls is the data source type. Audit Manager looks for the response of a
   specific IAM API call ([GetAccountPasswordPolicy](../../../IAM/latest/APIReference/API_GetAccountPasswordPolicy.md "../../../IAM/latest/APIReference/API_GetAccountPasswordPolicy.md")). It then returns the password policies for the
   AWS accounts that are in scope of your assessment.
2. The result of the resource assessment is saved and converted into auditor-friendly
   evidence. Audit Manager generates _configuration data_ evidence
   for controls that use API calls as a data source. This evidence contains the original
   data that's captured from the API responses, and additional metadata that indicates
   which control the data supports.
3. Audit Manager attaches the saved evidence to the custom control in your assessment that’s
   named `Password Use`.

###### How you can use Audit Manager to demonstrate compliance with this control

After the evidence is attached to the control, you—or a delegate of your
choice—can review the evidence to see if it’s sufficient or if any remediation is
necessary.

In this example, you can review the evidence to see the response from the API call. The
[GetAccountPasswordPolicy](../../../IAM/latest/APIReference/API_GetAccountPasswordPolicy.md "../../../IAM/latest/APIReference/API_GetAccountPasswordPolicy.md") response describes the complexity requirements and
mandatory rotation periods for the user passwords in your account. You can use this API
response as evidence to show that you have sufficient password access control policies in
place for the AWS accounts that are in the scope of your assessment. If you want, you can
also provide additional commentary about these policies by adding a comment to the
control.

When you’re satisfied that the password policies of your IAM principals are in line
with the custom control, you can mark the control as _Reviewed_ and add the evidence to your assessment report. You can then share
this report with auditors to demonstrate that the control is working as intended.

## Automated controls that use AWS CloudTrail as a data source type

This example shows a control that uses AWS CloudTrail as a data source type. This is a
standard control taken from the [HIPAA Security Rule 2003
framework](HIPAA.md "HIPAA.md"). Audit Manager uses this control to generate evidence that can help to bring your
AWS environment in line with HIPAA requirements.

###### Example control details

- **Control name** – `164.308(a)(5)(ii)(C):
Administrative Safeguards - 164.308(a)(5)(ii)(C)`
- **Control set** – This control belongs to the
  control set that's called `Section 308`. This is a framework-specific
  grouping of HIPAA controls that relate to administrative safeguards.
- **Evidence source** – AWS managed source (core
  controls)
- **Underlying data source type** –
  AWS CloudTrail
- **Evidence type** – User activity

Here’s this control shown within an Audit Manager assessment that was created from the HIPAA
framework:

![Screenshot that shows the CloudTrail control in an assessment.](images/control-example-automated_cloudtrail-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

This control requires that you have monitoring procedures in place for detecting
unauthorized access. An example of unauthorized access is when someone signs in to the
console without multi-factor authentication (MFA) enabled. Audit Manager helps you to validate this
control by providing evidence that you configured Amazon CloudWatch to monitor for management
console sign-in requests where MFA is not enabled.

###### How Audit Manager collects evidence for this control

Audit Manager takes the following steps to collect evidence for this control:

1. For each control, Audit Manager assesses your in-scope resources using the evidence sources
   that are specified in the control settings. In this case, the control uses several core
   controls as evidence sources.

Each core control is a managed grouping of individual data sources. In our example,
one of these core controls (`Configure Amazon CloudWatch alarms to detect management console
 sign-in requests without MFA enabled`) uses a CloudTrail event
(`monitoring_EnableAlarmActions`) as the underlying data source.

Audit Manager reviews your CloudTrail logs, using the `monitoring_EnableAlarmActions`
keyword to find CloudWatch alarm enabling actions that are logged by CloudTrail. It then returns a
log of the relevant events that are within the scope of your assessment. 2. The result of the resource assessment is saved and converted into auditor-friendly
evidence. Audit Manager generates _user activity_ evidence for
controls that use CloudTrail as a data source type. This evidence contains the original data
that's captured from Amazon CloudWatch, and additional metadata that indicates which control the
data supports. 3. Audit Manager attaches the saved evidence to the control in your assessment that’s named
`164.308(a)(5)(ii)(C): Administrative Safeguards - 164.308(a)(5)(ii)(C)`.

###### How you can use Audit Manager to demonstrate compliance with this control

After the evidence is attached to the control, you—or a delegate of your
choice—can review the evidence to see if any remediation is necessary.

In this example, you can review the evidence to see the alarm enablement events that
were logged by CloudTrail. You can use this log as evidence to show that you have sufficient
monitoring procedures in place to detect when console sign-ins occur without MFA enabled. If
you like, you can also provide additional commentary by adding a comment to the control. For
example, if the log shows multiple sign-ins without MFA, you can add a comment that
describes how you remediated the issue. Regular monitoring of console sign-ins helps you to
prevent security problems that may arise from discrepancies and inappropriate sign-in
attempts. In turn, this best practice helps to bring your AWS environment in line with
HIPAA requirements.

When you’re satisfied that your monitoring procedure is in line with the control, you
can mark the control as _Reviewed_ and add the evidence to
your assessment report. You can then share this report with auditors to demonstrate that the
control is working as intended.

## Manual controls

Some controls don’t support automated evidence collection. This includes controls that
rely on the provision of physical records and signatures, in addition to observations,
interviews, and other events that aren’t generated in the cloud. In these cases, you can
manually upload evidence to demonstrate that you’re satisfying the requirements of the
control.

This example shows a manual control taken from the [NIST 800-53 (Rev. 5)
framework](NIST800-53r5.md "NIST800-53r5.md"). You can use Audit Manager to upload and store evidence that demonstrates
compliance for this control.

###### Example control details

- **Control name** – `AT-4: Training
Records`
- **Control set** – `(AT) Awareness and
training`. This is a framework-specific grouping of NIST controls that relate to
  training.
- **Evidence source** – Individual data source
- **Data source type** – Manual
- **Evidence type** – Manual

Here’s this control shown within an Audit Manager assessment that was created from the NIST
800-53 (Rev. 5) Low-Moderate-High framework:

![Screenshot that shows the control in an assessment.](images/control-example-manual-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

You can use this control to help you ensure that your personnel receive the
appropriate level of security and privacy training. Specifically, you can demonstrate that
you have documented security and privacy training activities in place for all staff, based
on their role. You can also show proof that training records are retained for each
individual.

###### How you can manually upload evidence for this control

To upload manual evidence that supplements the automated evidence, see [Uploading
manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md"). Audit Manager attaches the uploaded evidence to the control
in your assessment that’s named `AT-4: Training Records`.

###### How you can use Audit Manager to demonstrate compliance with this control

If you have documentation that supports this control, you can upload it as manual
evidence. For example, you can upload the latest copy of mandated role-based training
materials that your Human Resources department issues to employees.

Much like with automated controls, you can delegate manual controls to stakeholders who
can help you to review evidence (or, in this case, supply it). For example, when you review
this control, you might realize that you only partially meet its requirements. This could be
the case if you don’t have a copy of any attendance tracking for in-person trainings. You
could delegate the control to an HR stakeholder, who can then upload a list of staff that
attended the training.

When you’re satisfied that you’re in line with the control, you can mark it as _Reviewed_ and add the evidence to your assessment report. You can
then share this report with auditors to demonstrate that the control is working as
intended.

## Controls with mixed data source types (automated and manual)

In many cases, a combination of automated and manual evidence is needed to satisfy a
control. Although Audit Manager can provide automated evidence that’s relevant to the control, you
might need to supplement this data with manual evidence that you identify and upload
yourself.

This example shows a control that uses a combination of manual evidence and automated
evidence. This is a standard control taken from the [NIST 800-53 (Rev. 5)
framework](NIST800-53r5.md "NIST800-53r5.md"). Audit Manager uses this control to generate evidence that can help to bring your
AWS environment in line with NIST requirements.

###### Example control details

- **Control name** – `Personnel
Termination`
- **Control set** – `(PS) Personnel Security
(10)`. This is a framework-specific grouping of NIST controls that relate to the
  individuals who perform hardware or software maintenance on organizational
  systems.
- **Evidence source** – AWS managed (core
  controls) and individual data sources (manual)
- **Underlying data source type** – AWS API
  calls, AWS CloudTrail, AWS Config, Manual
- **Evidence type** – Configuration data, user
  activity, compliance check, manual evidence)

Here’s this control shown within an Audit Manager assessment that was created from the NIST
800-53 (Rev. 5) framework:

![Screenshot that shows the control in an assessment.](images/control-example-mixed-console.png)

The assessment shows the control status. It also shows how much evidence was collected
for this control so far. From here, you can delegate the control set for review or complete
the review yourself. Choosing the control name opens a detail page with more information,
including the evidence for that control.

###### What this control does

You can use this control to confirm that you’re protecting organizational information
in the event that an employee is terminated. Specifically, you can demonstrate that you
disabled system access and revoked credentials for the individual. Moreover, you can
demonstrate that all terminated individuals participated in an exit interview that
included discussion of the relevant security protocols for your organization.

###### How Audit Manager collects evidence for this control

Audit Manager takes the following steps to collect evidence for this control:

1. For each control, Audit Manager assesses your in-scope resources using the evidence sources
   that are specified in the control settings.

In this case, the control uses several core controls as evidence sources. In turn,
each of these core controls collect relevant evidence from individual data sources
(AWS API calls, AWS CloudTrail, and AWS Config). Audit Manager uses these data source types to assess your
IAM resources (such as groups, keys, and policies) against the relevant API calls,
CloudTrail events, and AWS Config rules. 2. The result of the resource assessment is saved and converted into auditor-friendly
evidence. This evidence contains the original data that's captured from each data
source, and additional metadata that indicates which control the data supports. 3. Audit Manager attaches the saved evidence to the control in your assessment that’s named
`Personnel Termination`.

###### How you can manually upload evidence for this control

To upload manual evidence that supplements the automated evidence, see [Uploading
manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md"). Audit Manager attaches the uploaded evidence to the control
in your assessment that’s named `Personnel Termination`.

###### How you can use Audit Manager to demonstrate compliance with this control

After the evidence is attached to the control, you—or a delegate of your
choice—can review the evidence to see if it’s sufficient or if any remediation is
necessary. For example, when you review this control, you might realize that you only
partially meet its requirements. This could be the case if you have proof that access was
revoked, but don’t have a copy of any exit interviews. You could delegate the control to
an HR stakeholder, who can then upload a copy of the exit interview paperwork. Or, if no
employees were terminated during the audit period, you can leave a comment that states why
no signed paperwork is attached to the control.

When you’re satisfied that you're in line with the control, mark the control as
_Reviewed_ and add the evidence to your assessment
report. You can then share this report with auditors to demonstrate that the control is
working as intended.
