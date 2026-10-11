

# Handoff sequence
<a name="connect-warm-transfer"></a>

1.  **Classify and instruct.** The triage classifier returns P0 or P1. On P0 the driver hears and sees the safety instruction first.

1.  **Recommend.** The supervisor says it recommends speaking with an agent and does not describe a handoff as done. The app shows the card.

1.  **Confirm.** The driver taps **Talk to an agent** or **Request roadside**, or the tenant’s `autoOpenHumanChatOnP0` opens the chat on P0. **Talk to an agent** never orders a truck.

1.  **Escalate.** The runtime calls `/escalate`, which reads the tenant’s Connect settings, runs the P0 checks for any side effect, places the callback if configured, writes the roadside request if confirmed, and calls `StartChatContact`.

1.  **Join.** The app joins the chat with the returned participant token. The tier-2 agent answers with the initial message and attributes in view. Once a chat is open the card hides the roadside button and tells the driver to ask the agent, so a second request does not open a second contact.

If `StartChatContact` fails, `/escalate` returns an error that says whether the callback was placed, and the voice runtime tells the driver a support agent is calling their phone.