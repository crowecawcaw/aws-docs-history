

# Ambient documentation
<a name="ambient-documentation"></a>

Ambient documentation captures patient-clinician conversations in real time and generates structured clinical documentation for provider review. The service combines speech recognition with generative AI to produce clinical notes, extract medical terminology, identify speaker roles, and classify dialogue segments.

**Important**  
Amazon Connect Health is not a medical device in the US. Ambient documentation, the Connect Health feature currently available in the UK, is registered as a Class I medical device in the UK.  
Amazon Connect Health ambient documentation produces probabilistic results. Output accuracy varies based on audio quality, background noise, speaker clarity, medical terminology complexity, and context-specific language. All output must be reviewed for accuracy by a trained medical professional before use in patient care.

Amazon Connect Health ambient documentation is available in the US East (N. Virginia) (`us-east-1`) and US West (Oregon) (`us-west-2`) Regions, and as a Preview in the Europe (London) (`eu-west-2`) Region.

**Topics**
+ [How ambient documentation works](#al-how-it-works)
+ [Technical requirements](#al-technical-requirements)
+ [Consent and patient notification](#al-consent)
+ [Supported medical specialties](#al-supported-specialties)
+ [Getting started with ambient documentation](al-getting-started.md)
+ [Subscription management](al-subscription-management.md)
+ [Streaming audio](al-streaming.md)
+ [Encounter context](al-patient-context.md)
+ [Clinical note templates](al-templates.md)
+ [Storage and outputs](al-outputs.md)
+ [Troubleshooting ambient documentation](al-troubleshooting.md)

## How ambient documentation works
<a name="al-how-it-works"></a>

Ambient documentation uses real-time audio streaming over HTTP/2 or WebSocket. The workflow includes:

1.  **Create a subscription** — Associate a provider with the ambient documentation agent. Subscriptions are automatically created in activated mode.

1.  **Stream audio** — Your application streams audio from the patient-clinician conversation to Amazon Connect Health over HTTP/2 or WebSocket. The service transcribes the audio in real time and identifies speakers.

1.  **Generate documentation** — After the conversation ends, the service generates structured clinical notes, evidence mappings, and an after-visit summary based on the configured template.

1.  **Retrieve outputs** — The service writes the transcript, clinical documentation, and after-visit summary to your configured Amazon S3 bucket.

You configure two inputs before streaming starts — encounter context and a clinical note template — and stream audio for as long as the conversation continues. For a step-by-step walkthrough of your first session, see [Getting started with ambient documentation](al-getting-started.md).


| Concept | Where to learn more | 
| --- | --- | 
| Getting started | A step-by-step walkthrough of your first ambient documentation session. See [Getting started with ambient documentation](al-getting-started.md). | 
| Subscription | A configuration resource that associates a provider with the ambient documentation agent. See [Subscription management](al-subscription-management.md). | 
| Streaming audio | How you deliver audio over HTTP/2 or WebSocket, and the best practices that keep a session healthy. See [Streaming audio](al-streaming.md). | 
| Encounter context | Optional clinical background you provide before the conversation starts. See [Encounter context](al-patient-context.md). | 
| Clinical note template | The structure the generated note follows — a managed template or one you customize. See [Clinical note templates](al-templates.md). | 
| Outputs | The transcript, clinical documentation, and after-visit summary files written to Amazon S3. See [Storage and outputs](al-outputs.md). | 

Before you start a session, review [Consent and patient notification](#al-consent).

## Technical requirements
<a name="al-technical-requirements"></a>
+  **Supported languages** — US English (en-US) and Spanish
+  **Supported audio formats** — FLAC, PCM
+  **Encoding** — PCM 16-bit
+  **Sample rate** — The service accepts 8,000–48,000 Hz; 16,000 Hz or higher is recommended for best quality.

## Consent and patient notification
<a name="al-consent"></a>

Amazon Connect Health ambient documentation uses AI to capture and transcribe clinical conversations in real time. Because this feature records spoken communications that may contain protected health information (PHI), customers and their downstream integrators are responsible for complying with all applicable consent, recording, and privacy laws. This includes obtaining all legally required consents before enabling ambient documentation for any patient encounter. AWS does not collect consent from patients on your behalf.

Appropriate consent must be obtained from each patient and anyone present in the room when ambient documentation is used. As part of obtaining consent, patients should be informed that the visit will be recorded and used by an AI service provider to create clinical notes, that their information may be shared with service providers, and that they can decline without any impact on their care. Customers and integrators should maintain records of patient consent, in accordance with applicable state law and internal retention policies. Customers should ensure that consent is obtained in accordance with their organization’s privacy practices.

Sample language:

"Before we begin, I want to let you know that today’s visit will be recorded and monitored by an AI service provider to help with documentation. Do you consent to proceed?"

## Supported medical specialties
<a name="al-supported-specialties"></a>

Ambient documentation currently supports the following specialties:
+ Allergy Immunology
+ Cardiology
+ Dermatology
+ Endocrinology
+ Gastroenterology
+ Hematology/Oncology
+ Infectious Disease
+ Nephrology
+ Neurology
+ OBGYN
+ Oncology
+ Ophthalmology
+ Orthopedics
+ Otolaryngology
+ Pain Medicine
+ Pediatrics
+ Primary Care
+ Psychiatry
+ Pulmonology
+ Rheumatology
+ Surgery
+ Urology