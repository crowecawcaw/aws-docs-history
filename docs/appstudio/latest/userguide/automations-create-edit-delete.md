

# Creating, editing, and deleting automations
<a name="automations-create-edit-delete"></a>

**Contents**
+ [Creating an automation](#automations-create)
+ [Viewing or editing automation properties](#automations-edit)
+ [Deleting an automation](#automations-delete)

## Creating an automation
<a name="automations-create"></a>

Use the following procedure to create an automation in an App Studio application. Once created, an automation must be configured by editing its properties and adding actions to it.

**To create an automation**

1. If necessary, navigate to the application studio of your application.

1. Choose the **Automations** tab.

1. If you have no automations, choose **\+ Add automation** in the canvas. Otherwise, in the left-side **Automations** menu, choose **\+ Add**.

1. A new automation will be created, and you can start editing its properties or adding and configuring actions to define your application's business logic.

## Viewing or editing automation properties
<a name="automations-edit"></a>

Use the following procedure to view or edit automation properties.

**To view or edit automation properties**

1. If necessary, navigate to the application studio of your application.

1. Choose the **Automations** tab.

1. In the left-hand **Automations** menu, choose the automation for which you want to view or edit properties to open the right-side **Properties** menu.

1. In the **Properties** menu, you can view the following properties:
   + **Automation identifier**: The unique name of the automation. To edit it, enter a new identifier in the text field.
   + **Automation parameters**: Automation parameters are used to pass dynamic values from your app's UI to automation and data actions. To add a parameter, choose **\+ Add**. Choose the pencil icon to change the parameter's name, description, or type. To remove a parameter, choose the trash icon.
**Tip**  
You can also add automation parameters directly from the canvas.
   + **Automation output**: The automation output is used to configure which data from the automation can be referenced in other automations or components. By default, automations do not create an output. To add an automation output choose **\+ Add**. To remove the output, choose the trash icon.

1. You define what an automation does by adding and configuring actions. For more information about actions, see [Adding, editing, and deleting automation actions](automations-actions-add-edit-delete.md) and [Automation actions reference](automations-actions-reference.md).

## Deleting an automation
<a name="automations-delete"></a>

Use the following procedure to delete an automation in an App Studio application.

**To delete an automation**

1. If necessary, navigate to the application studio of your application.

1. Choose the **Automations** tab.

1. In the left-side **Automations** menu, choose the ellipses menu of the automation you want to delete, and choose **Delete**. Alternatively, you can choose the trash icon from the right-side **Properties** menu of the automation.

1. In the confirmation dialog box, choose **Delete**.