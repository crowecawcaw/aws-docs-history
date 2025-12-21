# Impact of consolidation on ASFF fields and

values

AWS Security Hub CSPM offers two types of consolidation for controls:

- **Consolidated controls view** – With this type of
  consolidation, each control has a single identifier across all standards. In addition, on
  the Security Hub CSPM console, the **Controls** page displays all controls across all
  standards.
- **Consolidated control findings** – With this type
  of consolidation, Security Hub CSPM produces a single finding for a control, even if the control applies
  to multiple enabled standards. This can reduce finding noise.
  You can't enable or disable consolidated controls view. Consolidated control findings is
  enabled by default if you enable Security Hub CSPM on or after February 23, 2023. Otherwise, it's disabled
  by default. However, for organizations, consolidated control findings is enabled for Security Hub CSPM
  member accounts only if it's enabled for the administrator account. To learn more about
  consolidated control findings, see [Generating and updating control findings](controls-findings-create-update.md "controls-findings-create-update.md").

Both types of consolidation affect fields and values for control findings in the [AWS Security Finding Format (ASFF)](securityhub-findings-format.md "securityhub-findings-format.md").

###### Topics

- [Consolidated controls
  view – ASFF changes](#securityhub-findings-format-consolidated-controls-view "#securityhub-findings-format-consolidated-controls-view")
- [Consolidated
  control findings – ASFF changes](#securityhub-findings-format-consolidated-control-findings "#securityhub-findings-format-consolidated-control-findings")
- [Generator IDs before and after
  enabling consolidated control findings](#securityhub-findings-format-changes-generator-ids "#securityhub-findings-format-changes-generator-ids")
- [How consolidation impacts
  control IDs and titles](#securityhub-findings-format-changes-ids-titles "#securityhub-findings-format-changes-ids-titles")
- [Updating workflows for
  consolidation](#securityhub-findings-format-changes-prepare "#securityhub-findings-format-changes-prepare")

## Consolidated controls

view – ASFF changes

The consolidated controls view feature introduced the following changes to fields and
values for control findings in the ASFF. If your workflows don’t rely on values for these ASFF
fields, no action is required. If you have workflows that rely on specific values for these
fields, update your workflows to use the current values.

| ASFF field                                  | Sample value before consolidated controls view                                                         | Sample value after consolidated controls view, and a description of the change                                                                                                                                                                                                   |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compliance.SecurityControlId                | Not applicable (new field)                                                                             | EC2.2<br>Introduces a single control ID across standards.<br>`ProductFields.RuleId` still provides the standard-based control ID for<br>CIS v1.2.0 controls. `ProductFields.ControlId` still provides the<br>standard-based control ID for controls in other standards.          |
| Compliance.AssociatedStandards              | Not applicable (new field)                                                                             | [{"StandardsId":<br>"standards/aws-foundational-security-best-practices/v/1.0.0"}]<br>Shows which standards a control is enabled in.                                                                                                                                             |
| ProductFields.ArchivalReasons:0/Description | Not applicable (new field)                                                                             | "The finding is in an ARCHIVED state because consolidated control findings has<br>been turned on or off. This causes findings in the previous state to be archived<br>when new findings are being generated."<br>Describes why Security Hub CSPM has archived existing findings. |
| ProductFields.ArchivalReasons:0/ReasonCode  | Not applicable (new field)                                                                             | "CONSOLIDATED_CONTROL_FINDINGS_UPDATE"<br>Provides the reason why Security Hub CSPM has archived existing findings.                                                                                                                                                              |
| ProductFields.RecommendationUrl             | https://docs.aws.amazon.com/console/securityhub/PCI.EC2.2/remediation                                  | https://docs.aws.amazon.com/console/securityhub/EC2.2/remediation<br>This field no longer references a standard.                                                                                                                                                                 |
| Remediation.Recommendation.Text             | "For directions on how to fix this issue, consult the AWS Security Hub CSPM PCI DSS<br>documentation." | "For directions on how to correct this issue, consult the AWS Security Hub CSPM controls<br>documentation."<br>This field no longer references a standard.                                                                                                                       |
| Remediation.Recommendation.Url              | https://docs.aws.amazon.com/console/securityhub/PCI.EC2.2/remediation                                  | https://docs.aws.amazon.com/console/securityhub/EC2.2/remediation<br>This field no longer references a standard.                                                                                                                                                                 |

## Consolidated

control findings – ASFF changes

If you enable consolidated control findings, you might be affected by the following
changes to fields and values for control findings in the ASFF. These changes are in addition
to the changes introduced by the consolidated controls view feature. If your workflows don’t
rely on values for these ASFF fields, no action is required. If you have workflows that rely
on specific values for these fields, update your workflows to use the current values.

###### Tip

If you use the [Automated Security Response on AWS v2.0.0](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/ "https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/") solution, note that it supports
consolidated control findings. This means that you can maintain your current workflows if
you enable consolidated control findings.

| ASFF field                                  | Example value before enabling consolidated control findings                                                                                                                                                           | Example value after enabling consolidated control findings, and a description of<br>the change                                                                                                                          |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GeneratorId                                 | aws-foundational-security-best-practices/v/1.0.0/Config.1                                                                                                                                                             | security-control/Config.1<br>This field no longer references a standard.                                                                                                                                                |
| Title                                       | PCI.Config.1 AWS Config should be enabled                                                                                                                                                                             | AWS Config should be enabled<br>This field no longer references standard-specific information.                                                                                                                          |
| Id                                          | arn:aws:securityhub:eu-central-1:123456789012:subscription/pci-dss/v/3.2.1/PCI.IAM.5/finding/ab6d6a26-a156-48f0-9403-115983e5a956                                                                                     | arn:aws:securityhub:eu-central-1:123456789012:security-control/iam.9/finding/ab6d6a26-a156-48f0-9403-115983e5a956<br>This field no longer references a standard.                                                        |
| ProductFields.ControlId                     | PCI.EC2.2                                                                                                                                                                                                             | Removed. See `Compliance.SecurityControlId` instead.<br>This field is removed in favor of a single, standard-agnostic control ID.                                                                                       |
| ProductFields.RuleId                        | 1.3                                                                                                                                                                                                                   | Removed. See `Compliance.SecurityControlId` instead.<br>This field is removed in favor of a single, standard-agnostic control ID.                                                                                       |
| Description                                 | This PCI DSS control checks whether AWS Config is enabled in the current account<br>and region.                                                                                                                       | This AWS control checks whether AWS Config is enabled in the current account and<br>region.This field no longer references a standard.                                                                                  |
| Severity                                    | "Severity": {<br>"Product": 90,<br>"Label": "CRITICAL",<br>"Normalized": 90,<br>"Original": "CRITICAL"<br>}                                                                                                           | "Severity": {<br>"Label": "CRITICAL",<br>"Normalized": 90,<br>"Original": "CRITICAL"<br>}<br>Security Hub CSPM no longer uses the Product field to describe the severity of a<br>finding.                               |
| Types                                       | ["Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS"]                                                                                                                                       | ["Software and Configuration Checks/Industry and Regulatory Standards"]<br>This field no longer references a standard.                                                                                                  |
| Compliance.RelatedRequirements              | ["PCI DSS 10.5.2",<br>"PCI DSS 11.5",<br>"CIS AWS Foundations 2.5"]                                                                                                                                                   | ["PCI DSS v3.2.1/10.5.2",<br>"PCI DSS v3.2.1/11.5",<br>"CIS AWS Foundations Benchmark v1.2.0/2.5"]<br>This field shows related requirements in all enabled standards.                                                   |
| CreatedAt                                   | 2022-05-05T08:18:13.138Z                                                                                                                                                                                              | 2022-09-25T08:18:13.138Z<br>Format remains the same, but value resets when you enable consolidated control<br>findings.                                                                                                 |
| FirstObservedAt                             | 2022-05-07T08:18:13.138Z                                                                                                                                                                                              | 2022-09-28T08:18:13.138Z Format remains the same, but value resets when you<br>enable consolidated control findings.                                                                                                    |
| ProductFields.RecommendationUrl             | https://docs.aws.amazon.com/console/securityhub/EC2.2/remediation                                                                                                                                                     | Removed. See `Remediation.Recommendation.Url` instead.                                                                                                                                                                  |
| ProductFields.StandardsArn                  | arn:aws:securityhub:::standards/aws-foundational-security-best-practices/v/1.0.0                                                                                                                                      | Removed. See `Compliance.AssociatedStandards` instead.                                                                                                                                                                  |
| ProductFields.StandardsControlArn           | arn:aws:securityhub:us-east-1:123456789012:control/aws-foundational-security-best-practices/v/1.0.0/Config.1                                                                                                          | Removed. Security Hub CSPM generates one finding for a security check across<br>standards.                                                                                                                              |
| ProductFields.StandardsGuideArn             | arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0                                                                                                                                                   | Removed. See `Compliance.AssociatedStandards` instead.                                                                                                                                                                  |
| ProductFields.StandardsGuideSubscriptionArn | arn:aws:securityhub:us-east-2:123456789012:subscription/cis-aws-foundations-benchmark/v/1.2.0                                                                                                                         | Removed. Security Hub CSPM generates one finding for a security check across<br>standards.                                                                                                                              |
| ProductFields.StandardsSubscriptionArn      | arn:aws:securityhub:us-east-1:123456789012:subscription/aws-foundational-security-best-practices/v/1.0.0                                                                                                              | Removed. Security Hub CSPM generates one finding for a security check across<br>standards.                                                                                                                              |
| ProductFields.aws/securityhub/FindingId     | arn:aws:securityhub:us-east-1::product/aws/securityhub/arn:aws:securityhub:us-east-1:123456789012:subscription/aws-foundational-security-best-practices/v/1.0.0/Config.1/finding/751c2173-7372-4e12-8656-a5210dfb1d67 | arn:aws:securityhub:us-east-1::product/aws/securityhub/arn:aws:securityhub:us-east-1:123456789012:security-control/Config.1/finding/751c2173-7372-4e12-8656-a5210dfb1d67<br>This field no longer references a standard. |

### Values for customer-provided ASFF fields after turning on consolidated control findings

If you enable consolidated control findings, Security Hub CSPM generates one finding across
standards and archives the original findings (separate findings for each standard).

Updates that you made to the original findings by using the Security Hub CSPM console or the [BatchUpdateFindings](finding-update-batchupdatefindings.md "finding-update-batchupdatefindings.md") operation won't be preserved in the new
findings. If necessary, you can recover this data by referring to the archived findings. To
review archived findings, you can use the **Findings** page on the Security Hub CSPM
console and set the **Record state** filter to
**ARCHIVED**. Alternatively, you can use the [GetFindings](../../1.0/APIReference/API_GetFindings.md "../../1.0/APIReference/API_GetFindings.md")
operation of the Security Hub CSPM API.

| Customer-provided ASFF field | Description of change after enabling consolidated control findings                                               |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Confidence                   | Resets to empty state.                                                                                           |
| Criticality                  | Resets to empty state.                                                                                           |
| Note                         | Resets to empty state.                                                                                           |
| RelatedFindings              | Resets to empty state.                                                                                           |
| Severity                     | Default severity of the finding (matches the severity of the<br>control).                                        |
| Types                        | Resets to standard-agnostic value.                                                                               |
| UserDefinedFields            | Resets to empty state.                                                                                           |
| VerificationState            | Resets to empty state.                                                                                           |
| Workflow                     | New failed findings have a default value of<br>`NEW`. New passed findings have a<br>default value of `RESOLVED`. |

## Generator IDs before and after

enabling consolidated control findings

The following table lists changes to generator ID values for controls when you enable
consolidated control findings. These changes apply to controls that Security Hub CSPM supported as of
February 15, 2023.

| GeneratorID before enabling consolidated control findings                     | GeneratorID after enabling consolidated control findings |
| ----------------------------------------------------------------------------- | -------------------------------------------------------- |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.1  | security-control/CloudWatch.1                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.10 | security-control/IAM.16                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.11 | security-control/IAM.17                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.12 | security-control/IAM.4                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.13 | security-control/IAM.9                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.14 | security-control/IAM.6                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.16 | security-control/IAM.2                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.2  | security-control/IAM.5                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.20 | security-control/IAM.18                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.22 | security-control/IAM.1                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.3  | security-control/IAM.8                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.4  | security-control/IAM.3                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.5  | security-control/IAM.11                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.6  | security-control/IAM.12                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.7  | security-control/IAM.13                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.8  | security-control/IAM.14                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.9  | security-control/IAM.15                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.1  | security-control/CloudTrail.1                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.2  | security-control/CloudTrail.4                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.3  | security-control/CloudTrail.6                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.4  | security-control/CloudTrail.5                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.5  | security-control/Config.1                                |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.6  | security-control/CloudTrail.7                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.7  | security-control/CloudTrail.2                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.8  | security-control/KMS.4                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/2.9  | security-control/EC2.6                                   |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.1  | security-control/CloudWatch.2                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.2  | security-control/CloudWatch.3                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.3  | security-control/CloudWatch.1                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.4  | security-control/CloudWatch.4                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.5  | security-control/CloudWatch.5                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.6  | security-control/CloudWatch.6                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.7  | security-control/CloudWatch.7                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.8  | security-control/CloudWatch.8                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.9  | security-control/CloudWatch.9                            |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.10 | security-control/CloudWatch.10                           |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.11 | security-control/CloudWatch.11                           |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.12 | security-control/CloudWatch.12                           |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.13 | security-control/CloudWatch.13                           |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/3.14 | security-control/CloudWatch.14                           |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/4.1  | security-control/EC2.13                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/4.2  | security-control/EC2.14                                  |
| arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/4.3  | security-control/EC2.2                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.10                                    | security-control/IAM.5                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.14                                    | security-control/IAM.3                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.16                                    | security-control/IAM.1                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.17                                    | security-control/IAM.18                                  |
| cis-aws-foundations-benchmark/v/1.4.0/1.4                                     | security-control/IAM.4                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.5                                     | security-control/IAM.9                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.6                                     | security-control/IAM.6                                   |
| cis-aws-foundations-benchmark/v/1.4.0/1.7                                     | security-control/CloudWatch.1                            |
| cis-aws-foundations-benchmark/v/1.4.0/1.8                                     | security-control/IAM.15                                  |
| cis-aws-foundations-benchmark/v/1.4.0/1.9                                     | security-control/IAM.16                                  |
| cis-aws-foundations-benchmark/v/1.4.0/2.1.2                                   | security-control/S3.5                                    |
| cis-aws-foundations-benchmark/v/1.4.0/2.1.5.1                                 | security-control/S3.1                                    |
| cis-aws-foundations-benchmark/v/1.4.0/2.1.5.2                                 | security-control/S3.8                                    |
| cis-aws-foundations-benchmark/v/1.4.0/2.2.1                                   | security-control/EC2.7                                   |
| cis-aws-foundations-benchmark/v/1.4.0/2.3.1                                   | security-control/RDS.3                                   |
| cis-aws-foundations-benchmark/v/1.4.0/3.1                                     | security-control/CloudTrail.1                            |
| cis-aws-foundations-benchmark/v/1.4.0/3.2                                     | security-control/CloudTrail.4                            |
| cis-aws-foundations-benchmark/v/1.4.0/3.4                                     | security-control/CloudTrail.5                            |
| cis-aws-foundations-benchmark/v/1.4.0/3.5                                     | security-control/Config.1                                |
| cis-aws-foundations-benchmark/v/1.4.0/3.6                                     | security-control/S3.9                                    |
| cis-aws-foundations-benchmark/v/1.4.0/3.7                                     | security-control/CloudTrail.2                            |
| cis-aws-foundations-benchmark/v/1.4.0/3.8                                     | security-control/KMS.4                                   |
| cis-aws-foundations-benchmark/v/1.4.0/3.9                                     | security-control/EC2.6                                   |
| cis-aws-foundations-benchmark/v/1.4.0/4.3                                     | security-control/CloudWatch.1                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.4                                     | security-control/CloudWatch.4                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.5                                     | security-control/CloudWatch.5                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.6                                     | security-control/CloudWatch.6                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.7                                     | security-control/CloudWatch.7                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.8                                     | security-control/CloudWatch.8                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.9                                     | security-control/CloudWatch.9                            |
| cis-aws-foundations-benchmark/v/1.4.0/4.10                                    | security-control/CloudWatch.10                           |
| cis-aws-foundations-benchmark/v/1.4.0/4.11                                    | security-control/CloudWatch.11                           |
| cis-aws-foundations-benchmark/v/1.4.0/4.12                                    | security-control/CloudWatch.12                           |
| cis-aws-foundations-benchmark/v/1.4.0/4.13                                    | security-control/CloudWatch.13                           |
| cis-aws-foundations-benchmark/v/1.4.0/4.14                                    | security-control/CloudWatch.14                           |
| cis-aws-foundations-benchmark/v/1.4.0/5.1                                     | security-control/EC2.21                                  |
| cis-aws-foundations-benchmark/v/1.4.0/5.3                                     | security-control/EC2.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/Account.1                    | security-control/Account.1                               |
| aws-foundational-security-best-practices/v/1.0.0/ACM.1                        | security-control/ACM.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.1                 | security-control/APIGateway.1                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.2                 | security-control/APIGateway.2                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.3                 | security-control/APIGateway.3                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.4                 | security-control/APIGateway.4                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.5                 | security-control/APIGateway.5                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.8                 | security-control/APIGateway.8                            |
| aws-foundational-security-best-practices/v/1.0.0/APIGateway.9                 | security-control/APIGateway.9                            |
| aws-foundational-security-best-practices/v/1.0.0/AutoScaling.1                | security-control/AutoScaling.1                           |
| aws-foundational-security-best-practices/v/1.0.0/AutoScaling.2                | security-control/AutoScaling.2                           |
| aws-foundational-security-best-practices/v/1.0.0/AutoScaling.3                | security-control/AutoScaling.3                           |
| aws-foundational-security-best-practices/v/1.0.0/Autoscaling.5                | security-control/Autoscaling.5                           |
| aws-foundational-security-best-practices/v/1.0.0/AutoScaling.6                | security-control/AutoScaling.6                           |
| aws-foundational-security-best-practices/v/1.0.0/AutoScaling.9                | security-control/AutoScaling.9                           |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.1                 | security-control/CloudFront.1                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.3                 | security-control/CloudFront.3                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.4                 | security-control/CloudFront.4                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.5                 | security-control/CloudFront.5                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.6                 | security-control/CloudFront.6                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.7                 | security-control/CloudFront.7                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.8                 | security-control/CloudFront.8                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.9                 | security-control/CloudFront.9                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.10                | security-control/CloudFront.10                           |
| aws-foundational-security-best-practices/v/1.0.0/CloudFront.12                | security-control/CloudFront.12                           |
| aws-foundational-security-best-practices/v/1.0.0/CloudTrail.1                 | security-control/CloudTrail.1                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudTrail.2                 | security-control/CloudTrail.2                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudTrail.4                 | security-control/CloudTrail.4                            |
| aws-foundational-security-best-practices/v/1.0.0/CloudTrail.5                 | security-control/CloudTrail.5                            |
| aws-foundational-security-best-practices/v/1.0.0/CodeBuild.1                  | security-control/CodeBuild.1                             |
| aws-foundational-security-best-practices/v/1.0.0/CodeBuild.2                  | security-control/CodeBuild.2                             |
| aws-foundational-security-best-practices/v/1.0.0/CodeBuild.3                  | security-control/CodeBuild.3                             |
| aws-foundational-security-best-practices/v/1.0.0/CodeBuild.4                  | security-control/CodeBuild.4                             |
| aws-foundational-security-best-practices/v/1.0.0/Config.1                     | security-control/Config.1                                |
| aws-foundational-security-best-practices/v/1.0.0/DMS.1                        | security-control/DMS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/DynamoDB.1                   | security-control/DynamoDB.1                              |
| aws-foundational-security-best-practices/v/1.0.0/DynamoDB.2                   | security-control/DynamoDB.2                              |
| aws-foundational-security-best-practices/v/1.0.0/DynamoDB.3                   | security-control/DynamoDB.3                              |
| aws-foundational-security-best-practices/v/1.0.0/EC2.1                        | security-control/EC2.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.3                        | security-control/EC2.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.4                        | security-control/EC2.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.6                        | security-control/EC2.6                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.7                        | security-control/EC2.7                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.8                        | security-control/EC2.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.9                        | security-control/EC2.9                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.10                       | security-control/EC2.10                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.15                       | security-control/EC2.15                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.16                       | security-control/EC2.16                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.17                       | security-control/EC2.17                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.18                       | security-control/EC2.18                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.19                       | security-control/EC2.19                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.2                        | security-control/EC2.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/EC2.20                       | security-control/EC2.20                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.21                       | security-control/EC2.21                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.23                       | security-control/EC2.23                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.24                       | security-control/EC2.24                                  |
| aws-foundational-security-best-practices/v/1.0.0/EC2.25                       | security-control/EC2.25                                  |
| aws-foundational-security-best-practices/v/1.0.0/ECR.1                        | security-control/ECR.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECR.2                        | security-control/ECR.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECR.3                        | security-control/ECR.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.1                        | security-control/ECS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.10                       | security-control/ECS.10                                  |
| aws-foundational-security-best-practices/v/1.0.0/ECS.12                       | security-control/ECS.12                                  |
| aws-foundational-security-best-practices/v/1.0.0/ECS.2                        | security-control/ECS.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.3                        | security-control/ECS.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.4                        | security-control/ECS.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.5                        | security-control/ECS.5                                   |
| aws-foundational-security-best-practices/v/1.0.0/ECS.8                        | security-control/ECS.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/EFS.1                        | security-control/EFS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/EFS.2                        | security-control/EFS.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/EFS.3                        | security-control/EFS.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/EFS.4                        | security-control/EFS.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/EKS.2                        | security-control/EKS.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/ElasticBeanstalk.1           | security-control/ElasticBeanstalk.1                      |
| aws-foundational-security-best-practices/v/1.0.0/ElasticBeanstalk.2           | security-control/ElasticBeanstalk.2                      |
| aws-foundational-security-best-practices/v/1.0.0/ELBv2.1                      | security-control/ELB.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.2                        | security-control/ELB.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.3                        | security-control/ELB.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.4                        | security-control/ELB.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.5                        | security-control/ELB.5                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.6                        | security-control/ELB.6                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.7                        | security-control/ELB.7                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.8                        | security-control/ELB.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.9                        | security-control/ELB.9                                   |
| aws-foundational-security-best-practices/v/1.0.0/ELB.10                       | security-control/ELB.10                                  |
| aws-foundational-security-best-practices/v/1.0.0/ELB.11                       | security-control/ELB.11                                  |
| aws-foundational-security-best-practices/v/1.0.0/ELB.12                       | security-control/ELB.12                                  |
| aws-foundational-security-best-practices/v/1.0.0/ELB.13                       | security-control/ELB.13                                  |
| aws-foundational-security-best-practices/v/1.0.0/ELB.14                       | security-control/ELB.14                                  |
| aws-foundational-security-best-practices/v/1.0.0/EMR.1                        | security-control/EMR.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/ES.1                         | security-control/ES.1                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.2                         | security-control/ES.2                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.3                         | security-control/ES.3                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.4                         | security-control/ES.4                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.5                         | security-control/ES.5                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.6                         | security-control/ES.6                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.7                         | security-control/ES.7                                    |
| aws-foundational-security-best-practices/v/1.0.0/ES.8                         | security-control/ES.8                                    |
| aws-foundational-security-best-practices/v/1.0.0/GuardDuty.1                  | security-control/GuardDuty.1                             |
| aws-foundational-security-best-practices/v/1.0.0/IAM.1                        | security-control/IAM.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.2                        | security-control/IAM.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.21                       | security-control/IAM.21                                  |
| aws-foundational-security-best-practices/v/1.0.0/IAM.3                        | security-control/IAM.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.4                        | security-control/IAM.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.5                        | security-control/IAM.5                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.6                        | security-control/IAM.6                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.7                        | security-control/IAM.7                                   |
| aws-foundational-security-best-practices/v/1.0.0/IAM.8                        | security-control/IAM.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/Kinesis.1                    | security-control/Kinesis.1                               |
| aws-foundational-security-best-practices/v/1.0.0/KMS.1                        | security-control/KMS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/KMS.2                        | security-control/KMS.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/KMS.3                        | security-control/KMS.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/Lambda.1                     | security-control/Lambda.1                                |
| aws-foundational-security-best-practices/v/1.0.0/Lambda.2                     | security-control/Lambda.2                                |
| aws-foundational-security-best-practices/v/1.0.0/Lambda.5                     | security-control/Lambda.5                                |
| aws-foundational-security-best-practices/v/1.0.0/NetworkFirewall.3            | security-control/NetworkFirewall.3                       |
| aws-foundational-security-best-practices/v/1.0.0/NetworkFirewall.4            | security-control/NetworkFirewall.4                       |
| aws-foundational-security-best-practices/v/1.0.0/NetworkFirewall.5            | security-control/NetworkFirewall.5                       |
| aws-foundational-security-best-practices/v/1.0.0/NetworkFirewall.6            | security-control/NetworkFirewall.6                       |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.1                 | security-control/Opensearch.1                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.2                 | security-control/Opensearch.2                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.3                 | security-control/Opensearch.3                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.4                 | security-control/Opensearch.4                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.5                 | security-control/Opensearch.5                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.6                 | security-control/Opensearch.6                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.7                 | security-control/Opensearch.7                            |
| aws-foundational-security-best-practices/v/1.0.0/Opensearch.8                 | security-control/Opensearch.8                            |
| aws-foundational-security-best-practices/v/1.0.0/RDS.1                        | security-control/RDS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.10                       | security-control/RDS.10                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.11                       | security-control/RDS.11                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.12                       | security-control/RDS.12                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.13                       | security-control/RDS.13                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.14                       | security-control/RDS.14                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.15                       | security-control/RDS.15                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.16                       | security-control/RDS.16                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.17                       | security-control/RDS.17                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.19                       | security-control/RDS.19                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.2                        | security-control/RDS.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.20                       | security-control/RDS.20                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.21                       | security-control/RDS.21                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.22                       | security-control/RDS.22                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.23                       | security-control/RDS.23                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.24                       | security-control/RDS.24                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.25                       | security-control/RDS.25                                  |
| aws-foundational-security-best-practices/v/1.0.0/RDS.3                        | security-control/RDS.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.4                        | security-control/RDS.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.5                        | security-control/RDS.5                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.6                        | security-control/RDS.6                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.7                        | security-control/RDS.7                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.8                        | security-control/RDS.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/RDS.9                        | security-control/RDS.9                                   |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.1                   | security-control/Redshift.1                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.2                   | security-control/Redshift.2                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.3                   | security-control/Redshift.3                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.4                   | security-control/Redshift.4                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.6                   | security-control/Redshift.6                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.7                   | security-control/Redshift.7                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.8                   | security-control/Redshift.8                              |
| aws-foundational-security-best-practices/v/1.0.0/Redshift.9                   | security-control/Redshift.9                              |
| aws-foundational-security-best-practices/v/1.0.0/S3.1                         | security-control/S3.1                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.12                        | security-control/S3.12                                   |
| aws-foundational-security-best-practices/v/1.0.0/S3.13                        | security-control/S3.13                                   |
| aws-foundational-security-best-practices/v/1.0.0/S3.2                         | security-control/S3.2                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.3                         | security-control/S3.3                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.5                         | security-control/S3.5                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.6                         | security-control/S3.6                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.8                         | security-control/S3.8                                    |
| aws-foundational-security-best-practices/v/1.0.0/S3.9                         | security-control/S3.9                                    |
| aws-foundational-security-best-practices/v/1.0.0/SageMaker.1                  | security-control/SageMaker.1                             |
| aws-foundational-security-best-practices/v/1.0.0/SageMaker.2                  | security-control/SageMaker.2                             |
| aws-foundational-security-best-practices/v/1.0.0/SageMaker.3                  | security-control/SageMaker.3                             |
| aws-foundational-security-best-practices/v/1.0.0/SecretsManager.1             | security-control/SecretsManager.1                        |
| aws-foundational-security-best-practices/v/1.0.0/SecretsManager.2             | security-control/SecretsManager.2                        |
| aws-foundational-security-best-practices/v/1.0.0/SecretsManager.3             | security-control/SecretsManager.3                        |
| aws-foundational-security-best-practices/v/1.0.0/SecretsManager.4             | security-control/SecretsManager.4                        |
| aws-foundational-security-best-practices/v/1.0.0/SQS.1                        | security-control/SQS.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/SSM.1                        | security-control/SSM.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/SSM.2                        | security-control/SSM.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/SSM.3                        | security-control/SSM.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/SSM.4                        | security-control/SSM.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.1                        | security-control/WAF.1                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.2                        | security-control/WAF.2                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.3                        | security-control/WAF.3                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.4                        | security-control/WAF.4                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.6                        | security-control/WAF.6                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.7                        | security-control/WAF.7                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.8                        | security-control/WAF.8                                   |
| aws-foundational-security-best-practices/v/1.0.0/WAF.10                       | security-control/WAF.10                                  |
| pci-dss/v/3.2.1/PCI.AutoScaling.1                                             | security-control/AutoScaling.1                           |
| pci-dss/v/3.2.1/PCI.CloudTrail.1                                              | security-control/CloudTrail.2                            |
| pci-dss/v/3.2.1/PCI.CloudTrail.2                                              | security-control/CloudTrail.3                            |
| pci-dss/v/3.2.1/PCI.CloudTrail.3                                              | security-control/CloudTrail.4                            |
| pci-dss/v/3.2.1/PCI.CloudTrail.4                                              | security-control/CloudTrail.5                            |
| pci-dss/v/3.2.1/PCI.CodeBuild.1                                               | security-control/CodeBuild.1                             |
| pci-dss/v/3.2.1/PCI.CodeBuild.2                                               | security-control/CodeBuild.2                             |
| pci-dss/v/3.2.1/PCI.Config.1                                                  | security-control/Config.1                                |
| pci-dss/v/3.2.1/PCI.CW.1                                                      | security-control/CloudWatch.1                            |
| pci-dss/v/3.2.1/PCI.DMS.1                                                     | security-control/DMS.1                                   |
| pci-dss/v/3.2.1/PCI.EC2.1                                                     | security-control/EC2.1                                   |
| pci-dss/v/3.2.1/PCI.EC2.2                                                     | security-control/EC2.2                                   |
| pci-dss/v/3.2.1/PCI.EC2.4                                                     | security-control/EC2.12                                  |
| pci-dss/v/3.2.1/PCI.EC2.5                                                     | security-control/EC2.13                                  |
| pci-dss/v/3.2.1/PCI.EC2.6                                                     | security-control/EC2.6                                   |
| pci-dss/v/3.2.1/PCI.ELBv2.1                                                   | security-control/ELB.1                                   |
| pci-dss/v/3.2.1/PCI.ES.1                                                      | security-control/ES.2                                    |
| pci-dss/v/3.2.1/PCI.ES.2                                                      | security-control/ES.1                                    |
| pci-dss/v/3.2.1/PCI.GuardDuty.1                                               | security-control/GuardDuty.1                             |
| pci-dss/v/3.2.1/PCI.IAM.1                                                     | security-control/IAM.4                                   |
| pci-dss/v/3.2.1/PCI.IAM.2                                                     | security-control/IAM.2                                   |
| pci-dss/v/3.2.1/PCI.IAM.3                                                     | security-control/IAM.1                                   |
| pci-dss/v/3.2.1/PCI.IAM.4                                                     | security-control/IAM.6                                   |
| pci-dss/v/3.2.1/PCI.IAM.5                                                     | security-control/IAM.9                                   |
| pci-dss/v/3.2.1/PCI.IAM.6                                                     | security-control/IAM.19                                  |
| pci-dss/v/3.2.1/PCI.IAM.7                                                     | security-control/IAM.8                                   |
| pci-dss/v/3.2.1/PCI.IAM.8                                                     | security-control/IAM.10                                  |
| pci-dss/v/3.2.1/PCI.KMS.1                                                     | security-control/KMS.4                                   |
| pci-dss/v/3.2.1/PCI.Lambda.1                                                  | security-control/Lambda.1                                |
| pci-dss/v/3.2.1/PCI.Lambda.2                                                  | security-control/Lambda.3                                |
| pci-dss/v/3.2.1/PCI.Opensearch.1                                              | security-control/Opensearch.2                            |
| pci-dss/v/3.2.1/PCI.Opensearch.2                                              | security-control/Opensearch.1                            |
| pci-dss/v/3.2.1/PCI.RDS.1                                                     | security-control/RDS.1                                   |
| pci-dss/v/3.2.1/PCI.RDS.2                                                     | security-control/RDS.2                                   |
| pci-dss/v/3.2.1/PCI.Redshift.1                                                | security-control/Redshift.1                              |
| pci-dss/v/3.2.1/PCI.S3.1                                                      | security-control/S3.3                                    |
| pci-dss/v/3.2.1/PCI.S3.2                                                      | security-control/S3.2                                    |
| pci-dss/v/3.2.1/PCI.S3.3                                                      | security-control/S3.7                                    |
| pci-dss/v/3.2.1/PCI.S3.5                                                      | security-control/S3.5                                    |
| pci-dss/v/3.2.1/PCI.S3.6                                                      | security-control/S3.1                                    |
| pci-dss/v/3.2.1/PCI.SageMaker.1                                               | security-control/SageMaker.1                             |
| pci-dss/v/3.2.1/PCI.SSM.1                                                     | security-control/SSM.2                                   |
| pci-dss/v/3.2.1/PCI.SSM.2                                                     | security-control/SSM.3                                   |
| pci-dss/v/3.2.1/PCI.SSM.3                                                     | security-control/SSM.1                                   |
| service-managed-aws-control-tower/v/1.0.0/ACM.1                               | security-control/ACM.1                                   |
| service-managed-aws-control-tower/v/1.0.0/APIGateway.1                        | security-control/APIGateway.1                            |
| service-managed-aws-control-tower/v/1.0.0/APIGateway.2                        | security-control/APIGateway.2                            |
| service-managed-aws-control-tower/v/1.0.0/APIGateway.3                        | security-control/APIGateway.3                            |
| service-managed-aws-control-tower/v/1.0.0/APIGateway.4                        | security-control/APIGateway.4                            |
| service-managed-aws-control-tower/v/1.0.0/APIGateway.5                        | security-control/APIGateway.5                            |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.1                       | security-control/AutoScaling.1                           |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.2                       | security-control/AutoScaling.2                           |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.3                       | security-control/AutoScaling.3                           |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.4                       | security-control/AutoScaling.4                           |
| service-managed-aws-control-tower/v/1.0.0/Autoscaling.5                       | security-control/Autoscaling.5                           |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.6                       | security-control/AutoScaling.6                           |
| service-managed-aws-control-tower/v/1.0.0/AutoScaling.9                       | security-control/AutoScaling.9                           |
| service-managed-aws-control-tower/v/1.0.0/CloudTrail.1                        | security-control/CloudTrail.1                            |
| service-managed-aws-control-tower/v/1.0.0/CloudTrail.2                        | security-control/CloudTrail.2                            |
| service-managed-aws-control-tower/v/1.0.0/CloudTrail.4                        | security-control/CloudTrail.4                            |
| service-managed-aws-control-tower/v/1.0.0/CloudTrail.5                        | security-control/CloudTrail.5                            |
| service-managed-aws-control-tower/v/1.0.0/CodeBuild.1                         | security-control/CodeBuild.1                             |
| service-managed-aws-control-tower/v/1.0.0/CodeBuild.2                         | security-control/CodeBuild.2                             |
| service-managed-aws-control-tower/v/1.0.0/CodeBuild.4                         | security-control/CodeBuild.4                             |
| service-managed-aws-control-tower/v/1.0.0/CodeBuild.5                         | security-control/CodeBuild.5                             |
| service-managed-aws-control-tower/v/1.0.0/DMS.1                               | security-control/DMS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/DynamoDB.1                          | security-control/DynamoDB.1                              |
| service-managed-aws-control-tower/v/1.0.0/DynamoDB.2                          | security-control/DynamoDB.2                              |
| service-managed-aws-control-tower/v/1.0.0/EC2.1                               | security-control/EC2.1                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.2                               | security-control/EC2.2                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.3                               | security-control/EC2.3                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.4                               | security-control/EC2.4                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.6                               | security-control/EC2.6                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.7                               | security-control/EC2.7                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.8                               | security-control/EC2.8                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.9                               | security-control/EC2.9                                   |
| service-managed-aws-control-tower/v/1.0.0/EC2.10                              | security-control/EC2.10                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.15                              | security-control/EC2.15                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.16                              | security-control/EC2.16                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.17                              | security-control/EC2.17                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.18                              | security-control/EC2.18                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.19                              | security-control/EC2.19                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.20                              | security-control/EC2.20                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.21                              | security-control/EC2.21                                  |
| service-managed-aws-control-tower/v/1.0.0/EC2.22                              | security-control/EC2.22                                  |
| service-managed-aws-control-tower/v/1.0.0/ECR.1                               | security-control/ECR.1                                   |
| service-managed-aws-control-tower/v/1.0.0/ECR.2                               | security-control/ECR.2                                   |
| service-managed-aws-control-tower/v/1.0.0/ECR.3                               | security-control/ECR.3                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.1                               | security-control/ECS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.2                               | security-control/ECS.2                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.3                               | security-control/ECS.3                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.4                               | security-control/ECS.4                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.5                               | security-control/ECS.5                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.8                               | security-control/ECS.8                                   |
| service-managed-aws-control-tower/v/1.0.0/ECS.10                              | security-control/ECS.10                                  |
| service-managed-aws-control-tower/v/1.0.0/ECS.12                              | security-control/ECS.12                                  |
| service-managed-aws-control-tower/v/1.0.0/EFS.1                               | security-control/EFS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/EFS.2                               | security-control/EFS.2                                   |
| service-managed-aws-control-tower/v/1.0.0/EFS.3                               | security-control/EFS.3                                   |
| service-managed-aws-control-tower/v/1.0.0/EFS.4                               | security-control/EFS.4                                   |
| service-managed-aws-control-tower/v/1.0.0/EKS.2                               | security-control/EKS.2                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.2                               | security-control/ELB.2                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.3                               | security-control/ELB.3                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.4                               | security-control/ELB.4                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.5                               | security-control/ELB.5                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.6                               | security-control/ELB.6                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.7                               | security-control/ELB.7                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.8                               | security-control/ELB.8                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.9                               | security-control/ELB.9                                   |
| service-managed-aws-control-tower/v/1.0.0/ELB.10                              | security-control/ELB.10                                  |
| service-managed-aws-control-tower/v/1.0.0/ELB.12                              | security-control/ELB.12                                  |
| service-managed-aws-control-tower/v/1.0.0/ELB.13                              | security-control/ELB.13                                  |
| service-managed-aws-control-tower/v/1.0.0/ELB.14                              | security-control/ELB.14                                  |
| service-managed-aws-control-tower/v/1.0.0/ELBv2.1                             | security-control/ELBv2.1                                 |
| service-managed-aws-control-tower/v/1.0.0/EMR.1                               | security-control/EMR.1                                   |
| service-managed-aws-control-tower/v/1.0.0/ES.1                                | security-control/ES.1                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.2                                | security-control/ES.2                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.3                                | security-control/ES.3                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.4                                | security-control/ES.4                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.5                                | security-control/ES.5                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.6                                | security-control/ES.6                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.7                                | security-control/ES.7                                    |
| service-managed-aws-control-tower/v/1.0.0/ES.8                                | security-control/ES.8                                    |
| service-managed-aws-control-tower/v/1.0.0/ElasticBeanstalk.1                  | security-control/ElasticBeanstalk.1                      |
| service-managed-aws-control-tower/v/1.0.0/ElasticBeanstalk.2                  | security-control/ElasticBeanstalk.2                      |
| service-managed-aws-control-tower/v/1.0.0/GuardDuty.1                         | security-control/GuardDuty.1                             |
| service-managed-aws-control-tower/v/1.0.0/IAM.1                               | security-control/IAM.1                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.2                               | security-control/IAM.2                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.3                               | security-control/IAM.3                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.4                               | security-control/IAM.4                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.5                               | security-control/IAM.5                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.6                               | security-control/IAM.6                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.7                               | security-control/IAM.7                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.8                               | security-control/IAM.8                                   |
| service-managed-aws-control-tower/v/1.0.0/IAM.21                              | security-control/IAM.21                                  |
| service-managed-aws-control-tower/v/1.0.0/Kinesis.1                           | security-control/Kinesis.1                               |
| service-managed-aws-control-tower/v/1.0.0/KMS.1                               | security-control/KMS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/KMS.2                               | security-control/KMS.2                                   |
| service-managed-aws-control-tower/v/1.0.0/KMS.3                               | security-control/KMS.3                                   |
| service-managed-aws-control-tower/v/1.0.0/Lambda.1                            | security-control/Lambda.1                                |
| service-managed-aws-control-tower/v/1.0.0/Lambda.2                            | security-control/Lambda.2                                |
| service-managed-aws-control-tower/v/1.0.0/Lambda.5                            | security-control/Lambda.5                                |
| service-managed-aws-control-tower/v/1.0.0/NetworkFirewall.3                   | security-control/NetworkFirewall.3                       |
| service-managed-aws-control-tower/v/1.0.0/NetworkFirewall.4                   | security-control/NetworkFirewall.4                       |
| service-managed-aws-control-tower/v/1.0.0/NetworkFirewall.5                   | security-control/NetworkFirewall.5                       |
| service-managed-aws-control-tower/v/1.0.0/NetworkFirewall.6                   | security-control/NetworkFirewall.6                       |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.1                        | security-control/Opensearch.1                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.2                        | security-control/Opensearch.2                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.3                        | security-control/Opensearch.3                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.4                        | security-control/Opensearch.4                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.5                        | security-control/Opensearch.5                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.6                        | security-control/Opensearch.6                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.7                        | security-control/Opensearch.7                            |
| service-managed-aws-control-tower/v/1.0.0/Opensearch.8                        | security-control/Opensearch.8                            |
| service-managed-aws-control-tower/v/1.0.0/RDS.1                               | security-control/RDS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.2                               | security-control/RDS.2                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.3                               | security-control/RDS.3                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.4                               | security-control/RDS.4                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.5                               | security-control/RDS.5                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.6                               | security-control/RDS.6                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.8                               | security-control/RDS.8                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.9                               | security-control/RDS.9                                   |
| service-managed-aws-control-tower/v/1.0.0/RDS.10                              | security-control/RDS.10                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.11                              | security-control/RDS.11                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.13                              | security-control/RDS.13                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.17                              | security-control/RDS.17                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.18                              | security-control/RDS.18                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.19                              | security-control/RDS.19                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.20                              | security-control/RDS.20                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.21                              | security-control/RDS.21                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.22                              | security-control/RDS.22                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.23                              | security-control/RDS.23                                  |
| service-managed-aws-control-tower/v/1.0.0/RDS.25                              | security-control/RDS.25                                  |
| service-managed-aws-control-tower/v/1.0.0/Redshift.1                          | security-control/Redshift.1                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.2                          | security-control/Redshift.2                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.4                          | security-control/Redshift.4                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.6                          | security-control/Redshift.6                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.7                          | security-control/Redshift.7                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.8                          | security-control/Redshift.8                              |
| service-managed-aws-control-tower/v/1.0.0/Redshift.9                          | security-control/Redshift.9                              |
| service-managed-aws-control-tower/v/1.0.0/S3.1                                | security-control/S3.1                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.2                                | security-control/S3.2                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.3                                | security-control/S3.3                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.5                                | security-control/S3.5                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.6                                | security-control/S3.6                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.8                                | security-control/S3.8                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.9                                | security-control/S3.9                                    |
| service-managed-aws-control-tower/v/1.0.0/S3.12                               | security-control/S3.12                                   |
| service-managed-aws-control-tower/v/1.0.0/S3.13                               | security-control/S3.13                                   |
| service-managed-aws-control-tower/v/1.0.0/SageMaker.1                         | security-control/SageMaker.1                             |
| service-managed-aws-control-tower/v/1.0.0/SecretsManager.1                    | security-control/SecretsManager.1                        |
| service-managed-aws-control-tower/v/1.0.0/SecretsManager.2                    | security-control/SecretsManager.2                        |
| service-managed-aws-control-tower/v/1.0.0/SecretsManager.3                    | security-control/SecretsManager.3                        |
| service-managed-aws-control-tower/v/1.0.0/SecretsManager.4                    | security-control/SecretsManager.4                        |
| service-managed-aws-control-tower/v/1.0.0/SQS.1                               | security-control/SQS.1                                   |
| service-managed-aws-control-tower/v/1.0.0/SSM.1                               | security-control/SSM.1                                   |
| service-managed-aws-control-tower/v/1.0.0/SSM.2                               | security-control/SSM.2                                   |
| service-managed-aws-control-tower/v/1.0.0/SSM.3                               | security-control/SSM.3                                   |
| service-managed-aws-control-tower/v/1.0.0/SSM.4                               | security-control/SSM.4                                   |
| service-managed-aws-control-tower/v/1.0.0/WAF.2                               | security-control/WAF.2                                   |
| service-managed-aws-control-tower/v/1.0.0/WAF.3                               | security-control/WAF.3                                   |
| service-managed-aws-control-tower/v/1.0.0/WAF.4                               | security-control/WAF.4                                   |

## How consolidation impacts

control IDs and titles

Consolidated controls view and consolidated control findings standardize control IDs and
titles across standards. The terms _security control ID_ and
_security control title_ refer to these standard-agnostic values.

The Security Hub CSPM console displays standard-agnostic security control IDs and security control
titles, regardless of whether consolidated control findings is enabled or disabled for your
account. However, Security Hub CSPM findings contain standard-specific control titles, for PCI DSS and CIS
v1.2.0, if consolidated control findings is disabled for your account. In addition, Security Hub CSPM
findings contain the standard-specific control ID and security control ID. For examples of how
consolidation impacts control findings, see [Samples of control findings](sample-control-findings.md "sample-control-findings.md").

For controls that are part of the [AWS Control Tower service-managed
standard](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md"), the prefix `CT.` is removed from the control ID and title in
findings when consolidated control findings is enabled.

To disable a security control in Security Hub CSPM, you must disable all standard controls that
correspond to the security control. The following table shows the mapping of security control
IDs and titles to standard-specific control IDs and titles. IDs and titles for controls that
belong to the AWS Foundational Security Best Practices (FSBP) standard are already standard-agnostic. For a mapping of
controls to the requirements of Center for Internet Security (CIS) v3.0.0, see [Mapping of controls to CIS requirements in each version](cis-aws-foundations-benchmark.md#cis-version-comparison "cis-aws-foundations-benchmark.md#cis-version-comparison"). To run your own
scripts on this table, you can [download it as a .csv file](samples/Consolidation_ID_Title_Changes.csv.md "samples/Consolidation_ID_Title_Changes.csv.md").

| Standard       | Standard control ID and title                                                                                                       | Security control ID and title                                                                                                                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CIS v1.2.0     | 1.1 Avoid the use of the root user                                                                                                  | [[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")                                                            |
| CIS v1.2.0     | 1.10 Ensure IAM password policy prevents password reuse                                                                             | [[IAM.16] Ensure IAM password policy prevents password reuse](iam-controls.md#iam-16 "iam-controls.md#iam-16")                                                                                                                 |
| CIS v1.2.0     | 1.11 Ensure IAM password policy expires passwords within 90 days or<br>less                                                         | [[IAM.17] Ensure IAM password policy expires passwords within 90 days or less](iam-controls.md#iam-17 "iam-controls.md#iam-17")                                                                                                |
| CIS v1.2.0     | 1.12 Ensure no root user access key exists                                                                                          | [[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")                                                                                                                             |
| CIS v1.2.0     | 1.13 Ensure MFA is enabled for the root user                                                                                        | [[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")                                                                                                                               |
| CIS v1.2.0     | 1.14 Ensure hardware MFA is enabled for the root user                                                                               | [[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")                                                                                                                      |
| CIS v1.2.0     | 1.16 Ensure IAM policies are attached only to groups or roles                                                                       | [[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")                                                                                                                       |
| CIS v1.2.0     | 1.2 Ensure multi-factor authentication (MFA) is enabled for all IAM users that<br>have a console password                           | [[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")                                                                                                  |
| CIS v1.2.0     | 1.20 Ensure a support role has been created to manage incidents with<br>Support                                                     | [[IAM.18] Ensure a support role has been created to manage incidents with<br>AWS Support](iam-controls.md#iam-18 "iam-controls.md#iam-18")                                                                                     |
| CIS v1.2.0     | 1.22 Ensure IAM policies that allow full "\*:\*" administrative privileges are<br>not created                                       | [[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")                                                                                                     |
| CIS v1.2.0     | 1.3 Ensure credentials unused for 90 days or greater are disabled                                                                   | [[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")                                                                                                                         |
| CIS v1.2.0     | 1.4 Ensure access keys are rotated every 90 days or less                                                                            | [[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")                                                                                                        |
| CIS v1.2.0     | 1.5 Ensure IAM password policy requires at least one uppercase letter                                                               | [[IAM.11] Ensure IAM password policy requires at least one uppercase letter](iam-controls.md#iam-11 "iam-controls.md#iam-11")                                                                                                  |
| CIS v1.2.0     | 1.6 Ensure IAM password policy requires at least one lowercase letter                                                               | [[IAM.12] Ensure IAM password policy requires at least one lowercase letter](iam-controls.md#iam-12 "iam-controls.md#iam-12")                                                                                                  |
| CIS v1.2.0     | 1.7 Ensure IAM password policy requires at least one symbol                                                                         | [[IAM.13] Ensure IAM password policy requires at least one symbol](iam-controls.md#iam-13 "iam-controls.md#iam-13")                                                                                                            |
| CIS v1.2.0     | 1.8 Ensure IAM password policy requires at least one number                                                                         | [[IAM.14] Ensure IAM password policy requires at least one number](iam-controls.md#iam-14 "iam-controls.md#iam-14")                                                                                                            |
| CIS v1.2.0     | 1.9 Ensure IAM password policy requires minimum password length of 14 or<br>greater                                                 | [[IAM.15] Ensure IAM password policy requires minimum password length of 14 or greater](iam-controls.md#iam-15 "iam-controls.md#iam-15")                                                                                       |
| CIS v1.2.0     | 2.1 Ensure CloudTrail is enabled in all regions                                                                                     | [[CloudTrail.1] CloudTrail should be enabled and configured with at least<br>one multi-Region trail that includes read and write management events](cloudtrail-controls.md#cloudtrail-1 "cloudtrail-controls.md#cloudtrail-1") |
| CIS v1.2.0     | 2.2 Ensure CloudTrail log file validation is enabled                                                                                | [[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")                                                                                   |
| CIS v1.2.0     | 2.3 Ensure the S3 bucket used to store CloudTrail logs is not publicly<br>accessible                                                | [[CloudTrail.6] Ensure the S3 bucket used to store CloudTrail logs is not<br>publicly accessible](cloudtrail-controls.md#cloudtrail-6 "cloudtrail-controls.md#cloudtrail-6")                                                   |
| CIS v1.2.0     | 2.4 Ensure CloudTrail trails are integrated with CloudWatch Logs                                                                    | [[CloudTrail.5] CloudTrail trails should be integrated with<br>Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")                                                              |
| CIS v1.2.0     | 2.5 Ensure AWS Config is enabled                                                                                                    | [[Config.1] AWS Config should be enabled and use the service-linked role for resource recording](config-controls.md#config-1 "config-controls.md#config-1")                                                                    |
| CIS v1.2.0     | 2.6 Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket                                                          | [[CloudTrail.7] Ensure S3 bucket access logging is enabled on the CloudTrail<br>S3 bucket](cloudtrail-controls.md#cloudtrail-7 "cloudtrail-controls.md#cloudtrail-7")                                                          |
| CIS v1.2.0     | 2.7 Ensure CloudTrail logs are encrypted at rest using KMS CMKs                                                                     | [[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")                                                                                  |
| CIS v1.2.0     | 2.8 Ensure rotation for customer created CMKs is enabled                                                                            | [[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")                                                                                                                                |
| CIS v1.2.0     | 2.9 Ensure VPC flow logging is enabled in all VPCs                                                                                  | [[EC2.6] VPC flow logging should be enabled in all<br>VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")                                                                                                                     |
| CIS v1.2.0     | 3.1 Ensure a log metric filter and alarm exist for unauthorized API calls                                                           | [[CloudWatch.2] Ensure a log metric filter and alarm exist for unauthorized API calls](cloudwatch-controls.md#cloudwatch-2 "cloudwatch-controls.md#cloudwatch-2")                                                              |
| CIS v1.2.0     | 3.10 Ensure a log metric filter and alarm exist for security group<br>changes                                                       | [[CloudWatch.10] Ensure a log metric filter and alarm exist for security group changes](cloudwatch-controls.md#cloudwatch-10 "cloudwatch-controls.md#cloudwatch-10")                                                           |
| CIS v1.2.0     | 3.11 Ensure a log metric filter and alarm exist for changes to Network Access<br>Control Lists (NACL)                               | [[CloudWatch.11] Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL)](cloudwatch-controls.md#cloudwatch-11 "cloudwatch-controls.md#cloudwatch-11")                                   |
| CIS v1.2.0     | 3.12 Ensure a log metric filter and alarm exist for changes to network<br>gateways                                                  | [[CloudWatch.12] Ensure a log metric filter and alarm exist for changes to network gateways](cloudwatch-controls.md#cloudwatch-12 "cloudwatch-controls.md#cloudwatch-12")                                                      |
| CIS v1.2.0     | 3.13 Ensure a log metric filter and alarm exist for route table changes                                                             | [[CloudWatch.13] Ensure a log metric filter and alarm exist for route table changes](cloudwatch-controls.md#cloudwatch-13 "cloudwatch-controls.md#cloudwatch-13")                                                              |
| CIS v1.2.0     | 3.14 Ensure a log metric filter and alarm exist for VPC changes                                                                     | [[CloudWatch.14] Ensure a log metric filter and alarm exist for VPC changes](cloudwatch-controls.md#cloudwatch-14 "cloudwatch-controls.md#cloudwatch-14")                                                                      |
| CIS v1.2.0     | 3.2 Ensure a log metric filter and alarm exist for Management Console sign-in<br>without MFA                                        | [[CloudWatch.3] Ensure a log metric filter and alarm exist for Management Console sign-in without MFA](cloudwatch-controls.md#cloudwatch-3 "cloudwatch-controls.md#cloudwatch-3")                                              |
| CIS v1.2.0     | 3.3 Ensure a log metric filter and alarm exist for usage of root user                                                               | [[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")                                                            |
| CIS v1.2.0     | 3.4 Ensure a log metric filter and alarm exist for IAM policy changes                                                               | [[CloudWatch.4] Ensure a log metric filter and alarm exist for IAM policy changes](cloudwatch-controls.md#cloudwatch-4 "cloudwatch-controls.md#cloudwatch-4")                                                                  |
| CIS v1.2.0     | 3.5 Ensure a log metric filter and alarm exist for CloudTrail configuration<br>changes                                              | [[CloudWatch.5] Ensure a log metric filter and alarm exist for CloudTrail<br>configuration changes](cloudwatch-controls.md#cloudwatch-5 "cloudwatch-controls.md#cloudwatch-5")                                                 |
| CIS v1.2.0     | 3.6 Ensure a log metric filter and alarm exist for AWS Management Console authentication<br>failures                                | [[CloudWatch.6] Ensure a log metric filter and alarm exist for AWS Management Console authentication failures](cloudwatch-controls.md#cloudwatch-6 "cloudwatch-controls.md#cloudwatch-6")                                      |
| CIS v1.2.0     | 3.7 Ensure a log metric filter and alarm exist for disabling or scheduled<br>deletion of customer created CMKs                      | [[CloudWatch.7] Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer managed keys](cloudwatch-controls.md#cloudwatch-7 "cloudwatch-controls.md#cloudwatch-7")                            |
| CIS v1.2.0     | 3.8 Ensure a log metric filter and alarm exist for S3 bucket policy<br>changes                                                      | [[CloudWatch.8] Ensure a log metric filter and alarm exist for S3 bucket policy changes](cloudwatch-controls.md#cloudwatch-8 "cloudwatch-controls.md#cloudwatch-8")                                                            |
| CIS v1.2.0     | 3.9 Ensure a log metric filter and alarm exist for AWS Config configuration<br>changes                                              | [[CloudWatch.9] Ensure a log metric filter and alarm exist for AWS Config configuration changes](cloudwatch-controls.md#cloudwatch-9 "cloudwatch-controls.md#cloudwatch-9")                                                    |
| CIS v1.2.0     | 4.1 Ensure no security groups allow ingress from 0.0.0.0/0 to port 22                                                               | [[EC2.13] Security groups should not allow ingress from<br>0.0.0.0/0 or ::/0 to port 22](ec2-controls.md#ec2-13 "ec2-controls.md#ec2-13")                                                                                      |
| CIS v1.2.0     | 4.2 Ensure no security groups allow ingress from 0.0.0.0/0 to port 3389                                                             | [[EC2.14] Security groups should not allow ingress from<br>0.0.0.0/0 or ::/0 to port 3389](ec2-controls.md#ec2-14 "ec2-controls.md#ec2-14")                                                                                    |
| CIS v1.2.0     | 4.3 Ensure the default security group of every VPC restricts all traffic                                                            | [[EC2.2] VPC default security groups should not allow<br>inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")                                                                                           |
| CIS v1.4.0     | 1.10 Ensure multi-factor authentication (MFA) is enabled for all IAM users<br>that have a console password                          | [[IAM.5] MFA should be enabled for all IAM users that have a console password](iam-controls.md#iam-5 "iam-controls.md#iam-5")                                                                                                  |
| CIS v1.4.0     | 1.14 Ensure access keys are rotated every 90 days or less                                                                           | [[IAM.3] IAM users' access keys should be rotated every 90 days or less](iam-controls.md#iam-3 "iam-controls.md#iam-3")                                                                                                        |
| CIS v1.4.0     | 1.16 Ensure IAM policies that allow full "\*:\*" administrative privileges are<br>not attached                                      | [[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")                                                                                                     |
| CIS v1.4.0     | 1.17 Ensure a support role has been created to manage incidents with<br>Support                                                     | [[IAM.18] Ensure a support role has been created to manage incidents with<br>AWS Support](iam-controls.md#iam-18 "iam-controls.md#iam-18")                                                                                     |
| CIS v1.4.0     | 1.4 Ensure no root user account access key exists                                                                                   | [[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")                                                                                                                             |
| CIS v1.4.0     | 1.5 Ensure MFA is enabled for the root user account                                                                                 | [[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")                                                                                                                               |
| CIS v1.4.0     | 1.6 Ensure hardware MFA is enabled for the root user account                                                                        | [[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")                                                                                                                      |
| CIS v1.4.0     | 1.7 Eliminate use of the root user for administrative and daily tasks                                                               | [[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")                                                            |
| CIS v1.4.0     | 1.8 Ensure IAM password policy requires minimum length of 14 or greater                                                             | [[IAM.15] Ensure IAM password policy requires minimum password length of 14 or greater](iam-controls.md#iam-15 "iam-controls.md#iam-15")                                                                                       |
| CIS v1.4.0     | 1.9 Ensure IAM password policy prevents password reuse                                                                              | [[IAM.16] Ensure IAM password policy prevents password reuse](iam-controls.md#iam-16 "iam-controls.md#iam-16")                                                                                                                 |
| CIS v1.4.0     | 2.1.2 Ensure S3 Bucket Policy is set to deny HTTP requests                                                                          | [[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")                                                                                                              |
| CIS v1.4.0     | 2.1.5.1 S3 Block Public Access setting should be enabled                                                                            | [[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")                                                                                                |
| CIS v1.4.0     | 2.1.5.2 S3 Block Public Access setting should be enabled at the bucket<br>level                                                     | [[S3.8] S3 general purpose buckets should block public access](s3-controls.md#s3-8 "s3-controls.md#s3-8")                                                                                                                      |
| CIS v1.4.0     | 2.2.1 Ensure EBS volume encryption is enabled                                                                                       | [[EC2.7] EBS default encryption should be enabled](ec2-controls.md#ec2-7 "ec2-controls.md#ec2-7")                                                                                                                              |
| CIS v1.4.0     | 2.3.1 Ensure that encryption is enabled for RDS Instances                                                                           | [[RDS.3] RDS DB instances should have encryption at-rest enabled](rds-controls.md#rds-3 "rds-controls.md#rds-3")                                                                                                               |
| CIS v1.4.0     | 3.1 Ensure CloudTrail is enabled in all regions                                                                                     | [[CloudTrail.1] CloudTrail should be enabled and configured with at least<br>one multi-Region trail that includes read and write management events](cloudtrail-controls.md#cloudtrail-1 "cloudtrail-controls.md#cloudtrail-1") |
| CIS v1.4.0     | 3.2 Ensure CloudTrail log file validation is enabled                                                                                | [[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")                                                                                   |
| CIS v1.4.0     | 3.4 Ensure CloudTrail trails are integrated with CloudWatch Logs                                                                    | [[CloudTrail.5] CloudTrail trails should be integrated with<br>Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")                                                              |
| CIS v1.4.0     | 3.5 Ensure AWS Config is enabled in all regions                                                                                     | [[Config.1] AWS Config should be enabled and use the service-linked role for resource recording](config-controls.md#config-1 "config-controls.md#config-1")                                                                    |
| CIS v1.4.0     | 3.6 Ensure S3 bucket access logging is enabled on the CloudTrail S3 bucket                                                          | [[CloudTrail.7] Ensure S3 bucket access logging is enabled on the CloudTrail<br>S3 bucket](cloudtrail-controls.md#cloudtrail-7 "cloudtrail-controls.md#cloudtrail-7")                                                          |
| CIS v1.4.0     | 3.7 Ensure CloudTrail logs are encrypted at rest using KMS CMKs                                                                     | [[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")                                                                                  |
| CIS v1.4.0     | 3.8 Ensure rotation for customer created CMKs is enabled                                                                            | [[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")                                                                                                                                |
| CIS v1.4.0     | 3.9 Ensure VPC flow logging is enabled in all VPCs                                                                                  | [[EC2.6] VPC flow logging should be enabled in all<br>VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")                                                                                                                     |
| CIS v1.4.0     | 4.4 Ensure a log metric filter and alarm exist for IAM policy changes                                                               | [[CloudWatch.4] Ensure a log metric filter and alarm exist for IAM policy changes](cloudwatch-controls.md#cloudwatch-4 "cloudwatch-controls.md#cloudwatch-4")                                                                  |
| CIS v1.4.0     | 4.5 Ensure a log metric filter and alarm exist for CloudTrail configuration<br>changes                                              | [[CloudWatch.5] Ensure a log metric filter and alarm exist for CloudTrail<br>configuration changes](cloudwatch-controls.md#cloudwatch-5 "cloudwatch-controls.md#cloudwatch-5")                                                 |
| CIS v1.4.0     | 4.6 Ensure a log metric filter and alarm exist for AWS Management Console authentication<br>failures                                | [[CloudWatch.6] Ensure a log metric filter and alarm exist for AWS Management Console authentication failures](cloudwatch-controls.md#cloudwatch-6 "cloudwatch-controls.md#cloudwatch-6")                                      |
| CIS v1.4.0     | 4.7 Ensure a log metric filter and alarm exist for disabling or scheduled<br>deletion of customer created CMKs                      | [[CloudWatch.7] Ensure a log metric filter and alarm exist for disabling or scheduled deletion of customer managed keys](cloudwatch-controls.md#cloudwatch-7 "cloudwatch-controls.md#cloudwatch-7")                            |
| CIS v1.4.0     | 4.8 Ensure a log metric filter and alarm exist for S3 bucket policy<br>changes                                                      | [[CloudWatch.8] Ensure a log metric filter and alarm exist for S3 bucket policy changes](cloudwatch-controls.md#cloudwatch-8 "cloudwatch-controls.md#cloudwatch-8")                                                            |
| CIS v1.4.0     | 4.9 Ensure a log metric filter and alarm exist for AWS Config configuration<br>changes                                              | [[CloudWatch.9] Ensure a log metric filter and alarm exist for AWS Config configuration changes](cloudwatch-controls.md#cloudwatch-9 "cloudwatch-controls.md#cloudwatch-9")                                                    |
| CIS v1.4.0     | 4.10 Ensure a log metric filter and alarm exist for security group<br>changes                                                       | [[CloudWatch.10] Ensure a log metric filter and alarm exist for security group changes](cloudwatch-controls.md#cloudwatch-10 "cloudwatch-controls.md#cloudwatch-10")                                                           |
| CIS v1.4.0     | 4.11 Ensure a log metric filter and alarm exist for changes to Network Access<br>Control Lists (NACL)                               | [[CloudWatch.11] Ensure a log metric filter and alarm exist for changes to Network Access Control Lists (NACL)](cloudwatch-controls.md#cloudwatch-11 "cloudwatch-controls.md#cloudwatch-11")                                   |
| CIS v1.4.0     | 4.12 Ensure a log metric filter and alarm exist for changes to network<br>gateways                                                  | [[CloudWatch.12] Ensure a log metric filter and alarm exist for changes to network gateways](cloudwatch-controls.md#cloudwatch-12 "cloudwatch-controls.md#cloudwatch-12")                                                      |
| CIS v1.4.0     | 4.13 Ensure a log metric filter and alarm exist for route table changes                                                             | [[CloudWatch.13] Ensure a log metric filter and alarm exist for route table changes](cloudwatch-controls.md#cloudwatch-13 "cloudwatch-controls.md#cloudwatch-13")                                                              |
| CIS v1.4.0     | 4.14 Ensure a log metric filter and alarm exist for VPC changes                                                                     | [[CloudWatch.14] Ensure a log metric filter and alarm exist for VPC changes](cloudwatch-controls.md#cloudwatch-14 "cloudwatch-controls.md#cloudwatch-14")                                                                      |
| CIS v1.4.0     | 5.1 Ensure no Network ACLs allow ingress from 0.0.0.0/0 to remote server<br>administration ports                                    | [[EC2.21] Network ACLs should not allow ingress from<br>0.0.0.0/0 to port 22 or port 3389](ec2-controls.md#ec2-21 "ec2-controls.md#ec2-21")                                                                                    |
| CIS v1.4.0     | 5.3 Ensure the default security group of every VPC restricts all traffic                                                            | [[EC2.2] VPC default security groups should not allow<br>inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")                                                                                           |
| PCI DSS v3.2.1 | PCI.AutoScaling.1 Auto scaling groups associated with a load balancer should use<br>load balancer health checks                     | [[AutoScaling.1] Auto Scaling groups associated with a load balancer should use ELB health checks](autoscaling-controls.md#autoscaling-1 "autoscaling-controls.md#autoscaling-1")                                              |
| PCI DSS v3.2.1 | PCI.CloudTrail.1 CloudTrail logs should be encrypted at rest using AWS KMS CMKs                                                     | [[CloudTrail.2] CloudTrail should have encryption at-rest enabled](cloudtrail-controls.md#cloudtrail-2 "cloudtrail-controls.md#cloudtrail-2")                                                                                  |
| PCI DSS v3.2.1 | PCI.CloudTrail.2 CloudTrail should be enabled                                                                                       | [[CloudTrail.3] At least one CloudTrail trail should be enabled](cloudtrail-controls.md#cloudtrail-3 "cloudtrail-controls.md#cloudtrail-3")                                                                                    |
| PCI DSS v3.2.1 | PCI.CloudTrail.3 CloudTrail log file validation should be enabled                                                                   | [[CloudTrail.4] CloudTrail log file validation should be enabled](cloudtrail-controls.md#cloudtrail-4 "cloudtrail-controls.md#cloudtrail-4")                                                                                   |
| PCI DSS v3.2.1 | PCI.CloudTrail.4 CloudTrail trails should be integrated with Amazon CloudWatch Logs                                                 | [[CloudTrail.5] CloudTrail trails should be integrated with<br>Amazon CloudWatch Logs](cloudtrail-controls.md#cloudtrail-5 "cloudtrail-controls.md#cloudtrail-5")                                                              |
| PCI DSS v3.2.1 | PCI.CodeBuild.1 CodeBuild GitHub or Bitbucket source repository URLs should use<br>OAuth                                            | [[CodeBuild.1] CodeBuild Bitbucket source repository URLs should not contain sensitive credentials](codebuild-controls.md#codebuild-1 "codebuild-controls.md#codebuild-1")                                                     |
| PCI DSS v3.2.1 | PCI.CodeBuild.2 CodeBuild project environment variables should not contain clear text<br>credentials                                | [[CodeBuild.2] CodeBuild project environment variables should not contain clear text credentials](codebuild-controls.md#codebuild-2 "codebuild-controls.md#codebuild-2")                                                       |
| PCI DSS v3.2.1 | PCI.Config.1 AWS Config should be enabled                                                                                           | [[Config.1] AWS Config should be enabled and use the service-linked role for resource recording](config-controls.md#config-1 "config-controls.md#config-1")                                                                    |
| PCI DSS v3.2.1 | PCI.CW.1 A log metric filter and alarm should exist for usage of the "root"<br>user                                                 | [[CloudWatch.1] A log metric filter and alarm should exist for usage of the "root" user](cloudwatch-controls.md#cloudwatch-1 "cloudwatch-controls.md#cloudwatch-1")                                                            |
| PCI DSS v3.2.1 | PCI.DMS.1 Database Migration Service replication instances should not be<br>public                                                  | [[DMS.1] Database Migration Service replication instances should not be public](dms-controls.md#dms-1 "dms-controls.md#dms-1")                                                                                                 |
| PCI DSS v3.2.1 | PCI.EC2.1 EBS snapshots should not be publicly restorable                                                                           | [[EC2.1] Amazon EBS snapshots should not be publicly<br>restorable](ec2-controls.md#ec2-1 "ec2-controls.md#ec2-1")                                                                                                             |
| PCI DSS v3.2.1 | PCI.EC2.2 VPC default security group should prohibit inbound and outbound<br>traffic                                                | [[EC2.2] VPC default security groups should not allow<br>inbound or outbound traffic](ec2-controls.md#ec2-2 "ec2-controls.md#ec2-2")                                                                                           |
| PCI DSS v3.2.1 | PCI.EC2.4 Unused EC2 EIPs should be removed                                                                                         | [[EC2.12] Unused Amazon EC2 EIPs should be removed](ec2-controls.md#ec2-12 "ec2-controls.md#ec2-12")                                                                                                                           |
| PCI DSS v3.2.1 | PCI.EC2.5 Security groups should not allow ingress from 0.0.0.0/0 to port<br>22                                                     | [[EC2.13] Security groups should not allow ingress from<br>0.0.0.0/0 or ::/0 to port 22](ec2-controls.md#ec2-13 "ec2-controls.md#ec2-13")                                                                                      |
| PCI DSS v3.2.1 | PCI.EC2.6 VPC flow logging should be enabled in all VPCs                                                                            | [[EC2.6] VPC flow logging should be enabled in all<br>VPCs](ec2-controls.md#ec2-6 "ec2-controls.md#ec2-6")                                                                                                                     |
| PCI DSS v3.2.1 | PCI.ELBv2.1 Application Load Balancer should be configured to redirect all HTTP requests to<br>HTTPS                                | [[ELB.1] Application Load Balancer should be configured to redirect all HTTP requests<br>to HTTPS](elb-controls.md#elb-1 "elb-controls.md#elb-1")                                                                              |
| PCI DSS v3.2.1 | PCI.ES.1 Elasticsearch domains should be in a VPC                                                                                   | [[ES.2] Elasticsearch domains should not be publicly accessible](es-controls.md#es-2 "es-controls.md#es-2")                                                                                                                    |
| PCI DSS v3.2.1 | PCI.ES.2 Elasticsearch domains should have encryption at-rest enabled                                                               | [[ES.1] Elasticsearch domains should have encryption at-rest enabled](es-controls.md#es-1 "es-controls.md#es-1")                                                                                                               |
| PCI DSS v3.2.1 | PCI.GuardDuty.1 GuardDuty should be enabled                                                                                         | [[GuardDuty.1] GuardDuty should be enabled](guardduty-controls.md#guardduty-1 "guardduty-controls.md#guardduty-1")                                                                                                             |
| PCI DSS v3.2.1 | PCI.IAM.1 IAM root user access key should not exist                                                                                 | [[IAM.4] IAM root user access key should not exist](iam-controls.md#iam-4 "iam-controls.md#iam-4")                                                                                                                             |
| PCI DSS v3.2.1 | PCI.IAM.2 IAM users should not have IAM policies attached                                                                           | [[IAM.2] IAM users should not have IAM policies attached](iam-controls.md#iam-2 "iam-controls.md#iam-2")                                                                                                                       |
| PCI DSS v3.2.1 | PCI.IAM.3 IAM policies should not allow full "\*" administrative<br>privileges                                                      | [[IAM.1] IAM policies should not allow full "\*" administrative privileges](iam-controls.md#iam-1 "iam-controls.md#iam-1")                                                                                                     |
| PCI DSS v3.2.1 | PCI.IAM.4 Hardware MFA should be enabled for the root user                                                                          | [[IAM.6] Hardware MFA should be enabled for the root user](iam-controls.md#iam-6 "iam-controls.md#iam-6")                                                                                                                      |
| PCI DSS v3.2.1 | PCI.IAM.5 Virtual MFA should be enabled for the root user                                                                           | [[IAM.9] MFA should be enabled for the root user](iam-controls.md#iam-9 "iam-controls.md#iam-9")                                                                                                                               |
| PCI DSS v3.2.1 | PCI.IAM.6 MFA should be enabled for all IAM users                                                                                   | [[IAM.19] MFA should be enabled for all IAM users](iam-controls.md#iam-19 "iam-controls.md#iam-19")                                                                                                                            |
| PCI DSS v3.2.1 | PCI.IAM.7 IAM user credentials should be disabled if not used within a<br>pre-defined number days                                   | [[IAM.8] Unused IAM user credentials should be removed](iam-controls.md#iam-8 "iam-controls.md#iam-8")                                                                                                                         |
| PCI DSS v3.2.1 | PCI.IAM.8 Password policies for IAM users should have strong<br>configurations                                                      | [[IAM.10] Password policies for IAM users should have strong<br>configurations](iam-controls.md#iam-10 "iam-controls.md#iam-10")                                                                                               |
| PCI DSS v3.2.1 | PCI.KMS.1 Customer master key (CMK) rotation should be enabled                                                                      | [[KMS.4] AWS KMS key rotation should be enabled](kms-controls.md#kms-4 "kms-controls.md#kms-4")                                                                                                                                |
| PCI DSS v3.2.1 | PCI.Lambda.1 Lambda functions should prohibit public access                                                                         | [[Lambda.1] Lambda function policies should prohibit public<br>access](lambda-controls.md#lambda-1 "lambda-controls.md#lambda-1")                                                                                              |
| PCI DSS v3.2.1 | PCI.Lambda.2 Lambda functions should be in a VPC                                                                                    | [[Lambda.3] Lambda functions should be in a VPC](lambda-controls.md#lambda-3 "lambda-controls.md#lambda-3")                                                                                                                    |
| PCI DSS v3.2.1 | PCI.Opensearch.1 OpenSearch domains should be in a VPC                                                                              | [[Opensearch.2] OpenSearch domains should not be publicly accessible](opensearch-controls.md#opensearch-2 "opensearch-controls.md#opensearch-2")                                                                               |
| PCI DSS v3.2.1 | PCI.Opensearch.2 EBS snapshots should not be publicly restorable                                                                    | [[Opensearch.1] OpenSearch domains should have encryption at rest enabled](opensearch-controls.md#opensearch-1 "opensearch-controls.md#opensearch-1")                                                                          |
| PCI DSS v3.2.1 | PCI.RDS.1 RDS snapshot should be private                                                                                            | [[RDS.1] RDS snapshot should be private](rds-controls.md#rds-1 "rds-controls.md#rds-1")                                                                                                                                        |
| PCI DSS v3.2.1 | PCI.RDS.2 RDS DB Instances should prohibit public access                                                                            | [[RDS.2] RDS DB Instances should prohibit public access, as determined by the PubliclyAccessible configuration](rds-controls.md#rds-2 "rds-controls.md#rds-2")                                                                 |
| PCI DSS v3.2.1 | PCI.Redshift.1 Amazon Redshift clusters should prohibit public access                                                               | [[Redshift.1] Amazon Redshift clusters should prohibit public access](redshift-controls.md#redshift-1 "redshift-controls.md#redshift-1")                                                                                       |
| PCI DSS v3.2.1 | PCI.S3.1 S3 buckets should prohibit public write access                                                                             | [[S3.3] S3 general purpose buckets should block public write<br>access](s3-controls.md#s3-3 "s3-controls.md#s3-3")                                                                                                             |
| PCI DSS v3.2.1 | PCI.S3.2 S3 buckets should prohibit public read access                                                                              | [[S3.2] S3 general purpose buckets should block public read<br>access](s3-controls.md#s3-2 "s3-controls.md#s3-2")                                                                                                              |
| PCI DSS v3.2.1 | PCI.S3.3 S3 buckets should have cross-region replication enabled                                                                    | [[S3.7] S3 general purpose buckets should use cross-Region replication](s3-controls.md#s3-7 "s3-controls.md#s3-7")                                                                                                             |
| PCI DSS v3.2.1 | PCI.S3.5 S3 buckets should require requests to use Secure Socket Layer                                                              | [[S3.5] S3 general purpose buckets should require requests to use SSL](s3-controls.md#s3-5 "s3-controls.md#s3-5")                                                                                                              |
| PCI DSS v3.2.1 | PCI.S3.6 S3 Block Public Access setting should be enabled                                                                           | [[S3.1] S3 general purpose buckets should have block public access settings enabled](s3-controls.md#s3-1 "s3-controls.md#s3-1")                                                                                                |
| PCI DSS v3.2.1 | PCI.SageMaker.1 Amazon SageMaker notebook instances should not have direct<br>internet access                                       | [[SageMaker.1] Amazon SageMaker notebook instances should not have<br>direct internet access](sagemaker-controls.md#sagemaker-1 "sagemaker-controls.md#sagemaker-1")                                                           |
| PCI DSS v3.2.1 | PCI.SSM.1 EC2 instances managed by Systems Manager should have a patch compliance<br>status of COMPLIANT after a patch installation | [[SSM.2] Amazon EC2 instances managed by Systems Manager should have a patch<br>compliance status of COMPLIANT after a patch installation](ssm-controls.md#ssm-2 "ssm-controls.md#ssm-2")                                      |
| PCI DSS v3.2.1 | PCI.SSM.2 EC2 instances managed by Systems Manager should have an association<br>compliance status of COMPLIANT                     | [[SSM.3] Amazon EC2 instances managed by Systems Manager should have an<br>association compliance status of COMPLIANT](ssm-controls.md#ssm-3 "ssm-controls.md#ssm-3")                                                          |
| PCI DSS v3.2.1 | PCI.SSM.3 EC2 instances should be managed by AWS Systems Manager                                                                    | [[SSM.1] Amazon EC2 instances should be managed by AWS Systems Manager](ssm-controls.md#ssm-1 "ssm-controls.md#ssm-1")                                                                                                         |

## Updating workflows for

consolidation

If your workflows don’t rely on the specific format of any fields in control findings, no
action is required.

If your workflows rely on the specific format of one or more fields in control findings,
as noted in the preceding tables, you should update your workflows. For example, If you
created an Amazon EventBridge rule that triggered an action for a specific control ID, such as invoking
an AWS Lambda function if the control ID equals CIS 2.7, update the rule to use CloudTrail.2, which
is the value for the `Compliance.SecurityControlId` field for that control.

If you created [custom insights](securityhub-custom-insights.md "securityhub-custom-insights.md") that use
any of the fields or values that changed, update those insights to use the new fields or
values.
