# AWS HealthScribe

AWS HealthScribe is a HIPAA-eligible machine learning (ML) capability that combines speech recognition and
generative AI to transcribe patient-clinician conversations and generate easy-to-review clinical notes. AWS HealthScribe helps healthcare software vendors build clinical applications that reduce the documentation burden and improve
consultation experience. The service automatically provides rich conversation transcripts, identifies speaker roles,
classifies dialogues, extracts medical terms, and generates preliminary clinical notes. AWS HealthScribe
combines these capabilities to remove the need to integrate and optimize separate AI services, enabling you to expedite
implementation.

Common use cases:

- **Reduce documentation time** — Enable clinicians to quickly complete clinical documentation
  with AI-generated clinical notes that are easy to review, adjust, and finalize in your application.
- **Boost medical scribe efficiency** — Equip medical scribes with AI-generated transcript and
  clinical notes, along with the consultation audio, to expedite documentation turn-around time.
- **Efficient patient visit recap** — Create an experience that enables users to quickly
  recollect key highlights of their conversation in your application.

###### Important

The results produced by AWS HealthScribe are probabilistic and may not always be accurate due to various
factors, including audio quality, background noise, speaker clarity, the complexity of medical terminology, context-specific
language nuances, and [the nature of machine learning
and generative AI](https://aws.amazon.com/machine-learning/responsible-ai/policy/ "https://aws.amazon.com/machine-learning/responsible-ai/policy/"). AWS HealthScribe is designed to be used in an assistive role for clinicians and
medical scribes. AWS HealthScribe output should only be used in patient care scenarios, including, but not
limited to as part of Electronic Health Records, after review for accuracy and imposition of sound medical judgment by
trained medical professionals. AWS HealthScribe output is not a substitute for professional medical advice,
diagnosis, or treatment, and is not intended to cure, treat, mitigate, prevent, or diagnose any disease or health condition.

###### Topics

- [Security](#health-scribe-security-overview "#health-scribe-security-overview")
- [Service availability](#health-scribe-availability "#health-scribe-availability")
- [Technical requirements](#health-scribe-tech-requirements-overview "#health-scribe-tech-requirements-overview")
- [Supported Medical Specialties](#health-scribe-specialties "#health-scribe-specialties")
- [Workflows](#health-scribe-workflows "#health-scribe-workflows")
- [AWS HealthScribe Transcript file](health-scribe-transcript.md "health-scribe-transcript.md")
- [AWS HealthScribe Clinical Documentation file](health-scribe-insights.md "health-scribe-insights.md")
- [AWS HealthScribe transcription jobs](health-scribe-job.md "health-scribe-job.md")
- [AWS HealthScribe streaming](health-scribe-streaming.md "health-scribe-streaming.md")
- [Data Encryption at rest for AWS HealthScribe](health-scribe-encryption.md "health-scribe-encryption.md")

## Security

AWS HealthScribe operates under a shared responsibility model, whereby AWS is responsible
for protecting the infrastructure that runs AWS HealthScribe and you are responsible for managing
your data. For more information, see [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

By default, AWS HealthScribe provides encryption at rest to protect sensitive customer data using Amazon S3-managed keys. When you create
AWS HealthScribe transcription job or start a stream, you can specify a customer managed key. This adds a second layer of
encryption. For more information, see [Data Encryption at rest for AWS HealthScribe](health-scribe-encryption.md "health-scribe-encryption.md").

## Service availability

AWS HealthScribe is available in the US East (N. Virginia) region.

## Technical requirements

- **Supported Language:** US English (en-US)
- **Recommended Audio Format:** Lossless audio (such as FLAC or WAV)
- **Encoding:** PCM 16-bit
- **Sample Rate:** 16,000 Hz or higher

## Supported Medical Specialties

AWS HealthScribe currently supports the following specialties:

- Allergy Immunology
- Cardiology
- Dermatology
- Endocrinology
- Gastroenterology
- Hematology/Oncology
- Infectious Disease
- Nephrology
- Neurology
- OBGYN
- Oncology
- Ophthalmology
- Orthopedics
- Otolaryngology
- Pain Medicine
- Pediatrics
- Primary Care
- Psychiatry
- Pulmonology
- Rheumatology
- Surgery
- Urology

## Workflows

AWS HealthScribe workflows include transcription jobs and streaming. After you run a transcription job or complete a stream,
AWS HealthScribe generates a transcript file, with turn-by-turn transcription output and insights for each conversation turn. Also it generates a
clinical documentation file, with summaries and evidence links. For more information see [AWS HealthScribe Transcript file](health-scribe-transcript.md "health-scribe-transcript.md") and [AWS HealthScribe Clinical Documentation file](health-scribe-insights.md "health-scribe-insights.md").

- **Transcription jobs** – With transcription jobs, AWS HealthScribe analyzes completed medical consultation
  media files from an Amazon S3 bucket. The following are API operations specific to AWS HealthScribe transcription jobs.

      + [StartMedicalScribeJob](../APIReference/API_StartMedicalScribeJob.md "../APIReference/API_StartMedicalScribeJob.md")
      + [ListMedicalScribeJobs](../APIReference/API_ListMedicalScribeJobs.md "../APIReference/API_ListMedicalScribeJobs.md")
      + [GetMedicalScribeJob](../APIReference/API_GetMedicalScribeJob.md "../APIReference/API_GetMedicalScribeJob.md")
      + [DeleteMedicalScribeJob](../APIReference/API_DeleteMedicalScribeJob.md "../APIReference/API_DeleteMedicalScribeJob.md")

  For more information, including code examples, see [AWS HealthScribe transcription jobs](health-scribe-job.md "health-scribe-job.md").

- **Streaming** – AWS HealthScribe streaming is a real-time HTTP2 based bi-directional
  service that accepts audio stream on one channel and vends an audio transcription on the other channel.

The following are API operations specific to AWS HealthScribe streaming:

    + [StartMedicalScribeStream](../APIReference/API_streaming_StartMedicalScribeStream.md "../APIReference/API_streaming_StartMedicalScribeStream.md")
    + [GetMedicalScribeStream](../APIReference/API_streaming_GetMedicalScribeStream.md "../APIReference/API_streaming_GetMedicalScribeStream.md")

For more information, including code examples, see [AWS HealthScribe streaming](health-scribe-streaming.md "health-scribe-streaming.md").
