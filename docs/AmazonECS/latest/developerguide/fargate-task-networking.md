

# Amazon ECS task networking options for Fargate
<a name="fargate-task-networking"></a>

By default, every Amazon ECS task on Fargate is provided an elastic network interface (ENI) with a primary private IP address. When using a public subnet, you can optionally assign a public IP address to the task's ENI. If your VPC is configured for dual-stack mode and you use a subnet with an IPv6 CIDR block, your task's ENI also receives an IPv6 address. A task can only have one ENI that's associated with it at a time. Containers that belong to the same task can also communicate over the `localhost` interface. For more information about VPCs and subnets, see [How Amazon VPC works](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html) in the *Amazon VPC User Guide*.

For a task on Fargate to pull a container image, the task must have a route to the internet. The following describes how you can verify that your task has a route to the internet.
+ When using a public subnet, you can assign a public IP address to the task ENI.
+ When using a private subnet, the subnet can have a NAT gateway attached.
+ When using container images that are hosted in Amazon ECR, you can configure Amazon ECR to use an interface VPC endpoint and the image pull occurs over the task's private IPv4 address. For more information, see [Amazon ECR interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/vpc-endpoints.html) in the *Amazon Elastic Container Registry User Guide*.

Because each task gets its own ENI, you can use networking features such as VPC Flow Logs, which you can use to monitor traffic to and from your tasks. For more information, see [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) in the *Amazon VPC User Guide*.

You can also take advantage of AWS PrivateLink. You can configure a VPC interface endpoint so that you can access Amazon ECS APIs through private IP addresses. AWS PrivateLink restricts all network traffic between your VPC and Amazon ECS to the Amazon network. You don't need an internet gateway, a NAT device, or a virtual private gateway. For more information, see [Amazon ECS interface VPC endpoints (AWS PrivateLink)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/vpc-endpoints.html).

For examples of how to use the `NetworkConfiguration` resource with CloudFormation, see [CloudFormation example templates for Amazon ECS](working-with-templates.md).

The ENIs that are created are fully managed by AWS Fargate. Moreover, there's an associated IAM policy that's used to grant permissions for Fargate. For tasks using Fargate platform version `1.4.0` or later, the task receives a single ENI (referred to as the task ENI) and all network traffic flows through that ENI within your VPC. This traffic is recorded in your VPC flow logs. For tasks that use Fargate platform version `1.3.0` and earlier, in addition to the task ENI, the task also receives a separate Fargate owned ENI, which is used for some network traffic that isn't visible in the VPC flow logs. The following table describes the network traffic behavior and the required IAM policy for each platform version.


|  Action  |  Traffic flow with Linux platform version `1.3.0` and earlier  |  Traffic flow with Linux platform version `1.4.0`  |  Traffic flow with Windows platform version `1.0.0`  |  IAM permission  | 
| --- | --- | --- | --- | --- | 
|  Retrieving Amazon ECR login credentials  |  Fargate owned ENI  |  Task ENI  |  Task ENI  |  Task execution IAM role  | 
|  Image pull  |  Task ENI  |  Task ENI  |  Task ENI  |  Task execution IAM role  | 
|  Sending logs through a log driver  |  Task ENI  |  Task ENI  |  Task ENI  |  Task execution IAM role  | 
|  Sending logs through FireLens for Amazon ECS  |  Task ENI  |  Task ENI  |  Task ENI  |  Task IAM role  | 
|  Retrieving secrets from Secrets Manager or Systems Manager  |  Fargate owned ENI  |  Task ENI  |  Task ENI  |  Task execution IAM role  | 
|  Amazon EFS file system traffic  |  Not available  |  Task ENI  |  Task ENI  |  Task IAM role  | 
|  Application traffic  |  Task ENI  |  Task ENI  |  Task ENI  |  Task IAM role  | 

## Considerations
<a name="fargate-task-networking-considerations"></a>

Consider the following when using task networking.
+ The Amazon ECS service-linked role is required to provide Amazon ECS with the permissions to make calls to other AWS services on your behalf. This role is created for you when you create a cluster or if you create or update a service in the AWS Management Console. For more information, see [Using service-linked roles for Amazon ECS](using-service-linked-roles.md). You can also create the service-linked role using the following AWS CLI command.

  ```
  aws iam [create-service-linked-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-service-linked-role.html) --aws-service-name ecs.amazonaws.com
  ```
+ Amazon ECS populates the hostname of the task with an Amazon provided DNS hostname when both the `enableDnsHostnames` and `enableDnsSupport` options are enabled on your VPC. If these options aren't enabled, the DNS hostname of the task is set to a random hostname. For more information about the DNS settings for a VPC, see [Using DNS with Your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html) in the *Amazon VPC User Guide*.
+ You can only specify up to 16 subnets and 5 security groups for `awsVpcConfiguration`. For more information, see [AwsVpcConfiguration](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_AwsVpcConfiguration.html) in the *Amazon Elastic Container Service API Reference*.
+ You can't manually detach or modify the ENIs that are created and attached by Fargate. This is to prevent the accidental deletion of an ENI that's associated with a running task. To release the ENIs for a task, stop the task.
+ If a VPC subnet is updated to change the DHCP options set it uses, you can't also apply these changes to existing tasks that use the VPC. Start new tasks, which will receive the new setting to smoothly migrate while testing the new change and then stop the old ones, if no rollback is required.
+ The following applies to tasks run on Fargate platform version `1.4.0` or later for Linux or `1.0.0` for Windows. Tasks launched in dual-stack subnets receive an IPv4 address and an IPv6 address. Tasks launched in IPv6-only subnets receive only an IPv6 address.
+ For tasks that use platform version `1.4.0` or later for Linux or `1.0.0` for Windows, the task ENIs support jumbo frames. Network interfaces are configured with a maximum transmission unit (MTU), which is the size of the largest payload that fits within a single frame. The larger the MTU, the more application payload can fit within a single frame, which reduces per-frame overhead and increases efficiency. Supporting jumbo frames reduces overhead when the network path between your task and the destination supports jumbo frames.
+ Services with tasks that use Fargate only support Application Load Balancer and Network Load Balancer. Classic Load Balancer isn't supported. When you create any target groups, you must choose `ip` as the target type, not `instance`. For more information, see [Use load balancing to distribute Amazon ECS service traffic](service-load-balancing.md).

## Using a VPC in dual-stack mode
<a name="fargate-task-networking-vpc-dual-stack"></a>

When using a VPC in dual-stack mode, your tasks can communicate over IPv4 or IPv6, or both. IPv4 and IPv6 addresses are independent of each other and you must configure routing and security in your VPC separately for IPv4 and IPv6. For more information about configuring your VPC for dual-stack mode, see [Migrating to IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon VPC User Guide*.

If the following conditions are met, Amazon ECS tasks on Fargate are assigned an IPv6 address:
+ Your Amazon ECS `dualStackIPv6` account setting is turned on (`enabled`) for the IAM principal launching your tasks in the Region you're launching your tasks in. This setting can only be modified using the API or AWS CLI. You have the option to turn this setting on for a specific IAM principal on your account or for your entire account by setting your account default setting. For more information, see [Access Amazon ECS features with account settings](ecs-account-settings.md).
+ Your VPC and subnet are enabled for IPv6. For more information about how to configure your VPC for dual-stack mode, see [Migrating to IPv6](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6.html) in the *Amazon VPC User Guide*.
+ Your subnet is enabled for auto-assigning IPv6 addresses. For more information about how to configure your subnet, see [Modify the IPv6 addressing attribute for your subnet](https://docs.aws.amazon.com/vpc/latest/userguide/modify-subnets.html) in the *Amazon VPC User Guide*.
+ The task or service uses Fargate platform version `1.4.0` or later for Linux.

For Amazon ECS tasks on Fargate running in a VPC in dual-stack mode, to communicate with dependency services used in task launch process such as ECR, SSM and SecretManager, the public subnet's route table needs IPv4 (0.0.0.0/0) route to an internet gateway and the private subnet's route table needs IPv4 (0.0.0.0/0) route to an NAT gateway. For more information, see [Internet gateways](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) and [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon VPC User Guide*. 

For examples of how to configure a dual-stack VPC, see [ Example dual-stack VPC configuration](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-example.html). 

## Using a VPC in IPv6-only mode
<a name="fargate-task-networking-vpc-ipv6-only"></a>

In an IPv6-only configuration, your Amazon ECS tasks communicate exclusively over IPv6. To set up VPCs and subnets for an IPv6-only configuration, you must add an IPv6 CIDR block to the VPC and create subnets that include only an IPv6 CIDR block. For more information see [Add IPv6 support for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-migrate-ipv6-add.html) and [Create a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/create-subnets.html) in the *Amazon VPC User Guide*. You must also update route tables with IPv6 targets and configure security groups with IPv6 rules. For more information, see [Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) and [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the *Amazon VPC User Guide*.

The following considerations apply:
+ You can update an IPv4-only or dualstack Amazon ECS service to an IPv6-only configuration by either updating the service directly to use IPv6-only subnets or by creating a parallel IPv6-only service and using Amazon ECS blue-green deployments to shift traffic to the new service. For more information about Amazon ECS blue-green deployments, see [Amazon ECS blue/green deployments](deployment-type-blue-green.md).
+ An IPv6-only Amazon ECS service must use dualstack load balancers with IPv6 target groups. If you're migrating an existing Amazon ECS service that's behind a Application Load Balancer or a Network Load Balancer, you can create a new dualstack load balancer and shift traffic from the old load balancer, or update the IP address type of the existing load balancer.

   For more information about Network Load Balancers, see [Create a Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-network-load-balancer.html) and [Update the IP address types for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-ip-address-type.html) in the *User Guide for Network Load Balancers*. For more information about Application Load Balancers, see [Create an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-application-load-balancer.html) and [Update the IP address types for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-ip-address-type.html) in the *User Guide for Application Load Balancers*.
+ IPv6-only configuration isn't supported on Windows.
+ For Amazon ECS tasks in an IPv6-only configuration to communicate with IPv4-only endpoints, you can set up DNS64 and NAT64 for network address translation from IPv6 to IPv4. For more information, see [DNS64 and NAT64](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-nat64-dns64.html) in the *Amazon VPC User Guide*.
+ IPv6-only configuration is supported on Fargate platform version `1.4.0` or later.
+ Amazon ECS workloads in an IPv6-only configuration must use Amazon ECR dualstack image URI endpoints when pulling images from Amazon ECR. For more information, see [Getting started with making requests over IPv6](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-requests.html#ipv6-access-getting-started) in the *Amazon Elastic Container Registry User Guide*.
**Note**  
Amazon ECR doesn't support dualstack interface VPC endpoints that tasks in an IPv6-only configuration can use. For more information, see [Getting started with making requests over IPv6](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr-requests.html#ipv6-access-getting-started) in the *Amazon Elastic Container Registry User Guide*.
+ Amazon ECS Exec isn't supported in an IPv6-only configuration.
+ Amazon CloudWatch doesn't support a dualstack FIPS endpoint that can be used to monitor Amazon ECS tasks in IPv6-only configuration that use FIPS-140 compliance. For more information about FIPS-140, see [AWS Fargate Federal Information Processing Standard (FIPS-140)](ecs-fips-compliance.md).

### AWS Regions that support IPv6-only mode for Amazon ECS
<a name="fargate-task-networking-ipv6-only-regions"></a>

You can run tasks in an IPv6-only configuration in the following AWS Regions that Amazon ECS is available in:
+ US East (Ohio)
+ US East (N. Virginia)
+ US West (N. California)
+ US West (Oregon)
+ Africa (Cape Town)
+ Asia Pacific (Hong Kong)
+ Asia Pacific (Hyderabad)
+ Asia Pacific (Jakarta)
+ Asia Pacific (Melbourne)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Osaka)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Canada West (Calgary)
+ China (Beijing)
+ China (Ningxia)
+ Europe (Frankfurt)
+ Europe (London)
+ Europe (Milan)
+ Europe (Paris)
+ Europe (Spain)
+ Israel (Tel Aviv)
+ Middle East (Bahrain)
+ Middle East (UAE)
+ South America (São Paulo)
+ AWS GovCloud (US-East)
+ AWS GovCloud (US-West)