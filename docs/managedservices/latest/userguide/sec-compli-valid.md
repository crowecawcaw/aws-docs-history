# Compliance validation

AMS deploys and manages a library of AWS Config rules and remediation actions,
to protect against misconfigurations that could reduce the security and operational integrity of your accounts.

As an example, when an Amazon S3 bucket is created, AWS Config can evaluate the Amazon S3 bucket against a rule that requires Amazon S3 buckets to deny public read access.
If the Amazon S3 bucket policy or bucket access control list (ACL), allows public read access, AWS Config flags both the
bucket and the rule as noncompliant. These AWS Config Rules mark resources as either Compliant, Noncompliant, or Not Applicable, based on the result of their evaluation.
For more information about AWS Config service, see the
[AWS Config Developer Guide](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md").

You can use the AWS Config console, AWS CLI, or AWS Config API to view the rules deployed in your
account and the compliance state of your rules and resources. For more information, see the AWS Config documentation:
[Viewing Configuration Compliance](../../../config/latest/developerguide/evaluate-config_view-compliance.md "../../../config/latest/developerguide/evaluate-config_view-compliance.md").

###### Note

Additional information on this topic is available by accessing AWS Artifact reports. For more information, see [Downloading reports in AWS Artifact](../../../artifact/latest/ug/downloading-documents.md "../../../artifact/latest/ug/downloading-documents.md"). To access AWS Artifact, you can contact your CSDM for instructions or go to [Getting Started with AWS Artifact](https://aws.amazon.com/artifact/getting-started "https://aws.amazon.com/artifact/getting-started"). This information is not included in this user guide because it contains sensitive security content.
