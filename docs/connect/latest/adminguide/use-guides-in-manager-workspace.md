

# Use step-by-step guides in workspaces
<a name="use-guides-in-manager-workspace"></a>

You can use step-by-step guides for users other than the agents in your contact center, including managers and other business users. Add a guide to a workspace page, so these users can follow a structured workflow outside of a contact. Before you start, [set up a workspace](amazon-connect-workspaces.md).

In the UI builder, drag the **Connect Application** component onto the canvas. The component embeds a Connect Customer application, such as a guide, in the view. Configure the following properties:
+ **Application Namespace** – The type of application to embed.
+ **ContactFlowId** – If you choose **Guide** as the application namespace, the contact flow ID of the guide to run.

To start the guide, users choose **Begin**. The guide runs on a chat contact that starts in the background. After the guide finishes, users choose **Restart** to run it again from the start.

**Note**  
You can embed a guide only in a view that you use as a workspace page. You can't embed a guide in a view that's already part of a guide.