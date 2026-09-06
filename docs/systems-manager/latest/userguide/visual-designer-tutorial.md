

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Tutorial: Create a runbook using the visual design experience
<a name="visual-designer-tutorial"></a>

In this tutorial, you learn the basics of working with the visual design experience provided by Systems Manager Automation. In the visual design experience, you can create a runbook that uses multiple actions. You use the move feature to arrange actions on the canvas. You also search for, select, and configure these actions. Then, you can view the auto-generated YAML code for your runbook's workflow, exit the visual design experience, run the runbook, and review the execution details.

This tutorial also shows you how to update the runbook and view the new version. At the end of the tutorial, you perform a clean-up step and delete your runbook.

After you complete this tutorial, you'll know how to use the visual design experience to create a runbook. You'll also know how to update, run, and delete your runbook.

**Note**  
Before you start this tutorial, make sure to complete [Setting up Automation](automation-setup.md).

**Topics**
+ [Step 1: Navigate to the visual design experience](#navigate-console)
+ [Step 2: Create a workflow](#create-workflow)
+ [Step 3: Review the auto-generated code](#view-generated-code)
+ [Step 4: Run your new runbook](#use-tutorial-runbook)
+ [Step 5: Clean up](#cleanup-tutorial-runbook)

## Step 1: Navigate to the visual design experience
<a name="navigate-console"></a>

1. Sign in to the [Systems Manager Automation console](https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/).

1. Choose **Create automation runbook**.

## Step 2: Create a workflow
<a name="create-workflow"></a>

In the visual design experience, a workflow is a graphical representation of your runbook on the canvas. You can use the visual design experience to define, configure, and examine the individual actions of your runbook.

**To create a workflow**

1. Next to the **Design** and **Code** toggle, select the pencil icon and enter a name for your runbook. For this tutorial, enter **VisualDesignExperienceTutorial**.  
![Visual design experience name your runbook](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_tutorial_name.png)

1. In the **Document attributes** section of the **Form** panel, expand the **Input parameters** dropdown, and select **Add a parameter**.

   1. In the **Parameter name** field, enter **InstanceId**.

   1. In the **Type** dropdown, choose **AWS::EC2::Instance**.

   1. Select the **Required** toggle.  
![Create a parameter for your runbook](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_actions_tutorial_parameter.png)

1. In the **AWS APIs** browser, enter **DescribeInstances** in the search bar.

1. Move an **Amazon EC2 – DescribeInstances** action to the empty canvas.

1. For **Step name**, enter a value. For this tutorial, you can use the name **GetInstanceState**.  
![Choose an Amazon EC2 describe instances API action.](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_tutorial_api_action.png)

   1. Expand the **Additional inputs** dropdown, and in the **Input name** field, enter **InstanceIds**.

   1. Choose the **Inputs** tab.

   1. In the **Input value** field, choose the **InstanceId** document input. This references the value of the input parameter that you created at the beginning of the procedure. Since the **InstanceIds** input for the `DescribeInstances` action accepts `StringList` values, you must wrap the **InstanceId** input in square brackets. The YAML for the **Input value** should match the following: **['{{ InstanceId }}']**.

   1. In the **Outputs** tab, select **Add an output** and enter **InstanceState** in the **Name** field.

   1. In the **Selector** field, enter **$.Reservations[0].Instances[0].State.Name**.

   1. In the **Type** dropdown, choose **String**.

1. Move a **Branch** action from the **Actions** browser, into the position below the **`GetInstanceState`** step. 

1. For **Step name**, enter a value. For this tutorial, use the name `BranchOnInstanceState`.

   To define the branching logic, do the following:

   1. Choose the **`Branch`** state on the canvas. Then, under **Inputs** and **Choices**, select the pencil icon to edit **Rule \#1**.

   1. Choose **Add conditions**.

   1. In the **Conditions for rule \#1** dialog box, choose the **GetInstanceState.InstanceState** step output from the **Variable** dropdown.

   1. For **Operator**, choose **is equal to**.

   1. For **Value**, choose **String** from the dropdown list. Enter **stopped**.  
![Define a condition for a branch action.](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_tutorial_condition.png)

   1. Select **Save conditions**.

   1. Choose **Add new choice rule**.

   1. Choose **Add conditions** for **Rule \#2**.

   1. In the **Conditions for rule \#2** dialog box, choose the **GetInstanceState.InstanceState** step output from the **Variable** dropdown.

   1. For **Operator**, choose **is equal to**.

   1. For **Value**, choose **String** from the dropdown list. Enter **stopping**.

   1. Select **Save conditions**.

   1. Choose **Add new choice rule**.

   1. For **Rule \#3**, choose **Add conditions**.

   1. In the **Conditions for rule \#3** dialog box, choose the **GetInstanceState.InstanceState** step output from the **Variable** dropdown.

   1. For **Operator**, choose **is equal to**.

   1. For **Value**, choose **String** from the dropdown list. Enter **running**.

   1. Select **Save conditions**.

   1. In the **Default rule**, choose **Go to end** for the **Default step**.

1. Move a **Change an instance state** action to the empty **Drag action here** box under the **{{ GetInstanceState.InstanceState }} == "stopped"** condition.

   1. For the **Step name**, enter **StartInstance**.

   1. In the **Inputs** tab, under **Instance IDs**, choose the **InstanceId** document input value from the dropdown.

   1. For the **Desired state**, specify **`running`**.

1. Move a **Wait on AWS resource** action to the empty **Drag action here** box under the **{{ GetInstanceState.InstanceState }} == "stopping"** condition.

1. For **Step name**, enter a value. For this tutorial, use the name `WaitForInstanceStop`.

   1. For the **Service** field, choose **Amazon EC2**.

   1. For the **API** field, choose **DescribeInstances**.

   1. For the **Property selector** field, enter **$.Reservations[0].Instances[0].State.Name**.

   1. For the **Desired values** parameter, enter **`["stopped"]`**.

   1. In the **Configuration** tab of the **WaitForInstanceStop** action, choose **StartInstance** from the **Next step** dropdown.

1. Move a **Run command on instances** action to the empty **Drag action here** box under the **{{ GetInstanceState.InstanceState }} == "running"** condition.

1. For the **Step name**, enter **SayHello**.

   1. In the **Inputs** tab, enter **AWS-RunShellScript** for the **Document name** parameter.

   1. For **InstanceIds**, choose the **InstanceId** document input value from the dropdown.

   1. Expand the **Additional inputs** dropdown, and in the **Input name** dropdown, choose **Parameters**.

   1. In the **Input value** field, enter **`{"commands": "echo 'Hello World'"}`**.

1. Review the completed runbook in the canvas and select **Create runbook** to save the tutorial runbook.  
![Review and create the runbook.](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_tutorial_complete.png)

## Step 3: Review the auto-generated code
<a name="view-generated-code"></a>

As you move actions from the **Actions** browser onto the canvas, the visual design experience automatically composes the YAML or JSON content of your runbook in real-time. You can view and edit this code. To view the auto-generated code, select **Code** for the **Design** and **Code** toggle.

## Step 4: Run your new runbook
<a name="use-tutorial-runbook"></a>

After creating your runbook, you can run the automation.

**To run your new automation runbook**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Automation**, and then choose **Execute automation**.

1. In the **Automation document** list, choose a runbook. Choose one or more options in the **Document categories** pane to filter SSM documents according to their purpose. To view a runbook that you own, choose the **Owned by me** tab. To view a runbook that is shared with your account, choose the **Shared with me** tab. To view all runbooks, choose the **All documents** tab.
**Note**  
You can view information about a runbook by choosing the runbook name.

1. In the **Document details** section, verify that **Document version** is set to the version that you want to run. The system includes the following version options: 
   + **Default version at runtime** – Choose this option if the Automation runbook is updated periodically and a new default version is assigned.
   + **Latest version at runtime** – Choose this option if the Automation runbook is updated periodically, and you want to run the version that was most recently updated.
   + **1 (Default)** – Choose this option to run the first version of the document, which is the default.

1. Choose **Next**.

1. In the **Execute automation runbook** section, choose **Simple execution**.

1. In the **Input parameters** section, specify the required inputs. Optionally, you can choose an IAM service role from the **AutomationAssumeRole** list.

1. (Optional) Choose a CloudWatch alarm to apply to your automation for monitoring. If your alarm enters `ALARM` state, the automation is canceled and any defined `onCancel` steps run. If you use AWS CloudTrail, you see the `StopAutomationExecution` API call in your trail. For more information, see [Configuring Automations to monitor CloudWatch Alarms](automation-cw-alarm-monitoring.md).

1. Choose **Execute**. 

## Step 5: Clean up
<a name="cleanup-tutorial-runbook"></a>

**To delete your runbook**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/).

1. In the navigation pane, choose **Documents**.

1. Select the **Owned by me** tab.

1. Locate the **VisualDesignExperienceTutorial** runbook.

1. Select the button on the document card page, and then choose **Delete document** from the **Actions** dropdown.