End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# Step 3: Add a Custom and Built-in Intent

An _intent_ represents an action that the call center
agent wants the bot to perform. In this case, the agent wants the bot to suggest
responses and helpful resources based on the agent's conversation with the customer.

Amazon Lex has two types of intents: custom intents and built-in intents.
`AMAZON.KendraSearchIntent` is a built-in intent. The bot uses the
`AMAZON.KendraSearchIntent` intent to query the index and display the
responses suggested by Amazon Kendra.

The bot in this example doesn't need a custom intent. However, to build the bot, you
must create at least one custom intent with at least one sample utterance. This intent
is required only to build your agent assistant bot. It doesn’t perform any other
function. The utterance for the intent must not answer any of the questions that the
customer might ask. This ensures that the `AMAZON.KendraSearchIntent` is
called to answer customer queries. For more information, see [AMAZON.KendraSearchIntent](built-in-intent-kendra-search.md "built-in-intent-kendra-search.md").

###### To create the required custom intent

1. On the **Getting started with your bot** page, choose
   **Create intent**.
2. For **Add intent**, choose **Create
   intent**.
3. In the **Create intent** dialog box, enter a descriptive name
   for the intent, such as `RequiredIntent`.
4. For **Sample utterances**, enter a descriptive utterance,
   such as `Required utterance`.
5. Choose **Save intent**.

###### To add the AMAZON.KendraSearchIntent intent and response message

1. In the navigation pane, choose the plus sign (+) next to
   **Intents**.
2. Choose **Search existing intents**.
3. In the **Search intents** box, enter
   `AMAZON.KendraSearchIntent`, then choose it from the
   list.
4. Give the intent a descriptive name, such as
   `AgentAssistSearchIntent`, then choose
   **Add**.
5. In the intent editor, choose **Amazon Kendra query** to open the
   query options.
6. Choose the index that you want the intent to search,
7. In the **Response** section, add the following three messages
   to a message group.

```
I found an answer for the customer query: ((x-amz-lex:kendra-search-response-question_answer-question-1)) and the answer is ((x-amz-lex:kendra-search-response-question_answer-answer-1)).
I found an excerpt from a helpful document: ((x-amz-lex:kendra-search-response-document-1)).
I think this answer will help the customer: ((x-amz-lex:kendra-search-response-answer-1)).

```

8. Choose **Save intent**.
9. Choose **Build** to build the bot.

## Next step

[Step 4: Set up Amazon Cognito](agent-step-4.md "agent-step-4.md")
