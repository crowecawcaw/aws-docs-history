# AWS Fargate Linux platform version deprecation

###### Important

On March 2, 2026, AWS will start force-updating all the Amazon ECS services running Fargate platform version 1.3.0 that are not migrated to the platform version 1.4.0. That may potentially impact your workloads. Starting March 16, 2026, we will make the platform version 1.3.0 as Retired. At that time, you will not be able to launch new tasks or create new services configured with platform version 1.3.0, but your existing tasks will continue running. On March 31, 2026, we will terminate all the remaining running tasks configured with platform version 1.3.0.

For information about how to migrate to platform version 1.4, see [Migrating to Linux platform version 1.4.0 on Amazon ECS](platform-version-migration.md "platform-version-migration.md").

The following table lists Linux platform versions that AWS Fargate has deprecated or have been scheduled for deprecation. These platform versions remain available until the published deprecation date.

A _force update date_ is provided for each platform version scheduled for deprecation.
On the force update date, any service using the `LATEST` platform version
that is pointed to a platform version that is scheduled for deprecation will be updated using the force new
deployment option. When the service is updated using the force new deployment option, all tasks running on a
platform version scheduled for deprecation are stopped and new tasks are launched using the platform version
that the `LATEST` tag points to at that time. Standalone tasks or services with an explicit platform version set are
not affected by the force update date.

For information about how to migrate to latest platform version, see [Migrating to Linux platform version 1.4.0 on Amazon ECS](platform-version-migration.md "platform-version-migration.md").

After a platform version reaches the _deprecation date_, the
platform version will no longer be available for new tasks or services. Any standalone
tasks or services which explicitly use a deprecated platform version will continue using
that platform version until the tasks are stopped. After the deprecation date, a
deprecated platform version will no longer receive any security updates or bug
fixes.

| Platform version | Force update date | Deprecation date  |
| ---------------- | ----------------- | ----------------- |
| 1.0.0            | October 26, 2020  | December 14, 2020 |
| 1.1.0            | October 26, 2020  | December 14, 2020 |
| 1.2.0            | October 26, 2020  | December 14, 2020 |
| 1.3.0            | March 2, 2026     | March 16, 2026    |

For information about current platform versions, see [Fargate platform versions for Amazon ECS](platform-fargate.md "platform-fargate.md").

## Deprecated Fargate Linux versions change log

### 1.3.0

The following is the changelog for platform version `1.3.0`.

- Beginning on Sept 30, 2019, any new Fargate task that is
  launched supports the `awsfirelens` log driver. Configure the
  FireLens for Amazon ECS to use task definition parameters to route logs to an
  AWS service or AWS Partner Network (APN) destination for log storage and
  analytics. For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").
- Added task recycling for Fargate tasks, which is the process
  of refreshing tasks that are a part of an Amazon ECS service. For more
  information, [Task
  retirement and maintenance for AWS Fargate on Amazon ECS](task-maintenance.md "task-maintenance.md").
- Beginning on March 27, 2019, any new Fargate task that is
  launched can use additional task definition parameters that you use to
  define a proxy configuration, dependencies for container startup and
  shutdown as well as a per-container start and stop timeout value. For more
  information, see [Proxy configuration](task_definition_parameters.md#proxyConfiguration "task_definition_parameters.md#proxyConfiguration"), [Container dependency](task_definition_parameters.md#container_definition_dependson "task_definition_parameters.md#container_definition_dependson"), and [Container timeouts](task_definition_parameters.md#container_definition_timeout "task_definition_parameters.md#container_definition_timeout").
- Beginning on April 2, 2019, any new Fargate task that is
  launched supports injecting sensitive data into your containers by storing
  your sensitive data in either AWS Secrets Manager secrets or AWS Systems Manager Parameter Store
  parameters and then referencing them in your container definition. For more
  information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").
- Beginning on May 1, 2019, any new Fargate task that is
  launched supports referencing sensitive data in the log configuration of a
  container using the `secretOptions` container definition
  parameter. For more information, see [Pass sensitive data to an Amazon ECS container](specifying-sensitive-data.md "specifying-sensitive-data.md").
- Beginning on May 1, 2019, any new Fargate task that is
  launched supports the `splunk` log driver in addition to the
  `awslogs` log driver. For more information, see [Storage and logging](task_definition_parameters.md#container_definition_storage "task_definition_parameters.md#container_definition_storage").
- Beginning on July 9, 2019, any new Fargate tasks that is
  launched supports CloudWatch Container Insights. For more information, see [Monitor Amazon ECS containers using Container Insights with enhanced observability](cloudwatch-container-insights.md "cloudwatch-container-insights.md").
- Beginning on December 3, 2019, the Fargate Spot capacity provider is
  supported. For more information, see [Amazon ECS clusters for Fargate](fargate-capacity-providers.md "fargate-capacity-providers.md").
- Based on Amazon Linux 2.

### 1.2.0

The following is the changelog for platform version `1.2.0`.

###### Note

Platform version `1.2.0` is no longer available. For information about platform version
deprecation, see [AWS Fargate Linux platform version deprecation](platform-versions-retired.md "platform-versions-retired.md").

- Added support for private registry authentication using AWS Secrets Manager. For
  more information, see [Using non-AWS container images in Amazon ECS](private-auth.md "private-auth.md").

### 1.1.0

The following is the changelog for platform version `1.1.0`.

###### Note

Platform version `1.1.0` is no longer available. For information about platform version
deprecation, see [AWS Fargate Linux platform version deprecation](platform-versions-retired.md "platform-versions-retired.md").

- Added support for the Amazon ECS task metadata endpoint. For more information,
  see [Amazon ECS task metadata available for tasks on Fargate](fargate-metadata.md "fargate-metadata.md").
- Added support for Docker health checks in container definitions. For more
  information, see [Health check](task_definition_parameters.md#container_definition_healthcheck "task_definition_parameters.md#container_definition_healthcheck").
- Added support for Amazon ECS service discovery. For more information, see [Use service discovery to connect Amazon ECS services with DNS names](service-discovery.md "service-discovery.md").

### 1.0.0

The following is the changelog for platform version `1.0.0`.

###### Note

Platform version `1.0.0` is no longer available. For information about platform version
deprecation, see [AWS Fargate Linux platform version deprecation](platform-versions-retired.md "platform-versions-retired.md").

- Based on Amazon Linux 2017.09.
- Initial release.
