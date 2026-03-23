# Sample contact flow

Amazon Connect Health provides a pre-built sample contact flow for testing and operationalizing appointment management conversations powered by AI agents. The flow simulates a typical appointment scheduling conversation including patient identity verification. You can use it to validate end-to-end agent behavior before moving to production.

The sample flow is deployed automatically at domain creation, whether Amazon Connect Health creates a new Amazon Connect instance or you use an existing one.

###### Topics

- [Locate the sample flow](#cf-locate-flow "#cf-locate-flow")
- [Provisioned resources](#cf-provisioned-resources "#cf-provisioned-resources")
- [Session attributes](#cf-session-attributes "#cf-session-attributes")
- [Lambda function](#cf-lambda-function "#cf-lambda-function")
- [Amazon Lex bot](#cf-lex-bot "#cf-lex-bot")
- [Customize the contact flow](#cf-customization "#cf-customization")

## Locate the sample flow

To find the sample contact flow:

1. Sign in to your Amazon Connect instance.
2. In the navigation pane, choose **Routing**, then choose **Contact flows**.
3. Search for `connect-health-{DOMAIN_ID}-inbound-flow`, where `{DOMAIN_ID}` is your Amazon Connect Health domain identifier.

You can assign this flow to your preferred phone number if the provisioned number doesn’t fit your workflows.

![Sample Connect Health Contact Flow](images/sample-contact-flow.png)

## Provisioned resources

###### Sample Connect Health contact flow

Amazon Connect Health provisions the following resources as part of the sample contact flow deployment:

| Resource                                                      | Naming pattern                            |
| ------------------------------------------------------------- | ----------------------------------------- |
| Amazon Connect instance (if created by Amazon Connect Health) | `connect-health-{DOMAIN_ID}`              |
| Sample contact flow                                           | `connect-health-{DOMAIN_ID}-inbound-flow` |
| Lambda function                                               | `connect-health-{DOMAIN_ID}-lambda`       |
| Lambda function role                                          | `connect-health-{DOMAIN_ID}-lambda-role`  |
| Amazon Lex bot                                                | `connect-health-{DOMAIN_ID}-bot`          |
| Amazon Lex bot role                                           | `connect-health-{DOMAIN_ID}-lex-bot-role` |

## Session attributes

Session attributes are key-value pairs passed between contact flow blocks and Lambda functions during a voice call. Amazon Connect administrators configure session attributes to carry patient context — such as verification status, appointment intent, and escalation reason — across flow transitions.

The sample contact flow includes the following session attributes for the AI agent identifiers:

- `patient_agent_id` – The identifier for the Patient verification agent.
- `appointment_agent_id` – The identifier for the Appointment management agent.

To view or modify session attributes, open the sample flow in the Amazon Connect flow editor and inspect the **Set contact attributes** block.

## Lambda function

The pre-built Lambda function (`connect-health-{DOMAIN_ID}-lambda`) handles EHR lookups, insurance verification, and session attribute processing during each patient call. The associated IAM execution role (`connect-health-{DOMAIN_ID}-lambda-role`) provides the required permissions. The Lambda function currently includes `"appointmentType": {"id": "1004", "type": "External"}` and can be updated to handle other appointment types you have.

You can extend or replace this function with your own implementation to support custom integrations or business logic.

## Amazon Lex bot

The Amazon Lex bot (`connect-health-{DOMAIN_ID}-bot`) enables natural language understanding and supports patient conversation segments beyond the scope of the Amazon Connect Health agents, such as initial greetings and intent routing.

## Customize the contact flow

Amazon Connect Health provisions a sample Amazon Connect contact flow that demonstrates how Amazon Connect Health agents are invoked within a call routing sequence, but it is intentionally generic. Customize the sample contact flow to align with your operational processes, queue structures, escalation policies, and patient communication standards (including privacy and consent practices) before production deployment.

Customization typically includes the following tasks:

- **Queue assignments and routing profiles** — Reassign contact flow branches to your existing queues and agent routing profiles configured in your Amazon Connect instance.
- **Call flow logic** — Update branching conditions and agent handoff sequences to reflect your department processes.
- **IVR integration** — Integrate the sample flow with existing IVR menus or self-service flows so that Amazon Connect Health agents are reachable within your broader telephony environment.
- **Localization** — Replace default audio with organization-approved recordings or text-to-speech content that reflects your communication standards.

For guidance on building and modifying contact flows, see [Use the flow designer in Amazon Connect to create flows](../../../connect/latest/adminguide/create-contact-flow.md "../../../connect/latest/adminguide/create-contact-flow.md") in the _Amazon Connect Administrator Guide_.
