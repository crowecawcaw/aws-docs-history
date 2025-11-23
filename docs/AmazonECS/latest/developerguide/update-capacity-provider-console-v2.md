# Updating an Amazon ECS capacity

provider

When you use an Amazon EC2 Auto Scaling group as a capacity provider, you can modify the group's scaling
policy.

###### To update a capacity provider for the cluster (Amazon ECS console)

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the cluster.
4. On the **Cluster : `name`** page, choose
   **Infrastructure**, and then choose
   **Update**.
5. On the **Create capacity providers** page, configure the
   following options.
   1. Under **Amazon EC2 Auto Scaling group**, under **Scaling
      policies**, configure the following options.
      - To have Amazon ECS manage the scale-in and scale-out actions, select
        **Turn on managed scaling**.
      - To prevent EC2 instances with running Amazon ECS tasks from being
        terminated, select **Turn on scaling
        protection**.
      - For **Set target capacity**, enter the target
        value for the CloudWatch metric used in the Amazon ECS-managed target tracking
        scaling policy.

6. Choose **Update**.
