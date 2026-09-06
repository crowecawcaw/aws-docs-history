

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Overview of the visual design experience interface
<a name="visual-designer-interface-overview"></a>

The visual design experience for Systems Manager Automation is a low-code visual workflow designer that helps you create automation runbooks.

Get to know the visual design experience with an overview of the interface components:

![Visual design experience components](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_overview.png)

+ The **Actions** browser contains the **Actions**, **AWS APIs**, and **Runbooks** tabs.
+ The *canvas* is where you move actions into your workflow graph. You can also change the order of actions and select them to configure.
+ The **Form** panel is where you can view and edit the properties of any action that you selected on the canvas. Select the **Content** toggle to view the YAML or JSON for your runbook, with the currently selected action highlighted. 

**Info** links open a panel with contextual information when you need help. These panels also include links to related topics in the Systems Manager Automation documentation. 

## Actions browser
<a name="visual-designer-actions"></a>

From the **Actions** browser, you can select actions to move into your workflow graph. You can search all actions using the search field at the top of the **Actions** browser. The **Actions** browser contains the following tabs:
+ The **Actions** tab provides a list of automation actions that you can move into your runbook's workflow graph in the canvas.
+ The **AWS APIs** tab lists AWS APIs that you can move into your runbook's workflow graph.
+ The **Runbooks** tab provides ready-to-use runbooks as building blocks. For example, you can use them to perform common remediation tasks on Amazon EC2 instances without re-creating the same actions.

![Visual design experience actions browser](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_actions_multi_view.png)


## Canvas
<a name="visual-designer-canvas"></a>

After you choose an action, drag it to the canvas and drop it into your workflow graph. You can also move actions to reorder them. If your workflow is complex, you might not see all of it at once. Use the controls at the top to zoom in or out. To view other parts, move the workflow graph in the canvas. 

Move an action from the **Actions** browser into your runbook's workflow graph. A line shows where it will be placed in your workflow. To change the order of an action, you can move it to a different place in your workflow. The new action has been added to your workflow, and its code is auto-generated.

![Visual design experience canvas](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_canvas.png)


## Form
<a name="visual-designer-form"></a>

After you add an action to your runbook workflow, you can configure it to meet your use case. Choose the action that you want to configure, and you see its parameters and options in the **Form** panel. You can also see the YAML or JSON code by choosing the **Content** toggle. The code associated with the action you have selected is highlighted.

![Visual design experience form panel](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_form.png)


![Visual design experience content panel](http://docs.aws.amazon.com/systems-manager/latest/userguide/images/visual_designer_content.png)


## Keyboard shortcuts
<a name="visual-designer-keyboard-shortcuts"></a>

The visual design experience supports the keyboard shortcuts shown in the following table.


| Keyboard shortcut | Function | 
| --- | --- | 
| Ctrl\+Z | Undo the last operation. | 
| Ctrl\+Shift\+Z | Redo the last operation. | 
| Alt\+C | Center the workflow in the canvas. | 
| Backspace | Remove all selected states. | 
| Delete | Remove all selected states. | 
| Ctrl\+D | Duplicate the selected state. | 