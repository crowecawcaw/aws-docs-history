

# Tutorial: Create an active/passive Region switch plan
<a name="tutorial-region-switch"></a>

This tutorial guides you through creating an active/passive Region switch plan for an application running in us-east-1 and recovering into us-west-2. The example includes Amazon EC2 instances for compute, Amazon Aurora Global Database for storage, and Amazon Route 53 for DNS.

In this tutorial, you'll complete the following steps:
+ Create a Region switch plan
+ Build the plan's workflows and execution blocks
+ Build an EC2 Auto Scaling group execution block
+ Build two manual approval execution blocks
+ Build two custom action Lambda execution blocks
+ Build an Amazon Aurora Global Database execution block
+ Build an ARC routing control block
+ Execute the Region switch plan

## Prerequisites
<a name="tutorial-rs-prerequisites"></a>

Before you begin this tutorial, verify that you have the following prerequisites in both Regions:
+ IAM roles with appropriate permissions
+ EC2 Auto Scaling groups
+ Lambda functions for maintenance page and fencing
+ Aurora Global Database
+ ARC routing controls

## Step 1: Create the Region switch plan
<a name="tutorial-rs-create-plan"></a>

1. From the Region switch console, choose **Create Region switch plan**.

1. Provide the following details:
   + **Primary Region**: Choose us-east-1
   + **Standby Region**: Choose us-west-2
   + **Desired recovery time objective (RTO)** (optional)
   + **IAM role**: Enter the plan execution IAM role. This IAM role allows Region switch to call AWS services during execution.

1. Choose **Create**.

(Optional) Add resources from different AWS accounts to your Region switch plan:

1. Create the cross-account role:
   + In the account hosting the resource, create an IAM role.
   + Add permissions for the specific resources that the plan will access.
   + Add a trust policy that allows the execution role to assume the new role.
   + Enter and take note of an external ID that you will use as a shared secret.

1. Configure the resource in your plan:
   + When you add the resource to your plan, specify two additional fields:
     + **crossAccountRole**: The ARN of the role that you created in step 1
     + **externalId**: The external ID that you entered in step 1

Example configuration for an EC2 Auto Scaling execution block accessing resources in account 987654321:

```
{
  "executionBlock": "EC2AutoScaling",
  "name": "ASG",
  "crossAccountRole": "arn:aws:iam::987654321:role/RegionSwitchCrossAccountRole",
  "externalId": "unique-external-id-123",
  "autoScalingGroupArn": "arn:aws:autoscaling:us-west-2:987654321:autoScalingGroup:*:autoScalingGroupName/CrossAccountASG"
}
```

Required permissions:
+ The execution role must have sts:AssumeRole permission for the cross-account role.
+ The cross-account role must have permissions only for the specific resources being accessed.
+ The cross-account role's trust policy must include:
  + The execution role's account as a trusted entity.
  + The external ID condition.
+ For more information on configuring a cross-account role, see [Cross-account resource permissions](security_iam_region_switch_cross_account.md).

Before executing the plan, Region switch will verify the following:
+ The execution role can assume the cross-account role.
+ The cross-account role has the required permissions.
+ The external ID matches the trust policy.

## Step 2: Build the plan's workflows and execution blocks
<a name="tutorial-rs-build-workflows"></a>

1. From the Region switch plan details page, choose **Build workflows**.

1. Select **Build the same activation workflow for all Regions**.

1. Enter a Region activation workflow description (optional). This will be used to easily identify the workflow when executing the plan.

1. Choose **Save and continue**.

### Add EC2 Auto Scaling execution block
<a name="tutorial-rs-build-workflows-ec2"></a>

For more information about this execution block, see [Amazon EC2 Auto Scaling group execution block](ec2-auto-scaling-block.md).

1. Choose **Add a step**, and then select **Run in sequence**.

1. Select the **EC2 Auto Scaling execution block**, and then choose **Add and edit**. This block will allow you to start increasing capacity in the passive Region.

1. In the right panel, configure the block:
   + **Step name**: Enter "Scale"
   + **Step description** (optional)
   + **Auto Scaling group ARN for us-east-1**: The ARN of your ASG in us-east-1
   + **Auto Scaling group ARN for us-west-2**: The ARN of your ASG in us-west-2
   + **Percent to match the source Region's capacity**: Enter 100
   + **Capacity monitoring approach**: Leave as "Most recent"
   + **Timeout** (optional)

   For information about the required IAM permissions for this execution block, see [EC2 Auto Scaling execution block sample policy](security_iam_region_switch_ec2_autoscaling.md).

1. Choose **Save step**.

### Add manual approval execution block
<a name="tutorial-rs-build-workflows-manual-approval-1"></a>

For more information about this execution block, see [Manual approval execution block](manual-approval-block.md).

1. Choose **Add a step**.

1. Select the **Manual approval execution block** and add it to the design window. This block allows for human verification before proceeding.

1. In the right panel, configure the block:
   + **Step name**: Enter "Manual approval before setup"
   + **Step description** (optional)
   + **IAM approval role**: The role a user must assume in order to approve the execution
   + **Timeout** (optional). After timeout, execution pauses and you can choose to retry, skip, or cancel.

   For information about the required IAM permissions for this execution block, see [Manual approval execution block sample policy](security_iam_region_switch_manual_approval.md).

1. Choose **Save step**.

### Add custom action Lambda execution block for maintenance page
<a name="tutorial-rs-build-workflows-lambda-maintenance"></a>

For more information about this execution block, see [Custom action Lambda execution block](custom-action-lambda-block.md).

1. Choose **Add a step**.

1. Select the **Custom action Lambda execution block**, and then choose **Add and edit**. This block publishes a maintenance page in the Region that is activating.

1. In the right panel, configure the block:
   + **Step name**: Enter "Display maintenance page"
   + **Step description** (optional)
   + **Lambda ARN for activating us-east-1**: The ARN of the maintenance page Lambda function deployed in us-east-1
   + **Lambda ARN for activating us-west-2**: The ARN of the maintenance page Lambda function deployed in us-west-2
   + **Region to run the Lambda function**: Choose **Run in activating Region**
   + **Timeout** (optional)
   + **Retry interval** (optional)

   For information about the required IAM permissions for this execution block, see [Custom action Lambda execution block sample policy](security_iam_region_switch_lambda.md).

1. Choose **Save step**.

### Add Aurora Global Database execution block
<a name="tutorial-rs-build-workflows-aurora"></a>

For more information about this execution block, see [Amazon Aurora Global Database execution block](aurora-global-database-block.md).

1. Choose **Add a step**.

1. Select the **Aurora Global Database execution block**, and then choose **Add and edit**. This block triggers an Aurora global database switchover (no data loss). For more information, see [Using switchover or failover for Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html) in the *Aurora User Guide*.

1. In the right panel, configure the block:
   + **Step name**: Enter **Aurora switchover**
   + **Step description** (optional)
   + **Aurora global database identifier**: The name of the Aurora cluster
   + **Cluster ARN used for activating us-east-1**: The Aurora cluster ARN in us-east-1
   + **Cluster ARN used for activating us-west-2**: The Aurora cluster ARN in us-west-2
   + **Select the option for Aurora database**: Choose **Switchover**
   + **Timeout** (optional)

   For information about the required IAM permissions for this execution block, see [Aurora Global Database execution block sample policy](security_iam_region_switch_aurora.md).

1. Choose **Save step**.

### Add ARC routing control execution block
<a name="tutorial-rs-build-workflows-routing-control"></a>

For more information about this execution block, see [ARC routing control execution block](arc-routing-controls-block.md).

1. Choose **Add a step**.

1. Select **ARC routing control execution block**, and then choose **Add and edit**. This block performs a DNS failover to shift traffic to the passive Region.

1. In the right panel, configure the block:
   + **Step name**: Enter **Toggle DNS**
   + **Step description** (optional)
   + **Routing controls used in activating us-east-1**: Choose **Add routing controls**
   + **Timeout**: Enter a timeout value.

1. Choose **Add routing control**:
   + **Routing control ARN**: The ARN of the routing control that controls us-east-1
   + **Routing control state**: Choose **On**

1. Choose **Add routing control** again:
   + **Routing control ARN**: The ARN of the routing control that controls us-west-2
   + **Routing control state**: Choose **Off**

1. Choose **Save**.

1. **Routing controls used in activating us-west-2**: Choose **Add routing controls**

1. Choose **Add routing control**:
   + **Routing control ARN**: The ARN of the routing control that controls us-west-2
   + **Routing control state**: Choose **On**

1. Choose **Add routing control** again:
   + **Routing control ARN**: The ARN of the routing control that controls us-east-1
   + **Routing control state**: Choose **Off**

1. Choose **Save**.

1. Choose **Save step**.

   For information about the required IAM permissions for this execution block, see [ARC routing controls execution block sample policy](security_iam_region_switch_arc_routing.md).

1. Choose **Save**.

## Step 3: Execute the plan
<a name="tutorial-rs-execute-plan"></a>

1. On the Region switch plan details page, in the top right, choose **Execute**.

1. Enter the execution details:
   + Select the Region to activate.
   + Select the plan execution mode.
   + (Optional) View the execution steps.
   + Acknowledge the plan execution.

1. Choose **Start**.

1. You can view detailed steps as the plan executes on the execution details page. You can see each step in the plan execution, including start time, end time, resource ARN, and log messages.

When the impaired Region has recovered, you can execute the plan again (changing the parameters that you provide) to activate the original Region, to switch back your application operations to the original primary Region.