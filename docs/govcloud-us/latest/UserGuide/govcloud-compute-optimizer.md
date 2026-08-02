# AWS Compute Optimizer in AWS GovCloud (US)

AWS Compute Optimizer recommends optimal AWS compute resources for your workloads to reduce costs and improve performance. Compute Optimizer uses machine learning to analyze your historical utilization metrics to help you choose the optimal AWS resource configuration.

## How AWS Compute Optimizer differs

The following differences apply to AWS Compute Optimizer:

- Compute Optimizer only supports FIPS enabled endpoints in AWS GovCloud (US). To call Compute Optimizer APIs in AWS GovCloud (US), set the environment variable `AWS_USE_FIPS_ENDPOINT` to `true` for the AWS CLI and SDK.
- The following AWS Compute Optimizer features are not available:

  - Estimated monthly savings, savings opportunity, Reserved Instances (RI) coverage, and RI utilization information for Amazon Elastic Compute Cloud (Amazon EC2) instances and Amazon EC2 Auto Scaling groups
  - Savings opportunity summary displayed in the Compute Optimizer dashboard
  - External metrics ingestion
  - Enhanced infrastructure metrics
  - Recommendations for Amazon ECS services on AWS Fargate
  - Recommendations for RDS databases
  - Rightsizing recommendation preferences
  - Recommendations for idle resources
  - Recommendations for EC2 Auto Scaling groups that have mixed instance types, scaling policies, or both

- Recommendations for Amazon EC2 instances that use instance families not supported in AWS GovCloud (US). AWS GovCloud (US) supports a smaller set of Amazon EC2 instance families than commercial AWS Regions. Certain newer families — including M7i and M7i-flex (and other recently introduced families such as C7i, M6id, and R6id) — are not supported. If you request a recommendation for an instance whose family is not supported, Compute Optimizer returns an `UNSUPPORTED_CONFIGURATION` error (for example, `Unsupported instance with type m7i.12xlarge`).

## Documentation

- [Compute Optimizer documentation](../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md "../../../compute-optimizer/latest/ug/what-is-compute-optimizer.md")

## Export-controlled content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- No data will leave the AWS GovCloud (US) Regions for this service.
