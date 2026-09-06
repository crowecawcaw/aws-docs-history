

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Chat client application permissions for Amazon Q Developer in chat applications
<a name="app-permissions"></a>

When you install Amazon Q Developer in chat applications on Microsoft Teams and Slack applications, each authorization process requests approval to grant Amazon Q Developer in chat applications app permissions. The following permissions are requested for each chat client.

## Microsoft Teams permissions
<a name="teams-app-permissions"></a>
+ Team.ReadBasic.All
+ Channel.ReadBasic.All
+ ChannelMember.Read.All
+ User.ReadBasic.All

For more information, see [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference).

## Slack permissions
<a name="slack-app-permissions"></a>
+ app\_mentions:read
+ channels:read
+ chat:write
+ chat:write.public
+ groups:read
+ team:read
+ users:read

For more information, see [Permission scopes](https://api.slack.com/scopes).