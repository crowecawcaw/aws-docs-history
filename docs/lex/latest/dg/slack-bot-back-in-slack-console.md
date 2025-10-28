End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 5: Complete

Slack Integration

In this section, use the Slack API console to complete integration
of the Slack application.

1. Sign in to the Slack API console at [http://api.slack.com](http://api.slack.com "http://api.slack.com").
   Choose the app that you created in [Step 3: Create a Slack
   Application](slack-bot-assoc-create-app.md "slack-bot-assoc-create-app.md").
2. Update the **OAuth & Permissions**
   feature as follows:
   1. In the left menu, choose **OAuth &
      Permissions**.
   2. In the **Redirect URLs** section,
      add the OAuth URL that Amazon Lex provided in the
      preceding step. Choose **Add a new Redirect
      URL**, and then choose **Save
      URLs**.
   3. In the **Bot Token Scopes**
      section, add two permissions with the **Add
      an OAuth Scope** button. Filter the
      list with the following text:
      - `chat:write`
      - `team:read`

3. Update the **Interactivity &
   Shortcuts** feature by updating the
   **Request URL** value to the Postback
   URL that Amazon Lex provided in the preceding step. Enter the
   postback URL that you saved in step 4, and then choose
   **Save Changes**.
4. Subscribe to the **Event Subscriptions**
   feature as follows:
   - Enable events by choosing the
     **On** option.
   - Set the **Request URL** value to
     the Postback URL that Amazon Lex provided in the
     preceding step.
   - In the **Subscribe to Bot
     Events** section, subscribe to the
     `message.im` bot event to enable
     direct messaging between the end user and the Slack
     bot.
   - Save the changes.

5. Enable sending messages from the messages tab as follows:
   - From the left menu, choose **App
     Home**.
   - In the **Show Tabs** section,
     choose **Allow users to send Slash commands
     and messages from the messages
     tab.**

###### Next Step

[Step 6: Test the Integration](slack-bot-test.md "slack-bot-test.md")
