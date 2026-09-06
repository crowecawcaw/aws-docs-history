# Testing your application

Testing in agentic CX designer lets you validate how your conversational AI
application behaves before it is used in a live customer experience.

Use testing to confirm that your application:

- Starts from the expected flow
- Routes user utterances to the correct flows
- Captures slots and variables correctly
- Applies state modifications as expected
- Uses Data requests, knowledge bases, and tools successfully
  Agentic CX designer includes several testing tools for different stages of review:

|                      |                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| **Application test** | Run an end-to-end test conversation from the application's starting point.                           |
| **Flow test**        | Test a specific flow in isolation from the Canvas.                                                   |
| **Routing tests**    | Validate whether different user utterances invoke the expected flows.                                |
| **Flow logic tests** | Save and replay a sequence of test inputs for repeatable flow testing.                               |
| **Debugger**         | Inspect turn-by-turn events, variables, state, node traversal, and errors during test conversations. |

A successful build is required before workspace testing features can run against
your application package.

A build packages the current version of your application, including attached flows,
routing descriptions, guardrails, slots, languages, and settings. Testing then lets
you validate that packaged version before deploying it.

## Application test

Use an application test when you want to validate the full end-to-end experience.
The conversation starts from the flow assigned to the application's Welcome
default behavior.

###### To run an application test

1. Open **Applications**.
2. Select the application you want to test.
3. Confirm the application has at least one successful build.
4. Select the **Test** tab.
5. Start a new conversation.
6. Type test user messages.
7. Review how the application responds by choosing the Debugger option in the
   upper right to see turn-by-turn events.

Use this test when you want to experience the application the way a user would
from the beginning of a conversation.

## Flow test

Use a flow test when you want to isolate and troubleshoot a specific flow.

Flow testing opens directly from the Canvas and begins from the first turn of the
selected flow instead of the application's Welcome flow. This is useful when you are
building or refining one flow and do not want to start from the full application every
time.

###### To run a flow test

1. Open **Flows** from the workspace menu.
2. Select **Canvas**.
3. Choose the flow you want to test.
4. Select the **Test** icon from the Canvas toolbar.
5. Enter test user responses in the test chat.
6. Refresh the test chat as needed.

The test panel in a flow test includes settings that let you adjust the test session.

Use the settings option (gear icon) when your test requires a specific starting point,
context value, language, or environment.

Common settings include:

|                       |                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| **Starting flow**     | Change which flow the test initializes from.                                                          |
| **Context variables** | Enter values that would normally be set earlier in the conversation or passed from<br>another system. |
| **Language**          | Test language-specific behavior, if available.                                                        |
| **Environment**       | Choose whether Data requests should use Development or Production endpoints,<br>when configured.      |

For example, if a troubleshooting flow expects the user to already be authenticated,
you can set an `isAuthenticated` context variable before running the test.

After changing test settings, select **Restart conversation** so the updated settings apply
to the session.

## Routing tests

Routing tests validate whether user utterances invoke the expected flows.

Routing tests are located in the application's **Test** area under
**Routing tests**. They use the AI descriptions added to flows to evaluate whether a test utterance should
match a specific flow.

Use routing tests when you want to confirm that different ways of asking for help
route correctly.

Examples:

| Utterance                          | Expected flow                 |
| ---------------------------------- | ----------------------------- |
| "I need to change my appointment." | Appointment rescheduling      |
| "Can I talk to someone?"           | Escalation                    |
| "What are your hours?"             | Policy or knowledge base flow |
| "I need help with billing."        | Billing support               |
| "Can I check my order?"            | Order status                  |

###### To create a routing test

1. Open the application.
2. Select the application **Test**.
3. Go to the **Routing tests** section.
4. Under **Routing tests**, select **Create test**.
5. Enter a test name.
6. Add one or more test utterances.
7. Select the expected flow for each utterance.
8. Save the test.

###### To run a routing test

1. Open the saved routing test.
2. Select the test execution option.
3. Run the test.
4. Review the results.
5. Compare the expected flow against the actual matched flow.

A failed routing test means the utterance did not match the expected flow. Review
the flow's AI description and routing coverage, then update and test again.

## Flow logic tests

Flow logic tests let you save and replay a sequence of inputs for repeatable testing.

Use flow logic tests when you want to quickly validate the same path after making
changes. This is helpful for regression testing, repeated QA, and confirming that
known scenarios still work as expected.

###### To create a flow logic test

1. Open a flow from **Flows**.
2. Select the **Test** icon from the Canvas toolbar.
3. Enter the sequence of user inputs you want to test.
4. Save the input sequence as a new flow logic test by selecting the play icon on
   the bottom of the test panel:

   1. Enter a clear test name.
   2. Save the test.

After a flow logic test is saved, you can replay it to confirm the flow still behaves as
expected after future changes. Replay a test by choosing the play button and the
launch play icon on a saved named test.

## Test chat controls

Test chats on an application or in a flow include controls that help you repeat or
reset test sessions.

|              |                                                                         |
| ------------ | ----------------------------------------------------------------------- |
| **Replay**   | Reruns the last conversation using the same inputs.                     |
| **Reset**    | Starts the test session over and clears previous inputs.                |
| **Debugger** | Opens event details for troubleshooting a selected application message. |

Use **Replay** when you want to quickly retest the same path. Use **Reset** when you
need a clean session.

## Debugger

The debugger helps you inspect what happened during a specific turn in a test
conversation.

###### To open debugger details

1. Run a test conversation.
2. Select an application message in the transcript or choose the debugger icon on
   an application test.
3. Review the event list for that turn.
4. Expand events to inspect details.

Use the debugger when the application behaves unexpectedly, such as skipping a
question, repeating a message, routing incorrectly, looping, triggering fallback, or
failing after a Data request.

Many unexpected testing issues are related to state, slots, variables, or agentic or
generative node prompts.

When troubleshooting, start with the last successful turn and inspect the events
that followed.

If needed, simplify the flow path:

1. Start from the first node in the affected turn.
2. Temporarily disconnect later nodes.
3. Connect the first node to a simple Basic node with a success message.
4. Save and test.
5. If the turn succeeds, reconnect one additional node.
6. Test again.
7. Continue until the turn fails.

The last reconnected node is often where the issue begins.

## Testing best practices

- Create a successful build before using application or flow testing.
- Use application tests for end-to-end behavior.
- Use flow tests for focused troubleshooting.
- Use routing tests to validate flow recognition across different utterances.
- Use flow logic tests for repeatable paths and regression testing.
- Set context variables before testing flows that depend on earlier conversation
  state.
- Test happy paths, unclear inputs, missing information, retries, No match paths,
  fallback paths, and escalation.
- Use the debugger to inspect unexpected behavior.
