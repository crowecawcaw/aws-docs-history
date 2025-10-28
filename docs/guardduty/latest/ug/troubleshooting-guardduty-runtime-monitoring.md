# Runtime Monitoring issues

This section lists the errors that you may experience when setting up or using Runtime Monitoring.

## Runtime coverage issues

When the runtime coverage of your protected resources become **Unhealthy**,
the GuardDuty console provides the exact issue type. After you have the issue type, use the following documents
to view the troubleshooting steps for each supported resource type:

- [Troubleshooting Amazon EC2
  runtime coverage issues](gdu-assess-coverage-ec2.md#ec2-runtime-monitoring-coverage-issues-troubleshoot "gdu-assess-coverage-ec2.md#ec2-runtime-monitoring-coverage-issues-troubleshoot")
- [Troubleshooting
  Amazon ECS-Fargate runtime coverage issues](gdu-assess-coverage-ecs.md#ecs-runtime-monitoring-coverage-issues-troubleshoot "gdu-assess-coverage-ecs.md#ecs-runtime-monitoring-coverage-issues-troubleshoot")
- [Troubleshooting Amazon EKS
  runtime coverage issues](eks-runtime-monitoring-coverage.md#eks-runtime-monitoring-coverage-issues-troubleshoot "eks-runtime-monitoring-coverage.md#eks-runtime-monitoring-coverage-issues-troubleshoot")

## Troubleshooting out of memory error

in Runtime Monitoring (Amazon EC2 support only)

This section provides the troubleshooting steps when you experience out of memory error
based on the [CPU and memory limit](prereq-runtime-monitoring-ec2-support.md#ec2-cpu-memory-limits-gdu-agent "prereq-runtime-monitoring-ec2-support.md#ec2-cpu-memory-limits-gdu-agent") to deploy the GuardDuty security agent
manually.

If `systemd` terminates the GuardDuty agent because of the
`out-of-memory` issue and you evaluate that providing more memory to the GuardDuty agent
is reasonable, you can update the limit.

1. With the root permission, open
   `/lib/systemd/system/amazon-guardduty-agent.service`.
2. Find `MemoryLimit` and `MemoryMax`, and update both the
   values.

```
MemoryLimit=256M
MemoryMax=256M
```

3. After updating the values, restart the GuardDuty agent by using the following command:

```
sudo systemctl daemon-reload
sudo systemctl restart amazon-guardduty-agent
```

4. Run the following command to view the status:

```
sudo systemctl status amazon-guardduty-agent
```

The expected output will show the new memory limit:

```
Main PID: 2540 (amazon-guardduty)
Tasks: 16
Memory: 21.9M (limit: 256.0M)
```

## My AWS Step Functions workflow is failing

unexpectedly

If the GuardDuty container contributed to the workflow failure, see [Troubleshooting
Amazon ECS-Fargate runtime coverage issues](gdu-assess-coverage-ecs.md#ecs-runtime-monitoring-coverage-issues-troubleshoot "gdu-assess-coverage-ecs.md#ecs-runtime-monitoring-coverage-issues-troubleshoot"). If the issue persists,
then to prevent the workflow failure because of the GuardDuty container, perform **one** of the following steps:

- Add the `GuardDutyManaged`:`false` tag to associated Amazon ECS
  cluster.
- Disable the automated agent configuration for AWS Fargate (ECS only) at the account
  level. Add the inclusion tag `GuardDutyManaged`:`true` to the associated
  Amazon ECS cluster that you want to continue monitoring with the GuardDuty automated agent.
