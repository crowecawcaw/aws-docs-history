

# Storage and outputs
<a name="al-outputs"></a>

**Topics**
+ [Storage](#al-storage)
+ [Outputs](#al-outputs-list)

## Storage
<a name="al-storage"></a>

An S3 storage location must be specified at the start of a session. Output artifacts are stored at the following base location:

 `s3://{customer-provided-uri}/health-agent-listening-session/{domainId}/{subscriptionId}/{sessionId}/post-stream-action/` 

Clinical notes are stored in a `clinical-notes` folder at this base location.

## Outputs
<a name="al-outputs-list"></a>

Ambient documentation generates three output files:


| File | Contains | 
| --- | --- | 
| Transcript | Turn-by-turn transcription with word-level timestamps and speaker labels | 
| Clinical documentation and evidence mapping | The structured clinical note, plus a mapping from each generated statement back to its source | 
| After-visit summary | A patient-facing summary in plain language, generated from the clinical documentation file | 

### Transcript file
<a name="al-transcript"></a>

The transcript file contains turn-by-turn transcription with word-level timestamps. Amazon Connect Health adds participant role detection, labeling each speaker as CLINICIAN or PATIENT. If a conversation has more than one participant in each category, each participant is assigned a number (for example, `CLINICIAN_0`, `CLINICIAN_1`).

### Clinical documentation and evidence mapping file
<a name="al-clinical-doc"></a>

The clinical documentation file contains the structured clinical note generated from the patient-clinician conversation and a section linking each generated statement back to its source in the conversation transcript or encounter context input.

The file follows the managed template or customization instructions provided at the start of the session. Each section can contain visit-derived content (from the conversation) and context-derived content (from encounter context input). Multiple output formats are supported: prose/free-text and structured JSON depending on template configuration. The evidence mapping section enables clinicians to verify the origin of any AI-generated content. Each mapping entry contains the generated sentence and the source transcript/context reference.

### After-visit summary file
<a name="al-after-visit"></a>

The after-visit summary file contains a patient-facing summary written in accessible language for a clinician’s review and finalization. It includes a plain-language description of the visit, current medications with dosage and frequency, clinician’s follow-up instructions, and action items for the patient.

The summary is generated from the clinical documentation file, not directly from the transcript, ensuring consistency between the clinical note and the patient-facing summary.

For complete API parameter details, request/response schemas, and streaming setup instructions, see the [Amazon Connect Health API Reference](https://docs.aws.amazon.com/connecthealth/latest/APIReference/Welcome.html).