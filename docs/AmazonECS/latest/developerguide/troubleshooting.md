# Amazon ECS troubleshooting

You might need to troubleshoot issues with your load balancers, tasks, services, or
container instances. This chapter helps you find diagnostic information from the Amazon ECS
container agent, the Docker daemon on the container instance, and the service event log in
the Amazon ECS console.

For information about stopped tasks, see one of the following.

| Action                                  | Learn more                                                                                             |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Resolve stopped task errors.            | [Viewing Amazon ECS stopped task errors](stopped-task-errors.md "stopped-task-errors.md")              |
| View stopped task errors.               | [Resolve Amazon ECS stopped task errors](resolve-stopped-errors.md "resolve-stopped-errors.md")        |
| Review stopped task error codes.        | [Amazon ECS stopped tasks error messages](stopped-task-error-codes.md "stopped-task-error-codes.md")   |
| Review CannotPullContainer task errors. | [CannotPullContainer task errors in Amazon ECS](task_cannot_pull_image.md "task_cannot_pull_image.md") |
| View task IAM role requests.            | [Viewing IAM role requests for Amazon ECS tasks](task_iam_roles-logs.md "task_iam_roles-logs.md")      |
| Troubleshoot using task events.         | [Amazon ECS event capture in the console](task-lifecycle-events.md "task-lifecycle-events.md")         |

For information about service errors, see one of the following.

| Action                              | Learn more                                                                                                                                 |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| View service event messages.        | [Viewing Amazon ECS service event messages](service-event-messages.md "service-event-messages.md")                                         |
| Review service event messages.      | [Amazon ECS service event messages](service-event-messages-list.md "service-event-messages-list.md")                                       |
| Review load balancer issues.        | [Troubleshooting service load<br>balancers in Amazon ECS](troubleshoot-service-load-balancers.md "troubleshoot-service-load-balancers.md") |
| Review service auto scaling issues. | [Troubleshooting service auto<br>scaling in Amazon ECS](troubleshoot-service-auto-scaling.md "troubleshoot-service-auto-scaling.md")       |

For information about task definition errors, see one of the following.

| Action                                | Learn more                                                                                                                  |
| ------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Resolve task definition memory error. | [Troubleshoot Amazon ECS task definition invalid CPU or memory errors](task-cpu-memory-error.md "task-cpu-memory-error.md") |

For information about Amazon ECS agent errors, see one of the following.

| Action                                                 | Learn more                                                                                                          |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| View Amazon ECS container agent logs.                  | [Viewing Amazon ECS container agent logs](logs.md "logs.md")                                                        |
| Learn how to collect Amazon ECS logs.                  | [Collecting container logs with Amazon ECS logs collector](ecs-logs-collector.md "ecs-logs-collector.md")           |
| Retrieve diagnostic details with the Amazon ECS agent. | [Retrieve Amazon ECS diagnostic details with agent<br>introspection](introspection-diag.md "introspection-diag.md") |

For information about Docker errors, see one of the following.

| Action                             | Learn more                                                                                                                           |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Use Docker diagnostics.            | [Docker diagnostics in Amazon ECS](docker-diags.md "docker-diags.md")                                                                |
| Turn on Docker debug mode.         | [Configuring verbose output from the Docker daemon in Amazon ECS](docker-debug-mode.md "docker-debug-mode.md")                       |
| Troubleshoot Docker API error 500. | [Troubleshoot the Docker API error (500):<br>devmapper in Amazon ECS](CannotCreateContainerError.md "CannotCreateContainerError.md") |

For information about ECS Exec and Amazon ECS Anywhere errors, see one of the following.

| Action                            | Learn more                                                                                                      |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| Troubleshoot ECS Exec.            | [Troubleshoot Amazon ECS Exec issues](ecs-exec-troubleshooting.md "ecs-exec-troubleshooting.md")                |
| Troubleshoot Amazon ECS Anywhere. | [Troubleshoot Amazon ECS Anywhere<br>issues](ecs-anywhere-troubleshooting.md "ecs-anywhere-troubleshooting.md") |

For information about issues with attaching Amazon EBS volumes to Amazon ECS tasks, see the following:

| Action                                                                | Learn more                                                                                                                                           |
| --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Troubleshooting Amazon EBS volume attachments to Amazon ECS tasks.    | [Troubleshooting Amazon EBS volume attachments to Amazon ECS<br>tasks](troubleshoot-ebs-volumes.md "troubleshoot-ebs-volumes.md")                    |
| Status reasons for Amazon EBS volume attachments to Amazon ECS tasks. | [Status reasons for Amazon EBS volume attachment to Amazon ECS tasks](troubleshoot-ebs-volumes-scenarios.md "troubleshoot-ebs-volumes-scenarios.md") |

For information about issues with using shared AWS Cloud Map namespaces with Amazon ECS Service Connect, see one of the following:

| Action                                                                           | Learn more                                                                                                                                                                                        |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Troubleshooting Amazon ECS Service Connect with shared AWS Cloud Map namespaces. | [Troubleshooting<br>Amazon ECS Service Connect with shared AWS Cloud Map namespaces](service-connect-shared-namespaces-troubleshooting.md "service-connect-shared-namespaces-troubleshooting.md") |

For information about throttling issues, see one of the following.

| Action                                              | Learn more                                                                                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Learn about Fargate throttling quotas.              | [AWS Fargate throttling quotas](throttling.md "throttling.md")                                                                        |
| Learn the best practices for Amazon ECS throttling. | [Handle Amazon ECS throttling<br>issues](operating-at-scale-dealing-with-throttles.md "operating-at-scale-dealing-with-throttles.md") |

For information about API errors, see one of the following.

| Action              | Learn more                                                                            |
| ------------------- | ------------------------------------------------------------------------------------- |
| Resolve API errors. | [Amazon ECS API failure reasons](api_failures_messages.md "api_failures_messages.md") |

For information about AI-powered troubleshooting, see the following:

| Action                                                           | Learn more                                                                                       |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Troubleshoot with Amazon Q Developer in the console.             | [Troubleshooting with Amazon Q Developer](troubleshooting-with-Q.md "troubleshooting-with-Q.md") |
| Troubleshoot with AI assistants using the Amazon ECS MCP server. | [Amazon ECS MCP server](ecs-mcp-introduction.md "ecs-mcp-introduction.md")                       |
