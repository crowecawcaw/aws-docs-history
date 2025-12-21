# Metrics analyzed by AWS Compute Optimizer

After you [opt in](getting-started.md "getting-started.md"), AWS Compute Optimizer analyzes the
specifications, such as vCPUs, memory, or storage, and the Amazon CloudWatch metrics of your running
resources from a period over the last 14 days. If you activate the [enhanced infrastructure metrics recommendation
preference](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md"), AWS Compute Optimizer analyzes your resources for up to 93 days.

The analysis can take up to 24 hours to complete. When the analysis is complete, the
findings are displayed on the dashboard page of the Compute Optimizer console. For more
information, see [Using the AWS Compute Optimizer dashboard](viewing-dashboard.md "viewing-dashboard.md").

###### Note

- To generate recommendations for
  Amazon EC2 instances, EC2 Auto Scaling groups, Amazon EBS volumes, Lambda functions, and commercial software licenses, Compute Optimizer uses
  the maximum utilization point within each five-minute time interval over the lookback period. For ECS
  services on Fargate recommendations, Compute Optimizer uses the maximum utilization point within each
  one-minute time interval.
- AWS might use your utilization data to help improve the overall quality of Compute Optimizer's
  recommendations. To stop AWS using your utilization data, contact [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support").

###### Contents

- [EC2 instance metrics](ec2-metrics-analyzed.md "ec2-metrics-analyzed.md")
- [EBS volume metrics](ebs-metrics-analyzed.md "ebs-metrics-analyzed.md")
- [Lambda function metrics](lambda-metrics-analyzed.md "lambda-metrics-analyzed.md")
- [Metrics for Amazon ECS services on Fargate](ecs-fargate-metrics-analyzed.md "ecs-fargate-metrics-analyzed.md")
- [Metrics for commercial software licenses](license-metrics-analyzed.md "license-metrics-analyzed.md")
- [Aurora and RDS database metrics](rds-metrics-analyzed.md "rds-metrics-analyzed.md")
