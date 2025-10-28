# Connect to a AWS PCS cluster created with

AWS CloudFormation

After you create an AWS PCS cluster from a AWS CloudFormation template, you can use the AWS PCS console
(in the AWS Management Console) to administer the cluster. You can also connect to 1 of the cluster's
login nodes to administer the cluster, run jobs, and manage data. The AWS CloudFormation stack provides
links you can use to connect to your cluster.

###### To connect to your cluster

1. Open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation")
2. Choose the stack you created.
3. Choose the **Outputs** tab of the stack.

The stack provides the following links:

    * **PcsConsoleUrl** — Choose this link
     to open the AWS PCS console with the cluster selected. You can use it
     to explore the cluster, node group, and queue configurations.
    * **Ec2ConsoleUrl** — Choose this link
     to open the Amazon EC2 console, filtered to show
     the instances that the cluster's login node group manages.


    From this view, you can select an instance and choose
     **Connect**. The sample cluster's instance
     supports inbound SSH and AWS Systems Manager connections in a web browser. For
     more information, see [Connect to your AWS PCS cluster](getting-started_connect.md "getting-started_connect.md").


    After you connect to a login instance, you can follow the tutorial
     at [Explore the cluster environment in AWS PCS](getting-started_explore.md "getting-started_explore.md").
