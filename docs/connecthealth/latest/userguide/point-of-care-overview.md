

# Point of care agents
<a name="point-of-care-overview"></a>

Amazon Connect Health point of care features are AI-powered capabilities that streamline administrative workflows in outpatient clinical settings. Point of care agentic capabilities combine speech recognition, generative AI, and reasoning to reduce documentation burden for clinicians and back-office staff.

Point of care features operate within a domain that you provision in your AWS account. Each feature accepts inputs (such as a real-time audio stream of a patient-clinician conversation, patient context from the EHR, a clinical note template, or finalized clinical documentation) and produces structured outputs for provider review, including clinical documentation, evidence mappings, after-visit summaries, and suggested medical codes.

Point of care agents include patient insights (preview), ambient documentation (generally available), and medical coding (gated preview). Each agent supports a different stage of the visit. The agents don’t pass outputs to each other. Your application decides what to send to each agent. For example, it can send the pre-visit summary from patient insights to ambient documentation as encounter context (optional), and submit the clinical note from ambient documentation to medical coding.

![Point of care agents across a visit: patient insights before, ambient documentation during, and medical coding after.](https://docs.aws.amazon.com/connecthealth/latest/userguide/images/point-of-care-visit-timeline.png)


**Topics**
+ [Key concepts](#poc-key-concepts)
+ [Regional availability](#poc-regional-availability)
+ [Patient insights](patient-insights.md)
+ [Ambient documentation](ambient-documentation.md)
+ [Medical coding](medical-coding.md)

## Key concepts
<a name="poc-key-concepts"></a>


| Concept | Description | 
| --- | --- | 
| Domain | An isolated environment within your AWS account where you provision point of care agents. | 
| Subscription | A configuration resource that associates a provider or session with an agent. Required for ambient documentation. | 
| Template | A structured definition of the clinical note format. Used by ambient documentation to generate documentation. | 
| Job | An asynchronous unit of work that you start and later poll for results. Used by medical coding to generate suggested codes from clinical documentation. | 
| Vended artifacts | The output files written to your Amazon S3 bucket, such as pre-visit summaries, transcripts, clinical notes, and suggested medical codes. | 

## Regional availability
<a name="poc-regional-availability"></a>

Point of care agents are available in the following AWS Regions. Availability differs by agent.


| Region name | Region code | Point of care agents | 
| --- | --- | --- | 
| US East (N. Virginia) |  `us-east-1`  | Patient insights (preview), Ambient documentation (generally available), Medical coding (gated preview) | 
| US West (Oregon) |  `us-west-2`  | Patient insights (preview), Ambient documentation (generally available), Medical coding (gated preview) | 
| Europe (London) |  `eu-west-2`  | Ambient documentation (preview) | 

**Note**  
Preview and gated preview agents are subject to change and are not intended for production use. Gated preview agents additionally require access to be granted by your AWS account team.