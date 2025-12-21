# Updating an Amazon ECS Express Mode service

The Express Mode service simplifies the service update process by providing configurable
options for networking, load balancing, and Application Auto Scaling and orchestrating changes across these services.

You can update your Express Mode service to modify container images, adjust resource
allocation, or change configuration settings. Updates are deployed using canary deployments with alarm based rollback alarms
to maintain availability.

## Deployment behavior

An Express Mode service uses canary deployments by default to ensure safe
updates and quick rollbacks:

- A new environment is created and tasks deployed with your changes
- 5% of traffic is shifted to the new environment
- Alarm Based Rollbacks will trigger if sum of 4xx and 5xx errors percentage is > 1 for 2 datapoints within 3 minutes
- Health checks verify the new tasks are healthy
- After 3 minutes bake time, 100% of traffic is shifted to new environment
- After 3 minutes bake time for monitoring, old tasks are gradually stopped and replaced

For more information, see [Amazon ECS canary deployments](canary-deployment.md "canary-deployment.md")

## Procedure

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. In the navigation pane, choose **Clusters**.
3. On the **Clusters** page, choose the name of the cluster that
   contains your Express Mode service.
4. On the cluster details page, choose the **Services** tab.
5. Configure a filter to view your Express Mode services. For **Filter resource
   management type**, choose **ECS**.

An Express Mode service has a **Express** badge next to the
name. 6. Under **Configuration**:

    1. Specify the image to use for your application. For **Image URI**, enter the URI for your image. To browse your Amazon ECR images, choose **Browse ECR images**, and then do the following:


    	1. For **Private repository**, choose the Amazon ECR private repository.
    	2. For **Image**, choose your image.
    	3. Choose how to identify the image. For **Select image by**, choose one of the following options:




    		* AWS recommends that you choose **Image digest**.
    		* To use the tag, choose **Image tag** and then choose the tag.
    2. To use a private registry, select **Private registry**.
     Then, for **Secrets Manager ARN or name**, enter the Secrets Manager
     ARN you created in the prerequisites.
    3. For **Task execution role**, choose the roles or create a new role and refresh. You can update the task execution role when you need to add additional permissions.

7. Under **Additional configurations**, customize your service.
   1. Under **Container**:
      1. For **Container port**, update the port your application listens on (default is 80).
      2. For **Health check path**, update the path for health checks (for example, `/health`).

   2. Under **Environment variables**, add key-value pairs for environment variables your application needs:
      1. For **Key**, enter the environment variable name.
      2. For **Value type**, choose **Environment variable** or **Secret**.
      3. For **Value or value from**, enter the value or reference.
      4. Choose **Add environment variable** to add more variables as needed.

   3. For **Command**, optionally enter a custom command to override the Docker CMD instruction.
   4. For **Task role**, add an IAM role that grants permissions to your application running in your containers. This allows your application to make API calls to AWS services.
   5. Under **Compute**:
      1. For **CPU**, update the vCPU allocation for your tasks (for example, 1 vCPU).
      2. For **Memory**, update the memory allocation for your tasks (for example, 2 GB).

   6. Under **Auto Scaling**:
      1. For **ECS service metric**, choose the metric to scale on (for example, **ECS Service
         Average Memory Utilization** or **Request count per target**).
      2. For **Target value**, enter the target for scaling (for example, **60** or **1000**).
      3. For **Minimum number of tasks** and **Maximum number of tasks**, update the scaling limits.

   7. Under **Logs**:
      1. For **Amazon CloudWatch log group**, update the log group name for your application logs. Note this will not move existing logs, but begin writing logs from the new service revision.
      2. For **Amazon CloudWatch log stream prefix**, enter a new prefix for log streams.

8. Choose **Update** to update your Express Mode service.
