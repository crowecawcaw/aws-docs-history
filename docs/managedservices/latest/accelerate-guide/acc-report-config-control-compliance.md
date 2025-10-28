# AWS Config Control Compliance report

The AWS Config Control Compliance report provides an in-depth look at resource and AWS Config rule compliance of AMS accounts, You filter the report by Config Rule Severity to prioritize the most critical findings. The following table lists the data provided by this report:

| **Field**               | **Description**                                                      |
| ----------------------- | -------------------------------------------------------------------- |
| Date                    | Report date                                                          |
| Customer name           | Customer name                                                        |
| AWS account ID          | Associated AWS account ID for customer                               |
| Source identifier       | AWS Config rule unique source identifier                             |
| Rule Description        | AWS Config rule description                                          |
| Rule Type               | AWS Config rule type                                                 |
| Compliance Flag         | AWS Config rule compliance state                                     |
| Resource Type           | AWS resource type                                                    |
| Resource Name           | AWS resource name                                                    |
| Severity                | Default recommended severity defined by AMS for the AWS Config rule  |
| Remediation Category    | Associated remediation response category for a AWS Config rule       |
| Remediation Description | Remediation action explained to make AWS Config rule to be compliant |
| Customer action         | Customer action required to make the AWS Config rule to be compliant |
| Delta metrics report    | Changes for compliance of a rule between given 2 dates               |
