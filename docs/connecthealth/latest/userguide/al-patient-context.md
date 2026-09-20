

# Encounter context
<a name="al-patient-context"></a>

Encounter context provides the agent with clinical history before the conversation through the `encounterContext` API parameter. The `encounterContext` object contains the field `unstructuredContext`, which accepts free-form text that gives the service background that isn’t spoken aloud during the visit. When you include encounter context, the agent uses it to enrich the generated documentation with background information that was not explicitly discussed during the visit. Encounter context is optional — if you omit it, the session still runs, but providing it helps the service generate a more accurate and complete note, because providers rarely restate a patient’s full history out loud.

Encounter context can include:
+ Prior encounter notes and visit summaries
+ Active medication lists
+ Problem lists and diagnoses
+ Allergies and immunizations
+ Relevant lab and imaging reports
+ Surgical and family history
+ Patient’s preferred pronouns, used when referring to the patient in generated clinical output
+ The reason for the visit and any pre-visit notes

You provide this text once per session, in the configuration event. It applies to the whole session.

**Tip**  
If you have more source data than fits, prioritize. Send the highest-value, most current information first (active problems, current medications, reason for visit) and trim verbose or historical free text. Summarizing long narrative history into concise bullet points is usually more effective than sending everything.

**Topics**
+ [Size limit](#al-encounter-context-size-limit)
+ [Character support](#al-encounter-context-character-support)
+ [Sanitize before you send](#al-encounter-context-sanitize)
+ [Formatting context as Markdown](#al-encounter-context-markdown)

## Size limit
<a name="al-encounter-context-size-limit"></a>


| Property | Value | 
| --- | --- | 
| Maximum size | 20 KB (20,480 bytes) of text per session | 
| How the limit is measured | UTF-8 byte length of the string, not the number of characters you see — accented and non-Latin characters use two or more bytes each | 
| What happens if you exceed it | The session request is rejected with a validation error, and the session does not start | 

For example, the word `José` is 4 characters but 5 bytes in UTF-8 (the `é` is two bytes). A context block full of accented patient names, non-Latin text, or symbols reaches the 20 KB ceiling with fewer visible characters than an all-ASCII block. When you are near the limit, count bytes, not characters.

**Note**  
20 KB is the default limit. If your workload consistently needs more context per session, contact your AWS account team to discuss your requirements.

## Character support
<a name="al-encounter-context-character-support"></a>

 `unstructuredContext` accepts a broad, Unicode-aware set of characters so that you can pass realistic clinical text, including international patient names and common medical notation.


| Property | Value | 
| --- | --- | 
| Type | String | 
| Required | No | 
| Pattern | \+^[\\p{L}\\p{N}\\s\\\*\_\\-\#\\[\\]\\(\\)\\.,:;\!?'"`<>\~/ | 

 **Supported characters:** 
+ Unicode letters, including accented and non-Latin characters (for example, José, Müller, 施)
+ Unicode digits
+ Whitespace
+ The following punctuation and symbols: \* \_ - \# [ ] ( ) . , : ; \! ? ' " ` > \~ / \| \+ = % @ \\ { } ^

The entire string must match the pattern. A single unsupported character anywhere in the string causes the whole context to be rejected.


| Input | Result | Why | 
| --- | --- | --- | 
|  `Patient reports 2 partners + is sexually active.`  | Valid |  `+` and `.` are supported | 
|  `BP 120/80; HR 72. Allergies: penicillin (rash).`  | Valid |  `/ ; . : ( )` are all supported | 
|  `Weight loss ~5 kg over 3 months`  | Valid |  `~` is supported | 
|  `Follow-up in 2–3 weeks`  | Invalid |  `–` is an en dash, not the supported hyphen `-`  | 
|  `Temp 38°C`  | Invalid |  `°` (degree sign) is not in the supported set | 
|  `Cost was €40`  | Invalid |  `€` is not in the supported set | 

## Sanitize before you send
<a name="al-encounter-context-sanitize"></a>

If your source system (for example, an EHR) can emit characters outside the supported set, sanitize the text before you submit it. Common strategies:
+  **Map to a supported equivalent** — replace an en dash `–` or em dash `—` with a hyphen `-`, replace smart quotes `“ ”` with straight quotes `" "`, and replace `°` with the word `degrees`.
+  **Convert currency symbols** — currency symbols such as `£`, `€`, `$`, and `¥` are not supported. Replace them with the currency code or word — for example, `£40` → `GBP 40` or `40 pounds`, `€40` → `EUR 40`.
+  **Drop unsupported characters** — remove any character that isn’t in the supported set. This is simple but can lose meaning, so prefer mapping where the character matters.

 **Before / after** 

```
Before:  Temp 38°C, follow-up in 2–3 weeks — see notes.
After:   Temp 38 degrees C, follow-up in 2-3 weeks - see notes.
```

## Formatting context as Markdown
<a name="al-encounter-context-markdown"></a>

The supported set includes the `|`, `#`, `*`, `[`, `]`, `(`, `)`, `{`, and `}` characters, so you can format context as Markdown — including headings, lists, and tables — to present structured information clearly. For example, a medication list as a Markdown table:

```
## Current medications

| Medication | Dose   | Frequency   |
| ---------- | ------ | ----------- |
| Lisinopril | 10 mg  | Once daily  |
| Metformin  | 500 mg | Twice daily |
```

**Note**  
The following example uses fictional patient data for illustration purposes only.

 **Example encounter context** 

```
## Patient Information
Name: Patricia Underwood
Age: 28 years
Sex: female
Pronouns: she/her
MEDICATIONS:
Ondansetron 4mg PO PRN - Nausea/vomiting
Dicyclomine 20mg PO BID PRN - Abdominal cramping
Sertraline 50mg PO daily - Depression
Ferrous sulfate 325mg PO TID - Iron deficiency anemia
ALLERGIES: NKDA (No Known Drug Allergies)
PAST MEDICAL HISTORY:
Brainstem pilocytic astrocytoma diagnosed 04/2010
Posterior fossa craniotomy with gross total resection 05/12/2010
Hyperprolactinemia diagnosed 08/2013
Autoimmune hemolytic anemia diagnosed 12/2012
Splenomegaly secondary to autoimmune hemolytic anemia 01/2013
Major depressive disorder diagnosed 08/2012
Substance use disorder (heroin) in sustained remission since 04/2011
Tobacco use disorder, quit 09/15/2013 (10 pack-year history)
Iron deficiency anemia diagnosed 01/2013
Gastroesophageal reflux disease diagnosed 05/2013
Appendectomy 07/23/2009 (uncomplicated laparoscopic)
Wisdom teeth extraction 11/08/2008
FAMILY HISTORY:
Maternal grandmother: Cervical cancer, ovarian cancer, dementia/Alzheimer's
Maternal aunt: Cervical cancer
Paternal grandfather: Type 2 diabetes, hypertension, kidney transplant
Maternal great-grandfather: Colon cancer
Multiple maternal great-uncles: Colon cancer
No family history of breast, uterine, or cardiac disease
SOCIAL HISTORY:
Tobacco: Former smoker, quit 09/15/2013 (10 pack-year history)
Alcohol: Not documented
Illicit drugs: History of IV heroin use, abstinent since 04/2011, occasional marijuana use
Sexual history: Single, sexually active, monogamous relationship since 05/2012
Previous relationship with military personnel ended 03/2012
Employment: Lives independently, employed
Contraception: Not currently using
Former plasma donor, discontinued 10/2013 due to positive syphilis screening
PROBLEM LIST:
History of brainstem pilocytic astrocytoma (C71.7) - Diagnosed 04/2010 with posterior fossa craniotomy and gross total resection 05/12/2010. Annual MRI surveillance shows post-surgical changes, no residual tumor. Most recent MRI 10/18/2013 normal. Followed by neurology with annual visits.
Hyperprolactinemia (E22.1) - Diagnosed 08/2013 with prolactin 45.2 ng/mL (normal 25). Referred to neurology for pituitary evaluation. Recent MRI 10/18/2013 shows normal pituitary gland. Not currently on treatment. Neurology follow-up scheduled.
Autoimmune hemolytic anemia with splenomegaly (D59.1) - Diagnosed 12/2012-01/2013. Positive direct Coombs test, elevated LDH 420 U/L, low haptoglobin 10 mg/dL, reticulocyte count 8.2%. Associated splenomegaly. Managed by primary care physician. On iron supplementation for concurrent iron deficiency.
Major depressive disorder, mild (F32.0) - Diagnosed 08/2012. Started sertraline 50mg daily 09/08/2012 with good response. Stable mood, no current suicidal ideation. Continues on current regimen.
Substance use disorder (heroin), in sustained remission (F11.21) - History of IV drug use, abstinent since 04/2011. Not currently in formal treatment program. Maintains abstinence, occasional marijuana use.
Iron deficiency anemia (D50.9) - Diagnosed 01/2013 concurrent with autoimmune hemolytic anemia. Started ferrous sulfate 325mg TID 01/14/2013. Recent Hgb 9.8 g/dL, Hct 29%, MCV 102 fL.
Gastroesophageal reflux disease (K21.9) - Diagnosed 05/2013. Managed with lifestyle modifications. Symptoms of nausea and vomiting, taking ondansetron and dicyclomine PRN.
RECENT LABS (Various dates 2013):
Prolactin: 45.2 ng/mL (08/22/2013, elevated)
CBC: Hgb 9.8, Hct 29%, MCV 102 fL (10/28/2013)
Direct Coombs: Positive (01/14/2013)
LDH: 420 U/L, Haptoglobin 10 mg/dL (01/14/2013)
MRI brain with contrast: Normal pituitary, post-surgical changes only (10/18/2013)
Pap smear: Normal cytology, HPV negative (11/15/2012)
Mammogram: BI-RADS 1, normal (02/28/2013)
```