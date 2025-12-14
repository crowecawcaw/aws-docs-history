# AWS Security Hub CSPM controls supported by AWS Audit Manager

You can use Audit Manager to capture Security Hub CSPM findings as evidence for audits. When you create or edit
a custom control, you can specify one or more Security Hub CSPM controls as a data source mapping for
evidence collection. Security Hub CSPM performs compliance checks based on these controls, and Audit Manager
reports the results as compliance check evidence.

###### Contents

- [Key points](control-data-sources-ash.md#using-security-hub-controls "control-data-sources-ash.md#using-security-hub-controls")
- [Supported Security Hub CSPM
  controls](control-data-sources-ash.md#security-hub-controls-for-custom-control-data-sources "control-data-sources-ash.md#security-hub-controls-for-custom-control-data-sources")
- [Additional
  resources](control-data-sources-ash.md#using-security-hub-controls-additional-resources "control-data-sources-ash.md#using-security-hub-controls-additional-resources")

## Key points

- Audit Manager doesn’t collect evidence from [service-linked AWS Config rules that are created by Security Hub CSPM](../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md "../../../securityhub/latest/userguide/securityhub-standards-awsconfigrules.md").
- On November 9, 2022, Security Hub CSPM launched automated security checks aligned to the Center
  for Internet Security’s (CIS) AWS Foundations Benchmark version 1.4.0 requirements,
  Level 1 and 2 (CIS v1.4.0). In Security Hub CSPM, the [CIS v1.4.0
  standard](../../../securityhub/latest/userguide/securityhub-cis-controls-1.4.md "../../../securityhub/latest/userguide/securityhub-cis-controls-1.4.md") is supported in addition to the [CIS v1.2.0
  standard](../../../securityhub/latest/userguide/securityhub-cis-controls.md "../../../securityhub/latest/userguide/securityhub-cis-controls.md").
- We recommend that you turn on the [consolidated control findings](../../../securityhub/latest/userguide/controls-findings-create-update.md#consolidated-control-findings "../../../securityhub/latest/userguide/controls-findings-create-update.md#consolidated-control-findings") setting in Security Hub CSPM if it's not turned on already.
  If you enable Security Hub CSPM on or after February 23, 2023, this setting is turned _on_ by default.

When consolidated findings is enabled, Security Hub CSPM produces a single finding for each
security check (even when the same check applies to multiple standards). Each Security Hub CSPM
finding is collected as one unique resource assessment in Audit Manager. As a result,
consolidated findings results in a decrease of the total unique resource assessments
that Audit Manager performs for Security Hub CSPM findings. For this reason, using consolidated findings can
often result in a reduction in your Audit Manager usages costs, without sacrificing evidence
quality and availability. For more information about pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/ "https://aws.amazon.com/audit-manager/pricing/").

The following examples show a comparison of how Audit Manager collects and presents evidence
depending on your Security Hub CSPM settings.

When consolidated findings is turned on
Let's say that you have enabled the following three security standards in
Security Hub CSPM: AWS FSBP, PCI DSS, and CIS Benchmark v1.2.0.

- All three of these standards use the same control ([IAM.4](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4"))
  with the same underlying AWS Config rule ([iam-root-access-key-check](../../../config/latest/developerguide/iam-root-access-key-check.md "../../../config/latest/developerguide/iam-root-access-key-check.md")).
- Because the consolidated findings setting is **turned
  on**, Security Hub CSPM generates one single finding for this control.
- Security Hub CSPM sends the consolidated finding to Audit Manager for this control.
- The consolidated finding counts as one unique resource assessment in Audit Manager.
  As a result, one single piece of evidence is added to your assessment.

Here's an example of how that evidence might look:

```
{
    "SchemaVersion": "2018-10-08",
    "Id": "arn:aws:securityhub:us-west-2:111122223333:security-control/IAM.4/finding/09876543-p0o9-i8u7-y6t5-098765432109",
    "ProductArn": "arn:aws:securityhub:us-west-2::product/aws/securityhub",
    "ProductName": "Security Hub",
    "CompanyName": "AWS",
    "Region": "us-west-2",
    "GeneratorId": "security-control/IAM.4",
    "AwsAccountId": "111122223333",
    "Types": [
        "Software and Configuration Checks/Industry and Regulatory Standards"
    ],
    "FirstObservedAt": "2023-10-25T11:32:24.861Z",
    "LastObservedAt": "2023-11-02T11:59:19.546Z",
    "CreatedAt": "2023-10-25T11:32:24.861Z",
    "UpdatedAt": "2023-11-02T11:59:15.127Z",
    "Severity": {
        "Label": "INFORMATIONAL",
        "Normalized": 0,
        "Original": "INFORMATIONAL"
    },
    "Title": "IAM root user access key should not exist",
    "Description": "This AWS control checks whether the root user access key is available.",
    "Remediation": {
        "Recommendation": {
            "Text": "For information on how to correct this issue, consult the AWS Security Hub controls documentation.",
            "Url": "https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation"
        }
    },
    "ProductFields": {
        "RelatedAWSResources:0/name": "securityhub-iam-root-access-key-check-000270f5",
        "RelatedAWSResources:0/type": "AWS::Config::ConfigRule",
        "aws/securityhub/ProductName": "Security Hub",
        "aws/securityhub/CompanyName": "AWS",
        "Resources:0/Id": "arn:aws:iam::111122223333:root",
        "aws/securityhub/FindingId": "arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:security-control/IAM.4/finding/09876543-p0o9-i8u7-y6t5-098765432109"
    },
    "Resources": [{
        "Type": "AwsAccount",
        "Id": "AWS::::Account:111122223333",
        "Partition": "aws",
        "Region": "us-west-2"
    }],
    "Compliance": {
        "Status": "PASSED",
        "RelatedRequirements": [
            "CIS AWS Foundations Benchmark v1.2.0/1.12"
        ],
        "SecurityControlId": "IAM.4",
        "AssociatedStandards": [{
                "StandardsId": "ruleset/cis-aws-foundations-benchmark/v/1.2.0"
            },
            {
                "StandardsId": "standards/aws-foundational-security-best-practices/v/1.0.0"
            }
        ]
    },
    "WorkflowState": "NEW",
    "Workflow": {
        "Status": "RESOLVED"
    },
    "RecordState": "ACTIVE",
    "FindingProviderFields": {
        "Severity": {
            "Label": "INFORMATIONAL",
            "Original": "INFORMATIONAL"
        },
        "Types": [
            "Software and Configuration Checks/Industry and Regulatory Standards"
        ]
    },
    "ProcessedAt": "2023-11-02T11:59:20.980Z"
}
```

When consolidated findings is turned off
Let's say that you have enabled the following three security standards in
Security Hub CSPM: AWS FSBP, PCI DSS, and CIS Benchmark v1.2.0.

- All three of these standards use the same control ([IAM.4](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4"))
  with the same underlying AWS Config rule ([iam-root-access-key-check](../../../config/latest/developerguide/iam-root-access-key-check.md "../../../config/latest/developerguide/iam-root-access-key-check.md")).
- Because the consolidated findings setting is **turned
  off**, Security Hub CSPM generates a separate finding per security check for
  each enabled standard (in this case, three findings).
- Security Hub CSPM sends three separate standard-specific findings to Audit Manager for this
  control.
- The three findings count as three unique resource assessments in Audit Manager. As
  a result, three separate pieces of evidence are added to your
  assessment.

Here's an example of how that evidence might look. Note that in this example,
each of the following three payloads has the same security control ID
(`SecurityControlId":"IAM.4"`). For this
reason, the assessment control that collects this evidence in Audit Manager (IAM.4)
receives three separate pieces of evidence when the following findings come in
from Security Hub CSPM.

**Evidence for IAM.4 (FSBP)**

```
{
  "version":"0",
  "id":"12345678-1q2w-3e4r-5t6y-123456789012",
  "detail-type":"Security Hub Findings - Imported",
  "source":"aws.securityhub",
  "account":"111122223333",
  "time":"2023-10-27T18:55:59Z",
  "region":"us-west-2",
  "resources":[
     "arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0/Lambda.1/finding/b5e68d5d-43c3-46c8-902d-51cb0d4da568"
  ],
  "detail":{
     "findings":[
        {
           "SchemaVersion":"2018-10-08",
           "Id":"arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.4/finding/8e2e05a2-4d50-4c2e-a78f-3cbe9402d17d",
           "ProductArn":"arn:aws:securityhub:us-west-2::product/aws/securityhub",
           "ProductName":"Security Hub",
           "CompanyName":"AWS",
           "Region":"us-west-2",
           "GeneratorId":"aws-foundational-security-best-practices/v/1.0.0/IAM.4",
           "AwsAccountId":"111122223333",
           "Types":[
              "Software and Configuration Checks/Industry and Regulatory Standards/AWS-Foundational-Security-Best-Practices"
           ],
           "FirstObservedAt":"2020-10-05T19:18:47.848Z",
           "LastObservedAt":"2023-11-01T14:12:04.106Z",
           "CreatedAt":"2020-10-05T19:18:47.848Z",
           "UpdatedAt":"2023-11-01T14:11:53.720Z",
           "Severity":{
              "Product":0,
              "Label":"INFORMATIONAL",
              "Normalized":0,
              "Original":"INFORMATIONAL"
           },
           "Title":"IAM.4 IAM root user access key should not exist",
           "Description":"This AWS control checks whether the root user access key is available.",
           "Remediation":{
              "Recommendation":{
                 "Text":"For information on how to correct this issue, consult the AWS Security Hub controls documentation.",
                 "Url":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation"
              }
           },
           "ProductFields":{
              "StandardsArn":"arn:aws:securityhub:::standards/aws-foundational-security-best-practices/v/1.0.0",
              "StandardsSubscriptionArn":"arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0",
              "ControlId":"IAM.4",
              "RecommendationUrl":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation",
              "RelatedAWSResources:0/name":"securityhub-iam-root-access-key-check-67cbb1c4",
              "RelatedAWSResources:0/type":"AWS::Config::ConfigRule",
              "StandardsControlArn":"arn:aws:securityhub:us-west-2:111122223333:control/aws-foundational-security-best-practices/v/1.0.0/IAM.4",
              "aws/securityhub/ProductName":"Security Hub",
              "aws/securityhub/CompanyName":"AWS",
              "Resources:0/Id":"arn:aws:iam::111122223333:root",
              "aws/securityhub/FindingId":"arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0/IAM.4/finding/8e2e05a2-4d50-4c2e-a78f-3cbe9402d17d"
           },
           "Resources":[
              {
                 "Type":"AwsAccount",
                 "Id":"AWS::::Account:111122223333",
                 "Partition":"aws",
                 "Region":"us-west-2"
              }
           ],
           "Compliance":{
              "Status":"PASSED",
              `"SecurityControlId":"IAM.4"`,
              "AssociatedStandards":[
                 {
                    "StandardsId":"standards/aws-foundational-security-best-practices/v/1.0.0"
                 }
              ]
           },
           "WorkflowState":"NEW",
           "Workflow":{
              "Status":"RESOLVED"
           },
           "RecordState":"ACTIVE",
           "FindingProviderFields":{
              "Severity":{
                 "Label":"INFORMATIONAL",
                 "Original":"INFORMATIONAL"
              },
              "Types":[
                 "Software and Configuration Checks/Industry and Regulatory Standards/AWS-Foundational-Security-Best-Practices"
              ]
           },
           "ProcessedAt":"2023-11-01T14:12:07.395Z"
        }
     ]
  }
}


```

**Evidence for IAM.4 (CIS 1.2)**

```
{
  "version":"0",
  "id":"12345678-1q2w-3e4r-5t6y-123456789012",
  "detail-type":"Security Hub Findings - Imported",
  "source":"aws.securityhub",
  "account":"111122223333",
  "time":"2023-10-27T18:55:59Z",
  "region":"us-west-2",
  "resources":[
     "arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0/Lambda.1/finding/1dd8f2f8-cf1b-47c9-a875-8d7387fc9c23"
  ],
  "detail":{
     "findings":[
        {
           "SchemaVersion":"2018-10-08",
           "Id":"arn:aws:securityhub:us-west-2:111122223333:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.12/finding/1dd8f2f8-cf1b-47c9-a875-8d7387fc9c23",
           "ProductArn":"arn:aws:securityhub:us-west-2::product/aws/securityhub",
           "ProductName":"Security Hub",
           "CompanyName":"AWS",
           "Region":"us-west-2",
           "GeneratorId":"arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0/rule/1.12",
           "AwsAccountId":"111122223333",
           "Types":[
              "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
           ],
           "FirstObservedAt":"2020-10-05T19:18:47.775Z",
           "LastObservedAt":"2023-11-01T14:12:07.989Z",
           "CreatedAt":"2020-10-05T19:18:47.775Z",
           "UpdatedAt":"2023-11-01T14:11:53.720Z",
           "Severity":{
              "Product":0,
              "Label":"INFORMATIONAL",
              "Normalized":0,
              "Original":"INFORMATIONAL"
           },
           "Title":"1.12 Ensure no root user access key exists",
           "Description":"The root user is the most privileged user in an AWS account. AWS Access Keys provide programmatic access to a given AWS account. It is recommended that all access keys associated with the root user be removed.",
           "Remediation":{
              "Recommendation":{
                 "Text":"For information on how to correct this issue, consult the AWS Security Hub controls documentation.",
                 "Url":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation"
              }
           },
           "ProductFields":{
              "StandardsGuideArn":"arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
              "StandardsGuideSubscriptionArn":"arn:aws:securityhub:us-west-2:111122223333:subscription/cis-aws-foundations-benchmark/v/1.2.0",
              "RuleId":"1.12",
              "RecommendationUrl":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation",
              "RelatedAWSResources:0/name":"securityhub-iam-root-access-key-check-67cbb1c4",
              "RelatedAWSResources:0/type":"AWS::Config::ConfigRule",
              "StandardsControlArn":"arn:aws:securityhub:us-west-2:111122223333:control/cis-aws-foundations-benchmark/v/1.2.0/1.12",
              "aws/securityhub/ProductName":"Security Hub",
              "aws/securityhub/CompanyName":"AWS",
              "Resources:0/Id":"arn:aws:iam::111122223333:root",
              "aws/securityhub/FindingId":"arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/cis-aws-foundations-benchmark/v/1.2.0/1.12/finding/1dd8f2f8-cf1b-47c9-a875-8d7387fc9c23"
           },
           "Resources":[
              {
                 "Type":"AwsAccount",
                 "Id":"AWS::::Account:111122223333",
                 "Partition":"aws",
                 "Region":"us-west-2"
              }
           ],
           "Compliance":{
              "Status":"PASSED",
              `"SecurityControlId":"IAM.4"`,
              "AssociatedStandards":[
                 {
                    "StandardsId":"ruleset/cis-aws-foundations-benchmark/v/1.2.0"
                 }
              ]
           },
           "WorkflowState":"NEW",
           "Workflow":{
              "Status":"RESOLVED"
           },
           "RecordState":"ACTIVE",
           "FindingProviderFields":{
              "Severity":{
                 "Label":"INFORMATIONAL",
                 "Original":"INFORMATIONAL"
              },
              "Types":[
                 "Software and Configuration Checks/Industry and Regulatory Standards/CIS AWS Foundations Benchmark"
              ]
           },
           "ProcessedAt":"2023-11-01T14:12:13.436Z"
        }
     ]
  }
}
```

**Evidence for PCI.IAM.1 (PCI DSS)**

```
{
  "version":"0",
  "id":"12345678-1q2w-3e4r-5t6y-123456789012",
  "detail-type":"Security Hub Findings - Imported",
  "source":"aws.securityhub",
  "account":"111122223333",
  "time":"2023-10-27T18:55:59Z",
  "region":"us-west-2",
  "resources":[
     "arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/aws-foundational-security-best-practices/v/1.0.0/Lambda.1/finding/1dd8f2f8-cf1b-47c9-a875-8d7387fc9c23"
  ],
  "detail":{
     "findings":[
        {
           "SchemaVersion":"2018-10-08",
           "Id":"arn:aws:securityhub:us-west-2:111122223333:subscription/pci-dss/v/3.2.1/PCI.IAM.1/finding/3c75f651-6e2e-44f4-8e22-297d5c2d0c8b",
           "ProductArn":"arn:aws:securityhub:us-west-2::product/aws/securityhub",
           "ProductName":"Security Hub",
           "CompanyName":"AWS",
           "Region":"us-west-2",
           "GeneratorId":"pci-dss/v/3.2.1/PCI.IAM.1",
           "AwsAccountId":"111122223333",
           "Types":[
              "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS"
           ],
           "FirstObservedAt":"2020-10-05T19:18:47.788Z",
           "LastObservedAt":"2023-11-01T14:12:02.413Z",
           "CreatedAt":"2020-10-05T19:18:47.788Z",
           "UpdatedAt":"2023-11-01T14:11:53.720Z",
           "Severity":{
              "Product":0,
              "Label":"INFORMATIONAL",
              "Normalized":0,
              "Original":"INFORMATIONAL"
           },
           "Title":"PCI.IAM.1 IAM root user access key should not exist",
           "Description":"This AWS control checks whether the root user access key is available.",
           "Remediation":{
              "Recommendation":{
                 "Text":"For information on how to correct this issue, consult the AWS Security Hub controls documentation.",
                 "Url":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation"
              }
           },
           "ProductFields":{
              "StandardsArn":"arn:aws:securityhub:::standards/pci-dss/v/3.2.1",
              "StandardsSubscriptionArn":"arn:aws:securityhub:us-west-2:111122223333:subscription/pci-dss/v/3.2.1",
              "ControlId":"PCI.IAM.1",
              "RecommendationUrl":"https://docs.aws.amazon.com/console/securityhub/IAM.4/remediation",
              "RelatedAWSResources:0/name":"securityhub-iam-root-access-key-check-67cbb1c4",
              "RelatedAWSResources:0/type":"AWS::Config::ConfigRule",
              "StandardsControlArn":"arn:aws:securityhub:us-west-2:111122223333:control/pci-dss/v/3.2.1/PCI.IAM.1",
              "aws/securityhub/ProductName":"Security Hub",
              "aws/securityhub/CompanyName":"AWS",
              "Resources:0/Id":"arn:aws:iam::111122223333:root",
              "aws/securityhub/FindingId":"arn:aws:securityhub:us-west-2::product/aws/securityhub/arn:aws:securityhub:us-west-2:111122223333:subscription/pci-dss/v/3.2.1/PCI.IAM.1/finding/3c75f651-6e2e-44f4-8e22-297d5c2d0c8b"
           },
           "Resources":[
              {
                 "Type":"AwsAccount",
                 "Id":"AWS::::Account:111122223333",
                 "Partition":"aws",
                 "Region":"us-west-2"
              }
           ],
           "Compliance":{
              "Status":"PASSED",
              "RelatedRequirements":[
                 "PCI DSS 2.1",
                 "PCI DSS 2.2",
                 "PCI DSS 7.2.1"
              ],
              `"SecurityControlId":"IAM.4"`,
              "AssociatedStandards":[
                 {
                    "StandardsId":"standards/pci-dss/v/3.2.1"
                 }
              ]
           },
           "WorkflowState":"NEW",
           "Workflow":{
              "Status":"RESOLVED"
           },
           "RecordState":"ACTIVE",
           "FindingProviderFields":{
              "Severity":{
                 "Label":"INFORMATIONAL",
                 "Original":"INFORMATIONAL"
              },
              "Types":[
                 "Software and Configuration Checks/Industry and Regulatory Standards/PCI-DSS"
              ]
           },
           "ProcessedAt":"2023-11-01T14:12:05.950Z"
        }
     ]
  }
}
```

## Supported Security Hub CSPM

controls

The following Security Hub CSPM controls are currently supported by Audit Manager. You can use any of the
following standard-specific control ID keywords when you set up a data source for a custom
control.

| Security standard                        | Supported keyword in Audit Manager (standard control ID in Security Hub CSPM) | Related control documentation (corresponding security control ID in<br>Security Hub CSPM)                                                                                                           |
| ---------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CIS v1.2.0                               | 1.2                                                                           | [IAM.5](../../../securityhub/latest/userguide/iam-controls.md#iam-5 "../../../securityhub/latest/userguide/iam-controls.md#iam-5")                                                                  |
| CIS v1.2.0                               | 1.3                                                                           | [IAM.8](../../../securityhub/latest/userguide/iam-controls.md#iam-8 "../../../securityhub/latest/userguide/iam-controls.md#iam-8")                                                                  |
| CIS v1.2.0                               | 1.4                                                                           | [IAM.3](../../../securityhub/latest/userguide/iam-controls.md#iam-3 "../../../securityhub/latest/userguide/iam-controls.md#iam-3")                                                                  |
| CIS v1.2.0                               | 1.5                                                                           | [IAM.11](../../../securityhub/latest/userguide/iam-controls.md#iam-11 "../../../securityhub/latest/userguide/iam-controls.md#iam-11")                                                               |
| CIS v1.2.0                               | 1.6                                                                           | [IAM.12](../../../securityhub/latest/userguide/iam-controls.md#iam-12 "../../../securityhub/latest/userguide/iam-controls.md#iam-12")                                                               |
| CIS v1.2.0                               | 1.7                                                                           | [IAM.13](../../../securityhub/latest/userguide/iam-controls.md#iam-13 "../../../securityhub/latest/userguide/iam-controls.md#iam-13")                                                               |
| CIS v1.2.0                               | 1.8                                                                           | [IAM.14](../../../securityhub/latest/userguide/iam-controls.md#iam-14 "../../../securityhub/latest/userguide/iam-controls.md#iam-14")                                                               |
| CIS v1.2.0                               | 1.9                                                                           | [IAM.15](../../../securityhub/latest/userguide/iam-controls.md#iam-15 "../../../securityhub/latest/userguide/iam-controls.md#iam-15")                                                               |
| CIS v1.2.0                               | 1.10                                                                          | [IAM.16](../../../securityhub/latest/userguide/iam-controls.md#iam-16 "../../../securityhub/latest/userguide/iam-controls.md#iam-16")                                                               |
| CIS v1.2.0                               | 1.11                                                                          | [IAM.17](../../../securityhub/latest/userguide/iam-controls.md#iam-17 "../../../securityhub/latest/userguide/iam-controls.md#iam-17")                                                               |
| CIS v1.2.0                               | 1.12                                                                          | [IAM.4](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4")                                                                  |
| CIS v1.2.0                               | 1.13                                                                          | [IAM.9](../../../securityhub/latest/userguide/iam-controls.md#iam-9 "../../../securityhub/latest/userguide/iam-controls.md#iam-9")                                                                  |
| CIS v1.2.0                               | 1.14                                                                          | [IAM.6](../../../securityhub/latest/userguide/iam-controls.md#iam-6 "../../../securityhub/latest/userguide/iam-controls.md#iam-6")                                                                  |
| CIS v1.2.0                               | 1.16                                                                          | [IAM.2](../../../securityhub/latest/userguide/iam-controls.md#iam-2 "../../../securityhub/latest/userguide/iam-controls.md#iam-2")                                                                  |
| CIS v1.2.0                               | 1.20                                                                          | [IAM.18](../../../securityhub/latest/userguide/iam-controls.md#iam-18 "../../../securityhub/latest/userguide/iam-controls.md#iam-18")                                                               |
| CIS v1.2.0                               | 1.22                                                                          | [IAM.1](../../../securityhub/latest/userguide/iam-controls.md#iam-1 "../../../securityhub/latest/userguide/iam-controls.md#iam-1")                                                                  |
| CIS v1.2.0                               | 2.1                                                                           | [CloudTrail.1](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1")                               |
| CIS v1.2.0                               | 2.2                                                                           | [CloudTrail.4](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4")                               |
| CIS v1.2.0                               | 2.3                                                                           | [CloudTrail.6](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-6 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-6")                               |
| CIS v1.2.0                               | 2.4                                                                           | [CloudTrail.5](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-5 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-5")                               |
| CIS v1.2.0                               | 2.5                                                                           | [Config.1](../../../securityhub/latest/userguide/config-controls.md#config-1 "../../../securityhub/latest/userguide/config-controls.md#config-1")                                                   |
| CIS v1.2.0                               | 2.6                                                                           | [CloudTrail.7](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-7 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-7")                               |
| CIS v1.2.0                               | 2.7                                                                           | [CloudTrail.2](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2")                               |
| CIS v1.2.0                               | 2.8                                                                           | [KMS.4](../../../securityhub/latest/userguide/kms-controls.md#kms-4 "../../../securityhub/latest/userguide/kms-controls.md#kms-4")                                                                  |
| CIS v1.2.0                               | 2.9                                                                           | [EC2.6](../../../securityhub/latest/userguide/ec2-controls.md#ec2-6 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-6")                                                                  |
| CIS v1.2.0                               | 3.1                                                                           | [CloudWatch.2](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-2 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-2")                               |
| CIS v1.2.0                               | 3.2                                                                           | [CloudWatch.3](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-3 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-3")                               |
| CIS v1.2.0                               | 3.3                                                                           | [CloudWatch.1](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1")                               |
| CIS v1.2.0                               | 3.4                                                                           | [CloudWatch.4](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-4 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-4")                               |
| CIS v1.2.0                               | 3.5                                                                           | [CloudWatch.5](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-5 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-5")                               |
| CIS v1.2.0                               | 3.6                                                                           | [CloudWatch.6](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-6 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-6")                               |
| CIS v1.2.0                               | 3.7                                                                           | [CloudWatch.7](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-7 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-7")                               |
| CIS v1.2.0                               | 3.8                                                                           | [CloudWatch.8](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-8 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-8")                               |
| CIS v1.2.0                               | 3.9                                                                           | [CloudWatch.9](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-9 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-9")                               |
| CIS v1.2.0                               | 3.10                                                                          | [CloudWatch.10](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-10 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-10")                            |
| CIS v1.2.0                               | 3.11                                                                          | [CloudWatch.11](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-11 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-11")                            |
| CIS v1.2.0                               | 3.12                                                                          | [CloudWatch.12](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-12 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-12")                            |
| CIS v1.2.0                               | 3.13                                                                          | [CloudWatch.13](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-13 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-13")                            |
| CIS v1.2.0                               | 3.14                                                                          | [CloudWatch.14](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-14 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-14")                            |
| CIS v1.2.0                               | 4.1                                                                           | [EC2.13](../../../securityhub/latest/userguide/ec2-controls.md#ec2-13 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-13")                                                               |
| CIS v1.2.0                               | 4.2                                                                           | [EC2.14](../../../securityhub/latest/userguide/ec2-controls.md#ec2-14 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-14")                                                               |
| CIS v1.2.0                               | 4.3                                                                           | [EC2.2](../../../securityhub/latest/userguide/ec2-controls.md#ec2-2 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-2")                                                                  |
| PCI DSS                                  | PCI.AutoScaling.1                                                             | [AutoScaling.1](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-1 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-1")                          |
| PCI DSS                                  | PCI.CloudTrail.1                                                              | [CloudTrail.1](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1")                               |
| PCI DSS                                  | PCI.CloudTrail.2                                                              | [CloudTrail.2](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2")                               |
| PCI DSS                                  | PCI.CloudTrail.3                                                              | [CloudTrail.3](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-3 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-3")                               |
| PCI DSS                                  | PCI.CloudTrail.4                                                              | [CloudTrail.4](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4")                               |
| PCI DSS                                  | PCI.CodeBuild.1                                                               | [CodeBuild.1](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-1 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-1")                                    |
| PCI DSS                                  | PCI.CodeBuild.2                                                               | [CodeBuild.2](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-2 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-2")                                    |
| PCI DSS                                  | PCI.Config.1                                                                  | [Config.1](../../../securityhub/latest/userguide/config-controls.md#config-1 "../../../securityhub/latest/userguide/config-controls.md#config-1")                                                   |
| PCI DSS                                  | PCI.CW.1                                                                      | [CloudWatch.1](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1")                               |
| PCI DSS                                  | PCI.DMS.1                                                                     | [DMS.1](../../../securityhub/latest/userguide/dms-controls.md#dms-1 "../../../securityhub/latest/userguide/dms-controls.md#dms-1")                                                                  |
| PCI DSS                                  | PCI.EC2.1                                                                     | [EC2.1](../../../securityhub/latest/userguide/ec2-controls.md#ec2-1 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-1")                                                                  |
| PCI DSS                                  | PCI.EC2.2                                                                     | [EC2.2](../../../securityhub/latest/userguide/ec2-controls.md#ec2-2 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-2")                                                                  |
| PCI DSS                                  | PCI.EC2.3                                                                     | [EC2.3](../../../securityhub/latest/userguide/ec2-controls.md#ec2-3 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-3")                                                                  |
| PCI DSS                                  | PCI.EC2.4                                                                     | [EC2.12](../../../securityhub/latest/userguide/ec2-controls.md#ec2-12 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-12")                                                               |
| PCI DSS                                  | PCI.EC2.5                                                                     | [EC2.13](../../../securityhub/latest/userguide/ec2-controls.md#ec2-13 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-13")                                                               |
| PCI DSS                                  | PCI.EC2.6                                                                     | [EC2.6](../../../securityhub/latest/userguide/ec2-controls.md#ec2-6 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-6")                                                                  |
| PCI DSS                                  | PCI.ELBv2.1                                                                   | [ELB.1](../../../securityhub/latest/userguide/elb-controls.md#elb-1 "../../../securityhub/latest/userguide/elb-controls.md#elb-1")                                                                  |
| PCI DSS                                  | PCI.ES.1                                                                      | [ES.1](../../../securityhub/latest/userguide/es-controls.md#es-1 "../../../securityhub/latest/userguide/es-controls.md#es-1")                                                                       |
| PCI DSS                                  | PCI.ES.2                                                                      | [ES.2](../../../securityhub/latest/userguide/es-controls.md#es-2 "../../../securityhub/latest/userguide/es-controls.md#es-2")                                                                       |
| PCI DSS                                  | PCI.GuardDuty.1                                                               | [GuardDuty.1](../../../securityhub/latest/userguide/guardduty-controls.md#guardduty-1 "../../../securityhub/latest/userguide/guardduty-controls.md#guardduty-1")                                    |
| PCI DSS                                  | PCI.IAM.1                                                                     | [IAM.1](../../../securityhub/latest/userguide/iam-controls.md#iam-1 "../../../securityhub/latest/userguide/iam-controls.md#iam-1")                                                                  |
| PCI DSS                                  | PCI.IAM.2                                                                     | [IAM.2](../../../securityhub/latest/userguide/iam-controls.md#iam-2 "../../../securityhub/latest/userguide/iam-controls.md#iam-2")                                                                  |
| PCI DSS                                  | PCI.IAM.3                                                                     | [IAM.3](../../../securityhub/latest/userguide/iam-controls.md#iam-3 "../../../securityhub/latest/userguide/iam-controls.md#iam-3")                                                                  |
| PCI DSS                                  | PCI.IAM.4                                                                     | [IAM.4](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4")                                                                  |
| PCI DSS                                  | PCI.IAM.5                                                                     | [IAM.9](../../../securityhub/latest/userguide/iam-controls.md#iam-9 "../../../securityhub/latest/userguide/iam-controls.md#iam-9")                                                                  |
| PCI DSS                                  | PCI.IAM.6                                                                     | [IAM.6](../../../securityhub/latest/userguide/iam-controls.md#iam-6 "../../../securityhub/latest/userguide/iam-controls.md#iam-6")                                                                  |
| PCI DSS                                  | PCI.IAM.7                                                                     | [PCI.IAM.7](../../../securityhub/latest/userguide/iam-controls.md#iam-7 "../../../securityhub/latest/userguide/iam-controls.md#iam-7")                                                              |
| PCI DSS                                  | PCI.IAM.8                                                                     | [PCI.IAM8.](../../../securityhub/latest/userguide/iam-controls.md#iam-8 "../../../securityhub/latest/userguide/iam-controls.md#iam-8")                                                              |
| PCI DSS                                  | PCI.KMS.1                                                                     | [PCI.KMS.4](../../../securityhub/latest/userguide/kms-controls.md#kms-4 "../../../securityhub/latest/userguide/kms-controls.md#kms-4")                                                              |
| PCI DSS                                  | PCI.Lambda.1                                                                  | [Lambda.1](../../../securityhub/latest/userguide/lambda-controls.md#lambda-1 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-1")                                                   |
| PCI DSS                                  | PCI.Lambda.2                                                                  | [Lambda.3](../../../securityhub/latest/userguide/lambda-controls.md#lambda-3 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-3")                                                   |
| PCI DSS                                  | PCI.Opensearch.1                                                              | [Opensearch.1](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-1 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-1")                               |
| PCI DSS                                  | PCI.Opensearch.2                                                              | [Opensearch.2](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-2 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-2")                               |
| PCI DSS                                  | PCI.RDS.1                                                                     | [RDS.1](../../../securityhub/latest/userguide/rds-controls.md#rds-1 "../../../securityhub/latest/userguide/rds-controls.md#rds-1")                                                                  |
| PCI DSS                                  | PCI.RDS.2                                                                     | [RDS.2](../../../securityhub/latest/userguide/rds-controls.md#rds-2 "../../../securityhub/latest/userguide/rds-controls.md#rds-2")                                                                  |
| PCI DSS                                  | PCI.Redshift.1                                                                | [Redshift.1](../../../securityhub/latest/userguide/redshift-controls.md#redshift-1 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-1")                                         |
| PCI DSS                                  | PCI.S3.1                                                                      | [S3.1](../../../securityhub/latest/userguide/s3-controls.md#s3-1 "../../../securityhub/latest/userguide/s3-controls.md#s3-1")                                                                       |
| PCI DSS                                  | PCI.S3.2                                                                      | [S3.2](../../../securityhub/latest/userguide/s3-controls.md#s3-2 "../../../securityhub/latest/userguide/s3-controls.md#s3-2")                                                                       |
| PCI DSS                                  | PCI.S3.3                                                                      | [S3.3](../../../securityhub/latest/userguide/s3-controls.md#s3-3 "../../../securityhub/latest/userguide/s3-controls.md#s3-3")                                                                       |
| PCI DSS                                  | PCI.S3.4                                                                      | [S3.4](../../../securityhub/latest/userguide/s3-controls.md#s3-4 "../../../securityhub/latest/userguide/s3-controls.md#s3-4")                                                                       |
| PCI DSS                                  | PCI.S3.5                                                                      | [S3.5](../../../securityhub/latest/userguide/s3-controls.md#s3-5 "../../../securityhub/latest/userguide/s3-controls.md#s3-5")                                                                       |
| PCI DSS                                  | PCI.S3.6                                                                      | [S3.1](../../../securityhub/latest/userguide/s3-controls.md#s3-1 "../../../securityhub/latest/userguide/s3-controls.md#s3-1")                                                                       |
| PCI DSS                                  | PCI.SageMaker.1                                                               | [SageMaker.1](../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-1 "../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-1")                                    |
| PCI DSS                                  | PCI.SSM.1                                                                     | [SSM.1](../../../securityhub/latest/userguide/ssm-controls.md#ssm-1 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-1")                                                                  |
| PCI DSS                                  | PCI.SSM.2                                                                     | [SSM.2](../../../securityhub/latest/userguide/ssm-controls.md#ssm-2 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-2")                                                                  |
| PCI DSS                                  | PCI.SSM.3                                                                     | [SSM.3](../../../securityhub/latest/userguide/ssm-controls.md#ssm-3 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-3")                                                                  |
| AWS Foundational Security Best Practices | Account.1                                                                     | [Account.1](../../../securityhub/latest/userguide/account-controls.md#account-1 "../../../securityhub/latest/userguide/account-controls.md#account-1")                                              |
| AWS Foundational Security Best Practices | Account.2                                                                     | [Account.2](../../../securityhub/latest/userguide/account-controls.md#account-2 "../../../securityhub/latest/userguide/account-controls.md#account-2")                                              |
| AWS Foundational Security Best Practices | ACM.1                                                                         | [ACM.1](../../../securityhub/latest/userguide/acm-controls.md#acm-1 "../../../securityhub/latest/userguide/acm-controls.md#acm-1")                                                                  |
| AWS Foundational Security Best Practices | ACM.2                                                                         | [ACM.2](../../../securityhub/latest/userguide/acm-controls.md#acm-2 "../../../securityhub/latest/userguide/acm-controls.md#acm-2")                                                                  |
| AWS Foundational Security Best Practices | APIGateway.1                                                                  | [APIGateway.1](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-1 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-1")                               |
| AWS Foundational Security Best Practices | APIGateway.2                                                                  | [APIGateway.2](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-2 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-2")                               |
| AWS Foundational Security Best Practices | APIGateway.3                                                                  | [APIGateway.3](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-3 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-3")                               |
| AWS Foundational Security Best Practices | APIGateway.4                                                                  | [APIGateway.4](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-4 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-4")                               |
| AWS Foundational Security Best Practices | APIGateway.5                                                                  | [APIGateway.5](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-5 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-5")                               |
| AWS Foundational Security Best Practices | APIGateway.8                                                                  | [APIGateway.8](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-8 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-8")                               |
| AWS Foundational Security Best Practices | APIGateway.9                                                                  | [APIGateway.9](../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-9 "../../../securityhub/latest/userguide/apigateway-controls.md#apigateway-9")                               |
| AWS Foundational Security Best Practices | AppSync.2                                                                     | [AppSync.2](../../../securityhub/latest/userguide/appsync-controls.md#appsync-2 "../../../securityhub/latest/userguide/appsync-controls.md#appsync-2")                                              |
| AWS Foundational Security Best Practices | AppSync.5                                                                     | [AppSync.5](../../../securityhub/latest/userguide/appsync-controls.md#appsync-5 "../../../securityhub/latest/userguide/appsync-controls.md#appsync-5")                                              |
| AWS Foundational Security Best Practices | Athena.1                                                                      | [Athena.1](../../../securityhub/latest/userguide/athena-controls.md#athena-1 "../../../securityhub/latest/userguide/athena-controls.md#athena-1")                                                   |
| AWS Foundational Security Best Practices | AutoScaling.1                                                                 | [AutoScaling.1](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-1 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-1")                          |
| AWS Foundational Security Best Practices | AutoScaling.2                                                                 | [AutoScaling.2](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-2 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-2")                          |
| AWS Foundational Security Best Practices | AutoScaling.3                                                                 | [AutoScaling.3](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-3 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-3")                          |
| AWS Foundational Security Best Practices | AutoScaling.4                                                                 | [AutoScaling.4](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-4 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-4")                          |
| AWS Foundational Security Best Practices | Autoscaling.5                                                                 | [Autoscaling.5](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-5 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-5")                          |
| AWS Foundational Security Best Practices | AutoScaling.6                                                                 | [AutoScaling.6](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-6 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-6")                          |
| AWS Foundational Security Best Practices | AutoScaling.9                                                                 | [AutoScaling.9](../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-9 "../../../securityhub/latest/userguide/autoscaling-controls.md#autoscaling-9")                          |
| AWS Foundational Security Best Practices | Backup.1                                                                      | [Backup.1](../../../securityhub/latest/userguide/backup-controls.md#backup-1 "../../../securityhub/latest/userguide/backup-controls.md#backup-1")                                                   |
| AWS Foundational Security Best Practices | CloudFormation.1                                                              | [CloudFormation.1](../../../securityhub/latest/userguide/cloudformation-controls.md#cloudformation-1 "../../../securityhub/latest/userguide/cloudformation-controls.md#cloudformation-1")           |
| AWS Foundational Security Best Practices | CloudFront.1                                                                  | [CloudFront.1](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-1 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-1")                               |
| AWS Foundational Security Best Practices | CloudFront.2                                                                  | [CloudFront.2](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-2 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-2")                               |
| AWS Foundational Security Best Practices | CloudFront.3                                                                  | [CloudFront.3](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-3 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-3")                               |
| AWS Foundational Security Best Practices | CloudFront.4                                                                  | [CloudFront.4](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-4 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-4")                               |
| AWS Foundational Security Best Practices | CloudFront.5                                                                  | [CloudFront.5](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-5 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-5")                               |
| AWS Foundational Security Best Practices | CloudFront.6                                                                  | [CloudFront.6](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-6 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-6")                               |
| AWS Foundational Security Best Practices | CloudFront.7                                                                  | [CloudFront.7](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-7 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-7")                               |
| AWS Foundational Security Best Practices | CloudFront.8                                                                  | [CloudFront.8](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-8 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-8")                               |
| AWS Foundational Security Best Practices | CloudFront.9                                                                  | [CloudFront.9](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-9 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-9")                               |
| AWS Foundational Security Best Practices | CloudFront.10                                                                 | [CloudFront.10](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-10 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-10")                            |
| AWS Foundational Security Best Practices | CloudFront.12                                                                 | [CloudFront.12](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-12 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-12")                            |
| AWS Foundational Security Best Practices | CloudFront.13                                                                 | [CloudFront.13](../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-13 "../../../securityhub/latest/userguide/cloudfront-controls.md#cloudfront-13")                            |
| AWS Foundational Security Best Practices | CloudTrail.1                                                                  | [CloudTrail.1](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-1")                               |
| AWS Foundational Security Best Practices | CloudTrail.2                                                                  | [CloudTrail.2](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-2")                               |
| AWS Foundational Security Best Practices | CloudTrail.3                                                                  | [CloudTrail.3](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-3 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-3")                               |
| AWS Foundational Security Best Practices | CloudTrail.4                                                                  | [CloudTrail.4](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-4")                               |
| AWS Foundational Security Best Practices | CloudTrail.5                                                                  | [CloudTrail.5](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-5 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-5")                               |
| AWS Foundational Security Best Practices | CloudTrail.6                                                                  | [CloudTrail.6](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-6 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-6")                               |
| AWS Foundational Security Best Practices | CloudTrail.7                                                                  | [CloudTrail.7](../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-7 "../../../securityhub/latest/userguide/cloudtrail-controls.md#cloudtrail-7")                               |
| AWS Foundational Security Best Practices | CloudWatch.1                                                                  | [CloudWatch.1](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-1")                               |
| AWS Foundational Security Best Practices | CloudWatch.2                                                                  | [CloudWatch.2](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-2 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-2")                               |
| AWS Foundational Security Best Practices | CloudWatch.3                                                                  | [CloudWatch.3](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-3 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-3")                               |
| AWS Foundational Security Best Practices | CloudWatch.4                                                                  | [CloudWatch.4](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-4 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-4")                               |
| AWS Foundational Security Best Practices | CloudWatch.5                                                                  | [CloudWatch.5](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-5 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-5")                               |
| AWS Foundational Security Best Practices | CloudWatch.6                                                                  | [CloudWatch.6](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-6 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-6")                               |
| AWS Foundational Security Best Practices | CloudWatch.7                                                                  | [CloudWatch.7](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-7 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-7")                               |
| AWS Foundational Security Best Practices | CloudWatch.8                                                                  | [CloudWatch.8](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-8 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-8")                               |
| AWS Foundational Security Best Practices | CloudWatch.9                                                                  | [CloudWatch.9](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-9 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-9")                               |
| AWS Foundational Security Best Practices | CloudWatch.10                                                                 | [CloudWatch.10](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-10 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-10")                            |
| AWS Foundational Security Best Practices | CloudWatch.11                                                                 | [CloudWatch.11](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-11 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-11")                            |
| AWS Foundational Security Best Practices | CloudWatch.12                                                                 | [CloudWatch.12](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-12 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-12")                            |
| AWS Foundational Security Best Practices | CloudWatch.13                                                                 | [CloudWatch.13](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-13 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-13")                            |
| AWS Foundational Security Best Practices | CloudWatch.14                                                                 | [CloudWatch.14](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-14 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-14")                            |
| AWS Foundational Security Best Practices | CloudWatch.15                                                                 | [CloudWatch.15](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-15 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-15")                            |
| AWS Foundational Security Best Practices | CloudWatch.16                                                                 | [CloudWatch.16](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-16 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-16")                            |
| AWS Foundational Security Best Practices | CloudWatch.17                                                                 | [CloudWatch.17](../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-17 "../../../securityhub/latest/userguide/cloudwatch-controls.md#cloudwatch-17")                            |
| AWS Foundational Security Best Practices | CodeBuild.1                                                                   | [CodeBuild.1](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-1 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-1")                                    |
| AWS Foundational Security Best Practices | CodeBuild.2                                                                   | [CodeBuild.2](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-2 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-2")                                    |
| AWS Foundational Security Best Practices | CodeBuild.3                                                                   | [CodeBuild.3](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-3 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-3")                                    |
| AWS Foundational Security Best Practices | CodeBuild.4                                                                   | [CodeBuild.4](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-4 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-4")                                    |
| AWS Foundational Security Best Practices | CodeBuild.5                                                                   | [CodeBuild.5](../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-5 "../../../securityhub/latest/userguide/codebuild-controls.md#codebuild-5")                                    |
| AWS Foundational Security Best Practices | Config.1                                                                      | [Config.1](../../../securityhub/latest/userguide/config-controls.md#config-1 "../../../securityhub/latest/userguide/config-controls.md#config-1")                                                   |
| AWS Foundational Security Best Practices | DMS.1                                                                         | [DMS.1](../../../securityhub/latest/userguide/dms-controls.md#dms-1 "../../../securityhub/latest/userguide/dms-controls.md#dms-1")                                                                  |
| AWS Foundational Security Best Practices | DMS.6                                                                         | [DMS.6](../../../securityhub/latest/userguide/dms-controls.md#dms-6 "../../../securityhub/latest/userguide/dms-controls.md#dms-6")                                                                  |
| AWS Foundational Security Best Practices | DMS.7                                                                         | [DMS.7](../../../securityhub/latest/userguide/dms-controls.md#dms-7 "../../../securityhub/latest/userguide/dms-controls.md#dms-7")                                                                  |
| AWS Foundational Security Best Practices | DMS.8                                                                         | [DMS.8](../../../securityhub/latest/userguide/dms-controls.md#dms-8 "../../../securityhub/latest/userguide/dms-controls.md#dms-8")                                                                  |
| AWS Foundational Security Best Practices | DMS.9                                                                         | [DMS.9](../../../securityhub/latest/userguide/dms-controls.md#dms-9 "../../../securityhub/latest/userguide/dms-controls.md#dms-9")                                                                  |
| AWS Foundational Security Best Practices | DocumentDB.1                                                                  | [DocumentDB.1](../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-1 "../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-1")                               |
| AWS Foundational Security Best Practices | DocumentDB.2                                                                  | [DocumentDB.2](../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-2 "../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-2")                               |
| AWS Foundational Security Best Practices | DocumentDB.3                                                                  | [DocumentDB.3](../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-3 "../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-3")                               |
| AWS Foundational Security Best Practices | DocumentDB.4                                                                  | [DocumentDB.4](../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-4 "../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-4")                               |
| AWS Foundational Security Best Practices | DocumentDB.5                                                                  | [DocumentDB.5](../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-5 "../../../securityhub/latest/userguide/documentdb-controls.md#documentdb-5")                               |
| AWS Foundational Security Best Practices | DynamoDB.1                                                                    | [DynamoDB.1](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-1 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-1")                                         |
| AWS Foundational Security Best Practices | DynamoDB.2                                                                    | [DynamoDB.2](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-2 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-2")                                         |
| AWS Foundational Security Best Practices | DynamoDB.3                                                                    | [DynamoDB.3](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-3 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-3")                                         |
| AWS Foundational Security Best Practices | DynamoDB.4                                                                    | [DynamoDB.4](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-4 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-4")                                         |
| AWS Foundational Security Best Practices | DynamoDB.6                                                                    | [DynamoDB.6](../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-6 "../../../securityhub/latest/userguide/dynamodb-controls.md#dynamodb-6")                                         |
| AWS Foundational Security Best Practices | EC2.1                                                                         | [EC2.1](../../../securityhub/latest/userguide/ec2-controls.md#ec2-1 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-1")                                                                  |
| AWS Foundational Security Best Practices | EC2.2                                                                         | [EC2.2](../../../securityhub/latest/userguide/ec2-controls.md#ec2-2 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-2")                                                                  |
| AWS Foundational Security Best Practices | EC2.3                                                                         | [EC2.3](../../../securityhub/latest/userguide/ec2-controls.md#ec2-3 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-3")                                                                  |
| AWS Foundational Security Best Practices | EC2.4                                                                         | [EC2.4](../../../securityhub/latest/userguide/ec2-controls.md#ec2-4 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-4")                                                                  |
| AWS Foundational Security Best Practices | EC2.6                                                                         | [EC2.6](../../../securityhub/latest/userguide/ec2-controls.md#ec2-6 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-6")                                                                  |
| AWS Foundational Security Best Practices | EC2.7                                                                         | [EC2.7](../../../securityhub/latest/userguide/ec2-controls.md#ec2-7 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-7")                                                                  |
| AWS Foundational Security Best Practices | EC2.8                                                                         | [EC2.8](../../../securityhub/latest/userguide/ec2-controls.md#ec2-8 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-8")                                                                  |
| AWS Foundational Security Best Practices | EC2.9                                                                         | [EC2.9](../../../securityhub/latest/userguide/ec2-controls.md#ec2-9 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-9")                                                                  |
| AWS Foundational Security Best Practices | EC2.10                                                                        | [EC2.10](../../../securityhub/latest/userguide/ec2-controls.md#ec2-10 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-10")                                                               |
| AWS Foundational Security Best Practices | EC2.12                                                                        | [EC2.12](../../../securityhub/latest/userguide/ec2-controls.md#ec2-12 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-12")                                                               |
| AWS Foundational Security Best Practices | EC2.13                                                                        | [EC2.13](../../../securityhub/latest/userguide/ec2-controls.md#ec2-13 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-13")                                                               |
| AWS Foundational Security Best Practices | EC2.14                                                                        | [EC2.14](../../../securityhub/latest/userguide/ec2-controls.md#ec2-14 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-14")                                                               |
| AWS Foundational Security Best Practices | EC2.15                                                                        | [EC2.15](../../../securityhub/latest/userguide/ec2-controls.md#ec2-15 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-15")                                                               |
| AWS Foundational Security Best Practices | EC2.16                                                                        | [EC2.16](../../../securityhub/latest/userguide/ec2-controls.md#ec2-16 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-16")                                                               |
| AWS Foundational Security Best Practices | EC2.17                                                                        | [EC2.17](../../../securityhub/latest/userguide/ec2-controls.md#ec2-17 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-17")                                                               |
| AWS Foundational Security Best Practices | EC2.18                                                                        | [EC2.18](../../../securityhub/latest/userguide/ec2-controls.md#ec2-18 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-18")                                                               |
| AWS Foundational Security Best Practices | EC2.19                                                                        | [EC2.19](../../../securityhub/latest/userguide/ec2-controls.md#ec2-19 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-19")                                                               |
| AWS Foundational Security Best Practices | EC2.20                                                                        | [EC2.20](../../../securityhub/latest/userguide/ec2-controls.md#ec2-20 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-20")                                                               |
| AWS Foundational Security Best Practices | EC2.21                                                                        | [EC2.21](../../../securityhub/latest/userguide/ec2-controls.md#ec2-21 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-21")                                                               |
| AWS Foundational Security Best Practices | EC2.22                                                                        | [EC2.22](../../../securityhub/latest/userguide/ec2-controls.md#ec2-22 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-22")                                                               |
| AWS Foundational Security Best Practices | EC2.23                                                                        | [EC2.23](../../../securityhub/latest/userguide/ec2-controls.md#ec2-23 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-23")                                                               |
| AWS Foundational Security Best Practices | EC2.24                                                                        | [EC2.24](../../../securityhub/latest/userguide/ec2-controls.md#ec2-24 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-24")                                                               |
| AWS Foundational Security Best Practices | EC2.25                                                                        | [EC2.25](../../../securityhub/latest/userguide/ec2-controls.md#ec2-25 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-25")                                                               |
| AWS Foundational Security Best Practices | EC2.28                                                                        | [EC2.28](../../../securityhub/latest/userguide/ec2-controls.md#ec2-28 "../../../securityhub/latest/userguide/ec2-controls.md#ec2-28")                                                               |
| AWS Foundational Security Best Practices | EC2.51                                                                        | [EC2.51](https://portal.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51 "https://portal.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51")                 |
| AWS Foundational Security Best Practices | ECR.1                                                                         | [ECR.1](../../../securityhub/latest/userguide/ecr-controls.md#ecr-1 "../../../securityhub/latest/userguide/ecr-controls.md#ecr-1")                                                                  |
| AWS Foundational Security Best Practices | ECR.2                                                                         | [ECR.2](../../../securityhub/latest/userguide/ecr-controls.md#ecr-2 "../../../securityhub/latest/userguide/ecr-controls.md#ecr-2")                                                                  |
| AWS Foundational Security Best Practices | ECR.3                                                                         | [ECR.3](../../../securityhub/latest/userguide/ecr-controls.md#ecr-3 "../../../securityhub/latest/userguide/ecr-controls.md#ecr-3")                                                                  |
| AWS Foundational Security Best Practices | ECS.1                                                                         | [ECS.1](../../../securityhub/latest/userguide/ecs-controls.md#ecs-1 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-1")                                                                  |
| AWS Foundational Security Best Practices | ECS.2                                                                         | [ECS.2](../../../securityhub/latest/userguide/ecs-controls.md#ecs-2 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-2")                                                                  |
| AWS Foundational Security Best Practices | ECS.3                                                                         | [ECS.3](../../../securityhub/latest/userguide/ecs-controls.md#ecs-3 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-3")                                                                  |
| AWS Foundational Security Best Practices | ECS.4                                                                         | [ECS.4](../../../securityhub/latest/userguide/ecs-controls.md#ecs-4 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-4")                                                                  |
| AWS Foundational Security Best Practices | ECS.5                                                                         | [ECS.5](../../../securityhub/latest/userguide/ecs-controls.md#ecs-5 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-5")                                                                  |
| AWS Foundational Security Best Practices | ECS.8                                                                         | [ECS.8](../../../securityhub/latest/userguide/ecs-controls.md#ecs-8 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-8")                                                                  |
| AWS Foundational Security Best Practices | ECS.9                                                                         | [ECS.9](../../../securityhub/latest/userguide/ecs-controls.md#ecs-9 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-9")                                                                  |
| AWS Foundational Security Best Practices | ECS.10                                                                        | [ECS.10](../../../securityhub/latest/userguide/ecs-controls.md#ecs-10 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-10")                                                               |
| AWS Foundational Security Best Practices | ECS.12                                                                        | [ECS.12](../../../securityhub/latest/userguide/ecs-controls.md#ecs-12 "../../../securityhub/latest/userguide/ecs-controls.md#ecs-12")                                                               |
| AWS Foundational Security Best Practices | EFS.1                                                                         | [EFS.1](../../../securityhub/latest/userguide/efs-controls.md#efs-1 "../../../securityhub/latest/userguide/efs-controls.md#efs-1")                                                                  |
| AWS Foundational Security Best Practices | EFS.2                                                                         | [EFS.2](../../../securityhub/latest/userguide/efs-controls.md#efs-2 "../../../securityhub/latest/userguide/efs-controls.md#efs-2")                                                                  |
| AWS Foundational Security Best Practices | EFS.3                                                                         | [EFS.3](../../../securityhub/latest/userguide/efs-controls.md#efs-3 "../../../securityhub/latest/userguide/efs-controls.md#efs-3")                                                                  |
| AWS Foundational Security Best Practices | EFS.4                                                                         | [EFS.4](../../../securityhub/latest/userguide/efs-controls.md#efs-4 "../../../securityhub/latest/userguide/efs-controls.md#efs-4")                                                                  |
| AWS Foundational Security Best Practices | EKS.1                                                                         | [EKS.1](../../../securityhub/latest/userguide/eks-controls.md#eks-1 "../../../securityhub/latest/userguide/eks-controls.md#eks-1")                                                                  |
| AWS Foundational Security Best Practices | EKS.2                                                                         | [EKS.2](../../../securityhub/latest/userguide/eks-controls.md#eks-2 "../../../securityhub/latest/userguide/eks-controls.md#eks-2")                                                                  |
| AWS Foundational Security Best Practices | EKS.8                                                                         | [EKS.8](../../../securityhub/latest/userguide/eks-controls.md#eks-8 "../../../securityhub/latest/userguide/eks-controls.md#eks-8")                                                                  |
| AWS Foundational Security Best Practices | ElastiCache.1                                                                 | [ElastiCache.1](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-1 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-1")                          |
| AWS Foundational Security Best Practices | ElastiCache.2                                                                 | [ElastiCache.2](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-2 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-2")                          |
| AWS Foundational Security Best Practices | ElastiCache.3                                                                 | [ElastiCache.3](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-3 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-3")                          |
| AWS Foundational Security Best Practices | ElastiCache.4                                                                 | [ElastiCache.4](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-4 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-4")                          |
| AWS Foundational Security Best Practices | ElastiCache.5                                                                 | [ElastiCache.5](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-5 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-5")                          |
| AWS Foundational Security Best Practices | ElastiCache.6                                                                 | [ElastiCache.6](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-6 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-6")                          |
| AWS Foundational Security Best Practices | ElastiCache.7                                                                 | [ElastiCache.7](../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-7 "../../../securityhub/latest/userguide/elasticache-controls.md#elasticache-7")                          |
| AWS Foundational Security Best Practices | ElasticBeanstalk.1                                                            | [ElasticBeanstalk.1](../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-1 "../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-1") |
| AWS Foundational Security Best Practices | ElasticBeanstalk.2                                                            | [ElasticBeanstalk.2](../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-2 "../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-2") |
| AWS Foundational Security Best Practices | ElasticBeanstalk.3                                                            | [ElasticBeanstalk.3](../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-3 "../../../securityhub/latest/userguide/elasticbeanstalk-controls.md#elasticbeanstalk-3") |
| AWS Foundational Security Best Practices | ELB.1                                                                         | [ELB.1](../../../securityhub/latest/userguide/elb-controls.md#elb-1 "../../../securityhub/latest/userguide/elb-controls.md#elb-1")                                                                  |
| AWS Foundational Security Best Practices | ELB.2                                                                         | [ELB.2](../../../securityhub/latest/userguide/elb-controls.md#elb-2 "../../../securityhub/latest/userguide/elb-controls.md#elb-2")                                                                  |
| AWS Foundational Security Best Practices | ELB.3                                                                         | [ELB.3](../../../securityhub/latest/userguide/elb-controls.md#elb-3 "../../../securityhub/latest/userguide/elb-controls.md#elb-3")                                                                  |
| AWS Foundational Security Best Practices | ELB.4                                                                         | [ELB.4](../../../securityhub/latest/userguide/elb-controls.md#elb-4 "../../../securityhub/latest/userguide/elb-controls.md#elb-4")                                                                  |
| AWS Foundational Security Best Practices | ELB.5                                                                         | [ELB.5](../../../securityhub/latest/userguide/elb-controls.md#elb-5 "../../../securityhub/latest/userguide/elb-controls.md#elb-5")                                                                  |
| AWS Foundational Security Best Practices | ELB.6                                                                         | [ELB.6](../../../securityhub/latest/userguide/elb-controls.md#elb-6 "../../../securityhub/latest/userguide/elb-controls.md#elb-6")                                                                  |
| AWS Foundational Security Best Practices | ELB.7                                                                         | [ELB.7](../../../securityhub/latest/userguide/elb-controls.md#elb-7 "../../../securityhub/latest/userguide/elb-controls.md#elb-7")                                                                  |
| AWS Foundational Security Best Practices | ELB.8                                                                         | [ELB.8](../../../securityhub/latest/userguide/elb-controls.md#elb-8 "../../../securityhub/latest/userguide/elb-controls.md#elb-8")                                                                  |
| AWS Foundational Security Best Practices | ELB.9                                                                         | [ELB.9](../../../securityhub/latest/userguide/elb-controls.md#elb-9 "../../../securityhub/latest/userguide/elb-controls.md#elb-9")                                                                  |
| AWS Foundational Security Best Practices | ELB.10                                                                        | [ELB.10](../../../securityhub/latest/userguide/elb-controls.md#elb-10 "../../../securityhub/latest/userguide/elb-controls.md#elb-10")                                                               |
| AWS Foundational Security Best Practices | ELB.12                                                                        | [ELB.12](../../../securityhub/latest/userguide/elb-controls.md#elb-12 "../../../securityhub/latest/userguide/elb-controls.md#elb-12")                                                               |
| AWS Foundational Security Best Practices | ELB.13                                                                        | [ELB.13](../../../securityhub/latest/userguide/elb-controls.md#elb-13 "../../../securityhub/latest/userguide/elb-controls.md#elb-13")                                                               |
| AWS Foundational Security Best Practices | ELB.14                                                                        | [ELB.14](../../../securityhub/latest/userguide/elb-controls.md#elb-14 "../../../securityhub/latest/userguide/elb-controls.md#elb-14")                                                               |
| AWS Foundational Security Best Practices | ELB.16                                                                        | [ELB.16](../../../securityhub/latest/userguide/elb-controls.md#elb-16 "../../../securityhub/latest/userguide/elb-controls.md#elb-16")                                                               |
| AWS Foundational Security Best Practices | ELBv2.1                                                                       | [ELB.1](../../../securityhub/latest/userguide/elb-controls.md#elb-1 "../../../securityhub/latest/userguide/elb-controls.md#elb-1")                                                                  |
| AWS Foundational Security Best Practices | EMR.1                                                                         | [EMR.1](../../../securityhub/latest/userguide/emr-controls.md#emr-1 "../../../securityhub/latest/userguide/emr-controls.md#emr-1")                                                                  |
| AWS Foundational Security Best Practices | EMR.2                                                                         | [EMR.2](../../../securityhub/latest/userguide/emr-controls.md#emr-2 "../../../securityhub/latest/userguide/emr-controls.md#emr-2")                                                                  |
| AWS Foundational Security Best Practices | ES.1                                                                          | [ES.1](../../../securityhub/latest/userguide/es-controls.md#es-1 "../../../securityhub/latest/userguide/es-controls.md#es-1")                                                                       |
| AWS Foundational Security Best Practices | ES.2                                                                          | [ES.2](../../../securityhub/latest/userguide/es-controls.md#es-2 "../../../securityhub/latest/userguide/es-controls.md#es-2")                                                                       |
| AWS Foundational Security Best Practices | ES.3                                                                          | [ES.3](../../../securityhub/latest/userguide/es-controls.md#es-3 "../../../securityhub/latest/userguide/es-controls.md#es-3")                                                                       |
| AWS Foundational Security Best Practices | ES.4                                                                          | [ES.4](../../../securityhub/latest/userguide/es-controls.md#es-4 "../../../securityhub/latest/userguide/es-controls.md#es-4")                                                                       |
| AWS Foundational Security Best Practices | ES.5                                                                          | [ES.5](../../../securityhub/latest/userguide/es-controls.md#es-5 "../../../securityhub/latest/userguide/es-controls.md#es-5")                                                                       |
| AWS Foundational Security Best Practices | ES.6                                                                          | [ES.6](../../../securityhub/latest/userguide/es-controls.md#es-6 "../../../securityhub/latest/userguide/es-controls.md#es-6")                                                                       |
| AWS Foundational Security Best Practices | ES.7                                                                          | [ES.7](../../../securityhub/latest/userguide/es-controls.md#es-7 "../../../securityhub/latest/userguide/es-controls.md#es-7")                                                                       |
| AWS Foundational Security Best Practices | ES.8                                                                          | [ES.8](../../../securityhub/latest/userguide/es-controls.md#es-8 "../../../securityhub/latest/userguide/es-controls.md#es-8")                                                                       |
| AWS Foundational Security Best Practices | EventBridge.3                                                                 | [EventBridge3.](../../../securityhub/latest/userguide/eventbridge-controls.md#eventbridge-3 "../../../securityhub/latest/userguide/eventbridge-controls.md#eventbridge-3")                          |
| AWS Foundational Security Best Practices | EventBridge.4                                                                 | [EventBridge.4](../../../securityhub/latest/userguide/eventbridge-controls.md#eventbridge-4 "../../../securityhub/latest/userguide/eventbridge-controls.md#eventbridge-4")                          |
| AWS Foundational Security Best Practices | FSx.1                                                                         | [FSx.1](../../../securityhub/latest/userguide/fsx-controls.md#fsx-1 "../../../securityhub/latest/userguide/fsx-controls.md#fsx-1")                                                                  |
| AWS Foundational Security Best Practices | GuardDuty.1                                                                   | [GuardDuty.1](../../../securityhub/latest/userguide/guardduty-controls.md#guardduty-1 "../../../securityhub/latest/userguide/guardduty-controls.md#guardduty-1")                                    |
| AWS Foundational Security Best Practices | IAM.1                                                                         | [IAM.1](../../../securityhub/latest/userguide/iam-controls.md#iam-1 "../../../securityhub/latest/userguide/iam-controls.md#iam-1")                                                                  |
| AWS Foundational Security Best Practices | IAM.2                                                                         | [IAM.2](../../../securityhub/latest/userguide/iam-controls.md#iam-2 "../../../securityhub/latest/userguide/iam-controls.md#iam-2")                                                                  |
| AWS Foundational Security Best Practices | IAM.3                                                                         | [IAM.3](../../../securityhub/latest/userguide/iam-controls.md#iam-3 "../../../securityhub/latest/userguide/iam-controls.md#iam-3")                                                                  |
| AWS Foundational Security Best Practices | IAM.4                                                                         | [IAM.4](../../../securityhub/latest/userguide/iam-controls.md#iam-4 "../../../securityhub/latest/userguide/iam-controls.md#iam-4")                                                                  |
| AWS Foundational Security Best Practices | IAM.5                                                                         | [IAM.5](../../../securityhub/latest/userguide/iam-controls.md#iam-5 "../../../securityhub/latest/userguide/iam-controls.md#iam-5")                                                                  |
| AWS Foundational Security Best Practices | IAM.6                                                                         | [IAM.6](../../../securityhub/latest/userguide/iam-controls.md#iam-6 "../../../securityhub/latest/userguide/iam-controls.md#iam-6")                                                                  |
| AWS Foundational Security Best Practices | IAM.7                                                                         | [IAM.7](../../../securityhub/latest/userguide/iam-controls.md#iam-7 "../../../securityhub/latest/userguide/iam-controls.md#iam-7")                                                                  |
| AWS Foundational Security Best Practices | IAM.8                                                                         | [IAM.8](../../../securityhub/latest/userguide/iam-controls.md#iam-8 "../../../securityhub/latest/userguide/iam-controls.md#iam-8")                                                                  |
| AWS Foundational Security Best Practices | IAM.9                                                                         | [IAM.9](../../../securityhub/latest/userguide/iam-controls.md#iam-9 "../../../securityhub/latest/userguide/iam-controls.md#iam-9")                                                                  |
| AWS Foundational Security Best Practices | IAM.10                                                                        | [IAM.10](../../../securityhub/latest/userguide/iam-controls.md#iam-10 "../../../securityhub/latest/userguide/iam-controls.md#iam-10")                                                               |
| AWS Foundational Security Best Practices | IAM.11                                                                        | [IAM.11](../../../securityhub/latest/userguide/iam-controls.md#iam-11 "../../../securityhub/latest/userguide/iam-controls.md#iam-11")                                                               |
| AWS Foundational Security Best Practices | IAM.12                                                                        | [IAM.12](https://forums.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-12 "https://forums.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-12")                 |
| AWS Foundational Security Best Practices | IAM.13                                                                        | [IAM.13](../../../securityhub/latest/userguide/iam-controls.md#iam-13 "../../../securityhub/latest/userguide/iam-controls.md#iam-13")                                                               |
| AWS Foundational Security Best Practices | IAM.14                                                                        | [IAM.14](../../../securityhub/latest/userguide/iam-controls.md#iam-14 "../../../securityhub/latest/userguide/iam-controls.md#iam-14")                                                               |
| AWS Foundational Security Best Practices | IAM.15                                                                        | [IAM.15](../../../securityhub/latest/userguide/iam-controls.md#iam-15 "../../../securityhub/latest/userguide/iam-controls.md#iam-15")                                                               |
| AWS Foundational Security Best Practices | IAM.16                                                                        | [IAM.16](../../../securityhub/latest/userguide/iam-controls.md#iam-16 "../../../securityhub/latest/userguide/iam-controls.md#iam-16")                                                               |
| AWS Foundational Security Best Practices | IAM.17                                                                        | [IAM.17](../../../securityhub/latest/userguide/iam-controls.md#iam-17 "../../../securityhub/latest/userguide/iam-controls.md#iam-17")                                                               |
| AWS Foundational Security Best Practices | IAM.18                                                                        | [IAM.18](../../../securityhub/latest/userguide/iam-controls.md#iam-18 "../../../securityhub/latest/userguide/iam-controls.md#iam-18")                                                               |
| AWS Foundational Security Best Practices | IAM.19                                                                        | [IAM.19](../../../securityhub/latest/userguide/iam-controls.md#iam-19 "../../../securityhub/latest/userguide/iam-controls.md#iam-19")                                                               |
| AWS Foundational Security Best Practices | IAM.21                                                                        | [IAM.21](../../../securityhub/latest/userguide/iam-controls.md#iam-21 "../../../securityhub/latest/userguide/iam-controls.md#iam-21")                                                               |
| AWS Foundational Security Best Practices | IAM.22                                                                        | [IAM.22](../../../securityhub/latest/userguide/iam-controls.md#iam-22 "../../../securityhub/latest/userguide/iam-controls.md#iam-22")                                                               |
| AWS Foundational Security Best Practices | Kinesis.1                                                                     | [Kinesis.1](../../../securityhub/latest/userguide/kinesis-controls.md#kinesis-1 "../../../securityhub/latest/userguide/kinesis-controls.md#kinesis-1")                                              |
| AWS Foundational Security Best Practices | KMS.1                                                                         | [KMS.1](../../../securityhub/latest/userguide/kms-controls.md#kms-1 "../../../securityhub/latest/userguide/kms-controls.md#kms-1")                                                                  |
| AWS Foundational Security Best Practices | KMS.2                                                                         | [KMS.2](../../../securityhub/latest/userguide/kms-controls.md#kms-2 "../../../securityhub/latest/userguide/kms-controls.md#kms-2")                                                                  |
| AWS Foundational Security Best Practices | KMS.3                                                                         | [KMS.3](../../../securityhub/latest/userguide/kms-controls.md#kms-3 "../../../securityhub/latest/userguide/kms-controls.md#kms-3")                                                                  |
| AWS Foundational Security Best Practices | KMS.4                                                                         | [KMS.4](../../../securityhub/latest/userguide/kms-controls.md#kms-4 "../../../securityhub/latest/userguide/kms-controls.md#kms-4")                                                                  |
| AWS Foundational Security Best Practices | Lambda.1                                                                      | [Lambda.1](../../../securityhub/latest/userguide/lambda-controls.md#lambda-1 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-1")                                                   |
| AWS Foundational Security Best Practices | Lambda.2                                                                      | [Lambda.2](../../../securityhub/latest/userguide/lambda-controls.md#lambda-2 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-2")                                                   |
| AWS Foundational Security Best Practices | Lambda.3                                                                      | [Lambda.3](../../../securityhub/latest/userguide/lambda-controls.md#lambda-3 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-3")                                                   |
| AWS Foundational Security Best Practices | Lambda.5                                                                      | [Lambda.5](../../../securityhub/latest/userguide/lambda-controls.md#lambda-5 "../../../securityhub/latest/userguide/lambda-controls.md#lambda-5")                                                   |
| AWS Foundational Security Best Practices | Macie.1                                                                       | [Macie.1](../../../securityhub/latest/userguide/macie-controls.md#macie-1 "../../../securityhub/latest/userguide/macie-controls.md#macie-1")                                                        |
| AWS Foundational Security Best Practices | MQ.5                                                                          | [MQ.5](../../../securityhub/latest/userguide/mq-controls.md#mq-5 "../../../securityhub/latest/userguide/mq-controls.md#mq-5")                                                                       |
| AWS Foundational Security Best Practices | MQ.6                                                                          | [MQ.6](../../../securityhub/latest/userguide/mq-controls.md#mq-6 "../../../securityhub/latest/userguide/mq-controls.md#mq-6")                                                                       |
| AWS Foundational Security Best Practices | MSK.1                                                                         | [MSK.1](../../../securityhub/latest/userguide/msk-controls.md#msk-1 "../../../securityhub/latest/userguide/msk-controls.md#msk-1")                                                                  |
| AWS Foundational Security Best Practices | MSK.2                                                                         | [MSK.2](../../../securityhub/latest/userguide/msk-controls.md#msk-2 "../../../securityhub/latest/userguide/msk-controls.md#msk-2")                                                                  |
| AWS Foundational Security Best Practices | Neptune.1                                                                     | [Neptune.1](../../../securityhub/latest/userguide/neptune-controls.md#neptune-1 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-1")                                              |
| AWS Foundational Security Best Practices | Neptune.2                                                                     | [Neptune.2](../../../securityhub/latest/userguide/neptune-controls.md#neptune-2 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-2")                                              |
| AWS Foundational Security Best Practices | Neptune.3                                                                     | [Neptune.3](../../../securityhub/latest/userguide/neptune-controls.md#neptune-3 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-3")                                              |
| AWS Foundational Security Best Practices | Neptune.4                                                                     | [Neptune.4](../../../securityhub/latest/userguide/neptune-controls.md#neptune-4 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-4")                                              |
| AWS Foundational Security Best Practices | Neptune.5                                                                     | [Neptune.5](../../../securityhub/latest/userguide/neptune-controls.md#neptune-5 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-5")                                              |
| AWS Foundational Security Best Practices | Neptune.6                                                                     | [Neptune.6](../../../securityhub/latest/userguide/neptune-controls.md#neptune-6 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-6")                                              |
| AWS Foundational Security Best Practices | Neptune.7                                                                     | [Neptune.7](../../../securityhub/latest/userguide/neptune-controls.md#neptune-7 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-7")                                              |
| AWS Foundational Security Best Practices | Neptune.8                                                                     | [Neptune.8](../../../securityhub/latest/userguide/neptune-controls.md#neptune-8 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-8")                                              |
| AWS Foundational Security Best Practices | Neptune.9                                                                     | [Neptune.9](../../../securityhub/latest/userguide/neptune-controls.md#neptune-9 "../../../securityhub/latest/userguide/neptune-controls.md#neptune-9")                                              |
| AWS Foundational Security Best Practices | NetworkFirewall.1                                                             | [NetworkFirewall.1](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-1 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-1")      |
| AWS Foundational Security Best Practices | NetworkFirewall.2                                                             | [NetworkFirewall.2](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-2 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-2")      |
| AWS Foundational Security Best Practices | NetworkFirewall.3                                                             | [NetworkFirewall.3](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-3 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-3")      |
| AWS Foundational Security Best Practices | NetworkFirewall.4                                                             | [NetworkFirewall.4](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-4 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-4")      |
| AWS Foundational Security Best Practices | NetworkFirewall.5                                                             | [NetworkFirewall.5](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-5 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-5")      |
| AWS Foundational Security Best Practices | NetworkFirewall.6                                                             | [NetworkFirewall.6](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-6 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-6")      |
| AWS Foundational Security Best Practices | NetworkFirewall.9                                                             | [NetworkFirewall.9](../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-9 "../../../securityhub/latest/userguide/networkfirewall-controls.md#networkfirewall-9")      |
| AWS Foundational Security Best Practices | Opensearch.1                                                                  | [Opensearch.1](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-1 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-1")                               |
| AWS Foundational Security Best Practices | Opensearch.2                                                                  | [Opensearch.2](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-2 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-2")                               |
| AWS Foundational Security Best Practices | Opensearch.3                                                                  | [Opensearch.3](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-3 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-3")                               |
| AWS Foundational Security Best Practices | Opensearch.4                                                                  | [Opensearch.4](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-4 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-4")                               |
| AWS Foundational Security Best Practices | Opensearch.5                                                                  | [Opensearch.5](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-5 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-5")                               |
| AWS Foundational Security Best Practices | Opensearch.6                                                                  | [Opensearch.6](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-6 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-6")                               |
| AWS Foundational Security Best Practices | Opensearch.7                                                                  | [Opensearch.7](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-7 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-7")                               |
| AWS Foundational Security Best Practices | Opensearch.8                                                                  | [Opensearch.8](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-8 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-8")                               |
| AWS Foundational Security Best Practices | Opensearch.10                                                                 | [Opensearch.10](../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-10 "../../../securityhub/latest/userguide/opensearch-controls.md#opensearch-10")                            |
| AWS Foundational Security Best Practices | PCA.1                                                                         | [PCA.1](../../../securityhub/latest/userguide/pca-controls.md#pca-1 "../../../securityhub/latest/userguide/pca-controls.md#pca-1")                                                                  |
| AWS Foundational Security Best Practices | RDS.1                                                                         | [RDS.1](../../../securityhub/latest/userguide/rds-controls.md#rds-1 "../../../securityhub/latest/userguide/rds-controls.md#rds-1")                                                                  |
| AWS Foundational Security Best Practices | RDS.2                                                                         | [RDS.2](../../../securityhub/latest/userguide/rds-controls.md#rds-2 "../../../securityhub/latest/userguide/rds-controls.md#rds-2")                                                                  |
| AWS Foundational Security Best Practices | RDS.3                                                                         | [RDS.3](../../../securityhub/latest/userguide/rds-controls.md#rds-3 "../../../securityhub/latest/userguide/rds-controls.md#rds-3")                                                                  |
| AWS Foundational Security Best Practices | RDS.4                                                                         | [RDS.4](../../../securityhub/latest/userguide/rds-controls.md#rds-4 "../../../securityhub/latest/userguide/rds-controls.md#rds-4")                                                                  |
| AWS Foundational Security Best Practices | RDS.5                                                                         | [RDS.5](../../../securityhub/latest/userguide/rds-controls.md#rds-5 "../../../securityhub/latest/userguide/rds-controls.md#rds-5")                                                                  |
| AWS Foundational Security Best Practices | RDS.6                                                                         | [RDS.6](../../../securityhub/latest/userguide/rds-controls.md#rds-6 "../../../securityhub/latest/userguide/rds-controls.md#rds-6")                                                                  |
| AWS Foundational Security Best Practices | RDS.7                                                                         | [RDS.7](../../../securityhub/latest/userguide/rds-controls.md#rds-7 "../../../securityhub/latest/userguide/rds-controls.md#rds-7")                                                                  |
| AWS Foundational Security Best Practices | RDS.8                                                                         | [RDS.8](../../../securityhub/latest/userguide/rds-controls.md#rds-8 "../../../securityhub/latest/userguide/rds-controls.md#rds-8")                                                                  |
| AWS Foundational Security Best Practices | RDS.9                                                                         | [RDS.9](../../../securityhub/latest/userguide/rds-controls.md#rds-9 "../../../securityhub/latest/userguide/rds-controls.md#rds-9")                                                                  |
| AWS Foundational Security Best Practices | RDS.10                                                                        | [RDS.10](../../../securityhub/latest/userguide/rds-controls.md#rds-10 "../../../securityhub/latest/userguide/rds-controls.md#rds-10")                                                               |
| AWS Foundational Security Best Practices | RDS.11                                                                        | [RDS.11](../../../securityhub/latest/userguide/rds-controls.md#rds-11 "../../../securityhub/latest/userguide/rds-controls.md#rds-11")                                                               |
| AWS Foundational Security Best Practices | RDS.12                                                                        | [RDS.12](../../../securityhub/latest/userguide/rds-controls.md#rds-12 "../../../securityhub/latest/userguide/rds-controls.md#rds-12")                                                               |
| AWS Foundational Security Best Practices | RDS.13                                                                        | [RDS.13](../../../securityhub/latest/userguide/rds-controls.md#rds-13 "../../../securityhub/latest/userguide/rds-controls.md#rds-13")                                                               |
| AWS Foundational Security Best Practices | RDS.14                                                                        | [RDS.14](../../../securityhub/latest/userguide/rds-controls.md#rds-14 "../../../securityhub/latest/userguide/rds-controls.md#rds-14")                                                               |
| AWS Foundational Security Best Practices | RDS.15                                                                        | [RDS.15](../../../securityhub/latest/userguide/rds-controls.md#rds-15 "../../../securityhub/latest/userguide/rds-controls.md#rds-15")                                                               |
| AWS Foundational Security Best Practices | RDS.16                                                                        | [RDS.16](../../../securityhub/latest/userguide/rds-controls.md#rds-16 "../../../securityhub/latest/userguide/rds-controls.md#rds-16")                                                               |
| AWS Foundational Security Best Practices | RDS.17                                                                        | [RDS.17](../../../securityhub/latest/userguide/rds-controls.md#rds-17 "../../../securityhub/latest/userguide/rds-controls.md#rds-17")                                                               |
| AWS Foundational Security Best Practices | RDS.18                                                                        | [RDS.18](../../../securityhub/latest/userguide/rds-controls.md#rds-18 "../../../securityhub/latest/userguide/rds-controls.md#rds-18")                                                               |
| AWS Foundational Security Best Practices | RDS.19                                                                        | [RDS.19](../../../securityhub/latest/userguide/rds-controls.md#rds-19 "../../../securityhub/latest/userguide/rds-controls.md#rds-19")                                                               |
| AWS Foundational Security Best Practices | RDS.20                                                                        | [RDS.20](../../../securityhub/latest/userguide/rds-controls.md#rds-20 "../../../securityhub/latest/userguide/rds-controls.md#rds-20")                                                               |
| AWS Foundational Security Best Practices | RDS.21                                                                        | [RDS.21](../../../securityhub/latest/userguide/rds-controls.md#rds-21 "../../../securityhub/latest/userguide/rds-controls.md#rds-21")                                                               |
| AWS Foundational Security Best Practices | RDS.22                                                                        | [RDS.22](../../../securityhub/latest/userguide/rds-controls.md#rds-22 "../../../securityhub/latest/userguide/rds-controls.md#rds-22")                                                               |
| AWS Foundational Security Best Practices | RDS.23                                                                        | [RDS.23](../../../securityhub/latest/userguide/rds-controls.md#rds-23 "../../../securityhub/latest/userguide/rds-controls.md#rds-23")                                                               |
| AWS Foundational Security Best Practices | RDS.24                                                                        | [RDS.24](../../../securityhub/latest/userguide/rds-controls.md#rds-24 "../../../securityhub/latest/userguide/rds-controls.md#rds-24")                                                               |
| AWS Foundational Security Best Practices | RDS.25                                                                        | [RDS.25](../../../securityhub/latest/userguide/rds-controls.md#rds-25 "../../../securityhub/latest/userguide/rds-controls.md#rds-25")                                                               |
| AWS Foundational Security Best Practices | RDS.26                                                                        | [RDS.26](../../../securityhub/latest/userguide/rds-controls.md#rds-27 "../../../securityhub/latest/userguide/rds-controls.md#rds-27")                                                               |
| AWS Foundational Security Best Practices | RDS.27                                                                        | [RDS.27](../../../securityhub/latest/userguide/rds-controls.md#rds-26 "../../../securityhub/latest/userguide/rds-controls.md#rds-26")                                                               |
| AWS Foundational Security Best Practices | RDS.34                                                                        | [RDS.34](../../../securityhub/latest/userguide/rds-controls.md#rds-34 "../../../securityhub/latest/userguide/rds-controls.md#rds-34")                                                               |
| AWS Foundational Security Best Practices | RDS.35                                                                        | [RDS.35](../../../securityhub/latest/userguide/rds-controls.md#rds-35 "../../../securityhub/latest/userguide/rds-controls.md#rds-35")                                                               |
| AWS Foundational Security Best Practices | Redshift.1                                                                    | [Redshift.1](../../../securityhub/latest/userguide/redshift-controls.md#redshift-1 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-1")                                         |
| AWS Foundational Security Best Practices | Redshift.2                                                                    | [Redshift.2](../../../securityhub/latest/userguide/redshift-controls.md#redshift-2 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-2")                                         |
| AWS Foundational Security Best Practices | Redshift.3                                                                    | [Redshift.3](../../../securityhub/latest/userguide/redshift-controls.md#redshift-3 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-3")                                         |
| AWS Foundational Security Best Practices | Redshift.4                                                                    | [Redshift.4](../../../securityhub/latest/userguide/redshift-controls.md#redshift-4 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-4")                                         |
| AWS Foundational Security Best Practices | Redshift.6                                                                    | [Redshift.6](../../../securityhub/latest/userguide/redshift-controls.md#redshift-6 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-6")                                         |
| AWS Foundational Security Best Practices | Redshift.7                                                                    | [Redshift.7](../../../securityhub/latest/userguide/redshift-controls.md#redshift-7 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-7")                                         |
| AWS Foundational Security Best Practices | Redshift.8                                                                    | [Redshift.8](../../../securityhub/latest/userguide/redshift-controls.md#redshift-8 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-8")                                         |
| AWS Foundational Security Best Practices | Redshift.9                                                                    | [Redshift.9](../../../securityhub/latest/userguide/redshift-controls.md#redshift-9 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-9")                                         |
| AWS Foundational Security Best Practices | Redshift.10                                                                   | [Redshift.10](../../../securityhub/latest/userguide/redshift-controls.md#redshift-10 "../../../securityhub/latest/userguide/redshift-controls.md#redshift-10")                                      |
| AWS Foundational Security Best Practices | Route53.2                                                                     | [Route53.2](../../../securityhub/latest/userguide/route53-controls.md#route53-2 "../../../securityhub/latest/userguide/route53-controls.md#route53-2")                                              |
| AWS Foundational Security Best Practices | S3.1                                                                          | [S3.1](../../../securityhub/latest/userguide/s3-controls.md#s3-1 "../../../securityhub/latest/userguide/s3-controls.md#s3-1")                                                                       |
| AWS Foundational Security Best Practices | S3.2                                                                          | [S3.2](../../../securityhub/latest/userguide/s3-controls.md#s3-2 "../../../securityhub/latest/userguide/s3-controls.md#s3-2")                                                                       |
| AWS Foundational Security Best Practices | S3.3                                                                          | [S3.3](../../../securityhub/latest/userguide/s3-controls.md#s3-3 "../../../securityhub/latest/userguide/s3-controls.md#s3-3")                                                                       |
| AWS Foundational Security Best Practices | S3.4                                                                          | [S3.4](../../../securityhub/latest/userguide/s3-controls.md#s3-4 "../../../securityhub/latest/userguide/s3-controls.md#s3-4")                                                                       |
| AWS Foundational Security Best Practices | S3.5                                                                          | [S3.5](../../../securityhub/latest/userguide/s3-controls.md#s3-5 "../../../securityhub/latest/userguide/s3-controls.md#s3-5")                                                                       |
| AWS Foundational Security Best Practices | S3.6                                                                          | [S3.6](../../../securityhub/latest/userguide/s3-controls.md#s3-6 "../../../securityhub/latest/userguide/s3-controls.md#s3-6")                                                                       |
| AWS Foundational Security Best Practices | S3.7                                                                          | [S3.7](../../../securityhub/latest/userguide/s3-controls.md#s3-7 "../../../securityhub/latest/userguide/s3-controls.md#s3-7")                                                                       |
| AWS Foundational Security Best Practices | S3.8                                                                          | [S3.8](../../../securityhub/latest/userguide/s3-controls.md#s3-8 "../../../securityhub/latest/userguide/s3-controls.md#s3-8")                                                                       |
| AWS Foundational Security Best Practices | S3.9                                                                          | [S3.9](../../../securityhub/latest/userguide/s3-controls.md#s3-9 "../../../securityhub/latest/userguide/s3-controls.md#s3-9")                                                                       |
| AWS Foundational Security Best Practices | S3.11                                                                         | [S3.11](../../../securityhub/latest/userguide/s3-controls.md#s3-11 "../../../securityhub/latest/userguide/s3-controls.md#s3-11")                                                                    |
| AWS Foundational Security Best Practices | S3.12                                                                         | [S3.12](../../../securityhub/latest/userguide/s3-controls.md#s3-12 "../../../securityhub/latest/userguide/s3-controls.md#s3-12")                                                                    |
| AWS Foundational Security Best Practices | S3.13                                                                         | [S3.13](../../../securityhub/latest/userguide/s3-controls.md#s3-13 "../../../securityhub/latest/userguide/s3-controls.md#s3-13")                                                                    |
| AWS Foundational Security Best Practices | S3.14                                                                         | [S3.14](../../../securityhub/latest/userguide/s3-controls.md#s3-14 "../../../securityhub/latest/userguide/s3-controls.md#s3-14")                                                                    |
| AWS Foundational Security Best Practices | S3.15                                                                         | [S3.15](../../../securityhub/latest/userguide/s3-controls.md#s3-15 "../../../securityhub/latest/userguide/s3-controls.md#s3-15")                                                                    |
| AWS Foundational Security Best Practices | S3.17                                                                         | [S3.17](../../../securityhub/latest/userguide/s3-controls.md#s3-17 "../../../securityhub/latest/userguide/s3-controls.md#s3-17")                                                                    |
| AWS Foundational Security Best Practices | S3.19                                                                         | [S3.19](../../../securityhub/latest/userguide/s3-controls.md#s3-19 "../../../securityhub/latest/userguide/s3-controls.md#s3-19")                                                                    |
| AWS Foundational Security Best Practices | S3.19                                                                         | [S3.20](../../../securityhub/latest/userguide/s3-controls.md#s3-20 "../../../securityhub/latest/userguide/s3-controls.md#s3-20")                                                                    |
| AWS Foundational Security Best Practices | SageMaker.1                                                                   | [SageMaker.1](../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-1 "../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-1")                                    |
| AWS Foundational Security Best Practices | SageMaker.2                                                                   | [SageMaker.2](../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-2 "../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-2")                                    |
| AWS Foundational Security Best Practices | SageMaker.3                                                                   | [SageMaker.3](../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-3 "../../../securityhub/latest/userguide/sagemaker-controls.md#sagemaker-3")                                    |
| AWS Foundational Security Best Practices | SecretsManager.1                                                              | [SecretsManager.1](../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-1 "../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-1")           |
| AWS Foundational Security Best Practices | SecretsManager.2                                                              | [SecretsManager.2](../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-2 "../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-2")           |
| AWS Foundational Security Best Practices | SecretsManager.3                                                              | [SecretsManager.3](../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-3 "../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-3")           |
| AWS Foundational Security Best Practices | SecretsManager.4                                                              | [SecretsManager.4](../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-4 "../../../securityhub/latest/userguide/secretsmanager-controls.md#secretsmanager-4")           |
| AWS Foundational Security Best Practices | SNS.1                                                                         | [SNS.1](../../../securityhub/latest/userguide/sns-controls.md#sns-1 "../../../securityhub/latest/userguide/sns-controls.md#sns-1")                                                                  |
| AWS Foundational Security Best Practices | SNS.2                                                                         | [SNS.2](../../../securityhub/latest/userguide/sns-controls.md#sns-2 "../../../securityhub/latest/userguide/sns-controls.md#sns-2")                                                                  |
| AWS Foundational Security Best Practices | SQS.1                                                                         | [SQS.1](../../../securityhub/latest/userguide/sqs-controls.md#sqs-1 "../../../securityhub/latest/userguide/sqs-controls.md#sqs-1")                                                                  |
| AWS Foundational Security Best Practices | SSM.1                                                                         | [SSM.1](../../../securityhub/latest/userguide/ssm-controls.md#ssm-1 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-1")                                                                  |
| AWS Foundational Security Best Practices | SSM.2                                                                         | [SSM.2](../../../securityhub/latest/userguide/ssm-controls.md#ssm-2 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-2")                                                                  |
| AWS Foundational Security Best Practices | SSM.3                                                                         | [SSM.3](../../../securityhub/latest/userguide/ssm-controls.md#ssm-3 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-3")                                                                  |
| AWS Foundational Security Best Practices | SSM.4                                                                         | [SSM.4](../../../securityhub/latest/userguide/ssm-controls.md#ssm-4 "../../../securityhub/latest/userguide/ssm-controls.md#ssm-4")                                                                  |
| AWS Foundational Security Best Practices | StepFunctions.1                                                               | [StepFunctions.1](../../../securityhub/latest/userguide/stepfunctions-controls.md#stepfunctions-1 "../../../securityhub/latest/userguide/stepfunctions-controls.md#stepfunctions-1")                |
| AWS Foundational Security Best Practices | WAF.1                                                                         | [WAF.1](../../../securityhub/latest/userguide/waf-controls.md#waf-1 "../../../securityhub/latest/userguide/waf-controls.md#waf-1")                                                                  |
| AWS Foundational Security Best Practices | WAF.2                                                                         | [WAF.2](../../../securityhub/latest/userguide/waf-controls.md#waf-2 "../../../securityhub/latest/userguide/waf-controls.md#waf-2")                                                                  |
| AWS Foundational Security Best Practices | WAF.3                                                                         | [WAF.3](../../../securityhub/latest/userguide/waf-controls.md#waf-3 "../../../securityhub/latest/userguide/waf-controls.md#waf-3")                                                                  |
| AWS Foundational Security Best Practices | WAF.4                                                                         | [WAF.4](../../../securityhub/latest/userguide/waf-controls.md#waf-4 "../../../securityhub/latest/userguide/waf-controls.md#waf-4")                                                                  |
| AWS Foundational Security Best Practices | WAF.6                                                                         | [WAF.6](../../../securityhub/latest/userguide/waf-controls.md#waf-6 "../../../securityhub/latest/userguide/waf-controls.md#waf-6")                                                                  |
| AWS Foundational Security Best Practices | WAF.7                                                                         | [WAF.7](../../../securityhub/latest/userguide/waf-controls.md#waf-7 "../../../securityhub/latest/userguide/waf-controls.md#waf-7")                                                                  |
| AWS Foundational Security Best Practices | WAF.8                                                                         | [WAF.8](../../../securityhub/latest/userguide/waf-controls.md#waf-8 "../../../securityhub/latest/userguide/waf-controls.md#waf-8")                                                                  |
| AWS Foundational Security Best Practices | WAF.10                                                                        | [WAF.10](../../../securityhub/latest/userguide/waf-controls.md#waf-10 "../../../securityhub/latest/userguide/waf-controls.md#waf-10")                                                               |
| AWS Foundational Security Best Practices | WAF.11                                                                        | [WAF.11](../../../securityhub/latest/userguide/waf-controls.md#waf-11 "../../../securityhub/latest/userguide/waf-controls.md#waf-11")                                                               |
| AWS Foundational Security Best Practices | WAF.12                                                                        | [WAF.12](../../../securityhub/latest/userguide/waf-controls.md#waf-12 "../../../securityhub/latest/userguide/waf-controls.md#waf-12")                                                               |

## Additional

resources

- To find help with evidence collection issues for this data source type, see [My assessment isn’t collecting compliance check evidence
  from AWS Security Hub CSPM](evidence-collection-issues.md#no-evidence-from-security-hub "evidence-collection-issues.md#no-evidence-from-security-hub").
- To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md "create-controls.md").
- To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md "custom-frameworks.md").
- To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md "edit-custom-frameworks.md").
