# Understanding AWS Audit Manager concepts and terminology

To help you get started, this page defines terms and explains some of the key concepts of
AWS Audit Manager.

## A

A | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Assessment**

You can use an Audit Manager assessment to automatically collect evidence that’s relevant
for an audit.

An assessment is based on a framework, which is a grouping of controls that are
related to your audit. You can create an assessment from a standard framework or a
custom framework. Standard frameworks contain prebuilt control sets that support a
specific compliance standard or regulation. In contrast, custom frameworks contain
controls that you can customize and group according to your specific audit
requirements. Using a framework as a starting point, you can create an assessment that
specifies the AWS accounts that you want to include in the scope of your
audit.

When you create an assessment, Audit Manager automatically starts to assess resources in
your AWS accounts based on the controls that are defined in the framework. Next, it
collects the relevant evidence and converts it into an auditor-friendly format. After
doing this, it then attaches the evidence to the controls in your assessment. When
it's time for an audit, you—or a delegate of your choice—can review the
collected evidence and then add it to an assessment report. This assessment report
helps you to demonstrate that your controls are working as intended.

Evidence collection is an ongoing process that starts when you create your
assessment. You can stop evidence collection by changing the assessment status to
_inactive_. Alternatively, you can stop evidence
collection at the control level. You can do this by changing the status of a specific
control within your assessment to _inactive_.

For instructions on how to create and manage assessments, see [Managing assessments in AWS Audit Manager](assessments.md "assessments.md").

**Assessment
report**

An assessment report is a finalized document that's generated from an Audit Manager
assessment. These reports summarize the relevant evidence that's collected for your
audit. They link to the relevant evidence folders. The folders are named and organized
according to the controls that are specified in your assessment. For each assessment,
you can review the evidence that Audit Manager collects, and decide which evidence you want to
include in the assessment report.

To learn more about assessment reports, see [Assessment reports](assessment-reports.md "assessment-reports.md"). To learn how to generate an assessment report,
see [Preparing an assessment report in AWS Audit Manager](generate-assessment-report.md "generate-assessment-report.md").

**Assessment report destination**

An assessment report destination is the default S3 bucket where Audit Manager saves your
assessment reports. To learn more, see [Configuring your default assessment report
destination](settings-destination.md "settings-destination.md").

**Audit**

An audit is an independent examination of the assets, operations, or business
integrity of your organization. An information technology (IT) audit specifically
examines the controls within the information systems of your organization. The goal of
an IT audit is to determine if information systems safeguard assets, operate
effectively, and maintain data integrity. All of these are important to meeting the
regulatory requirements that are mandated by a compliance standard or regulation.

**Audit owner**

The term _audit owner_ has two different meanings
depending on the context.

In the context of Audit Manager, an audit owner is a user or role that manages an
assessment and its related resources. The responsibilities of this Audit Manager persona
include creating assessments, reviewing evidence, and generating assessment reports.
Audit Manager is a collaborative service, and audit owners benefit when other stakeholders
participate in their assessments. For example, you can add other audit owners to your
assessment to share management tasks. Or, if you’re an audit owner and you need help
interpreting the evidence that was collected for a control, you can [delegate
that control set](delegate.md "delegate.md") to a stakeholder who has subject matter expertise in that
area. Such a person is known as a _delegate_
persona.

In business terms, an audit owner is someone who coordinates and oversees the
audit readiness efforts of their company, and presents evidence to an auditor.
Typically, this is a governance, risk, and compliance (GRC) professional, such as a
Compliance Officer or a GDPR Data Protection Officer. GRC professionals have the
expertise and authority to manage audit preparation. More specifically, they
understand compliance requirements, and can analyze, interpret, and prepare reporting
data. However, other business roles can also assume the Audit Manager persona of an audit
owner—not only GRC professionals take on this role. For example, you might
choose to have your Audit Manager assessments set up and managed by a technical expert from one
of the following teams:

- SecOps
- IT/DevOps
- Security Operations Center/Incident Response
- Similar teams that own, develop, remediate, and deploy cloud assets, and
  understand the cloud infrastructure of your organization

Who you choose to assign as an audit owner in your Audit Manager assessment depends greatly
on your organization. It also depends on how you structure your security operations
and the specifics of the audit. In Audit Manager, the same individual can assume the audit
owner persona in one assessment, and the delegate persona in another.

No matter how you choose to use Audit Manager, you can manage the separation of duties
across your organization using the audit owner/delegate persona and granting specific
IAM policies to each user. Through this two-step approach, Audit Manager ensures that you
have full control over all of the specifics of an individual assessment. For more
information, see [Recommended policies for user personas in AWS Audit Manager](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-personas").

**AWS managed
source**

An AWS managed source is an evidence source that AWS maintains for you.

Each AWS managed source is a predefined grouping of data sources that maps to a
specific common control or core control. When you use a common control as an evidence
source, you automatically collect evidence for all the core controls that support that
common control. You can also use individual core controls as an evidence
source.

Whenever an AWS managed source is updated, the same updates are automatically
applied to all custom controls that use that AWS managed source. This means that
your custom controls collect evidence against the latest definitions of that evidence
source. This helps you to ensure continuous compliance as the cloud compliance
environment changes.

See also: [customer managed source](#customer-managed-source "#customer-managed-source"),
[evidence source](#evidence-source "#evidence-source").

## C

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | C | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Changelog**

For each control in an assessment, Audit Manager tracks user activity for that control. You
can then review an audit trail of activities that are related to a specific control.
For more information about which user activities are captured in the changelog, see
[Changelog tab](review-controls.md#review-changelog "review-controls.md#review-changelog").

**Cloud compliance**

Cloud compliance is the general principle that cloud-delivered systems must be
compliant with the standards that are faced by cloud customers.

**Common control**

See [control](#control "#control").

**Compliance
regulation**

A compliance regulation is a law, rule, or other order that's prescribed by an
authority, typically to regulate conduct. One example is GDPR.

**Compliance
standard**

A compliance standard is a structured set of guidelines that detail the processes
of an organization for maintaining accordance with established regulations,
specifications, or legislation. Examples include PCI DSS and HIPAA.

**Control**

A control is a safeguard or countermeasure that’s prescribed for an information
system or an organization. Controls are designed to protect the confidentiality,
integrity, and availability of your information, and to meet a set of defined
requirements. They provide an assurance that your resources are operating as intended,
your data is reliable, and your organization is compliant with applicable laws and
regulations.

In Audit Manager, a control can also represent a question in a vendor risk assessment
questionnaire. In this case, a control is a specific question that asks information
about an organization’s security and compliance posture.

Controls collect evidence continually when they’re active in your Audit Manager
assessments. You can also manually add evidence to any control. Each piece of evidence
is a record that helps you to demonstrate compliance with the control’s
requirements.

Audit Manager provides the following types of controls:

| Control type         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Common control**   | You can think of a common control as an action that helps you to fulfill<br>a control objective. Because common controls aren’t specific to any<br>compliance standard, they help you to collect evidence that can support a<br>range of overlapping compliance obligations.<br>For example, let's say you have a control objective called _Data classification and handling_. To fulfill this<br>objective, you could implement a common control called *Access controls<br>• to monitor and detect<br>unauthorized access to your resources.<br>• *Automated common controls* collect<br>evidence for you. They consist of a grouping of one or more related core<br>controls. In turn, each of these core controls automatically collects<br>relevant evidence from a predefined group of AWS data sources. AWS<br>manages these underlying data sources for you, and updates them whenever<br>regulations and standards change and new data sources are identified.<br>• *Manual common controls\* require<br>you to upload your own evidence. This is because they typically require<br>the provision of physical records, or details about events that happen<br>outside of your AWS environment. For this reason, there are often no<br>AWS data sources that can produce evidence to support the manual<br>common control’s requirements.<br>You can’t edit a common control. However, you can use any common control<br>as an evidence source when you [create a custom control](customize-control-from-scratch.md "customize-control-from-scratch.md"). |
| **Core control**     | This is a prescriptive guideline for your AWS environment. You can<br>think of a core control as an action that helps you to meet the requirements<br>of a common control.<br>For example, let's say you use a common control called *Access controls<br>• to monitor unauthorized access to<br>your resources. To support this common control, you could use the core<br>control called *Block public read access in S3<br>buckets\*.<br>Because core controls aren’t specific to any compliance standard, they<br>collect evidence that can support a range of overlapping compliance<br>obligations. Each core control uses one or more data sources to collect<br>evidence about a specific AWS service. AWS manages these underlying data<br>sources for you, and updates them whenever regulations and standards change<br>and new data sources are identified.<br>You can’t edit a core control. However, you can use any core control as<br>an evidence source when you [create a custom control](customize-control-from-scratch.md "customize-control-from-scratch.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Standard control** | This is a prebuilt control that Audit Manager provides.You can<br>use standard controls to assist you with audit preparation for a specific<br>compliance standard. Each standard control is related to a specific standard<br>[framework](#framework "#framework") in Audit Manager, and<br>collects evidence that you can use to demonstrate compliance with that<br>framework. Standard controls collect evidence from underlying data sources<br>that AWS manages. These data sources are automatically updated whenever<br>regulations and standards change and new data sources are identified.<br>You can’t edit standard controls. However, you can [make an editable copy](customize-control-from-existing.md "customize-control-from-existing.md") of any standard control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Custom control**   | This is a control that you create in Audit Manager to meet your specific<br>compliance requirements.<br>You can create a custom control from scratch, or make an editable copy<br>of an existing standard control. When you create a custom control, you can<br>define specific [evidence source](#evidence-source "#evidence-source")s that determine where Audit Manager collects<br>evidence from. After you create a custom control, you can edit that control<br>or add it to a custom framework. You can also [make an editable copy](customize-control-from-existing.md "customize-control-from-existing.md") of any custom control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

**Control domain**

You can think of a control domain as a category of controls that’s not specific to
any compliance standard. An example of a control domain is _Data protection_.

Controls are often grouped by domain for simple organizational purposes. Each
domain has multiple objectives.

Control domain groupings are one of the most powerful features of the [Audit Manager
dashboard](dashboard.md "dashboard.md"). Audit Manager highlights the controls in your assessments that have
non-compliant evidence, and groups them by control domain. This enables you to focus
your remediation efforts on specific subject domains as you prepare for an audit.

**Control
objective**

A control objective describes the goal of the common controls that fall underneath
it. Each objective can have multiple common controls. If these common controls are
implemented successfully, they’ll help you to fulfill the objective.

Each control objective falls under a control domain. For example, the _Data protection_ control domain might have a control
objective named _Data classification and handling._
To support this control objective, you could use a common control called _Access controls_ to monitor and detect unauthorized access
to your resources.

**Core control**

See [control](#control "#control").

**Custom control**

See [control](#control "#control").

**Customer
managed source**

A customer managed source is an evidence source that you define.

When you create a custom control in Audit Manager, you can use this option to create your
own individual data sources. This gives you the flexibility to collect automated
evidence from a business-specific resource, such as a custom AWS Config rule. You can
also use this option if you want to add manual evidence to your custom control.

When you use customer managed sources, you are responsible for maintaining all of
the data sources that you create.

See also: [AWS managed source](#aws-managed-source "#aws-managed-source"),
[evidence source](#evidence-source "#evidence-source").

## D

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | D | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Data source**

Audit Manager uses _data sources_ to collect evidence for
a control. A data source has the following properties:

- A **data source type** defines which type of data source Audit Manager
  collects evidence from.
  - For automated evidence, the type can be _AWS Security Hub_, _AWS Config,
    AWS CloudTrail_, or _AWS API calls._
  - If you upload your own evidence, the type is _Manual_.
  - The Audit Manager API refers to a data source type as a [sourceType](../APIReference/API_ControlMappingSource.md#auditmanager-Type-ControlMappingSource-sourceType "../APIReference/API_ControlMappingSource.md#auditmanager-Type-ControlMappingSource-sourceType").

- A **data source mapping** is a keyword that pinpoints where
  evidence is collected from for a given data source type.
  - For example, this might be the name of a CloudTrail event or the name of an
    AWS Config rule.
  - The Audit Manager API refers to a data source mapping as a [sourceKeyword](../APIReference/API_SourceKeyword.md "../APIReference/API_SourceKeyword.md").

- A **data source name** labels the pairing of a data source
  type and mapping.
  - For standard controls, Audit Manager provides a default name.
  - For custom controls, you can provide your own name.
  - The Audit Manager API refers to a data source name as a [sourceName](../APIReference/API_ControlMappingSource.md#auditmanager-Type-ControlMappingSource-sourceName "../APIReference/API_ControlMappingSource.md#auditmanager-Type-ControlMappingSource-sourceName").

A single control can have multiple data source types and multiple mappings. For
example, one control might collect evidence from a mixture of data source types (such
as AWS Config and Security Hub). Another control might have AWS Config as its only data source
type, with multiple AWS Config rules as mappings.

The following table lists the automated data source types and shows examples of
some corresponding mappings.

| Data source type | Description                                                                                                                                                                                                                                         | Mapping example     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- |
| AWS Security Hub | Use this data source type to capture a snapshot of your resource<br>security posture.<br>Audit Manager uses the name of a Security Hub control as the mapping keyword, and<br>reports the result of that security check directly from Security Hub. | `EC2.1`             |
| AWS Config       | Use this data source type to capture a snapshot of your resource<br>security posture.<br>Audit Manager uses the name of an AWS Config rule as the mapping keyword, and<br>reports the result of that rule check directly from AWS Config.           | `SNS_ENCRYPTED_KMS` |
| AWS CloudTrail   | Use this data source type to track a specific user activity that's<br>needed in your audit.<br>Audit Manager uses the name of a CloudTrail event as the mapping keyword, and collects<br>the related user activity from your CloudTrail logs.       | `CreateAccessKey`   |
| AWS API calls    | Use this data source type to take a snapshot of your resource<br>configuration through an API call to a specific AWS service.<br>Audit Manager uses the name of API call as the mapping keyword, and collects the<br>API response.                  | `kms_ListKeys`      |

**Delegate**

A delegate is an AWS Audit Manager user with limited permissions. Delegates typically have
specialized business or technical expertise. For example, these expertise might be in
data retention policies, training plans, network infrastructure, or identity
management. Delegates help audit owners review collected evidence for controls that
are in their area of expertise. Delegates can review control sets and their related
evidence, add comments, upload additional evidence, and update the status of each of
the controls that you assign to them for review.

Audit owners assign specific control sets to delegates, not entire assessments. As
a result, delegates have limited access to assessments. For instructions on how to
delegate a control set, see [Delegations in AWS Audit Manager](delegate.md "delegate.md").

## E

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | E | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Evidence**

Evidence is a record that contains the information that's needed to demonstrate
compliance with a control's requirements. Examples of evidence include a change
activity invoked by a user, and a system configuration snapshot.

There are two main types of evidence in Audit Manager: _automated
evidence_ and _manual evidence_.

| Evidence type          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Automated evidence** | This is the evidence that Audit Manager collects automatically. This<br>includes the following three categories of automated evidence:<br>1. **Compliance check\*<br>• — The result<br>of a compliance check is captured from AWS Security Hub, AWS Config, or both.<br>Examples of compliance checks include a security check result from<br>Security Hub for a PCI DSS control, and an AWS Config rule evaluation for a HIPAA<br>control.<br>For more information, see [AWS Config Rules supported by AWS Audit Manager](control-data-sources-config.md "control-data-sources-config.md") and [AWS Security Hub controls supported by AWS Audit Manager](control-data-sources-ash.md "control-data-sources-ash.md").<br>2. **User activity**— User activity<br>that changes a resource configuration is captured from CloudTrail logs as that<br>activity occurs.<br>Examples of user activities include a route table update, an Amazon RDS<br>instance backup setting change, and an S3 bucket encryption policy<br>change.<br>For more information, see [AWS CloudTrail event names supported by<br>AWS Audit Manager](control-data-sources-cloudtrail.md "control-data-sources-cloudtrail.md").<br>3. **Configuration data\*<br>• — A<br>snapshot of the resource configuration is captured directly from an<br>AWS service on a daily, weekly, or monthly basis.<br>Examples of configuration snapshots include a list of routes for a<br>VPC route table, an Amazon RDS instance backup setting, and an S3 bucket<br>encryption policy.<br>For more information, see [AWS API calls supported by AWS Audit Manager](control-data-sources-api.md "control-data-sources-api.md"). |
| **Manual evidence**    | This is the evidence that you add to Audit Manager yourself. There are three ways<br>to add your own evidence:<br>1. Import a file from Amazon S3<br>2. Upload a file from your browser<br>3. Enter a text response to a risk assessment question<br>For more information, see [Adding manual evidence in AWS Audit Manager](upload-evidence.md "upload-evidence.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

Automated evidence collection starts when you create an assessment. This is an
ongoing process, and Audit Manager collects evidence at different frequencies depending on the
evidence type and the underlying data source. For more information, see [Understanding how AWS Audit Manager collects
evidence](how-evidence-is-collected.md "how-evidence-is-collected.md").

For instructions on how to review evidence in an assessment, see [Reviewing evidence in AWS Audit Manager](review-evidence.md "review-evidence.md").

**Evidence source**

An evidence source defines where a control collects evidence from. It can be an
individual data source, or a predefined grouping of data sources that maps to a common
control or a core control.

When you create a custom control, you can collect evidence from AWS
managed sources, customer managed sources, or both.

###### Tip

We recommend that you use AWS managed sources. Whenever an AWS managed source is updated,
the same updates are automatically applied to all custom controls that use these
sources. This means that your custom controls always collect evidence against the
latest definitions of that evidence source. This helps you to ensure continuous
compliance as the cloud compliance environment changes.

See also: [AWS managed source](#aws-managed-source "#aws-managed-source"),
[customer managed source](#customer-managed-source "#customer-managed-source").

**Evidence collection method**

There are two ways that a control can collect evidence.

| Evidence collection method | Description                                                                                                                                                                     |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Automated**              | Automated controls automatically collect evidence from AWS data<br>sources. This automated evidence can help you to demonstrate full or partial<br>compliance with the control. |
| **Manual**                 | Manual controls require you to [upload your own<br>evidence](upload-evidence.md "upload-evidence.md") to demonstrate compliance with the control.                               |

###### Note

You can attach manual evidence to any automated control. In many cases, a
combination of automated and manual evidence is needed to demonstrate full
compliance with a control. Although Audit Manager can provide automated evidence that’s
helpful and relevant, some automated evidence might only demonstrate partial
compliance. In this case, you can supplement the automated evidence that Audit Manager
provides with your own evidence.

For example:

- The [AWS Generative AI Best Practices
  Framework v2](aws-generative-ai-best-practices.md "aws-generative-ai-best-practices.md") contains a control
  called `Error analysis`. This control requires you to identify when
  inaccuracies are detected in your model usage. It also requires you to conduct a
  thorough error analysis to understand the root causes and take corrective
  action.
- To support this control, Audit Manager collects automated evidence that shows if CloudWatch
  alarms are enabled for the AWS account where your assessment is running. You
  can use this evidence to demonstrate partial compliance with the control by
  proving that your alarms and checks are configured correctly.
- To demonstrate full compliance, you can supplement the automated evidence
  with manual evidence. For example, you can upload a policy or a procedure that
  shows your error analysis process, your thresholds for escalations and
  reporting, and the results of your root cause analysis. You can use this manual
  evidence to demonstrate that established policies are in place, and that
  corrective action was taken when prompted.
  For a more detailed example, see [Controls with mixed data sources](examples-of-controls.md#mixed "examples-of-controls.md#mixed").

**Export destination**

An export destination is the default S3 bucket where Audit Manager saves the files that you
export from evidence finder. For more information, see [Configuring your default export
destination for evidence finder](settings-export-destination.md "settings-export-destination.md").

## F

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | F | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Framework**

An Audit Manager framework structures and automate assessments for a specific standard or
risk governance principle. These frameworks include a collection of prebuilt or
customer defined controls, and they help you to map your AWS resources to the
requirements of these controls.

There are two types of framework in Audit Manager.

| Framework type         | Description                                                                                                                                                                                                                                                              |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Standard framework** | This is a prebuilt framework that is based on AWS best practices for<br>various compliance standards and regulations.<br>You can use standard frameworks to assist with audit preparation for a<br>specific compliance standard or regulation, such as PCI DSS or HIPAA. |
| **Custom framework**   | This is a customized frameworks that you define as an Audit Manager user.<br>You can use custom frameworks to assist with audit preparation according<br>to your specific GRC requirements.                                                                              |

For instructions on how to create and manage frameworks, see [Using the framework library to manage frameworks in
AWS Audit Manager](framework-library.md "framework-library.md").

###### Note

AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance
with specific compliance standards and regulations. However, it doesn't assess your
compliance itself. The evidence that's collected through AWS Audit Manager therefore might
not include all the information about your AWS usage that's needed for audits.
AWS Audit Manager isn't a substitute for legal counsel or compliance experts.

**Framework sharing**

You can use the [Sharing a custom framework in AWS Audit Manager](share-custom-framework.md "share-custom-framework.md") feature to quickly share your custom
frameworks across AWS accounts and Regions. To share a custom framework, you create
a _share request._ The recipient then has 120 days to
accept or decline the request. When they accept, Audit Manager replicates the shared custom
framework into their framework library. In addition to replicating the custom
framework, Audit Manager also replicates any custom control sets and controls that are
contained within that framework. These custom controls are added to the recipient’s
control library. Audit Manager doesn’t replicate standard frameworks or controls. This is
because these resources are already available by default in each account and
Region.

## I

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | I | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Inconclusive Evidence**

AWS Audit Manager marks evidence as inconclusive when automated compliance evaluation isn't
possible. This occurs in the following situations:

- You haven't enabled AWS Config or AWS Security Hub, which are key data sources.
- Evidence is collected directly from AWS services via API calls, AWS CloudTrail
  logs, or manual uploads.

When there's no mechanism for automatic evaluation of this evidence, AWS Audit Manager
can't provide evaluation details. As a result, it marks the evidence as
_inconclusive_.

###### Important

Inconclusive evidence doesn't indicate failure. Instead, it signals that you
need to manually evaluate the evidence for compliance.

## R

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | R | [S](#auditmanager-concepts-S "#auditmanager-concepts-S") | T | U | V | W | X | Y | Z

**Resource**

A resource is a physical or information asset that's assessed in an audit.
Examples of AWS resources include Amazon EC2 instances, Amazon RDS instances, Amazon S3 buckets,
and Amazon VPC subnets.

**Resource assessment**

A resource assessment is the process of assessing an individual resource. This
assessment is based on the requirement of a control. While an assessment is active,
Audit Manager runs resource assessments for each individual resource in the scope of the
assessment. A resource assessment runs the following set of tasks:

1. Collects evidence including resource configurations, event logs, and
   findings
2. Translates and maps evidence to controls
3. Stores and tracks the lineage of evidence to enable integrity

**Resource
compliance**

Resource compliance refers to the evaluation status of a resource that was
assessed when collecting compliance check evidence.

Audit Manager collects compliance check evidence for controls that use AWS Config and Security Hub
as a data source type. Multiple resources might be assessed during this evidence
collection. As a result, a single piece of compliance check evidence can include one
or more resources.

You can use the **Resource compliance** filter in evidence finder
to explore compliance status at the resource level. After your search is complete, you
can then preview the resources that matched your search query.

In evidence finder, there are three possible values for resource
compliance:

| Value             | Description                                                                                                                                                                                                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Non-compliant** | This refers to resources with compliance check issues.<br>This happens if Security Hub reports a *Fail<br>• result for the resource, or if AWS Config reports a<br>*Non-compliant<br>• result.                                                                                                                                                                           |
| **Compliant**     | This refers to resources that don’t have compliance check issues.<br>This happens if Security Hub reports a _Pass_<br>result for the resource, or if AWS Config reports a \*Compliant<br>• result.                                                                                                                                                                       |
| **Inconclusive**  | This refers to resources for which a compliance check isn’t available or<br>applicable.<br>This happens if AWS Config or Security Hub is the underlying data source type,<br>but those services aren't enabled.<br>This also happens if the underlying data source type doesn't support<br>compliance checks (such as manual evidence, AWS API calls, or<br>CloudTrail). |

## S

[A](#auditmanager-concepts-A "#auditmanager-concepts-A") | B | [C](#auditmanager-concepts-C "#auditmanager-concepts-C") | [D](#auditmanager-concepts-D "#auditmanager-concepts-D") | [E](#auditmanager-concepts-E "#auditmanager-concepts-E") | [F](#auditmanager-concepts-F "#auditmanager-concepts-F") | G | H | [I](#auditmanager-concepts-I "#auditmanager-concepts-I") | J | K | L | M | N | O | P
| Q | [R](#auditmanager-concepts-R "#auditmanager-concepts-R") | S | T | U | V | W | X | Y | Z

**Service in scope**

Audit Manager manages which AWS services are in scope for your assessments. If you have
an older assessment, it’s possible that you manually specified the services in scope
in the past. After June 04, 2024, you can’t manually specify or edit services in
scope.

A _service in scope_ is an AWS service that
your assessment collects evidence about. When a service is included in the scope of
your assessment, Audit Manager assesses that service's resources. Some example resources
include the following:

- An Amazon EC2 instance
- An S3 bucket
- An IAM user or role
- A DynamoDB table
- A network component such as an Amazon Virtual Private Cloud (VPC), security group, or network
  access control list (ACL) table

For example, if Amazon S3 is a service in scope, Audit Manager can collect evidence about your
S3 buckets. The exact evidence that's collected is determined by a control's [data source](#control-data-source "#control-data-source"). For instance,
if the data source type is AWS Config, and the data source mapping is an AWS Config rule (such as
`s3-bucket-public-write-prohibited`), Audit Manager collects the result of that
rule evaluation as evidence.

###### Note

Keep in mind that a service in scope is different to a _data source type_, which can also be an AWS service or something
else. For more information, see [What's the
difference between a service in scope and a data source type?](evidence-collection-issues.md#data-source-vs-service-in-scope "evidence-collection-issues.md#data-source-vs-service-in-scope") in the _Troubleshooting_ section of this guide.

**Standard control**

See [control](#control "#control").
