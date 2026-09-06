

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Setting up Slack for connecting to Amazon Q
<a name="slack-credentials"></a>

Before you connect Slack to Amazon Q, you need to create and retrieve the Slack credentials you will use to connect Slack to Amazon Q. You will also need to add any permissions needed by Slack to connect to Amazon Q.

The following procedure gives you an overview of how to configure Slack for connecting with Amazon Q. 

**Configuring Slack authentication for Amazon Q**

1. Log in to your [Slack account](https://slack.com/signin) and sign into your Slack workspace.
**Note**  
To configure Slack for Amazon Q, you must be an admin user in the Slack account.

1. From the workspace menu, select **Tools and settings** and then select **Manage apps**.  
![Screenshot of the Slack workspace menu showing how to access the App Directory to create a new app for integration.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-1.png)

1. From the **Slack App Directory** menu, select **Build**.  
![Screenshot of the Slack App Directory menu with the "Build" option highlighted, which is used to create a new app for integration.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-2.png)

1. On the **Your Apps** page, select **Create an App**.  
![Screenshot of the Slack "Your Apps" page showing the "Create an App" button that users need to click to begin creating a new Slack app.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-3.png)

1. On the **Create an app** page, select **From scratch**.  
![Screenshot of the Slack "Create an app" page showing the "From scratch" option that allows users to create a new app from the beginning.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-4.png)

1. In the **Name app & choose workspace** dialog box that opens, add an **App name** and **Pick a workspace to deploy your app in**. Then select **Create App**.  
![Screenshot of the "Name app & choose workspace" dialog box where users enter an app name and select a workspace for deployment.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-11.png)

1. On the **Basic Information** page, from the **Settings** menu, select **OAuth & Permissions**.  
![Screenshot of the Slack app's "Basic Information" page with the "OAuth & Permissions" option highlighted in the Settings menu.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-5.png)

1. On the **OAuth & Permissions** page, go to **Scopes**, and then do the following based on whether you want to use a Bot Token to connect Slack to Amazon Q, or a User Token:
**Important**  
If you use the bot token as part of your Slack credentials, you cannot index direct messages and group messages, and you must add the bot token to the channel you want to index. For information on Slack token types, see [Token types](https://api.slack.com/authentication/token-types) in Slack API.
   + Add the following **Bot Token Scopes**:  
![Screenshot of the Slack "OAuth & Permissions" page showing the Bot Token Scopes section where users can add permission scopes for the bot.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-6.png)
     + `channels:history` – View messages and other content in public channels that your app has been added to
     + `channels:manage` – Manage public channels that your app has been added to and create new ones
     + `channels:read` – View basic information about public channels in a workspace
     + `conversations.connect:manage` – Receive Slack Connect invite events sent to the channels your app is in
     + `conversations.connect:read` – Receive Slack Connect invite events sent to the channels your app is in
     + `files:read` – View files shared in channels and conversations that your app has been added to
     + `groups:history` – View messages and other content in private channels that your app has been added to
     + `groups:read` – View basic information about private channels that your app has been added to
     + `im:history` – View messages and other content in direct messages that your app has been added to
     + `im:read` – View basic information about direct messages that your app has been added to
     + `mpim:history` – View messages and other content in group direct messages that your app has been added to 
     + `mpim:read` – View basic information about group direct messages that your app has been added to
     + `reactions:read` – View emoji reactions and their associated content in channels and conversations that your app has been added to
     + `team:read` – View the name, email domain, and icon for workspaces your app is connected to
     + `usergroups:read` – Create and manage user groups
     + `users.profile:read` – View profile details about people in a workspace
     + `users:read` – View people in a workspace
     + `users:read.email` – View email addresses of people in a workspace
   + Add the following **User Token Scopes**:  
![Screenshot of the Slack "OAuth & Permissions" page showing the User Token Scopes section where users can add permission scopes for user-level access.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-7.png)
     + `channels:history` – View messages and other content in a user’s public channels
     + `channels:read` – View basic information about public channels in a workspace
     + `emoji:read` – View custom emoji in a workspace
     + `files:read` – View files shared in channels and conversations that a user has access to
     + `groups:history` – View messages and other content in a user’s private channels
     + `groups:read` – View basic information about a user’s private channels
     + `im:history` – View messages and other content in a user’s direct messages
     + `im:read` – View basic information about a user’s direct messages
     + `mpim:history` – View messages and other content in a user’s group direct messages
     + `mpim:read` – View basic information about a user’s group direct messages
     + `team:read` – View the name, email domain, and icon for workspaces a user is connected to
     + `users.profile:read` – View profile details about people in a workspace
     + `users:read.email` – View email addresses of people in a workspace
     + `users:read` – View people in a workspace

1. Then, scroll to **OAuth Tokens** section, and choose **Install to Workspace**.  
![Screenshot of the Slack "OAuth & Permissions" page showing the "Install to Workspace" button that users need to click to install the app to their workspace.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-8.png)

1. On the dialog box that opens up informing you that the app that you created is requesting permission to access the Slack workspace you wanted to connect it to, select **Allow**.  
![Screenshot of the Slack permission request dialog box asking for authorization to access the workspace, with an "Allow" button for users to grant permissions.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-9.png)

   On successful completion, the console will display a **OAuth Tokens** screen.

1. From the **OAuth Tokens** screen, copy and save the OAuth token you will use to connect to Amazon Q—either **User OAuth Token** or **Bot User OAuth Token**. You input this as **Slack token** when you connect to Amazon Q.  
![Screenshot of the Slack "OAuth Tokens" screen displaying the generated OAuth tokens that need to be copied for connecting to Amazon Q Business.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-10.png)

1. Next, you retrieve your Slack team ID. You need this to connect to Amazon Q.

   From the Slack workspace menu, select **Tools and settings** and then select **Manage apps**. You'll find your team ID in the URL of the page that opens.   
![](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-1.png)  
![Screenshot showing the URL of the Slack workspace management page with the team ID highlighted, which is needed for connecting to Amazon Q Business.](http://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/images/slack-12.png)

You now have the Slack Team ID and Slack token you need to connect to Amazon Q.