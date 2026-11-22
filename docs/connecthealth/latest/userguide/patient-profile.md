

# Patient profile

The patient profile is a unified view displayed in the Amazon Connect Customer Agent Workspace that provides human agents with upstream call leg context when they are connected with a caller. Whether the call is transferred after successful patient verification or escalated during appointment management, this profile reduces the need for patients to repeat information and reduces cognitive burden on human agents.

![Patient Profile feature in Amazon Connect Customer Agent Workspace.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/patient-profile-workspace.png)


**Topics**
+ [Patient information displayed](#pp-patient-info)
+ [Patient verification status](#pp-verification-status)
+ [Escalation information](#pp-escalation-info)
+ [Self-service summary](#pp-self-service-summary)
+ [Error scenarios](#pp-error-scenarios)

## Patient information displayed
<a name="pp-patient-info"></a>

The patient profile displays the following information:
+ Verified demographic info as it applies: Full name, date of birth, medical record number (MRN), and last 4 digits of SSN
+ Contact information, including phone number and address
+ Primary care provider and care team

## Patient verification status
<a name="pp-verification-status"></a>

The profile shows the outcome of the identity verification process:
+ Verification outcome: verified, partially verified, or failed
+ Factors that were successfully verified
+ Number of verification attempts

## Escalation information
<a name="pp-escalation-info"></a>

When a call is escalated from an AI agent, the profile includes:
+ Reason for escalation, such as a safety concern, complex request, patient frustration, or verification failure
+ Escalation timestamp and originating flow

## Self-service summary
<a name="pp-self-service-summary"></a>

The profile provides a summary of actions completed by the AI agent before the escalation, including any of the following:
+ Actions completed or attempted during the self-service interaction
+ Appointment changes made or confirmed
+ Insurance verification outcome, if applicable
+ Prescription names, refill request and refill status details

## Error scenarios
<a name="pp-error-scenarios"></a>

When patient verification was incomplete or failed, the patient profile displays all information collected from the caller during the verification attempt. This ensures that human agents can see which verification factors were already provided and which ones failed or were missing, eliminating the need to ask patients to repeat information they have already shared.