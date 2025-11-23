# Resources created by Amazon ECS Express Mode services

An Express Mode service reduces the complexity of deploying containerized applications by providing sensible defaults and
automating the configuration of supporting AWS services. Instead of managing hundreds of configuration parameters across multiple services,
an Express Mode service requires only a container image, task execution role and infrastructure role to get started.

Express Mode services have simplified procedures for provisioning and configuring an Amazon ECS
Service that bundles together the preferred infrastructure for getting a production web application
running. Express Mode services automatically incorporate operational and configuration best
practices. The following resources are created:

- The ECS default cluster (if it does not already exist) with Fargate capacity providers
- A task definition with container, logging, and networking configurations
- A service with canary deployment and auto scaling
- Application Load Balancer with HTTPS listener, listener rules, and target groups
- Security groups with minimal required ingress
- Service Linked Roles for auto-scaling and load balancing
- Application Auto Scaling scalable target and target tracking scaling policy.

The scaling policy adds or removes service tasks as required to keep the metric
at, or close to, the specified target value. In addition to keeping the metric close to the target
value, a target tracking scaling policy also adjusts to the fluctuations in the metric due to a
fluctuating load pattern and minimizes rapid fluctuations in the number of tasks running in your service.

- Log group specific to the service
- Metric alarm for detecting faulty deployments
- ACM certificate
  Use the defaults to get started with Express Mode services, or configure your
  application using a minimal set of parameters.

## Cluster defaults

The following defaults are configurable from within Express Mode for the Cluster:

- clusterName: Uses the `default` cluster.

You can customize this option by using the **Additional
configurations** option in the console, or by specifying
`create-express-gateway-service --cluster`.

The following defaults are set by Express Mode but can be updated in the Cluster directly.

- capacityProviders: ["FARGATE"] - Uses Fargate

## Task definition defaults

The following defaults are configurable from within Express Mode for the task definition:

- cpu: 1024 - 1 vCPU unit allocated to the task

You can customize this option by using the **Additional
configurations** option in the console, or by running
`create-express-gateway-service --cpu`.

- memory: 2048 - 2 GB of memory allocated to the task

You can customize this option by using the **Additional
configurations** option in the console, or by running
`create-express-gateway-service --memory`.

The following defaults are set by Express Mode but can be updated in the Task Definition directly.

- networkMode: "awsvpc" - Uses `awsvpc` networking mode
- operatingSystemFamily: "LINUX" - Runs on Linux operating system
- cpuArchitecture: "X86_64" - Uses x86_64 processor architecture
- requiresCompatibilities: ["FARGATE"] - Compatible with Fargate launch type
- platformVersion: "LATEST" - Uses the latest Fargate platform version

## Container definition defaults

The following defaults are configurable from within Express Mode for the container:

- port: 80 - Default port for container traffic

The following defaults are set by Express Mode but can be updated in the Task Definition - Container Definition directly:

- essential: true - Container is marked as essential for task health
- protocol: "tcp" - Default protocol for load balancer communication
- name: "Main" - Default name for the primary container

Changing the name of the default container can effect Express Mode's ability to make subsequent updates to your service.
This is not recommended if you intend to continue using the Express Mode Console or APIs

- versionConsistency: enabled - Resolves image tags to digest IDs for consistent deployments
- initProcessEnabled: true - Enables Docker init process support.
- stopTimeout: 30 seconds - Time between SIGTERM and SIGKILL signals.

## Logging defaults

The following defaults are configurable from within Express Mode for the CloudWatch Logs:

- awslogs-group: "/aws/ecs/<cluster>/<name>-####" - Log group name derived from cluster and service name

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --primary-container “awsLogsConfiguration”=[{“logGroup”=“/my/logGroup/”}]`.

- awslogs-stream-prefix: "ecs" - Prefix for log stream names

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --primary-container “awsLogsConfiguration”=[{“logStreamPrefix”=“myprefix”}]`.

The following defaults are set by Express Mode but can be updated in the Task Definition - Log Configuration directly:

- logDriver: "awslogs" - Uses CloudWatch Logs
- awslogs-region: current Region - Uses the same Region as the
  Express Mode service
- mode: "non-blocking" - Logging mode set to non-blocking
- max-buffer-size: "25m" - Maximum buffer size for log writes

## Service defaults

The following defaults are configurable from within Express Mode for the Amazon ECS Service:

- serviceName: Express Mode service → Name - Name of the service (customer provided or derived from the image name)

Name can only be configured on create, and is not available to be configured on updates.

- cluster: Express Mode service → Cluster - ECS cluster for this service (customer provided or default)

Cluster can only be configured on create, and is not available to be configured on updates.

- desiredCount: Express Mode service → MinTasks - Desired count for service (default is 1)

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --scaling-target ‘{“minTaskCount”=3}',`

- tags: Express Mode service Tags for AWS tagging (customer provided)

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --tags`. Tags can only be added on the create of a new resource.

The following defaults are set by Express Mode but can be updated in the Amazon ECS Service directly:

- availabilityZoneRebalancing: true - Enables automatic AZ rebalancing
- CapacityProviderStrategy: {"base": 1, "capacityProvider": "FARGATE", "weight": 1} - Uses Fargate for compute capacity
- deploymentConfiguration: Canary by default - Express Mode service uses Canary deployments

Note that deployment strategy can not be updated on Express Mode services.

- enableECSManagedTags: true - Enables ECS-managed resource tagging
- healthCheckGracePeriodSeconds: 300 - Grace period before Scheduler looks at ELB or Lattice health checks (aligns with ELB health check grace period default)
- launchType: <Not set> - Uses capacity providers
- loadBalancers: Load balancer configuration handled by ECS

Note that load balancer configurations can not be updated on Express Mode services.

- placementStrategy: Not set - Uses Fargate at launch (should always be AZ Spread)
- platformVersion: LATEST - Fargate platform version (hard coded to LATEST)
- propagateTags: "SERVICE" - Propagates tags from the service to tasks
- schedulingStrategy: "REPLICA" - Express Mode services are REPLICA services
- taskDefinition: Express Mode service created - The task definition to use (provided by Express Mode service)

## Network configuration defaults

The following defaults are configurable from within Express Mode for the Amazon ECS Service - Network Configuration:

- networkConfiguration.Subnets: If none are provided, Express Mode will use the default public subnets in the default VPC.

The default VPC must have at least two public subnets, in at least two availability zones, with at least 8 free IPs available, per assigned
CIDR block, per subnet.

If you provide custom public subnets, Express Mode will provision an internet-facing ALB and turn on assignPublicIP for your tasks.
If you provide private subnets (subnets without an internet gateway in their route table), Express Mode will provision an internal ALB.

If you specify subnets, the first Express Mode service for a VPC defines the subnets associated with either the internet-facing or
internal load balancer for that VPC. Subsequent Express Mode services that launch in the same VPC must have subnets that match the availability
zones supported by the load balancer. Because of this, we recommend creating Express Mode services with subnets from all availability zones.

- networkConfiguration.SecurityGroups: If none are provided, Express Mode creates both a Service Security Group and a Load
  Balancer Security Group

The Service Security Group allows outbound traffic to the public internet, but this may be restricted depending on other aspects of your
networking, such as your subnet configuration.

The Load Balancer Security Group The Load Balancer Security Group allows inbound traffic for HTTPS resolution and outbound traffic to
your Service Security Group on the container port you specify (default 80). And is automatically updated to match the container port provided
in your Express Mode Create or Update calls.

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --network-configuration '{"securityGroup": ["sg-xxxxxxx"]}'`. When you provide a security group
you are providing an additional ingress path to your service.

The following defaults are set by Express Mode but can be updated in the Amazon ECS Service - Network Configuration directly:

- assignPublicIp: Based on subnet type - Enabled for public subnets to ensure users of the default VPC are able to access the public internet,
  we enable public IPs on each task by default. This is disabled if you provide a private subnet, and you are then responsible for configuring a NAT gateway
  if your tasks need internet access.

## IAM role defaults

The following IAM roles are configurable for an Express Mode Service with automatic creation of service-linked roles where appropriate.

- executionRoleArn: Task Execution Role (required parameter)

While the required permissions are in the managed policy, additional policies and permissions can be attached. Additional details on the
[AmazonECSTaskExecutionRolePolicy](../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md "../../../aws-managed-policy/latest/reference/AmazonECSTaskExecutionRolePolicy.md") in the AWS Managed Policy Reference Guide

- infrastructureRoleArn: Infrastructure Role for Express Gateway Services (required parameter)

While the required permissions are in the managed policy, additional policies and permissions can be attached. Additional details on the
[AmazonECSInfrastructureRoleforExpressGatewayServices](../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRoleforExpressGatewayServices.md "../../../aws-managed-policy/latest/reference/AmazonECSInfrastructureRoleforExpressGatewayServices.md") Managed Policy in the AWS Managed Policy Reference Guide

- taskRoleArn: Task Role for calls from container application code (optional)

You can customize this option by using the **Additional configurations** option in the console, or by running
`create-express-gateway-service --task-role-arn`.

You must create the new IAM role before you create or update the Express Mode service.

The following IAM roles are configured by Express Mode automatically.

- ecsServiceRoleForECS: Allows Amazon ECS to manage your cluster
- AWSServiceRoleForElasticLoadBalancing: Calls other AWS services for you on your behalf - created automatically by ELB
- AWSServiceRoleForApplicationAutoScaling_ECSService: Calls other AWS services on your behalf - created automatically by Application Auto Scaling

## Application Auto Scaling defaults

The following Application Auto Scaling settings can be configured in Express Mode:

- autoScalingTargetValue: 60 - Target CPU utilization percentage for scaling
- autoScalingMetric: "CPUUtilization" - Metric used for auto scaling decisions
- desiredMinTaskCount: 1 - Minimum number of tasks to maintain
- desiredMaxTaskCount: 20 - Maximum number of tasks to scale to (can be increased or decreased)

The following settings can be conifgured in Application Auto Scaling directly:

- policyType: "TargetTrackingScaling" - Uses target tracking scaling policy
- disableScaleIn: false - Allows scaling down when demand decreases

## Application scaling target defaults

Application Auto Scaling targets define the scalable resource and capacity limits for automatic scaling operations. The following can be modified in Express Mode:

- MaxCapacity: Express Mode service → MaxTasks - Maximum tasks the service will scale up to (default from CreateLoadBalancedService or customer provided)
- MinCapacity: Express Mode service → MinTasks - Minimum tasks the service will scale down to (default from CreateLoadBalancedService or customer provided)
- ScalableDimension: ecs:service:DesiredCount - The property to scale
- Tags: Derived from the tags passed in CreateLoadBalancedService - Resource tags for this resource

The following defaults can be modified in Application Auto Scaling scalable target:

- DynamicScalingInSuspended: false - Indicates if scaling in is suspended
- DynamicScalingOutSuspended: false - Indicates if scaling out is suspended
- ScheduledScalingSuspended: false - Indicates if scheduled scaling is suspended

## Application scaling policy defaults

Scaling policies implement target tracking algorithms that monitor CPU utilization and adjust task count to maintain optimal performance. The following can be modified from Express Mode:

- TargetValue: 60% - The target value for the tracking policy (Express Mode service → scaling-target-value)
- PredefinedMetricType: ECSServiceAverageCPUUtilization - The name type of metric being tracked (Express Mode service → scaling-metric)

Express Mode provides scaling metrics for Average CPUUtilization, Average Memory Utilization, and Request Count per Target. Request Count per Target comes from the Application Load Balancer
and can be set up to 65536 requests per target per second, which is your Amazon ECS Service in the Application Load Balancer target group.

The following defaults are set by Express Mode but can be changed in the Application Auto Scaling policy:

- PolicyName: <ServiceName><"TargetMetric"> - Name of this scaling policy (derived from ECS Service name and Target Metric)
- PolicyType: TargetTrackingScaling - The type of scaling being done (predefined default)
- ScalableDimension: "ecs:service:DesiredCount" - The property to be scaled (predefined default)
- DisableScaleIn: false - Indicates if scale in is disabled

## Application Load Balancer defaults

The following Application Load Balancer defaults can be configured in Express Mode:

- scheme: depends on subnets - Creates an Internet-facing load balancer with public IP addresses when public subnets are provided.
  Creates an Internal load balancer with private IP addresses when private subnets are provided.
- ip-address-type: depends on subnets - Creates an IPv4 only Application Load Balancer when addresses are IPv4. When there are IPv6-enabled subnets,
  a dual-stack Application Load Balancer will be created. Note that if you have IPv6-enabled subnets, the first Express Mode service in a VPC defines the internal or
  internet-facing load balancer for that VPC. Because of this, we recommend creating your IPv6-only subnets first, or in a new VPC.

The following defaults are set in Express Mode and can be configured in Application Load Balancer:

- desync-mitigation-mode: Off - HTTP desync mitigation is disabled
- access-logs.enabled: false - Access logging is disabled
- listener-configurations.protocol: https - Uses HTTPS protocol for secure communication
- listener-configurations.port: 443 - Listens on standard HTTPS port
- listener-configurations.rule-type: host-header - Routes traffic based on host header rules

## Target group defaults

The following Amazon EC2 Target Group defaults can be configured in Express Mode:

- health-check-path: (default "/") Express Mode service health check path - URL path for health check requests
- port: (default 80) - Port on which targets receive traffic
- health-check-port: (default 80) - Port for health check requests

The following defaults are set by Express Mode and can be configured in Amazon EC2 Target Groups:

- protocol: HTTP - Protocol for routing traffic to targets
- protocol-version: HTTP1 - HTTP protocol version for communication
- vpc-id: default is the default VPC - Virtual Private Cloud identifier for the target group, but will be derived from the subnets provided
- health-check-protocol: Same as Protocol - Protocol for health check requests
- health-check-enabled: Always enabled - Health checks are automatically enabled
- health-check-interval-seconds: 30 - Time between health checks of individual targets
- health-check-timeout-seconds: 5 - Timeout duration for health check responses
- healthy-threshold-count: 5 - Consecutive successful health checks required for healthy status
- unhealthy-threshold-count: 2 - Consecutive failed health checks required for unhealthy status
- target-type: ip - Targets are registered by IP address
- ip-address-type: ipv4 - Uses IPv4 addresses for target registration

## Resource sharing and cost optimization

Express Mode services automatically share resources when possible to optimize costs:

- **Load balancer sharing** - Up to 25 Express Mode services in the same VPC can share an Application Load Balancer.
  Express Mode will provision additional Application Load Balancers as necessary depending on the amount of Express Mode services you have provisioned. And as you reduce
  the amount of Express Mode services in your VPC, Express Mode will also deprovision unused Application Load Balancers.This sharing reduces the effective cost per
  application as you deploy more Express Mode services.
- **Cluster sharing** - Express Mode services can be grouped together in Amazon ECS Clusters. Express Mode services
  can also share Amazon ECS Clusters with Amazon ECS Services not managed by Express Mode.
