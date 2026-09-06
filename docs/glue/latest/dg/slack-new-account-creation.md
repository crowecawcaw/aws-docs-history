

# Creating a new Slack account and configuring the client app
<a name="slack-new-account-creation"></a>

**Creating a Slack account**

1. Open the [Slack home page](https://slack.com/intl/en-in/) to sign-up for an account. 

1. Choose **SIGN UP WITH EMAIL ADDRESS**. Enter your email ID and choose **Continue**.

1. Enter the 6-character code sent to your email address, it will redirect you to create a workspace or to join an existing workspace.

1. Choose **Create a workspace** to create a new workspace. It will redirect you to answer a few questions as a part of the set-up process.
   + Name of company
   + Your name
   + To add colleagues by email
   + What's your team working on? (This will be the channel name)

1. Fill in the input fields for these questions and continue. Your account is now ready to be used.



**Creating a Slack developer app**

1. Log in to your Slack account and sign into your Slack workspace.

1. From the workspace menu, select **Tools and settings** and then select **Manage apps**.

1. From the Slack App Directory menu, select **Build**.

1. On the **Your Apps** page, select **Create an App**.

1. On the **Create an app** page, select **From scratch**.

1. In the **Name app & choose workspace** dialog box that opens, add an App name and **Pick a workspace to deploy your app in**. Then select **Create App**.

1. Note down your Client Id and Secret displayed in App Credentials

1. On the OAuth & Permissions sidebar, go to Scopes and choose **Add an OAuth Scope**. You can add the redirect URLs to your app for configuration to automatically generate the 'Add to Slack' button or to distribute your app. Scroll up to the Redirect URLs section and choose **Add New Redirect URL** and save. 

1. Then, scroll to OAuth Tokens for Your Workspace section, and choose **Install to Workspace**.

1. On the dialog box that opens up informing you that the app that you created is requesting permission to access the Slack workspace you wanted to connect it to, select **Allow**.

1. On successful completion, the console will display a OAuth Tokens for Your Workspace screen.

1. From the OAuth Tokens for Your Workspace screen, copy and save the OAuth token you will use to connect to AWS Glue

1. Next, you retrieve your Slack team ID. From the Slack workspace menu, select **Tools and settings** and then select **Manage apps**. You'll find your team ID in the URL of the page that opens.

1. To publicly distribute your app, you can activate by heading over to the **Manage Distribution** button on the sidebar. Scroll down to the Share Your App with Other Workspaces section and choose **Remove Hard Coded Information**. Provide consent and choose **Active Public Distribution**. 

1. Your app is now publicly distributed. To access the entity APIs, the app needs to be added to every workspace channel the user wants to access from.

1. Sign into your slack account and open the workspace whose channel needs to be accessed.

1. In the workspace, open the channel for which the app wants to access and choose the channel title. Select the **Integrations** tab from the pop-up and add the app. In this way, the app is integrated with the channel to have access to its API.

   The OAuth 2.0 client ID must have one or more authorized redirect URLs. Redirect URLs have the following format:
**Note**  
 Appflow redirect URLs are subject to change post redirect URLs for AWS Glue platform are available. Client ID and Client Secret are from the settings for your OAuth 2.0 client ID.     
<a name="slack-redirect-url-detail"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/slack-new-account-creation.html)