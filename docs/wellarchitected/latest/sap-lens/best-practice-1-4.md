# Best Practice 1.4 – Implement workload

configuration monitoring

Design and configure your workload to provide information about its current
configuration and changes to this configuration. Some examples are new or removed EC2
instances, scaling events, code change, patch levels, security group configuration, and
resource deletion. Use this information to determine when a response is required and to
decide whether a change was expected or permitted. Monitor the cost implications of
configuration changes and adjust or analyze budgets if required.

**Suggestion 1.4.1 - Implement workload configuration
monitoring**

Set up and configure AWS CloudTrail to monitor high priority and critical events,
particularly in your SAP production accounts. Example events include new Amazon EC2 instances,
Amazon EC2 decommissioning or changes, security group changes, and AWS KMS and IAM security
change events. Use these events to configure CloudWatch Log Alarms (if required) and take
action in the event of an unexpected change.

- AWS Documentation: [What Is
  AWS CloudTrail?](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- AWS Service: [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/")
- AWS Documentation: [Monitoring CloudTrail Log Files with Amazon CloudWatch Logs](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md")
- AWS Documentation: [AWS CloudTrail Security Best Practices](../../../awscloudtrail/latest/userguide/best-practices-security.md "../../../awscloudtrail/latest/userguide/best-practices-security.md")

**Suggestion 1.4.2 - Implement workload configuration enforcement and
remediation**

Set up and configure AWS Config to track, evaluate, and enforce configuration
policy of your AWS resources supporting your SAP production applications. Common
examples include enforcing read-only protection on S3 buckets containing SAP backups,
mandatory Amazon EBS encryption, blocking common network ports, and checking that all
resources have required tags. Use AWS Config [Managed Rules](../../../config/latest/developerguide/managed-rules-by-aws-config.md "../../../config/latest/developerguide/managed-rules-by-aws-config.md") to improve the security and change control posture of your AWS
environment supporting SAP. Use AWS tags to enforce configuration rules and apply
automated remediation where possible.

- AWS Service: [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- AWS Documentation: [Getting started with AWS Config](../../../config/latest/developerguide/getting-started.md "../../../config/latest/developerguide/getting-started.md")
- AWS Documentation: [Using AWS Config Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
- SAP on AWS Blog: [Audit your SAP systems with AWS Config – Part I](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-i/ "https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-i/")
- SAP on AWS Blog: [Audit your SAP systems with AWS Config – Part II](https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-ii/ "https://aws.amazon.com/blogs/awsforsap/audit-your-sap-systems-with-aws-config-part-ii/")
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/")

**Suggestion 1.4.3 - Implement workload cost monitoring**

Set up and configure [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/ "https://aws.amazon.com/aws-cost-management/aws-budgets/") with
custom budgets that alert you when you exceed (or are forecasted to exceed) your billing
thresholds. Align budgets with your projected SAP environment spend and monitor for any
anomalies to prevent cost overruns. Monitor your use and coverage of Reserved Instances
and Savings Plans by using budget reports. Use AWS tags to assist in understanding cost
allocation and usage across your SAP workload.

- AWS Blog: [Getting Started with AWS Budgets](https://aws.amazon.com/blogs/aws-cost-management/getting-started-with-aws-budgets/ "https://aws.amazon.com/blogs/aws-cost-management/getting-started-with-aws-budgets/")
- AWS Blog: [AWS Budgets Reports](https://aws.amazon.com/blogs/aws-cost-management/launch-aws-budgets-reports/ "https://aws.amazon.com/blogs/aws-cost-management/launch-aws-budgets-reports/")
- AWS Documentation: [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/")
- AWS Documentation: [AWS
  Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/ "https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/")
- SAP on AWS Blog: [Tagging Recommendations for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/ "https://aws.amazon.com/blogs/awsforsap/tagging-recommendations-for-sap-on-aws/")
