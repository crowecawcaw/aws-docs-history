# Amazon ECS Service Connect configuration

overview

When you use Service Connect, there are parameters you need to configure in your
resources.

The following table describes the configuration parameters for the Amazon ECS resources.

| Parameter location | App type      | Description                                                                                                                                                                                                                                                                                                                                                                                             | Required |
| ------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Task definition    | Client        | There are no changes available for Service Connect in client task<br>definitions.                                                                                                                                                                                                                                                                                                                       | N/A      |
| Task definition    | Client-server | Servers must add `name` fields to ports in the<br>`portMappings` of containers. For more information, see [portMappings](task_definition_parameters.md#ContainerDefinition-portMappings "task_definition_parameters.md#ContainerDefinition-portMappings")                                                                                                                                               | Yes      |
| Task definition    | Client-server | Servers can optionally provide an application protocol (for example,<br>HTTP) to receive protocol-specific metrics for their server applications<br>(for example, `HTTP 5xx`).                                                                                                                                                                                                                          | No       |
| Service definition | Client        | Client services must add a `serviceConnectConfiguration` to<br>configure the namespace to join. This namespace must contain all of the<br>server services that this service needs to discover. For more information,<br>see [serviceConnectConfiguration](service_definition_parameters.md#Service-serviceConnectConfiguration "service_definition_parameters.md#Service-serviceConnectConfiguration"). | Yes      |
| Service definition | Client-server | Server services must add a `serviceConnectConfiguration` to<br>configure the DNS names, port numbers, and namespace that the service is<br>available from. For more information, see [serviceConnectConfiguration](service_definition_parameters.md#Service-serviceConnectConfiguration "service_definition_parameters.md#Service-serviceConnectConfiguration").                                        | Yes      |
| Cluster            | Client        | Clusters can add a default Service Connect namespace. New services in<br>the cluster inherit the namespace when Service Connect is configured in a<br>service.                                                                                                                                                                                                                                          | No       |
| Cluster            | Client-server | There are no changes available for Service Connect in clusters that<br>apply to server services. Server task definitions and services must set the<br>respective configuration.                                                                                                                                                                                                                         | N/A      |

###### Overview of steps to configure Service Connect

The following steps provide an overview of how to configure Service Connect.

###### Important

- Service Connect creates AWS Cloud Map services in your account. Modifying these
  AWS Cloud Map resources by manually registering/deregistering instances, changing
  instance attributes, or deleting a service may lead to unexpected behavior for
  your application traffic or subsequent deployments.
- Service Connect doesn't support links in the task definition.

1. Add port names to the port mappings in your task definitions. Additionally, you
   can identify the layer 7 protocol of the application, to get additional
   metrics.
2. Create a cluster with a AWS Cloud Map namespace, use a shared namespace, or create the namespace separately.
   For simple organization, create a cluster with the name that you want for the
   namespace and specify the identical name for the namespace. In this case, Amazon ECS
   creates a new HTTP namespace with the necessary configuration. Service Connect
   doesn't use or create DNS hosted zones in Amazon Route 53.
3. Configure services to create Service Connect endpoints within the
   namespace.
4. Deploy services to create the endpoints. Amazon ECS adds a Service Connect proxy
   container to each task, and creates the Service Connect endpoints in AWS Cloud Map.
   This container isn't configured in the task definition, and the task definition can
   be reused without modification to create multiple services in the same namespace or
   in multiple namespaces.
5. Deploy client apps as services to connect to the endpoints. Amazon ECS connects them to
   the Service Connect endpoints through the Service Connect proxy in each
   task.

Applications only use the proxy to connect to Service Connect endpoints. There is
no additional configuration to use the proxy. The proxy performs round-robin load
balancing, outlier detection, and retries. For more information about the proxy, see
[Service Connect proxy](service-connect-concepts-deploy.md#service-connect-concepts-proxy "service-connect-concepts-deploy.md#service-connect-concepts-proxy"). 6. Monitor traffic through the Service Connect proxy in Amazon CloudWatch.

## Cluster

configuration

You can set a default namespace for Service Connect when you create or update the
cluster. The namespace name that you specify as a default can either be in the same AWS Region and
account, or in the same AWS Region and shared by another AWS account using AWS Resource Access Manager.

If you create a cluster and specify a default Service Connect namespace, the cluster
waits in the `PROVISIONING` status while Amazon ECS creates the namespace. You can
see an `attachment` in the status of the cluster that shows the status of the
namespace. Attachments aren't displayed by default in the AWS CLI, you must add
`--include ATTACHMENTS` to see them.

If you want to use a namespace that is shared with your AWS account using AWS RAM,
specify the Amazon Resource Name (ARN) of the namespace in the cluster configuration. For more
information about shared AWS Cloud Map namespaces, see [Amazon ECS Service Connect with shared
AWS Cloud Map namespaces](service-connect-shared-namespaces.md "service-connect-shared-namespaces.md").

## Service configuration

Service Connect is designed to require the minimum configuration. You need to set a
name for each port mapping that you would like to use with Service Connect in the task
definition. In the service, you need to turn on Service Connect and select either a namespace
in your AWS account or a shared namespace to make a client service. To make a client-server service, you need to add a single
Service Connect service configuration that matches the name of one of the port
mappings. Amazon ECS reuses the port number and port name from the task definition to define
the Service Connect service and endpoint. To override those values, you can use the
other parameters **Discovery**, **DNS**, and
**Port** in the console, or `discoveryName` and
`clientAliases`, respectively in the Amazon ECS API.

## Initial Health Check configuration

Service Connect ensures tasks are healthy before routing traffic to them. When a task launches (during deployments, scaling, or replacements), Service Connect monitors the health of your task to ensure it is ready to accept traffic. You must define health checks for the essential container in your task definition to enable this behavior.

The behavior of the initial health check accounts for potential delays with reaching the state when a task is ready to accept traffic:

- If a task is `HEALTHY`, it's immediately available for traffic.
- If a task's health is `UNKNOWN`, Service Connect follows the container health check configuration (see [Health check](task_definition_parameters.md#container_definition_healthcheck "task_definition_parameters.md#container_definition_healthcheck")) of the task's essential containers to calculate a timeout, up to `8 minutes`, before making it available to traffic, even if it remains `UNKNOWN`.
- If a task is `UNHEALTHY`, Service Connect delays traffic routing for up to `8 minutes`. During this time, Amazon ECS may launch replacement tasks. If no healthy tasks are available, your deployment might be rolled back based on your service's configuration.

For all ongoing traffic, Service Connect uses passive health checks based on outlier detection to route traffic efficiently.
