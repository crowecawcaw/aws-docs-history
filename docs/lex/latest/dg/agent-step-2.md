End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 2: Create an Amazon Lex Bot

Amazon Lex provides an interface between the call center agent and the Amazon Kendra index. It
keeps track of the conversation between the agent and the customer and calls the
`AMAZON.KendraSearchIntent` intent based on the questions the customer
asks. An _intent_ is an action that the user wants to
perform.

Amazon Kendra searches the indexed documents and returns an answer to Amazon Lex that it displays
in the bot. This answer is visible only to the agent.

###### To create an agent assistant bot

1. Sign in to the AWS Management Console and open the Amazon Lex console at
   [https://console.aws.amazon.com/lex/](https://console.aws.amazon.com/lex/ "https://console.aws.amazon.com/lex/").
2. In the navigation pane, choose **Bots**.
3. Choose **Create**.
4. Choose **Custom bot** and configure the bot.
   1. **Bot name** – Enter a name that indicates the
      bot's purpose, such as `AgentAssistBot`.
   2. **Output voice** – Choose
      **None**.
   3. **Session timeout** – Enter
      `5`.
   4. **COPPA** – Choose
      **No**.

5. Choose **Create**. After creating the bot, Amazon Lex displays the
   bot editor tab.

## Next step

[Step 3: Add a Custom and Built-in Intent](agent-step-3.md "agent-step-3.md")
