# Amazon ECS service unhealthy event messages

The following are examples of service unhealthy event messages.

## EC2: (service `service-name`) (task `task-id`) (instance `instance-id`) (port `port-number`) is unhealthy in (target-group `target-group-name`) due to (reason `failure-reason`)

This message indicates that a task running on an EC2 instance is failing health
checks. For more information, see the following:

- [How do I get my Amazon ECS tasks that use EC2 to pass the Application Load Balancer health check?](https://repost.aws/knowledge-center/troubleshoot-unhealthy-checks-ecs "https://repost.aws/knowledge-center/troubleshoot-unhealthy-checks-ecs")

## EC2 with taskSet: (service `service-name`, taskSet `taskSet-id`) (task `task-id`) (instance `instance-id`) (port `port-number`) is unhealthy in (target-group `target-group-name`) due to (reason `failure-reason`)

This message indicates that a task in a task set running on an EC2 instance is failing health checks. For more information, see the following:

- [How do I get my Amazon ECS tasks that use the EC2 to pass the Application Load Balancer health check?](https://repost.aws/knowledge-center/troubleshoot-unhealthy-checks-ecs "https://repost.aws/knowledge-center/troubleshoot-unhealthy-checks-ecs")

## Fargate: (service `service-name`) (task `task-id`) (port `port-number`) is unhealthy in (target-group `target-group-name`) due to (reason `failure-reason`)

This message indicates that a Fargate task is failing health checks.

For more information about troubleshooting health check failures in Fargate tasks, see [How do I troubleshoot health check failures for Amazon ECS tasks on Fargate?](https://repost.aws/knowledge-center/ecs-fargate-health-check-failures "https://repost.aws/knowledge-center/ecs-fargate-health-check-failures").

## Fargate with taskSet: (service `service-name`, taskSet `taskSet-id`) (task `task-id`) (port `port-number`) is unhealthy in (target-group `target-group-name`) due to (reason `failure-reason`)

This message indicates that a task in a task set running on Fargate is failing health checks.

For more information about troubleshooting health check failures in Fargate tasks, see [How do I troubleshoot health check failures for Amazon ECS tasks on Fargate?](https://repost.aws/knowledge-center/ecs-fargate-health-check-failures "https://repost.aws/knowledge-center/ecs-fargate-health-check-failures").
