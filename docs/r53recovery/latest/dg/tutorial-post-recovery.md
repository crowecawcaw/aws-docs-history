

# Tutorial: Execute an RDS post-recovery workflow
<a name="tutorial-post-recovery"></a>

This tutorial guides you through executing a post-recovery workflow after a successful RDS failover. This post-recovery execution restores redundancy by re-establishing cross-Region replication for the RDS database, ensuring your RDS database is prepared for future regional events.

In this tutorial, you'll complete the following steps:
+ Verify prerequisites for post-recovery execution
+ Create a post-recovery workflow with RDS Create Cross-Region Replica execution block
+ Execute the post-recovery workflow

## Prerequisites
<a name="tutorial-post-recovery-prerequisites"></a>

Before you begin this tutorial, verify that you have the following:
+ A Region switch active/passive plan with an activate workflow that includes an RDS Promote Read Replica execution block
+ A successful activate execution that promoted a read replica in the other Region
+ Both Regions are healthy and accessible
+ The execution ID from the most recent recovery execution

## Step 1: Create a post-recovery workflow
<a name="tutorial-post-recovery-create-workflow"></a>

1. From the Region switch console choose the plan, choose **Edit workflows**, select **Config**, check **Include post recovery workflow in the plan** and save.

1. In the Edit workflows page, Select the **Select a workflow to add steps** drop down and choose **Post-recovery**.

1. Choose **Add a step**.

1. Select the **Amazon RDS create cross Region replica execution block**.

1. In the right panel, configure the block:
   + **Step name**: Enter "Create cross-Region read replica"
   + **Step description** (optional)
   + **RDS DB instance ARN for primary Region**: The ARN of the database in primary Region, should be the same as the promote read replica step
   + **RDS DB instance ARN for secondary Region**: The ARN of the promoted database in secondary, should be the same as the promote read replica step
   + **Timeout** (optional): Enter a timeout value, such as 90 minutes

   For information about the required IAM permissions for this execution block, see [Amazon RDS execution block sample policy](security_iam_region_switch_rds.md).

1. Choose **Save step**.

1. Choose **Save workflow**.

## Step 2: Execute the post-recovery workflow
<a name="tutorial-post-recovery-execute"></a>

1. On the Region switch plan details page, in the top right, choose **Execute post-recovery**.

1. Enter the execution details:
   + **Recovery execution ID**: Enter the execution ID of the most recent recovery execution. This field is used to identify the Region that is active currently.
   + **Region to execute in**: Select the inactive Region which is not receiving any application traffic. This is the Region where a read replica will be created.

1. Review the execution steps and acknowledge the execution.

1. Choose **Start Execution**.

1. Monitor the execution progress on the execution details page. The RDS Create Cross-Region Replica execution block will rename your old primary instance and create a new read replica in the previously impaired Region.

After the post-recovery execution completes successfully, your application will have cross-Region replication re-established, and you'll be prepared for future regional events. You can verify if the new read replica was created by checking the RDS console in the target Region. The old primary will be renamed and tagged with *renamedByRegionSwitch*.

**Important**  
Region switch validates that the recovery execution ID matches the last known execution for the plan. If the execution ID is invalid or is not ID of the last known recovery execution, the post-recovery execution will not run.