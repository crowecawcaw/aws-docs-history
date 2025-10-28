# AWS HealthScribe transcription jobs

An AWS HealthScribe transcription job processes media files from an Amazon S3 bucket. When it processes a media file, it transcribes
patient-clinician conversations and analyzes medical consultation to produces two JSON output files: a [transcript](health-scribe-job.md#health-scribe-output-example "health-scribe-job.md#health-scribe-output-example")
file and a [clinical documentation](health-scribe-job.md#health-scribe-output-example "health-scribe-job.md#health-scribe-output-example") file.

The following are API operations specific to AWS HealthScribe transcription jobs:

- [StartMedicalScribeJob](../APIReference/API_StartMedicalScribeJob.md "../APIReference/API_StartMedicalScribeJob.md")
- [ListMedicalScribeJobs](../APIReference/API_ListMedicalScribeJobs.md "../APIReference/API_ListMedicalScribeJobs.md")
- [GetMedicalScribeJob](../APIReference/API_GetMedicalScribeJob.md "../APIReference/API_GetMedicalScribeJob.md")
- [DeleteMedicalScribeJob](../APIReference/API_DeleteMedicalScribeJob.md "../APIReference/API_DeleteMedicalScribeJob.md")
