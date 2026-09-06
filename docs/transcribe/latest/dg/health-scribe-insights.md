

# AWS HealthScribe Clinical Documentation file
<a name="health-scribe-insights"></a>

AWS HealthScribe can use one of the following templates for the clinical note summary. The default is `HISTORY_AND_PHYSICAL`.
+ HISTORY\_AND\_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan. 
+ GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.
+ BIRP: Focuses on the patient's behavioral patterns and responses. Examples of sections include Behavior, Intervention, Response, and Plan.
+ SIRP: Emphasizes the situational context of therapy. Examples of sections include Situation, Intervention, Response, and Plan.
+ DAP: Provides a simplified format for clinical documentation. Examples of sections include Data, Assessment, and Plan.
+ BH\_SOAP: Behavioral health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.
+ PH\_SOAP: Physical health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.

To specify what template to use, do the following:
+  For transcription jobs, specify the template to use in the `NoteTemplate` of the [ClinicalNoteGenerationSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_ClinicalNoteGenerationSettings.html) of the `Settings` of your [StartMedicalScribeJob](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_StartMedicalScribeJob.html) API operation. 
+  For streaming, you specify the template to use in the `NoteTemplate` of the [ClinicalNoteGenerationSettings](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_ClinicalNoteGenerationSettings.html) of the `PostStreamAnalyticsSettings` of your [MedicalScribeConfigurationEvent](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_streaming_MedicalScribeConfigurationEvent.html). 

## Medical Scribe context
<a name="health-scribe-contextual-information"></a>

The `MedicalScribeContext` object contains contextual information used to customize clinical note generation with patient-specific details.

The `MedicalScribeContext` object includes the following components:
+ **PatientContext** - Contains patient-specific information used to customize clinical note generation. This includes:
  + **Pronouns** - The patient's preferred pronouns that you want to provide as context for clinical note generation. These pronouns are used when referring to the patient in the generated clinical output.

For information on how to set up the medical scribe context, see [MedicalScribeContext](https://docs.aws.amazon.com/transcribe/latest/APIReference/API_MedicalScribeContext.html).

**Topics**
+ [Medical Scribe context](#health-scribe-contextual-information)
+ [HISTORY\_AND\_PHYSICAL template sections](#health-scribe-history-physical-insights)
+ [GIRPP template sections](#health-scribe-GIRPP-insights)
+ [BIRP template sections](#health-scribe-BIRP-insights)
+ [SIRP template sections](#health-scribe-SIRP-insights)
+ [DAP template sections](#health-scribe-DAP-insights)
+ [BH\_SOAP template sections](#health-scribe-BH-SOAP-insights)
+ [PH\_SOAP template sections](#health-scribe-PH-SOAP-insights)

## HISTORY\_AND\_PHYSICAL template sections
<a name="health-scribe-history-physical-insights"></a>

The HISTORY\_AND\_PHYSICAL insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| CHIEF COMPLAINT | Brief description for the patient's reason for visiting the clinician. | 
| HISTORY OF PRESENT ILLNESS | Notes that provide information on patient's illness, including reference to severity, onset, timing of symptoms, current treatments, and the affected areas. | 
| REVIEW OF SYSTEMS | Patient-reported evaluation of symptoms across different body systems. | 
| PAST MEDICAL HISTORY | Details a patient's previous medical conditions, surgeries, and treatments. | 
| ASSESSMENT | Notes that provide information on clinician's assessment of patient's health. | 
| PLAN | Notes that reference any medical treatments, lifestyle adjustments, and further appointments. | 
| PHYSICAL\_EXAMINATION | Documentation of clinician's findings from physical examination of patient's body systems and vital signs. | 
| PAST\_FAMILY\_HISTORY | Information about health conditions that run in the patient's family. | 
| PAST\_SOCIAL\_HISTORY | Details about patient's social life, habits, occupation, and environmental factors affecting health. | 
| DIAGNOSTIC\_TESTING | Results and interpretation of laboratory tests, imaging studies, and other diagnostic procedures. | 

Each sentence present in the `Summary` includes `EvidenceLinks` that provide the `SegmentId` for the relevant dialogues in the transcript that were summarized. This helps users validate accuracy of the summary in your application. Like explainability, providing traceability and transparency for AI-generated insights is consistent with Responsible AI principles. Providing these references along with the summary notes to clinicians or medical scribes helps foster trust and encourage the safe use of AI in the clinical settings.

For an example of a Clinical Documentation file from a transcription job, see the a Clinical Documentation file example in [Transcription job output examples](starting-health-scribe-job.md#health-scribe-output-example). For an example of a Clinical Documentation file from streaming, see the a Clinical Documentation file example in [Streaming transcription output examples](health-scribe-streaming-setting-up.md#health-scribe-streaming-output-example). 

## GIRPP template sections
<a name="health-scribe-GIRPP-insights"></a>

The GIRPP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Goal | The identified problem, challenge, or behavior that needs to be addressed through treatment. | 
| Intervention | The specific treatment, method, or technique used by the clinician to help the patient address the identified goal. | 
| Response | How the patient responded to the intervention, including their participation level, reactions, and feedback. | 
| Progress | The clinician's assessment of movement toward treatment goals, including observations of patient improvement or barriers. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 

## BIRP template sections
<a name="health-scribe-BIRP-insights"></a>

The BIRP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Behavior | The problems that the patient presents and their response to the treatment. | 
| Intervention | The specific treatment, method, or technique used by the clinician to help the patient address the identified goal. | 
| Response | How the patient responded to the intervention, including their participation level, reactions, and feedback. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 

## SIRP template sections
<a name="health-scribe-SIRP-insights"></a>

The SIRP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Situation | The problem that the patient presents and their goal for seeking therapy. | 
| Intervention | The specific treatment, method, or technique used by the clinician to help the patient address the identified goal. | 
| Response | How the patient responded to the intervention, including their participation level, reactions, and feedback. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 

## DAP template sections
<a name="health-scribe-DAP-insights"></a>

The DAP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Data | The patient's reasons for seeking treatment and information about the patient. | 
| Assessment | The clinician's diagnosis of the patient's situation. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 

## BH\_SOAP template sections
<a name="health-scribe-BH-SOAP-insights"></a>

The BH\_SOAP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Subjective | The client's goals for treatment and their experiences, as well as existing and past issues. | 
| Objective | Data and facts about the client. | 
| Assessment | The clinician's diagnosis of the patient's situation. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 

## PH\_SOAP template sections
<a name="health-scribe-PH-SOAP-insights"></a>

The PH\_SOAP insights template includes the following sections.


| Section | Description | 
| --- | --- | 
| Subjective | The client's goals for treatment and their experiences, as well as existing and past issues. | 
| Objective | Data and facts about the client. | 
| Assessment | The clinician's diagnosis of the patient's situation. | 
| Plan | The next steps in treatment, including future interventions, homework assignments, and referrals. | 