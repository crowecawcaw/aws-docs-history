

# Add Profile explorer to the agent workspace
<a name="add-profileexplorer-to-agentworkspace"></a>

By default users who have the appropriate [security profile permissions](enabling-profile-explorer.md) can view Profile explorer on the Connect Customer admin website. You might also want your agents to have access to Profile explorer in their agent workspace. This topic explains how to do that.

The following image shows an example of Profile explorer in the agent workspace. 

![The agent workspace, the Profile explorer tab.](http://docs.aws.amazon.com/connect/latest/adminguide/images/profile-explorer-agent-workspace.png)


## Create the Profile explorer layout you want to share with agents
<a name="begin-petoaw"></a>

Here's a high-level overview:

1. Make sure you have the [security profile permissions](enabling-profile-explorer.md) to create a Profile explorer layout.

1. Follow the instructions in [Get started with Connect Customer Customer Profiles Profile Explorer](getting-started-profile-explorer.md) to create and save the layout you want to share with agents.

## Add Profile explorer to Connect Customer as an integration
<a name="add-pe-console"></a>

1. On the Connect Customer console, in the left navigation, choose **Integrations**, as shown in the following image.   
![The Connect Customer console, the Integrations menu item.](http://docs.aws.amazon.com/connect/latest/adminguide/images/integrations.png)

1. On the **Integrations** page, choose **Add integration**.

1. On the **Add integration** page, complete following fields in the **Integration information** section:

   1. **Display name**: A friendly name for the application. **This name is displayed to your agents on the tab in the agent workspace**. It is also displayed on security profiles. You can come back and change this name.

   1. **Integration identifier**: The official name that is unique for your integration. If you have only one integration per access URL, we recommend that you use the origin of the access URL. You cannot change this name.

   1. **Description (optional)**: You might optionally provide any description for this application. This description is not displayed to agents.

   1. **Integration type**: Choose **Standard application**. 

   1. **Contact Scope**: Choose **Per contact**. This is a required setting for incoming call support.

   1. **Initialization timeout**: The maximum time, in milliseconds, allowed to establish a connection with the workspace. 

   The following image shows the configuration of these fields. Initialization timeout is set to 5 seconds.   
![The Integration information section, configured for the Profile explorer in the agent workspace.](http://docs.aws.amazon.com/connect/latest/adminguide/images/add-integration.png)

1. In the **Access** section, complete the following fields:

   1. **Access URL**: This is the URL where your application is hosted. The URL must be secure, starting with https, unless it's a local host.
**Important**  
The URL must contain `?_appLayoutMode=embedded`. For example:  
`https://{CONNECT_INSTANCE}/customer-profiles/profile-explorer?_appLayoutMode=embedded`  
If you don't include `?_appLayoutMode=embedded`, the left navigation from the Connect Customer admin website appears in the agent workspace.  
For more details about what is allowed for this field, see [Add a third-party application](3p-apps.md#onboard-3p-apps-how-to-integrate). 

   1. **Approved origins (optional)**: Allowlist URLs that should be permitted, if different than the access URL. The URL must be secure, starting with https, unless it's a local host.

1. Completing the next two sections—**Permissions** and **Iframe configuration**—is optional and not required to add the Profile explorer to the agent workspace. For information about these sections, see [Add a third-party application](3p-apps.md#onboard-3p-apps-how-to-integrate).

1. **Instance association**: Choose the instance your agents are using.

   You can give any instance(s) within this account-region access to this integration.

1. Choose **Add integration**.

## Assign agents permission to the new security profile
<a name="assign-pe-agent-permissions"></a>

In this step you need to assign agents permissions to access the new integration AND view permission to the Profile explorer.

1. In the Connect Customer admin website, navigate to the **Agent** security profile. 

1. On the **Edit security profile** page, assign the following permissions: 
   + **Customer Profiles** - **Profile explorer** - **View**
   + **Agent Applications** - **name of your integration** - **Access**

   The following image shows an example of permissions added for a new integration named **Profile explorer**.  
![Security profile permissions for the new integration.](http://docs.aws.amazon.com/connect/latest/adminguide/images/profile-explorer-securityperms.png)

## Tell agents to pin the new application
<a name="assign-pe-agent-permissions"></a>

Using your normal communication method, tell agents to pin the new application to their agent workspace. This allows them to access Profile explorer across workspace instances.
+ In the agent workspace, choose the more icon, then choose **Pin tab**, as shown in the following image.  
![The agent workspace, the Pin tab option.](http://docs.aws.amazon.com/connect/latest/adminguide/images/pin-tab.png)

## Supported functionality
<a name="supported-pe-functionality"></a>

After you complete the above steps, Profile explorer supports lookups on incoming contacts. The following are supported:
+ Phone and chat: Full support
+ Custom contact attributes: Full support for user-defined attributes that Profile explorer reads. You can set user-defined attributes within a flow to support any customer use case. For example:

  ```
  { 
  "profileSearchKey": "_phone", 
  "profileSearchValue": "<Phone number>" }
  ```

  For more information, see [Automatically populate customer profiles](auto-pop-customer-profile.md).