# Microsoft Teams integration

With Microsoft Teams integration, you can create actions that interact with Microsoft Teams for messaging, channel management, meeting operations, and team collaboration. This integration supports action capabilities for managing Teams communications and workflows.

## What you can do

Microsoft Teams integration provides team collaboration capabilities to help you work with your Microsoft Teams environment.

**Action integration**

Execute Microsoft Teams actions such as sending messages, managing channels, creating meetings, and accessing team information through Microsoft Graph API calls.

## Before you begin

Make sure you have the following before you set up Microsoft Teams integration.

- Microsoft 365 account with Teams access.
- Azure Active Directory application registration.
- Appropriate Teams permissions and roles.
- Author or higher.
- Administrative access to configure OAuth applications.

## Set up Microsoft Teams integration

Follow these steps to create your Microsoft Teams integration.

1.  In the console, choose **Integrations**.
2.  Choose **Microsoft Teams** from the integration options, and
    click the Add (plus "+") button.
3.  Fill in the integration details:
    - **Name** - Descriptive name for your Microsoft Teams integration.
    - **Description** (Optional) - Purpose of the integration.

4.  Choose your connection type:
    - **User authentication** - OAuth-based authentication for individual user access.
    - **Service authentication** - Application permissions for automated access.

5.  Fill in the connection settings based on your selected authentication method (either user or service):
    1.  For **User authentication (OAuth)**, configure the following fields:

            * **Client ID** - Azure AD application client ID.
            * **Client Secret** - Azure AD application client secret.
            * **Token URL** - Microsoft OAuth token endpoint.
            * **Auth URL** - Microsoft OAuth authorization endpoint.
            * **Redirect URL** - OAuth redirect URI.

        **Required OAuth scopes:**

            * `ChatMessage.Send` - Send chat messages.
            * `ChannelMessage.Read.All` - Read channel messages.
            * `ChannelMessage.Send` - Send channel messages.
            * `Chat.ReadWrite` - Read and write chat information.
            * `Team.ReadBasic.All` - Read basic team information.
            * `TeamMember.ReadWrite.All` - Read and write team member information.
            * `Channel.ReadBasic.All` - Read basic channel information.
            * `ChannelMember.ReadWrite.All` - Read and write channel member information.
            * `OnlineMeetingRecording.Read.All` - Read meeting recordings.
            * `OnlineMeetingTranscript.Read.All` - Read meeting transcripts.
            * `User.Read.All` - Read user profiles.
            * `offline_access` - Maintain access when user is offline.

    2.  For **Service authentication (Application permissions)**, configure the following fields:

            * **Client ID** - Service application client ID.
            * **Client Secret** - Service application client secret.
            * **Token URL** - Microsoft OAuth token endpoint.

        **Required scope for token generation:**

            * `.default` - Default application permissions scope.

        **Set the following scopes in your Azure AD application:**

            * `Chat.Send` - Send chat messages.
            * `ChannelMessage.Read.All` - Read channel messages.
            * `ChannelMessage.Send` - Send channel messages.
            * `Chat.Read.All` - Read chat information.
            * `Team.ReadBasic.All` - Read basic team information.
            * `TeamMember.ReadWrite.All` - Read and write team member information.
            * `Channel.ReadBasic.All` - Read basic channel information.
            * `ChannelMember.ReadWrite.All` - Read and write channel member information.
            * `OnlineMeetingRecording.Read.All` - Read meeting recordings.
            * `OnlineMeetingTranscript.Read.All` - Read meeting transcripts.
            * `User.Read.All` - Read user profiles.

6.  Select **Create and continue**.
7.  Choose users to share the integration with.
8.  Click **Next**.

## Available actions

Microsoft Teams integration provides the following action capabilities.

- Send messages to channels and chats.
- Create and manage team channels.
- Manage team and channel memberships.
- Read channel and chat messages.
- Access meeting recordings and transcripts.
- Retrieve team and user information.
- Manage team settings and configurations.

###### Note

The specific actions available depend on the OAuth scopes configured and the permissions granted during authentication.

## Manage Microsoft Teams integrations

After you create your Microsoft Teams integration, you can manage it through several options.

- **Edit integration** - Update OAuth settings or Teams configuration.
- **Share integration** - Make the integration available to other users.
- **Monitor usage** - View integration activity and API usage.
- **Review actions** - See available Microsoft Teams actions.
- **Delete integration** - Remove the integration and revoke Teams access.
