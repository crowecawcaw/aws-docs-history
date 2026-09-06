

# Amazon Transcribe Medical
<a name="transcribe-medical"></a>

Amazon Transcribe Medical is an automatic speech recognition (ASR) service designed for medical professionals who want to transcribe medical-related speech, such as physician-dictated notes, drug safety monitoring, telemedicine appointments, or physician-patient conversations. Amazon Transcribe Medical is available through either real-time streaming (via microphone) or transcription of an uploaded file (batch).

**Important**  
Amazon Transcribe Medical is not a substitute for professional medical advice, diagnosis, or treatment. Identify the right confidence threshold for your use case, and use high confidence thresholds in situations that require high accuracy. For certain use cases, results should be reviewed and verified by appropriately trained human reviewers. Amazon Transcribe Medical transcriptions should only be used in patient care scenarios after review for accuracy and sound medical judgment by trained medical professionals.

Amazon Transcribe Medical operates under a shared responsibility model, whereby AWS is responsible for protecting the infrastructure that runs Amazon Transcribe Medical and you are responsible for managing your data. For more information, see [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/).

Amazon Transcribe Medical is available in US English (en-US).

For best results, use a lossless audio format, such as FLAC or WAV, with PCM 16-bit encoding. Amazon Transcribe Medical supports sample rates of 16,000 Hz or higher.

For analysis of your transcripts, you can use other AWS services, such as [Amazon Comprehend Medical](https://docs.aws.amazon.com/comprehend/latest/dg/comprehend-medical.html).


**Supported specialties**  

| Specialty | Sub-specialty | Audio input | 
| --- | --- | --- | 
| Cardiology | none | streaming only | 
| Neurology | none | streaming only | 
| Oncology | none | streaming only | 
| Primary Care | Family Medicine | batch, streaming | 
| Primary Care | Internal Medicine | batch, streaming | 
| Primary Care | Obstetrics and Gynecology (OB-GYN) | batch, streaming | 
| Primary Care | Pediatrics | batch, streaming | 
| Radiology | none | streaming only | 
| Urology | none | streaming only | 

## Region availability and quotas
<a name="med-regions"></a>

Call Analytics is supported in the following AWS Regions:


| **Region** | **Transcription type** | 
| --- | --- | 
| af-south-1 (Cape Town) | batch | 
| ap-east-1 (Hong Kong) | batch | 
| ap-northeast-1 (Tokyo) | batch, streaming | 
| ap-northeast-2 (Seoul) | batch, streaming | 
| ap-south-1 (Mumbai) | batch | 
| ap-southeast-1 (Singapore) | batch | 
| ap-southeast-2 (Sydney) | batch, streaming | 
| ca-central-1 (Canada, Central) | batch, streaming | 
| eu-central-1 (Frankfurt) | batch, streaming | 
| eu-north-1 (Stockholm) | batch | 
| eu-west-1 (Ireland) | batch, streaming | 
| eu-west-2 (London) | batch, streaming | 
| eu-west-3 (Paris) | batch | 
| me-south-1 (Bahrain) | batch | 
| sa-east-1 (São Paulo) | batch, streaming | 
| us-east-1 (N. Virginia) | batch, streaming | 
| us-east-2 (Ohio) | batch, streaming | 
| us-gov-east-1 (GovCloud, US-East) | batch, streaming | 
| us-gov-west-1 (GovCloud, US-West) | batch, streaming | 
| us-west-1 (San Francisco) | batch | 
| us-west-2 (Oregon) | batch, streaming | 

Note that Region support differs for [Amazon Transcribe](what-is.md#tsc-regions), Amazon Transcribe Medical, and [Call Analytics.](call-analytics.md#tca-regions).

To get the endpoints for each supported Region, see [Service endpoints](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#transcribe_region) in the *AWS General Reference*.

For a list of quotas that pertain to your transcriptions, refer to the [Service quotas](https://docs.aws.amazon.com/general/latest/gr/transcribe.html#limits-amazon-transcribe) in the *AWS General Reference*. Some quotas can be changed upon request. If the **Adjustable** column contains '**Yes**', you can request an increase. To do so, select the provided link.