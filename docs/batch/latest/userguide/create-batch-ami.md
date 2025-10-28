# Tutorial: Create a compute resource AMI

You can create your own custom compute resource AMI to use for your managed and unmanaged
compute environments. For instructions, see the [Compute resource AMI specification](batch-ami-spec.md "batch-ami-spec.md"). Then, after you created a custom AMI, you can create a compute
environment that uses that AMI that you can associate a job queue with. Last, start submitting
jobs to that queue.

###### To create a custom compute resource AMI

1. Choose a base AMI to start from. The base AMI must use HVM virtualization. The base
   AMI can't be a Windows AMI.

###### Note

The AMI that you choose for a compute environment must match the architecture of the instance types that
you intend to use for that compute environment. For example, if your compute environment uses A1 instance types,
the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the
Amazon ECS optimized Amazon Linux 2 AMI. For more information, see [Amazon ECS optimized Amazon Linux 2 AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html")
in the _Amazon Elastic Container Service Developer Guide_.

The Amazon ECS optimized Amazon Linux 2 AMI is the default AMI for compute resources in managed
compute environments. The Amazon ECS optimized Amazon Linux 2 AMI is preconfigured and tested on AWS Batch by
AWS engineers. It's a minimal AMI that you can get started with and to get your compute
resources that are running on AWS quickly. For more information, see [Amazon ECS Optimized AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md") in the
_Amazon Elastic Container Service Developer Guide_.

Alternatively, you can choose another Amazon Linux 2 variant and install the `ecs-init`
package with the following commands. For more information, see [Installing
the Amazon ECS container agent on an Amazon Linux 2 EC2 instance](../../../AmazonECS/latest/developerguide/ecs-agent-install.md#ecs-agent-install-al2 "../../../AmazonECS/latest/developerguide/ecs-agent-install.md#ecs-agent-install-al2") in the
_Amazon Elastic Container Service Developer Guide_:

```
`$` `sudo amazon-linux-extras disable docker`
`$` `sudo amazon-linux-extras install ecs-init`

```

For example, if you want to run GPU workloads on your AWS Batch compute resources, you can
start with the [Amazon Linux Deep Learning
AMI](https://aws.amazon.com/https://aws.amazon.com/marketplace/pp/B01M0AXXQB "https://aws.amazon.com/https://aws.amazon.com/marketplace/pp/B01M0AXXQB"). Then, configure the AMI to run AWS Batch jobs. For more information, see [Use a GPU workload AMI](batch-gpu-ami.md "batch-gpu-ami.md").

###### Important

You can choose a base AMI that doesn't support the `ecs-init` package.
However, if you do, you must configure a way to start the Amazon ECS agent at boot and keep it
running. You can also view several example user data configuration scripts that use
`systemd` to start and monitor the Amazon ECS container agent. For more information, see
[Example container instance user data
configuration scripts](../../../AmazonECS/latest/developerguide/example_user_data_scripts.md "../../../AmazonECS/latest/developerguide/example_user_data_scripts.md") in the _Amazon Elastic Container Service Developer Guide_. 2. Launch an instance from your selected base AMI with the appropriate storage options for
your AMI. You can configure the size and number of attached Amazon EBS volumes, or instance storage
volumes if the instance type you selected supports them. For more information, see [Launching an Instance](../../../AWSEC2/latest/UserGuide/launching-instance.md "../../../AWSEC2/latest/UserGuide/launching-instance.md") and [Amazon EC2 Instance Store](../../../AWSEC2/latest/UserGuide/InstanceStorage.md "../../../AWSEC2/latest/UserGuide/InstanceStorage.md") in the
_Amazon EC2 User Guide_. 3. Connect to your instance with SSH and perform any necessary configuration
tasks. This might include any or all of the following steps:

    * Installing the Amazon ECS container agent. For more information, see [Installing the Amazon ECS Container Agent](../../../AmazonECS/latest/developerguide/ecs-agent-install.md "../../../AmazonECS/latest/developerguide/ecs-agent-install.md") in the
     *Amazon Elastic Container Service Developer Guide*.
    * Configuring a script to format instance store volumes.
    * Adding instance store volume or Amazon EFS file systems to the `/etc/fstab` file so that
     they're mounted at boot.
    * Configuring Docker options, such as enabling debugging or adjusting base image size.
    * Installing packages or copying files.

For more information, see [Connecting to Your Linux
Instance Using SSH](../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md "../../../AWSEC2/latest/UserGuide/AccessingInstancesLinux.md") in the _Amazon EC2 User Guide_. 4. If you started the Amazon ECS container agent on your instance, you must stop it and remove any
persistent data checkpoint files before creating your AMI. Otherwise, if you don't do this,
the agent doesn't start on instances that are launched from your AMI.

    1. Stop the Amazon ECS container agent.




    	* Amazon ECS-optimized Amazon Linux 2 AMI:



    	```
    	`sudo systemctl stop ecs`
    	```
    	* Amazon ECS-optimized Amazon Linux AMI:



    	```
    	`sudo stop ecs`
    	```
    2. Remove the persistent data checkpoint files. By default, these files are located in the
     `/var/lib/ecs/data/` directory. Use the following command to remove these
     files, if there are any.



    ```
    `sudo rm -rf /var/lib/ecs/data/*`
    ```

5. Create a new AMI from your running instance. For more information, see [Creating an Amazon EBS Backed Linux AMI](../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md "../../../AWSEC2/latest/UserGuide/creating-an-ami-ebs.md") in
   the _Amazon EC2 User Guide_ guide.

###### To use your new AMI with AWS Batch

1. After the new AMI is created, create a compute environment with the new AMI. To do
   this,choose the image type and enter the custom AMI ID in the **Image ID
   override** box when you create the AWS Batch compute environment. For more information,
   see [Tutorial: Create a managed compute
   environment using Amazon EC2 resources](create-compute-environment-managed-ec2.md "create-compute-environment-managed-ec2.md").

###### Note

The AMI that you choose for a compute environment must match the architecture of the instance types that
you intend to use for that compute environment. For example, if your compute environment uses A1 instance types,
the compute resource AMI that you choose must support ARM instances. Amazon ECS vends both x86 and ARM versions of the
Amazon ECS optimized Amazon Linux 2 AMI. For more information, see [Amazon ECS optimized Amazon Linux 2 AMI](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#ecs-optimized-ami-linux-variants.html")
in the _Amazon Elastic Container Service Developer Guide_. 2. Create a job queue and associate your new compute environment. For more information, see [Create a job queue](create-job-queue.md "create-job-queue.md").

###### Note

All compute environments that are associated with a job queue must share the same architecture. AWS Batch
doesn't support mixing compute environment architecture types in a single job queue. 3. (Optional) Submit a sample job to your new job queue. For more information, see [Job definition examples](example-job-definitions.md "example-job-definitions.md"), [Create a single-node job definition](create-job-definition.md "create-job-definition.md") , and [Tutorial: submit a job](submit_job.md "submit_job.md").
