# Step 4: Complete Slack

integration with your Lex V2 bot

In this section, use the Slack API console to complete integration
with the Slack application.

1. Sign in to the Slack API console at [https://api.slack.com](https://api.slack.com "https://api.slack.com").
   Choose the app that you created in [Step 2: Create a Slack
   application](slack-step-2.md "slack-step-2.md") .
2. Update the **OAuth & Permissions**
   feature as follows:
   1. In the left menu, choose **OAuth &
      Permissions**.
   2. In the **Redirect URLs** section,
      add the OAuth endpoint that Amazon Lex provided in
      the preceding step. Choose **Add**,
      and then choose **Save URLs**.
   3. In the **Bot Token Scopes**
      section, add two permissions with the **Add
      an OAuth Scope** button. Filter the
      list with the following text:
      - `chat:write`
      - `team:read`

3. Update the **Interactivity &
   Shortcuts** feature by updating the
   **Request URL** value to the endpoint
   that Amazon Lex provided in the preceding step. Enter the
   endpoint that you saved in step 3, and then choose
   **Save Changes**.
4. Subscribe to the **Event Subscriptions**
   feature as follows:
   - Enable events by choosing the
     **On** option.
   - Set the **Request URL** value to
     the endpoint that Amazon Lex provided in the
     preceding step.
   - In the **Subscribe to Bot
     Events** section, select
     **Add Bot User Event** and add the
     `message.im` bot event to enable
     direct messaging between the end user and the Slack
     bot.
   - Save the changes.

5. Enable sending messages from the messages tab as
   follows:
   - From the left menu, choose **App
     Home**.
   - In the **Show Tabs** section,
     choose **Allow users to send Slash commands
     and messages from the messages
     tab.**

6. Choose **Manage Distribution** under
   **Settings**. Choose **Add to
   Slack** to install the application. If you
   are authenticated to multiple workspaces, first choose the
   correct workspace in the upper right-hand corner from the
   drop-down list. Next, select **Allow**
   to authorize the bot to respond to messages.

###### Note

If you make any changes to your Slack application
settings later, you must redo this substep.

## Next step

[Step 5: Test the integration between your Lex V2 bot and Slack](slack-step-5.md "slack-step-5.md")
