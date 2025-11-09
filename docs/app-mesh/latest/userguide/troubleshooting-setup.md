# App Mesh setup troubleshooting

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

This topic details common issues that you may experience with App Mesh setup.

## Cannot pull Envoy container image

###### Symptoms

You receive the following error message in an Amazon ECS task. The Amazon ECR `account
 ID` and `Region` in the following message may be
different, depending on which Amazon ECR repository that you pulled the container image from.

```
CannotPullContainerError: Error response from daemon: pull access denied for `840364872350`.dkr.ecr.`us-west-2`.amazonaws.com/aws-appmesh-envoy, repository does not exist or may require 'docker login'
```

###### Resolution

This error indicates that the task execution role being used does not have permission to
communicate to Amazon ECR and cannot pull the Envoy container image from the repository. The task
execution role assigned to your Amazon ECS task needs an IAM policy with the following
statements:

```
{
  "Action": [
    "ecr:BatchCheckLayerAvailability",
    "ecr:GetDownloadUrlForLayer",
    "ecr:BatchGetImage"
  ],
  "Resource": "arn:aws:ecr:`us-west-2`:`111122223333`:repository/aws-appmesh-envoy",
  "Effect": "Allow"
},
{
  "Action": "ecr:GetAuthorizationToken",
  "Resource": "*",
  "Effect": "Allow"
}
```

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Cannot connect to App Mesh Envoy management

service

###### Symptoms

Your Envoy proxy is unable to connect to the App Mesh Envoy management service. You are
seeing:

- Connection refused errors
- Connection timeouts
- Errors resolving the App Mesh Envoy management service endpoint
- gRPC errors

###### Resolution

Make sure that your Envoy proxy has access to the internet or to a private [VPC endpoint](vpc-endpoints.md "vpc-endpoints.md") and that your [security groups](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") allow outbound
traffic on port 443. App Mesh’s public Envoy management service endpoints follow the fully
qualified domain name (FQDN) format.

```
# App Mesh Production Endpoint
appmesh-envoy-management.`Region-code`.amazonaws.com

# App Mesh Preview Endpoint
appmesh-preview-envoy-management.`Region-code`.amazonaws.com
```

You can debug your connection to EMS using the command below. This sends a valid, but empty gRPC
request to the Envoy Management Service.

```
curl -v -k -H 'Content-Type: application/grpc' -X POST https://appmesh-envoy-management.`Region-code`.amazonaws.com:443/envoy.service.discovery.v3.AggregatedDiscoveryService/StreamAggregatedResources
```

If you receive these messages back, your connection to Envoy Management Service is functional.
For debugging gRPC related errors, see the errors in [Envoy
disconnected from App Mesh Envoy management service with error text.](troubleshooting-setup.md#ts-setup-grpc-error-codes "troubleshooting-setup.md#ts-setup-grpc-error-codes")

```
grpc-status: 16
grpc-message: Missing Authentication Token
```

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Envoy disconnected from App Mesh Envoy management service

with error text

###### Symptoms

Your Envoy proxy is unable to connect to the App Mesh Envoy management service and receive its
configuration. Your Envoy proxy logs contain a log entry like the following.

```
gRPC config stream closed: `gRPC status code`, `message`
```

###### Resolution

In most cases, the message portion of the log should indicate the problem. The following
table lists the most common gRPC status codes that you might see, their causes, and their
resolutions.

| gRPC status code | Cause                                                                                                                                       | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `0`              | Graceful disconnect from the Envoy management service.                                                                                      | There is no issue. App Mesh occasionally disconnects Envoy proxies with this<br>status code. Envoy will reconnect and continue receiving updates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `3`              | The mesh endpoint (virtual node or virtual gateway), or one of its associated<br>resources, could not be found.                             | Double check your Envoy configuration to make sure that it has the appropriate<br>name of the App Mesh resource that it represents. If your App Mesh resource is<br>integrated with other AWS resources, such as AWS Cloud Map namespaces or ACM<br>certificates, then make sure that those resources exist.                                                                                                                                                                                                                                                                                                                                                  |
| `7`              | The Envoy proxy is unauthorized to perform an action, such as connect to the<br>Envoy management service, or retrieve associated resources. | Make sure that you [create an IAM policy](proxy-authorization.md#create-iam-policy "proxy-authorization.md#create-iam-policy") that has the appropriate policy statements for App Mesh and other services<br>and attach that policy to the IAM user or role that your Envoy proxy is using to<br>connect to the Envoy management service.                                                                                                                                                                                                                                                                                                                     |
| `8`              | The number of Envoy proxies for a given App Mesh resource exceeds the<br>account-level service quota.                                       | See [App Mesh service quotas](service-quotas.md "service-quotas.md") for<br>information on default account quotas and how to request a quota increase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `16`             | The Envoy proxy does not have valid authentication credentials for<br>AWS.                                                                  | Make sure that the Envoy has appropriate credentials to connect to AWS<br>services through an IAM user or role. A known issue, [#24136](https://github.com/envoyproxy/envoy/issues/24136 "https://github.com/envoyproxy/envoy/issues/24136"), in Envoy<br>for version `v1.24` and before fails to fetch the credentials if Envoy<br>process uses over `1024` file descriptors. This happens when Envoy is<br>serving high traffic volume. You can confirm this issue by checking Envoy logs at<br>debug level for the text "`A libcurl function was given a bad<br>argument`". To mitigate this issue, upgrade to Envoy version<br>`v1.25.1.0-prod` or later. |

You can observe the status codes and messages from your Envoy proxy with [Amazon CloudWatch
Insights](../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md "../../../AmazonCloudWatch/latest/logs/AnalyzingLogData.md") by using the following query:

```
`filter @message like /gRPC config stream closed/
| parse @message "gRPC config stream closed: *, *" as StatusCode, Message`
```

If the provided error message was not helpful, or your issue is still not resolved, then consider
opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here").

## Envoy container health check, readiness probe, or

liveliness probe failing

###### Symptoms

Your Envoy proxy is failing health checks in an Amazon ECS task, Amazon EC2 instance, or Kubernetes
pod. For example, you query the Envoy administration interface with the following command and
receive a status other than `LIVE`.

```
`curl -s http://`my-app.default.svc.cluster.local`:`9901`/server_info | jq '.state'`
```

###### Resolution

The following is a list of remediation steps depending on the status returned by the Envoy
proxy.

- `PRE_INITIALIZING` or `INITIALIZING` – The Envoy proxy has
  yet to receive configuration, or cannot connect and retrieve configuration from App Mesh
  Envoy management service. The Envoy may be receiving an error from the Envoy management
  service when trying to connect. For more information, see the errors in [Envoy disconnected from App Mesh Envoy management service
  with error text](#ts-setup-grpc-error-codes "#ts-setup-grpc-error-codes").
- `DRAINING` – The Envoy proxy has begun draining connections in response
  to a `/healthcheck/fail` or `/drain_listeners` request on the Envoy
  administration interface. We do not recommend invoking these paths on the administration
  interface unless you are about to terminate your Amazon ECS task, Amazon EC2 instance, or Kubernetes
  pod.

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Health check from the load balancer to the

mesh endpoint is failing

###### Symptoms

Your mesh endpoint is considered healthy by the container health check or readiness probe,
but the health check from the load balancer to the mesh endpoint is failing.

###### Resolution

To resolve the issue, complete the following tasks.

- Make sure that the [security group](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") associated
  with your mesh endpoint accepts inbound traffic on the port you've configured for your
  health check.
- Make sure that the health check is succeeding consistently when requested manually; for
  example, from a [bastion host within your VPC](https://aws.amazon.com/quickstart/architecture/linux-bastion/ "https://aws.amazon.com/quickstart/architecture/linux-bastion/").
- If you are configuring a health check for a virtual node, then we recommend implementing
  a health check endpoint in your application; for example, /ping for HTTP. This ensures that
  both the Envoy proxy and your application are routable from the load balancer.
- You can use any elastic load balancer type for the virtual node, depending on the
  features that you need. For more information, see [Elastic Load Balancing
  features](https://aws.amazon.com/elasticloadbalancing/features/#compare "https://aws.amazon.com/elasticloadbalancing/features/#compare").
- If you are configuring a health check for a [virtual
  gateway](virtual_gateways.md "virtual_gateways.md"), then we recommend using a [network load
  balancer](../../../elasticloadbalancing/latest/network/network-load-balancers.md "../../../elasticloadbalancing/latest/network/network-load-balancers.md") with a TCP or TLS health check on the virtual gateway's listener port.
  This ensures that the virtual gateway listener is bootstrapped and ready to accept
  connections.

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").

## Virtual gateway not accepting traffic on ports 1024 or

less

###### Symptoms

Your virtual gateway is not accepting traffic on port 1024 or less, but does accept traffic
on a port number that is greater than 1024. For example, you query the Envoy stats with the
following command and receive a value other than zero.

```
`curl -s http://my-app.default.svc.cluster.local:9901/stats | grep "update_rejected"`
```

You might see text similar to the following text in your logs describing a failure to bind to a
privileged port:

```
gRPC config for type.googleapis.com/envoy.api.v2.Listener rejected: Error adding/updating listener(s) lds_ingress_0.0.0.0_port_<port num>: cannot bind '0.0.0.0:<port num>': Permission denied
```

###### Resolution

To resolve the issue, the user specified for the gateway needs to have the linux capability
`CAP_NET_BIND_SERVICE`. For more information, see [Capabilities](https://www.man7.org/linux/man-pages/man7/capabilities.7.html "https://www.man7.org/linux/man-pages/man7/capabilities.7.html") in
the Linux Programmer's Manual, [Linux parameters](../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_linuxparameters "../../../AmazonECS/latest/developerguide/task_definition_parameters.md#container_definition_linuxparameters") in ECS Task definition parameters, and [Set capabilities for a container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container "https://kubernetes.io/docs/tasks/configure-pod-container/security-context/#set-capabilities-for-a-container") in the Kubernetes documentation.

###### Important

Fargate must use a port value greater than 1024.

If your issue is still not resolved, then consider opening a [GitHub issue](https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here "https://github.com/aws/aws-app-mesh-roadmap/issues/new?assignees=&labels=Bug&template=issue--bug-report.md&title=Bug%3A+describe+bug+here") or contact [AWS
Support](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/").
