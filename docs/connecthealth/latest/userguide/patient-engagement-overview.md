

# Patient engagement

Amazon Connect Health provides the agentic capabilities for patient access to handle routine patient calls. Patients call one phone number and have one conversation. The agent greets the caller, verifies the patient when a task needs it, and then helps with one or more tasks in the same call. Patients speak naturally instead of choosing options from a phone menu.

A single orchestrator coordinates the capabilities in one conversation. It identifies what the patient needs, moves between tasks, applies clinical guardrails, and escalates to a person with context when needed. A patient can switch from one task to another during the call. Patients can ask general questions during a task without losing their place. The agent works with your Epic electronic health record (EHR) in real time.

## Available capabilities
<a name="pe-overview-available-capabilities"></a>

You choose which of the following capabilities to turn on for each agent:
+  **Patient verification** – Confirms the patient’s identity once against your EHR before the agent shares information or completes a task. A caller can also verify on behalf of a patient, such as a caregiver. Capabilities that handle patient data require verification first. For more information, see [Patient verification](patient-verification.md).
+  **Appointment management** – Schedules, reschedules, cancels, and looks up visits using real-time EHR availability. It can also offer open scheduling and an optional insurance eligibility check with copay information. For more information, see [Appointment management](appointment-management.md).
+  **Prescription management** – Handles refill requests and refill status for existing prescriptions that your health system pharmacy fills. Clinical medication questions transfer to a person. For more information, see [Prescription management](prescription-management.md).
+  **MyChart password reset** – Sends a MyChart password reset link to a verified patient by email or text message. For more information, see [MyChart password reset](password-reset.md).
+  **Information assistance** – Answers general, non-clinical questions, such as hours, directions, and parking, from the knowledge base that you provide. For more information, see [Information assistance](information-assistance.md).

## Memory and personalization
<a name="pe-overview-memory-and-personalization"></a>

When memory and personalization is turned on for your domain, the capabilities can resume an unfinished task, reuse a patient’s earlier choices, and mention an upcoming appointment on a later call. For more information, see [Memory and personalization](pe-memory.md).

## How a call is handled
<a name="pe-overview-how-a-call-is-handled"></a>

For a description of the greeting, the verification step, routing between capabilities, and escalation to a person, see [How a patient call is handled](pe-call-routing.md).

## Set up agents
<a name="pe-overview-set-up-agents"></a>

To turn capabilities on or off and configure them, you use the patient engagement web app. For more information, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

## Channel, language, and EHR support
<a name="pe-overview-channel-language-and-ehr-support"></a>

The agentic capabilities for patient access support the following:
+  **Channel** – Voice only. Patients reach the agent by phone through Amazon Connect Customer. There is no patient chat or text message channel. The agent uses text messages only to send a password reset link.
+  **Language** – English only.
+  **EHR** – Epic only. For other EHRs, contact your AWS account team.

## Consent and patient notification
<a name="pe-overview-consent"></a>

The agentic capabilities for patient access use AI to talk with patients by phone. Calls can include protected health information (PHI), and your Amazon Connect Customer instance can record and transcribe them. You and your downstream integrators are responsible for complying with all applicable consent, recording, and privacy laws. This includes any notice or consent that is required before a patient talks with an AI agent or before a call is recorded. AWS does not collect consent from patients on your behalf.

At the start of each call, the agent tells the patient that they are talking with AI and that the call may be recorded in its default configuration:

"Hi, I’m an AI that answers calls for your health care provider. This call may be monitored and recorded by your health care provider and its service providers to improve their services."

When memory and personalization is turned on, the agent can use the choices a patient made and the tasks a patient did not finish on earlier calls. Your health system controls whether memory and personalization is turned on for its domain. Patients cannot turn off memory and personalization for themselves.