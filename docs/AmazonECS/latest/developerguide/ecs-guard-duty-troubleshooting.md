# Runtime Monitoring Troubleshooting

You might need to troubleshoot or verify that Runtime Monitoring is enabled and running on your
tasks and containers.

###### Topics

- [How can I tell if Runtime Monitoring is active on my account?](#verify-ecs-runtime-enabled "#verify-ecs-runtime-enabled")
- [How can I tell if Runtime Monitoring is active on a cluster?](#verify-ecs-runtime-enabled "#verify-ecs-runtime-enabled")
- [How can I tell if the GuardDuty security agent is running on a Fargate task?](#verify-ecs-runtime-fargate-run "#verify-ecs-runtime-fargate-run")
- [How can I tell if the GuardDuty security agent is running on an EC2 container instance?](#verify-ecs-runtime-ec2-run "#verify-ecs-runtime-ec2-run")
- [What happens when there is no task execution role for a task running on the cluster?](#no-task-execution-role "#no-task-execution-role")
- [How can I tell if I have the correct permissions to tag clusters for Runtime Monitoring?](#tag-permissions "#tag-permissions")
- [What happens when there is no connection Amazon ECR?](#no-ecr-connection "#no-ecr-connection")
- [How do I address out of memory errors on my Fargate tasks after enabling Runtime Monitoring?](#memory-error "#memory-error")

## How can I tell if Runtime Monitoring is active on my account?

In the Amazon ECS console, the information is in on the **Account
Settings** page.

You can also run `list-account-settings` with the
`effective-settings` option.

```
aws ecs list-account-settings --effective-settings
```

Output

The setting with **name** set to `guardDutyActivate` and
**value** set to `on` indicates that the account is
configured. You must check with your GuardDuty administrator to see if the management is
automatic or manual.

```
{
    "setting": {
        **"name": "guardDutyActivate",
 "value": "enabled",**
        "principalArn": "arn:aws:iam::123456789012:root",
        "type": "aws-managed"
    }
}
```

## How can I tell if Runtime Monitoring is active on a cluster?

You can review the coverage statistics in the GuardDuty console. This includes information
for the Amazon ECS resources associated with your own account or your member accounts is the
percentage of the healthy clusters over all the clusters in the selected AWS Region.
This includes the coverage for clusters that use the Fargate and EC2s. For
more information, see [Reviewing coverage statistics](../../../guardduty/latest/ug/gdu-assess-coverage-ecs.md#ecs-review-coverage-statistics-ecs-runtime-monitoring "../../../guardduty/latest/ug/gdu-assess-coverage-ecs.md#ecs-review-coverage-statistics-ecs-runtime-monitoring") in the _Amazon GuardDuty User
Guide_.

## How can I tell if the GuardDuty security agent is running on a Fargate task?

The GuardDuty security agent runs as a sidecar container for Fargate tasks.

In the Amazon ECS console, the sidecar is displayed under **Containers**
on the **Task details** page.

You can run `describe-tasks` and look for the container with a
**name** set to `aws-gd-agent` and the
**lastStatus** set to `RUNNING`.

The following example shows the output for the default cluster for task
`aws:ecs:us-east-1:123456789012:task/0b69d5c0-d655-4695-98cd-5d2d5EXAMPLE`.

```
aws ecs describe-tasks --cluster default --tasks aws:ecs:us-east-1:123456789012:task/0b69d5c0-d655-4695-98cd-5d2d5EXAMPLE
```

Output

The container named `gd-agent` is in the `RUNNING` state.

```
"containers": [
      {
        "containerArn": "arn:aws:ecs:us-east-1:123456789012:container/4df26bb4-f057-467b-a079-96167EXAMPLE",
        "taskArn": "arn:aws:ecs:us-east-1:123456789012:task/0b69d5c0-d655-4695-98cd-5d2d5EXAMPLE",
        "lastStatus": "**RUNNING**",
        "healthStatus": "UNKNOWN",
        "memory": "string",
        "name": "**aws-gd-agent**"
      }
    ]
```

## How can I tell if the GuardDuty security agent is running on an EC2 container instance?

Run the following command to view the status:

```
sudo systemctl status amazon-guardduty-agent
```

The log file is in the following location:

```
/var/log/amzn-guardduty-agent
```

## What happens when there is no task execution role for a task running on the cluster?

For Fargate tasks, the task starts without the GuardDuty security agent sidecar
container. The GuardDuty dashboard will show that the task is missing protection in the
coverage statistics dashboard.

## How can I tell if I have the correct permissions to tag clusters for Runtime Monitoring?

In order to tag a cluster, you must have the `ecs:TagResource` action for
both `CreateCluster` and `UpdateCluster`.

The following is a snippet of an example policy.

```
{
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
         "ecs:TagResource"
      ],
      "Resource": "*",
      "Condition": {
         "StringEquals": {
             "ecs:CreateAction" : "CreateCluster",
             "ecs:CreateAction" : "UpdateCluster",
          }
       }
    }
  ]
}
```

## What happens when there is no connection Amazon ECR?

For Fargate tasks, the task starts without the GuardDuty security agent sidecar
container. The GuardDuty dashboard will show that the task is missing protection in the
coverage statistics dashboard.

## How do I address out of memory errors on my Fargate tasks after enabling Runtime Monitoring?

The GuardDuty security agent is a lightweight process. However, the process still
consumes resources according to the size of the workload. We recommend using container
resource tracking tooling, such as Amazon CloudWatch Container Insights to stage GuardDuty
deployments in your cluster. These tools help you to discover the consumption profile of
the GuardDuty security agent for your applications. You can then adjust your Fargate task
size, if required, to avoid potential out of memory conditions.
