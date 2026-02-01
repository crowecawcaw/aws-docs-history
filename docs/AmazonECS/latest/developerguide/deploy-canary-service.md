# Creating an Amazon ECS canary deployment

By using Amazon ECS canary deployments, you can shift a small percentage of traffic to your new
service revision (the "canary"). Validate the deployment, and then shift the remaining
traffic all at once after a specified interval. This approach allows you to test new
functionality with minimal risk before full deployment.

## Prerequisites

Perform the following operations before you start a canary deployment.

1. Configure the appropriate permissions.
   - For information about Elastic Load Balancing permissions, see [Amazon ECS infrastructure
     IAM role for load balancers](AmazonECSInfrastructureRolePolicyForLoadBalancers.md "AmazonECSInfrastructureRolePolicyForLoadBalancers.md").
   - For information about Lambda permissions, see [Permissions required for Lambda functions in Amazon ECS blue/green deployments](blue-green-permissions.md "blue-green-permissions.md").

2. Amazon ECS canary deployments require that your service to use one of the
   following features: Configure the appropriate resources.
   - Application Load Balancer - For more information, see [Application Load Balancer resources for blue/green, linear, and canary deployments](alb-resources-for-blue-green.md "alb-resources-for-blue-green.md").
   - Network Load Balancer - For more information, see [Network Load Balancer resources for Amazon ECS blue/green, linear and canary deployments](nlb-resources-for-blue-green.md "nlb-resources-for-blue-green.md").
   - Service Connect - For more information, see [Service Connect resources for Amazon ECS blue/green, linear, and canary deployments](service-connect-blue-green.md "service-connect-blue-green.md").

## Procedure

You can use the console or the AWS CLI to create an Amazon ECS canary deployment service.

Console

1. Open the console at
   [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2 "https://console.aws.amazon.com/ecs/v2").
2. Determine the resource from where you launch the service.

| To start a service from | Steps                                                                                                                                                                             |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clusters                | 1. On the **Clusters\*<br>• page, select<br>the cluster to create the service in.<br>The cluster details page displays.<br>2. On the **Services\*<br>• tab, choose<br>**Create**. |
| Task definition         | 1. On the **Task definitions\*<br>• page,<br>select the task definition.<br>2. From the **Deploy\*<br>• menu, choose<br>**Create service**.                                       |

The **Create service** page displays. 3. Under **Service details**, do the following:

    1. For **Task definition family**, choose the task
     definition to use. Then, for **Task definition
     revision**, enter the revision to use.
    2. For **Service name**, enter a name for your
     service.

4. To run the service in an existing cluster, for **Existing
   cluster**, choose the cluster. To run the service in a new cluster,
   choose **Create cluster**
5. Choose how your tasks are distributed across your cluster infrastructure.
   Under **Compute configuration**, choose your option.

| Compute option             | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Capacity provider strategy | 1. Under **Compute options**, choose<br>**Capacity provider<br>strategy**.<br>2. Choose a strategy:<br>• To use the cluster's default capacity<br>provider strategy, choose **Use cluster<br>default**.<br>• If your cluster doesn't have a default<br>capacity provider strategy, or to use a custom<br>strategy, choose **Use custom**,<br>**Add capacity provider<br>strategy**, and then define your custom<br>capacity provider strategy by specifying a<br>**Base**, **Capacity<br>provider**, and<br>**Weight**.<br>NoteTo use a capacity provider in a strategy, the capacity<br>provider must be associated with the cluster. |
| Launch type                | 1. In the **Compute options**<br>section, select **Launch<br>type**.<br>2. For **Launch type**, choose a<br>launch type.<br>3. (Optional) When the Fargate is<br>specified, for **Platform<br>version**, specify the platform version to<br>use. If a platform version isn't specified, the<br>`LATEST` platform version is<br>used.                                                                                                                                                                                                                                                                                                   |

6.  Under **Deployment configuration**, do the following:
    1. For **Service type**, choose
       **Replica**.
    2. For **Desired
       tasks**, enter the number of tasks to launch and maintain
       in the service.
    3. To have Amazon ECS monitor the
       distribution of tasks across Availability Zones, and redistribute them
       when there is an imbalance, under **Availability Zone service
       rebalancing**, select **Availability Zone service
       rebalancing**.
    4. For **Health check grace period**, enter the amount
       of time (in seconds) that the service scheduler ignores unhealthy Elastic Load Balancing, VPC Lattice, and container
       health checks after a task has first started. If you do not specify a
       health check grace period value, the default value of 0 is used.

7.  Under **Deployment configuration**, configure the canary deployment settings:
    1. For **Deployment strategy**, choose **Canary**.
    2. For **Canary percentage**, enter the percentage of traffic to shift to the green service revision in the first stage (for example, 10% for the initial canary traffic).
    3. For **Canary bake time**, enter the time
       in minutes to wait before shifting the remaining traffic to
       the green service revision.
    4. For **Bake time**, enter the number of minutes that both the blue and green service revisions will run simultaneously after the final traffic shift before the blue revision is terminated.
    5. (Optional) Run Lambda functions to run at specific stages of the deployment. Under **Deployment lifecycle hooks**, select the stages to run the lifecycle hooks.

    To add a lifecycle hook:

        1. Choose **Add**.
        2. For **Lambda function**, enter the function name or ARN.
        3. For **Role**, select the IAM role that has permission to invoke the Lambda function.
        4. For **Lifecycle stages**, select the stages when the Lambda function should run.

8.  To configure how Amazon ECS detects and handles deployment failures, expand
    **Deployment failure detection**, and then choose
    your options.
    1. To stop a deployment when the tasks cannot start, select **Use the Amazon ECS
       deployment circuit breaker**.

    To have the software automatically roll back the deployment to the last
    completed deployment state when the deployment circuit breaker sets the
    deployment to a failed state, select **Rollback on
    failures**. 2. To stop a deployment based on application metrics, select **Use CloudWatch alarm(s)**.
    Then, from **CloudWatch alarm name**, choose the alarms. To create a new alarm,
    go to the CloudWatch console.

    To have the software automatically roll back the deployment to the last
    completed deployment state when a CloudWatch alarm sets the
    deployment to a failed state, select **Rollback on
    failures**.

9.  (Optional) To interconnect your service using Service Connect, expand
    **Service Connect**, and then specify the
    following:
    1.  Select **Turn on Service Connect**.
    2.  Under **Service Connect configuration**, specify the
        client mode.
        - If your service runs a network client application that only
          needs to connect to other services in the namespace, choose
          **Client side only**.
        - If your service runs a network or web service application and
          needs to provide endpoints for this service, and connects to
          other services in the namespace, choose **Client and
          server**.

    3.  To use a namespace that is not the default cluster namespace, for
        **Namespace**, choose the service namespace. This
        can be a namespace created separately in the same AWS Region in your
        AWS account or a namespace in the same Region that is shared with your
        account using AWS Resource Access Manager (AWS RAM). For more information about shared AWS Cloud Map namespaces, see [Cross-account AWS Cloud Map namespace
        sharing](../../../cloud-map/latest/dg/sharing-namespaces.md "../../../cloud-map/latest/dg/sharing-namespaces.md") in the _AWS Cloud Map Developer Guide_.
    4.  (Optional) Configure test traffic header rules for canary deployments. Under **Test traffic routing**, specify the following:
        1.  Select **Enable test traffic header rules** to route specific requests to the green service revision during testing.
        2.  For **Header matching rules**, configure the criteria for routing test traffic:

                * **Header name**: Enter the name of the HTTP header to match (for example, `X-Test-Version` or `User-Agent`).
                * **Match type**: Choose the matching criteria:




                	+ **Exact match**: Route requests where the header value exactly matches the specified value
                	+ **Header present**: Route requests that contain the specified header, regardless of value
                	+ **Pattern match**: Route requests where the header value matches a specified pattern
                * **Header value** (if using exact match or pattern match): Enter the value or pattern to match against.

            You can add multiple header matching rules to create complex routing logic. Requests matching any of the configured rules will be routed to the green service revision for testing.

        3.  Choose **Add header rule** to configure additional header matching conditions.###### Note

    Test traffic header rules enable you to validate new functionality with controlled traffic before completing the full deployment. This allows you to test the green service revision with specific requests (such as those from internal testing tools or beta users) while maintaining normal traffic flow to the blue service revision. 5. (Optional) Specify a log configuration. Select **Use log
    collection**. The default option sends container logs to
    CloudWatch Logs. The other log driver options are configured using AWS FireLens.
    For more information, see [Send Amazon ECS logs to an AWS service or AWS Partner](using_firelens.md "using_firelens.md").

    The following describes each container log destination in more
    detail.

        * **Amazon CloudWatch** – Configure the task to
         send container logs to CloudWatch Logs. The default log driver options are
         provided, which create a CloudWatch log group on your behalf. To
         specify a different log group name, change the driver option
         values.
        * **Amazon Data Firehose** – Configure the task to
         send container logs to Firehose. The default log driver options are
         provided, which send logs to a Firehose delivery stream. To specify
         a different delivery stream name, change the driver option
         values.
        * **Amazon Kinesis Data Streams** – Configure the task to
         send container logs to Kinesis Data Streams. The default log driver options are
         provided, which send logs to an Kinesis Data Streams stream. To specify a
         different stream name, change the driver option values.
        * **Amazon OpenSearch Service** – Configure the task to
         send container logs to an OpenSearch Service domain. The log driver options
         must be provided.
        * **Amazon S3** – Configure the task to send
         container logs to an Amazon S3 bucket. The default log driver options
         are provided, but you must specify a valid Amazon S3 bucket
         name.

10. (Optional) Configure **Load balancing** for canary
    deployment.

| Elastic Load Balancing type | Steps                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Application Load Balancer   | 1. For **Load balancer type**,<br>choose **Application Load Balancer**.<br>2. Choose **Create a new load<br>balancer\*<br>• to create a new Application<br>Load Balancer or **Use an existing load<br>balancer*<br>• to select an existing<br>Application Load Balancer.<br>3. For **Container**, choose the container<br>that hosts the service.<br>4. For **Load balancer name**, enter<br>a unique name.<br>5. For **Listener**, enter a port and<br>protocol for the Application Load Balancer to listen for connection<br>requests on. By default, the load balancer will be<br>configured to use port 80 and HTTP.<br>• For **Production rule**,<br>enter the **Evaluation order**<br>and \*\*Path pattern*<br>• for the<br>rule.<br>This rule is for your production (blue)<br>service revision traffic.<br>• For **Test rule**, enter<br>the **Evaluation order\*<br>• and<br>**Path pattern\*<br>• for the<br>rule.<br>This rule is for your test (green) service<br>revision traffic.<br>6. For **Target group**,<br>configure the following:<br>• For **Target group name**, enter<br>a name and a protocol for the target group that the<br>Application Load Balancer routes requests to.<br>• For **Protocol**, choose the protocol for the target group that the<br>Application Load Balancer routes requests to. By default, the target<br>group routes requests to the first container defined<br>in your task definition.<br>• For **Deregistration delay**,<br>enter the number of seconds for the load balancer to<br>change the target state to `UNUSED`. The<br>default is 300 seconds.<br>• For **Health check path**, enter<br>an existing path within your container where the<br>Application Load Balancer periodically sends requests to verify the<br>connection health between the Application Load Balancer and the<br>container. The default is the root directory<br>(`/`).<br>• For **Alternate group<br>name**, enter the group name for the<br>target group for your test service<br>revision. |
| Network Load Balancer       | 1. For **Load balancer type**,<br>select **Network Load Balancer**.<br>2. For **Load Balancer**, choose an<br>existing Network Load Balancer.<br>3. For **Choose container to load<br>balance**, choose the container that<br>hosts the service.<br>4. For **Production listener**,<br>choose the **Production listener<br>port**, and the **Production<br>listener protocol**.<br>This is the listener for your production<br>service revision traffic.<br>5. For **Test listener**, choose<br>the **Test listener port**, and<br>the **Test listener<br>protocol**.<br>This is the listener for your test<br>service revision traffic.<br>6. For **Target group**,<br>configure the following:<br>• For **Target group name**, enter<br>a name and a protocol for the target group that the<br>Network Load Balancer routes requests to.<br>• For **Protocol**, choose the protocol for the target group that the<br>Network Load Balancer routes requests to. By default, the target<br>group routes requests to the first container defined<br>in your task definition.<br>• For **Deregistration delay**,<br>enter the number of seconds for the load balancer to<br>change the target state to `UNUSED`. The<br>default is 300 seconds.<br>• For **Health check path**, enter<br>an existing path within your container where the<br>Application Load Balancer periodically sends requests to verify the<br>connection health between the Application Load Balancer and the<br>container. The default is the root directory<br>(`/`).<br>• For **Alternate group<br>name**, enter the group name for the<br>target group for your test (green) service<br>revision.                                                                                                                                                                                                                                                                                                                                                        |

11. (Optional) To help identify your service and tasks, expand the
    **Tags** section, and then configure your tags.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the task definition tags, select **Turn on Amazon ECS managed
tags**, and then for **Propagate tags from**,
choose **Task definitions**.

To have Amazon ECS automatically tag all newly launched tasks with the cluster name
and the service tags, select **Turn on Amazon ECS managed tags**,
and then for **Propagate tags from**, choose
**Service**.

Add or remove a tag.

    * [Add a tag] Choose **Add tag**, and then do the
     following:




    	+ For **Key**, enter the key name.
    	+ For **Value**, enter the key value.
    * [Remove a tag] Next to the tag, choose **Remove
     tag**.

12. Choose **Create**.

AWS CLI

1. Create a file named `canary-service-definition.json` with the following content.

Replace the `user-input` with your values.

```
{
  "serviceName": "myCanaryService",
  "cluster": "arn:aws:ecs:us-west-2:123456789012:cluster/sample-fargate-cluster",
  "taskDefinition": "sample-fargate:1",
  "desiredCount": 5,
  "launchType": "FARGATE",
  "networkConfiguration": {
    "awsvpcConfiguration": {
      "subnets": [
        "subnet-09ce6e74c116a2299",
        "subnet-00bb3bd7a73526788",
        "subnet-0048a611aaec65477"
      ],
      "securityGroups": [
        "sg-09d45005497daa123"
      ],
      "assignPublicIp": "ENABLED"
    }
  },
  "deploymentController": {
    "type": "ECS"
  },
  "deploymentConfiguration": {
    "strategy": "CANARY",
    "maximumPercent": 200,
    "minimumHealthyPercent": 100,
    "canaryConfiguration" : {
        "canaryPercent" : 5.0,
        "canaryBakeTime" : 10
    },
    "bakeTimeInMinutes": 10,
    "alarms": {
      "alarmNames": [
        "myAlarm"
      ],
      "rollback": true,
      "enable": true
    }
  },
  "loadBalancers": [
    {
      "targetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/blue-target-group/54402ff563af1197",
      "containerName": "fargate-app",
      "containerPort": 80,
      "advancedConfiguration": {
        "alternateTargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/green-target-group/cad10a56f5843199",
        "productionListenerRule": "arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-canary-demo/32e0e4f946c3c05b/9cfa8c482e204f7d/831dbaf72edb911",
        "roleArn": "arn:aws:iam::123456789012:role/LoadBalancerManagementforECS"
      }
    }
  ]
}
```

2. Run `create-service`.

```
aws ecs create-service --cli-input-json file://canary-service-definition.json
```

## Next steps

After configuring your canary deployment, complete these steps:

- Update the service to start the deployment. For more information, see [Updating an Amazon ECS service](update-service-console-v2.md "update-service-console-v2.md").
- Monitor the deployment process to ensure it follows the canary pattern:
  - The green service revision is created and scaled up
  - A small percentage of traffic (canary) is shifted to the green revision
  - The system waits for the specified canary interval
  - The remaining traffic is shifted all at once to the green revision
  - After the bake time, the blue revision is terminated
