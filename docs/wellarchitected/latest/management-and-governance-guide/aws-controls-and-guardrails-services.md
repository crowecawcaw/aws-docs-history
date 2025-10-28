# Control services

The following AWS services can be used to help you follow the
guidance provided by the M&G Guide:

[AWS Organizations](https://aws.amazon.com/organizations/ "https://aws.amazon.com/organizations/") includes service control policies (SCPs) that
you can use to provide centralized control over all accounts in
your organization. You can configure an SCP to define a guardrail,
or set a limit, on the actions that the account’s administrator
can delegate to the users and roles for the affected accounts. The
administrator must still attach identity-based or resource-based
policies to IAM roles, or to the resources in your accounts to
actually grant permissions. The
[effective
permissions](../../../organizations/latest/userguide/orgs_manage_policies_scps.md#scp-effects-on-permissions "../../../organizations/latest/userguide/orgs_manage_policies_scps.md#scp-effects-on-permissions") are the logical intersection between what is
allowed by the SCP and what is allowed by IAM and the
resource-based policies.

[AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") complements AWS Organizations by implementing
preventive and detective controls as you provision accounts. You
can quickly set up and configure a new AWS environment, automate
ongoing policy management, and view policy-level summaries of your
AWS environments.

[AWS Security Hub](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") provides a single place that aggregates,
organizes, and prioritizes your security alerts, or findings, from
multiple AWS services. These include Amazon GuardDuty, Amazon Inspector, Amazon Macie, AWS Firewall Manager, AWS Systems Manager
Patch Manager, AWS Config, AWS IAM Access Analyzer, as well as
from many AWS Partner Network (APN) solutions.

[Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") is a threat detection service that continually
monitors for malicious activity and unintended behavior to protect
your AWS accounts, workloads, and data stored in Amazon S3. Amazon GuardDuty uses machine learning, anomaly detection, and integrated
threat intelligence to identify and prioritize potential threats.
GuardDuty analyzes tens of billions of events across multiple AWS
data sources, such as AWS CloudTrail event logs, Amazon VPC Flow
Logs, and DNS logs.

[Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") gives you constant visibility of the data security
and data privacy of your data stored in Amazon S3. Macie
automatically and continually evaluates all of your S3 buckets and
alerts you to any unencrypted buckets, publicly accessible
buckets, or buckets shared with AWS accounts outside those you
have defined in the AWS Organizations.

In [AWS Config](https://aws.amazon.com/config/ "https://aws.amazon.com/config/"), you to create and manage singular rules (detective
controls), or group them as conformance packs. [AWS Config
conformance packs](../../../config/latest/developerguide/conformance-packs.md "../../../config/latest/developerguide/conformance-packs.md") help you manage configuration compliance of your
AWS resources at scale – from policy definition to auditing and
aggregated reporting – using a common framework and packaging
model. Additionally, AWS Config conformance packs enable you to
simplify compliance reporting, as it is now reported at a new
level - the pack level alongside the detailed view for each
individual rule and resource level.

The
[AWS Config Conformance Pack Sample Templates](../../../config/latest/developerguide/conformancepack-sample-templates.md "../../../config/latest/developerguide/conformancepack-sample-templates.md") help you create
your own conformance packs with different or additional rules,
input parameters, and remediation actions that suit your
environment. The sample templates, including many related to
compliance standards and industry benchmarks, are not designed to
ensure your compliance with a specific governance standard. They
cannot replace your internal efforts or ensure that you will pass a
compliance assessment.

[AWS Audit Manager](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/") helps you continually audit your AWS usage by
simplifying how you assess risk and compliance with regulations
and open standards. Audit Manager provides a fully customizable
framework that automates evidence collection, simplifies the
tracking of chain of custody for evidence, and manages evidence
security and integrity.

If you would like support implementing this guidance, or assisting
you with building the foundational elements prescribed by the
M&G Guide, we recommend you review the offerings provided by
[AWS Professional Services](https://aws.amazon.com/professional-services/ "https://aws.amazon.com/professional-services/") or the AWS Partners in the
[Built
on Control Tower program](https://aws.amazon.com/controltower/partners/ "https://aws.amazon.com/controltower/partners/").

If you are seeking help to operate your workloads in AWS following
this guidance,
[AWS Managed Services (AMS)](https://aws.amazon.com/managed-services/ "https://aws.amazon.com/managed-services/") can augment your operational
capabilities as a short-term accelerator or a long-term solution,
letting you focus on transforming your applications and businesses
in the cloud.
