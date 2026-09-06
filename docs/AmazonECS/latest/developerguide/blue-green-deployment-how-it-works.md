

# Amazon ECS blue/green service deployments workflow
<a name="blue-green-deployment-how-it-works"></a>

The Amazon ECS blue/green deployment process follows a structured approach with six distinct phases that ensure safe and reliable application updates. Each phase serves a specific purpose in validating and transitioning your application from the current version (blue) to the new version (green).

1. **Preparation Phase**: Create the green environment alongside the existing blue environment. This includes provisioning new service revisions, and preparing target groups.

1. **Deployment Phase**: Deploy the new service revision to the green environment. Amazon ECS launches new tasks using the updated service revision while the blue environment continues serving production traffic.

1. **Testing Phase**: Validate the green environment using test traffic routing. The Application Load Balancer directs test requests to the green environment while production traffic remains on blue.

1. **Traffic Shifting Phase**: Shift production traffic from blue to green based on your configured deployment strategy. This phase includes monitoring and validation checkpoints.

1. **Monitoring Phase**: Monitor application health, performance metrics, and alarm states during the bake time period. A rollback operation is initiated when issues are detected.

1. **Completion Phase**: Finalize the deployment by terminating the blue environment or maintaining it for potential rollback scenarios, depending on your configuration.

## Workflow
<a name="blue-green-deployment-workflow"></a>

The following diagram illustrates the comprehensive blue/green deployment workflow, showing the interaction between Amazon ECS, and the Application Load Balancer:

![Comprehensive diagram showing the blue/green deployment process in Amazon ECS with detailed component interactions, traffic shifting phases, and monitoring checkpoints](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/images/blue-green.png)


The enhanced deployment workflow includes the following detailed steps:

1. **Initial State**: The blue service (current production) handles 100% of production traffic. The Application Load Balancer has a single listener with rules that route all requests to the blue target group containing healthy blue tasks.

1. **Green Environment Provisioning**: Amazon ECS creates new tasks using the updated task definition. These tasks are registered with a new green target group but receive no traffic initially.

1. **Health Check Validation**: The Application Load Balancer performs health checks on green tasks. Only when green tasks pass health checks does the deployment proceed to the next phase.

1. **Test Traffic Routing**: If configured, the Application Load Balancer's listener rules route specific traffic patterns (such as requests with test headers) to the green environment for validation while production traffic remains on blue. This is controlled by the same listener that handles production traffic, using different rules based on request attributes.

1. **Production Traffic Shift**: Based on the deployment configuration, traffic shifts from blue to green. In ECS blue/green deployments, this is an immediate (all-at-once) shift where 100% of the traffic is moved from the blue to the green environment. The Application Load Balancer uses a single listener with listener rules that control traffic distribution between the blue and green target groups based on weights.

1. **Monitoring and Validation**: Throughout the traffic shift, Amazon ECS monitors CloudWatch metrics, alarm states, and deployment health. Automatic rollback triggers activate if issues are detected.

1. **Bake Time Period**: The duration when both blue and green service revisions are running simultaneously after the production traffic has shifted.

1. **Blue Environment Termination**: After successful traffic shift and validation, the blue environment is terminated to free up cluster resources, or maintained for rapid rollback capability.

1. **Final State**: The green environment becomes the new production environment, handling 100% of traffic. The deployment is marked as successful.

## Deployment lifecycle stages
<a name="blue-green-deployment-stages"></a>

The blue/green deployment process progresses through distinct lifecycle stages (a series of events in the deployment operation, such as "after production traffic shift"), each with specific responsibilities and validation checkpoints. Understanding these stages helps you monitor deployment progress and troubleshoot issues effectively.

 Each lifecycle stage can last up to 24 hours. We recommend that the value remains below the 24-hour mark. This is because asynchronous processes need time to trigger the hooks. The system times out, fails the deployment, and then initiates a rollback after a stage reaches 24 hours. CloudFormation deployments have additional timeout restrictions. While the 24-hour stage limit remains in effect, CloudFormation enforces a 36-hour limit on the entire deployment. CloudFormation fails the deployment, and then initiates a rollback if the process doesn't complete within 36 hours.

For pause hooks, you can configure the timeout up to 20,160 minutes (14 days). The overall deployment timeout is 30 days.


| Lifecycle stages | Description | Use this stage for lifecycle hook? | 
| --- | --- | --- | 
| RECONCILE\_SERVICE | This stage only happens when you start a new service deployment with more than 1 service revision in an ACTIVE state. | Yes | 
| PRE\_SCALE\_UP | The green service revision has not started. The blue service revision is handling 100% of the production traffic. There is no test traffic. | Yes | 
| SCALE\_UP | The time when the green service revision scales up to 100% and launches new tasks. The green service revision is not serving any traffic at this point. | No | 
| POST\_SCALE\_UP | The green service revision has started. The blue service revision is handling 100% of the production traffic. There is no test traffic. | Yes | 
| TEST\_TRAFFIC\_SHIFT | The blue and green service revisions are running. The blue service revision handles 100% of the production traffic. The green service revision is migrating from 0% to 100% of test traffic. | Yes (Lambda only) | 
| POST\_TEST\_TRAFFIC\_SHIFT | The test traffic shift is complete. The green service revision handles 100% of the test traffic. | Yes | 
| PRE\_PRODUCTION\_TRAFFIC\_SHIFT | Occurs before the production traffic shift. For blue/green deployments, this stage is invoked once. | Yes | 
| PRODUCTION\_TRAFFIC\_SHIFT | Production traffic is shifting to the green service revision. The green service revision is migrating from 0% to 100% of production traffic. | Yes (Lambda only) | 
| POST\_PRODUCTION\_TRAFFIC\_SHIFT | The production traffic shift is complete. | Yes | 
| BAKE\_TIME | The duration when both blue and green service revisions are running simultaneously. | No | 
| CLEAN\_UP | The blue service revision has completely scaled down to 0 running tasks. The green service revision is now the production service revision after this stage. | No | 

Each lifecycle stage includes built-in validation checkpoints that must pass before proceeding to the next stage. If any validation fails, the deployment can be automatically rolled back to maintain service availability and reliability.

When you use a Lambda function, the function must complete the work, or return IN\_PROGRESS within 15 minutes. You can use the `callBackDelaySeconds` to delay the call to Lambda. For more information, see [app.py function](https://github.com/aws-samples/sample-amazon-ecs-blue-green-deployment-patterns/blob/main/ecs-bluegreen-lifecycle-hooks/src/approvalFunction/app.py#L20-L25) in the sample-amazon-ecs-blue-green-deployment-patterns on GitHub.