# AWS HealthScribe Transcript file

In the transcript file, in addition to standard turn-by-turn transcription output with
word level timestamps, AWS HealthScribe provides you with:

- **Participant role detection** so you can distinguish the patients
  from the clinicians in the conversation transcript.
- **Transcript sectioning**, which categorizes transcript dialogues
  based on their clinical relevance like small talk, subjective, objective, etc. This can
  be used to show specific portions of the transcript.
- **Clinical entities**, which includes structured information like
  medications, medical conditions, and treatments mentioned in the conversation.
  In addition, the following insights are provided for each conversation turn:

- **Participant role** — Each participant is labeled as either a clinician or a patient. If a
  conversation has more than one participant in each category, each participant is assigned a number. For example,
  `CLINICIAN_0`, `CLINICIAN_1` and `PATIENT_0`, `PATIENT_1`.
- **Section** — Each dialogue turn is assigned to one of four possible sections based on the
  content identified.
  - **Subjective** — Information provided by the patient about their health concerns.
  - **Objective** — Information observed by the clinician through physical exam, lab,
    imaging, or diagnostic tests.
  - **Assessment and Plan** — Information that relates to the doctor's assessment and
    treatment plan.
  - **Visit Flow Management** — Information related to small talk or
    transitions.

- **Insights** — Extract clinically relevant entities (`ClinicalEntity`) present in
  the conversation. AWS HealthScribe detects all clinical entities supported by [Amazon Comprehend Medical](https://aws.amazon.com//comprehend/medical "https://aws.amazon.com//comprehend/medical").
  For an example of a transcript from a transcription job, see the transcript output in [Transcription job output examples](starting-health-scribe-job.md#health-scribe-output-example "starting-health-scribe-job.md#health-scribe-output-example").
  For an example of a transcript from streaming, see the transcript output in [Streaming transcription output examples](health-scribe-streaming-setting-up.md#health-scribe-streaming-output-example "health-scribe-streaming-setting-up.md#health-scribe-streaming-output-example").
