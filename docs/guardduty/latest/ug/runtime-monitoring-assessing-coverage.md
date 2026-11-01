

# Reviewing runtime coverage statistics and troubleshooting issues
<a name="runtime-monitoring-assessing-coverage"></a>

After you enable Runtime Monitoring and the GuardDuty security agent is deployed to your resource, GuardDuty provides coverage statistics per resource type (EKS clusters, EC2 instances, ECS clusters) and a coverage status for each resource in your account. GuardDuty determines coverage status by checking that you have enabled Runtime Monitoring, that you have deployed the security agent, and that the security agent can connect to GuardDuty. A **Healthy** coverage status indicates that GuardDuty is able to receive runtime events from the monitored resource. An **Unhealthy** status indicates an issue with configuring Runtime Monitoring, deploying the security agent, or the security agent connecting to GuardDuty. When the coverage status is unhealthy, GuardDuty can't receive or monitor the runtime behavior of the resource, or generate Runtime Monitoring findings.

The following topics will help you review coverage statistics, configure EventBridge notifications, and troubleshoot the coverage issues for a specific resource type.

**Topics**
+ [Runtime coverage and troubleshooting for Amazon EC2 instance](gdu-assess-coverage-ec2.md)
+ [Runtime coverage and troubleshooting for ECS-EC2 Bottlerocket](gdu-assess-coverage-bottlerocket-ecs-ec2.md)
+ [Runtime coverage and troubleshooting for Amazon ECS clusters](gdu-assess-coverage-ecs.md)
+ [Runtime coverage and troubleshooting for Amazon EKS clusters](eks-runtime-monitoring-coverage.md)
+ [Troubleshooting agent connectivity](runtime-monitoring-agent-connectivity-troubleshooting.md)