

# Medical coding
<a name="medical-coding"></a>

**Important**  
Medical coding is available as a gated preview. To request access, contact your AWS account team. Features and availability are subject to change, and gated preview features should not be used in production environments.

Every patient encounter must be translated into standardized codes before the provider is paid. A coder reads the clinical note and identifies each diagnosis and each procedure or service. The coder then assigns International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) codes to the diagnoses and Current Procedural Terminology (CPT) codes, with any required modifiers, to the procedures and services. For office and telehealth visits, the coder sets the evaluation and management (E/M) level from the documented medical decision making (MDM). Finally, the coder confirms that the diagnoses support medical necessity for every billed service. The work is skilled, manual, and repeated for every visit. Coding backlogs delay claim submission, and coding errors lead to denials, rework, and compliance exposure.

Medical coding generates this code set directly from the clinical documentation. For each encounter, it returns the diagnosis codes, the procedure and service codes with modifiers, the E/M level, and the evidence in the note that supports each code. Coders and clinicians review a complete code set backed by evidence instead of building one from scratch. Your application decides how much review each encounter receives.

Medical coding is a point of care agent. You integrate it into your own application through two asynchronous APIs, `StartMedicalCodingJob` and `GetMedicalCodingJob`, and it does not require a contact center. It is available as a gated preview in the US East (N. Virginia) (`us-east-1`) and US West (Oregon) (`us-west-2`) Regions.

**Topics**
+ [What medical coding generates](#mc-what-it-generates)
+ [What medical coding optimizes for](#mc-what-it-optimizes)
+ [Specialty scope and model performance](#mc-specialty-scope)
+ [Medical coding topics](#mc-topics)
+ [Getting started with medical coding](mc-getting-started.md)
+ [How medical coding works](mc-how-it-works.md)
+ [Medical coding inputs](mc-inputs.md)
+ [Medical coding outputs](mc-outputs.md)
+ [Integrating medical coding into your workflows](mc-integration.md)
+ [Troubleshooting medical coding](mc-troubleshooting.md)

## What medical coding generates
<a name="mc-what-it-generates"></a>


| Code set | Covers | Output | 
| --- | --- | --- | 
| ICD-10-CM | Diagnoses | A code for each documented condition, at the most specific level the documentation supports | 
| CPT | Procedures and services, including E/M visits | Procedure and service codes, including the E/M level derived from documented MDM | 
| CPT modifiers | Circumstances that change how a service is reported | Modifiers where the documentation requires them | 
| Code linkage | Medical necessity | Each CPT code linked to the ICD-10-CM codes that support it | 
| Evidence | Auditability | References to the note passages that support each code | 
| Confidence | Review prioritization | A score from 0 to 1 for each code, reflecting medical necessity, diagnosis-to-treatment alignment, and code specificity | 

## What medical coding optimizes for
<a name="mc-what-it-optimizes"></a>


| Objective | How it is measured or delivered | 
| --- | --- | 
| Code accuracy | Suggested codes are evaluated against the codes that professional coders assigned for the same encounters. | 
| Claim-ready completeness | Diagnosis and procedure codes are generated together and linked, the way they are submitted on a claim. | 
| Traceability | Every code carries the documentation evidence a coder or auditor needs to validate it. | 
| Workflow fit | Structured JSON output works at the point of care, in a coder’s workbench, or in an automated pipeline. See [Integrating medical coding into your workflows](mc-integration.md). | 

## Specialty scope and model performance
<a name="mc-specialty-scope"></a>

Medical coding is optimized for primary care office and telehealth encounters coded with E/M services. Documentation from other specialties can be submitted, but suggestions for those specialties may be less accurate and should be reviewed with particular care. Medical coding generates professional codes for outpatient encounters. Inpatient facility coding, such as ICD-10-PCS procedure codes and DRG assignment, is not supported.

Two factors have the largest effect on coding accuracy:
+  **Encounter and patient context.** The `encounterContext` and `patientContext` request fields are optional, but they are important for optimal performance. The type and setting of the visit, and the patient’s status and demographics, directly affect which codes apply. Provide them whenever you have the data. See [How context affects code selection](mc-inputs.md#mc-input-context-impact).
+  **Your specialty and code distribution.** Health systems differ in the codes they bill most and the documentation styles they use. Your AWS account team can adapt the model to your organization by using your target code list or historical coding samples, and can work with you to assess and improve performance for specialties other than primary care.

## Medical coding topics
<a name="mc-topics"></a>


| Topic | What you’ll learn | 
| --- | --- | 
|  [Getting started with medical coding](mc-getting-started.md)  | Run your first coding job end to end | 
|  [How medical coding works](mc-how-it-works.md)  | How codes are derived from documentation, and the asynchronous job lifecycle | 
|  [Medical coding inputs](mc-inputs.md)  | An example request, the clinical text, the encounter and patient context that drive code selection, and validation rules | 
|  [Medical coding outputs](mc-outputs.md)  | An example response, the code set, linkage, evidence, and confidence, and where results are written | 
|  [Integrating medical coding into your workflows](mc-integration.md)  | Point of care coding, computer-assisted coding, and autonomous coding | 
|  [Troubleshooting medical coding](mc-troubleshooting.md)  | Errors and job-status issues, and how to resolve them | 