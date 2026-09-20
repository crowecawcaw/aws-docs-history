

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


<table>
<thead>
  <tr><th>To start a service from</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Clusters</td><td> <ol><li> On the <b>Clusters</b> page, select the cluster to create the service in. </li><li> From the <b>Services</b> tab, choose <b>Create</b>. </li></ol> </td><td></td></tr>
  <tr><td>Task definition</td><td> <ol><li> On the <b>Task definitions</b> page, select the option button next to the task definition. </li><li> On the <b>Deploy</b> menu, choose <b>Create service</b>. </li></ol> </td><td></td></tr>
</tbody>
</table>


   The **Create service** page appears.

1. Under Service details, do the following:

   1. For **Task definition**, enter the task definition to use. Then, for **Revision**, choose the revision to use.

   1. For **Service name**, enter a name for your service.

1. For **Existing cluster**, choose the cluster.

   Choose **Create cluster** to run the task on a new cluster

1. Choose how your tasks are distributed across your cluster infrastructure. Under **Compute configuration**, choose your option.


<table>
<thead>
  <tr><th>Compute option</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Capacity provider strategy</td><td> <ol><li> Under <b>Compute options</b>, choose <b>Capacity provider strategy</b>. </li><li> Choose a strategy: <ul><li> To use the cluster's default capacity provider strategy, choose <b>Use cluster default</b>. </li><li> If your cluster doesn't have a default capacity provider strategy, or to use a custom strategy, choose <b>Use custom</b>, <b>Add capacity provider strategy</b>, and then define your custom capacity provider strategy by specifying a <b>Base</b>, <b>Capacity provider</b>, and <b>Weight</b>. </li></ul> </li></ol>  To use a capacity provider in a strategy, the capacity provider must be associated with the cluster.   </td><td></td></tr>
  <tr><td>Launch type</td><td> <ol><li> In the <b>Compute options</b> section, select <b>Launch type</b>. </li><li> For <b>Launch type</b>, choose a launch type. </li><li> (Optional) When you use Fargate, for <b>Platform version</b>, specify the platform version to use. If a platform version isn't specified, the <code>LATEST</code> platform version is used. </li></ol> </td><td></td></tr>
</tbody>
</table>


1. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.

1. Under **Deployment configuration**, do the following:

   1. For **Service type**, choose the service scheduling strategy.
      + To have the scheduler deploy exactly one task on each active container instance that meets all of the task placement constraints, choose **Daemon**.
      + To have the scheduler place and maintain the desired number of tasks in your cluster, choose **Replica**.

   1. If you chose **Replica**, for **Desired tasks**, enter the number of tasks to launch and maintain in the service.

   1. If you chose **Replica**, to have Amazon ECS monitor the distribution of tasks across Availability Zones, and redistribute them when there is an imbalance, under **Availability Zone service rebalancing**, select **Availability Zone service rebalancing**.

   1. For **Health check grace period**, enter the amount of time (in seconds) that the enter the amount of time (in seconds) that the service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used.

   1. Determine the deployment type for your service. Expand **Deployment options**, and then specify the following parameters.


<table>
<thead>
  <tr><th>Deployment type</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Rolling update</td><td> <ol><li> For <b>Min running tasks</b>, enter the lower limit on the number of tasks in the service that must remain in the <code>RUNNING</code> state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer). For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html#sd-deploymentconfiguration">Deployment configuration</a>. </li><li> For <b>Max running tasks</b>, enter the upper limit on the number of tasks in the service that are allowed in the <code>RUNNING</code> or <code>PENDING</code> state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer). </li></ol> </td><td></td></tr>
</tbody>
</table>


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


<table>
<thead>
  <tr><th>To use this load balancer</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Application Load Balancer</td><td> <ol><li> For <b>Load balancer type</b>, select <b>Application Load Balancer</b>. </li><li> Choose <b>Create a new load balancer</b> to create a new Application Load Balancer or <b>Use an existing load balancer</b> to select an existing Application Load Balancer. </li><li> For <b>Load balancer name</b>, enter a unique name. </li><li> For <b>Choose container to load balance</b>, choose the container that hosts the service. </li><li> For <b>Listener</b>, enter a port and protocol for the Application Load Balancer to listen for connection requests on. By default, the load balancer will be configured to use port 80 and HTTP. </li><li> For <b>Target group name</b>, enter a name and a protocol for the target group that the Application Load Balancer routes requests to. By default, the target group routes requests to the first container defined in your task definition. </li><li> For <b>Degregistration delay</b>, enter the number of seconds for the load balancer to change the target state to <code>UNUSED</code>. The default is 300 seconds. </li><li> For <b>Health check path</b>, enter an existing path within your container where the Application Load Balancer periodically sends requests to verify the connection health between the Application Load Balancer and the container. The default is the root directory (<code>/</code>). </li></ol></td><td></td></tr>
  <tr><td>Network Load Balancer</td><td> <ol><li> For <b>Load balancer type</b>, select <b>Network Load Balancer</b>. </li><li> For <b>Load Balancer</b>, choose an existing Network Load Balancer. </li><li> For <b>Choose container to load balance</b>, choose the container that hosts the service. </li><li> For <b>Target group name</b>, enter a name and a protocol for the target group that the Network Load Balancer routes requests to. By default, the target group routes requests to the first container defined in your task definition. </li><li> For <b>Degregistration delay</b>, enter the number of seconds for the load balancer to change the target state to <code>UNUSED</code>. The default is 300 seconds. </li><li> For <b>Health check path</b>, enter an existing path within your container where the Network Load Balancer periodically sends requests to verify the connection health between the Application Load Balancer and the container. The default is the root directory (<code>/</code>). </li></ol> </td><td></td></tr>
</tbody>
</table>


1. (Optional) To configure service Auto Scaling, expand **Service auto scaling**, and then specify the following parameters.To use predicte auto scaling, which looks at past load data from traffic flows, configure it after you create the service. For more information, see [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md).

   1. To use service auto scaling, select **Service auto scaling**.

   1. For **Minimum number of tasks**, enter the lower limit of the number of tasks for service auto scaling to use. The desired count will not go below this count.

   1. For **Maximum number of tasks**, enter the upper limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.

   1. Choose the policy type. Under **Scaling policy type**, choose one of the following options.


<table>
<thead>
  <tr><th>To use this policy type</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Target tracking</td><td> <ol><li> For <b>Scaling policy type</b>, choose <b>Target tracking</b>. </li><li> For <b>Policy name</b>, enter the name of the policy. </li><li> For <b>ECS service metric</b>, select one of the following metrics. <ul><li>  <b>ECSServiceAverageCPUUtilization</b> – Average CPU utilization of the service.  </li><li> <b>ECSServiceAverageMemoryUtilization</b> – Average memory utilization of the service.  </li><li> <b>ALBRequestCountPerTarget</b> – Number of requests completed per target in an Application Load Balancer target group.  </li></ul> </li><li> For <b>Target value</b>, enter the value the service maintains for the selected metric. </li><li> For <b>Scale-out cooldown period</b>, enter the amount of time, in seconds, after a scale-out activity (add tasks) that must pass before another scale-out activity can start. </li><li> For <b>Scale-in cooldown period</b>, enter the amount of time, in seconds, after a scale-in activity (remove tasks) that must pass before another scale-in activity can start. </li><li> To prevent the policy from performing a scale-in activity, select <b>Turn off scale-in</b>. </li><li> • (Optional) Select <b>Turn off scale-in</b> if you want your scaling policy to scale out for increased traffic but don’t need it to scale in when traffic decreases. </li></ol></td><td></td></tr>
  <tr><td>Step scaling </td><td> <ol><li> For <b>Scaling policy type</b>, choose <b>Step scaling</b>. </li><li> For <b>Policy name</b>, enter the policy name. </li><li> For <b>Alarm name</b>, enter a unique name for the alarm. </li><li> For <b>Amazon ECS service metric</b>, choose the metric to use for the alarm. </li><li> For <b>Statistic</b>, choose the alarm statistic. </li><li> For <b>Period</b>, choose the period for the alarm. </li><li> For <b>Alarm condition</b>, choose how to compare the selected metric to the defined threshold. </li><li> For <b>Threshold to compare metrics</b> and <b>Evaluation period to initiate alarm</b>, enter the threshold used for the alarm and how long to evaluate the threshold. </li><li> Under <b>Scaling actions</b>, do the following: <ul><li> For <b>Action</b>, select whether to add, remove, or set a specific desired count for your service. </li><li> If you chose to add or remove tasks, for <b>Value</b>, enter the number of tasks (or percent of existing tasks) to add or remove when the scaling action is initiated. If you chose to set the desired count, enter the number of tasks. For <b>Type</b>, select whether the <b>Value</b> is an integer or a percent value of the existing desired count. </li><li>  For <b>Lower bound</b> and <b>Upper bound</b>, enter the lower boundary and upper boundary of your step scaling adjustment. By default, the lower bound for an add policy is the alarm threshold and the upper bound is positive (+) infinity. By default, the upper bound for a remove policy is the alarm threshold and the lower bound is negative (-) infinity. </li><li> (Optional) Add additional scaling options. Choose <b>Add new scaling action</b>, and then repeat the <b>Scaling actions</b> steps. </li><li> For <b>Cooldown period</b>, enter the amount of time, in seconds, to wait for a previous scaling activity to take effect. For an add policy, this is the time after a scale-out activity that the scaling policy blocks scale-in activities and limits how many tasks can be scale out at a time. For a remove policy, this is the time after a scale-in activity that must pass before another scale-in activity can start.  </li></ul> </li></ol> </td><td></td></tr>
</tbody>
</table>


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


<table>
<thead>
  <tr><th>To configure this volume type</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Amazon EBS</td><td> <ol><li> For <b>EBS volume type</b>, choose the type of EBS volume that you want to attach to your task. </li><li> For <b>Size (GiB)</b>, enter a valid value for the volume size in gibibytes (GiB). You can specify a minimum of 1 GiB and a maximum of 16,384 GiB volume size. This value is required unless you provide a snapshot ID.  </li><li> For <b>IOPS</b>, enter the maximum number of input/output operations (IOPS) that the volume should provide. This value is configurable only for <code>io1</code>,<code>io2</code>, and <code>gp3</code> volume types. </li><li> For <b>Throughput (MiB/s)</b>, enter the throughput that the volume should provide, in mebibytes per second (MiBps, or MiB/s). This value is configurable only for the <code>gp3</code> volume type. </li><li> For <b>Snapshot ID</b>, choose an existing Amazon EBS volume snapshot or enter the ARN of a snapshot if you want to create a volume from a snapshot. You can also create a new, empty volume by not choosing or entering a snapshot ID. </li><li> If you specify a <b>Snapshot ID</b>, you can specify a <b>Volume initialization rate (MiB/s)</b>. Enter a value between 100 and 300, in MiB/s, that will determine how fast data is loaded from the snapshot specified using <b>Snapshot ID</b> for volume creation. </li><li> For <b>File system type</b>, choose the type of file system that will be used for data storage and retrieval on the volume. You can choose either the operating system default or a specific file system type. The default for Linux is <code>XFS</code>. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start. </li><li> For <b>Infrastructure role</b>, choose an IAM role with the necessary permissions that allow Amazon ECS to manage Amazon EBS volumes for tasks. You can attach the <code>AmazonECSInfrastructureRolePolicyForVolumes</code> managed policy to the role, or you can use the policy as a guide to create and attach an your own policy with permissions that meet your specific needs. For more information about the necessary permissions, see <a href="infrastructure_IAM_role.md">Amazon ECS infrastructure IAM role</a>. </li><li> For <b>Encryption</b>, choose <b>Default</b> if you want to use the Amazon EBS encryption by default settings. If your account has <a href="https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html">Encryption by default</a> configured, the volume will be encrypted with the AWS Key Management Service (AWS KMS) key that's specified in the setting. If you choose <b>Default</b> and Amazon EBS default encryption isn't turned on, the volume will be unencrypted.  <br />If you choose <b>Custom</b>, you can specify an AWS KMS key of your choice for volume encryption.  <br />If you choose <b>None</b>, the volume will be unencrypted unless you have encryption by default configured, or if you create a volume from an encrypted snapshot.  </li><li> If you've chosen <b>Custom</b> for <b>Encryption</b>, you must specify the AWS KMS key that you want to use. For <b>KMS key</b>, choose an AWS KMS key or enter a key ARN. If you choose to encrypt your volume by using a symmetric customer managed key, make sure that you have the right permissions defined in your AWS KMS key policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html?icmpid=docs_ecs_hp-deploy#ebs-kms-encryption">Data encryption for Amazon EBS volumes</a>.  </li><li> (Optional) Under <b>Tags</b>, you can add tags to your Amazon EBS volume by either propagating tags from the task definition or service, or by providing your own tags. <br /> If you want to propagate tags from the task definition, choose <b>Task definition</b> for <b>Propagate tags from</b>. If you want to propagate tags from the service, choose <b>Service</b> for <b>Propagate tags from</b>. If you choose <b>Do not propagate</b>, or if you don't choose a value, the tags aren't propagated. <br />If you want to provide your own tags, choose <b>Add tag</b> and then provide the key and value for each tag you add. <br />For more information about tagging Amazon EBS volumes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-ebs-config.html#ebs-volume-tagging">Tagging Amazon EBS volumes</a>. </li></ol></td><td></td></tr>
</tbody>
</table>


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