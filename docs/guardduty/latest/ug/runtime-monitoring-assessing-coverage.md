# Reviewing runtime coverage statistics and

troubleshooting issues

After you enable Runtime Monitoring and the GuardDuty security agent gets deployed to your resource, GuardDuty
provides coverage statistics for the corresponding resource type and individual coverage status
for the resources that belong to your account. Coverage status is determined by making sure that
you have enabled Runtime Monitoring, your Amazon VPC endpoint has been created, and the GuardDuty security agent for
the corresponding resource has been deployed. A **Healthy** coverage
status indicates that when there is a runtime event related to your resource, GuardDuty is able to
receive the said runtime event through the Amazon VPC endpoint, and monitor the behavior. If there was
an issue at the time of configuring Runtime Monitoring, creating an Amazon VPC endpoint, or deploying the GuardDuty
security agent, the coverage status appears as **Unhealthy**. When
the coverage status is unhealthy, GuardDuty will not be able to receive or monitor the runtime
behavior of the corresponding resource, or generate any Runtime Monitoring findings.

The following topics will help you review coverage statistics, configure EventBridge notifications,
and troubleshoot the coverage issues for a specific resource type.

###### Contents

- [Runtime coverage and troubleshooting for Amazon EC2
  instance](gdu-assess-coverage-ec2.md "gdu-assess-coverage-ec2.md")
- [Runtime coverage and troubleshooting for Amazon ECS
  clusters](gdu-assess-coverage-ecs.md "gdu-assess-coverage-ecs.md")
- [Runtime coverage and troubleshooting for Amazon EKS
  clusters](eks-runtime-monitoring-coverage.md "eks-runtime-monitoring-coverage.md")
