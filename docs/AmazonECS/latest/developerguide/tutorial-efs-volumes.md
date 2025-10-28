# Configuring Amazon EFS file systems for Amazon ECS using the

console

Learn how to use Amazon Elastic File System (Amazon EFS) file systems with Amazon ECS.

## Step 1: Create an Amazon ECS cluster

Use the following steps to create an Amazon ECS cluster.

###### To create a new cluster (Amazon ECS console)

Before you begin, assign the appropriate IAM permission. For more information, see
[Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies "security_iam_id-based-policy-examples.md#IAM_cluster_policies").

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Clusters**.
4. On the **Clusters** page, choose **Create
   cluster**.
5. Under **Cluster configuration**, for **Cluster
   name**, enter `EFS-tutorial` for the cluster
   name.
6. (Optional) To change the VPC and subnets where your tasks and services launch,
   under **Networking**, perform any of the following
   operations:
   - To remove a subnet, under **Subnets**, choose
     **X** for each subnet that you want to
     remove.
   - To change to a VPC other than the **default** VPC,
     under **VPC**, choose an existing
     **VPC**, and then under
     **Subnets**, select each subnet.

7. To add Amazon EC2 instances to your cluster, expand
   **Infrastructure**, and then select **Amazon EC2
   instances**. Next, configure the Auto Scaling group which acts as the
   capacity provider:
   1. To create a Auto Scaling group, from **Auto Scaling group
      (ASG)**, select **Create new group**, and
      then provide the following details about the group:
      - For **Operating system/Architecture**, choose
        Amazon Linux 2.
      - For **EC2 instance type**, choose
        `t2.micro`.

      For **SSH key pair**, choose the pair that
      proves your identity when you connect to the instance.
      - For **Capacity**, enter
        `1`.

8. Choose **Create**.

## Step 2: Create a security group for Amazon EC2 instances

and the Amazon EFS file system

In this step, you create a security group for your Amazon EC2 instances that allows inbound
network traffic on port 80 and your Amazon EFS file system that allows inbound access from
your container instances.

Create a security group for your Amazon EC2 instances with the following options:

- **Security group name** - a unique name for your security
  group.
- **VPC** - the VPC that you identified earlier for your
  cluster.
- **Inbound rule**
  - **Type** - **HTTP**
  - **Source** - **0.0.0.0/0**.

Create a security group for your Amazon EFS file system with the following options:

- **Security group name** - a unique name for your security
  group. For example,
  `EFS-access-for-sg-`dc025fa2``.
- **VPC** - the VPC that you identified earlier for your
  cluster.
- **Inbound rule**
  - **Type** - **NFS**
  - **Source** - **Custom** with the ID
    of the security group you created for your instances.

For information about how to create a security group, see [Create a security group for your Amazon EC2 instance](../../../AWSEC2/latest/UserGuide/creating-security-group.md "../../../AWSEC2/latest/UserGuide/creating-security-group.md") in the _Amazon EC2 User Guide_.

## Step 3: Create an Amazon EFS file system

In this step, you create an Amazon EFS file system.

###### To create an Amazon EFS file system for Amazon ECS tasks.

1. Open the Amazon Elastic File System console at
   [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/ "https://console.aws.amazon.com/efs/").
2. Choose **Create file system**.
3. Enter a name for your file system and then
   choose the VPC
   that your container instances are hosted in. By default, each subnet in the
   specified VPC receives a mount target that uses the default security group for
   that VPC. Then, choose **Customize**.

###### Note

This tutorial assumes that your Amazon EFS file system, Amazon ECS cluster, container
instances, and tasks are in the same VPC. For more
information about mounting a file system from a different VPC, see [Walkthrough: Mount a file
system from a different VPC](../../../efs/latest/ug/efs-different-vpc.md "../../../efs/latest/ug/efs-different-vpc.md") in the _Amazon EFS User
Guide_. 4. On the **File system settings** page, configure optional
settings and then under **Performance settings**, choose the
**Bursting** throughput mode for your file system. After
you have configured settings, select **Next**.

    1. (Optional) Add tags for your file system. For example, you could
     specify a unique name for the file system by entering that name in the
     **Value** column next to the
     **Name** key.
    2. (Optional) Enable lifecycle management to save money on infrequently
     accessed storage. For more information, see [EFS Lifecycle
     Management](../../../efs/latest/ug/lifecycle-management-efs.md "../../../efs/latest/ug/lifecycle-management-efs.md") in the
     *Amazon Elastic File System User Guide*.
    3. (Optional) Enable encryption. Select the check box to enable
     encryption of your Amazon EFS file system at rest.

5. On the **Network access** page, under **Mount
   targets**, replace the existing security group configuration for
   every availability zone with the security group you created for the file system
   in [Step 2: Create a security group for Amazon EC2 instances
   and the Amazon EFS file system](#efs-security-group "#efs-security-group") and
   then choose **Next**.
6. You do not need to configure **File system policy** for this
   tutorial, so you can skip the section by choosing
   **Next**.
7. Review your file system options and choose **Create** to
   complete the process.
8. From the **File systems** screen, record the **File
   system ID**.
   In the
   next step, you will reference this value in your Amazon ECS task definition.

## Step 4: Add content to the Amazon EFS file system

In this step, you mount the Amazon EFS file system to an Amazon EC2 instance and add content to
it. This is for testing purposes in this tutorial, to illustrate the persistent nature
of the data. When using this feature you would normally have your application or another
method of writing data to your Amazon EFS file system.

###### To create an Amazon EC2 instance and mount the Amazon EFS file system

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance**.
3. Under **Application and OS Images (Amazon Machine Image)**,
   select the **Amazon Linux 2 AMI (HVM)**.
4. Under **Instance type**, keep the default instance type,
   `t2.micro`.
5. Under **Key pair (login)**, select a key pair for SSH access
   to the instance.
6. Under **Network settings**, select the VPC that you specified
   for your Amazon EFS file system and Amazon ECS cluster. Select a subnet and the instance
   security group created in [Step 2: Create a security group for Amazon EC2 instances
   and the Amazon EFS file system](#efs-security-group "#efs-security-group"). Configure the instance's security
   group. Ensure that **Auto-assign public IP** is enabled.
7. Under **Configure storage**, choose the
   **Edit** button for file systems and then choose
   **EFS**. Select the file system you created in [Step 3: Create an Amazon EFS file system](#efs-create-filesystem "#efs-create-filesystem"). You
   can optionally change the mount point or leave the default value.

###### Important

Your must select a subnet before you can add a file system to the
instance. 8. Clear the **Automatically create and attach security
groups**. Leave the other check box selected. Choose **Add
shared file system**. 9. Under **Advanced Details**, ensure that the user data script
is populated automatically with the Amazon EFS file system mounting steps. 10. Under **Summary**, ensure the **Number of
instances** is **1**. Choose **Launch
instance**. 11. On the **Launch an instance** page, choose **View all
instances** to see the status of your instances. Initially, the
**Instance state** status is `PENDING`. After
the state changes to `RUNNING` and the instance passes all status
checks, the instance is ready for use.

Now, you connect to the Amazon EC2 instance and add content to the Amazon EFS file
system.

###### To connect to the Amazon EC2 instance and add content to the Amazon EFS file system

1. SSH to the Amazon EC2 instance you created. For more information, see [Connect to your Linux instance using SSH](../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md "../../../AWSEC2/latest/UserGuide/connect-to-linux-instance.md") in the
   _Amazon EC2 User Guide_.
2. From the terminal window, run the **df -T** command to verify
   that the Amazon EFS file system is mounted. In the following output, we have
   highlighted the Amazon EFS file system mount.

```
$ df -T
Filesystem     Type            1K-blocks    Used        Available Use% Mounted on
devtmpfs       devtmpfs           485468       0           485468   0% /dev
tmpfs          tmpfs              503480       0           503480   0% /dev/shm
tmpfs          tmpfs              503480     424           503056   1% /run
tmpfs          tmpfs              503480       0           503480   0% /sys/fs/cgroup
/dev/xvda1     xfs               8376300 1310952          7065348  16% /
`127.0.0.1:/ nfs4 9007199254739968 0 9007199254739968 0% /mnt/efs/fs1`
tmpfs          tmpfs              100700       0           100700   0% /run/user/1000
```

3. Navigate to the directory that the Amazon EFS file system is mounted at. In the
   example above, that is `/mnt/efs/fs1`.
4. Create a file named `index.html` with the following content:

```
<html>
    <body>
        <h1>It Works!</h1>
        <p>You are using an Amazon EFS file system for persistent container storage.</p>
    </body>
</html>
```

## Step 5: Create a task definition

The following task definition creates a data volume named `efs-html`. The
`nginx` container mounts the host data volume at the NGINX root,
`/usr/share/nginx/html`.

###### To create a new task definition using the Amazon ECS console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Task definitions**.
3. Choose **Create new task definition**, **Create new
   task definition with JSON**.
4. In the JSON editor box, copy and paste the following JSON text, replacing the
   `fileSystemId` with the ID of your Amazon EFS file system.

```
{
    "containerDefinitions": [
        {
            "memory": 128,
            "portMappings": [
                {
                    "hostPort": 80,
                    "containerPort": 80,
                    "protocol": "tcp"
                }
            ],
            "essential": true,
            "mountPoints": [
                {
                    "containerPath": "`/usr/share/nginx/html`",
                    "sourceVolume": "`efs-html`"
                }
            ],
            "name": "nginx",
            "image": "public.ecr.aws/docker/library/nginx:latest"
        }
    ],
    "volumes": [
        {
            "name": "`efs-html`",
            "efsVolumeConfiguration": {
                "fileSystemId": "`fs-1324abcd`",
                "transitEncryption": "`ENABLED`"
            }
        }
    ],
    "family": "efs-tutorial",
    "executionRoleArn":"arn:aws:iam::111122223333:role/`ecsTaskExecutionRole`"
}
```

###### Note

The Amazon ECS task execution IAM role does not require any specific Amazon EFS-related
permissions to mount an Amazon EFS file system. By default, if no Amazon EFS resource-based
policy exists, access is granted to all principals (\*) at file system creation.

The Amazon ECS task role is only required if "EFS IAM authorization" is enabled in the
Amazon ECS task definition. When enabled, the task role identity must be allowed access
to the Amazon EFS file system in the Amazon EFS resource-based policy, and anonymous access
should be disabled. 5. Choose **Create**.

## Step 6: Run a task and view the results

Now that your Amazon EFS file system is created and there is web content for the NGINX
container to serve, you can run a task using the task definition that you created. The
NGINX web server serves your simple HTML page. If you update the content in your Amazon EFS
file system, those changes are propagated to any containers that have also mounted that
file system.

The task runs in the subnet that you defined for the cluster.

###### To run a task and view the results using the console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. On the **Clusters** page, select the cluster to run the
   standalone task in.

Determine the resource from where you launch the service.

| To start a service from | Steps                                                                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clusters                | 1. On the **Clusters** page, select the cluster to create the service in. 2. From the **Tasks** tab, choose **Run new task**.                        |
| Launch type             | 1. On the **Task** page, choose the task definition. 2. If there is more than one revision, select the revision. 3. Choose **Create**, **Run task**. | 3. (Optional) Choose how your scheduled task is distributed across your cluster infrastructure. Expand **Compute configuration**, and then do the following:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Distribution method     | Steps                                                                                                                                                |
| ---                     | ---                                                                                                                                                  |
| Launch type             | 1. In the **Compute options** section, select **Launch type**. 2. For **Launch type**, choose **EC2**.                                               | 4. For **Application type**, choose **Task**. 5. For **Task definition**, choose the `efs-tutorial` task definition that you created earlier. 6. For **Desired tasks**, enter `1`. 7. Choose **Create**. 8. On the **Cluster** page, choose **Infrastructure**. 9. Under **Container Instances**, choose the container instance to connect to. 10. On the **Container Instance** page, under **Networking**, record the **Public IP** for your instance. 11. Open a browser and enter the public IP address. You should see the following message: `It works! You are using an Amazon EFS file system for persistent container storage.` ###### Note If you do not see the message, make sure that the security group for your container instance allows inbound network traffic on port 80 and the security group for your file system allows inbound access from the container instance. |
