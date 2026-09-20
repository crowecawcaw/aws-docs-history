

# Running an application as an Amazon ECS task
<a name="standalone-task-create"></a>

You can create a task for a one-time process using the AWS Management Console.

**To create a standalone task (AWS Management Console)**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. The Amazon ECS console allows you to create a standalone task from either your cluster detail page or from the task definition revision list. Use the following steps to create your standalone task depending on the resource page you choose.


<table>
<thead>
  <tr><th>To start a service from</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>The cluster detail page</td><td> <ol><li> On the <b>Clusters</b> page, select the cluster to create the service in. </li><li> From the <b>Tasks</b> tab, choose <b>Run task</b>. </li></ol> </td><td></td></tr>
  <tr><td>The task definition revision page</td><td> <ol><li> On the <b>Task definitions</b> page, choose the task definition family to display the revisions for that family. </li><li> Select the revision you want to use. </li><li> From the <b>Deploy</b> menu, choose <b>Run task</b>. </li></ol> </td><td></td></tr>
</tbody>
</table>


1. For **Existing cluster**, choose the cluster.

   Choose **Create cluster** to run the task on a new cluster

1. Choose how your tasks are distributed across your cluster infrastructure. Under **Compute configuration**, choose your option.To use a capacity provider strategy, you must configure your capacity providers at the cluster level. 

   If you haven't configured your cluster to use a capacity provider, use a launch type instead.

   If you want to run your workloads on Amazon ECS Managed Instances, you must use the Capacity provider strategy option.


<table>
<thead>
  <tr><th>Distribution method</th><th>Steps</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Capacity provider strategy</td><td> <ol><li> In the <b>Compute options</b> section, select <b>Capacity provider strategy</b>. </li><li> Choose a strategy: <ul><li> To use the cluster's default capacity provider strategy, choose <b>Use cluster default</b>. </li><li> If your cluster doesn't have a default capacity provider strategy, or to use a custom strategy, choose <b>Use custom</b>, <b>Add capacity provider strategy</b> and define your custom capacity provider strategy by specifying a <b>Base</b>, <b>Capacity provider</b>, and <b>Weight</b>. </li></ul> </li></ol>  To use a capacity provider in a strategy, the capacity provider must be associated with the cluster.  </td><td></td></tr>
  <tr><td>Launch type</td><td> <ol><li> In the <b>Compute options</b> section, select <b>Launch type</b>. </li><li> For <b>Launch type</b>, choose a launch type. </li><li> (Optional) When you use Fargate, for <b>Platform version</b>, specify the platform version to use. If a platform version isn't specified, the <code>LATEST</code> platform version is used. </li></ol> </td><td></td></tr>
</tbody>
</table>


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


<table>
<thead>
  <tr><th>To configure this volume type</th><th>Do this</th><th></th></tr>
</thead>
<tbody>
  <tr><td>Amazon EBS</td><td> <ol><li> For <b>EBS volume type</b>, choose the type of EBS volume that you want to attach to your task. </li><li> For <b>Size (GiB)</b>, enter a valid value for the volume size in gibibytes (GiB). You can specify a minimum of 1 GiB and a maximum of 16,384 GiB volume size. This value is required unless you provide a snapshot ID.  </li><li> For <b>IOPS</b>, enter the maximum number of input/output operations (IOPS) that the volume should provide. This value is configurable only for <code>io1</code>,<code>io2</code>, and <code>gp3</code> volume types. </li><li> For <b>Throughput (MiB/s)</b>, enter the throughput that the volume should provide, in mebibytes per second (MiBps, or MiB/s). This value is configurable only for the <code>gp3</code> volume type. </li><li> For <b>Snapshot ID</b>, choose an existing Amazon EBS volume snapshot or enter the ARN of a snapshot if you want to create a volume from a snapshot. You can also create a new, empty volume by not choosing or entering a snapshot ID. </li><li> If you specify a <b>Snapshot ID</b>, you can specify a <b>Volume initialization rate (MiB/s)</b>. Enter a value between 100 and 300, in MiB/s, that will determine how fast data is loaded from the snapshot specified using <b>Snapshot ID</b> for volume creation. </li><li> For <b>Termination policy</b>, deselect the checkbox if you want the volume configured for attachment to the task to be preserved after the task is terminated. By default, EBS volumes that are attached to tasks are deleted when the task is terminated. </li><li> For <b>File system type</b>, choose the type of file system that will be used for data storage and retrieval on the volume. You can choose either the operating system default or a specific file system type. The default for Linux is <code>XFS</code>. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start. </li><li> For <b>Infrastructure role</b>, choose an IAM role with the necessary permissions that allow Amazon ECS to manage Amazon EBS volumes for tasks. You can attach the <code>AmazonECSInfrastructureRolePolicyForVolumes</code> managed policy to the role, or you can use the policy as a guide to create and attach an your own policy with permissions that meet your specific needs. For more information about the necessary permissions, see see <a href="infrastructure_IAM_role.md">Amazon ECS infrastructure IAM role</a>. </li><li> For <b>Encryption</b>, choose <b>Default</b> if you want to use the Amazon EBS encryption by default settings. If your account has <a href="https://docs.aws.amazon.com/ebs/latest/userguide/encryption-by-default.html">Encryption by default</a> configured, the volume will be encrypted with the AWS Key Management Service (AWS KMS) key that's specified in the setting. If you choose <b>Default</b> and Amazon EBS default encryption isn't turned on, the volume will be unencrypted.  <br />If you choose <b>Custom</b>, you can specify an AWS KMS key of your choice for volume encryption.  <br />If you choose <b>None</b>, the volume will be unencrypted unless you have encryption by default configured, or if you create a volume from an encrypted snapshot.  </li><li> If you've chosen <b>Custom</b> for <b>Encryption</b>, you must specify the AWS KMS key that you want to use. For <b>KMS key</b>, choose an AWS KMS key or enter a key ARN. If you choose to encrypt your volume by using a symmetric customer managed key, make sure that you have the right permissions defined in your AWS KMS key policy. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-volumes.html?icmpid=docs_ecs_hp-deploy#ebs-kms-encryption">Data encryption for Amazon EBS volumes</a>.  </li><li> (Optional) Under <b>Tags</b>, you can add tags to your Amazon EBS volume by either propagating tags from the task definition or by providing your own tags. <br /> If you want to propagate tags from the task definition, choose <b>Task definition</b> for <b>Propagate tags from</b>. If you choose <b>Do not propagate</b>, or if you don't choose a value, the tags aren't propagated. <br />If you want to provide your own tags, choose <b>Add tag</b> and then provide the key and value for each tag you add. <br />For more information about tagging Amazon EBS volumes, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/specify-ebs-config.html#ebs-volume-tagging">Tagging Amazon EBS volumes</a>. </li></ol></td><td></td></tr>
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