

# Updating an Amazon ECS Express Mode service
<a name="express-service-update-full"></a>

The Express Mode service simplifies the service update process by providing configurable options for networking, load balancing, and Application Auto Scaling and orchestrating changes across these services.

You can update your Express Mode service to modify container images, adjust resource allocation, or change configuration settings. Updates are deployed using canary deployments with alarm based rollback alarms to maintain availability.

## Deployment behavior
<a name="express-service-update-full-behavior"></a>

An Express Mode service uses canary deployments by default to ensure safe updates and quick rollbacks:
+ A new environment is created and tasks deployed with your changes
+ 5% of traffic is shifted to the new environment
+ Alarm Based Rollbacks will trigger if sum of 4xx and 5xx errors percentage is > 1 for 2 datapoints within 3 minutes
+ Health checks verify the new tasks are healthy
+ After 3 minutes bake time, 100% of traffic is shifted to new environment
+ After 3 minutes bake time for monitoring, old tasks are gradually stopped and replaced

For more information, see [Amazon ECS canary deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/canary-deployment.html)

## Procedure
<a name="express-service-update-full-procedure"></a>

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. In the navigation pane, choose **Clusters**.

1. On the **Clusters** page, choose the name of the cluster that contains your Express Mode service.

1. On the cluster details page, choose the **Services** tab.

1. Configure a filter to view your Express Mode services. For **Filter resource management type**, choose **ECS**.

   An Express Mode service has a **Express** badge next to the name.

1. Under **Configuration**:

   1. Specify the image to use for your application. For **Image URI**, enter the URI for your image. To browse your Amazon ECR images, choose **Browse ECR images**, and then do the following:

      1. For **Private repository**, choose the Amazon ECR private repository.

      1. For **Image**, choose your image.

      1. Choose how to identify the image. For **Select image by**, choose one of the following options:
         + AWS recommends that you choose **Image digest**.
         + To use the tag, choose **Image tag** and then choose the tag.

   1. To use a private registry, select **Private registry**. Then, for **Secrets Manager ARN or name**, enter the Secrets Manager ARN you created in the prerequisites.

   1. For **Task execution role**, choose the roles or create a new role and refresh. You can update the task execution role when you need to add additional permissions.

1. Under **Additional configurations**, customize your service.

   1. Under **Container**:

      1. For **Container port**, update the port your application listens on (default is 80).

      1. For **Health check path**, update the path for health checks (for example, `/health`).

   1. Under **Environment variables**, add key-value pairs for environment variables your application needs:

      1. For **Key**, enter the environment variable name.

      1. For **Value type**, choose **Environment variable** or **Secret**.

      1. For **Value or value from**, enter the value or reference.

      1. Choose **Add environment variable** to add more variables as needed.

   1. For **Command**, optionally enter a custom command to override the Docker CMD instruction.

   1. For **Task role**, add an IAM role that grants permissions to your application running in your containers. This allows your application to make API calls to AWS services.

   1. Under **Compute**:

      1. For **CPU**, update the vCPU allocation for your tasks (for example, 1 vCPU).

      1. For **Memory**, update the memory allocation for your tasks (for example, 2 GB).

   1. Under **Auto Scaling**:

      1. For **ECS service metric**, choose the metric to scale on (for example, **ECS Service Average Memory Utilization** or **Request count per target**).

      1. For **Target value**, enter the target for scaling (for example, **60** or **1000**).

      1. For **Minimum number of tasks** and **Maximum number of tasks**, update the scaling limits.

   1. Under **Logs**:

      1. For **Amazon CloudWatch log group**, update the log group name for your application logs. Note this will not move existing logs, but begin writing logs from the new service revision.

      1. For **Amazon CloudWatch log stream prefix**, enter a new prefix for log streams.

1. Choose **Update** to update your Express Mode service.

### Updating with a custom task definition
<a name="express-service-update-custom-td"></a>

You can update your Express Mode service with a custom task definition by specifying the `taskDefinitionArn` parameter. Express Mode uses your task definition as-is and continues to manage the rest of the infrastructure.

On subsequent updates, you can either:
+ Create a new revision of your task definition and update the `taskDefinitionArn`. Express Mode uses the new revision for the next service deployment.
+ Update Express Mode parameters directly:
  + For parameters unrelated to the task definition (such as `healthCheckPath`, `networkConfiguration`, or `scalingTarget`), Express Mode applies the changes without modifying the task definition.
  + For task-definition related parameters (such as image, CPU, or memory using `primaryContainer` or `cpu`/`memory`), Express Mode creates a new managed task definition with your changes while preserving your other task-level configuration.

**To update with a custom task definition (Amazon ECS console)**

1. Open the Amazon ECS console and navigate to your Express Mode service.

1. Choose the dropdown arrow next to **Update service**, then choose **Update with custom task definition**.

1. For **Task definition family**, select an existing task definition family. To create a new task definition, choose the **Task definitions** link.

1. For **Task definition revision**, select the revision to use, or leave blank to use the latest revision.

1. (Optional) Expand **Additional configurations** to update health check path, networking, or auto scaling settings.

1. Choose **Update**.

The following AWS AWS CLI command updates your Express Mode service with a custom task definition:

```
aws ecs update-express-gateway-service \
    --service-arn arn:aws:ecs:us-west-2:123456789012:service/default/my-service \
    --task-definition-arn arn:aws:ecs:us-west-2:123456789012:task-definition/my-td:4
```

**Note**  
If you use CloudFormation and are adding `taskDefinitionArn` to your Express Mode service for the first time, redeploy your stack once first. This ensures rollback compatibility.