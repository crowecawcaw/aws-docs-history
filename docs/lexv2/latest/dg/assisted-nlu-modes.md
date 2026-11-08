

# Assisted NLU mode - Primary and Fallback
<a name="assisted-nlu-modes"></a>

Assisted NLU runs in one of the following modes. Choose the mode that matches how well your bot already performs and how much control you want the LLM to have over each turn.

Primary mode  
Amazon Lex V2 uses the LLM as the primary means of processing every user input to determine the user's intent and to fill slot values. Use Primary mode when you are building a new bot or when you have limited training data (fewer than 20 sample utterances per intent). For example, a healthcare bot handling appointment scheduling can classify inputs such as **I need to see someone about my knee** or **Book me with a cardiologist next week** without extensive utterance engineering.

Fallback mode  
Amazon Lex V2 uses traditional NLU first and invokes the LLM only when the confidence score is lower than the configured threshold or the input would otherwise route to the `FallbackIntent`. In this mode the LLM also fills slot values only when traditional NLU does not capture a value. Use Fallback mode with an existing bot that already performs well, so the LLM intervenes only on edge cases. For example, use it for a banking bot with high accuracy that occasionally fails on variations like **What's my balance looking like?** instead of **Check balance**.

Dialog Manager mode  
The LLM manages the dialog itself, deciding the next step in the conversation on each turn instead of following the deterministic slot priorities and conversation flow that Amazon Lex V2 uses by default. Use Dialog Manager mode when you want more natural, flexible conversations, such as dialogs where users correct values, switch topics, or provide several values at once. This mode changes how some existing configuration behaves, so review the guidance before you enable it. For more information, see [Assisted NLU mode - Dialog Manager](generative-llm-dialog-management.md).

**Choosing between Primary and Fallback mode**

Consider the following when you choose between Primary and Fallback mode:
+ Don't switch a well-performing bot to Primary mode without A/B testing. You might introduce latency without a meaningful accuracy gain.
+ Don't assume one mode works for every use case. Your data distribution and your users' language patterns determine the right mode.
+ Use CloudWatch Logs Insights on your conversation logs to track the percentage of utterances where `fulfilledByAssistedNlu` is `true`. If more than 30 percent of utterances invoke the LLM in Fallback mode, consider switching to Primary mode for consistency. For more information, see [Monitoring assisted NLU in production](#assisted-nlu-monitoring).

## Enabling assisted NLU
<a name="enable-assisted-nlu"></a>

------
#### [ Console ]

**Using assisted NLU with your Amazon Lex V2 bot**

1. Sign in to the AWS Management Console and open the Amazon Lex V2 console at [https://console.aws.amazon.com/lexv2/home](https://console.aws.amazon.com/lexv2/home).

1. On the **Bots** page, select the bot you want to use with assisted NLU.

1. On the **Bot Locale** page, choose **Configure** under the **Assisted NLU** section.

1. Under the **Runtime generative AI features** section, use the toggle beside Assisted NLU to turn on the feature.

1. Select **Primary** or **Fallback** mode.

1. Choose **Save**. On the **Bot Locale** page, verify that Assisted NLU is turned on in the **Assisted NLU** section.

1. Build the bot to apply the changes. The build might take a few minutes. After the build completes, use the test panel in the console or run a test set to see the improvements from Assisted NLU.

------

For programmatic configuration, see the [NluImprovementSpecification](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_NluImprovementSpecification.html) API reference.

**Note**  
When you enable this feature, your data might be processed across AWS Regions. For more information, see [Cross-Region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) in the *Amazon Bedrock User Guide*.

**Important**  
Enable this feature in a draft version of the bot. Test it before using it in a production alias.

## Writing effective intent and slot descriptions
<a name="assisted-nlu-descriptions"></a>

With assisted NLU, intent and slot descriptions are prompts to the LLM, not documentation for your team. They are the primary signal the model uses to classify intents and extract slot values, so their quality directly determines accuracy. The following best practices help you get the most out of the feature.
+ **Make intent names self-explanatory** – Use names that immediately convey the action or purpose of the intent. For example, name an intent for booking flights `BookFlight`.
+ **Keep names clean and simple** – Avoid prefixes, suffixes, or unnecessary words in your intent and slot names. Extra elements like `Dev` or `Test` can confuse the LLM and make the purpose less clear.
+ **Write intent descriptions as prompts** – Start each description with **Intent to** followed by a clear action verb, the object or entity, and any context that resolves edge cases — for example, **Intent to book a hotel room for overnight accommodation**. Derive descriptions from your existing sample utterances, keep one action per intent, and avoid overlapping language across intents. Don't include specific slot values in the description, because doing so overconstrains matching.
+ **Write specific slot descriptions** – Describe what the slot captures, add contextual constraints, and give valid-value guidance — for example, **Check-in date for the hotel reservation, not the checkout or booking date**. Specific descriptions let the LLM distinguish between similar slots (for example, number of nights versus number of guests) and resolve natural language to the right value without a dedicated custom slot type.

When multiple intents could match a user's input, assisted NLU can present disambiguation options to clarify the user's goal. For more information, see [Resolve ambiguous user inputs with Intent Disambiguation](generative-intent-disambiguation.md).

## Testing your assisted NLU configuration
<a name="assisted-nlu-testing"></a>

After you write your intent and slot descriptions, validate your configuration with the Amazon Lex V2 Test Workbench to measure how well assisted NLU handles real-world utterance variations. When you configure the test run, select the bot and alias where assisted NLU is enabled — the test exercises assisted NLU only if the alias points to a version with Primary or Fallback mode configured. For more information, see [Evaluating Lex V2 bot performance with the Test Workbench](test-workbench.md).

Focus your testing where assisted NLU adds the most value:
+ Edge cases that deviate from standard phrasing, such as typos (**i wanna book an hotell**), colloquial expressions (**hook me up with a room downtown**), ambiguous requests (**I need transportation**), and incomplete utterances (**booking for next week**).
+ Slot variations, such as date formats (**next Tuesday**, **the 15th**) and location aliases (**NYC**, **New York City**). For custom slots, verify that user phrasing maps to your defined values — for example, that **largest room** resolves to `Suite`.

Use pass rates to prioritize where to focus. Intents in the 0–30 percent range are high priority (rewrite the description and check for overlap with confused intents), 30–70 percent are medium priority (analyze failed utterances for patterns), and 70–100 percent need only minor tuning.

**Note**  
Assisted NLU uses the LLM strictly as a classification and extraction engine constrained by your bot definition. The LLM can only select an intent and extract slot values that are defined in your bot — it can't invent new intents, trigger actions outside your bot definition, or return raw LLM-generated text to your users. This architecture limits the prompt-injection attack surface, but you should still verify that adversarial inputs route predictably to the `FallbackIntent`.

## Monitoring assisted NLU in production
<a name="assisted-nlu-monitoring"></a>

Enable conversation logs on your production alias to track assisted NLU performance with real traffic. For more information, see [Configuring conversation logs for your Lex V2 bot](conversation-logs-configure.md). Monitor the following fields:
+ `fulfilledByAssistedNlu` – A Boolean flag indicating when the LLM handled classification or slot resolution.
+ `nluConfidence` – The confidence score for the selected intent.
+ `missedUtterance` – A Boolean indicating that the `FallbackIntent` was classified.

To compare Primary and Fallback mode, create a separate bot version for each mode, point a different alias to each, and compare their metrics in CloudWatch.

## Rolling out assisted NLU
<a name="assisted-nlu-rollout"></a>

If you are building a new bot, start with Primary mode. Begin with 10–15 sample utterances per intent and invest your effort in high-quality intent and slot descriptions. If you have an existing bot that already performs well, start with Fallback mode so the LLM intervenes only when traditional NLU is uncertain, and run A/B tests before considering a switch to Primary mode. Maintain a previous bot version so you can roll back if needed. Before you promote to production, confirm that you have documented baseline metrics, tested edge cases in development, enabled conversation logs, and defined a rollback procedure.