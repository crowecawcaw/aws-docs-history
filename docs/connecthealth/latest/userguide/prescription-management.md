

# Prescription management

Prescription management is part of the agentic capabilities for patient access. It helps a verified patient request refills and check refill status for prescriptions through a health system pharmacy. Use it with patient verification on a pharmacy line. Callers reach it by phone.

To make prescription management available to callers, turn it on in the Amazon Connect Health app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

## Prerequisites
<a name="rx-prerequisites"></a>

Before you turn on prescription management, make sure the following are in place:
+ Patient verification is turned on for the same agent.
+ A pharmacy SOAP endpoint is configured on your electronic health record (EHR) integration. If you add the endpoint to an `ACTIVE` integration, the integration returns to `PENDING`. After you set the endpoint, you can’t change it while the integration is `ACTIVE`.
+ The Epic Clinical Pharmacy Web Services 2018 APIs `GetPrescriptionInfo` and `RequestFills` are enabled for your Amazon Connect Health client. For more information, see [Epic EHR integration](epic-ehr-integration.md).

## How it works
<a name="rx-how-it-works"></a>

Prescription management helps a verified patient as follows:
+ The patient names the existing prescription, gives the prescription (Rx) number, or gives the last four characters of the Rx number.
+ The capability reads back the prescription name and strength so the patient can confirm it. It does not read dosage instructions.
+ If the patient cannot name a prescription, it lists active prescriptions three at a time.
+ The patient can handle several prescriptions in one call.

For a refill, the patient chooses pickup, mail, or courier. For mail or courier, the capability reads back the delivery address on file. For refill status, it reports the refill as in progress, eligible, or not eligible. Epic decides whether a refill needs prescriber renewal.

## Guardrails
<a name="rx-guardrails"></a>

Prescription management applies the following guardrails:
+ All emergency and safety guardrails apply to this capability. For example, if a patient says they have acute chest pain, the capability transfers them immediately to an on-call staff member.
+ Clinical medication questions, such as dosage or side effects, transfer to a person immediately.

## What prescription management does not do
<a name="rx-limitations"></a>

Prescription management does not do the following:
+ Give medical advice, such as dosage or usage advice
+ Give refill or delivery dates
+ Change the pharmacy or the delivery address. Currently it transfers these requests to a pharmacist.
+ Prescribe new medication. It transfers these requests to a pharmacist.

## Customization options
<a name="rx-customization"></a>

You can configure prescription management in the web app. For instructions on setting up agents, see [Set up agents in the patient engagement web app](setting-up-pe-web-app.md).

Prescription management provides two configurations to address two use cases:
+  **Refill request**: The capability takes prescription refill requests.
+  **Refill status**: The capability checks the status of a refill when asked.