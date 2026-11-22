

# Preparing coded encounters for site-specific coding

A site-specific dataset is built from historical encounters that your organization has already coded. Each encounter is a finalized clinical note together with the codes that were submitted for it. The service uses these encounters as reference examples, so their quality directly affects the suggested codes.

**Topics**
+ [Choose the scope](#mc-ss-prepare-scope)
+ [How much data to provide](#mc-ss-prepare-volume)
+ [What each encounter contains](#mc-ss-prepare-contents)
+ [Input file format](#mc-ss-prepare-format)
+ [Data quality](#mc-ss-prepare-quality)
+ [Hold out test encounters](#mc-ss-prepare-test)
+ [What to leave out](#mc-ss-prepare-exclude)
+ [Keep reference data current](#mc-ss-prepare-current)

## Choose the scope
<a name="mc-ss-prepare-scope"></a>

Assemble encounters for one care setting and specialty at a time. Use the following guidelines to choose them.


| Item | Guideline | 
| --- | --- | 
| Care setting | One care setting, such as ambulatory or outpatient | 
| Specialty | One specialty, such as family medicine | 
| Code systems | CPT, including modifiers, and ICD-10-CM | 
| Time window | The most recent 2 years, so that the coding follows current CPT and ICD-10-CM guidelines | 

## How much data to provide
<a name="mc-ss-prepare-volume"></a>

 `CreateDataset` enforces the following limits on the encounters at your `s3InputPath`. The limits apply to the dataset as a whole. The service doesn’t identify the specialty of an encounter, so if a dataset covers more than one specialty, the minimum still applies to the dataset and not to each specialty in it.


| Limit | Value | Notes | 
| --- | --- | --- | 
| Minimum valid encounters | 3,000 | A dataset with fewer encounters fails during validation, with a `statusDetails` message of the form `s3InputPath has <count> encounters; at least 3000 are required`. | 
| Maximum encounters | No fixed limit | The total size, file count, and per-note limits apply instead. | 
| Total input size | 500 MB | Across all files under `s3InputPath`. | 
| Maximum files | 50,000 | Across all files under `s3InputPath`. | 
| Maximum note size | 100 KB | Per clinical note. | 

The service holds out 10 percent of your encounters, up to 1,000, as a test set. It codes those encounters and compares the results with your submitted codes to produce the evaluation scores. The held-out encounters aren’t used as reference examples. See [Review evaluation results](mc-datasets.md#mc-ds-evaluation).

## What each encounter contains
<a name="mc-ss-prepare-contents"></a>

Each encounter needs the clinical note and its final submitted codes. Patient and visit context measurably improves accuracy, so include it wherever you have it.


| Component | Details | Requirement | 
| --- | --- | --- | 
| Clinical note | The finalized, documented encounter note | Required | 
| Final submitted codes | The ICD-10-CM diagnosis codes and CPT procedure codes, with modifiers, that were submitted for the encounter | Required | 
| CPT to ICD-10-CM linkage | For each CPT code, the ICD-10-CM diagnosis codes that justify the procedure | Required | 
| Patient context | Age or date of birth, sex, insurance, and patient status (new or established) | Strongly preferred | 
| Visit context | Visit type (in person or telehealth), reason for visit, visit date, whether the encounter was after hours, and the encounter duration in minutes | Strongly preferred | 

The context fields in the preceding table are the ones the service reads. Place of service, provider specialty, and procedure global period aren’t read today, so don’t spend effort collecting them for a dataset. For the exact field names, see [Input file format](#mc-ss-prepare-format).

Use the final, submitted codes for each encounter, not draft or pre-scrubber codes. The CPT to ICD-10-CM linkage and the CPT modifiers matter in particular. Together, they capture which diagnosis supports each billed procedure. This is the pattern the service looks for in your reference examples.

## Input file format
<a name="mc-ss-prepare-format"></a>

Every object under `s3InputPath` must be a JSON or JSON Lines file of encounter records. The service validates all of them before it builds the dataset. The following table lists the requirements.


| Item | Requirement | 
| --- | --- | 
| File types |  `.json`, holding either one encounter record or an array of records, or `.jsonl`, holding one record per line. Any other file under `s3InputPath` fails the dataset. | 
| Files that are skipped | Files whose names begin with a period (`.`) or an underscore (`_`), such as `_SUCCESS` or `.DS_Store`, and the zero-byte folder markers that the Amazon S3 console creates. | 
| Storage class | Objects in an archive storage class fail validation until you restore them. | 
| Validation | All or nothing. A single invalid record fails the whole dataset. `statusDetails` reports a count for each problem it found, such as `3 with no note`, not the individual records. | 

The following example shows one encounter record:

```json
{
  "note": "...finalized clinical note text...",
  "icd-10-cm": [
    { "code": "J45.909" }
  ],
  "cpt": [
    {
      "code": "99214",
      "modifiers": ["25"],
      "linked_icd_codes": ["J45.909"]
    }
  ],
  "context": {
    "age": 54,
    "sex": "F",
    "patient_status": "established",
    "visit_type": "in-person",
    "visit_date": "2024-06-14",
    "encounter_reason": "Asthma follow-up",
    "after_hours": false,
    "encounter_duration_minutes": 25,
    "insurance": "Medicare"
  }
}
```

The following fields are required in every record:
+  `note` – The finalized clinical note text, up to 100 KB.
+  `icd-10-cm` – At least one ICD-10-CM code.
+  `cpt` – At least one CPT code.
+  `linked_icd_codes` – Required on every CPT code. Each linked code must also appear in the same record’s `icd-10-cm` list. The service compares codes with and without the decimal point, so `J45.909` and `J45909` match.

The `context` object and all of its fields are optional. For the patient’s age, you can provide `age` or `date_of_birth` (`YYYY-MM-DD`). If a record has both, the service uses `date_of_birth`.

Because a single invalid value fails the whole dataset, check each record against the following rules:
+  **CPT codes** – Four digits followed by a digit, `F`, or `T`. This covers Category I, II, and III codes.
+  **ICD-10-CM codes** – A letter, a digit, and a letter or digit, followed by up to 4 more letters or digits. The dot is optional, and case is ignored.
+  **Modifiers** – Two characters, each a letter or a digit.
+  ** `age` ** – A whole number from 0 to 130.
+  ** `encounter_reason` and `insurance` ** – Text that isn’t blank.
+  ** `after_hours` ** – A Boolean value.
+  ** `encounter_duration_minutes` ** – A whole number, 0 or greater.
+  ** `visit_date` and `date_of_birth` ** – Dates in `YYYY-MM-DD` format.

An invalid `context` value is reported in `statusDetails` as `with an invalid context value`.

**Important**  
In a dataset file, `visit_type` is `in-person` or `telehealth`, and `patient_status` is `new` or `established`, in any case. Note the hyphen in `in-person`. The `StartMedicalCodingJob` value `IN_PERSON` isn’t accepted. Dates use the `YYYY-MM-DD` format in both.

A dataset contains coded encounters only. You can’t add coding policy documents, such as house rules or documentation conventions, to a dataset.

## Data quality
<a name="mc-ss-prepare-quality"></a>

Before you create a dataset, check that your encounters meet the following expectations:
+  **Complete codes.** Each encounter includes its full set of final submitted codes.
+  **Linkage present.** Each CPT code carries its linked ICD-10-CM diagnosis codes.
+  **Complete notes.** Each note is the finalized documented note, not a partial draft.
+  **Representative mix.** The encounters reflect the normal mix of visits for the specialty. Don’t hand-pick a subset of unusual or difficult cases.
+  **No test overlap.** Encounters that you hold out for testing don’t also appear in the dataset.

## Hold out test encounters
<a name="mc-ss-prepare-test"></a>

To measure accuracy before you rely on a dataset, keep a separate set of test encounters. After the dataset is `ACTIVE`, run coding jobs on the test notes with the `datasetId`. Then compare the suggested codes with the final submitted codes. The test encounters should meet the following conditions:
+ They come from the same care setting and specialty as the dataset.
+ They fall within the same time window, the most recent 2 years.
+ They contain the same components as the dataset encounters.
+ They don’t overlap with the encounters in the dataset.

The service also produces its own evaluation scores, from the 10 percent of your input that it holds out at create time. See [How much data to provide](#mc-ss-prepare-volume). Your own test encounters serve a different purpose: they let you measure accuracy on encounters the service never received, through the same API path your application uses. Keep them out of `s3InputPath`.

## What to leave out
<a name="mc-ss-prepare-exclude"></a>

Don’t include substance use disorder treatment records covered by 42 CFR Part 2 without first discussing them with your AWS account team. These records carry restrictions beyond HIPAA, so they need separate handling.

## Keep reference data current
<a name="mc-ss-prepare-current"></a>

Your coding conventions continue to evolve after you start using a dataset. Periodically refresh your reference data with recently coded encounters. Datasets are immutable, so to refresh, you create a new dataset and point your jobs at it. For instructions, see [Replace a dataset with new data](mc-datasets.md#mc-ds-replace).