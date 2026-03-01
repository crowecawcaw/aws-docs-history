# App Mesh scaling troubleshooting

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

This topic details common issues that you may experience with App Mesh scaling.

## Connectivity fails and container health checks fail when scaling beyond 50 replicas for a virtual node/virtual gateway

###### Symptoms

When you are scaling the number of replicas, such as Amazon ECS tasks, Kubernetes pods, or Amazon EC2
instances, for a virtual node/virtual gateway beyond 50, Envoy container health checks for new
and currently running Envoys begin to fail. Downstream applications sending traffic to the
virtual node/virtual gateway begin seeing request failures with HTTP status code
`503`.

###### Resolution

App Mesh's default quota for the number of Envoys per virtual node/virtual gateway is 50. When
the number of running Envoys exceeds this quota, new and currently running Envoys fail to
connect to App Mesh's Envoy management service with gRPC status code `8`
(`RESOURCE_EXHAUSTED`). This quota can be raised. For more information, see
[App Mesh service quotas](service-quotas.md "service-quotas.md").

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Requests fail with `503` when a virtual service backend horizontally scales out or in

###### Symptoms

When a backend virtual service is horizontally scaled out or in, requests from downstream
applications fail with an `HTTP 503` status code.

###### Resolution

App Mesh recommends several approaches to mitigate failure cases while scaling applications
horizontally. For detailed information about how to prevent these failures, see [App Mesh best practices](best-practices.md "best-practices.md").

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Envoy container crashes with segfault under increased load

###### Symptoms

Under a high traffic load, the Envoy proxy crashes due to a segmentation fault (Linux exit
code `139`). The Envoy process logs contain a statement like the following.

```
Caught Segmentation fault, suspect faulting address 0x0"
```

###### Resolution

The Envoy proxy has likely breached the operating system's default nofile ulimit, the limit
on the number of files a process can have open at a time. This breach is due to the traffic
causing more connections, which consume additional operating system sockets. To resolve this
issue, increase the ulimit nofile value on the host operating system. If you are using Amazon ECS,
this limit can be changed through the [Ulimit settings](../../../AmazonECS/latest/APIReference/API_Ulimit.md "../../../AmazonECS/latest/APIReference/API_Ulimit.md") on the task
definition's [resource limits settings](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_limits "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_limits").

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Increase in default resources is not reflected in Service Limits

###### Symptoms

After increasing the default limit of App Mesh resources, the new value is not reflected when
you look at your service limits.

###### Resolution

While the new limits aren't currently shown, customers can still exercise them.

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Application crashes due to a huge number of health checks calls.

###### Symptoms

After enabling active health checks for a virtual node, there is an uptick in the number of
health check calls. The application crashes due to the greatly increased volume of health check
calls made to the application.

###### Resolution

When active health checking is enabled, each Envoy endpoint of the downstream (client) sends
health requests to each endpoint of the upstream cluster (server) in order to make routing
decisions. As a result the total number of health check requests would be `number of
 client Envoys` \* `number of server Envoys` \* `active health check
 frequency`.

To resolve this issue, modify the frequency of the health check probe, which would reduce the
total volume of health check probes. In addition to active health checks, App Mesh allows configuring
[outlier detection](../APIReference/API_OutlierDetection.md "../APIReference/API_OutlierDetection.md") as means of passive health checking. Use outlier detection to
configure when to remove a particular host based on consecutive `5xx` responses.

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
