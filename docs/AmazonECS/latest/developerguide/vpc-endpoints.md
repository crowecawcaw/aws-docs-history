

# Amazon ECS interface VPC endpoints (AWS PrivateLink)
<a name="vpc-endpoints"></a>

You can improve the security posture of your VPC by configuring Amazon ECS to use an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink, a technology that allows you to privately access Amazon ECS APIs by using private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and Amazon ECS to the Amazon network. You don't need an internet gateway, a NAT device, or a virtual private gateway.

For more information about AWS PrivateLink and VPC endpoints, see [VPC endpoints ](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html#concepts-vpc-endpoints) in the *Amazon VPC User Guide*.

## Considerations
<a name="ecs-vpc-endpoint-considerations"></a>

### Considerations for endpoints in Regions introduced starting on December 23, 2023
<a name="fargate-ecs-vpc-endpoint-region-considerations"></a>

Before you set up interface VPC endpoints for Amazon ECS, be aware of the following considerations:
+ You must have the following Region-specific VPC endpoints:
**Note**  
If you do not configure all of the endpoints, your traffic will go over the public endpoints, not your VPC endpoint.
  + `com.amazonaws.{{region}}.ecs-agent`
  + `com.amazonaws.{{region}}.ecs-telemetry`
  + `com.amazonaws.{{region}}.ecs`

  For example, the Canada West (Calgary) (ca-west-1) Region needs the following VPC endpoints:
  + `com.amazonaws.ca-west-1.ecs-agent`
  + `com.amazonaws.ca-west-1.ecs-telemetry`
  + `com.amazonaws.ca-west-1.ecs`
+ When you use a template to create AWS resources in the new Region and the template was copied from a Region introduced before December 23, 2023, depending on the copy-from Region, perform one of the following operations.

  For example, the copy-from Region is US East (N. Virginia) (us-east-1). The copy-to Region is Canada West (Calgary) (ca-west-1).


<table>
<thead>
  <tr><th>Configuration</th><th>Action</th><th></th></tr>
</thead>
<tbody>
  <tr><td>The copied-from Region does not have any VPC endpoints.</td><td>Create all three VPC endpoints for the new Region (for example, <code>com.amazonaws.ca-west-1.ecs-agent</code>).</td><td></td></tr>
  <tr><td>The copied-from Region contains Region-specific VPC endpoints.</td><td> <ol><li> Create all three VPC endpoints for the new Region (for example, <code>com.amazonaws.ca-west-1.ecs-agent</code>). </li><li> Delete all three VPC endpoints for the copy-from Region (for example, <code>com.amazonaws.us-east-1.ecs-agent</code>). </li></ol> </td><td></td></tr>
</tbody>
</table>


### Considerations for Amazon ECS VPC endpoints for Fargate
<a name="fargate-ecs-vpc-endpoint-considerations"></a>

When there is an VPC endpoint for `ecr.dkr` and `ecr.api` in the same VPC where a Fargate task is deployed into, it will use the VPC endpoint. If there is no VPC endpoint, it will use the Fargate interface.

Before you set up interface VPC endpoints for Amazon ECS, be aware of the following considerations:
+ Tasks using Fargate don't require the interface VPC endpoints for Amazon ECS, but you might need interface VPC endpoints for Amazon ECR, Secrets Manager, or Amazon CloudWatch Logs described in the following points.
  + To allow your tasks to pull private images from Amazon ECR, you must create the interface VPC endpoints for Amazon ECR. For more information, see [Interface VPC Endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html) in the *Amazon Elastic Container Registry User Guide*.
**Important**  
If you configure Amazon ECR to use an interface VPC endpoint, you can create a task execution role that includes condition keys to restrict access to a specific VPC or VPC endpoint. For more information, see [Fargate tasks pulling Amazon ECR images over interface endpoints permissions](task_execution_IAM_role.md#task-execution-ecr-conditionkeys).
If your tasks are in an IPv6-only configuration and use an Amazon ECR dualstack image URI, note that Amazon ECR doesn't support dualstack interface VPC endpoints. For more information, see [Getting started with making requests over IPv6](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-requests.html#ipv6-access-getting-started) in the *Amazon Elastic Container Registry User Guide*.
  + To allow your tasks to pull sensitive data from Secrets Manager, you must create the interface VPC endpoints for Secrets Manager. For more information, see [Using Secrets Manager with VPC Endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html) in the *AWS Secrets Manager User Guide*.
  + If your VPC doesn't have an internet gateway and your tasks use the `awslogs` log driver to send log information to CloudWatch Logs, you must create an interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with Interface VPC Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html) in the *Amazon CloudWatch Logs User Guide*.
+ VPC endpoints currently don't support cross-Region requests. Ensure that you create your endpoint in the same Region where you plan to issue your API calls to Amazon ECS. For example, assume that you want to run tasks in US East (N. Virginia). Then, you must create the Amazon ECS VPC endpoint in US East (N. Virginia). An Amazon ECS VPC endpoint created in any other region can't run tasks in US East (N. Virginia).
+ VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+ The security group attached to the VPC endpoint must allow incoming connections on TCP port 443 from the private subnet of the VPC.
+ Service Connect management of the Envoy proxy uses the `com.amazonaws.{{region}}.ecs-agent` VPC endpoint. When you don't use the VPC endpoints, Service Connect management of the Envoy proxy uses the `ecs-sc` endpoint in that Region. For a list of the Amazon ECS endpoints in each Region, see  [Amazon ECS endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/ecs-service.html).  

### Considerations for Amazon ECS VPC endpoints for EC2
<a name="ec2-ecs-vpc-endpoint-considerations"></a>

Before you set up interface VPC endpoints for Amazon ECS, be aware of the following considerations:
+ Tasks using EC2 require that the container instances that they're launched on to run version `1.25.1` or later of the Amazon ECS container agent. For more information, see [Amazon ECS Linux container instance management](manage-linux.md).
+ To allow your tasks to pull sensitive data from Secrets Manager, you must create the interface VPC endpoints for Secrets Manager. For more information, see [Using Secrets Manager with VPC Endpoints](https://docs.aws.amazon.com/secretsmanager/latest/userguide/vpc-endpoint-overview.html) in the *AWS Secrets Manager User Guide*.
+ If your VPC doesn't have an internet gateway and your tasks use the `awslogs` log driver to send log information to CloudWatch Logs, you must create an interface VPC endpoint for CloudWatch Logs. For more information, see [Using CloudWatch Logs with Interface VPC Endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html) in the *Amazon CloudWatch Logs User Guide*.
+ VPC endpoints currently don't support cross-Region requests. Ensure that you create your endpoint in the same Region where you plan to issue your API calls to Amazon ECS. For example, assume that you want to run tasks in US East (N. Virginia). Then, you must create the Amazon ECS VPC endpoint in US East (N. Virginia). An Amazon ECS VPC endpoint created in any other Region can't run tasks in US East (N. Virginia).
+ VPC endpoints only support Amazon-provided DNS through Amazon Route 53. If you want to use your own DNS, you can use conditional DNS forwarding. For more information, see [DHCP Options Sets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_DHCP_Options.html) in the *Amazon VPC User Guide*.
+ The security group attached to the VPC endpoint must allow incoming connections on TCP port 443 from the private subnet of the VPC.

## Understanding Amazon ECS endpoint naming patterns
<a name="ecs-endpoint-naming-patterns"></a>

The Amazon ECS container agent uses the [DiscoverPollEndpoint](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DiscoverPollEndpoint.html) API to find the agent and telemetry endpoints to connect to. The returned hostnames depend on whether the call uses the `com.amazonaws.{{region}}.ecs` interface VPC endpoint.
+ When the call goes through the `ecs` interface VPC endpoint, the returned endpoints use the base private DNS names `ecs-a.{{region}}.amazonaws.com` and `ecs-t.{{region}}.amazonaws.com`. A numeric identifier appears in the URL path, for example `https://ecs-a.{{region}}.amazonaws.com/acs/1/`.
+ When the call doesn't go through the `ecs` interface VPC endpoint, the returned endpoints can use numbered hostnames, such as `ecs-a-1.{{region}}.amazonaws.com` and `ecs-t-1.{{region}}.amazonaws.com`. These hostnames resolve to public endpoints.

You don't need to create DNS records for numbered hostnames. If you use your own Route 53 private hosted zones instead of the endpoint's private DNS, create hosted zones only for the following domains:
+ `ecs.{{region}}.amazonaws.com`
+ `ecs-a.{{region}}.amazonaws.com`
+ `ecs-t.{{region}}.amazonaws.com`

### Troubleshooting agent connectivity through VPC endpoints
<a name="ecs-discoverpollendpoint-role"></a>

If your container instances connect to numbered hostnames such as `ecs-a-1.{{region}}.amazonaws.com`, the agent's DiscoverPollEndpoint call isn't going through the `ecs` interface VPC endpoint. Check the following from the container instance:
+ `ecs.{{region}}.amazonaws.com` resolves to the private IP addresses of your `ecs` endpoint.
+ If the agent uses an HTTP proxy, either the proxy resolves `ecs.{{region}}.amazonaws.com` to your `ecs` endpoint, or the hostname is in `NO_PROXY`. Otherwise the proxy can send the call over the public path even when DNS on the instance is correct. For more information, see [Using an HTTP proxy for Amazon ECS Linux container instances](http_proxy_config.md).

After the call goes through the `ecs` endpoint, the agent connects to `ecs-a.{{region}}.amazonaws.com` and `ecs-t.{{region}}.amazonaws.com`. Make sure that you also created the `ecs-agent` and `ecs-telemetry` interface VPC endpoints and that those hostnames resolve to their private IP addresses. For more information, see [Creating the VPC Endpoints for Amazon ECS](#ecs-setting-up-vpc-create).

## Creating the VPC Endpoints for Amazon ECS
<a name="ecs-setting-up-vpc-create"></a>

To create the VPC endpoint for the Amazon ECS service, use the [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html#create-interface-endpoint) procedure in the *Amazon VPC User Guide* to create the following endpoints. If you have existing container instances within your VPC, you should create the endpoints in the order that they're listed. If you plan on creating your container instances after your VPC endpoint is created, the order doesn't matter.

**Note**  
If you do not configure all of the endpoints, your traffic will go over the public endpoints, not your VPC endpoint.  
When you create endpoints, Amazon ECS also creates a private DNS name for the endpoint. For example, `ecs-a.region.amazonaws.com` for ecs-agent and `ecs-t.region.amazonaws.com` for ecs-telemetry.
+ `com.amazonaws.{{region}}.ecs-agent`
+ `com.amazonaws.{{region}}.ecs-telemetry`
+ `com.amazonaws.{{region}}.ecs`

**Note**  
{{region}} represents the Region identifier for an AWS Region supported by Amazon ECS, such as `us-east-2` for the US East (Ohio) Region.

The `ecs-agent` endpoint uses the `ecs:poll` API, and the `ecs-telemetry` endpoint uses the `ecs:poll` and `ecs:StartTelemetrySession` API.

If you have existing tasks that are using the EC2 launch type, after you have created the VPC endpoints, each container instance needs to pick up the new configuration. For this to happen, you must either reboot each container instance or restart the Amazon ECS container agent on each container instance. To restart the container agent, do the following.<a name="procedure_restart_ecs_agent"></a>

**To restart the Amazon ECS container agent**

1. Log in to your container instance via SSH.

1. Stop the container agent.

   ```
   sudo docker stop ecs-agent
   ```

1. Start the container agent.

   ```
   sudo docker start ecs-agent
   ```

After you have created the VPC endpoints and restarted the Amazon ECS container agent on each container instance, all newly launched tasks pick up the new configuration.

## Creating a VPC endpoint policy for Amazon ECS
<a name="vpc-endpoint-policy"></a>

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon ECS. The policy specifies the following information:
+ The principal that can perform actions.
+ The actions that can be performed.
+ The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide*.

**Example: VPC endpoint policy for Amazon ECS actions**  
The following is an example of an endpoint policy for Amazon ECS. When attached to an endpoint, this policy grants access to permission to create and list clusters. The `CreateCluster` and `ListClusters` actions do not accept any resources, so the resource definition is set to \* for all resources. 

```
{
   "Statement":[
    {
      "Principal":"*",
      "Effect": "Allow",
      "Action": [
        "ecs:CreateCluster",
        "ecs:ListClusters"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}
```