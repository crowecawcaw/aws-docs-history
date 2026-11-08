

# Assisted NLU mode - Dialog Manager
<a name="generative-llm-dialog-management"></a>

The Dialog Manager is a mode of Assisted NLU that uses a large language model (LLM) to manage the dialog with your user. On each turn, the LLM takes the current conversation state and the NLU resolution as input and decides the next step in the conversation – what to elicit, how to respond, and how to move the conversation forward. This is an alternative to the deterministic dialog management that Amazon Lex V2 performs by default, in which the next step is driven by the configured slot priorities and conversation flow.

Because the LLM decides the next step dynamically from context, Dialog Manager mode lets you build more natural, flexible conversations with less manual flow configuration. It also changes how some existing configuration behaves, most notably bot prompts and intent switching, so review the guidance in this topic before you enable it.

The following are common reasons to use the Dialog Manager:
+ Handle conversations that do not follow a fixed, pre-defined path, including clarifications and follow-up questions.
+ Reduce the amount of slot-priority and conversation-flow configuration you have to maintain by hand.
+ Let the model generate responses and elicitation dynamically from the conversation context instead of relying only on statically configured prompts.

The Dialog Manager also handles the following conversation patterns without additional configuration:

Greetings  
When a user opens with a greeting such as **Hi there** without making a request, the bot replies and asks how it can help, instead of routing the input to the `FallbackIntent`.

Slot carry-over during an intent switch  
When the user switches to a different intent before the current intent is complete, slot values that the user already provided carry over to the new intent if it has a slot with the same name, and the bot doesn't ask for them again. For example, while changing their seat on flight 123, the user can ask **Is that flight on time?** and the flight number carries over. A value that the user provides in the current turn takes precedence over a carried-over value. Values don't carry over when the user indicates they mean a different item, such as **Book a different flight**, or when the earlier intent has already been fulfilled or closed.

Slot value correction  
When the user corrects a value that they already provided for the current intent, such as **Actually, make it Tuesday**, the bot replaces the value and continues the conversation. If you use a Lambda function to validate slot values, it runs again for the corrected value. If the user corrects a value while the bot is confirming the intent, the bot updates the value and resumes collecting slots.

Multiple slot values on any turn  
The user can provide several slot values in one utterance, including values for slots that the bot hasn't asked for yet, on any turn of the conversation – not only the first. For example, when the bot asks for the check-in date, the user can reply **Next Friday, for three nights, two guests** and the bot captures all three values.

**Important**  
Dialog Manager mode is available with Connect Customer pricing. You can try Dialog Manager mode in the draft version of your bot (TSTALIAS) at no additional cost. To use it with a published bot version and alias for production traffic, your account must have an Amazon Connect instance onboarded to Connect Customer pricing (Unlimited AI). For more information, see [Connect Customer pricing](https://aws.amazon.com/connect/pricing/).

**Important**  
Enable this feature in a draft version of the bot and test it before using it in a production alias.

## How Dialog Manager differs from Primary and Fallback mode
<a name="llm-dm-comparison"></a>

In Primary and Fallback mode, the LLM only helps classify the intent and fill slot values. Amazon Lex V2 still decides the next step in the conversation using the configured slot priorities and conversation flow. In Dialog Manager mode, the LLM also decides the next step. The following table summarizes the differences.


| Behavior | Primary mode | Fallback mode | Dialog Manager mode | 
| --- | --- | --- | --- | 
| When the LLM is invoked | On every turn. | Only when traditional NLU confidence is below the threshold, the input would route to the `FallbackIntent`, or a slot value is not captured. | On every turn. | 
| What the LLM decides | Intent and slot values. | Intent and slot values, for inputs that traditional NLU can't resolve. | Intent and slot values (intent classification, slot labeling and slot resolution), plus the next step in the conversation: what to elicit and how to respond. | 
| Next conversation step | Driven by configured slot priorities and conversation flow. | Driven by configured slot priorities and conversation flow. | Decided dynamically by the LLM from the conversation context. | 
| Bot prompts | Played as configured. | Played as configured. | Played verbatim when configured, which suppresses dynamic dialog management for that turn. When no prompt is configured, the LLM generates the response. | 
| Intent switching | Standard Amazon Lex V2 behavior. | Standard Amazon Lex V2 behavior. | Sensitive to small changes in user input. The LLM re-evaluates the intent on every turn, so the bot can switch intents mid-conversation on small changes in user input. Keep intents distinct to avoid unintended switches | 
| Pricing | Included with Amazon Lex V2 pricing. | Included with Amazon Lex V2 pricing. | Available with Connect Customer pricing. | 

## Best practices for Dialog Manager mode
<a name="llm-dm-best-practices"></a>

Dialog Manager changes how bot prompts and intent switching behave. Follow these practices to get the most out of the feature.
+ **Leave bot prompts out** – A configured bot prompt is always played verbatim. The LLM doesn't override it or generate its own response for that turn, and the prompt continues to be played until you remove it. To take full advantage of Dialog Manager, leave bot prompts out. Configure a prompt only when you need exact wording for a specific turn and are willing to give up dynamic dialog management for that turn.
+ **Document your top resolutions** – Identify the intents and conversation paths that handle the most traffic, and record which of them have bot prompts configured, including the exact wording and the turn each prompt applies to. On those paths, the configured prompts – not the LLM – determine what your customers hear. To hand a turn back to the LLM, remove its prompt.
+ **Keep intents clear and non-overlapping** – Intent switching is highly sensitive in this mode. The bot might switch to a different intent mid-conversation in response to small changes in user input, which can interrupt an in-progress flow. Keep intent names, descriptions, and sample utterances distinct so the model has less reason to switch between similar intents.
+ **Test with realistic conversations** – Test conversations that include clarifications, corrections, and follow-up questions. Verify that the bot stays on the current intent when the user isn't changing topic, and that your highest-traffic paths complete without unexpected intent switches before you promote to a production alias.