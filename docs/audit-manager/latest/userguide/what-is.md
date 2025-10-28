# What is AWS Audit Manager?

Welcome to the AWS Audit Manager User Guide.

AWS Audit Manager helps you continually audit your AWS usage to simplify how you manage risk and
compliance with regulations and industry standards. Audit Manager automates evidence collection so you
can more easily assess whether your policies, procedures, and activities—also known as _controls_—are operating effectively. When it's time for an audit, Audit Manager
helps you manage stakeholder reviews of your controls. This means that you can build audit-ready
reports with much less manual effort.

Audit Manager provides prebuilt frameworks that structure and automate assessments for a given
compliance standard or regulation. Frameworks include a prebuilt collection of controls with
descriptions and testing procedures. These controls are grouped according to the requirements of
the specified compliance standard or regulation. You can also customize frameworks and controls
to support internal audits according to your specific requirements.

You can create an assessment from any framework. When you create an assessment, Audit Manager
automatically runs resource assessments. These assessments collect data for the AWS accounts
that you define as in scope for your audit. The data that's collected is automatically
transformed into audit-friendly evidence. Then, it's attached to the relevant controls to help
you demonstrate compliance in security, change management, business continuity, and software
licensing. This evidence collection process is ongoing, and starts when you create your
assessment. After you complete an audit and you no longer need Audit Manager to collect evidence, you can
stop evidence collection. To do this, change the status of your assessment to _inactive_.

## Features of Audit Manager

With AWS Audit Manager, you can do the following tasks:

- Get started quickly — [Create your first
  assessment](tutorial-for-audit-owners.md "tutorial-for-audit-owners.md") by selecting from a gallery of prebuilt frameworks that support a
  range of compliance standards and regulations. Then, initiate automatic evidence
  collection to audit your AWS service usage.
- Upload and manage evidence from hybrid or multicloud
  environments — In addition to the evidence that Audit Manager collects from your
  AWS environment, you can also [upload](upload-evidence.md "upload-evidence.md") and centrally
  manage evidence from your on-premises or multicloud environment.
- Support common compliance standards and regulations
  — Choose one of the [AWS Audit Manager standard
  frameworks](framework-overviews.md "framework-overviews.md"). These frameworks provide prebuilt control mappings for common
  compliance standards and regulations. These include the CIS Foundation Benchmark, PCI DSS,
  GDPR, HIPAA, SOC2, GxP, and AWS operational best practices.
- Monitor your active assessments — Use the Audit Manager
  [dashboard](dashboard.md "dashboard.md") to view analytics data for your active assessments, and quickly
  identify non-compliant evidence that needs to be remediated.
- Search for evidence — Use the [Evidence finder](evidence-finder.md "evidence-finder.md") feature to quickly find
  evidence that’s relevant to your search query. You can generate an assessment report from
  your search results, or export your search results in CSV format.
- **Create custom controls** — [Create your own
  control from scratch](customize-control-from-scratch.md "customize-control-from-scratch.md") or [make an
  editable copy of an existing standard control or custom control](customize-control-from-existing.md "customize-control-from-existing.md"). You can also
  use the custom controls feature to create risk assessment questions and store the
  responses to those questions as manual evidence.
- **Map your enterprise controls to predefined groupings of AWS
  data sources** — Choose the common controls that represent your goals,
  and use them to [create custom
  controls](customize-control-from-scratch.md "customize-control-from-scratch.md") that collect evidence for your portfolio of compliance needs.
- Create custom frameworks — [Create
  your own frameworks](custom-frameworks.md "custom-frameworks.md") with standard or custom controls based on your specific
  requirements for internal audits.
- Share custom frameworks —[Share your custom Audit Manager frameworks](share-custom-framework.md "share-custom-framework.md") with another AWS account, or replicate them
  into another AWS Region under your own account.
- Support cross-team collaboration — [Delegate control sets](delegate-for-audit-owners.md "delegate-for-audit-owners.md") to subject matter experts who can review related
  evidence, add comments, and update the status of each control.
- Create reports for auditors — [Generate
  assessment reports](generate-assessment-report.md "generate-assessment-report.md") that summarize the relevant evidence that's collected for
  your audit and link to folders that contain the detailed evidence.
- Ensure evidence integrity — [Store
  evidence](settings-destination.md "settings-destination.md") in a secure location, where it remains unaltered.

###### Note

AWS Audit Manager assists in collecting evidence that's relevant for verifying compliance with
specific compliance standards and regulations. However, it doesn't assess your compliance
itself. The evidence that's collected through AWS Audit Manager therefore might not include all the
information about your AWS usage that's needed for audits. AWS Audit Manager isn't a substitute for
legal counsel or compliance experts.

## Pricing for Audit Manager

For more information about pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/ "https://aws.amazon.com/audit-manager/pricing/").

## Are you a first-time user of Audit Manager?

If you're a first-time user of Audit Manager, we recommend that you start with the following pages:

1. [Understanding AWS Audit Manager concepts and terminology](concepts.md "concepts.md") – Learn about the key concepts and
   terms used in Audit Manager, such as assessments, frameworks, and controls.
2. [Understanding how AWS Audit Manager collects
   evidence](how-evidence-is-collected.md "how-evidence-is-collected.md") –
   Learn about how Audit Manager gathers evidence for a resource assessment.
3. [Setting up AWS Audit Manager with the recommended settings](setting-up.md "setting-up.md") – Learn about the setup
   requirements for Audit Manager.
4. [Getting started with AWS Audit Manager](getting-started.md "getting-started.md") – Follow a tutorial
   to create your first Audit Manager assessment.
5. [AWS Audit Manager API
   Reference](../APIReference/Welcome.md "../APIReference/Welcome.md") – Familiarize yourself with the Audit Manager API actions and data
   types.

## Related AWS services

AWS Audit Manager integrates with multiple AWS services to automatically collect evidence that
you can include in your assessment reports.

###### AWS Security Hub

AWS Security Hub monitors your environment using automated security checks that are based on
AWS best practices and industry standards. Audit Manager captures snapshots of your resource
security posture by reporting the results of security checks directly from Security Hub. For more
information about Security Hub, see [What is AWS Security Hub?](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") in
the _AWS Security Hub User Guide_.

###### AWS CloudTrail

AWS CloudTrail helps you monitor the calls made to AWS resources in your account. These
include calls made by the AWS Management Console, the AWS CLI, and other AWS services.
Audit Manager collects log data from CloudTrail directly, and converts the processed logs into user
activity evidence. For more information about CloudTrail, see [What is AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
in the _AWS CloudTrail User Guide_.

###### AWS Config

AWS Config provides a detailed view of the configuration of AWS resources in your
AWS account. This includes information about how resources are related to one another and
how they were configured in the past. Audit Manager captures snapshots of your resource security
posture by reporting findings directly from AWS Config. For more information about AWS Config, see
[What is
AWS Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") in the _AWS Config User Guide_.

###### AWS License Manager

AWS License Manager streamlines the process of bringing software vendor licenses to the cloud. As
you build out cloud infrastructure on AWS, you can save costs by repurposing your existing
license inventory for use with cloud resources. Audit Manager provides a License Manager framework to assist you with your audit preparation. This framework is integrated with License Manager to aggregate license usage information based on customer defined
licensing rules. For more information on License Manager, see [What is AWS License Manager?](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md") in
the _AWS License Manager User Guide_.

###### AWS Control Tower

AWS Control Tower enforces preventative and detective guardrails for cloud infrastructure.
Audit Manager provides an AWS Control Tower Guardrails framework to assist you with your audit
preparation. This framework contains all of the AWS Config rules that are based on
guardrails from AWS Control Tower. For more information about AWS Control Tower, see [What
is AWS Control Tower?](../../../controltower/latest/userguide/what-is-control-tower.md "../../../controltower/latest/userguide/what-is-control-tower.md") in the _AWS Control Tower User Guide_.

###### AWS Artifact

AWS Artifact is a self-service audit artifact retrieval portal that provides on-demand access
to the compliance documentation and certifications for AWS infrastructure. AWS Artifact offers
evidence to prove that the AWS Cloud infrastructure meets the compliance requirements. In
contrast, AWS Audit Manager helps you collect, review, and manage evidence to demonstrate that your
usage of AWS services is in compliance. For more information about AWS Artifact, see [What is
AWS Artifact?](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md") in the _AWS Artifact User Guide_. You can download a [list of AWS reports](https://console.aws.amazon.com/artifact/reports "https://console.aws.amazon.com/artifact/reports") in the
AWS Management Console.

###### Amazon EventBridge

Amazon EventBridge helps you automate your AWS services and respond automatically to system
events such as application availability issues or resource changes. You can use EventBridge rules
to detect and react to Audit Manager events. Based on the rules that you create, EventBridge invokes one or
more target actions when an event matches the values that you specify in a rule. For more
information, see [Monitoring AWS Audit Manager with Amazon EventBridge](automating-with-eventbridge.md "automating-with-eventbridge.md").

For a list of AWS services in scope of specific compliance programs, see [AWS services in Scope by Compliance
Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/"). For more general information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").

## More Audit Manager resources

Explore the following resources to learn more about Audit Manager.

- Video: Collect Evidence and Manage Audit Data Using AWS Audit Manager
- [Integrate across the Three Lines Model (Part 2): Transform AWS Config conformance packs into AWS Audit Manager assessments](https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-2-transform-aws-config-conformance-packs-into-aws-audit-manager-assessments/ "https://aws.amazon.com/blogs/mt/integrate-across-the-three-lines-model-part-2-transform-aws-config-conformance-packs-into-aws-audit-manager-assessments/") from the _AWS Management & Governance Blog_
