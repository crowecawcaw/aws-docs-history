

# Configuring Amazon EFS file systems for Amazon ECS using the console
<a name="tutorial-efs-volumes"></a>

Learn how to use Amazon Elastic File System (Amazon EFS) file systems with Amazon ECS.

## Step 1: Create an Amazon ECS cluster
<a name="efs-create-cluster"></a>

Use the following steps to create an Amazon ECS cluster. 

**To create a new cluster (Amazon ECS console)**

Before you begin, assign the appropriate IAM permission. For more information, see [Amazon ECS cluster examples](security_iam_id-based-policy-examples.md#IAM_cluster_policies).

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. From the navigation bar, select the Region to use.

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose **Create cluster**.

1. Under **Cluster configuration**, for **Cluster name**, enter `EFS-tutorial` for the cluster name.

1. (Optional) To change the VPC and subnets where your tasks and services launch, under **Networking**, perform any of the following operations:
   + To remove a subnet, under **Subnets**, choose **X** for each subnet that you want to remove.
   + To change to a VPC other than the **default** VPC, under **VPC**, choose an existing **VPC**, and then under **Subnets**, select each subnet.

1.  To add Amazon EC2 instances to your cluster, expand **Infrastructure**, and then select **Amazon EC2 instances**. Next, configure the Auto Scaling group which acts as the capacity provider:

   1. To create a Auto Scaling group, from **Auto Scaling group (ASG)**, select **Create new group**, and then provide the following details about the group:
     + For **Operating system/Architecture**, choose Amazon Linux 2.
     + For **EC2 instance type**, choose `t2.micro`.

        For **SSH key pair**, choose the pair that proves your identity when you connect to the instance.
     + For **Capacity**, enter `1`.

1. Choose **Create**.

## Step 2: Create a security group for Amazon EC2 instances and the Amazon EFS file system
<a name="efs-security-group"></a>

In this step, you create a security group for your Amazon EC2 instances that allows inbound network traffic on port 80 and your Amazon EFS file system that allows inbound access from your container instances. 

Create a security group for your Amazon EC2 instances with the following options:
+ **Security group name** - a unique name for your security group.
+ **VPC** - the VPC that you identified earlier for your cluster.
+ **Inbound rule**
  + **Type** - **HTTP**
  + **Source** - **0.0.0.0/0**.

Create a security group for your Amazon EFS file system with the following options:
+ **Security group name** - a unique name for your security group. For example, `EFS-access-for-sg-{{dc025fa2}}`.
+ **VPC** - the VPC that you identified earlier for your cluster.
+ **Inbound rule**
  + **Type** - **NFS**
  + **Source** - **Custom** with the ID of the security group you created for your instances.

For information about how to create a security group, see [Create a security group for your Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-security-group.html) in the *Amazon EC2 User Guide*.

## Step 3: Create an Amazon EFS file system
<a name="efs-create-filesystem"></a>

In this step, you create an Amazon EFS file system.

**To create an Amazon EFS file system for Amazon ECS tasks.**

1. Open the Amazon Elastic File System console at [https://console.aws.amazon.com/efs/](https://console.aws.amazon.com/efs/).

1. Choose **Create file system**.

1. Enter a name for your file system and then choose the VPC that your container instances are hosted in. By default, each subnet in the specified VPC receives a mount target that uses the default security group for that VPC. Then, choose ** Customize**.
**Note**  
This tutorial assumes that your Amazon EFS file system, Amazon ECS cluster, container instances, and tasks are in the same VPC. For more information about mounting a file system from a different VPC, see [Walkthrough: Mount a file system from a different VPC](https://docs.aws.amazon.com/efs/latest/ug/efs-different-vpc.html) in the *Amazon EFS User Guide*.

1. On the **File system settings** page, configure optional settings and then under **Performance settings**, choose the **Bursting** throughput mode for your file system. After you have configured settings, select **Next**.

   1. (Optional) Add tags for your file system. For example, you could specify a unique name for the file system by entering that name in the **Value** column next to the **Name** key.

   1. (Optional) Enable lifecycle management to save money on infrequently accessed storage. For more information, see [EFS Lifecycle Management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) in the *Amazon Elastic File System User Guide*.

   1. (Optional) Enable encryption. Select the check box to enable encryption of your Amazon EFS file system at rest.

1. On the **Network access** page, under **Mount targets**, replace the existing security group configuration for every availability zone with the security group you created for the file system in [Step 2: Create a security group for Amazon EC2 instances and the Amazon EFS file system](#efs-security-group) and then choose **Next**.

1.  You do not need to configure **File system policy** for this tutorial, so you can skip the section by choosing **Next**.

1. Review your file system options and choose **Create** to complete the process.

1. From the **File systems** screen, record the **File system ID**. In the next step, you will reference this value in your Amazon ECS task definition.

## Step 4: Add content to the Amazon EFS file system
<a name="efs-add-content"></a>

In this step, you mount the Amazon EFS file system to an Amazon EC2 instance and add content to it. This is for testing purposes in this tutorial, to illustrate the persistent nature of the data. When using this feature you would normally have your application or another method of writing data to your Amazon EFS file system.

**To create an Amazon EC2 instance and mount the Amazon EFS file system**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Choose **Launch Instance**.

1. Under **Application and OS Images (Amazon Machine Image)**, select the **Amazon Linux 2 AMI (HVM)**.

1. Under **Instance type**, keep the default instance type, `t2.micro`.

1.  Under **Key pair (login)**, select a key pair for SSH access to the instance.

1. Under **Network settings**, select the VPC that you specified for your Amazon EFS file system and Amazon ECS cluster. Select a subnet and the instance security group created in [Step 2: Create a security group for Amazon EC2 instances and the Amazon EFS file system](#efs-security-group). Configure the instance's security group. Ensure that **Auto-assign public IP** is enabled.

1. Under **Configure storage**, choose the **Edit** button for file systems and then choose **EFS**. Select the file system you created in [Step 3: Create an Amazon EFS file system](#efs-create-filesystem). You can optionally change the mount point or leave the default value.
**Important**  
Your must select a subnet before you can add a file system to the instance.

1. Clear the **Automatically create and attach security groups**. Leave the other check box selected. Choose **Add shared file system**.

1. Under **Advanced Details**, ensure that the user data script is populated automatically with the Amazon EFS file system mounting steps.

1.  Under **Summary**, ensure the **Number of instances** is **1**. Choose **Launch instance**.

1. On the **Launch an instance** page, choose **View all instances** to see the status of your instances. Initially, the **Instance state** status is `PENDING`. After the state changes to `RUNNING` and the instance passes all status checks, the instance is ready for use.

Now, you connect to the Amazon EC2 instance and add content to the Amazon EFS file system.

**To connect to the Amazon EC2 instance and add content to the Amazon EFS file system**

1. SSH to the Amazon EC2 instance you created. For more information, see [Connect to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html) in the *Amazon EC2 User Guide*.

1. From the terminal window, run the **df -T** command to verify that the Amazon EFS file system is mounted. In the following output, we have highlighted the Amazon EFS file system mount.

   ```
   $ df -T
   Filesystem     Type            1K-blocks    Used        Available Use% Mounted on
   devtmpfs       devtmpfs           485468       0           485468   0% /dev
   tmpfs          tmpfs              503480       0           503480   0% /dev/shm
   tmpfs          tmpfs              503480     424           503056   1% /run
   tmpfs          tmpfs              503480       0           503480   0% /sys/fs/cgroup
   /dev/xvda1     xfs               8376300 1310952          7065348  16% /
   {{127.0.0.1:/    nfs4     9007199254739968       0 9007199254739968   0% /mnt/efs/fs1}}
   tmpfs          tmpfs              100700       0           100700   0% /run/user/1000
   ```

1. Navigate to the directory that the Amazon EFS file system is mounted at. In the preceding example, that is `/mnt/efs/fs1`.

1. Create a file named `index.html` with the following content:

   ```
   <html>
       <body>
           <h1>It Works!</h1>
           <p>You are using an Amazon EFS file system for persistent container storage.</p>
       </body>
   </html>
   ```

## Step 5: Create a task definition
<a name="efs-task-def"></a>

The following task definition creates a data volume named `efs-html`. The `nginx` container mounts the host data volume at the NGINX root, `/usr/share/nginx/html`.

**To create a new task definition using the Amazon ECS console**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Task definitions**.

1. Choose **Create new task definition**, **Create new task definition with JSON**.

1. In the JSON editor box, copy and paste the following JSON text, replacing the `fileSystemId` with the ID of your Amazon EFS file system.

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
                       "containerPath": "{{/usr/share/nginx/html}}",
                       "sourceVolume": "{{efs-html}}"
                   }
               ],
               "name": "nginx",
               "image": "public.ecr.aws/docker/library/nginx:latest"
           }
       ],
       "volumes": [
           {
               "name": "{{efs-html}}",
               "efsVolumeConfiguration": {
                   "fileSystemId": "{{fs-1324abcd}}",
                   "transitEncryption": "{{ENABLED}}"
               }
           }
       ],
       "family": "efs-tutorial",
       "executionRoleArn":"arn:aws:iam::111122223333:role/{{ecsTaskExecutionRole}}"
   }
   ```
**Note**  
The Amazon ECS task execution IAM role does not require any specific Amazon EFS-related permissions to mount an Amazon EFS file system. By default, if no Amazon EFS resource-based policy exists, access is granted to all principals (\*) at file system creation.  
The Amazon ECS task role is only required if "EFS IAM authorization" is enabled in the Amazon ECS task definition. When enabled, the task role identity must be allowed access to the Amazon EFS file system in the Amazon EFS resource-based policy, and anonymous access should be disabled.

1. Choose **Create**.

## Step 6: Run a task and view the results
<a name="efs-run-task"></a>

Now that your Amazon EFS file system is created and there is web content for the NGINX container to serve, you can run a task using the task definition that you created. The NGINX web server serves your simple HTML page. If you update the content in your Amazon EFS file system, those changes are propagated to any containers that have also mounted that file system.

The task runs in the subnet that you defined for the cluster.

**To run a task and view the results using the console**

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, select the cluster to run the standalone task in.

   Determine the resource from where you launch the service.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-efs-volumes.html)

1. (Optional) Choose how your scheduled task is distributed across your cluster infrastructure. Expand **Compute configuration**, and then do the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/tutorial-efs-volumes.html)

1. For **Application type**, choose **Task**.

1. For **Task definition**, choose the `efs-tutorial` task definition that you created earlier.

1. For **Desired tasks**, enter `1`.

1. Choose **Create**.

1. On the **Cluster** page, choose **Infrastructure**.

1. Under **Container Instances**, choose the container instance to connect to.

1. On the **Container Instance** page, under **Networking**, record the **Public IP** for your instance.

1. Open a browser and enter the public IP address. You should see the following message:

   ```
   It works!
   You are using an Amazon EFS file system for persistent container storage.
   ```
**Note**  
If you do not see the message, make sure that the security group for your container instance allows inbound network traffic on port 80 and the security group for your file system allows inbound access from the container instance.