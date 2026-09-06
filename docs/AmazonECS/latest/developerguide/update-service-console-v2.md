

# Updating an Amazon ECS service
<a name="update-service-console-v2"></a>

After you create a service, there are times when you might need to update the service parameters, for example the number of tasks.

When you update a service that uses Amazon ECS circuit breaker, Amazon ECS creates a service deployment and a service revision. These resources allow you to view detailed information about the service history. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md).

## Prerequisites
<a name="update-service-prerequisites"></a>

Before updating a service, verify which service parameters can be changed for your deployment type. For a complete list of changeable parameters, see [Update Amazon ECS service parameters](update-service-parameters.md).

## Procedure
<a name="update-service-procedure"></a>

------
#### [ Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. On the **Clusters** page, choose the cluster.

1. On the cluster details page, in the **Services** section, select the check box next to the service, and then choose **Update**.

1. To have your service start a new deployment, select **Force new deployment**.

1. For **Task definition**, choose the task definition family and revision.
**Important**  
The console validates that the selected task definition family and revision are compatible with the defined compute configuration. If you receive a warning, verify both your task definition compatibility and the compute configuration that you selected.

1. If you chose **Replica**, for **Desired tasks**, enter the number of tasks to launch and maintain in the service.

1. If you chose **Replica**, to have Amazon ECS monitor the distribution of tasks across Availability Zones, and redistribute them when there is an imbalance, under **Availability Zone service rebalancing**, select **Availability Zone service rebalancing**.

1. For **Min running tasks**, enter the lower limit on the number of tasks in the service that must remain in the `RUNNING` state during a deployment, as a percentage of the desired number of tasks (rounded up to the nearest integer). For more information, see [Deployment configuration](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html#sd-deploymentconfiguration).

1. For **Max running tasks**, enter the upper limit on the number of tasks in the service that are allowed in the `RUNNING` or `PENDING` state during a deployment, as a percentage of the desired number of tasks (rounded down to the nearest integer).

1. To configure how tasks are deployed for your service, expand **Deployment options** and then configure your options.

   1. For **Deployment controller type**, specify the service deployment controller. The Amazon ECS console supports the following controller types: `ECS`.

   1. For **Deployment strategy**, choose the strategy used by Amazon ECS to deploy new versions of the service.

   1. Depending on the choice of **Deployment strategy**, do the following:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html)

   1. To run Lambda functions for a lifecycle stage, under **Deployment lifecyce hooks** do the following for each unique Lambda function:

      1. Choose **Add**.

         Repeat for every unique function you want to run.

      1. For **Lambda function**, enter the function name.

      1. For **Role**, choose the role that you created in the prerequisites with the blue/green permissions.

         For more information, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md).

      1. For **Lifecycle stages**, select the stages the Lambda function runs.

      1.  (Optional) For **Hook details**, enter a key value pair that provides information about the hook.

1. Under **Deployment configuration**, to complete the deployment before the target service revision reaches the full desired count, configure early success criteria. You can also choose when Amazon ECS cleans up the tasks on the source service revision.

   1. Turn on **Early success criteria**.

   1. For **Healthy percent**, enter the percentage of tasks that must be running and healthy on the target service revision before Amazon ECS completes the deployment.

   1. For **Source service revision cleanup**, choose **Blocking** or **Deferred**.

1. To configure how Amazon ECS detects and handles deployment failures, expand **Deployment failure detection**, and then choose your options. 

   1. To stop a deployment when the tasks cannot start, select **Use the Amazon ECS deployment circuit breaker**.

      To have the software automatically roll back the deployment to the last completed deployment state when the deployment circuit breaker sets the deployment to a failed state, select **Rollback on failures**.

   1. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**. Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm, go to the CloudWatch console.

      To have the software automatically roll back the deployment to the last completed deployment state when a CloudWatch alarm sets the deployment to a failed state, select **Rollback on failures**.

1. To change the compute options, expand **Compute configuration**, and then do the following: 

   1. For services on AWS Fargate, for **Platform version**, choose the new version.

   1. For services that use a capacity provider strategy, for **Capacity provider strategy**, do the following:
      + To add an additional capacity provider, choose **Add more**. Then, for **Capacity provider**, choose the capacity provider.
      + To remove a capacity provider, to the right of the capacity provider, choose **Remove**.

      A service that's using an Auto Scaling group capacity provider can't be updated to use a Fargate capacity provider. A service that's using a Fargate capacity provider can't be updated to use an Auto Scaling group capacity provider.

1. (Optional) To configure service Auto Scaling, expand **Service auto scaling**, and then specify the following parameters.To use predicte auto scaling, which looks at past load data from traffic flows, configure it after you create the service. For more information, see [Use historical patterns to scale Amazon ECS services with predictive scaling](predictive-auto-scaling.md).

   1. To use service auto scaling, select **Service auto scaling**.

   1. For **Minimum number of tasks**, enter the lower limit of the number of tasks for service auto scaling to use. The desired count will not go below this count.

   1. For **Maximum number of tasks**, enter the upper limit of the number of tasks for service auto scaling to use. The desired count will not go above this count.

   1. Choose the policy type. Under **Scaling policy type**, choose one of the following options.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html)

1. (Optional) To use Service Connect, select **Turn on Service Connect**, and then specify the following:

   1. Under **Service Connect configuration**, specify the client mode.
      + If your service runs a network client application that only needs to connect to other services in the namespace, choose **Client side only**.
      + If your service runs a network or web service application and needs to provide endpoints for this service, and connects to other services in the namespace, choose **Client and server**.

   1. To use a namespace that is not the default cluster namespace, for **Namespace**, choose the service namespace. This can be a namespace created separately in the same AWS Region in your AWS account or a namespace in the same Region that is shared with your account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the *AWS Cloud Map Developer Guide*

   1. (Optional) Specify a log configuration. Select **Use log collection**. The default option sends container logs to CloudWatch Logs. The other log driver options are configured using AWS FireLens. For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md).

      The following describes each container log destination in more detail.
      + **Amazon CloudWatch** – Configure the task to send container logs to CloudWatch Logs. The default log driver options are provided, which create a CloudWatch log group on your behalf. To specify a different log group name, change the driver option values.
      + **Amazon Data Firehose** – Configure the task to send container logs to Firehose. The default log driver options are provided, which send logs to a Firehose delivery stream. To specify a different delivery stream name, change the driver option values.
      + **Amazon Kinesis Data Streams** – Configure the task to send container logs to Kinesis Data Streams. The default log driver options are provided, which send logs to an Kinesis Data Streams stream. To specify a different stream name, change the driver option values.
      + **Amazon OpenSearch Service** – Configure the task to send container logs to an OpenSearch Service domain. The log driver options must be provided. 
      + **Amazon S3** – Configure the task to send container logs to an Amazon S3 bucket. The default log driver options are set by default, but you must specify a valid Amazon S3 bucket name.

   1. To enable access logs, follow these steps:

      1. Expand **Access log configuration**. For **Format**, choose either **JSON** or `TEXT`.

      1. To include query parameters in access logs, select **Include query parameters**.
**Note**  
To disable access logs, for **Format**, choose **None**.

1. If your task uses a data volume that's compatible with configuration at deployment, you can configure the volume by expanding **Volume**.

   The volume name and volume type are configured when you create a task definition revision and can't be changed when you update a service. To update the volume name and type, you must create a new task definition revision and update the service by using the new revision.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html)

1. (Optional) To help identify your service, expand the **Tags** section, and then configure your tags.
   + [Add a tag] Choose **Add tag**, and do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Update**.

------
#### [ AWS CLI ]
+ Run `update-service`. For information about running the command, see [update-service](https://docs.aws.amazon.com/cli/latest/reference/ecs/update-service.html) in the AWS Command Line Interface Reference. 

  The following `update-service` example updates the desired task count of the service `my-http-service` to 2.

  Replace the {{user-input}} with your values.

  ```
  aws ecs update-service \
      --cluster {{MyCluster}} \
      --service {{my-http-service}} \
      --desired-count 2
  ```

------

## Next steps
<a name="update-service-next-steps"></a>

Track your deployment and view your service history for services that Amazon ECS circuit breaker. For more information, see [View service history using Amazon ECS service deployments](service-deployment.md).