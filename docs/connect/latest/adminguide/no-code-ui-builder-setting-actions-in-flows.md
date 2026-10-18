

# Set actions that appear as flow branches in the Show view block
<a name="no-code-ui-builder-setting-actions-in-flows"></a>

In step-by-step guides, users choose a button to move to the next page. You configure these buttons in the UI builder by setting an **Action** for each button. For example, you can configure a button to submit a form.

When a user chooses the button at runtime, the guide sends the button's action to the flow. The **Action** value determines the branching path from the [Show view](show-view-block.md) block.

For example, a view with three buttons, each with a different action, gives the [Show view](show-view-block.md) block three branches. You then build the logic for each branch in the flow.

The following image shows an example of the **Action** section in the **Customize** panel of the UI builder.

![The Action section of the Customize panel in the UI builder.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-setting-actions-in-flows-example.png)
