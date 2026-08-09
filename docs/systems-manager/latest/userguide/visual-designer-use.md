# Using the visual design experience

Learn to create, edit, and run runbook workflows using the visual design experience. When your workflow
is ready, save or export it. You can also use it for rapid
prototyping.

## Create a runbook workflow

1. Sign in to the [Systems Manager Automation console](https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/ "https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/").
2. Choose **Create runbook**.
3. In the **Name** box, enter a name for your runbook, for example,
   `MyNewRunbook`.
4. Next to the **Design** and **Code** toggle, select
   the pencil icon and enter a name for your runbook.

You can now design a workflow for your new runbook.

## Design a runbook

To design a runbook workflow, drag an automation action from
the **Actions** browser into the canvas. Place it where you want it in
your workflow. You can re-order actions by dragging them to
a different location. As you drag an action onto the canvas, a line shows where you can
drop it. After you drop an action, its code is
auto-generated and added to your runbook's content.

Use the search box at the top of the
**Actions** browser to find an action by name.

After you drop an action onto the canvas, configure it using the
**Form** panel on the right. This panel has
**General**, **Inputs**, **Outputs**,
and **Configuration** tabs for each action
on the canvas. The **General** tab has the
following sections:

- The **Step name** identifies the step. Specify a unique value for
  the step name.
- The **Description** helps you describe what the action is doing in
  your runbook's workflow.

The **Inputs** tab contains fields that vary based on the action. For
example, the `aws:executeScript` automation action consists of the following
sections:

- The **Runtime** is the language to use for running the provided
  script.
- The **Handler** is the name of your function. You must ensure that
  the function defined in the handler has two parameters: `events` and
  `context`. The PowerShell runtime doesn't support this
  parameter.
- The **Script** is an embedded script that you want to run during
  the workflow.
- (Optional) The **Attachment** is for standalone scripts or .zip
  files that can be invoked by the action. This parameter is required for JSON
  runbooks.

The **Outputs** tab helps you specify the values that you want to
output from an action. You can reference output values in later actions of your workflow, or
generate output from actions for logging purposes. Not all actions will have an
**Outputs** tab because not all actions support outputs. For example, the
`aws:pause` action doesn't support outputs. For actions that do support
outputs, the **Outputs** tab consists of the following sections:

- The **Name** is the name to be used for the output value. You can
  reference outputs in later actions of your workflow.
- The **Selector** is a JSONPath expression string
  beginning with `"$."` that is used to select one or more components within a
  JSON element.
- The **Type** is the data type for the output value. For example, a
  `String` or `Integer` data type.

The **Configuration** tab contains properties and options that all
automation actions can use. The action consists of the following sections:

- The **Max attempts** property is the number of times an action
  retries if it fails.
- The **Timeout seconds** property specifies the timeout value for an
  action.
- The **Is critical** property determines if the action failure stops
  the entire automation.
- The **Next step** property determines which action the automation
  goes to next in the runbook.
- The **On failure** property determines which action the automation
  goes to next in the runbook if the action fails.
- The **On cancel** property determines which action the automation
  goes to next in the runbook if the action is canceled by a user.

To delete an action, you can use backspace, the toolbar above the canvas, or right-click
and choose **Delete action**.

As your workflow grows, it might not fit in the canvas. To help make the workflow fit in
the canvas, try one of the following options:

- Use the controls on the side panels to resize or close the panels.
- Use the toolbar at the top of the canvas to zoom the workflow graph in or
  out.

## Update your runbook

You can update an existing runbook workflow by creating a new version of your runbook.
Updates to your runbooks can be made by using the visual design experience, or by editing the code
directly. To update an existing runbook, use the following procedure:

1. Sign in to the [Systems Manager Automation console](https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/ "https://console.aws.amazon.com/systems-manager/automation/home?region=us-east-1#/").
2. Choose the runbook that you want to update.
3. Choose **Create new version**.
4. The visual design experience has two panes: A code pane and a visual workflow pane. Choose
   **Design** in the visual workflow pane to edit your workflow with the
   visual design experience. When you're done, choose **Create new version** to save
   your changes and exit.
5. (Optional) Use the code pane to edit the runbook content in YAML or JSON.

## Export your runbook

To export your runbook's workflow YAML or JSON code, and also a graph of your workflow,
use the following procedure:

1. Choose your runbook in the **Documents** console.
2. Choose **Create new version**.
3. In the **Actions** dropdown, choose whether you want to export the
   graph or runbook, and which format you prefer.
