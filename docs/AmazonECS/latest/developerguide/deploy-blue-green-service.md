

# Creating an Amazon ECS blue/green deployment
<a name="deploy-blue-green-service"></a>

 By using Amazon ECS blue/green deployments, you can make and test service changes before implementing them in a production environment. 

## Prerequisites
<a name="deploy-blue-green-service-prerequisites"></a>

Perform the following operations before you start a blue/green deployment. 

1. Configure the appropriate permissions.
   + For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md).
   + For information about Lambda permissions, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md)

1. (Optional) For managed traffic shifting, configure one of the following resources. If your service is headless (no load balancer or Service Connect), you can skip this step. Amazon ECS doesn't manage the traffic shift automatically for headless services.
   + Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md).
   + Network Load Balancer - For more information, see [Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments](nlb-resources-for-blue-green.md).
   + Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md).

1. Decide if you want to run Lambda functions for the lifecycle stages.
   + PRE\_SCALE\_UP
   + POST\_SCALE\_UP
   + TEST\_TRAFFIC\_SHIFT
   + POST\_TEST\_TRAFFIC\_SHIFT
   + PRODUCTION\_TRAFFIC\_SHIFT
   + POST\_PRODUCTION\_TRAFFIC\_SHIFT

   For more information, see [Create a Lambda function with the console](https://docs.aws.amazon.com/lambda/latest/dg/getting-started.html#getting-started-create-function) in the *AWS Lambda Developer Guide*.

## Procedure
<a name="deploy-blue-green-service-procedure"></a>

You can use the console or the AWS CLI to create an Amazon ECS blue/green service.

------
#### [ Console ]

1. Open the console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).

1. Determine the resource from where you launch the service.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-blue-green-service.html)

   The **Create service** page displays.

1. Under **Service details**, do the following:

   1. For **Task definition family**, choose the task definition to use. Then, for **Task definition revision**, enter the revision to use.

   1. For **Service name**, enter a name for your service.

1. To run the service in an existing cluster, for **Existing cluster**, choose the cluster. To run the service in a new cluster, choose **Create cluster** 

1. Choose how your tasks are distributed across your cluster infrastructure. Under **Compute configuration**, choose your option.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-blue-green-service.html)

1. Under **Deployment configuration**, do the following:

   1. For **Service type**, choose **Replica**.

   1. For **Desired tasks**, enter the number of tasks to launch and maintain in the service.

   1. To have Amazon ECS monitor the distribution of tasks across Availability Zones, and redistribute them when there is an imbalance, under **Availability Zone service rebalancing**, select **Availability Zone service rebalancing**.

   1. For **Health check grace period**, enter the amount of time (in seconds) that the service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container health checks after a task has first started. If you do not specify a health check grace period value, the default value of 0 is used.

1. 

   1. For **Bake time**, enter the number of minutes that both the blue and green service revisions will run simultaneously before the blue revision is terminated. This allows time for verification and testing.

   1. (Optional) Configure lifecycle hooks to run at specific stages of the deployment. Under **Deployment lifecycle hooks**, choose **Add**.

      For Lambda hooks:
      + For **Target type**, choose **Lambda**.
      + For **Lambda function**, enter the function name or ARN.
      + For **Role**, select the IAM role that has permission to invoke the Lambda function.
      + For **Lifecycle stages**, select the stages when the Lambda function should run.

      For pause hooks:
      + For **Target type**, choose **Pause**.
      + For **Lifecycle stages**, select the stages where the deployment should pause.
      + (Optional) For **Timeout**, configure the timeout duration and action.

1. To configure how Amazon ECS detects and handles deployment failures, expand **Deployment failure detection**, and then choose your options. 

   1. To stop a deployment when the tasks cannot start, select **Use the Amazon ECS deployment circuit breaker**.

      To have the software automatically roll back the deployment to the last completed deployment state when the deployment circuit breaker sets the deployment to a failed state, select **Rollback on failures**.

   1. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**. Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm, go to the CloudWatch console.

      To have the software automatically roll back the deployment to the last completed deployment state when a CloudWatch alarm sets the deployment to a failed state, select **Rollback on failures**.

1. (Optional) To interconnect your service using Service Connect, expand **Service Connect**, and then specify the following:

   1.  Select **Turn on Service Connect**.

   1. Under **Service Connect configuration**, specify the client mode.
      + If your service runs a network client application that only needs to connect to other services in the namespace, choose **Client side only**.
      + If your service runs a network or web service application and needs to provide endpoints for this service, and connects to other services in the namespace, choose **Client and server**.

   1. To use a namespace that is not the default cluster namespace, for **Namespace**, choose the service namespace. This can be a namespace created separately in the same AWS Region in your AWS account or a namespace in the same Region that is shared with your account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace sharing](https://docs.aws.amazon.com/cloud-map/latest/dg/sharing-namespaces.html) in the *AWS Cloud Map Developer Guide*.

   1. (Optional) Configure test traffic header rules for blue/green deployments. Under **Test traffic routing**, specify the following:

      1. Select **Enable test traffic header rules** to route specific requests to the green service revision during testing.

      1. For **Header matching rules**, configure the criteria for routing test traffic:
         + **Header name**: Enter the name of the HTTP header to match (for example, `X-Test-Version` or `User-Agent`).
         + **Match type**: Choose the matching criteria:
           + **Exact match**: Route requests where the header value exactly matches the specified value
           + **Header present**: Route requests that contain the specified header, regardless of value
           + **Pattern match**: Route requests where the header value matches a specified pattern
         + **Header value** (if using exact match or pattern match): Enter the value or pattern to match against.

         You can add multiple header matching rules to create complex routing logic. Requests matching any of the configured rules will be routed to the green service revision for testing.

      1. Choose **Add header rule** to configure additional header matching conditions.
**Note**  
Test traffic header rules enable you to validate new functionality with controlled traffic before completing the full deployment. This allows you to test the green service revision with specific requests (such as those from internal testing tools or beta users) while maintaining normal traffic flow to the blue service revision.

   1. (Optional) Specify a log configuration. Select **Use log collection**. The default option sends container logs to CloudWatch Logs. The other log driver options are configured using AWS FireLens. For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md).

      The following describes each container log destination in more detail.
      + **Amazon CloudWatch** – Configure the task to send container logs to CloudWatch Logs. The default log driver options are provided, which create a CloudWatch log group on your behalf. To specify a different log group name, change the driver option values.
      + **Amazon Data Firehose** – Configure the task to send container logs to Firehose. The default log driver options are provided, which send logs to a Firehose delivery stream. To specify a different delivery stream name, change the driver option values.
      + **Amazon Kinesis Data Streams** – Configure the task to send container logs to Kinesis Data Streams. The default log driver options are provided, which send logs to an Kinesis Data Streams stream. To specify a different stream name, change the driver option values.
      + **Amazon OpenSearch Service** – Configure the task to send container logs to an OpenSearch Service domain. The log driver options must be provided. 
      + **Amazon S3** – Configure the task to send container logs to an Amazon S3 bucket. The default log driver options are set by default, but you must specify a valid Amazon S3 bucket name.

1. (Optional) Configure **Load balancing** for blue/green deployment.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/deploy-blue-green-service.html)

1. (Optional) To help identify your service and tasks, expand the **Tags** section, and then configure your tags.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the task definition tags, select **Turn on Amazon ECS managed tags**, and then for **Propagate tags from**, choose **Task definitions**.

   To have Amazon ECS automatically tag all newly launched tasks with the cluster name and the service tags, select **Turn on Amazon ECS managed tags**, and then for **Propagate tags from**, choose **Service**.

   Add or remove a tag.
   + [Add a tag] Choose **Add tag**, and then do the following:
     + For **Key**, enter the key name.
     + For **Value**, enter the key value.
   + [Remove a tag] Next to the tag, choose **Remove tag**.

1. Choose **Create**.

------
#### [ AWS CLI ]

1. Create a file named `service-definition.json` with the following content.

   Replace the {{user-input}} with your values.

   ```
   {
     "serviceName": "{{myBlueGreenService}}",
     "cluster": "{{arn:aws:ecs:us-west-2:123456789012:cluster/sample-fargate-cluster}}",
     "taskDefinition": "{{sample-fargate:1}}",
     "desiredCount": 5,
     "launchType": "FARGATE",
     "networkConfiguration": {
       "awsvpcConfiguration": {
         "subnets": [
           "{{subnet-09ce6e74c116a2299}}",
           "{{subnet-00bb3bd7a73526788}}",
           "{{subnet-0048a611aaec65477}}"
         ],
         "securityGroups": [
           "{{sg-09d45005497daa123}}"
         ],
         "assignPublicIp": "ENABLED"
       }
     },
     "deploymentController": {
       "type": "ECS"
     },
     "deploymentConfiguration": {
       "strategy": "BLUE_GREEN",
       "maximumPercent": 200,
       "minimumHealthyPercent": 100,
       "bakeTimeInMinutes": 2,
       "alarms": {
         "alarmNames": [
           "myAlarm"
         ],
         "rollback": true,
         "enable": true
       },
       "lifecycleHooks": [
         {
           "hookTargetArn": "{{arn:aws:lambda:us-west-2:7123456789012:function:checkExample}}",
           "roleArn": "{{arn:aws:iam::123456789012:role/ECSLifecycleHookInvoke}}",
           "lifecycleStages": [
             "PRE_SCALE_UP"
           ],
           "hookDetails": {
             "{{MY_CONFIG_KEY}}": "{{my-config-value}}"
           }
         }
       ]
     },
     "loadBalancers": [
       {
         "targetGroupArn": "{{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/blue-target-group/54402ff563af1197}}",
         "containerName": "{{fargate-app}}",
         "containerPort": 80,
         "advancedConfiguration": {
           "alternateTargetGroupArn": "{{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/green-target-group/cad10a56f5843199}}",
           "productionListenerRule": "{{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-blue-green-demo/32e0e4f946c3c05b/9cfa8c482e204f7d/831dbaf72edb911}}",
           "roleArn": "{{arn:aws:iam::123456789012:role/LoadBalancerManagementforECS}}"
         }
       }
     ]
   }
   ```

1. Run `create-service`.

   Replace the {{user-input}} with your values.

   ```
   aws ecs create-service --cli-input-json file://service-definition.json
   ```

   Alternatively, you can use the following example which creates a blue/green deployment service with a load balancer configuration:

   ```
   aws ecs create-service \
      --cluster "{{arn:aws:ecs:us-west-2:123456789012:cluster/MyCluster}}" \
      --service-name "blue-green-example-service" \
      --task-definition "nginxServer:1" \
      --launch-type "FARGATE" \
      --network-configuration "awsvpcConfiguration={subnets=[{{subnet-12345}},{{subnet-67890}},{{subnet-abcdef}},{{subnet-fedcba}}],securityGroups=[{{sg-12345}}],assignPublicIp=ENABLED}" \
      --desired-count 3 \
      --deployment-controller "type=ECS" \
      --deployment-configuration "strategy=BLUE_GREEN,maximumPercent=200,minimumHealthyPercent=100,bakeTimeInMinutes=0" \
      --load-balancers "targetGroupArn={{arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/MyBGtg1/abcdef1234567890}},containerName=nginx,containerPort=80,advancedConfiguration={alternateTargetGroupArn={{arn:aws:elasticloadbalancing:us-west-2:123456789012}}:{{targetgroup/MyBGtg2/0987654321fedcba}},productionListenerRule={{arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/MyLB/1234567890abcdef/1234567890abcdef}},roleArn={{arn:aws:iam::123456789012:role/ELBManagementRole}}}"
   ```

------

## Next steps
<a name="deploy-blue-green-service-next-steps"></a>
+ Update the service to start the deployment. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md).
+ Monitor the deployment process to ensure it follows the blue/green pattern:
  + The green service revision is created and scaled up
  + Test traffic is routed to the green revision (if configured)
  + Production traffic is shifted to the green revision
  + After the bake time, the blue revision is terminated