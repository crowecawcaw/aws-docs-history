

# Appointment management

Appointment management handles appointment scheduling, rescheduling, cancellation, and lookup through natural conversation, using real-time provider availability from your EHR.

Appointment management completes scheduling tasks in one conversation, from finding available slots for established patients across providers and locations to booking, rescheduling, and canceling appointments. The booking flow can include optional real-time insurance eligibility verification and copay information from your own real-time eligibility (RTE) service. When a request needs special handling, appointment management escalates to staff and passes a summary that includes the appointment details, patient preferences, and verification status.

## Scope and prerequisites
<a name="am-scope"></a>

Appointment management works within the following scope:
+  **Epic EHR only** – It integrates with the Epic EHR for appointment and clinical data.
+  **Established patients only** – It serves patients who already have a record in your EHR. It does not register new patients.
+  **Existing appointment types only** – It books, reschedules, and cancels appointment types that already exist in your EHR. It does not create new appointment types.

## Capabilities
<a name="am-capabilities"></a>

Appointment management provides the following:
+  **New appointment scheduling with real-time provider availability lookup** – Finds available slots for established patients and books appointments within a single conversation.
+  **Appointment rescheduling and cancellation** – Retrieves the current appointment, presents available alternatives for rescheduling, or processes cancellations and provides confirmation to the patient.
+  **Appointment lookup and status confirmation** – Retrieves and confirms upcoming appointment details for the patient.
+  **Open scheduling** – Lets patients schedule by visit type, without naming a provider. It maps the visit type to eligible providers and departments using an open scheduling configuration file that you add to your knowledge base. A decision tree guides the questions that the agent asks to determine the visit to book. For more information, see [Configuration options](#am-configuration).
+  **Optional real-time insurance eligibility (RTE) verification** – Verifies insurance eligibility before confirming a booking. This feature requires a customer-managed AWS Lambda function.
+  **Copay information before appointment confirmation** – Provides copay information to the patient before the appointment is confirmed.

## Requests that transfer to staff
<a name="am-transfers"></a>

Appointment management transfers the following requests to staff:
+  **Special accommodations** – It transfers requests that need special accommodations, such as an interpreter, wheelchair access, or financial assistance.
+  **Specialist referrals** – It transfers requests for a specialist referral, or requests where there is no existing relationship between the patient and the provider.

## Configuration options
<a name="am-configuration"></a>

To configure appointment management, use the patient engagement web app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

You can configure the following settings.


| Setting | Description | 
| --- | --- | 
| Enabled capabilities | Choose which appointment actions are available to patients: schedule, reschedule, cancel, and lookup. Actions that you turn off are routed to a person. | 
| Open scheduling | Available when scheduling is on. Lets patients schedule by visit type. Open scheduling maps a visit type to eligible providers and departments using the open scheduling configuration file in your knowledge base. | 
| Insurance check | Enable or disable real-time insurance eligibility verification. When enabled, appointment management invokes a customer-managed Lambda function to check eligibility and retrieve copay information. This setting requires an active RTE integration. For more information, see [Insurance verification](insurance-verification.md). | 
| Visit types for cancellation and rescheduling | Limit which visit types patients can cancel or reschedule. If you leave the list empty, all visit types are allowed. You can add up to 100 visit types. | 
| Decision tree | Upload a decision tree as a PDF file. The decision tree guides the questions that the agent asks to determine the visit to book, and the scheduling rules to apply. AWS reviews and publishes the decision tree before you can publish the agent. For more information, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md). | 

## Memory and personalization
<a name="am-memory"></a>

When memory and personalization is turned on for your domain, appointment management can do the following:
+ Resume an unfinished scheduling or rescheduling task from an earlier call.
+ Reuse a patient’s remembered provider, time of day, and location.
+ Mention an upcoming appointment, including any pre-visit instructions in your EHR.

For more information, see [Memory and personalization](pe-memory.md).