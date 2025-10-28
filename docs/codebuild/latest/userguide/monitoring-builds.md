# Monitor CodeBuild builds with CloudWatch

You can use Amazon CloudWatch to watch your builds, report when something is wrong, and take
automatic actions when appropriate. You can monitor your builds at two levels:

Project level

These metrics are for all builds in the specified project. To see metrics for
a project, specify `ProjectName` for the dimension in CloudWatch.

AWS account level

These metrics are for all builds in an account. To see metrics at the AWS
account level, do not enter a dimension in CloudWatch. Build resource utilization
metrics are not available at the AWS account level.

CloudWatch metrics show the behavior of your builds over time. For example, you can monitor:

- How many builds were attempted in a build project or an AWS account over time.
- How many builds were successful in a build project or an AWS account over time.
- How many builds failed in a build project or an AWS account over time.
- How much time CodeBuild spent running builds in a build project or an AWS account
  over time.
- Build resource utilization for a build or an entire build project. Build resource
  utilization metrics include metrics such as CPU, memory, and storage
  utilization.
  For more information, see [View CodeBuild metrics](monitoring-metrics.md "monitoring-metrics.md").
