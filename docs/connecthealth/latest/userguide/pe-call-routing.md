

# How a patient call is handled

When a patient calls, the agentic capabilities for patient access handle the call as one conversation. This topic describes what happens during a call.

## Greeting and intent
<a name="pe-greeting-intent"></a>

At the start of the call, the patient hears a greeting and any required disclosures, such as a recording notice. The agent then asks what the patient needs and determines the patient’s intent from what they say.

## Patient verification
<a name="pe-verification"></a>

Before the agent shares patient information or completes a task, it verifies the patient’s identity. Verification runs ahead of any capability that needs it, and you cannot remove this step. Information assistance doesn’t require verification to answer general questions that don’t involve patient information.

For how to configure the verification factors, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

## Resume a task or mention an upcoming appointment
<a name="pe-memory-offer"></a>

After verification, if memory and personalization is turned on for your domain, the agent can offer to resume one unfinished task or mention an upcoming appointment. For more information, see [Memory and personalization](pe-memory.md).

## Routing to enabled capabilities
<a name="pe-routing"></a>

The agent routes the call based on what the patient needs and the capabilities that you turn on:
+ The agent routes only to capabilities that are turned on.
+ The agent never offers a capability that is turned off.
+ When a patient asks what the agent can do, the agent lists only the capabilities that are turned on.

A patient can switch from one task to another during the call.

## Escalation to a person
<a name="pe-escalation"></a>

The agent transfers the call to a person when it cannot complete the request or when the patient asks for a person. Each transfer includes the reason for the escalation and the context from the call, so the person does not have to start over.

You can set how many times the agent retries, and how many times it redirects an off-topic conversation, before it escalates. For more information, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).