# Creating a

capacity provider for Amazon ECS

After the cluster creation completes, you can create a new capacity provider (Amazon EC2 Auto Scaling
group) for EC2. Capacity providers help to manage and scale
your the infrastructure for your applications.

Before you create the capacity provider, you need to create an Amazon EC2 Auto Scaling group. For more
information, see [Amazon EC2 Auto Scaling groups](../../../autoscaling/ec2/userguide/auto-scaling-groups.md "../../../autoscaling/ec2/userguide/auto-scaling-groups.md") in the
_Amazon EC2 Amazon EC2 Auto Scaling User Guide_.

###### To create a capacity provider for the cluster (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster.
4. On the **Cluster : `name`** page, choose
   **Infrastructure**, and then choose
   **Create**.
5. On the **Create capacity providers** page, configure the
   following options.
   1. Under **Basic details**, for **Capacity provider
      name**, enter a unique capacity provider name.
   2. Under **Amazon EC2 Auto Scaling group**, for **Use an existing Amazon EC2 Auto Scaling
      group**, choose the Amazon EC2 Auto Scaling group.
   3. (Optional) To configure a scaling policy, under **Scaling
      policies**, configure the following options.
      - To have Amazon ECS manage the scale-in and scale-out actions, select
        **Turn on managed scaling**.
      - To prevent EC2 instance with running Amazon ECS tasks from being
        terminated, select **Turn on scaling
        protection**.
      - For **Set target capacity**, enter the target
        value for the CloudWatch metric used in the Amazon ECS-managed target tracking
        scaling policy.

6. Choose **Create**.
