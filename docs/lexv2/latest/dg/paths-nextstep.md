# Configure next steps in the

conversation

You can configure a next step at each stage of the conversation to design
conversations. Typically, Amazon Lex V2 automatically configures the default
next steps for each stage of the conversation as per the following order.

Initial Response → Slot Elicitation → Confirmation (if active) → Fulfillment (if active)
→ Closing Response (if active) → End conversation

You can modify the default next steps and design the conversation based on the
expected user experience. The following next steps can be configured at each stage of
the conversation:

**Jump to**

- **Initial response** –
  The conversation is restarted from the beginning of the intent.
  You can choose to skip the initial response while configuring this
  next step
- **Elicit a slot** –
  You can elicit any slot in the intent.
- **Evaluate conditions** – You
  can evaluate conditions and branch conversation at any step of the
  conversation.
- **Invoke dialog code hook** – You
  can invoke business logic at any step.
- **Confirm intent** – The user will be
  prompted to confirm the intent.
- **Fulfill intent** – The fulfillment
  of the intent will begin as a next step.
- **Closing response** – The closing
  response will be returned to the user.
  **Switch to**

- **Intent** – You can transition to
  a different intent and continue the conversation for this intent. You
  can optionally skip the initial response of the intent while making the
  transition.
- **Intent: specific slot** – You can
  directly elicit a specific slot in a different intent if you have already
  captured some slot values in the current intent.
  **Wait for user input** – The bot waits for
  the user to provide inputs for recognizing any new intent. You can configure prompts
  such as "Is there anything else I can help you with?" before setting this next
  step. The bot will be in `ElicitIntent` dialog state.

**End conversation** – The conversation with the
bot is closed.

###### Note

On August 17, 2022, Amazon Lex V2 released a change to the way conversations
are managed with the user. This change gives you more control over
the path that the user takes through the conversation. For more information,
see [Changes to conversation flows in Amazon Lex V2](understanding-new-flows.md "understanding-new-flows.md").
Bots created before August 17, 2022 do not support dialog code hook messages, setting values,
configuring next steps, and adding conditions.
