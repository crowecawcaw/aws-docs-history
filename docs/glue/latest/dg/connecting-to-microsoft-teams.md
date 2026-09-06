

# Connecting to Microsoft Teams
<a name="connecting-to-microsoft-teams"></a>

 Microsoft Teams is a collaborative workspace within Microsoft 365 that acts as a central hub for workplace conversations, collaborative teamwork, video chats and document sharing, all designed to aid worker productivity in a unified suite of tools. 

**Topics**
+ [AWS Glue support for Microsoft Teams](microsoft-teams-support.md)
+ [Policies containing the API operations for creating and using connections](microsoft-teams-configuring-iam-permissions.md)
+ [Configuring Microsoft Teams](microsoft-teams-configuring.md)
+ [Configuring Microsoft Teams connections](microsoft-teams-configuring-connections.md)
+ [Reading from Microsoft Teams entities](microsoft-teams-reading-from-entities.md)
+ [Microsoft Teams connection option reference](microsoft-teams-connection-options.md)
+ [Limitations](microsoft-teams-connector-limitations.md)
+ [Create a new Microsoft Teams account:](#microsoft-teams-account-creation)

## Create a new Microsoft Teams account:
<a name="microsoft-teams-account-creation"></a>

1.  Navigate to Microsoft Teams’s homepage, [https://account.microsoft.com/account/](https://account.microsoft.com/account/) and choose **Sign in**. 

1.  Choose **Create one\!**. 

1.  Enter the required information for account creation and create a new account. 

1.  Navigate to the Microsoft Teams website at [ https://www.microsoft.com/en-in/microsoft-teams/log-in](https://www.microsoft.com/en-in/microsoft-teams/log-in). 

1.  Sign up using the Microsoft Account you just created. 

1.  After successful sign up on Teams, navigate to [https://account.microsft.com/services](https://account.microsft.com/services). 

1.  Choose **Try Microsoft 365**. 

1.  Activate one of below Microsoft 365 or Microsoft Teams subscription to access all required features of Microsoft Teams connector: 
   + Microsoft Teams Essentials
   + Microsoft 365 Business
   + Microsoft 365 Business Basic
   + Microsoft 365 Business Standard
   + Microsoft 365 Business Premium

**Create a managed client app:**

1.  To create a managed application, you need to register a new OAuth app on Microsoft Entra (formerly Azure Active Directory): 

1.  Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com). 

1.  If you have access to multiple tenants, use the Settings icon in the top menu to switch to the tenant in which you want to register the application from the Directories \+ subscriptions menu. 

1.  Navigate to Identity > Applications > App registrations and select **New registration**. 

1. Enter a display Name for your application.

1.  Specify who can use the application in the Supported account types section. To make this app global select “Accounts in any organizational directory” or “Accounts in any organizational directory and personal Microsoft accounts”. 

1.  Enter Redirect URI `https://{region}.console.aws.amazon.com/appflow/oauth`. For example, for the `us-west-2 region`, add `https://us-west-2.console.aws.amazon.com/appflow/oauth`. You can add multiple URLs for different regions that you want to use.

1.  Register the app. 

1.  Note the Client ID for future use. 

1.  Choose **Add a certificate or secret** in the Essentials section. 

1.  Choose **New Client Secret**. 

1.  Enter Description and Expires duration. 

1.  Copy and save the client secret for future use. 

1.  In the left side menu list, select **API permissions**. 

1.  Choose **Add a permission**. 

1.  Select “Microsoft Graph“. 

1.  Select “Delegated permissions”. 

1.  Check all the following permissions: 
   + User.Read
   + Offline\_access
   + User.Read.All
   + User.ReadWrite.All
   + TeamsTab.ReadWriteForTeam
   + TeamsTab.ReadWriteForChat
   + TeamsTab.ReadWrite.All
   + TeamsTab.Read.All
   + TeamSettings.ReadWrite.All
   + TeamSettings.Read.All
   + TeamMember.ReadWrite.All
   + TeamMember.Read.All
   + Team.ReadBasic.All
   + GroupMember.ReadWrite.All
   + GroupMember.Read.All
   + Group.ReadWrite.All
   + Group.Read.All
   + Directory.ReadWrite.All
   + Directory.Read.All
   + Directory.AccessAsUser.All
   + Chat.ReadWrite
   + Chat.ReadBasic
   + Chat.Read
   + ChannelSettings.ReadWrite.All
   + ChannelSettings.Read.All
   + ChannelMessage.Read.All
   + Channel.ReadBasic.All

1.  Choose **Add permissions**. Your app is now setup successfully. You can use the client ID and client secret to create a new connection. For more information, see [https://learn.microsoft.com/en-us/graph/auth-register-app-v2](https://learn.microsoft.com/en-us/graph/auth-register-app-v2). 