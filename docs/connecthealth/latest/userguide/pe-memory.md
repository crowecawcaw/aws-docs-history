

# Memory and personalization

With memory and personalization, the agent uses information from a patient’s earlier calls to help on the current call. The agent uses memory and personalization only after it verifies the patient. For more information about verification, see [How a patient call is handled](pe-call-routing.md).

## Turn on memory and personalization
<a name="pe-memory-turn-on"></a>

Memory and personalization is turned off by default. AWS turns on memory and personalization for your domain when you request it. You cannot turn it on in the patient engagement web app.

To turn on memory and personalization for your domain, contact your AWS account team.

## Resume an unfinished task
<a name="pe-memory-resume"></a>

If a call ends before a task is complete, the agent can offer to continue it on a later call. The agent offers to resume the following tasks:
+ Scheduling or rescheduling an appointment
+ Resetting a MyChart password

The agent keeps an unfinished task for 30 days. Before the agent resumes a task, it checks the current information in your electronic health record (EHR), such as appointment availability, so it does not rely on outdated details.

If the patient declines to resume the task, the agent deletes it.

## Reuse a patient’s earlier choices
<a name="pe-memory-preferences"></a>

The agent learns from the choices a patient makes and uses them to save time on later calls:
+  **Provider** – The provider the patient chooses for an appointment type.
+  **Time of day** – Morning, afternoon, or evening.
+  **Location** – The location where the patient books appointments.
+  **Reset channel** – Email or text message for a MyChart password reset.

The agent uses a choice only after the patient makes it at least two times in the last 30 days. If the patient chooses something different two times, the agent stops using the earlier choice. The patient can always choose something else during the call.

When the agent uses a remembered choice, it confirms with the patient before it applies the choice. For example, it might ask, "Would you like to see Dr. Johnson again, or are you open to other providers?"

## Mention an upcoming appointment
<a name="pe-memory-upcoming"></a>

If the patient has an appointment booked in the next 72 hours, the agent can mention it, including any pre-visit instructions in your EHR. The agent reads this information from your EHR during the call.

You can ask AWS to change this window to a value from 24 hours to 336 hours (14 days). To change it, contact your AWS account team.

## Which offer the agent makes first
<a name="pe-memory-which-offer-the-agent-makes-first"></a>

If the patient has both an unfinished task and an upcoming appointment, the agent offers to resume the unfinished task first.

The agent does not remind patients about prescriptions that need renewal.

## What is stored
<a name="pe-memory-data"></a>

Memory and personalization stores structured values only, such as record identifiers, categories, and dates. It reads appointment details and instructions from your EHR during each call and does not store them. For details about what is stored, how long it is kept, how it is deleted, and how it is encrypted, see [Data protection in Amazon Connect Health](data-protection.md).