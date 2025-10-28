# Measuring business performance with Analytics

With Analytics, you can evaluate the performance of your bot with metrics that are related
to success and failure rates of your bots’ interactions with customers. You can also
visualize patterns of conversation flows between your bot and customers. Analytics
streamlines your experience by summarizing these metrics in graphs and charts. Analytics provides
tools to help you filter results to identify issues and problems involving
intents, slots, utterances, and conversations. You can use this data to iterate and improve
upon your bot to create a better customer experience.

###### Note

For a user to access Analytics, either the [AWS
managed policy: AmazonLexFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexFullAccess") or a custom policy that includes analytics API permissions must be attached to their
IAM role. See [Managing access permissions for analytics](analytics-permissions.md "analytics-permissions.md") for details on how to handle user permissions with a custom policy. If the [AWS
managed policy: AmazonLexReadOnly](security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexReadOnly "security-iam-awsmanpol.md#security-iam-awsmanpol-AmazonLexReadOnly") is attached to a customer's
IAM role, an error displays the missing permissions that you need to add to the user's
IAM role for them to be able to access the Analytics dashboards.

###### To access Analytics

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home "https://console.aws.amazon.com/lexv2/home").
2. In the navigation pane under **Bots**, select the bot you want to
   view in analytics.
3. Select the section under **Analytics** that you want to view.

###### Topics

- [Key definitions](analytics-key-definitions.md "analytics-key-definitions.md")
- [Filtering results](analytics-filter.md "analytics-filter.md")
- [Overview: a summary of your bot performance](analytics-overview.md "analytics-overview.md")
- [Conversation dashboard: a summary of your bot
  conversations](conversation-dashboard.md "conversation-dashboard.md")
- [Performance dashboard: a summary of your bot's
  intent and utterance metrics](performance-dashboard.md "performance-dashboard.md")
- [Using APIs for analytics](analytics-api.md "analytics-api.md")
- [Managing access permissions for analytics](analytics-permissions.md "analytics-permissions.md")
