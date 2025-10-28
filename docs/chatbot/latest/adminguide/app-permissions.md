AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Chat client application permissions for Amazon Q Developer in chat applications

When you install Amazon Q Developer in chat applications on Microsoft Teams and Slack applications, each authorization process requests approval to grant Amazon Q Developer in chat applications app permissions.
The following permissions are requested for each chat client.

## Microsoft Teams permissions

- Team.ReadBasic.All
- Channel.ReadBasic.All
- ChannelMember.Read.All
- User.ReadBasic.All

For more information, see [Microsoft Graph permissions reference](https://learn.microsoft.com/en-us/graph/permissions-reference "https://learn.microsoft.com/en-us/graph/permissions-reference").

## Slack permissions

- app_mentions:read
- channels:read
- chat:write
- chat:write.public
- groups:read
- team:read
- users:read

For more information, see [Permission scopes](https://api.slack.com/scopes "https://api.slack.com/scopes").
