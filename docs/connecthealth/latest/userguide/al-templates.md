

# Clinical note templates
<a name="al-templates"></a>

Templates define the structure, sections, and formatting rules that the agent follows when generating clinical documentation. You must specify an output format by passing a configuration object to the `noteTemplateSettings` API parameter with every session. Ambient documentation supports two methods to specify the output format — managed templates or custom templates.

**Topics**
+ [Managed templates](#al-managed-templates)
+ [Custom templates](#al-custom-templates)
+ [Custom template limits](#al-custom-template-limits)
+ [Example customization instruction](#al-example-customization)
+ [Template best practices](#al-template-best-practices)

## Managed templates
<a name="al-managed-templates"></a>

Ambient documentation provides seven pre-built note templates. The configuration object for managed templates, `managedTemplate`, specifies the template through the `templateType` parameter. The default template is HISTORY\_AND\_PHYSICAL.


| Template | Description | Use case | 
| --- | --- | --- | 
| HISTORY\_AND\_PHYSICAL (default) | Summaries for key clinical documentation sections | General physical health encounters | 
| PHYSICAL\_SOAP | Physical health focused SOAP format | Physical health encounters using SOAP structure | 
| BEHAVIORAL\_SOAP | Behavioral health focused SOAP format | Behavioral health encounters using SOAP structure | 
| GIRPP | Progress-toward-goals format | Behavioral health — tracking patient progress | 
| BIRP | Behavioral patterns and responses format | Behavioral health — documenting behavioral patterns | 
| SIRP | Situational context of therapy format | Behavioral health — emphasizing situational context | 
| DAP | Simplified clinical documentation format | Brief or focused encounters | 

### HISTORY\_AND\_PHYSICAL sections
<a name="al-managed-template-sections"></a>


| Section | Description | 
| --- | --- | 
| CHIEF COMPLAINT | Brief description of the patient’s reason for visiting the clinician | 
| HISTORY OF PRESENT ILLNESS | Information on the patient’s illness, including severity, onset, timing, current treatments, and affected areas | 
| REVIEW OF SYSTEMS | Patient-reported evaluation of symptoms across different body systems | 
| PAST MEDICAL HISTORY | Previous medical conditions, surgeries, and treatments | 
| PAST FAMILY HISTORY | Health conditions that run in the patient’s family | 
| PAST SOCIAL HISTORY | Social life, habits, occupation, and environmental factors affecting health | 
| PHYSICAL EXAMINATION | Clinician’s findings from physical examination of body systems and vital signs | 
| DIAGNOSTIC TESTING | Results and interpretations of laboratory tests, imaging studies, and other diagnostic procedures | 
| ASSESSMENT | Clinician’s assessment of patient’s health | 
| PLAN | Clinician-recommended medical treatments, lifestyle adjustments, and further appointments | 

### PHYSICAL\_SOAP and BEHAVIORAL\_SOAP sections
<a name="al-soap-sections"></a>


| Section | Description | 
| --- | --- | 
| Subjective | The patient’s goals, experiences, and existing and past issues | 
| Objective | Data and facts about the patient | 
| Assessment | The clinician’s diagnosis of the patient’s situation | 
| Plan | Clinician-recommended next steps in treatment, including future interventions and referrals | 

**Note**  
PHYSICAL\_SOAP is optimized for physical health documentation. BEHAVIORAL\_SOAP is optimized for behavioral health documentation. Both share the same section structure.

### GIRPP sections
<a name="al-girpp-sections"></a>


| Section | Description | 
| --- | --- | 
| Goal | The identified problem, challenge, or behavior to address through treatment | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention, including participation level and feedback | 
| Progress | The clinician’s assessment of movement toward treatment goals | 
| Plan | Clinician-recommended next steps in treatment, including future interventions, homework, and referrals | 

### BIRP sections
<a name="al-birp-sections"></a>


| Section | Description | 
| --- | --- | 
| Behavior | The problems the patient presents and their response to treatment | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention | 
| Plan | Next steps in treatment | 

### SIRP sections
<a name="al-sirp-sections"></a>


| Section | Description | 
| --- | --- | 
| Situation | The problem the patient presents and their goal for seeking therapy | 
| Intervention | The specific treatment, method, or technique used by the clinician | 
| Response | How the patient responded to the intervention | 
| Plan | Clinician-recommended next steps in treatment | 

### DAP sections
<a name="al-dap-sections"></a>


| Section | Description | 
| --- | --- | 
| Data | The patient’s reasons for seeking treatment and information about the patient | 
| Assessment | The clinician’s diagnosis of the patient’s situation | 
| Plan | Clinician-recommended next steps in treatment | 

## Custom templates
<a name="al-custom-templates"></a>

Ambient documentation uses a two-layer customization model: Base and Output Specification. These two layers are managed in a configuration object, `customTemplate`. The `customTemplate` configuration object contains two parameters: `templateType` sets the Base template and `templateInstructions` contains the Output Specification.

The Base (`templateType`) sets the organization structure of the clinical facts detected during the conversation. The following base templates are supported:


| Base | Description | Use case | 
| --- | --- | --- | 
| HISTORY\_AND\_PHYSICAL | Summaries for key clinical documentation sections | General physical health encounters | 
| BEHAVIORAL\_SOAP | Behavioral health focused SOAP format | Behavioral health encounters using SOAP structure | 
| GIRPP | Progress-toward-goals format | Behavioral health — tracking patient progress | 
| BIRP | Behavioral patterns and responses format | Behavioral health — documenting behavioral patterns | 
| SIRP | Situational context of therapy format | Behavioral health — emphasizing situational context | 
| DAP | Simplified clinical documentation format | Brief or focused encounters | 

**Note**  
The custom-template base type list does not include PHYSICAL\_SOAP. PHYSICAL\_SOAP is available only as a managed template. If you pass it as a custom `templateType`, the request is rejected with a validation error.

The Output Specification object (`templateInstructions`) is organized as an array of instructions, with a `sectionHeader` that defines the section name and `sectionInstruction` that combines instructions and a template for that section.

## Custom template limits
<a name="al-custom-template-limits"></a>

The following limits apply to custom templates.

 **Number of section instructions** (`templateInstructions`, required)


| Property | Value | 
| --- | --- | 
| Minimum | 1 section instruction | 
| Maximum | 20 section instructions | 
| What happens if you exceed it | A request with 0 sections, or with more than 20, is rejected. If you need more than 20 logical sections, consolidate related content into a single section instruction. | 

Each section instruction is also size-limited individually — see **Section instruction** below.

 **Section header** (`sectionHeader`, required)


| Property | Value | 
| --- | --- | 
| Type | String | 
| Supported characters | Alphanumeric only (`A-Z`, `a-z`, `0-9`). No spaces, underscores, or punctuation. For example, use `ChiefComplaint` or `PhysicalExam`, not `Chief Complaint` or `Physical_Exam`. | 
| Pattern |  `^[a-zA-Z0-9]+$`  | 

 **Section instruction** (`sectionInstruction`, required)


| Property | Value | 
| --- | --- | 
| Type | String | 
| Maximum size | 15 KB (15,360 bytes) per section instruction, measured on the UTF-8 byte length. The limit applies to each section instruction individually, not to the template as a whole. | 
| Supported characters | The same set as encounter context (see [Character support](al-patient-context.md#al-encounter-context-character-support)) | 
| Pattern | \+^[\\p{L}\\p{N}\\s\\\*\_\\-\#\\[\\]\\(\\)\\.,:;\!?'"`<>\~/ | 

**Tip**  
Because the supported set includes `{`, `}`, `[`, `]`, and `|`, you can describe a structured output — such as a JSON object or a Markdown table — directly in a section instruction. When you do, state the exact keys or columns you want and instruct the model to return only that structure.

Customization instructions can include three types of directives:
+  **Verbosity instructions** — Control content conciseness or elaboration. Example: "Describe the chief complaint in 1 sentence or less."
+  **Template usage instructions** — Direct how the agent handles misalignment between the template and the encounter content. Example: "Follow the template exactly: if requested data is unavailable, write INFORMATION NOT FOUND."
+  **Style instructions** — Specify formatting, terminology, and reasoning requirements. Example: "Use numbered problems in the Assessment section."

Templates can be provided as text with placeholders, structured JSON schemas, or example previous notes.


| Method | Description | Use when | 
| --- | --- | --- | 
| Text template with placeholders | A template with section headers and placeholder fields (such as <chief\_complaint>) that the agent fills from the encounter | You want precise control over section layout and content placement | 
| Structured JSON template | A JSON schema defining fields, nesting, and per-field formatting rules | Your EHR requires structured data output rather than prose | 
| Example previous note | A prior clinical note provided as a reference for the desired format and style | A provider wants notes that match their existing documentation patterns | 

**Note**  
The service is stateless. To use a previous note as a style reference, your application must include it in the instructions for each session. The agent does not retain provider preferences across sessions.

## Example customization instruction
<a name="al-example-customization"></a>

The following example shows a customization instruction for a SOAP note using the `customTemplate` configuration object.

```
{
  "clinicalNoteGenerationSettings": {
    "noteTemplateSettings": {
      "customTemplate": {
        "templateType": "HISTORY_AND_PHYSICAL",
        "templateInstructions": [
          {
            "sectionHeader": "Subjective",
            "sectionInstruction": "You will be generating a SOAP note one section at a time, starting with the `S` section. Please use this template when generating the `S` section:\n<template>\nSUBJECTIVE:\nChief Complaint: <Brief statement, in patient's own words, if available>\nHistory of Present Illness: <Narrative description of current symptoms, onset, duration, quality, severity, timing, context, modifying factors, associated symptoms.>\nReview of Systems:\n• Constitutional: <fever, chills, weight changes, fatigue>\n• Cardiovascular: <chest pain, palpitations, shortness of breath>\n• Respiratory: <cough, dyspnea, wheezing>\n• GI: <nausea, vomiting, diarrhea, constipation, abdominal pain>\n• GU: <dysuria, frequency, urgency, hematuria>\n• Musculoskeletal: <joint pain, muscle weakness, back pain>\n• Neurological: <headache, dizziness, numbness, weakness>\n• Psychiatric: <mood changes, anxiety, sleep disturbances>\n• All other systems negative unless noted above Past Medical History: <List chronic conditions>\nPast Surgical History: <List previous surgeries with dates>\nMedications: <Current medications with doses>\nAllergies: <Drug allergies and reactions, or NKDA>\nSocial History: <Tobacco, alcohol, drugs, occupation, living situation>\nFamily History: <Relevant family medical history>\n</template>"
          }
        ]
      }
    }
  }
}
```

## Template best practices
<a name="al-template-best-practices"></a>

Well-designed templates produce clinical notes that consistently follow your intended structure. Apply the following practices when defining custom templates:
+  **Define your note structure with named section headers.** List each section of your desired note by name, using a consistent delimiter. The model uses these headers as structural anchors to place content in the correct location.
+  **Use descriptive placeholders** that explain what content belongs in each section. For example, `Chief Complaint: <Brief statement in patient’s own words, if available>`.
+  **Enumerate expected subsections** for multi-part fields. For sections that span multiple categories (such as body systems or problem lists), list them explicitly with representative values to indicate scope.
+  **Handle missing information gracefully.** Use phrasing like "if available" or "if applicable" within placeholders to signal that a section can be omitted when the encounter does not produce relevant content.
+  **Test templates across visit types.** A template that works for follow-up visits may not suit new patient encounters or wellness exams. Validate your templates against a representative sample of encounters before deploying broadly.