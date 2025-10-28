# Infrastructure security monitoring in AMS

When you onboard to AMS Accelerate, AWS deploys the following AWS Config baseline infrastructure and set
of rules, AMS Accelerate uses these rules to monitor your accounts.

- **AWS Config service-linked role**: AMS Accelerate
  deploys the service-linked role named **AWSServiceRoleForConfig**, which is used by
  AWS Config to query the status of other AWS services. The **AWSServiceRoleForConfig**
  service-linked role trusts the AWS Config service to assume the role. The permissions policy for the
  **AWSServiceRoleForConfig** role contains read-only and write-only permissions on
  AWS Config resources and read-only permissions for resources in other services that AWS Config supports. If you
  already have a role configured with AWS Config Recorder, AMS Accelerate validates that the existing role has
  an AWS Config managed-policy attached. If not, AMS Accelerate replaces the role with the service-linked
  role **AWSServiceRoleForConfig**.
- **AWS Config recorder and delivery channel**: AWS Config uses
  the configuration recorder to detect changes in your resource configurations and capture
  these changes as configuration items. AMS Accelerate deploys the configuration recorder in all
  service AWS Regions, with continuous recording of all resources. AMS Accelerate also creates the config delivery
  channel, an Amazon S3 bucket, that's used to record changes that occur in your AWS resources. The config recorder updates configuration states through the delivery channel. The config
  recorder and delivery channel are required for AWS Config to work. AMS Accelerate creates the recorder
  in all AWS Regions, and a delivery channel in a single AWS Region.
  If you already have a recorder and delivery channel in an AWS Region, then AMS Accelerate doesn't delete the
  existing AWS Config resources, instead AMS Accelerate uses your existing recorder and delivery channel
  after validating that they are properly configured. For more information on how to reduce AWS Config costs, see [Reduce AWS Config costs in Accelerate](acc-sec-compliance.md#acc-sec-compliance-reduct-config-spend "acc-sec-compliance.md#acc-sec-compliance-reduct-config-spend").
- **AWS Config rules**:
  AMS Accelerate maintains a library of AWS Config Rules and remediation actions to help you comply with
  industry standards for security and operational integrity.

AWS Config Rules continuously tracks configuration changes among your recorded resources.
If a change violates any rule conditions, AMS reports its findings, and allows you to
remediate violations automatically or by request, according to the severity of the violation.
AWS Config Rules facilitate compliance with standards set by: the Center for Internet Security (CIS),
the National Institute of Standards and Technology (NIST) Cloud Security Framework (CSF),
the Health Insurance Portability and Accountability Act (HIPAA), and the Payment Card
Industry (PCI) Data Security Standard (DSS).

- **AWS Config aggregator authorization**: An aggregator
  is an AWS Config resource type that collects AWS Config configuration and compliance data from multiple
  accounts and multiple Regions. AMS Accelerate onboards your account to a config aggregator from
  which AMS Accelerate
  aggregates your account's resource configuration information and config compliance
  data and
  generates the compliance report. If there are existing aggregators configured in
  the AMS-owned account, AMS Accelerate deploys an additional aggregator and the existing aggregator is not
  modified.

###### Note

The Config aggregator is not set up in your accounts; rather, it is set up in AMS-owned accounts and
your account(s) are onboarded to it.
To learn more about AWS Config, see:

- AWS Config: [What Is Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- AWS Config Rules: [Evaluating Resources with Rules](../../../config/latest/developerguide/evaluate-config.md "../../../config/latest/developerguide/evaluate-config.md")
- AWS Config Rules: [Dynamic Compliance Checking: AWS Config Rules – Dynamic Compliance Checking for Cloud Resources](https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/ "https://aws.amazon.com/blogs/aws/aws-config-rules-dynamic-compliance-checking-for-cloud-resources/")
- AWS Config Aggregator: [Multi-Account Multi-Region Data Aggregation](../../../config/latest/developerguide/aggregate-data.md "../../../config/latest/developerguide/aggregate-data.md")
  For information on reports, see [AWS Config Control Compliance report](acc-report-config-control-compliance.md "acc-report-config-control-compliance.md").
