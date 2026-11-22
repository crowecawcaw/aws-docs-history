

# Site-specific medical coding

Coding isn’t fully deterministic. Two experienced coders can reach different, defensible answers for the same note, and every organization develops its own consistent conventions. Site-specific coding lets medical coding take your organization’s conventions into account.

**Topics**
+ [How site-specific coding works](#mc-ss-how-it-works)
+ [How your dataset data is stored and used](#mc-ss-data-handling)
+ [Key concepts](#mc-ss-concepts)
+ [Workflow](#mc-ss-workflow)
+ [Scope](#mc-ss-scope)
+ [Related topics](#mc-ss-related)

## How site-specific coding works
<a name="mc-ss-how-it-works"></a>

Site-specific coding works by reference, not by training. You provide historical encounters that your organization has already coded, and medical coding builds a dataset from them. When a coding job uses that dataset, the service looks up similar encounters in it. It then uses them as examples alongside the note that it codes.

You choose the dataset for each job. In `StartMedicalCodingJob`, the optional `datasetId` field names an `ACTIVE` dataset in your domain. When you omit `datasetId`, the job uses the generalized knowledge base, which is the standard medical coding behavior. To return to the standard behavior, start jobs without a `datasetId`.

## How your dataset data is stored and used
<a name="mc-ss-data-handling"></a>

Site-specific coding doesn’t train or fine-tune a model on your encounters. The underlying model isn’t changed by your data. Your encounters are used only as reference examples, and only for the jobs that name the dataset they belong to. If you delete the dataset, or start jobs without a `datasetId`, coding returns to the standard behavior.

The following table describes how the service handles your dataset data.


| Stage | What the service does | 
| --- | --- | 
| Create |  `CreateDataset` copies the encounters at your `s3InputPath` once, into a service-managed Amazon S3 location in the same AWS Region as your domain. The copy is isolated per domain, with a separate location for each dataset. The service then divides the copy into notes, codes, and a held-out test set, and builds a knowledge base for the dataset. The knowledge base stores the note text alongside the vector embeddings generated from it. | 
| Encrypt | If your domain uses a customer managed AWS KMS key, the service-managed copy and the dataset’s knowledge base are encrypted with that key. The service creates the AWS KMS grants it needs on the key, and retires them when you delete the dataset. | 
| Use | At coding time, only jobs that name this `datasetId`, in the same domain, retrieve from the dataset. The service retrieves similar encounters and their codes and adds them to the model prompt as examples. Datasets aren’t shared across domains, and a job never retrieves from a dataset it didn’t name. | 
| Delete |  `DeleteDataset` deletes the dataset’s knowledge base, its provisioned search resources, and every version of every object in the service-managed copy. It then retires the AWS KMS grants. Your own `s3InputPath` objects and the evaluation scores in your `s3OutputPath` aren’t touched. | 

For the Amazon Connect Health opt-out policy for service improvement, see [Service improvement and how to opt out](data-protection.md#service-improvement).

## Key concepts
<a name="mc-ss-concepts"></a>

The following terms describe site-specific coding.


| Term | Description | 
| --- | --- | 
| Dataset | A resource in your domain that holds your coded encounters for one Amazon Connect Health feature. For site-specific coding, the dataset type is `MEDICAL_CODING`. | 
| Coded encounter | A finalized clinical note together with the codes that were submitted for it, the CPT to ICD-10-CM linkage, and patient and visit context where available. | 
| Generalized knowledge base | The reference knowledge that a coding job uses when the request doesn’t include a `datasetId`. | 
| Evaluation scores | A JSON file that the service writes to your output location after it builds a dataset. The scores measure code match and audit defensibility. | 

## Workflow
<a name="mc-ss-workflow"></a>

The following table shows the end-to-end workflow for site-specific coding.


| Step | What you do | 
| --- | --- | 
| 1. Prepare encounters | Collect finalized notes and their submitted codes for one care setting and specialty. See [Preparing coded encounters for site-specific coding](mc-ss-prepare.md). | 
| 2. Upload to Amazon S3 | Put the encounters in an S3 location that the caller can read. | 
| 3. Create a dataset | Call `CreateDataset` with the S3 input location and an S3 output location for evaluation scores. See [Create a dataset](mc-datasets.md#mc-ds-create). | 
| 4. Wait for the build | Call `GetDataset` until the dataset status is `ACTIVE` or `CREATE_FAILED`. | 
| 5. Review evaluation scores | Read the evaluation file at `artifacts.medicalCoding.evaluationS3Uri`. See [Review evaluation results](mc-datasets.md#mc-ds-evaluation). | 
| 6. Code against the dataset | Include the `datasetId` in `StartMedicalCodingJob` requests. See [Use a dataset in a coding job](mc-datasets.md#mc-ds-use). | 
| 7. Refresh with new data | Create a new dataset from updated encounters, and point jobs at it. Datasets are immutable. See [Replace a dataset with new data](mc-datasets.md#mc-ds-replace). | 

## Scope
<a name="mc-ss-scope"></a>

Set up site-specific coding one care setting and specialty at a time, because each benefits from its own set of examples. Datasets cover CPT codes, including modifiers, and ICD-10-CM codes.

You can build a dataset for any specialty. The service doesn’t check the specialty or care setting of your encounters, so a single dataset can contain more than one. We recommend one dataset per care setting and specialty, because each benefits from its own examples. Keep in mind that each domain can have at most 2 medical coding datasets.

## Related topics
<a name="mc-ss-related"></a>

For more information, see the following topics:
+  [Preparing coded encounters for site-specific coding](mc-ss-prepare.md) 
+  [Creating and managing medical coding datasets](mc-datasets.md) 
+  [Submitting feedback on medical codes](mc-feedback.md) 