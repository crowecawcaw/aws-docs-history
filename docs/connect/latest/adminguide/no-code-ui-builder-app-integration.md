

# Use screen pop functionality of third-party applications in the Connect Customer agent workspace
<a name="no-code-ui-builder-app-integration"></a>

To screen pop a third-party application, use step-by-step guides. For more information, see [Access 3P apps in the agent workspace](3p-apps-agent-workspace.md). When a contact arrives, the **Guides** tab opens first in the agent workspace. You can [configure the step-by-step guides](how-to-invoke-a-flow-sg.md) using flows.

**Note**  
When you configure a view:   
Make sure that the app name registered in the AWS Management Console exactly matches the app name that you are providing to the [Application](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/ui-component-application--with-agent-workspace-example) or App Launch component. 
If you get errors even though the names match, check the application name in the AWS Management Console for leading or trailing spaces.
+ With the [Application](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/ui-component-application--with-agent-workspace-example) component, you embed the application in the **Guides** tab, which opens first when a contact arrives.
+ With the App Launch component, the application opens in its own tab in the agent workspace. If you turn on auto-open, the guide keeps focus in the first tab and the application opens in another tab.
+ You can also use the [Link](https://d3irlmavjxd3d8.cloudfront.net/?path=/story/ui-component-link--default-case) component with auto-open to open any browser link in a new window.

You can also provide a path to send the contact to a more specific destination. The guide adds the path to the origin of the registered app domain, such as `https://example.com/`. End the registered app domain with a forward slash.

**Example 1 (Recommended)**:

```
App Domain registered in AWS Management Console: https://example.com/
Path: cats/siamese
Guides render: Domain https://example.com/ + Path cats/siamese
https://example.com/cats/siamese
Success if website exists!
```

**Example 2**:

```
App Domain registered in AWS Management Console: https://example.com/dogs/
Path: cats/siamese
Guides render: Domain https://example.com/ + Path cats/siamese
https://example.com/cats/siamese
Fails because only paths under https://example.com/dogs/ are allowed
```

**Example 3**:

```
App Domain registered in AWS Management Console: https://example.com/cats
Path: cats/siamese
Guides render: Domain https://example.com/ + Path cats/siamese
https://example.com/cats/siamese
Success if website exists!
```

The following image shows an App Launch component that's been dropped onto the canvas. The **Customize** panel shows an example of specifying the app name and app path.

![The Customize panel, an example app name and app path.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-app-integration-1.png)


The following image shows an example [Flow block in Connect Customer: Set event flow](set-event-flow.md) block that's added to the flow, and configured to the **DefaultAgentUI** event hook.

![A Set event flow block that is configured to the DefaultAgentUI event hook.](https://docs.aws.amazon.com/connect/latest/adminguide/images/no-code-ui-builder-app-integration-2.png)
