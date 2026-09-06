

AWS Audit Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Audit Manager availability change](https://docs.aws.amazon.com/audit-manager/latest/userguide/audit-manager-availability-change.html). 

# AWS Security Hub CSPM controls supported by AWS Audit Manager
<a name="control-data-sources-ash"></a>



You can use Audit Manager to capture Security Hub CSPM findings as evidence for audits. When you create or edit a custom control, you can specify one or more Security Hub CSPM controls as a data source mapping for evidence collection. Security Hub CSPM performs compliance checks based on these controls, and Audit Manager reports the results as compliance check evidence.

**Contents**
+ [Key points](#using-security-hub-controls)
+ [Supported Security Hub CSPM controls](#security-hub-controls-for-custom-control-data-sources)
+ [Additional resources](#using-security-hub-controls-additional-resources)

## Key points
<a name="using-security-hub-controls"></a>
+ Audit Manager doesn’t collect evidence from [service-linked AWS Config rules that are created by Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-awsconfigrules.html). 
+ On November 9, 2022, Security Hub CSPM launched automated security checks aligned to the Center for Internet Security’s (CIS) AWS Foundations Benchmark version 1.4.0 requirements, Level 1 and 2 (CIS v1.4.0). In Security Hub CSPM, the [CIS v1.4.0 standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls-1.4.0.html) is supported in addition to the [CIS v1.2.0 standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cis-controls.html). 
+ We recommend that you turn on the [consolidated control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#consolidated-control-findings) setting in Security Hub CSPM if it's not turned on already. If you enable Security Hub CSPM on or after February 23, 2023, this setting is turned *on* by default. 

  When consolidated findings is enabled, Security Hub CSPM produces a single finding for each security check (even when the same check applies to multiple standards). Each Security Hub CSPM finding is collected as one unique resource assessment in Audit Manager. As a result, consolidated findings results in a decrease of the total unique resource assessments that Audit Manager performs for Security Hub CSPM findings. For this reason, using consolidated findings can often result in a reduction in your Audit Manager usages costs, without sacrificing evidence quality and availability. For more information about pricing, see [AWS Audit Manager Pricing](https://aws.amazon.com/audit-manager/pricing/).

 

### Examples of evidence when consolidated findings is turned on or off
<a name="collapsible-section-1"></a>

The following examples show a comparison of how Audit Manager collects and presents evidence depending on your Security Hub CSPM settings.

------
#### [ When consolidated findings is turned on  ]

Let's say that you have enabled the following three security standards in Security Hub CSPM: AWS FSBP, PCI DSS, and CIS Benchmark v1.2.0. 
+ All three of these standards use the same control ([IAM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4)) with the same underlying AWS Config rule ([iam-root-access-key-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html)).
+ Because the consolidated findings setting is **turned on**, Security Hub CSPM generates one single finding for this control.
+ Security Hub CSPM sends the consolidated finding to Audit Manager for this control.
+ The consolidated finding counts as one unique resource assessment in Audit Manager. As a result, one single piece of evidence is added to your assessment.

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

------
#### [ When consolidated findings is turned off ]

Let's say that you have enabled the following three security standards in Security Hub CSPM: AWS FSBP, PCI DSS, and CIS Benchmark v1.2.0. 
+ All three of these standards use the same control ([IAM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4)) with the same underlying AWS Config rule ([iam-root-access-key-check](https://docs.aws.amazon.com/config/latest/developerguide/iam-root-access-key-check.html)).
+ Because the consolidated findings setting is **turned off**, Security Hub CSPM generates a separate finding per security check for each enabled standard (in this case, three findings).
+ Security Hub CSPM sends three separate standard-specific findings to Audit Manager for this control.
+ The three findings count as three unique resource assessments in Audit Manager. As a result, three separate pieces of evidence are added to your assessment.

Here's an example of how that evidence might look. Note that in this example, each of the following three payloads has the same security control ID ({{`SecurityControlId":"IAM.4"`}}). For this reason, the assessment control that collects this evidence in Audit Manager (IAM.4) receives three separate pieces of evidence when the following findings come in from Security Hub CSPM.

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
              {{"SecurityControlId":"IAM.4"}},
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
              {{"SecurityControlId":"IAM.4"}},
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
              {{"SecurityControlId":"IAM.4"}},
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

------

## Supported Security Hub CSPM controls
<a name="security-hub-controls-for-custom-control-data-sources"></a>

The following Security Hub CSPM controls are currently supported by Audit Manager. You can use any of the following standard-specific control ID keywords when you set up a data source for a custom control. 


| Security standard | Supported keyword in Audit Manager (standard control ID in Security Hub CSPM) | Related control documentation (corresponding security control ID in Security Hub CSPM) | 
| --- | --- | --- | 
| CIS v1.2.0 | 1.2 | [IAM.5](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-5) | 
| CIS v1.2.0 | 1.3 | [IAM.8](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-8) | 
| CIS v1.2.0 | 1.4 | [IAM.3](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-3) | 
| CIS v1.2.0 | 1.5 | [IAM.11](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-11) | 
| CIS v1.2.0 | 1.6  | [IAM.12](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-12) | 
| CIS v1.2.0 | 1.7  | [IAM.13](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-13) | 
| CIS v1.2.0 | 1.8  | [IAM.14](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-14) | 
| CIS v1.2.0 | 1.9  | [IAM.15](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-15) | 
| CIS v1.2.0 | 1.10 | [IAM.16](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-16) | 
| CIS v1.2.0 | 1.11 | [IAM.17](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-17) | 
| CIS v1.2.0 | 1.12 | [IAM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4) | 
| CIS v1.2.0 | 1.13 | [IAM.9](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-9) | 
| CIS v1.2.0 | 1.14  | [IAM.6](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-6) | 
| CIS v1.2.0 | 1.16 | [IAM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-2) | 
| CIS v1.2.0 | 1.20 | [IAM.18](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-18) | 
| CIS v1.2.0 | 1.22  | [IAM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-1) | 
| CIS v1.2.0 | 2.1  | [CloudTrail.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-1) | 
| CIS v1.2.0 | 2.2  | [CloudTrail.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-4) | 
| CIS v1.2.0 | 2.3 | [CloudTrail.6](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-6) | 
| CIS v1.2.0 | 2.4  | [CloudTrail.5](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-5) | 
| CIS v1.2.0 | 2.5  | [Config.1](https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1) | 
| CIS v1.2.0 | 2.6  | [CloudTrail.7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-7) | 
| CIS v1.2.0 | 2.7  | [CloudTrail.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-2) | 
| CIS v1.2.0 | 2.8 | [KMS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-4) | 
| CIS v1.2.0 | 2.9 | [EC2.6](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-6) | 
| CIS v1.2.0 | 3.1  | [CloudWatch.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-2) | 
| CIS v1.2.0 | 3.2  | [CloudWatch.3](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-3) | 
| CIS v1.2.0 | 3.3 | [CloudWatch.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-1) | 
| CIS v1.2.0 | 3.4 | [CloudWatch.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-4) | 
| CIS v1.2.0 | 3.5 | [CloudWatch.5](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-5) | 
| CIS v1.2.0 | 3.6 | [CloudWatch.6](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-6) | 
| CIS v1.2.0 | 3.7  | [CloudWatch.7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-7) | 
| CIS v1.2.0 | 3.8 | [CloudWatch.8](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-8) | 
| CIS v1.2.0 | 3.9 | [CloudWatch.9](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-9) | 
| CIS v1.2.0 | 3.10 | [CloudWatch.10](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-10) | 
| CIS v1.2.0 | 3.11  | [CloudWatch.11](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-11) | 
| CIS v1.2.0 | 3.12 | [CloudWatch.12](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-12) | 
| CIS v1.2.0 | 3.13  | [CloudWatch.13](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-13) | 
| CIS v1.2.0 | 3.14  | [CloudWatch.14](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-14) | 
| CIS v1.2.0 | 4.1 | [EC2.13](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-13) | 
| CIS v1.2.0 | 4.2 | [EC2.14](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-14) | 
| CIS v1.2.0 | 4.3  | [EC2.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-2) | 
| PCI DSS | PCI.AutoScaling.1  | [AutoScaling.1](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-1) | 
| PCI DSS | PCI.CloudTrail.1  | [CloudTrail.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-1) | 
| PCI DSS | PCI.CloudTrail.2  | [CloudTrail.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-2) | 
| PCI DSS | PCI.CloudTrail.3  | [CloudTrail.3](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-3) | 
| PCI DSS  | PCI.CloudTrail.4  | [CloudTrail.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-4) | 
| PCI DSS | PCI.CodeBuild.1  | [CodeBuild.1](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-1) | 
| PCI DSS | PCI.CodeBuild.2  | [CodeBuild.2](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-2) | 
| PCI DSS | PCI.Config.1  | [Config.1](https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1) | 
| PCI DSS  | PCI.CW.1  | [CloudWatch.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-1) | 
| PCI DSS  | PCI.DMS.1 | [DMS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1) | 
| PCI DSS  | PCI.EC2.1 | [EC2.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-1) | 
| PCI DSS | PCI.EC2.2  | [EC2.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-2) | 
| PCI DSS  | PCI.EC2.3  | [EC2.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-3) | 
| PCI DSS | PCI.EC2.4  | [EC2.12](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-12) | 
| PCI DSS  | PCI.EC2.5  | [EC2.13](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-13) | 
| PCI DSS  | PCI.EC2.6  | [EC2.6](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-6) | 
| PCI DSS | PCI.ELBv2.1 | [ELB.1](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1) | 
| PCI DSS  | PCI.ES.1  | [ ES.1](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-1) | 
| PCI DSS  | PCI.ES.2  | [ ES.2](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-2) | 
| PCI DSS  | PCI.GuardDuty.1  | [GuardDuty.1](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-1) | 
| PCI DSS  | PCI.IAM.1  | [IAM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-1) | 
| PCI DSS  | PCI.IAM.2  | [IAM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-2) | 
| PCI DSS  | PCI.IAM.3  | [IAM.3](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-3) | 
| PCI DSS  | PCI.IAM.4  | [IAM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4) | 
| PCI DSS | PCI.IAM.5  | [IAM.9](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-9) | 
| PCI DSS  | PCI.IAM.6  | [IAM.6](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-6) | 
| PCI DSS  | PCI.IAM.7 | [PCI.IAM.7](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-7) | 
| PCI DSS  | PCI.IAM.8  | [PCI.IAM8.](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-8) | 
| PCI DSS  | PCI.KMS.1  | [PCI.KMS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-4) | 
| PCI DSS | PCI.Lambda.1 | [Lambda.1](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-1) | 
| PCI DSS | PCI.Lambda.2  | [Lambda.3](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-3) | 
| PCI DSS | PCI.Opensearch.1 | [Opensearch.1](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-1) | 
| PCI DSS  | PCI.Opensearch.2  | [Opensearch.2](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-2) | 
| PCI DSS | PCI.RDS.1 | [RDS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-1) | 
| PCI DSS  | PCI.RDS.2  | [RDS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-2) | 
| PCI DSS  | PCI.Redshift.1  | [Redshift.1](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-1) | 
| PCI DSS | PCI.S3.1 | [S3.1](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-1) | 
| PCI DSS  | PCI.S3.2 | [S3.2](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-2) | 
| PCI DSS  | PCI.S3.3  | [S3.3](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-3) | 
| PCI DSS  | PCI.S3.4  | [S3.4](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-4) | 
| PCI DSS  | PCI.S3.5  | [S3.5](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-5) | 
| PCI DSS  | PCI.S3.6  | [S3.1](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-1) | 
| PCI DSS  | PCI.SageMaker.1  | [SageMaker.1](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-1) | 
| PCI DSS  | PCI.SSM.1 | [SSM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-1) | 
| PCI DSS  | PCI.SSM.2  | [SSM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-2) | 
| PCI DSS | PCI.SSM.3 | [SSM.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-3) | 
| AWS Foundational Security Best Practices  | Account.1 | [Account.1](https://docs.aws.amazon.com/securityhub/latest/userguide/account-controls.html#account-1) | 
| AWS Foundational Security Best Practices  | Account.2 | [Account.2](https://docs.aws.amazon.com/securityhub/latest/userguide/account-controls.html#account-2) | 
| AWS Foundational Security Best Practices  | ACM.1 | [ACM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/acm-controls.html#acm-1) | 
| AWS Foundational Security Best Practices  | ACM.2 | [ACM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/acm-controls.html#acm-2) | 
| AWS Foundational Security Best Practices  | APIGateway.1 | [APIGateway.1](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-1) | 
| AWS Foundational Security Best Practices  | APIGateway.2 | [APIGateway.2](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-2) | 
| AWS Foundational Security Best Practices  | APIGateway.3 | [APIGateway.3](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-3) | 
| AWS Foundational Security Best Practices  | APIGateway.4 | [APIGateway.4](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-4) | 
| AWS Foundational Security Best Practices  | APIGateway.5 | [APIGateway.5](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-5) | 
| AWS Foundational Security Best Practices  | APIGateway.8 | [APIGateway.8](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-8) | 
| AWS Foundational Security Best Practices  | APIGateway.9 | [APIGateway.9](https://docs.aws.amazon.com/securityhub/latest/userguide/apigateway-controls.html#apigateway-9) | 
| AWS Foundational Security Best Practices  | AppSync.2 | [AppSync.2](https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-2) | 
| AWS Foundational Security Best Practices  | AppSync.5 | [AppSync.5](https://docs.aws.amazon.com/securityhub/latest/userguide/appsync-controls.html#appsync-5) | 
| AWS Foundational Security Best Practices  | Athena.1 | [Athena.1](https://docs.aws.amazon.com/securityhub/latest/userguide/athena-controls.html#athena-1) | 
| AWS Foundational Security Best Practices  | AutoScaling.1 | [AutoScaling.1](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-1) | 
| AWS Foundational Security Best Practices  | AutoScaling.2 | [AutoScaling.2](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-2) | 
| AWS Foundational Security Best Practices  | AutoScaling.3 | [AutoScaling.3](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-3) | 
| AWS Foundational Security Best Practices  | AutoScaling.4 | [AutoScaling.4](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-4) | 
| AWS Foundational Security Best Practices  | Autoscaling.5 | [Autoscaling.5](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-5) | 
| AWS Foundational Security Best Practices  | AutoScaling.6 | [AutoScaling.6](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-6) | 
| AWS Foundational Security Best Practices  | AutoScaling.9 | [AutoScaling.9](https://docs.aws.amazon.com/securityhub/latest/userguide/autoscaling-controls.html#autoscaling-9) | 
| AWS Foundational Security Best Practices  | Backup.1 | [Backup.1](https://docs.aws.amazon.com/securityhub/latest/userguide/backup-controls.html#backup-1) | 
| AWS Foundational Security Best Practices  | CloudFormation.1 | [CloudFormation.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudformation-controls.html#cloudformation-1) | 
| AWS Foundational Security Best Practices  | CloudFront.1 | [CloudFront.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-1) | 
| AWS Foundational Security Best Practices  | CloudFront.2 | [CloudFront.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-2) | 
| AWS Foundational Security Best Practices  | CloudFront.3 | [CloudFront.3](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-3) | 
| AWS Foundational Security Best Practices  | CloudFront.4 | [CloudFront.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-4) | 
| AWS Foundational Security Best Practices  | CloudFront.5 | [CloudFront.5](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-5) | 
| AWS Foundational Security Best Practices  | CloudFront.6 | [CloudFront.6](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-6) | 
| AWS Foundational Security Best Practices  | CloudFront.7 | [CloudFront.7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-7) | 
| AWS Foundational Security Best Practices  | CloudFront.8 | [CloudFront.8](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-8) | 
| AWS Foundational Security Best Practices  | CloudFront.9 | [CloudFront.9](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-9) | 
| AWS Foundational Security Best Practices  | CloudFront.10 | [CloudFront.10](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-10) | 
| AWS Foundational Security Best Practices  | CloudFront.12 | [CloudFront.12](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-12) | 
| AWS Foundational Security Best Practices  | CloudFront.13 | [CloudFront.13](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudfront-controls.html#cloudfront-13) | 
| AWS Foundational Security Best Practices  | CloudTrail.1 | [CloudTrail.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-1) | 
| AWS Foundational Security Best Practices  | CloudTrail.2 | [CloudTrail.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-2) | 
| AWS Foundational Security Best Practices  | CloudTrail.3 | [CloudTrail.3](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-3) | 
| AWS Foundational Security Best Practices  | CloudTrail.4 | [CloudTrail.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-4) | 
| AWS Foundational Security Best Practices  | CloudTrail.5 | [CloudTrail.5](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-5) | 
| AWS Foundational Security Best Practices  | CloudTrail.6 | [CloudTrail.6](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-6) | 
| AWS Foundational Security Best Practices  | CloudTrail.7 | [CloudTrail.7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudtrail-controls.html#cloudtrail-7) | 
| AWS Foundational Security Best Practices  | CloudWatch.1 | [CloudWatch.1](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-1) | 
| AWS Foundational Security Best Practices  | CloudWatch.2 | [CloudWatch.2](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-2) | 
| AWS Foundational Security Best Practices  | CloudWatch.3 | [CloudWatch.3](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-3) | 
| AWS Foundational Security Best Practices  | CloudWatch.4 | [CloudWatch.4](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-4) | 
| AWS Foundational Security Best Practices  | CloudWatch.5 | [CloudWatch.5](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-5) | 
| AWS Foundational Security Best Practices  | CloudWatch.6 | [CloudWatch.6](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-6) | 
| AWS Foundational Security Best Practices  | CloudWatch.7 | [CloudWatch.7](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-7) | 
| AWS Foundational Security Best Practices  | CloudWatch.8 | [CloudWatch.8](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-8) | 
| AWS Foundational Security Best Practices  | CloudWatch.9 | [CloudWatch.9](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-9) | 
| AWS Foundational Security Best Practices  | CloudWatch.10 | [CloudWatch.10](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-10) | 
| AWS Foundational Security Best Practices  | CloudWatch.11 | [CloudWatch.11](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-11) | 
| AWS Foundational Security Best Practices  | CloudWatch.12 | [CloudWatch.12](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-12) | 
| AWS Foundational Security Best Practices  | CloudWatch.13 | [CloudWatch.13](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-13) | 
| AWS Foundational Security Best Practices  | CloudWatch.14 | [CloudWatch.14](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-14) | 
| AWS Foundational Security Best Practices  | CloudWatch.15 | [CloudWatch.15](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-15) | 
| AWS Foundational Security Best Practices  | CloudWatch.16 | [CloudWatch.16](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-16) | 
| AWS Foundational Security Best Practices  | CloudWatch.17 | [CloudWatch.17](https://docs.aws.amazon.com/securityhub/latest/userguide/cloudwatch-controls.html#cloudwatch-17) | 
| AWS Foundational Security Best Practices  | CodeBuild.1 | [CodeBuild.1](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-1) | 
| AWS Foundational Security Best Practices  | CodeBuild.2 | [CodeBuild.2](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-2) | 
| AWS Foundational Security Best Practices  | CodeBuild.3 | [CodeBuild.3](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-3) | 
| AWS Foundational Security Best Practices  | CodeBuild.4 | [CodeBuild.4](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-4) | 
| AWS Foundational Security Best Practices  | CodeBuild.5 | [CodeBuild.5](https://docs.aws.amazon.com/securityhub/latest/userguide/codebuild-controls.html#codebuild-5) | 
| AWS Foundational Security Best Practices  | Config.1 | [Config.1](https://docs.aws.amazon.com/securityhub/latest/userguide/config-controls.html#config-1) | 
| AWS Foundational Security Best Practices  | DMS.1 | [DMS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-1) | 
| AWS Foundational Security Best Practices  | DMS.6 | [DMS.6](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-6) | 
| AWS Foundational Security Best Practices  | DMS.7 | [DMS.7](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-7) | 
| AWS Foundational Security Best Practices  | DMS.8 | [DMS.8](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-8) | 
| AWS Foundational Security Best Practices  | DMS.9 | [DMS.9](https://docs.aws.amazon.com/securityhub/latest/userguide/dms-controls.html#dms-9) | 
| AWS Foundational Security Best Practices | DocumentDB.1 | [DocumentDB.1](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-1) | 
| AWS Foundational Security Best Practices | DocumentDB.2 | [DocumentDB.2](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-2) | 
| AWS Foundational Security Best Practices | DocumentDB.3 | [DocumentDB.3](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-3) | 
| AWS Foundational Security Best Practices | DocumentDB.4 | [DocumentDB.4](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-4) | 
| AWS Foundational Security Best Practices | DocumentDB.5 | [DocumentDB.5](https://docs.aws.amazon.com/securityhub/latest/userguide/documentdb-controls.html#documentdb-5) | 
| AWS Foundational Security Best Practices  | DynamoDB.1 | [DynamoDB.1](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-1) | 
| AWS Foundational Security Best Practices  | DynamoDB.2 | [DynamoDB.2](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-2) | 
| AWS Foundational Security Best Practices  | DynamoDB.3 | [DynamoDB.3](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-3) | 
| AWS Foundational Security Best Practices | DynamoDB.4 | [DynamoDB.4](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-4) | 
| AWS Foundational Security Best Practices | DynamoDB.6 | [DynamoDB.6](https://docs.aws.amazon.com/securityhub/latest/userguide/dynamodb-controls.html#dynamodb-6) | 
| AWS Foundational Security Best Practices  | EC2.1 | [EC2.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-1) | 
| AWS Foundational Security Best Practices  | EC2.2 | [EC2.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-2) | 
| AWS Foundational Security Best Practices  | EC2.3 | [EC2.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-3) | 
| AWS Foundational Security Best Practices  | EC2.4 | [EC2.4](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-4) | 
| AWS Foundational Security Best Practices  | EC2.6 | [EC2.6](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-6) | 
| AWS Foundational Security Best Practices  | EC2.7 | [EC2.7](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-7) | 
| AWS Foundational Security Best Practices  | EC2.8 | [EC2.8](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-8) | 
| AWS Foundational Security Best Practices  | EC2.9 | [EC2.9](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-9) | 
| AWS Foundational Security Best Practices  | EC2.10 | [EC2.10](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-10) | 
| AWS Foundational Security Best Practices | EC2.12 | [EC2.12](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-12) | 
| AWS Foundational Security Best Practices | EC2.13 | [EC2.13](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-13) | 
| AWS Foundational Security Best Practices | EC2.14 | [EC2.14](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-14) | 
| AWS Foundational Security Best Practices  | EC2.15 | [EC2.15](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-15) | 
| AWS Foundational Security Best Practices  | EC2.16 | [EC2.16](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-16) | 
| AWS Foundational Security Best Practices  | EC2.17 | [EC2.17](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-17) | 
| AWS Foundational Security Best Practices  | EC2.18 | [EC2.18](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-18) | 
| AWS Foundational Security Best Practices  | EC2.19 | [EC2.19](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-19) | 
| AWS Foundational Security Best Practices  | EC2.20 | [EC2.20](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-20) | 
| AWS Foundational Security Best Practices  | EC2.21 | [EC2.21](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-21) | 
| AWS Foundational Security Best Practices  | EC2.22 | [EC2.22](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-22) | 
| AWS Foundational Security Best Practices  | EC2.23 | [EC2.23](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-23) | 
| AWS Foundational Security Best Practices  | EC2.24 | [EC2.24](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-24) | 
| AWS Foundational Security Best Practices  | EC2.25 | [EC2.25](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-25) | 
| AWS Foundational Security Best Practices | EC2.28 | [EC2.28](https://docs.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-28) | 
| AWS Foundational Security Best Practices | EC2.51 | [EC2.51](https://portal.aws.amazon.com/securityhub/latest/userguide/ec2-controls.html#ec2-51) | 
| AWS Foundational Security Best Practices  | ECR.1 | [ECR.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-1) | 
| AWS Foundational Security Best Practices  | ECR.2 | [ECR.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-2) | 
| AWS Foundational Security Best Practices  | ECR.3 | [ECR.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ecr-controls.html#ecr-3) | 
| AWS Foundational Security Best Practices  | ECS.1 | [ECS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-1) | 
| AWS Foundational Security Best Practices  | ECS.2 | [ECS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-2) | 
| AWS Foundational Security Best Practices  | ECS.3 | [ECS.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-3) | 
| AWS Foundational Security Best Practices  | ECS.4 | [ECS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-4) | 
| AWS Foundational Security Best Practices  | ECS.5 | [ECS.5](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-5) | 
| AWS Foundational Security Best Practices  | ECS.8 | [ECS.8](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-8) | 
| AWS Foundational Security Best Practices  | ECS.9 | [ECS.9](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-9) | 
| AWS Foundational Security Best Practices  | ECS.10 | [ECS.10](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-10) | 
| AWS Foundational Security Best Practices  | ECS.12 | [ECS.12](https://docs.aws.amazon.com/securityhub/latest/userguide/ecs-controls.html#ecs-12) | 
| AWS Foundational Security Best Practices  | EFS.1 | [EFS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-1) | 
| AWS Foundational Security Best Practices  | EFS.2 | [EFS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-2) | 
| AWS Foundational Security Best Practices  | EFS.3 | [EFS.3](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-3) | 
| AWS Foundational Security Best Practices  | EFS.4 | [EFS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/efs-controls.html#efs-4) | 
| AWS Foundational Security Best Practices  | EKS.1 | [EKS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-1) | 
| AWS Foundational Security Best Practices  | EKS.2 | [EKS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-2) | 
| AWS Foundational Security Best Practices  | EKS.8 | [EKS.8](https://docs.aws.amazon.com/securityhub/latest/userguide/eks-controls.html#eks-8) | 
| AWS Foundational Security Best Practices  | ElastiCache.1 | [ElastiCache.1](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-1) | 
| AWS Foundational Security Best Practices  | ElastiCache.2 | [ElastiCache.2](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-2) | 
| AWS Foundational Security Best Practices  | ElastiCache.3 | [ElastiCache.3](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-3) | 
| AWS Foundational Security Best Practices  | ElastiCache.4 | [ElastiCache.4](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-4) | 
| AWS Foundational Security Best Practices  | ElastiCache.5 | [ElastiCache.5](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-5) | 
| AWS Foundational Security Best Practices  | ElastiCache.6 | [ElastiCache.6](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-6) | 
| AWS Foundational Security Best Practices  | ElastiCache.7 | [ElastiCache.7](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticache-controls.html#elasticache-7) | 
| AWS Foundational Security Best Practices  | ElasticBeanstalk.1 | [ElasticBeanstalk.1](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-1) | 
| AWS Foundational Security Best Practices  | ElasticBeanstalk.2 | [ElasticBeanstalk.2](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-2) | 
| AWS Foundational Security Best Practices  | ElasticBeanstalk.3 | [ElasticBeanstalk.3](https://docs.aws.amazon.com/securityhub/latest/userguide/elasticbeanstalk-controls.html#elasticbeanstalk-3) | 
| AWS Foundational Security Best Practices  | ELB.1 | [ELB.1](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1) | 
| AWS Foundational Security Best Practices  | ELB.2 | [ELB.2](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-2) | 
| AWS Foundational Security Best Practices  | ELB.3 | [ELB.3](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-3) | 
| AWS Foundational Security Best Practices  | ELB.4 | [ELB.4](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-4) | 
| AWS Foundational Security Best Practices  | ELB.5 | [ELB.5](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-5) | 
| AWS Foundational Security Best Practices  | ELB.6 | [ELB.6](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-6) | 
| AWS Foundational Security Best Practices  | ELB.7 | [ELB.7](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-7) | 
| AWS Foundational Security Best Practices  | ELB.8 | [ELB.8](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-8) | 
| AWS Foundational Security Best Practices  | ELB.9 | [ELB.9](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-9) | 
| AWS Foundational Security Best Practices  | ELB.10 | [ELB.10](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-10) | 
| AWS Foundational Security Best Practices  | ELB.12 | [ELB.12](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-12) | 
| AWS Foundational Security Best Practices  | ELB.13 | [ELB.13](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-13) | 
| AWS Foundational Security Best Practices  | ELB.14 | [ELB.14](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-14) | 
| AWS Foundational Security Best Practices  | ELB.16 | [ELB.16](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-16) | 
| AWS Foundational Security Best Practices  | ELBv2.1 | [ELB.1](https://docs.aws.amazon.com/securityhub/latest/userguide/elb-controls.html#elb-1) | 
| AWS Foundational Security Best Practices  | EMR.1 | [EMR.1](https://docs.aws.amazon.com/securityhub/latest/userguide/emr-controls.html#emr-1) | 
| AWS Foundational Security Best Practices  | EMR.2 | [EMR.2](https://docs.aws.amazon.com/securityhub/latest/userguide/emr-controls.html#emr-2) | 
| AWS Foundational Security Best Practices  | ES.1 | [ES.1](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-1) | 
| AWS Foundational Security Best Practices  | ES.2 | [ES.2](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-2) | 
| AWS Foundational Security Best Practices  | ES.3 | [ES.3](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-3) | 
| AWS Foundational Security Best Practices  | ES.4 | [ES.4](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-4) | 
| AWS Foundational Security Best Practices  | ES.5 | [ES.5](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-5) | 
| AWS Foundational Security Best Practices  | ES.6 | [ES.6](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-6) | 
| AWS Foundational Security Best Practices  | ES.7 | [ES.7](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-7) | 
| AWS Foundational Security Best Practices  | ES.8 | [ES.8](https://docs.aws.amazon.com/securityhub/latest/userguide/es-controls.html#es-8) | 
| AWS Foundational Security Best Practices  | EventBridge.3 | [EventBridge3.](https://docs.aws.amazon.com/securityhub/latest/userguide/eventbridge-controls.html#eventbridge-3) | 
| AWS Foundational Security Best Practices  | EventBridge.4 | [EventBridge.4](https://docs.aws.amazon.com/securityhub/latest/userguide/eventbridge-controls.html#eventbridge-4) | 
| AWS Foundational Security Best Practices  | FSx.1 | [FSx.1](https://docs.aws.amazon.com/securityhub/latest/userguide/fsx-controls.html#fsx-1) | 
| AWS Foundational Security Best Practices  | GuardDuty.1 | [GuardDuty.1](https://docs.aws.amazon.com/securityhub/latest/userguide/guardduty-controls.html#guardduty-1) | 
| AWS Foundational Security Best Practices  | IAM.1 | [IAM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-1) | 
| AWS Foundational Security Best Practices  | IAM.2 | [IAM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-2) | 
| AWS Foundational Security Best Practices  | IAM.3 | [IAM.3](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-3) | 
| AWS Foundational Security Best Practices  | IAM.4 | [IAM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-4) | 
| AWS Foundational Security Best Practices  | IAM.5 | [IAM.5](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-5) | 
| AWS Foundational Security Best Practices  | IAM.6 | [IAM.6](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-6) | 
| AWS Foundational Security Best Practices  | IAM.7 | [IAM.7](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-7) | 
| AWS Foundational Security Best Practices  | IAM.8 | [IAM.8](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-8) | 
| AWS Foundational Security Best Practices  | IAM.9 | [IAM.9](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-9) | 
| AWS Foundational Security Best Practices  | IAM.10 | [IAM.10](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-10) | 
| AWS Foundational Security Best Practices  | IAM.11 | [IAM.11](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-11) | 
| AWS Foundational Security Best Practices  | IAM.12 | [IAM.12](https://forums.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-12) | 
| AWS Foundational Security Best Practices  | IAM.13 | [IAM.13](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-13) | 
| AWS Foundational Security Best Practices  | IAM.14 | [IAM.14](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-14) | 
| AWS Foundational Security Best Practices | IAM.15 | [IAM.15](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-15) | 
| AWS Foundational Security Best Practices  | IAM.16 | [IAM.16](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-16) | 
| AWS Foundational Security Best Practices  | IAM.17 | [IAM.17](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-17) | 
| AWS Foundational Security Best Practices  | IAM.18 | [IAM.18](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-18) | 
| AWS Foundational Security Best Practices  | IAM.19 | [IAM.19](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-19) | 
| AWS Foundational Security Best Practices  | IAM.21 | [IAM.21](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-21) | 
| AWS Foundational Security Best Practices  | IAM.22 | [IAM.22](https://docs.aws.amazon.com/securityhub/latest/userguide/iam-controls.html#iam-22) | 
| AWS Foundational Security Best Practices  | Kinesis.1 | [Kinesis.1](https://docs.aws.amazon.com/securityhub/latest/userguide/kinesis-controls.html#kinesis-1) | 
| AWS Foundational Security Best Practices  | KMS.1 | [KMS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-1) | 
| AWS Foundational Security Best Practices  | KMS.2 | [KMS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-2) | 
| AWS Foundational Security Best Practices  | KMS.3 | [KMS.3](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-3) | 
| AWS Foundational Security Best Practices  | KMS.4 | [KMS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/kms-controls.html#kms-4) | 
| AWS Foundational Security Best Practices  | Lambda.1 | [Lambda.1](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-1) | 
| AWS Foundational Security Best Practices  | Lambda.2 | [Lambda.2](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-2) | 
| AWS Foundational Security Best Practices  | Lambda.3 | [Lambda.3](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-3) | 
| AWS Foundational Security Best Practices  | Lambda.5 | [Lambda.5](https://docs.aws.amazon.com/securityhub/latest/userguide/lambda-controls.html#lambda-5) | 
| AWS Foundational Security Best Practices  | Macie.1 | [Macie.1](https://docs.aws.amazon.com/securityhub/latest/userguide/macie-controls.html#macie-1) | 
| AWS Foundational Security Best Practices  | MQ.5 | [MQ.5](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-5) | 
| AWS Foundational Security Best Practices  | MQ.6 | [MQ.6](https://docs.aws.amazon.com/securityhub/latest/userguide/mq-controls.html#mq-6) | 
| AWS Foundational Security Best Practices  | MSK.1 | [MSK.1](https://docs.aws.amazon.com/securityhub/latest/userguide/msk-controls.html#msk-1) | 
| AWS Foundational Security Best Practices  | MSK.2 | [MSK.2](https://docs.aws.amazon.com/securityhub/latest/userguide/msk-controls.html#msk-2) | 
| AWS Foundational Security Best Practices  | Neptune.1 | [Neptune.1](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-1) | 
| AWS Foundational Security Best Practices  | Neptune.2 | [Neptune.2](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-2) | 
| AWS Foundational Security Best Practices  | Neptune.3 | [Neptune.3](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-3) | 
| AWS Foundational Security Best Practices  | Neptune.4 | [Neptune.4](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-4) | 
| AWS Foundational Security Best Practices | Neptune.5 | [Neptune.5](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-5) | 
| AWS Foundational Security Best Practices  | Neptune.6 | [Neptune.6](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-6) | 
| AWS Foundational Security Best Practices  | Neptune.7 | [Neptune.7](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-7) | 
| AWS Foundational Security Best Practices  | Neptune.8 | [Neptune.8](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-8) | 
| AWS Foundational Security Best Practices  | Neptune.9 | [Neptune.9](https://docs.aws.amazon.com/securityhub/latest/userguide/neptune-controls.html#neptune-9) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.1 | [NetworkFirewall.1](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-1) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.2 | [NetworkFirewall.2](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-2) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.3 | [NetworkFirewall.3](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-3) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.4 | [NetworkFirewall.4](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-4) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.5 | [NetworkFirewall.5](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-5) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.6 | [NetworkFirewall.6](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-6) | 
| AWS Foundational Security Best Practices  | NetworkFirewall.9 | [NetworkFirewall.9](https://docs.aws.amazon.com/securityhub/latest/userguide/networkfirewall-controls.html#networkfirewall-9) | 
| AWS Foundational Security Best Practices  | Opensearch.1 | [Opensearch.1](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-1) | 
| AWS Foundational Security Best Practices  | Opensearch.2 | [Opensearch.2](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-2) | 
| AWS Foundational Security Best Practices  | Opensearch.3 | [Opensearch.3](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-3) | 
| AWS Foundational Security Best Practices  | Opensearch.4 | [Opensearch.4](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-4) | 
| AWS Foundational Security Best Practices  | Opensearch.5 | [Opensearch.5](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-5) | 
| AWS Foundational Security Best Practices  | Opensearch.6 | [Opensearch.6](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-6) | 
| AWS Foundational Security Best Practices  | Opensearch.7 | [Opensearch.7](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-7) | 
| AWS Foundational Security Best Practices  | Opensearch.8 | [Opensearch.8](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-8) | 
| AWS Foundational Security Best Practices  | Opensearch.10 | [Opensearch.10](https://docs.aws.amazon.com/securityhub/latest/userguide/opensearch-controls.html#opensearch-10) | 
| AWS Foundational Security Best Practices | PCA.1 | [PCA.1](https://docs.aws.amazon.com/securityhub/latest/userguide/pca-controls.html#pca-1) | 
| AWS Foundational Security Best Practices  | RDS.1 | [RDS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-1) | 
| AWS Foundational Security Best Practices  | RDS.2 | [RDS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-2) | 
| AWS Foundational Security Best Practices  | RDS.3 | [RDS.3](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-3) | 
| AWS Foundational Security Best Practices  | RDS.4 | [RDS.4](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-4) | 
| AWS Foundational Security Best Practices  | RDS.5 | [RDS.5](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-5) | 
| AWS Foundational Security Best Practices  | RDS.6 | [RDS.6](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-6) | 
| AWS Foundational Security Best Practices  | RDS.7 | [RDS.7](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-7) | 
| AWS Foundational Security Best Practices  | RDS.8 | [RDS.8](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-8) | 
| AWS Foundational Security Best Practices  | RDS.9 | [RDS.9](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-9) | 
| AWS Foundational Security Best Practices  | RDS.10 | [RDS.10](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-10) | 
| AWS Foundational Security Best Practices  | RDS.11 | [RDS.11](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-11) | 
| AWS Foundational Security Best Practices  | RDS.12 | [RDS.12](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-12) | 
| AWS Foundational Security Best Practices  | RDS.13 | [RDS.13](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-13) | 
| AWS Foundational Security Best Practices  | RDS.14 | [RDS.14](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-14) | 
| AWS Foundational Security Best Practices  | RDS.15 | [RDS.15](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-15) | 
| AWS Foundational Security Best Practices  | RDS.16 | [RDS.16](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-16) | 
| AWS Foundational Security Best Practices  | RDS.17 | [RDS.17](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-17) | 
| AWS Foundational Security Best Practices  | RDS.18 | [RDS.18](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-18) | 
| AWS Foundational Security Best Practices  | RDS.19 | [RDS.19](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-19) | 
| AWS Foundational Security Best Practices  | RDS.20 | [RDS.20](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-20) | 
| AWS Foundational Security Best Practices  | RDS.21 | [RDS.21](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-21) | 
| AWS Foundational Security Best Practices  | RDS.22 | [RDS.22](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-22) | 
| AWS Foundational Security Best Practices  | RDS.23 | [RDS.23](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-23) | 
| AWS Foundational Security Best Practices  | RDS.24 | [RDS.24](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-24) | 
| AWS Foundational Security Best Practices  | RDS.25 | [RDS.25](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-25) | 
| AWS Foundational Security Best Practices  | RDS.26 | [RDS.26](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-27) | 
| AWS Foundational Security Best Practices  | RDS.27 | [RDS.27](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-26) | 
| AWS Foundational Security Best Practices  | RDS.34 | [RDS.34](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-34) | 
| AWS Foundational Security Best Practices  | RDS.35 | [RDS.35](https://docs.aws.amazon.com/securityhub/latest/userguide/rds-controls.html#rds-35) | 
| AWS Foundational Security Best Practices  | Redshift.1 | [Redshift.1](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-1) | 
| AWS Foundational Security Best Practices  | Redshift.2 | [Redshift.2](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-2) | 
| AWS Foundational Security Best Practices  | Redshift.3 | [Redshift.3](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-3) | 
| AWS Foundational Security Best Practices  | Redshift.4 | [Redshift.4](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-4) | 
| AWS Foundational Security Best Practices  | Redshift.6 | [Redshift.6](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-6) | 
| AWS Foundational Security Best Practices  | Redshift.7 | [Redshift.7](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-7) | 
| AWS Foundational Security Best Practices  | Redshift.8 | [Redshift.8](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-8) | 
| AWS Foundational Security Best Practices  | Redshift.9 | [Redshift.9](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-9) | 
| AWS Foundational Security Best Practices  | Redshift.10 | [Redshift.10](https://docs.aws.amazon.com/securityhub/latest/userguide/redshift-controls.html#redshift-10) | 
| AWS Foundational Security Best Practices  | Route53.2 | [Route53.2](https://docs.aws.amazon.com/securityhub/latest/userguide/route53-controls.html#route53-2) | 
| AWS Foundational Security Best Practices  | S3.1 | [S3.1](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-1) | 
| AWS Foundational Security Best Practices  | S3.2 | [S3.2](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-2) | 
| AWS Foundational Security Best Practices  | S3.3 | [S3.3](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-3) | 
| AWS Foundational Security Best Practices  | S3.4 | [S3.4](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-4) | 
| AWS Foundational Security Best Practices  | S3.5 | [S3.5](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-5) | 
| AWS Foundational Security Best Practices  | S3.6 | [S3.6](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-6) | 
| AWS Foundational Security Best Practices  | S3.7 | [S3.7](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-7) | 
| AWS Foundational Security Best Practices  | S3.8 | [S3.8](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-8) | 
| AWS Foundational Security Best Practices  | S3.9 | [S3.9](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-9) | 
| AWS Foundational Security Best Practices  | S3.11 | [S3.11](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-11) | 
| AWS Foundational Security Best Practices  | S3.12 | [S3.12](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-12) | 
| AWS Foundational Security Best Practices  | S3.13 | [S3.13](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-13) | 
| AWS Foundational Security Best Practices  | S3.14 | [S3.14](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-14) | 
| AWS Foundational Security Best Practices  | S3.15 | [S3.15](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-15) | 
| AWS Foundational Security Best Practices  | S3.17 | [S3.17](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-17) | 
| AWS Foundational Security Best Practices  | S3.19 | [S3.19](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-19) | 
| AWS Foundational Security Best Practices  | S3.19 | [S3.20](https://docs.aws.amazon.com/securityhub/latest/userguide/s3-controls.html#s3-20) | 
| AWS Foundational Security Best Practices  | SageMaker.1 | [SageMaker.1](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-1) | 
| AWS Foundational Security Best Practices  | SageMaker.2 | [SageMaker.2](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-2) | 
| AWS Foundational Security Best Practices  | SageMaker.3 | [SageMaker.3](https://docs.aws.amazon.com/securityhub/latest/userguide/sagemaker-controls.html#sagemaker-3) | 
| AWS Foundational Security Best Practices  | SecretsManager.1 | [SecretsManager.1](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-1) | 
| AWS Foundational Security Best Practices  | SecretsManager.2 | [SecretsManager.2](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-2) | 
| AWS Foundational Security Best Practices  | SecretsManager.3 | [SecretsManager.3](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-3) | 
| AWS Foundational Security Best Practices  | SecretsManager.4 | [SecretsManager.4](https://docs.aws.amazon.com/securityhub/latest/userguide/secretsmanager-controls.html#secretsmanager-4) | 
| AWS Foundational Security Best Practices  | SNS.1 | [SNS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/sns-controls.html#sns-1) | 
| AWS Foundational Security Best Practices  | SNS.2 | [SNS.2](https://docs.aws.amazon.com/securityhub/latest/userguide/sns-controls.html#sns-2) | 
| AWS Foundational Security Best Practices  | SQS.1 | [SQS.1](https://docs.aws.amazon.com/securityhub/latest/userguide/sqs-controls.html#sqs-1) | 
| AWS Foundational Security Best Practices  | SSM.1 | [SSM.1](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-1) | 
| AWS Foundational Security Best Practices  | SSM.2 | [SSM.2](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-2) | 
| AWS Foundational Security Best Practices  | SSM.3 | [SSM.3](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-3) | 
| AWS Foundational Security Best Practices  | SSM.4 | [SSM.4](https://docs.aws.amazon.com/securityhub/latest/userguide/ssm-controls.html#ssm-4) | 
| AWS Foundational Security Best Practices  | StepFunctions.1 | [StepFunctions.1](https://docs.aws.amazon.com/securityhub/latest/userguide/stepfunctions-controls.html#stepfunctions-1) | 
| AWS Foundational Security Best Practices  | WAF.1 | [WAF.1](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-1) | 
| AWS Foundational Security Best Practices  | WAF.2 | [WAF.2](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-2) | 
| AWS Foundational Security Best Practices  | WAF.3 | [WAF.3](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-3) | 
| AWS Foundational Security Best Practices  | WAF.4 | [WAF.4](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-4) | 
| AWS Foundational Security Best Practices  | WAF.6 | [WAF.6](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-6) | 
| AWS Foundational Security Best Practices  | WAF.7 | [WAF.7](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-7) | 
| AWS Foundational Security Best Practices  | WAF.8 | [WAF.8](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-8) | 
| AWS Foundational Security Best Practices  | WAF.10 | [WAF.10](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-10) | 
| AWS Foundational Security Best Practices  | WAF.11 | [WAF.11](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-11) | 
| AWS Foundational Security Best Practices  | WAF.12 | [WAF.12](https://docs.aws.amazon.com/securityhub/latest/userguide/waf-controls.html#waf-12) | 

## Additional resources
<a name="using-security-hub-controls-additional-resources"></a>
+ To find help with evidence collection issues for this data source type, see [My assessment isn’t collecting compliance check evidence from AWS Security Hub CSPM](evidence-collection-issues.md#no-evidence-from-security-hub).
+ To create a custom control using this data source type, see [Creating a custom control in AWS Audit Manager](create-controls.md).
+ To create a custom framework that uses your custom control, see [Creating a custom framework in AWS Audit Manager](custom-frameworks.md). 
+ To add your custom control to an existing custom framework, see [Editing a custom framework in AWS Audit Manager](edit-custom-frameworks.md).