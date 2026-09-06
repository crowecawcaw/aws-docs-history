# Guardrails

Guardrails help evaluate and control conversational behavior in agentic CX designer applications.

They act as a safety, compliance, and brand-control layer for conversations by
checking user inputs and application outputs against rules you define. Guardrails
can help prevent unsafe requests, off-brand responses, sensitive data exposure,
prompt injection attempts, hallucinated claims, or other behavior that does not align
with your business requirements.

Once created in your workspace, guardrails can be attached to one or more applications.

To access guardrails, select **Guardrails** from your workspace menu, then choose
**Guardrails**.

A guardrail is a reusable resource that evaluates conversation messages at runtime.

Guardrails can check:

- _User inputs_ before they are processed by the application
- _Application outputs_ before they are returned to the user
  This makes guardrails useful for controlling both sides of the conversation. For
  example, an input guardrail might detect a prompt injection attempt from a user,
  while an output guardrail might prevent the application from returning a response
  that includes unsupported claims or restricted language.

Guardrails run independently from flow logic and prompts. They provide an
additional layer of control so safety, compliance, and brand expectations are not
handled only inside individual flows or LLM instructions.

## Input and output guardrails

Guardrails can be configured as either Input or Output guardrails.

|                       |                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Input guardrails**  | Messages from the user before they are processed by the application. Use cases include detecting prompt injection attempts, masking or flagging sensitive information, blocking unsupported or risky requests.                               |
| **Output guardrails** | Messages from the application before they are returned to the user. Use cases include preventing hallucinated claims, enforcing brand tone, meeting compliance requirements, masking sensitive information, or redirecting unsafe responses. |

## Detection methods

Each guardrail rule uses a detection method to determine whether a message violates the rule.

|               |                                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Regex**     | Matches precise text patterns. Best for structured or predictable cases, such as account numbers, email addresses, or other formatted values.      |
| **Keyword**   | Triggers when specific words or phrases appear. Best for simple inclusion checks, such as blocked terms, competitor names, or restricted phrases.  |
| **LLM Judge** | Uses an LLM to evaluate whether the message violates the rule based on instructions you provide. Best for nuanced, contextual, or semantic checks. |

Use an LLM Judge when a rule requires interpretation rather than an exact match.

Examples:

- The user is attempting to override instructions or manipulate the application.
- The application output makes a claim that is not supported by available information.
- The response does not follow brand tone or compliance requirements.
- The message includes sensitive information that should not be disclosed.
- The user request asks for private account details that should not be shared.

When using an LLM Judge, you may select the model used in the guardrail's setting.

Guardrails can include multiple rules, so clear naming is important.

Use descriptive rule names that make the purpose easy to understand at a glance.

Clear rule names make guardrails easier to review, test, troubleshoot, and maintain over time.

## Enforcement actions

When a guardrail rule is triggered, choose how the application should respond.

Choose the enforcement action based on how serious the violation is and what the
user experience should be.

|              |                                                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------------------------------------- |
| **Override** | Replaces the original message with a safe alternative. May use static messaging or use an LLM to generate a new response. |
| **Mask**     | Allows the message through but redacts sensitive or restricted content.                                                   |
| **Redirect** | Routes the conversation to a specific flow, such as escalation, recovery, or a compliance-safe path.                      |
| **Flag**     | Logs the violation but allows the message to pass unchanged.                                                              |

For example, a prompt injection attempt may require an override or redirect, while a
lower-risk brand style issue may only need to be flagged for review.

In addition to detection and enforcement, a guardrail rule can trigger optional actions when it is activated.

Optional actions include:

|                         |                                                                                       |
| ----------------------- | ------------------------------------------------------------------------------------- |
| **Analytics tags**      | Apply one or more analytics tags so triggered guardrails can be tracked in reporting. |
| **State modifications** | Set, clear, or update variables when a guardrail rule is triggered.                   |

Use analytics tags when you want to monitor how often a specific rule is triggered.
Use state modifications when the conversation needs to remember that a safety,
compliance, or policy event occurred.

## Testing guardrails

Test guardrails before attaching them to a live application.

Testing helps confirm whether rules detect the correct messages and apply the
expected enforcement behavior.

###### To test a guardrail

1. Open **Guardrails**.
2. Select **Guardrails**.
3. Choose an existing guardrail.
4. Select the **Test** option.
5. Enter a sample message.
6. Run the test.
7. Review the result for each rule.

Test results help show whether each rule was clear or triggered.

|               |                                              |
| ------------- | -------------------------------------------- |
| **Clear**     | The message did not violate that rule.       |
| **Triggered** | The rule was triggered for the test message. |

Use a range of sample messages when testing. Include messages that should
trigger the rule and messages that should not trigger it.

## Guardrail activity logs

Each guardrail includes activity or log details that help you review when rules were triggered.

Use guardrail logs to:

- View when a rule was triggered
- Review the original message
- Inspect the final enforced output
- Confirm which enforcement action occurred
- Monitor patterns of misuse, sensitive disclosures, or policy violations
- Decide whether a rule needs tuning

Guardrail activity is useful after deployment because it helps confirm that safety
and compliance controls are working as expected in real conversations.

When exploring tracked events in the conversation transcripts or using the test
chat, the debugger also lists all guardrail events.

## Attaching guardrails to an application

After a guardrail is created, attach it to an application so it can run during conversations.

###### To use a guardrail

1. Open **Applications**.
2. Select the application.
3. Open the application configuration area.
4. Add one or more guardrails from the workspace.
5. Save the application.
6. Create a new build.
7. Deploy the build to the appropriate environment.

Once assigned and deployed, guardrails run automatically during conversations
where they apply. Input guardrails check incoming user messages, while output
guardrails check application responses before they are returned to the user.

## Evaluation order

When multiple guardrails and rules are attached to an application, agentic CX
designer evaluates them in a predictable order.

1. Guardrails attached to the application run in the order they appear in the application's guardrail list.
2. Rules within each guardrail run from top to bottom.
3. All triggered rules are evaluated and logged.
4. Only one corrective action is applied.
5. The corrective action comes from the first triggered rule in the evaluation order.

This means order matters. Place the most important or restrictive rules higher
in the list so they take priority when multiple rules are triggered during the same turn.

## Deactivating a rule

You can deactivate a guardrail rule without deleting it.

This is useful for testing, temporary policy changes, troubleshooting, or preserving
a rule for later use.

###### To deactivate a rule

1. Open **Guardrails**.
2. Select **Guardrails**.
3. Choose the guardrail.
4. Locate the rule.
5. Open the rule menu (three-dot menu).
6. Select **Deactivate**.

Deactivated rules remain saved in the guardrail, but they are not evaluated at
runtime until they are reactivated.
