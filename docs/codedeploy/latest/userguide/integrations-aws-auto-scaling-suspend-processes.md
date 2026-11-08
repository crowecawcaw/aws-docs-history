

# Suspending Amazon EC2 Auto Scaling processes during deployments
<a name="integrations-aws-auto-scaling-suspend-processes"></a>

Amazon EC2 Auto Scaling can remove or replace instances during an in-place deployment, including instances that CodeDeploy is updating. For example, a scale-in event can terminate an instance in the middle of its update, or rebalancing can move instances between Availability Zones. To prevent this, you can choose Amazon EC2 Auto Scaling processes for CodeDeploy to suspend while the deployment runs. CodeDeploy suspends these processes before it deploys to instances in your Auto Scaling groups. It resumes them when the deployment succeeds, fails, or is stopped.

**Topics**
+ [When you can suspend processes](#integrations-aws-auto-scaling-suspend-processes-conditions)
+ [Processes you can suspend](#integrations-aws-auto-scaling-suspend-processes-list)
+ [Required permissions for suspending Auto Scaling processes](#integrations-aws-auto-scaling-suspend-processes-permissions)
+ [Considerations for suspending Auto Scaling processes](#integrations-aws-auto-scaling-suspend-processes-considerations)
+ [Suspending processes for a deployment group (console)](#integrations-aws-auto-scaling-suspend-processes-console)
+ [Overriding the setting for a single deployment (console)](#integrations-aws-auto-scaling-suspend-processes-override)
+ [Suspending processes (AWS CLI)](#integrations-aws-auto-scaling-suspend-processes-cli)
+ [Resuming processes manually (AWS CLI)](#integrations-aws-auto-scaling-suspend-processes-resume)

## When you can suspend processes
<a name="integrations-aws-auto-scaling-suspend-processes-conditions"></a>

You can suspend processes for deployments that meet all of the following conditions:
+ The deployment group uses the in-place deployment type.
+ The deployment group includes at least one Auto Scaling group. The group can also include instances that you identify by tags, or on-premises instances.

CodeDeploy doesn't suspend processes for blue/green deployments. If you choose processes for a deployment group that doesn't meet these conditions, CodeDeploy rejects the request.

CodeDeploy suspends processes only on the Auto Scaling groups in the deployment group. It doesn't affect instances that you add to the deployment group by tags, or on-premises instances.

## Processes you can suspend
<a name="integrations-aws-auto-scaling-suspend-processes-list"></a>

You can suspend the following processes, in any combination:

`Terminate`  
Prevents scale-in events that remove instances while CodeDeploy updates them.

`AZRebalance`  
Prevents rebalancing, which launches and terminates instances to move them between Availability Zones.

`InstanceRefresh`  
Prevents instance refreshes, which replace instances.

`ScheduledActions`  
Prevents scheduled scaling actions from running. Amazon EC2 Auto Scaling skips scheduled actions that start during the deployment and doesn't run them later.

CodeDeploy allows only these processes because leaving them suspended has a limited impact, which is mostly extra cost. Other processes, such as `Launch`, `HealthCheck`, and `ReplaceUnhealthy`, keep the Auto Scaling group healthy and able to add capacity, so CodeDeploy doesn't suspend them.

If an Auto Scaling group already has a process suspended when the deployment starts, CodeDeploy doesn't resume that process after the deployment.

For more information about how suspending a process affects your Auto Scaling group, see [Understand how suspending processes affects other processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/understand-how-suspending-processes-affects-other-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.

## Required permissions for suspending Auto Scaling processes
<a name="integrations-aws-auto-scaling-suspend-processes-permissions"></a>

The service role for the deployment group must allow the following actions on the Auto Scaling groups in the deployment group:
+ `autoscaling:DescribeAutoScalingGroups`
+ `autoscaling:SuspendProcesses`
+ `autoscaling:ResumeProcesses`

If the service role uses the `AWSCodeDeployRole` managed policy, it already has these permissions. If you use a custom service role, add these actions to it. For instructions on creating a service role, see [Step 2: Create a service role for CodeDeploy](getting-started-create-service-role.md).

If the service role is missing these permissions, CodeDeploy doesn't create the deployment, and the error names the missing IAM actions.

## Considerations for suspending Auto Scaling processes
<a name="integrations-aws-auto-scaling-suspend-processes-considerations"></a>

**Important**  
If CodeDeploy can't resume the processes, the deployment fails and the processes stay suspended. The error message lists the Auto Scaling groups and processes that are still suspended. For instructions on resuming the processes, see [Resuming processes manually (AWS CLI)](#integrations-aws-auto-scaling-suspend-processes-resume).

Keep the following in mind when you suspend processes:
+ If CodeDeploy can't suspend the processes, the deployment fails before any instance is updated.
+ While `Terminate` is suspended, Amazon EC2 Auto Scaling doesn't replace unhealthy instances. If you suspend `Terminate`, set up a notification for failed deployments, such as a trigger or an Amazon EventBridge rule. For instructions on creating a trigger, see [Create a trigger for a CodeDeploy event](monitoring-sns-event-notifications-create-trigger.md).
+ Suspending `Terminate` doesn't prevent Spot Instance interruptions or terminations that you start yourself.
+ If you suspend `Terminate` but not `AZRebalance`, the Auto Scaling group can temporarily grow above its maximum size, by up to 10 percent, while it rebalances.
+ A rollback deployment suspends the same processes as the deployment that it rolls back.
+ If two deployment groups share an Auto Scaling group, a deployment in one group can resume processes while a deployment in the other group is still running. To avoid this, associate each Auto Scaling group with only one deployment group.

## Suspending processes for a deployment group (console)
<a name="integrations-aws-auto-scaling-suspend-processes-console"></a>

You can choose the processes when you create or edit a deployment group. Every deployment to the group uses this setting unless the deployment overrides it.

**To suspend processes for a deployment group (console)**

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy).
**Note**  
Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md).

1. In the navigation pane, expand **Deploy**, then choose **Applications**.

1. Choose the application.

1. Do one of the following:
   + To create a deployment group, choose **Create deployment group**. Complete the settings up to **Environment configuration**, including your Auto Scaling groups. For more information, see [Create a deployment group for an in-place deployment (console)](deployment-groups-create-in-place.md).
   + To change an existing deployment group, choose it, and then choose **Edit**.

1. In **Environment configuration**, expand **Auto Scaling process suspension**.

1. For **Processes to suspend**, select the processes that you want CodeDeploy to suspend during each deployment.

1. Choose **Create deployment group** or **Save changes**.

The deployment group details page shows the processes under **Processes to suspend**, in the Auto Scaling groups section.

## Overriding the setting for a single deployment (console)
<a name="integrations-aws-auto-scaling-suspend-processes-override"></a>

A deployment can suspend a different set of processes than its deployment group, or none.

**To override the setting for a single deployment (console)**

1. Sign in to the AWS Management Console and open the CodeDeploy console at [https://console.aws.amazon.com/codedeploy](https://console.aws.amazon.com/codedeploy).
**Note**  
Sign in with the same user that you set up in [Getting started with CodeDeploy](getting-started-codedeploy.md).

1. In the navigation pane, expand **Deploy**, then choose **Applications**.

1. Choose the application, and then choose **Create deployment**.

1. For **Deployment group**, choose an in-place deployment group that includes Auto Scaling groups.

1. Expand **Deployment group overrides**, and then for **Auto Scaling process suspension**, choose **Override for this deployment**.

1. Under **Processes to suspend**, select the processes to suspend for this deployment. To suspend no processes for this deployment, clear all of them.

1. Complete the rest of the deployment settings, and then choose **Create deployment**.

The deployment details page shows the processes under **Suspended Auto Scaling processes**.

## Suspending processes (AWS CLI)
<a name="integrations-aws-auto-scaling-suspend-processes-cli"></a>

Use the `ec2DeploymentOptions` parameter. For more information, see [EC2DeploymentOptions](https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_EC2DeploymentOptions.html) in the *AWS CodeDeploy API Reference*. Process names are case sensitive.

The examples are formatted for Linux, macOS, or Unix.

To set the processes on a deployment group, use the [create-deployment-group](https://docs.aws.amazon.com/cli/latest/reference/deploy/create-deployment-group.html) or [update-deployment-group](https://docs.aws.amazon.com/cli/latest/reference/deploy/update-deployment-group.html) command with the `--ec2-deployment-options` option. In the following examples, replace {{my-application}} and {{my-deployment-group}} with your application and deployment group names. The following AWS CLI command suspends `Terminate` and `AZRebalance` for every deployment in the deployment group:

```
aws deploy update-deployment-group \
    --application-name {{my-application}} \
    --current-deployment-group-name {{my-deployment-group}} \
    --ec2-deployment-options '{"autoScalingGroupProcessesToSuspend":["Terminate","AZRebalance"]}'
```

The following AWS CLI command stops suspending processes for the deployment group:

```
aws deploy update-deployment-group \
    --application-name {{my-application}} \
    --current-deployment-group-name {{my-deployment-group}} \
    --ec2-deployment-options '{"autoScalingGroupProcessesToSuspend":[]}'
```

To override the setting for a single deployment, use the [create-deployment](https://docs.aws.amazon.com/cli/latest/reference/deploy/create-deployment.html) command with the `--ec2-deployment-options` option. If you don't specify the option, the deployment uses the deployment group setting. If you specify an empty list, the deployment doesn't suspend any processes. The following AWS CLI command suspends only `Terminate` for this deployment:

```
aws deploy create-deployment \
    --application-name {{my-application}} \
    --deployment-group-name {{my-deployment-group}} \
    --s3-location bucket={{amzn-s3-demo-bucket}},key={{my-app.zip}},bundleType=zip \
    --ec2-deployment-options '{"autoScalingGroupProcessesToSuspend":["Terminate"]}'
```

## Resuming processes manually (AWS CLI)
<a name="integrations-aws-auto-scaling-suspend-processes-resume"></a>

Use the following AWS CLI command to list the suspended processes on an Auto Scaling group:

```
aws autoscaling describe-auto-scaling-groups \
    --auto-scaling-group-names {{my-asg}} \
    --query 'AutoScalingGroups[0].SuspendedProcesses'
```

If successful, the command returns output similar to the following:

```
[
    {
        "ProcessName": "Terminate",
        "SuspensionReason": "User suspended at 2026-10-27T10:15:42Z"
    },
    {
        "ProcessName": "AZRebalance",
        "SuspensionReason": "User suspended at 2026-10-27T10:15:42Z"
    }
]
```

Use the following AWS CLI command to resume the processes:

```
aws autoscaling resume-processes \
    --auto-scaling-group-name {{my-asg}} \
    --scaling-processes Terminate AZRebalance
```

You can also resume processes in the Amazon EC2 console. For more information, see [Resume processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/resume-processes.html) in the *Amazon EC2 Auto Scaling User Guide*.