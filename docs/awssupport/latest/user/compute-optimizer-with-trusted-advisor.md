# Opt in AWS Compute Optimizer for Trusted Advisor

checks

Compute Optimizer is a service that analyzes the configuration and utilization metrics of your AWS
resources. This service reports
whether
your resources are correctly configured for efficiency and reliability.
It also suggests improvements you can implement to improve workload performance. With Compute Optimizer,
you view the same recommendations in your Trusted Advisor checks.

You can opt in either your AWS account only, or all member accounts that are part of an
organization in AWS Organizations. For more information, see [Getting started](../../../compute-optimizer/latest/ug/getting-started.md#account-opt-in "../../../compute-optimizer/latest/ug/getting-started.md#account-opt-in") in the
_AWS Compute Optimizer User Guide_.

Once you opt in for Compute Optimizer, the following checks receive data from your Lambda functions and
Amazon EBS volumes. It can take up to 12 hours to generate the findings and optimization
recommendations. It can then take up to 48 hours to view your results in Trusted Advisor for the
following checks:

[Cost optimization](cost-optimization-checks.md "cost-optimization-checks.md")

- Amazon EBS over-provisioned volumes
- AWS Lambda over-provisioned functions for memory size
  [Performance](performance-checks.md "performance-checks.md")

- Amazon EBS under-provisioned volumes
- AWS Lambda under-provisioned functions for memory size

###### Notes

- Results for these checks are automatically refreshed several times daily.
  Refresh requests are not allowed. It might take a few hours for changes to
  appear. Currently, you can’t exclude resources from these checks.
- Trusted Advisor already has the Underutilized Amazon EBS Volumes and the Overutilized
  Amazon EBS Magnetic Volumes checks.

Once you opt in with Compute Optimizer, we recommend that you use the new Amazon EBS
over-provisioned volumes and Amazon EBS under-provisioned volumes checks
instead.

## Related information

For more information, see the following topics:

- [Viewing Amazon EBS volume recommendations](../../../compute-optimizer/latest/ug/view-ebs-recommendations.md "../../../compute-optimizer/latest/ug/view-ebs-recommendations.md") in the
  _AWS Compute Optimizer User Guide_
- [Viewing Lambda function recommendations](../../../compute-optimizer/latest/ug/view-lambda-recommendations.md "../../../compute-optimizer/latest/ug/view-lambda-recommendations.md") in the
  _AWS Compute Optimizer User Guide_
- [Configuring Lambda function memory](../../../lambda/latest/dg/configuration-function-common.md#configuration-memory-console "../../../lambda/latest/dg/configuration-function-common.md#configuration-memory-console") in the
  _AWS Lambda Developer Guide_
- [Request modifications to your Amazon EBS volumes](../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md "../../../AWSEC2/latest/UserGuide/requesting-ebs-volume-modifications.md") in
  the _Amazon EC2 User Guide_
