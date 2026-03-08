# Patient verification agent

The Patient verification agent provides secure, conversational identity verification through real-time EHR integration and configurable multi-attribute authentication such as date of birth and phone number. It provides patient profile lookup based on incoming call number and eliminates manual lookup by contact center staff. This agent collects and verifies patient identity through self service for caregivers on behalf of a patient.

The Patient verification agent eliminates time-consuming manual EHR lookups by automating the identity verification process. It queries Epic FHIR APIs in real time to match and verify patient records during the call.

###### Topics

- [Capabilities](#pv-capabilities "#pv-capabilities")
- [Customization options](#pv-customization "#pv-customization")

## Capabilities

The Patient verification agent provides the following capabilities:

- **Real-time patient identity verification** – Verifies patient identity through Epic FHIR APIs.
- **Configurable multi-factor authentication** – Supports verification using phone number, MRN, date of birth, zip code, and SSN.
- **LLM-based safety guardrails** – Detects safety concerns, frustrated patients, and complex requests.
- **Intelligent escalation to human agents** – Escalates to human agents with full verification context.
- **24/7 availability** – Provides around-the-clock availability for routine verification tasks.

## Customization options

You can configure the Patient verification agent to match your organization’s verification requirements. To customize the agent, choose **Customize** on the Agent setup card in the Amazon Connect Health console.

You can configure the following settings:

| Setting                 | Description                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Verification attributes | Choose which factors are required for authentication, such as MRN, date of birth, zip code, or last four digits of SSN. |

After you configure the settings, choose **Publish** to apply the changes.
