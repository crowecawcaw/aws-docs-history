

# Contact Center Integration
<a name="contact-center-integration"></a>

Amazon Connect is the primary contact center channel for AVX, providing voice and chat surfaces, intelligent routing, and the tier-2 human escalation path that the AVX agentic layer triggers when a conversation exceeds its autonomous resolution scope.

AVX integrates with Amazon Connect for voice and chat channels and for the human handoff. The safety instruction always comes first. A handoff opens when the driver taps **Talk to an agent** or **Request roadside**, or asks for a person: AVX starts a Connect chat on the tenant’s chat queue with the triage result and a conversation summary in the contact attributes.

![Contact center escalation architecture in five zones: the driver talks to AVX in the app by voice or text, and on a P0 or P1 classification the app shows a card with Talk to an agent and, on P0, Request roadside, whose tap sends only an intent; the supervisor on Amazon Bedrock AgentCore, with Amazon Nova 2 Sonic for voice, runs the deterministic triage classifier and on P0 gives the stop-driving instruction first, word for word; the runtime calls POST /escalate on Amazon API Gateway with a Cognito authorizer, and the api-escalate AWS Lambda function reads the tenant’s Connect settings (a chat flow and queue, and a callback flow and queue) and, for a verified P0 only, writes a roadside request to the rsa-dispatch table; in Amazon Connect, StartChatContact puts the chat on the tenant’s chat queue, with P0 on a high-priority branch, and for a verified P0 StartOutboundVoiceContact places a callback through the callback queue; the driver joins the chat through the Connect Participant Service, the tier-2 agent sees the summary and triage in the contact attributes, and the callback rings the assigned driver’s phone.](https://docs.aws.amazon.com/guidance/latest/agentic-vehicle-experience-on-aws/images/avx-escalation-architecture.png)
