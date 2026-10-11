

# Deployment wiring summary
<a name="connect-deploy-wiring"></a>

To integrate AVX with an Amazon Connect instance:

1.  **Deploy AVX stacks.** Deploy the AVX stacks as described in [Deploy the Guidance](deploy-the-guidance.md). The api stack carries `/escalate` and its grants (`connect:StartChatContact`, `connect:StartOutboundVoiceContact`, and `GetItem` on the CMS vehicles and drivers tables). The Connect instance itself is pre-existing or provisioned separately.

1.  **Create tenant contact flows.** In the Connect console, create the chat contact flow, hours-of-operation blocks and the chat queue for each tenant. Follow the tenant-branding conventions in [Tenant-branded contact flows](connect-tenant-branded-flows.md).

1.  **Run the wiring script.** Run `scripts/wire-connect-to-tenant.py` to write the instance, flow and queue identifiers into the tenant’s config.

1.  **Add the P0 callback (optional).** Claim a number, create the callback flow and caller ID, and write `escalation.callback` as described in [P0 callback](connect-escalation-queues.md#connect-p0-callback).

1.  **Verify end-to-end.** Start a session as a test driver, trigger a P0 or P1 classification, tap **Talk to an agent**, and confirm the chat reaches the tenant’s queue with the initial message and attributes.