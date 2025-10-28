# App Mesh interface VPC endpoints (AWS PrivateLink)

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

You can improve the security posture of your Amazon VPC by configuring App Mesh to use an
interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology
that enables you to privately access App Mesh APIs by using private IP addresses. PrivateLink
restricts all network traffic between your Amazon VPC and App Mesh to the Amazon network.

You're not required to configure PrivateLink, but we recommend it. For more information
about PrivateLink and interface VPC endpoints, see [Accessing
Services Through AWS PrivateLink](../../../vpc/latest/userguide/what-is-amazon-vpc.md#what-is-privatelink "../../../vpc/latest/userguide/what-is-amazon-vpc.md#what-is-privatelink").

## Considerations for App Mesh

interface VPC endpoints

Before you set up interface VPC endpoints for App Mesh, be aware of the following
considerations:

- If your Amazon VPC doesn't have an internet gateway and your tasks use the
  `awslogs` log driver to send log information to CloudWatch Logs, you must
  create an interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with Interface VPC Endpoints](../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md "../../../AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.md") in the
  _Amazon CloudWatch Logs User Guide_.
- VPC endpoints don't support AWS cross-Region requests. Ensure that you
  create your endpoint in the same Region where you plan to issue your API calls
  to App Mesh.
- VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want
  to use your own DNS, you can use conditional DNS forwarding. For more
  information, see [DHCP Options Sets](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md")
  in the _Amazon VPC User Guide_.
- The security group attached to the VPC endpoint must allow incoming
  connections on port 443 from the private subnet of the Amazon VPC.

###### Note

Controlling access to App Mesh by attaching an endpoint policy to the VPC
endpoint (for example, using the service name
`com.amazonaws.`Region`.appmesh-envoy-management`)
isn't supported for Envoy connection.

For additional considerations and limitations, see [Interface Endpoint Availability Zone Considerations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-availability-zones "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-availability-zones") and [Interface
Endpoint Properties and Limitations](../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations "../../../vpc/latest/userguide/vpce-interface.md#vpce-interface-limitations").

## Create the interface VPC endpoint for

App Mesh

To create the interface VPC endpoint for the App Mesh service, use the [Creating an
Interface Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") procedure in the _Amazon VPC User Guide_. Specify
`com.amazonaws.`Region`.appmesh-envoy-management`
for the service name for your Envoy proxy to connect to the App Mesh's public Envoy
management service and
`com.amazonaws.`Region`.appmesh` for mesh
operations.

###### Note

`Region` represents the Region identifier
for an AWS Region supported by App Mesh, such as `us-east-2` for the
US East (Ohio) Region.

Though you can define an interface VPC endpoint for App Mesh in any
Region where App Mesh is supported, you may not be able to define an
endpoint for all Availability Zones in each Region. To find out which
Availability Zones are supported with interface VPC endpoints in a
Region, use the [describe-vpc-endpoint-services](../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md "../../../cli/latest/reference/ec2/describe-vpc-endpoint-services.md") command or use the AWS Management Console. For example,
the following commands return the availability zones to which you can deploy an App Mesh
interface VPC endpoints within the US East (Ohio) Region:

```
`aws --region `us-east-2` ec2 describe-vpc-endpoint-services --query 'ServiceDetails[?ServiceName==`com.amazonaws.`us-east-2`.appmesh-envoy-management`].AvailabilityZones[]'`
```

```
`aws --region `us-east-2` ec2 describe-vpc-endpoint-services --query 'ServiceDetails[?ServiceName==`com.amazonaws.`us-east-2`.appmesh`].AvailabilityZones[]'`
```
