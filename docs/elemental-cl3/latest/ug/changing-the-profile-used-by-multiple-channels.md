

# Changing the profile used by multiple channels
<a name="changing-the-profile-used-by-multiple-channels"></a>

You can use the **Tasks** feature to change the profile so that several channels can use it. You can also change associations between channels and profiles so that each channel uses a different profile.

You can modify a channel even if it is running.

## Step 1. Create the task
<a name="step-a-create-the-task"></a>

**To create a task**

1. On the **Channels** page, select **Tasks** in the top left corner, and choose **Change Channel Profiles**. 

   The **Change Channel Profiles** page shows all the channels on all the nodes in the cluster.

1. Select the channels that you want to associate with one specific profile. 

   You can select by choosing individual channels.

   You can select by filtering. For example, you can filter by profile or by node. After you have filtered, choose the **Select All** button.

1. Choose **Next**.

1. Select the new profile to associate with all the selected channels. Choose **Next**.

1. If the new profile includes channel parameters, complete those parameters. When you are ready, choose **Next**.

   **Examples of changes in channel parameters**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-cl3/latest/ug/changing-the-profile-used-by-multiple-channels.html)

   You might get any combination of these types of discrepancies, and you are prompted to handle all of them.

1. On the final page, choose **Process Now** or **Save for Later**.

   **Process Now**: Conductor Live applies the change. The **Channels** page reappears, showing the change.

   **Save for Later**: This option lets you queue up several tasks and then perform them in one pass.
**Warning**  
**Save for Later **is intended to queue for a short time.  
Don't use **Save for Later** and then delay process the task in a few hours. Doing so might create undesired consequences.

   **Example of Save for Later**

   Assume that you want to move all existing channels from node A so that you can move another set of channels to node A. This is an opportunity to use bulk changes. Set up bulk changes as follows: do Bulk Change \#1 to move the channels from node A to node B (change the associated node for the channels). Then do Bulk Change \#2 to move the channels from node C to node A. 

   In order to do this two-part move with the least downtime, you could do the following:
   + Set up Bulk Change \#1 and choose **Save for Later**. 
   + Set up Bulk Change \#2 and choose **Save for Later**.

     Both bulk changes appear on the left side of the page, as shown below.
   + Then choose **Run Pending Actions**. Bulk Change \#1 runs. As soon as it has finished, Bulk Change \#2 runs.

## Step B. Monitor the status of the task
<a name="step-b-monitor-the-status-of-the-task"></a>

When you run **Process Now** to run the task, you can monitor the status of each modify action in the task.

1. On the Conductor Live main menu, choose **Status**, then choose **Task Reports**. The **Task Reports** page appears. 

1. In the **Task Reports** panel on the left, choose the task to monitor (newer tasks appear first).

   (This list shows running and completed tasks; for pending tasks, go to the **Channels** page and choose the **Pending Tasks** icon).

1. Find the relevant task and review the information:
   + The top line shows the count of total tasks, failed tasks, and successful tasks.
   + Below that, a line appears for each individual action. Each line shows the current status of the action: **Pending**, **Success**, or an explanation of why the task failed.

     As the status of an action changes, the page automatically refreshes to display the latest information.