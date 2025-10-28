# Help protect sensitive log data with masking

You can help safeguard sensitive data that's ingested by CloudWatch Logs by using log group _data protection policies_. These policies
let you audit and mask sensitive data that appears in log events ingested by the log groups in your account.

When you create a data protection policy, then by default, sensitive data that
matches the data identifiers you've selected is masked at all egress points, including CloudWatch Logs Insights, metric filters,
and subscription filters. Only users who have the `logs:Unmask` IAM permission
can view unmasked data.

You can create a data protection policy for all log groups in your account,
and you can also create a data protection policies for individual log groups. When you create a policy for your entire account,
it applies to both existing log groups and log groups that are created in the future.

If you create a data protection policy
for your entire account and you also create a policy for a single log group, both policies apply to that log group. All
managed data identifiers that are specified in either policy are audited and masked in that log group.

###### Note

Masking sensitive data is supported only for log groups in the Standard log class. If you create a data
protection policy for all log groups in your account, it applies only to log groups in the Standard log class.
For more information
about log classes, see [Log classes](CloudWatch_Logs_Log_Classes.md "CloudWatch_Logs_Log_Classes.md").

Each log group can have only one log group-level data protection policy, but that policy can specify many
managed data identifiers to audit and mask. The limit for a data protection policy is 30,720 characters.

###### Important

Sensitive data is detected and masked when it is ingested into the log group. When you set a
data protection policy, log events ingested to the log group before that time are not masked.

CloudWatch Logs supports many _managed data identifiers_, which offer preconfigured data types
you can select to protect financial data, personal health information (PHI), and personally identifiable
information (PII). CloudWatch Logs data protection allows you to leverage pattern matching and machine learning models to
detect sensitive data. For some types of managed data identifiers, the detection depends on also finding certain keywords in
proximity with the sensitive data. You can also use custom data identifiers to create data identifiers tailored to your specific use case.

A metric is emitted to CloudWatch when sensitive data is detected that matches the data identifiers you select.
This is the **LogEventsWithFindings** metric and it is emitted in the **AWS/Logs**
namespace. You can use this metric to create CloudWatch alarms, and you can visualize it in graphs and dashboards.
Metrics emitted by data protection are vended metrics and are free of charge. For more information
about metrics that CloudWatch Logs sends to CloudWatch, see
[Monitoring with CloudWatch metrics](CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md "CloudWatch-Logs-Monitoring-CloudWatch-Metrics.md").

Each managed data identifier is designed to detect a specific type of sensitive data,
such as credit card numbers, AWS secret access keys, or passport numbers for a
particular country or region. When you create a data protection policy, you can
configure it to use these identifiers to analyze logs ingested by the log group, and
take actions when they are detected.

CloudWatch Logs data protection can detect the following categories of sensitive data by using managed data identifiers:

- Credentials, such as private keys or AWS secret access keys
- Financial information, such as credit card numbers
- Personally Identifiable Information (PII) such as driver’s licenses or social security numbers
- Protected Health Information (PHI) such as health insurance or medical identification numbers
- Device identifiers, such as IP addresses or MAC addresses
  For details about the types of data that you can protect, see [Types of data that you can protect](protect-sensitive-log-data-types.md "protect-sensitive-log-data-types.md").

###### Contents

- [Understanding data protection
  policies](cloudwatch-logs-data-protection-policies.md "cloudwatch-logs-data-protection-policies.md")
  - [What are data protection
    policies?](cloudwatch-logs-data-protection-policies.md#what-are-data-protection-policies "cloudwatch-logs-data-protection-policies.md#what-are-data-protection-policies")
  - [How is the data protection policy
    structured?](cloudwatch-logs-data-protection-policies.md#overview-of-data-protection-policies "cloudwatch-logs-data-protection-policies.md#overview-of-data-protection-policies")
    - [JSON properties for the
      data protection policy](cloudwatch-logs-data-protection-policies.md#data-protection-policy-json-properties "cloudwatch-logs-data-protection-policies.md#data-protection-policy-json-properties")
    - [JSON properties for a policy
      statement](cloudwatch-logs-data-protection-policies.md#policy-statement-json-properties "cloudwatch-logs-data-protection-policies.md#policy-statement-json-properties")
    - [JSON properties for a policy
      statement operation](cloudwatch-logs-data-protection-policies.md#statement-operation-json-properties "cloudwatch-logs-data-protection-policies.md#statement-operation-json-properties")

- [IAM permissions required to create or work with
  a data protection policy](data-protection-policy-permissions.md "data-protection-policy-permissions.md")
  - [Permissions required
    for account-level data protection policies](data-protection-policy-permissions.md#data-protection-policy-permissions-accountlevel "data-protection-policy-permissions.md#data-protection-policy-permissions-accountlevel")
  - [Permissions required
    for data protection policies for a single log group](data-protection-policy-permissions.md#data-protection-policy-permissions-loggroup "data-protection-policy-permissions.md#data-protection-policy-permissions-loggroup")
  - [Sample data protection policy](data-protection-policy-permissions.md#data-protection-policy-sample "data-protection-policy-permissions.md#data-protection-policy-sample")

- [Create an account-wide data protection policy](mask-sensitive-log-data-accountlevel.md "mask-sensitive-log-data-accountlevel.md")
  - [Console](mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-accountlevel-console "mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-accountlevel-console")
  - [AWS CLI](mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-accountlevel-cli "mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-accountlevel-cli")
    - [Data protection policy syntax for AWS CLI or API operations](mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-policysyntax-account "mask-sensitive-log-data-accountlevel.md#mask-sensitive-log-data-policysyntax-account")

- [Create a data protection policy for a single log group](mask-sensitive-log-data-start.md "mask-sensitive-log-data-start.md")
  - [Console](mask-sensitive-log-data-start.md#mask-sensitive-log-data-start-console "mask-sensitive-log-data-start.md#mask-sensitive-log-data-start-console")
  - [AWS CLI](mask-sensitive-log-data-start.md#mask-sensitive-log-data-start-cli "mask-sensitive-log-data-start.md#mask-sensitive-log-data-start-cli")
    - [Data protection policy syntax for AWS CLI or API operations](mask-sensitive-log-data-start.md#mask-sensitive-log-data-policysyntax "mask-sensitive-log-data-start.md#mask-sensitive-log-data-policysyntax")

- [View unmasked data](mask-sensitive-log-data-viewunmasked.md "mask-sensitive-log-data-viewunmasked.md")
- [Audit findings reports](mask-sensitive-log-data-audit-findings.md "mask-sensitive-log-data-audit-findings.md")
  - [Required key policy to send audit findings to an
    bucket protected by AWS KMS](mask-sensitive-log-data-audit-findings.md#mask-sensitive-log-data-audit-findings-kms "mask-sensitive-log-data-audit-findings.md#mask-sensitive-log-data-audit-findings-kms")

- [Types of data that you can protect](protect-sensitive-log-data-types.md "protect-sensitive-log-data-types.md")
  - [CloudWatch Logs managed data identifiers for sensitive
    data types](CWL-managed-data-identifiers.md "CWL-managed-data-identifiers.md")
    - [Credentials](protect-sensitive-log-data-types-credentials.md "protect-sensitive-log-data-types-credentials.md")
      - [Data identifier ARNs for
        credential data types](protect-sensitive-log-data-types-credentials.md#cwl-data-protection-credentials-arns "protect-sensitive-log-data-types-credentials.md#cwl-data-protection-credentials-arns")

    - [Device identifiers](protect-sensitive-log-data-types-device.md "protect-sensitive-log-data-types-device.md")
      - [Data identifier ARNs for device
        data types](protect-sensitive-log-data-types-device.md#cwl-data-protection-devices-arns "protect-sensitive-log-data-types-device.md#cwl-data-protection-devices-arns")

    - [Financial information](protect-sensitive-log-data-types-financial.md "protect-sensitive-log-data-types-financial.md")
      - [Data identifier ARNs for
        financial data types](protect-sensitive-log-data-types-financial.md#cwl-data-protection-financial-arns "protect-sensitive-log-data-types-financial.md#cwl-data-protection-financial-arns")

    - [Protected health information (PHI)](protect-sensitive-log-data-types-health.md "protect-sensitive-log-data-types-health.md")
      - [Data identifier ARNs for protected
        health information data types (PHI)](protect-sensitive-log-data-types-health.md#cwl-data-protection-phi-arns "protect-sensitive-log-data-types-health.md#cwl-data-protection-phi-arns")

    - [Personally identifiable information
      (PII)](protect-sensitive-log-data-types-pii.md "protect-sensitive-log-data-types-pii.md")
      - [Keywords for driver’s license
        identification numbers](protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-dl-keywords "protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-dl-keywords")
      - [Keywords for national
        identification numbers](protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-natlid-keywords "protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-natlid-keywords")
      - [Keywords for passport
        numbers](protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-passport-keywords "protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-pii-passport-keywords")
      - [Keywords for taxpayer
        identification and reference numbers](protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-financial-tin-keywords "protect-sensitive-log-data-types-pii.md#CWL-managed-data-identifiers-financial-tin-keywords")
      - [Data identifier ARNs for personally
        identifiable information (PII)](protect-sensitive-log-data-types-pii.md#CWL-data-protection-pii-arns "protect-sensitive-log-data-types-pii.md#CWL-data-protection-pii-arns")

  - [Custom data identifiers](CWL-custom-data-identifiers.md "CWL-custom-data-identifiers.md")
    - [What are custom data identifiers?](CWL-custom-data-identifiers.md#what-are-custom-data-identifiers "CWL-custom-data-identifiers.md#what-are-custom-data-identifiers")
    - [Custom data identifier
      constraints](CWL-custom-data-identifiers.md#custom-data-identifiers-constraints "CWL-custom-data-identifiers.md#custom-data-identifiers-constraints")
    - [Using custom data identifiers in the console](CWL-custom-data-identifiers.md#using-custom-data-identifiers-console "CWL-custom-data-identifiers.md#using-custom-data-identifiers-console")
    - [Using custom data identifiers in your data
      protection policy](CWL-custom-data-identifiers.md#using-custom-data-identifiers "CWL-custom-data-identifiers.md#using-custom-data-identifiers")
