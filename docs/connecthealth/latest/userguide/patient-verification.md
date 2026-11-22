

# Patient verification

Patient verification confirms a patient’s identity through a conversation, using real-time EHR integration and configurable authentication factors such as date of birth and phone number. It looks up the patient’s record from the incoming phone number, so contact center staff don’t need to search for it.

A caller can verify for themselves or on behalf of someone else, such as a caregiver calling for a patient. At the start of verification, the capability asks whether the caller is calling for themselves or for someone else. It then asks for the patient’s verification factors.

Patient verification queries the Epic EHR through FHIR APIs in real time to match and verify patient records during the call.

## Capabilities
<a name="pv-capabilities"></a>

Patient verification provides the following:
+  **Real-time patient identity verification** – Verifies patient identity against EHR records in real time.
+  **Three-factor verification** – Verifies every patient with three factors: phone number or medical record number (MRN), date of birth, and ZIP code or the last four digits of the Social Security number (SSN).
+  **Keypad (DTMF) fallback** – Accepts keypad, or dual-tone multi-frequency (DTMF), input as a fallback for numeric fields and yes-or-no questions. This fallback is on by default, and patient verification offers keypad entry on retries.
+  **Escalation to a person** – Escalates to a person with full verification context.
+  **24/7 availability** – Handles routine verification tasks at any time of day.

## Customization options
<a name="pv-customization"></a>

To customize patient verification, use the patient engagement web app. For more information, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

You can configure the following settings.

Verification factors  
Patient verification always asks for all three factor groups, in order. For each group, you choose which identifiers the capability accepts. When a group accepts more than one identifier, the caller chooses which one to provide. The default configuration uses the following groups:  
+ First factor – Phone number or MRN
+ Second factor – Date of birth
+ Third factor – Last four digits of SSN

You can set the first factor to accept phone number, MRN, or either one. You can set the third factor to accept ZIP code, the last four digits of SSN, or either one.

Retry and escalation thresholds  
Set the number of retries before the capability escalates, and the number of off-topic redirects before it escalates. You set these thresholds on the agent, and every capability inherits them.

Each threshold accepts a value from 1 to 10 and defaults to 2.

After you configure the settings, publish the agent to apply the changes. For more information, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).