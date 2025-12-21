# Troubleshoot Amazon ECS deployment

issues

###### Topics

- [A timeout occurs while waiting for replacement
  task set](#troubleshooting-ecs-timeout "#troubleshooting-ecs-timeout")
- [A timeout occurs while waiting for a
  notification to continue](#troubleshooting-ecs-timeout-notif "#troubleshooting-ecs-timeout-notif")
- [The IAM role does not have enough
  permissions](#troubleshooting-ecs-iam "#troubleshooting-ecs-iam")
- [The deployment timed out while waiting
  for a status callback](#troubleshooting-ecs-timeout-callback "#troubleshooting-ecs-timeout-callback")
- [The deployment failed because one or more of
  the lifecycle event validation functions failed](#troubleshooting-ecs-lifecycle "#troubleshooting-ecs-lifecycle")
- [The ELB could not be updated due to the following
  error: Primary taskset target group must be behind listener](#troubleshooting-ecs-elb "#troubleshooting-ecs-elb")
- [My deployment sometimes fails when using
  Auto Scaling](#troubleshooting-ecs-auto-scaling "#troubleshooting-ecs-auto-scaling")
- [Only ALB supports gradual traffic routing, use
  AllAtOnce Traffic routing instead when you create/update Deployment group](#troubleshooting-ecs-lb "#troubleshooting-ecs-lb")
- [Even though my deployment succeeded,
  the replacement task set fails the ELB health checks, and my application is down](#troubleshooting-ecs-task-set-stability "#troubleshooting-ecs-task-set-stability")
- [Can I attach multiple load balancers to a
  deployment group?](#troubleshooting-ecs-lb-multi "#troubleshooting-ecs-lb-multi")
- [Can I perform CodeDeploy blue/green deployments without
  a load balancer?](#troubleshooting-ecs-lb-bg "#troubleshooting-ecs-lb-bg")
- [How can I update my Amazon ECS service with new
  information during a deployment?](#troubleshooting-ecs-exec "#troubleshooting-ecs-exec")

## A timeout occurs while waiting for replacement

task set

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The deployment timed out while waiting for the replacement task set to become
 healthy. This time out period is 60 minutes.`

**Possible cause**: This error might occur if there is a
mistake in your task definition file or other deployment-related files. For example, if there
is a typo in the `image` field in your task definition file, Amazon ECS will try to pull
the wrong container image and continuously fail, causing this error.

**Possible fixes and next steps**:

- Fix typographical errors and configuration problems in your task definition file and
  other files.
- Check the related Amazon ECS service event and find out why replacement tasks are not
  becoming healthy. For more information on Amazon ECS events, see [Amazon ECS events](../../../AmazonECS/latest/developerguide/ecs_cwe_events.md "../../../AmazonECS/latest/developerguide/ecs_cwe_events.md") in the
  _Amazon Elastic Container Service Developer Guide_.
- Check the [Amazon ECS troubleshooting](../../../AmazonECS/latest/developerguide/troubleshooting.md "../../../AmazonECS/latest/developerguide/troubleshooting.md")
  section in the _Amazon Elastic Container Service Developer Guide_ for errors related to the messages in
  the event.

## A timeout occurs while waiting for a

notification to continue

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The deployment timed out while waiting for a notification to continue. This time out
 period is `n` minutes.`

**Possible cause**: This error might occur if you specified a
wait time in the **Specify when to reroute traffic** field when you created
your deployment group, but the deployment couldn't finish before the wait time expired.

**Possible fixes and next steps**:

- In your deployment group, set the **Specify when to reroute traffic**
  to a larger amount of time and redeploy. For more information, see [Create a deployment group for an
  Amazon ECS deployment (console)](deployment-groups-create-ecs.md "deployment-groups-create-ecs.md").
- In your deployment group, change **Specify when to reroute traffic**
  to **Reroute traffic immediately** and redeploy. For more information,
  see [Create a deployment group for an
  Amazon ECS deployment (console)](deployment-groups-create-ecs.md "deployment-groups-create-ecs.md").
- Redeploy and then run the [`aws deploy
continue-deployment`](../../../cli/latest/reference/deploy/continue-deployment.md "../../../cli/latest/reference/deploy/continue-deployment.md") AWS CLI command with the
  `--deployment-wait-type` option set to `READY_WAIT`. Make sure to
  run this command _before_ the time specified in **Specify when
  to reroute traffic** expires.

## The IAM role does not have enough

permissions

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The IAM role `role-arn` does not give you permission to
 perform operations in the following AWS service: AWSLambda.`

**Possible cause**: This error might occur if you specified a
Lambda function in the [AppSpec file's Hooks
section](reference-appspec-file-structure-hooks.md#appspec-hooks-ecs "reference-appspec-file-structure-hooks.md#appspec-hooks-ecs"), but you did not give CodeDeploy permission to the Lambda service.

**Possible fix**: Add the `lambda:InvokeFunction`
permission to the CodeDeploy service role. To add this permission, add one of the following
AWS-managed policies to the role: `AWSCodeDeployRoleForECS` or
`AWSCodeDeployRoleForECSLimited`. For information about these policies
and how to add them to the CodeDeploy service role, see [Step 2: Create a service role for
CodeDeploy](getting-started-create-service-role.md "getting-started-create-service-role.md").

## The deployment timed out while waiting

for a status callback

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The deployment timed out while waiting for a status callback. CodeDeploy expects a status
 callback within one hour after a deployment hook is invoked.`

**Possible cause**: This error might occur if you specified a
Lambda function in the [AppSpec file's Hooks
section](reference-appspec-file-structure-hooks.md#appspec-hooks-ecs "reference-appspec-file-structure-hooks.md#appspec-hooks-ecs"), but Lambda function could not call the necessary
`PutLifecycleEventHookExecutionStatus` API to return a `Succeeded` or
`Failed` status to CodeDeploy.

**Possible fixes and next steps**:

- Add the `codedeploy:putlifecycleEventHookExecutionStatus` permission to the
  Lambda execution role used by the Lambda function that you specified in the AppSpec file.
  This permission grants the Lambda function the ability to return a status of
  `Succeeded` or `Failed` to CodeDeploy. For more information about the
  Lambda execution role, see [Lambda execution role](../../../lambda/latest/dg/lambda-intro-execution-role.md "../../../lambda/latest/dg/lambda-intro-execution-role.md") in
  the _AWS Lambda User Guide_.
- Check your Lambda function code and execution logs to make sure your Lambda function is
  calling CodeDeploy's `PutLifecycleEventHookExecutionStatus` API to inform CodeDeploy
  about whether the lifecycle validation test `Succeeded` or `Failed`.
  For information about the `putlifecycleEventHookExecutionStatus` API, see
  [PutLifecycleEventHookExecutionStatus](../APIReference/API_PutLifecycleEventHookExecutionStatus.md "../APIReference/API_PutLifecycleEventHookExecutionStatus.md") in the _AWS CodeDeploy API
  Reference_. For information about Lambda execution logs, see [Accessing
  Amazon CloudWatch logs for AWS Lambda](../../../lambda/latest/dg/monitoring-cloudwatchlogs.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs.md").

## The deployment failed because one or more of

the lifecycle event validation functions failed

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The deployment failed because one or more of the lifecycle event validation
 functions failed.`

**Possible cause**: This error might occur if you specified a
Lambda function in the [AppSpec file's Hooks
section](reference-appspec-file-structure-hooks.md#appspec-hooks-ecs "reference-appspec-file-structure-hooks.md#appspec-hooks-ecs"), but the Lambda function returned `Failed` to CodeDeploy when it called
`PutLifecycleEventHookExecutionStatus`. This failure indicates to CodeDeploy that the
lifecycle validation test failed.

**Possible next step**: Check your Lambda execution logs to
see why the validation test code is failing. For information about Lambda execution logs, see
[Accessing
Amazon CloudWatch logs for AWS Lambda](../../../lambda/latest/dg/monitoring-cloudwatchlogs.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs.md").

## The ELB could not be updated due to the following

error: Primary taskset target group must be behind listener

**Problem**: You see the following error message while
deploying your Amazon ECS application using CodeDeploy:

`The ELB could not be updated due to the following error: Primary taskset target
 group must be behind listener`

**Possible cause**: This error might occur if you have
configured an optional test listener, and it is configured with wrong target group. For more
information about the test listener in CodeDeploy, see [Before you begin an Amazon ECS
deployment](deployment-steps-ecs.md#deployment-steps-prerequisites-ecs "deployment-steps-ecs.md#deployment-steps-prerequisites-ecs") and [What happens during an Amazon ECS
deployment](deployment-steps-ecs.md#deployment-steps-what-happens "deployment-steps-ecs.md#deployment-steps-what-happens"). For
more information about task sets, see [TaskSet](../../../AmazonECS/latest/APIReference/API_TaskSet.md "../../../AmazonECS/latest/APIReference/API_TaskSet.md") in the
_Amazon Elastic Container Service API Reference_ and [describe-task-set](../../../cli/latest/reference/ecs/describe-task-set.md "../../../cli/latest/reference/ecs/describe-task-set.md") in the Amazon ECS
section of the _AWS CLI Command Reference_.

**Possible fix**: Make sure that the ELB's production
listener and test listener are both pointing to the target group that's currently serving your
workloads. There are three places to check:

- In Amazon EC2, in your load balancer's **Listeners and rules** settings.
  For more information, see [Listeners for
  your Application Load Balancers](../../../elasticloadbalancing/latest/application/load-balancer-listeners.md "../../../elasticloadbalancing/latest/application/load-balancer-listeners.md") in the _User Guide for Application Load Balancers_, or [Listeners for
  your Network Load Balancers](../../../elasticloadbalancing/latest/network/load-balancer-listeners.md "../../../elasticloadbalancing/latest/network/load-balancer-listeners.md") in the _User Guide for Network Load Balancers_.
- In Amazon ECS, in your cluster, under your service's **Networking**
  configuration. For more information, see [Application Load Balancer
  and Network Load Balancer considerations](../../../AmazonECS/latest/developerguide/load-balancer-types.md#alb-considerations "../../../AmazonECS/latest/developerguide/load-balancer-types.md#alb-considerations") in the _Amazon Elastic Container Service Developer Guide_.
- In CodeDeploy, in your deployment group settings. For more information, see [Create a deployment group for an
  Amazon ECS deployment (console)](deployment-groups-create-ecs.md "deployment-groups-create-ecs.md").

## My deployment sometimes fails when using

Auto Scaling

**Problem**: You are using Auto Scaling with CodeDeploy and you notice
that your deployments occasionally fail. For more information about the symptoms of this
problem, see the topic that reads [For services configured to use service auto scaling and the blue/green deployment type,
auto scaling is not blocked during a deployment but the deployment may fail under some
circumstances](../../../AmazonECS/latest/developerguide/deployment-type-bluegreen.md#deployment-type-bluegreen-considerations "../../../AmazonECS/latest/developerguide/deployment-type-bluegreen.md#deployment-type-bluegreen-considerations") in the _Amazon Elastic Container Service Developer Guide_.

**Possible cause**: This problem might occur if CodeDeploy and
Auto Scaling processes conflict.

**Possible fix**: Suspend and resume Auto Scaling processes during
the CodeDeploy deployment using the `RegisterScalableTarget` API (or the corresponding
`register-scalable-target` AWS CLI command). For more information, see [Suspend and resume scaling for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md") in the
_Application Auto Scaling User Guide_.

###### Note

CodeDeploy can't call `RegisterScaleableTarget` directly. To use this API, you
must configure CodeDeploy to send a notification or event to Amazon Simple Notification Service (or Amazon CloudWatch). You must
then configure Amazon SNS (or CloudWatch) to call a Lambda function, and configure the Lambda function to
call the `RegisterScalableTarget` API. The `RegisterScalableTarget`
API must be called with the `SuspendedState` parameter set to `true`
to suspend Auto Scaling operations, and `false` to resume them.

The notification or event that CodeDeploy sends out must occur when a deployment starts (to
trigger Auto Scaling suspend operations), or when a deployment succeeds, fails, or stops (to trigger
Auto Scaling resume operations).

For information about how to configure CodeDeploy to generate Amazon SNS notifications or CloudWatch
events, see [Monitoring deployments with Amazon CloudWatch Events](monitoring-cloudwatch-events.md "monitoring-cloudwatch-events.md"). and [Monitoring Deployments with Amazon SNS Event Notifications](monitoring-sns-event-notifications.md "monitoring-sns-event-notifications.md").

## Only ALB supports gradual traffic routing, use

AllAtOnce Traffic routing instead when you create/update Deployment group

**Problem**: You see the following error message while
creating or updating a deployment group in CodeDeploy:

`Only ALB supports gradual traffic routing, use AllAtOnce Traffic routing instead when
 you create/update Deployment group.`

**Possible cause**: This error might occur if you're using a
Network Load Balancer and tried to use a predefined deployment configuration other than
`CodeDeployDefault.ECSAllAtOnce`.

**Possible fixes**:

- Change your predefined deployment configuration to
  `CodeDeployDefault.ECSAllAtOnce`. This is the only predefined deployment
  configuration supported by Network Load Balancers.

For more information about predefined deployment configurations, see [Predefined deployment
configurations for an Amazon ECS compute platform](deployment-configurations.md#deployment-configurations-predefined-ecs "deployment-configurations.md#deployment-configurations-predefined-ecs").

- Change your load balancer to an Application Load Balancer. Application Load Balancer's support all the predefined deployment
  configurations. For more information about creating a Application Load Balancer, see [Set up a load balancer,
  target groups, and listeners for CodeDeploy Amazon ECS deployments](deployment-groups-create-load-balancer-for-ecs.md "deployment-groups-create-load-balancer-for-ecs.md").

## Even though my deployment succeeded,

the replacement task set fails the ELB health checks, and my application is down

**Problem**: Even though CodeDeploy indicates that my deployment
succeeded, the replacement task set fails the health checks from ELB, and my application is
down.

**Possible cause**: This issue might occur if you performed a
CodeDeploy all-at-once deployment, and your replacement (green) task set contains bad code that is
causing the ELB health checks to fail. With the all-at-once deployment configuration, the
load balancer’s health checks start running on the replacement task set
_after_ traffic has been shifted to it (that is,
_after_ CodeDeploy’s `AllowTraffic` lifecycle event occurs). That’s
why you will see health checks failing on the replacement task set after traffic has shifted,
but not before. For information about the lifecycle events that CodeDeploy generates, see [What happens during an Amazon ECS
deployment](deployment-steps-ecs.md#deployment-steps-what-happens "deployment-steps-ecs.md#deployment-steps-what-happens").

**Possible fixes**:

- Change your deployment configuration from all-at-once to canary or linear. In a canary
  or linear configuration, the load balancer’s health checks start running on the
  replacement task set while CodeDeploy installs your application in the replacement environment,
  and _before_ traffic is shifted (that is, during the
  `Install` lifecycle event, and _before_ the
  `AllowTraffic` event). By allowing the checks to run during the application
  installation but before traffic is shifted, bad application code will be detected and
  cause deployment failures before the application becomes publicly available.

For information about how to configure canary or linear deployments, see [Change deployment group settings with CodeDeploy](deployment-groups-edit.md "deployment-groups-edit.md").

For information about CodeDeploy lifecycle events that run during an Amazon ECS deployment, see
[What happens during an Amazon ECS
deployment](deployment-steps-ecs.md#deployment-steps-what-happens "deployment-steps-ecs.md#deployment-steps-what-happens").

###### Note

Canary and linear deployment configurations are only supported with Application Load Balancers.

- If you want to keep your all-at-once deployment configuration, set up a test listener
  and check the health status of the replacement task set with the
  `BeforeAllowTraffic` lifecycle hook. For more information, see [List of lifecycle
  event hooks for an Amazon ECS deployment](reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-list-ecs "reference-appspec-file-structure-hooks.md#reference-appspec-file-structure-hooks-list-ecs").

## Can I attach multiple load balancers to a

deployment group?

No. If you want to use multiple Application Load Balancers or Network Load Balancers, use Amazon ECS rolling updates instead of
CodeDeploy blue/green deployments. For more information about rolling updates, see [Rolling
update](../../../AmazonECS/latest/userguide/deployment-type-ecs.md "../../../AmazonECS/latest/userguide/deployment-type-ecs.md") in the _Amazon Elastic Container Service Developer Guide_. For more information about using
multiple load balancers with Amazon ECS, see [Registering
multiple target groups with a service](../../../AmazonECS/latest/developerguide/register-multiple-targetgroups.md "../../../AmazonECS/latest/developerguide/register-multiple-targetgroups.md") in the
_Amazon Elastic Container Service Developer Guide_.

## Can I perform CodeDeploy blue/green deployments without

a load balancer?

No, you cannot perform CodeDeploy blue/green deployments without a load balancer. If you are
unable to use a load balancer, use Amazon ECS's rolling updates feature instead. For more
information about Amazon ECS rolling updates, see [Rolling update](../../../AmazonECS/latest/userguide/deployment-type-ecs.md "../../../AmazonECS/latest/userguide/deployment-type-ecs.md") in the
_Amazon Elastic Container Service Developer Guide_.

## How can I update my Amazon ECS service with new

information during a deployment?

To have CodeDeploy update your Amazon ECS service with a new parameter while it conducts a
deployment, specify the parameter in the `resources` section of the AppSpec file.
Only a few Amazon ECS parameters are supported by CodeDeploy, such as the task definition file and
container name parameters. For a full list of Amazon ECS parameters that CodeDeploy can update, see
[AppSpec 'resources'
section for Amazon ECS deployments](reference-appspec-file-structure-resources.md#reference-appspec-file-structure-resources-ecs "reference-appspec-file-structure-resources.md#reference-appspec-file-structure-resources-ecs").

###### Note

If you need to update your Amazon ECS service with a parameter that is not supported by
CodeDeploy, complete these tasks:

1. Call Amazon ECS's `UpdateService` API with the parameter you want to update.
   For a full list of parameters that can be updated, see [UpdateService](../../../AmazonECS/latest/APIReference/API_UpdateService.md "../../../AmazonECS/latest/APIReference/API_UpdateService.md") in
   the _Amazon Elastic Container Service API Reference_.
2. To apply the change to the tasks, create a new Amazon ECS blue/green deployment. For more
   information, see [Create an
   Amazon ECS Compute Platform deployment (console)](deployments-create-console-ecs.md "deployments-create-console-ecs.md").
