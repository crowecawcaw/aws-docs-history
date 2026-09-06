

# Testing your application
<a name="acxd-testing"></a>

Testing in agentic CX designer lets you validate how your conversational AI application behaves before it is used in a live customer experience.

Use testing to confirm that your application:
+ Starts from the expected flow
+ Routes user utterances to the correct flows
+ Captures slots and variables correctly
+ Applies state modifications as expected
+ Uses Data requests, knowledge bases, and tools successfully

Agentic CX designer includes several testing tools for different stages of review:


|  |  | 
| --- |--- |
| **Application test** | Run an end-to-end test conversation from the application's starting point. | 
| **Flow test** | Test a specific flow in isolation from the Canvas. | 
| **Routing tests** | Validate whether different user utterances invoke the expected flows. | 
| **Flow logic tests** | Save and replay a sequence of test inputs for repeatable flow testing. | 
| **Debugger** | Inspect turn-by-turn events, variables, state, node traversal, and errors during test conversations. | 

A successful build is required before workspace testing features can run against your application package.

A build packages the current version of your application, including attached flows, routing descriptions, guardrails, slots, languages, and settings. Testing then lets you validate that packaged version before deploying it.

## Application test
<a name="acxd-testing-application"></a>

Use an application test when you want to validate the full end-to-end experience. The conversation starts from the flow assigned to the application's Welcome default behavior.

**To run an application test**

1. Open **Applications**.

1. Select the application you want to test.

1. Confirm the application has at least one successful build.

1. Select the **Test** tab.

1. Start a new conversation.

1. Type test user messages.

1. Review how the application responds by choosing the Debugger option in the upper right to see turn-by-turn events.

Use this test when you want to experience the application the way a user would from the beginning of a conversation.

## Flow test
<a name="acxd-testing-flow"></a>

Use a flow test when you want to isolate and troubleshoot a specific flow.

Flow testing opens directly from the Canvas and begins from the first turn of the selected flow instead of the application's Welcome flow. This is useful when you are building or refining one flow and do not want to start from the full application every time.

**To run a flow test**

1. Open **Flows** from the workspace menu.

1. Select **Canvas**.

1. Choose the flow you want to test.

1. Select the **Test** icon from the Canvas toolbar.

1. Enter test user responses in the test chat.

1. Refresh the test chat as needed.

The test panel in a flow test includes settings that let you adjust the test session.

Use the settings option (gear icon) when your test requires a specific starting point, context value, language, or environment.

Common settings include:


|  |  | 
| --- |--- |
| **Starting flow** | Change which flow the test initializes from. | 
| **Context variables** | Enter values that would normally be set earlier in the conversation or passed from another system. | 
| **Language** | Test language-specific behavior, if available. | 
| **Environment** | Choose whether Data requests should use Development or Production endpoints, when configured. | 

For example, if a troubleshooting flow expects the user to already be authenticated, you can set an `isAuthenticated` context variable before running the test.

After changing test settings, select **Restart conversation** so the updated settings apply to the session.

## Routing tests
<a name="acxd-testing-routing"></a>

Routing tests validate whether user utterances invoke the expected flows.

Routing tests are located in the application's **Test** area under **Routing tests**. They use the AI descriptions added to flows to evaluate whether a test utterance should match a specific flow.

Use routing tests when you want to confirm that different ways of asking for help route correctly.

Examples:


| Utterance | Expected flow | 
| --- | --- | 
| "I need to change my appointment." | Appointment rescheduling | 
| "Can I talk to someone?" | Escalation | 
| "What are your hours?" | Policy or knowledge base flow | 
| "I need help with billing." | Billing support | 
| "Can I check my order?" | Order status | 

**To create a routing test**

1. Open the application.

1. Select the application **Test**.

1. Go to the **Routing tests** section.

1. Under **Routing tests**, select **Create test**.

1. Enter a test name.

1. Add one or more test utterances.

1. Select the expected flow for each utterance.

1. Save the test.

**To run a routing test**

1. Open the saved routing test.

1. Select the test execution option.

1. Run the test.

1. Review the results.

1. Compare the expected flow against the actual matched flow.

A failed routing test means the utterance did not match the expected flow. Review the flow's AI description and routing coverage, then update and test again.

## Flow logic tests
<a name="acxd-testing-flow-logic"></a>

Flow logic tests let you save and replay a sequence of inputs for repeatable testing.

Use flow logic tests when you want to quickly validate the same path after making changes. This is helpful for regression testing, repeated QA, and confirming that known scenarios still work as expected.

**To create a flow logic test**

1. Open a flow from **Flows**.

1. Select the **Test** icon from the Canvas toolbar.

1. Enter the sequence of user inputs you want to test.

1. Save the input sequence as a new flow logic test by selecting the play icon on the bottom of the test panel:

   1. Enter a clear test name.

   1. Save the test.

After a flow logic test is saved, you can replay it to confirm the flow still behaves as expected after future changes. Replay a test by choosing the play button and the launch play icon on a saved named test.

## Test chat controls
<a name="acxd-testing-controls"></a>

Test chats on an application or in a flow include controls that help you repeat or reset test sessions.


|  |  | 
| --- |--- |
| **Replay** | Reruns the last conversation using the same inputs. | 
| **Reset** | Starts the test session over and clears previous inputs. | 
| **Debugger** | Opens event details for troubleshooting a selected application message. | 

Use **Replay** when you want to quickly retest the same path. Use **Reset** when you need a clean session.

## Debugger
<a name="acxd-testing-debugger"></a>

The debugger helps you inspect what happened during a specific turn in a test conversation.

**To open debugger details**

1. Run a test conversation.

1. Select an application message in the transcript or choose the debugger icon on an application test.

1. Review the event list for that turn.

1. Expand events to inspect details.

Use the debugger when the application behaves unexpectedly, such as skipping a question, repeating a message, routing incorrectly, looping, triggering fallback, or failing after a Data request.

Many unexpected testing issues are related to state, slots, variables, or agentic or generative node prompts.

When troubleshooting, start with the last successful turn and inspect the events that followed.

If needed, simplify the flow path:

1. Start from the first node in the affected turn.

1. Temporarily disconnect later nodes.

1. Connect the first node to a simple Basic node with a success message.

1. Save and test.

1. If the turn succeeds, reconnect one additional node.

1. Test again.

1. Continue until the turn fails.

The last reconnected node is often where the issue begins.

## Testing best practices
<a name="acxd-testing-best-practices"></a>
+ Create a successful build before using application or flow testing.
+ Use application tests for end-to-end behavior.
+ Use flow tests for focused troubleshooting.
+ Use routing tests to validate flow recognition across different utterances.
+ Use flow logic tests for repeatable paths and regression testing.
+ Set context variables before testing flows that depend on earlier conversation state.
+ Test happy paths, unclear inputs, missing information, retries, No match paths, fallback paths, and escalation.
+ Use the debugger to inspect unexpected behavior.