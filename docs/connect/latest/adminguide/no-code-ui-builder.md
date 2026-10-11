

# Build views with the UI builder in Connect Customer
<a name="no-code-ui-builder"></a>

You can use the UI builder to create views for step-by-step guides and workspace pages. With the UI builder, you can:
+ Drag and drop UI components onto a canvas.
+ Arrange your layout.
+ Edit the properties and styles of each component.

The following image shows an example of the UI builder page.

![The UI builder user interface.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-updates.png)

+ The **Create** panel, where you choose components from the **Library** tab or start from the **Templates** tab.
+ Components are grouped in collapsible sections, such as **General** and **Form**. Drag them onto the canvas.
+ The canvas, where you lay out the view.
+ The **Customize** panel. Choose the global settings icon to set page-wide properties, such as columns, alignment, and colors. Select a component on the canvas to set its properties.

  The following image shows an example of the **Properties** tab for the **Address** component. Choose the dynamic icon (the lightning bolt) to fill the field at runtime.  
![The Customize panel, the Properties tab, the dynamic icon.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-properties.png)

## Access the UI builder
<a name="no-code-ui-builder-how-to-access"></a>

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/. Use an Admin account, or an account that has the **Channels and flows - Views** permission in its security profile.

1. In the Connect Customer admin website, choose **UI Management**.

1. Choose **Create View**. In the **Create View** dialog box, specify a name for the view and choose the **Purpose type**. Views have two purposes:
   + **Guides**: Single-step or multistep workflows for agents, end customers, or managers. Guides show contact-specific or third-party data in one interface.
   + **Workspace Page**: Pages in a workspace, such as the home page. Workspace pages don't depend on a contact.

1. The UI builder opens. Start from a template, or build the view from scratch.

1. Choose **Create new**. An empty UI builder page appears, as shown in the following image.  
![An empty UI builder page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-blank-page.png)