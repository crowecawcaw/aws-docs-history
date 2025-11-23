# Creating an Amazon ECS rolling update

deployment

Create a service to run and maintain a specified number of instances of a task definition
simultaneously in a cluster. If one of your tasks fails or stops, the Amazon ECS service
scheduler launches another instance of your task definition to replace it. This helps
maintain your desired number of tasks in the service.

Decide on the following configuration parameters before you create a service:

- There are two compute options that distribute your tasks.
  - A **capacity provider strategy** causes Amazon ECS to
    distribute your tasks in one or across multiple capacity providers.

  If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.
  - A **launch type** causes Amazon ECS to launch our tasks
    directly on either Fargate or on the EC2 instances registered to your
    clusters.

  If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.

- Task definitions that use the `awsvpc` network mode or services
  configured to use a load balancer must have a networking configuration. By default,
  the console selects the default Amazon VPC along with all subnets and the default
  security group within the default Amazon VPC.
- The placement strategy, The default task placement strategy distributes tasks
  evenly across Availability Zones.

We recommend that you use Availability Zone rebalancing to help ensure high availability
for your service. For more information, see [Balancing an Amazon ECS service across Availability
Zones](service-rebalancing.md "service-rebalancing.md").

- When you use the **Launch Type** for your service deployment, by
  default the service starts in the subnets in your cluster VPC.
- For the **capacity provider strategy**, the console selects a
  compute option by default. The following describes the order that the console uses
  to select a default:
  - If your cluster has a default capacity provider strategy defined, it is
    selected.
  - If your cluster doesn't have a default capacity provider strategy defined
    but you have the Fargate capacity providers added to the
    cluster, a custom capacity provider strategy that uses the
    `FARGATE` capacity provider is selected.
  - If your cluster doesn't have a default capacity provider strategy defined
    but you have one or more Amazon EC2 Auto Scaling group capacity providers added to the cluster, the
    **Use custom (Advanced)** option is selected and you
    need to manually define the strategy.
  - If your cluster doesn't have a default capacity provider strategy defined
    and no capacity providers added to the cluster, the Fargate
    launch type is selected.

- The default deployment failure detection default options are to use the
  **Amazon ECS deployment circuit breaker** option with the
  **Rollback on failures** option.

For more information, see [How the Amazon ECS deployment circuit breaker
detects failures](deployment-circuit-breaker.md "deployment-circuit-breaker.md").

- Decide if you want Amazon ECS to increase or decrease the desired number of tasks in
  your service automatically. For information see, [Automatically scale your Amazon ECS service](service-auto-scaling.md "service-auto-scaling.md").
- If you need an application to connect to other applications that run in Amazon ECS,
  determine the option that fits your architecture. For more information, see [Interconnect Amazon ECS services](interconnecting-services.md "interconnecting-services.md").
- When you create a service that uses Amazon ECS circuit breaker, Amazon ECS creates a service
  deployment and a service revision. These resources allow you to view detailed
  information about the service history. For more information, see [View service history using Amazon ECS service
  deployments](service-deployment.md "service-deployment.md").

For information about how to create a service using the AWS CLI, see [create-service](../../../cli/latest/reference/ecs/create-service.md "../../../cli/latest/reference/ecs/create-service.md") in the _AWS Command Line Interface Reference_.

For information about how to create a service using AWS CloudFormation, see [AWS::ECS::Service](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ecs-service.md") in the _AWS CloudFormation User Guide_.

## Create a service with the default

options

You can use the console to quickly create and deploy a service. The service has the
following configuration:

- Deploys in the VPC and subnets associated with your cluster
- Deploys one task
- Uses the rolling deployment
- Uses the capacity provider strategy with your default capacity provider
- Uses the deployment circuit breaker to detect failures and sets the option to
  automatically roll back the deployment on failure

To deploy a service using the default parameters follow these steps.

###### To create a service (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation page, choose **Clusters**.
3. On the **Clusters** page, choose the cluster to create the
   service in.
4. From the **Services** tab, choose
   **Create**.

The **Create service** page appears. 5. Under **Service details**, do the following:

    1. For **Task definition**, enter the task definition
     family and revision to use.
    2. For **Service name**, enter a name for your
     service.

6. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.
7. Under **Deployment configuration**, do the following:
   1. For **Desired tasks**, enter the number of tasks to
      launch and maintain in the service.

8. (Optional) To help identify your service and tasks, expand the
   **Tags** section, and then configure your tags.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the task definition tags, select **Turn on Amazon ECS managed
tags**, and then select **Task
definitions**.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the service tags, select **Turn on Amazon ECS managed tags**,
and then select **Service**.

Add or remove a tag.

    * [Add a tag] Choose **Add tag**, and then do the
     following:




    	+ For **Key**, enter the key name.
    	+ For **Value**, enter the key value.
    * [Remove a tag] Next to the tag, choose **Remove
     tag**.

## Create a service using defined

parameters

To create a service by using defined parameters, follow these steps.

###### To create a service (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Determine the resource from where you launch the service.

| To start a service from | Steps                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clusters                | 1. On the **Clusters\*<br>• page, select<br>the cluster to create the service in.<br>2. From the **Services\*<br>• tab, choose<br>**Create**.                          |
| Task definition         | 1. On the **Task definitions\*<br>• page,<br>select the option button next to the task<br>definition.<br>2. On the **Deploy\*<br>• menu, choose<br>**Create service**. |

The **Create service** page appears. 3. Under Service details, do the following:

    1. For **Task definition**, enter the task definition to
     use. Then, for **Revision**, choose the revision to
     use.
    2. For **Service name**, enter a name for your
     service.

4. For **Existing cluster**, choose the cluster.

Choose **Create cluster** to run the task on a new
cluster 5. Choose how your tasks are distributed across your cluster infrastructure.
Under **Compute configuration**, choose your option.

| Compute option             | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capacity provider strategy | 1. Under **Compute options**, choose<br>**Capacity provider<br>strategy**.<br>2. Choose a strategy:<br>• To use the cluster's default capacity<br>provider strategy, choose **Use cluster<br>default**.<br>• If your cluster doesn't have a default<br>capacity provider strategy, or to use a custom<br>strategy, choose **Use custom**,<br>**Add capacity provider<br>strategy**, and then define your custom<br>capacity provider strategy by specifying a<br>**Base**, **Capacity<br>provider**, and<br>**Weight**.<br>NoteTo use a capacity provider in a strategy, the capacity<br>provider must be associated with the cluster. |
| Launch type                | 1. In the **Compute options**<br>section, select **Launch<br>type**.<br>2. For **Launch type**, choose a<br>launch type.<br>3. (Optional) When you use Fargate,<br>for **Platform<br>version**, specify the platform version to<br>use. If a platform version isn't specified, the<br>`LATEST` platform version is<br>used.                                                                                                                                                                                                                                                                                                            |

6.  To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.
7.  Under **Deployment configuration**, do the following:
    1. For **Service type**, choose the service scheduling
       strategy.
       - To have the scheduler deploy exactly one task on each active
         container instance that meets all of the task placement
         constraints, choose **Daemon**.
       - To have the scheduler place and maintain the desired number of
         tasks in your cluster, choose
         **Replica**.

    2. If you chose **Replica**, for **Desired
       tasks**, enter the number of tasks to launch and maintain
       in the service.
    3. If you chose **Replica**, to have Amazon ECS monitor the
       distribution of tasks across Availability Zones, and redistribute them
       when there is an imbalance, under **Availability Zone service
       rebalancing**, select **Availability Zone service
       rebalancing**.
    4. For **Health check grace period**, enter the amount
       of time (in seconds) that the enter the amount of time (in seconds) that
       the service scheduler ignores unhealthy ELB, VPC Lattice, and container
       health checks after a task has first started. If you do not specify a
       health check grace period value, the default value of 0 is used.
    5. Determine the deployment type for your service. Expand
       **Deployment options**, and then specify the
       following parameters.

    | Deployment type | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
    | --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Rolling update  | 1. For **Min running tasks**,<br>enter the lower limit on the number of tasks in<br>the service that must remain in the<br>`RUNNING` state during a deployment, as<br>a percentage of the desired number of tasks<br>(rounded up to the nearest integer). For more<br>information, see [Deployment configuration](service_definition_parameters.md#sd-deploymentconfiguration "service_definition_parameters.md#sd-deploymentconfiguration").<br>2. For **Max running tasks**,<br>enter the upper limit on the number of tasks in<br>the service that are allowed in the<br>`RUNNING` or `PENDING` state<br>during a deployment, as a percentage of the<br>desired number of tasks (rounded down to the<br>nearest integer). |
    6. To configure how Amazon ECS detects and handles deployment failures, expand
       **Deployment failure detection**, and then choose
       your options.
       1. To stop a deployment when the tasks cannot start, select **Use the Amazon ECS
          deployment circuit breaker**.

       To have the software automatically roll back the deployment to the last
       completed deployment state when the deployment circuit breaker sets the
       deployment to a failed state, select **Rollback on
       failures**. 2. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**.
       Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm,
       go to the CloudWatch console.

       To have the software automatically roll back the deployment to the last
       completed deployment state when a CloudWatch alarm sets the
       deployment to a failed state, select **Rollback on
       failures**.

8.  If your task definition uses the `awsvpc` network mode, you can
    specify a custom network configuration expand **Networking**,
    and then do the following:
    1. For **VPC**, select the VPC to use.
    2. For **Subnets**, select one or more subnets in the
       VPC that the task scheduler considers when placing your tasks.
    3. For **Security group**, you can either select an
       existing security group or create a new one. To use an existing security
       group, select the security group and move to the next step. To create a
       new security group, choose **Create a new security
       group**. You must specify a security group name,
       description, and then add one or more inbound rules for the security
       group.
    4. For **Public IP**, choose whether to auto-assign a
       public IP address to the elastic network interface (ENI) of the
       task.

    AWS Fargate tasks can be assigned a public IP address when run in a
    public subnet so they have a route to the internet. EC2
    tasks can't be assigned a public IP using this field. For more
    information, see [Amazon ECS task networking options for Fargate](fargate-task-networking.md "fargate-task-networking.md")
    and [Allocate a network interface for an Amazon ECS task](task-networking-awsvpc.md "task-networking-awsvpc.md").

9.  (Optional) To interconnect your service using Service Connect, expand
    **Service Connect**, and then specify the
    following:
    1. Select **Turn on Service Connect**.
    2. Under **Service Connect configuration**, specify the
       client mode.
       - If your service runs a network client application that only
         needs to connect to other services in the namespace, choose
         **Client side only**.
       - If your service runs a network or web service application and
         needs to provide endpoints for this service, and connects to
         other services in the namespace, choose **Client and
         server**.

    3. To use a namespace that is not the default cluster namespace, for
       **Namespace**, choose the service namespace. This
       can be a namespace created separately in the same AWS Region in your
       AWS account or a namespace in the same Region that is shared with your
       account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace
       sharing](../../../cloud-map/latest/dg/sharing-namespaces.md "../../../cloud-map/latest/dg/sharing-namespaces.md") in the _AWS Cloud Map Developer Guide_.
    4. (Optional) Specify a log configuration. Select **Use log
       collection**. The default option sends container logs to
       CloudWatch Logs. The other log driver options are configured using AWS FireLens.
       For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

    The following describes each container log destination in more
    detail.

        * **Amazon CloudWatch** – Configure the task to
         send container logs to CloudWatch Logs. The default log driver options are
         provided, which create a CloudWatch log group on your behalf. To
         specify a different log group name, change the driver option
         values.
        * **Amazon Data Firehose** – Configure the task to
         send container logs to Firehose. The default log driver options are
         provided, which send logs to a Firehose delivery stream. To specify
         a different delivery stream name, change the driver option
         values.
        * **Amazon Kinesis Data Streams** – Configure the task to
         send container logs to Kinesis Data Streams. The default log driver options are
         provided, which send logs to an Kinesis Data Streams stream. To specify a
         different stream name, change the driver option values.
        * **Amazon OpenSearch Service** – Configure the task to
         send container logs to an OpenSearch Service domain. The log driver options
         must be provided.
        * **Amazon S3** – Configure the task to send
         container logs to an Amazon S3 bucket. The default log driver options
         are provided, but you must specify a valid Amazon S3 bucket
         name.

    5. (Optional) To enable access logs, follow these steps:
       1. Expand **Access log configuration**. For **Format**, choose either **JSON** or `TEXT`.
       2. To include query parameters in access logs, select **Include query parameters**.

10. (Optional) To interconnect your service using Service Discovery, expand
    **Service discovery**, and then do the following.
    1.  Select **Use service discovery**.
    2.  To use a new namespace, choose **Create a new
        namespace** under **Configure namespace**,
        and then provide a namespace name and description. To use an existing
        namespace, choose **Select an existing namespace** and
        then choose the namespace that you want to use.
    3.  Provide Service Discovery service information such as the
        service's name and description.
    4.  To have Amazon ECS perform periodic container-level health checks, select
        **Enable Amazon ECS task health propagation**.
    5.  For **DNS record type**, select the DNS record type
        to create for your service. Amazon ECS service discovery only supports
        **A** and **SRV** records,
        depending on the network mode that your task definition specifies. For
        more information about these record types, see [Supported DNS Record Types](../../../Route53/latest/DeveloperGuide/ResourceRecordTypes.md "../../../Route53/latest/DeveloperGuide/ResourceRecordTypes.md") in the
        _Amazon Route 53 Developer Guide_.

            * If the task definition that your service task specifies uses
             the `bridge` or `host` network mode, only
             type **SRV** records are supported. Choose a
             container name and port combination to associate with the
             record.
            * If the task definition that your service task specifies uses
             the `awsvpc` network mode, select either the
             **A** or **SRV** record
             type. If you choose **A**, skip to the next
             step. If you choose **SRV**, specify either the
             port that the service can be found on or a container name and
             port combination to associate with the record.

        For **TTL**, enter the time in seconds how long a
        record set is cached by DNS resolvers and by web browsers.

11. (Optional) To interconnect your service using VPC Lattice, xxpand
    **VPC Lattice**, and then do the following:
    1. Select **Turn on VPC Lattice**
    2. For **Infrastructure role**, choose the
       infrastructure role.

    If you haven't created a role, choose **Create infrastructure
    role**. 3. Under **Target Groups** choose the target group or
    groups. You need to choose at least one target group and can have a
    maximum of five. Choose **Add target group** to add
    additional target groups. Choose the **Port name**,
    **Protocol**, and **Port** for
    each target group you chose.

    To delete a target group, choose **Remove**.

    ###### Note

        * If you want to add existing target groups, you need use
         the AWS CLI. For instructions on how to add target groups
         using the AWS CLI, see [register-targets](../../../cli/latest/reference/vpc-lattice/register-targets.md "../../../cli/latest/reference/vpc-lattice/register-targets.md")  in the *AWS Command Line Interface Reference*.
        * While a VPC Lattice service can have multiple target groups,
         each target group can only be added to one service.

    4. To complete the VPC Lattice configuration, by including your new target
       groups in the listener default action or in the rules of an existing
       VPC Lattice service in the VPC Lattice console. For more information, see
       [Listener rules for
       your VPC Lattice service](../../../vpc-lattice/latest/ug/listener-rules.md "../../../vpc-lattice/latest/ug/listener-rules.md").

12. (Optional) To configure a load balancer for your service, expand
    **Load balancing**.

Choose the load balancer.

| To use this load balancer | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application Load Balancer | 1. For **Load balancer type**,<br>select **Application Load Balancer**.<br>2. Choose **Create a new load<br>balancer\*<br>• to create a new Application Load Balancer or<br>**Use an existing load balancer**<br>to select an existing Application Load Balancer.<br>3. For **Load balancer name**, enter<br>a unique name.<br>4. For **Choose container to load<br>balance**, choose the container that<br>hosts the service.<br>5. For **Listener**, enter a port<br>and protocol for the Application Load Balancer to listen for connection<br>requests on. By default, the load balancer will be<br>configured to use port 80 and HTTP.<br>6. For **Target group name**, enter<br>a name and a protocol for the target group that the<br>Application Load Balancer routes requests to. By default, the target<br>group routes requests to the first container defined<br>in your task definition.<br>7. For **Degregistration delay**,<br>enter the number of seconds for the load balancer to<br>change the target state to `UNUSED`. The<br>default is 300 seconds.<br>8. For **Health check path\*\*, enter<br>an existing path within your container where the<br>Application Load Balancer periodically sends requests to verify the<br>connection health between the Application Load Balancer and the<br>container. The default is the root directory<br>(`/`). |
| Network Load Balancer     | 1. For **Load balancer type**,<br>select **Network Load Balancer**.<br>2. For **Load Balancer**, choose an<br>existing Network Load Balancer.<br>3. For **Choose container to load<br>balance**, choose the container that<br>hosts the service.<br>4. For **Target group name**, enter<br>a name and a protocol for the target group that the<br>Network Load Balancer routes requests to. By default, the target<br>group routes requests to the first container defined<br>in your task definition.<br>5. For **Degregistration delay**,<br>enter the number of seconds for the load balancer to<br>change the target state to `UNUSED`. The<br>default is 300 seconds.<br>6. For **Health check path**, enter<br>an existing path within your container where the<br>Network Load Balancer periodically sends requests to verify the<br>connection health between the Application Load Balancer and the<br>container. The default is the root directory<br>(`/`).                                                                                                                                                                                                                                                                                                                                                                                                      |

13. (Optional) To configure service Amazon EC2 Auto Scaling, expand **Service auto
    scaling**, and then specify the following parameters.To use predicte auto scaling, which looks at past load data from traffic flows, configure it after you create the service. For more information, see [Use historical patterns to scale Amazon ECS services with predictive
    scaling](predictive-auto-scaling.md "predictive-auto-scaling.md").
    1.  To use service auto scaling, select **Service auto
        scaling**.
    2.  For **Minimum number of tasks**, enter the lower limit of
        the number of tasks for service auto scaling to use. The desired count will not go below this count.
    3.  For **Maximum number of tasks**, enter the upper
        limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.
    4.  Choose the policy type. Under **Scaling policy type**, choose
        one of the following options.

    | To use this policy type | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Target tracking         | 1. For **Scaling policy<br>type**, choose **Target<br>tracking**.<br>2. For **Policy name**, enter<br>the name of the policy.<br>3. For **ECS service metric**,<br>select one of the following metrics.<br>• **ECSServiceAverageCPUUtilization** –<br>Average CPU utilization of the service.<br>• **ECSServiceAverageMemoryUtilization** –<br>Average memory utilization of the service.<br>• **ALBRequestCountPerTarget**<br>– Number of requests completed per target<br>in an Application Load Balancer target group.<br>4. For **Target value**, enter<br>the value the service maintains for the selected<br>metric.<br>5. For **Scale-out cooldown<br>period**, enter the amount of time, in seconds, after a scale-out activity (add tasks) that must pass before another scale-out activity can start.<br>6. For **Scale-in cooldown<br>period**, enter the amount of time, in seconds, after a scale-in activity (remove tasks) that must pass before another scale-in activity can start.<br>7. To prevent the policy from performing a<br>scale-in activity, select **Turn off<br>scale-in**.<br>8. • (Optional) Select \*_Turn off scale-in_<br>• if you want your scaling policy to scale out for increased traffic but don’t need it to scale in when traffic decreases.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
    | Step scaling            | 1. For **Scaling policy<br>type**, choose **Step<br>scaling**.<br>2. For **Policy name**, enter<br>the policy name.<br>3. For **Alarm name**, enter a<br>unique name for the alarm.<br>4. For **Amazon ECS service<br>metric**, choose the metric to use for<br>the alarm.<br>5. For **Statistic**, choose<br>the alarm statistic.<br>6. For **Period**, choose the<br>period for the alarm.<br>7. For **Alarm condition**,<br>choose how to compare the selected metric to the<br>defined threshold.<br>8. For **Threshold to compare<br>metrics\*<br>• and **Evaluation period<br>to initiate alarm**, enter the threshold<br>used for the alarm and how long to evaluate the<br>threshold.<br>9. Under **Scaling actions**, do<br>the following:<br>• For **Action**,<br>select whether to add, remove, or set a<br>specific desired count for your service.<br>• If you chose to add or remove tasks,<br>for **Value**, enter the number<br>of tasks (or percent of existing tasks) to add or<br>remove when the scaling action is initiated. If<br>you chose to set the desired count, enter the<br>number of tasks. For **Type**,<br>select whether the **Value*<br>• is<br>an integer or a percent value of the existing<br>desired count.<br>• For **Lower bound** and<br>**Upper bound**, enter the lower<br>boundary and upper boundary of your step scaling<br>adjustment. By default, the lower bound for an add policy is the alarm threshold and the upper bound is positive (+) infinity. By default, the upper bound for a remove policy is the alarm threshold and the lower bound is negative (-) infinity.<br>• (Optional) Add additional scaling options.<br>Choose **Add new scaling<br>action**, and then repeat the<br>\*\*Scaling actions*<br>• steps.<br>• For **Cooldown period**, enter the amount of time, in seconds, to wait for a previous scaling activity to take effect. For an add policy, this is the time after a scale-out activity that the scaling policy blocks scale-in activities and limits how many tasks can be scale out at a time. For a remove policy, this is the time after a scale-in activity that must pass before another scale-in activity can start. |

14. (Optional) To use a task placement strategy other than the
    default, expand **Task Placement**, and then choose
    from the following options.

For more information, see [How Amazon ECS places tasks on container instances](task-placement.md "task-placement.md").

    * **AZ Balanced Spread** – Distribute tasks
     across Availability Zones and across container instances in
     the Availability Zone.
    * **AZ Balanced BinPack** – Distribute
     tasks across Availability Zones and across container
     instances with the least available memory.
    * **BinPack** – Distribute tasks based on
     the least available amount of CPU or memory.
    * **One Task Per Host** – Place, at most,
     one task from the service on each container instance.
    * **Custom** – Define your own task placement strategy.

If you chose **Custom**, define the algorithm for placing tasks and the rules that are considered during task placement.

    * Under **Strategy**, for **Type** and **Field**, choose the algorithm and the entity to use for the algorithm.


    You can enter a maximum of 5 strategies.
    * Under **Constraint**, for **Type** and **Expression**, choose the rule and attribute for the constraint.


    For example, to set the constraint to place tasks on T2 instances, for the **Expression**, enter **attribute:ecs.instance-type =~ t2.\***.


    You can enter a maximum of 10 constraints.

15. If your task uses a data volume that's compatible with configuration at
    deployment, you can configure the volume by expanding
    **Volume**.

The volume name and volume type are configured when you create a task
definition revision and can't be changed when creating a service. To update
the volume name and type, you must create a new task definition revision and
create a service by using the new revision.

| To configure this volume type | Do this                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon EBS                    | 1. For **EBS volume type**, choose<br>the type of EBS volume that you want<br>to attach to your task.<br>2. For **Size (GiB)**, enter a valid<br>value for the volume size in gibibytes (GiB). You<br>can specify a minimum of 1 GiB and a maximum of<br>16,384 GiB volume size. This value is required<br>unless you provide a snapshot ID.<br>3. For **IOPS**, enter the maximum<br>number of input/output operations (IOPS) that the<br>volume should provide. This value is configurable<br>only for `io1`,`io2`, and<br>`gp3` volume types.<br>4. For **Throughput (MiB/s)**, enter<br>the throughput that the volume should provide, in<br>mebibytes per second (MiBps, or MiB/s). This value<br>is configurable only for the `gp3` volume<br>type.<br>5. For **Snapshot ID**, choose an<br>existing Amazon EBS volume snapshot or enter the ARN of a<br>snapshot if you want to create a volume from a<br>snapshot. You can also create a new, empty volume by<br>not choosing or entering a snapshot<br>ID.<br>6. If you specify a **Snapshot ID**, you<br>can specify a **Volume initialization rate<br>(MiB/s)**. Enter a value between 100 and<br>300, in MiB/s, that will determine how fast data is<br>loaded from the snapshot specified using<br>**Snapshot ID\*<br>• for volume<br>creation.<br>7. For **File system type**, choose<br>the type of file system that will be used for data<br>storage and retrieval on the volume. You can choose<br>either the operating system default or a specific<br>file system type. The default for Linux is<br>`XFS`. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start.<br>8. For **Infrastructure role**,<br>choose an IAM role with the necessary permissions<br>that allow Amazon ECS to manage Amazon EBS volumes for tasks.<br>You can attach the<br>`AmazonECSInfrastructureRolePolicyForVolumes`<br>managed policy to the role, or you can use the<br>policy as a guide to create and attach an your own<br>policy with permissions that meet your specific<br>needs. For more information about the necessary<br>permissions,<br>see<br>[Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").<br>9. For **Encryption**, choose<br>**Default*<br>• if you want to use<br>the Amazon EBS encryption by default settings. If your<br>account has [Encryption by default](../../../ebs/latest/userguide/encryption-by-default.md "../../../ebs/latest/userguide/encryption-by-default.md") configured, the<br>volume will be encrypted with the AWS Key Management Service (AWS KMS)<br>key that's specified in the setting. If you choose<br>\*\*Default*<br>• and Amazon EBS default<br>encryption isn't turned on, the volume will be<br>unencrypted.<br>If you choose **Custom**, you can<br>specify an AWS KMS key of your choice for volume<br>encryption.<br>If you choose **None**, the<br>volume will be unencrypted unless you have<br>encryption by default configured,<br>or<br>if you create a volume from an encrypted<br>snapshot.<br>10. If you've chosen **Custom\*<br>• for<br>**Encryption**, you must specify<br>the AWS KMS key that you want to use. For<br>**KMS key**, choose an<br>AWS KMS key or enter a key ARN. If you choose to<br>encrypt your volume by using a symmetric customer managed key,<br>make sure that you have the right permissions<br>defined in your AWS KMS key policy. For more<br>information, see [Data encryption for Amazon EBS volumes](ebs-volumes.md#ebs-kms-encryption "ebs-volumes.md#ebs-kms-encryption").<br>11. (Optional) Under **Tags**, you can<br>add tags to your Amazon EBS volume by either propagating tags<br>from the task definition or service, or by providing your own<br>tags.<br>If you want to propagate tags from the task<br>definition, choose **Task definition**<br>for **Propagate tags from**. If you want to propagate tags from the service, choose **Service**<br>for **Propagate tags from**. If you<br>choose **Do not propagate**, or if you<br>don't choose a value, the tags aren't propagated.<br>If you want to provide your own tags, choose<br>**Add tag\*<br>• and then provide the<br>key and value for each tag you add.<br>For more information about tagging Amazon EBS volumes, see<br>[Tagging Amazon EBS volumes](specify-ebs-config.md#ebs-volume-tagging "specify-ebs-config.md#ebs-volume-tagging"). |

16. To use ECS Exec to debug the service, under **Troubleshooting configuration**, select **Turn on ECS Exec**.
17. (Optional) To help identify your service and tasks, expand the
    **Tags** section, and then configure your tags.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the task definition tags, select **Turn on Amazon ECS managed
tags**, and then for **Propagate tags from**,
choose **Task definitions**.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the service tags, select **Turn on Amazon ECS managed tags**,
and then for **Propagate tags from**, choose
**Service**.

Add or remove a tag.

    * [Add a tag] Choose **Add tag**, and then do the
     following:




    	+ For **Key**, enter the key name.
    	+ For **Value**, enter the key value.
    * [Remove a tag] Next to the tag, choose **Remove
     tag**.

18. Choose **Create**.

## Next steps

The following are additional actions after you create a service.

- Configure predicte auto scaling, which looks at past load data from traffic
  flows. For more information, see [Use historical patterns to scale Amazon ECS services with predictive
  scaling](predictive-auto-scaling.md "predictive-auto-scaling.md").
- Track your deployment and view your service history for services that Amazon ECS
  circuit breaker. For more information, see [View service history using Amazon ECS service
  deployments](service-deployment.md "service-deployment.md").
