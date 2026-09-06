

# Running an application as an Amazon ECS task
<a name="standalone-task-create"></a>

You can create a task for a one-time process using the AWS Management Console.

**To create a standalone task (AWS Management Console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. The Amazon ECS console allows you to create a standalone task from either your cluster detail page or from the task definition revision list. Use the following steps to create your standalone task depending on the resource page you choose.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-create.html)

1. For **Existing cluster**, choose the cluster.

   Choose **Create cluster** to run the task on a new cluster

1. Choose how your tasks are distributed across your cluster infrastructure. Under **Compute configuration**, choose your option.To use a capacity provider strategy, you must configure your capacity providers at the cluster level. 

   If you haven't configured your cluster to use a capacity provider, use a launch type instead.

   If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-create.html)

1. Under **Deployment configuration**, do the following:

   1. For **Task definition**, enter the task definition.
**Important**  
The console validates the selection to ensure that the selected task definition family and revision are compatible with the defined compute configuration.

   1. For **Desired tasks**, enter the number of tasks to launch.

   1. For **Task group**, enter the task group name.

1. If your task definition uses the `awsvpc` network mode, expand **Networking**. Use the following steps to specify a custom configuration.

   1. For **VPC**, select the VPC to use.

   1. For **Subnets**, select one or more subnets in the VPC that the task scheduler considers when placing your tasks.

   1. For **Security group**, you can either choose an existing security group or create a new one. To use an existing security group, choose the security group and move to the next step. To create a new security group, choose **Create a new security group**. You must specify a security group name, description, and then add one or more inbound rules for the security group.

   1. For **Public IP**, choose whether to auto-assign a public IP address to the elastic network interface (ENI) of the task.

      AWS Fargate tasks can be assigned a public IP address when run in a public subnet so they have a route to the internet. EC2 tasks can't be assigned a public IP using this field. For more information, see [Amazon ECS task networking options for Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-task-networking.html) and [Allocate a network interface for an Amazon ECS task.](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking-awsvpc.html).

1. If your task uses a data volume that's compatible with configuration at deployment, you can configure the volume by expanding **Volume**.

   The volume name and volume type are configured when creating a task definition revision and can't be changed when you run a standalone task. To update the volume name and type, you must create a new task definition revision and run a task by using the new revision.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/standalone-task-create.html)

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

1. (Optional) To override the task IAM role, or task execution role that is defined in your task definition, expand **Task overrides**, and then complete the following steps:

   1. For **Task role**, choose an IAM role for this task. For more information, see [Amazon ECS task IAM role](task-iam-roles.md).

      Only roles with the `ecs-tasks.amazonaws.com` trust relationship are displayed. For instructions on how to create an IAM role for your tasks, see [Creating the task IAM role](task-iam-roles.md#create_task_iam_policy_and_role).

   1. For **Task execution role**, choose a task execution role. For more information, see [Amazon ECS task execution IAM role](task_execution_IAM_role.md).

1. (Optional) To override the container commands and environment variables, expand **Container Overrides**, and then expand the container.
   +  To send a command to the container other than the task definition command, for **Command override**, enter the Docker command.
   + To add an environment variable, choose **Add Environment Variable**. For **Key**, enter the name of your environment variable. For **Value**, enter a string value for your environment value (without the surrounding double quotation marks (`" "`)).

     AWS surrounds the strings with double quotation marks (" ") and passes the string to the container in the following format:

     ```
     MY_ENV_VAR="This variable contains a string."
     ```

1. (Optional) To help identify your task, expand the **Tags** section, and then configure your tags.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the task definition tags, select **Turn on Amazon ECS managed tags**, and then select **Task definitions**.

   Add or remove a tag.
   + [Add a tag] Choose **Add tag**, and then do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create**.