

# Creating an Amazon ECS rolling update deployment
<a name="create-service-console-v2"></a>

Create a service to run and maintain a specified number of instances of a task definition simultaneously in a cluster. If one of your tasks fails or stops, the Amazon ECS service scheduler launches another instance of your task definition to replace it. This helps maintain your desired number of tasks in the service.

Decide on the following configuration parameters before you create a service:
+ There are two compute options that distribute your tasks.
  + A **capacity provider strategy** causes Amazon ECS to distribute your tasks in one or across multiple capacity providers. 

    If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.
  + A **launch type** causes Amazon ECS to launch our tasks directly on either Fargate or on the EC2 instances registered to your clusters.

    If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.
+ Task definitions that use the `awsvpc` network mode or services configured to use a load balancer must have a networking configuration. By default, the console selects the default Amazon VPC along with all subnets and the default security group within the default Amazon VPC. 
+ The placement strategy, The default task placement strategy distributes tasks evenly across Availability Zones. 

  We recommend that you use Availability Zone rebalancing to help ensure high availability for your service. For more information, see [Balancing an Amazon ECS service across Availability Zones](service-rebalancing.md).
+ When you use the **Launch Type** for your service deployment, by default the service starts in the subnets in your cluster VPC.
+ For the **capacity provider strategy**, the console selects a compute option by default. The following describes the order that the console uses to select a default:
  + If your cluster has a default capacity provider strategy defined, it is selected.
  + If your cluster doesn't have a default capacity provider strategy defined but you have the Fargate capacity providers added to the cluster, a custom capacity provider strategy that uses the `FARGATE` capacity provider is selected.
  + If your cluster doesn't have a default capacity provider strategy defined but you have one or more Auto Scaling group capacity providers added to the cluster, the **Use custom (Advanced)** option is selected and you need to manually define the strategy.
  + If your cluster doesn't have a default capacity provider strategy defined and no capacity providers added to the cluster, the Fargate launch type is selected.
+ The default deployment failure detection default options are to use the **Amazon ECS deployment circuit breaker** option with the **Rollback on failures** option.

  For more information, see [How the Amazon ECS deployment circuit breaker detects failures](deployment-circuit-breaker.md).
+ Decide if you want Amazon ECS to increase or decrease the desired number of tasks in your service automatically. For information see, [Automatically scale your Amazon ECS service](service-auto-scaling.md).
+ If you need an application to connect to other applications that run in Amazon ECS, determine the option that fits your architecture. For more information, see [Interconnect Amazon ECS services](interconnecting-services.md). 
+ When you create a service that uses Amazon ECS circuit breaker, Amazon ECS creates a service deployment and a service revision. These resources allow you to view detailed information about the service history. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md).

  For information about how to create a service using the AWS CLI, see [create-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/create-service.html) in the *AWS Command Line Interface Reference*.

  For information about how to create a service using AWS CloudFormation, see [AWS::ECS::Service](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.html) in the *AWS CloudFormation User Guide*.

## Create a service with the default options
<a name="create-default-service"></a>

You can use the console to quickly create and deploy a service. The service has the following configuration:
+ Deploys in the VPC and subnets associated with your cluster
+ Deploys one task
+ Uses the rolling deployment
+ Uses the capacity provider strategy with your default capacity provider
+ Uses the deployment circuit breaker to detect failures and sets the option to automatically roll back the deployment on failure

To deploy a service using the default parameters follow these steps.

**To create a service (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation page, choose **Clusters**.

1. On the **Clusters** page, choose the cluster to create the service in.

1. From the **Services** tab, choose **Create**.

   The **Create service** page appears.

1. Under **Service details**, do the following:

   1. For **Task definition**, enter the task definition family and revision to use.

   1. For **Service name**, enter a name for your service.

1. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.

1. Under **Deployment configuration**, do the following:

   1. For **Desired tasks**, enter the number of tasks to launch and maintain in the service.

1. (Optional) To help identify your service and tasks, expand the **Tags** section, and then configure your tags.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the task definition tags, select **Turn on Amazon ECS managed tags**, and then select **Task definitions**.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the service tags, select **Turn on Amazon ECS managed tags**, and then select **Service**.

   Add or remove a tag.
   + [Add a tag] Choose **Add tag**, and then do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

## Create a service using defined parameters
<a name="create-custom-service"></a>

To create a service by using defined parameters, follow these steps.

**To create a service (Amazon ECS console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Determine the resource from where you launch the service.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

   The **Create service** page appears.

1. Under Service details, do the following:

   1. For **Task definition**, enter the task definition to use. Then, for **Revision**, choose the revision to use.

   1. For **Service name**, enter a name for your service.

1. For **Existing cluster**, choose the cluster.

   Choose **Create cluster** to run the task on a new cluster

1. Choose how your tasks are distributed across your cluster infrastructure. Under **Compute configuration**, choose your option.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

1. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.

1. Under **Deployment configuration**, do the following:

   1. For **Service type**, choose the service scheduling strategy.
      + To have the scheduler deploy exactly one task on each active container instance that meets all of the task placement constraints, choose **Daemon**.
      + To have the scheduler place and maintain the desired number of tasks in your cluster, choose **Replica**.

   1. If you chose **Replica**, for **Desired tasks**, enter the number of tasks to launch and maintain in the service.

   1. If you chose **Replica**, to have Amazon ECS monitor the distribution of tasks across Availability Zones, and redistribute them when there is an imbalance, under **Availability Zone service rebalancing**, select **Availability Zone service rebalancing**.

   1. For **Health check grace period**, enter the amount of time (in seconds) that the enter the amount of time (in seconds) that the service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used.

   1. Determine the deployment type for your service. Expand **Deployment options**, and then specify the following parameters.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

   1. Under **Deployment configuration**, to complete the deployment before the target service revision reaches the full desired count, configure early success criteria. You can also choose when Amazon ECS cleans up the tasks on the source service revision.

      1. Turn on **Early success criteria**.

      1. For **Healthy percent**, enter the percentage of tasks that must be running and healthy on the target service revision before Amazon ECS completes the deployment.

      1. For **Source service revision cleanup**, choose **Blocking** or **Deferred**.

   1. To configure how Amazon ECS detects and handles deployment failures, expand **Deployment failure detection**, and then choose your options. 

      1. To stop a deployment when the tasks cannot start, select **Use the Amazon ECS deployment circuit breaker**.

         To have the software automatically roll back the deployment to the last completed deployment state when the deployment circuit breaker sets the deployment to a failed state, select **Rollback on failures**.

      1. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**. Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm, go to the CloudWatch console.

         To have the software automatically roll back the deployment to the last completed deployment state when a CloudWatch alarm sets the deployment to a failed state, select **Rollback on failures**.

1. If your task definition uses the `awsvpc` network mode, you can specify a custom network configuration expand **Networking**, and then do the following:

   1. For **VPC**, select the VPC to use.

   1. For **Subnets**, select one or more subnets in the VPC that the task scheduler considers when placing your tasks.

   1. For **Security group**, you can either select an existing security group or create a new one. To use an existing security group, select the security group and move to the next step. To create a new security group, choose **Create a new security group**. You must specify a security group name, description, and then add one or more inbound rules for the security group.

   1. For **Public IP**, choose whether to auto-assign a public IP address to the elastic network interface (ENI) of the task.

      AWS Fargate tasks can be assigned a public IP address when run in a public subnet so they have a route to the internet. EC2 tasks can't be assigned a public IP using this field. For more information, see [Amazon ECS task networking options for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html) and [Allocate a network interface for an Amazon ECS task](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html).

1. (Optional) To interconnect your service using Service Connect, expand **Service Connect**, and then specify the following:

   1.  Select **Turn on Service Connect**.

   1. Under **Service Connect configuration**, specify the client mode.
      + If your service runs a network client application that only needs to connect to other services in the namespace, choose **Client side only**.
      + If your service runs a network or web service application and needs to provide endpoints for this service, and connects to other services in the namespace, choose **Client and server**.

   1. To use a namespace that is not the default cluster namespace, for **Namespace**, choose the service namespace. This can be a namespace created separately in the same AWS Region in your AWS account or a namespace in the same Region that is shared with your account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the *AWS Cloud Map Developer Guide*.

   1. (Optional) Specify a log configuration. Select **Use log collection**. The default option sends container logs to CloudWatch Logs. The other log driver options are configured using AWS FireLens. For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md).

      The following describes each container log destination in more detail.
      + **Amazon CloudWatch** – Configure the task to send container logs to CloudWatch Logs. The default log driver options are provided, which create a CloudWatch log group on your behalf. To specify a different log group name, change the driver option values.
      + **Amazon Data Firehose** – Configure the task to send container logs to Firehose. The default log driver options are provided, which send logs to a Firehose delivery stream. To specify a different delivery stream name, change the driver option values.
      + **Amazon Kinesis Data Streams** – Configure the task to send container logs to Kinesis Data Streams. The default log driver options are provided, which send logs to an Kinesis Data Streams stream. To specify a different stream name, change the driver option values.
      + **Amazon OpenSearch Service** – Configure the task to send container logs to an OpenSearch Service domain. The log driver options must be provided. 
      + **Amazon S3** – Configure the task to send container logs to an Amazon S3 bucket. The default log driver options are set by default, but you must specify a valid Amazon S3 bucket name.

   1. (Optional) To enable access logs, follow these steps:

      1. Expand **Access log configuration**. For **Format**, choose either **JSON** or `TEXT`.

      1. To include query parameters in access logs, select **Include query parameters**.

1. (Optional) To interconnect your service using Service Discovery, expand **Service discovery**, and then do the following.

   1. Select **Use service discovery**.

   1. To use a new namespace, choose **Create a new namespace** under **Configure namespace**, and then provide a namespace name and description. To use an existing namespace, choose **Select an existing namespace** and then choose the namespace that you want to use.

   1. Provide Service Discovery service information such as the service's name and description.

   1. To have Amazon ECS perform periodic container-level health checks, select **Enable Amazon ECS task health propagation**.

   1. For **DNS record type**, select the DNS record type to create for your service. Amazon ECS service discovery only supports **A** and **SRV** records, depending on the network mode that your task definition specifies. For more information about these record types, see [Supported DNS Record Types](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html) in the *Amazon Route 53 Developer Guide*.
      + If the task definition that your service task specifies uses the `bridge` or `host` network mode, only type **SRV** records are supported. Choose a container name and port combination to associate with the record.
      + If the task definition that your service task specifies uses the `awsvpc` network mode, select either the **A** or **SRV** record type. If you choose **A**, skip to the next step. If you choose **SRV**, specify either the port that the service can be found on or a container name and port combination to associate with the record.

      For **TTL**, enter the time in seconds how long a record set is cached by DNS resolvers and by web browsers.

1. (Optional) To interconnect your service using VPC Lattice, xxpand **VPC Lattice**, and then do the following:

   1. Select **Turn on VPC Lattice**

   1. For **Infrastructure role**, choose the infrastructure role.

      If you haven't created a role, choose **Create infrastructure role**.

   1. Under **Target Groups** choose the target group or groups. You need to choose at least one target group and can have a maximum of five. Choose **Add target group** to add additional target groups. Choose the **Port name**, **Protocol**, and **Port** for each target group you chose. 

      To delete a target group, choose **Remove**.
**Note**  
If you want to add existing target groups, you need use the AWS CLI. For instructions on how to add target groups using the AWS CLI, see [register-targets ](https://docs.aws.amazon.com/cli/latest/reference/vpc-lattice/register-targets.html) in the* AWS Command Line Interface Reference*.
While a VPC Lattice service can have multiple target groups, each target group can only be added to one service.

   1. To complete the VPC Lattice configuration, by including your new target groups in the listener default action or in the rules of an existing VPC Lattice service in the VPC Lattice console. For more information, see [Listener rules for your VPC Lattice service](https://docs.aws.amazon.com/vpc-lattice/latest/ug/listener-rules.html).

1. (Optional) To configure a load balancer for your service, expand **Load balancing**.

   Choose the load balancer.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

1. (Optional) To configure service Auto Scaling, expand **Service auto scaling**, and then specify the following parameters.To use predicte auto scaling, which looks at past load data from traffic flows, configure it after you create the service. For more information, see [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md).

   1. To use service auto scaling, select **Service auto scaling**.

   1. For **Minimum number of tasks**, enter the lower limit of the number of tasks for service auto scaling to use. The desired count will not go below this count.

   1. For **Maximum number of tasks**, enter the upper limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.

   1. Choose the policy type. Under **Scaling policy type**, choose one of the following options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

1. (Optional) To use a task placement strategy other than the default, expand **Task Placement**, and then choose from the following options.

    For more information, see [How Amazon ECS places tasks on container instances](task-placement.md).
   + **AZ Balanced Spread** – Distribute tasks across Availability Zones and across container instances in the Availability Zone.
   + **AZ Balanced BinPack** – Distribute tasks across Availability Zones and across container instances with the least available memory.
   + **BinPack** – Distribute tasks based on the least available amount of CPU or memory.
   + **One Task Per Host** – Place, at most, one task from the service on each container instance.
   + **Custom** – Define your own task placement strategy. 

   If you chose **Custom**, define the algorithm for placing tasks and the rules that are considered during task placement.
   + Under **Strategy**, for **Type** and **Field**, choose the algorithm and the entity to use for the algorithm.

     You can enter a maximum of 5 strategies.
   + Under **Constraint**, for **Type** and **Expression**, choose the rule and attribute for the constraint.

     For example, to set the constraint to place tasks on T2 instances, for the **Expression**, enter **attribute:ecs.instance-type =\~ t2.\***.

     You can enter a maximum of 10 constraints.

1. If your task uses a data volume that's compatible with configuration at deployment, you can configure the volume by expanding **Volume**.

   The volume name and volume type are configured when you create a task definition revision and can't be changed when creating a service. To update the volume name and type, you must create a new task definition revision and create a service by using the new revision.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-service-console-v2.html)

1. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.

1. (Optional) To help identify your service and tasks, expand the **Tags** section, and then configure your tags.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the task definition tags, select **Turn on Amazon ECS managed tags**, and then for **Propagate tags from**, choose **Task definitions**.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the service tags, select **Turn on Amazon ECS managed tags**, and then for **Propagate tags from**, choose **Service**.

   Add or remove a tag.
   + [Add a tag] Choose **Add tag**, and then do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create**.

## Next steps
<a name="create-service-next-steps"></a>

The following are additional actions after you create a service.
+ Configure predicte auto scaling, which looks at past load data from traffic flows. For more information, see [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md).
+ Track your deployment and view your service history for services that Amazon ECS circuit breaker. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md).