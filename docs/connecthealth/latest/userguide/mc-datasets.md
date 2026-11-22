

# Creating and managing medical coding datasets

A medical coding dataset holds your organization’s coded encounters as reference data for site-specific coding. You manage datasets with four operations: `CreateDataset`, `GetDataset`, `ListDatasets`, and `DeleteDataset`. Each dataset belongs to one domain. For more information about site-specific coding, see [Site-specific medical coding](mc-site-specific.md).

Datasets are immutable. You can’t change a dataset’s input or output locations after you create it, and there is no update operation. New data means a new dataset.

For the full request and response syntax, see [CreateDataset](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_CreateDataset.html), [GetDataset](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_GetDataset.html), [ListDatasets](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_ListDatasets.html), and [DeleteDataset](https://docs.aws.amazon.com/connecthealth/latest/APIReference/API_DeleteDataset.html) in the *Amazon Connect Health API Reference*. In the AWS SDKs, these operations are on the `ConnectHealth` client. In the AWS CLI, they’re `aws connecthealth create-dataset`, `get-dataset`, `list-datasets`, and `delete-dataset`.

**Topics**
+ [Dataset lifecycle](#mc-ds-lifecycle)
+ [Required permissions](#mc-ds-permissions)
+ [Create a dataset](#mc-ds-create)
+ [Check a dataset’s status](#mc-ds-get)
+ [Review evaluation results](#mc-ds-evaluation)
+ [Use a dataset in a coding job](#mc-ds-use)
+ [List datasets](#mc-ds-list)
+ [Replace a dataset with new data](#mc-ds-replace)
+ [Delete a dataset](#mc-ds-delete)

## Dataset lifecycle
<a name="mc-ds-lifecycle"></a>

A dataset’s `status` field shows where it is in its lifecycle. `CreateDataset` returns a dataset in `CREATING`. The dataset then moves to `ACTIVE` or `CREATE_FAILED`. When you delete a dataset from `ACTIVE`, `CREATE_FAILED`, or `DELETE_FAILED`, it moves to `DELETING`. It then moves to `DELETED` or `DELETE_FAILED`.


|  `status`  | Meaning | What you can do | 
| --- | --- | --- | 
|  `CREATING`  | The service is building the dataset. | Poll `GetDataset`. You can’t delete the dataset in this state. | 
|  `ACTIVE`  | The dataset is ready. Coding jobs can use it. | Use it in coding jobs, review its evaluation scores, or delete it. | 
|  `CREATE_FAILED`  | The build failed, and nothing usable was built. `statusDetails` describes the reason. | Delete the dataset. Its quota slot is freed once it reaches `DELETED`. Fix the input, and then create a new dataset. | 
|  `DELETING`  | The service is deleting the dataset and its provisioned resources. | Poll `GetDataset` or `ListDatasets` until the dataset no longer appears. | 
|  `DELETE_FAILED`  | Deletion failed partway, so some provisioned resources might remain. `statusDetails` describes the reason. | Call `DeleteDataset` again to finish. | 
|  `DELETED`  | The dataset and its provisioned resources are deleted. | None. `GetDataset` and `ListDatasets` don’t return deleted datasets. | 

Every dataset that isn’t `DELETED` counts toward your dataset quota, including datasets in `CREATING`, `CREATE_FAILED`, `DELETING`, and `DELETE_FAILED`. A quota slot is freed only when its dataset reaches `DELETED`.

For what the service stores for a dataset and what deletion removes, see [How your dataset data is stored and used](mc-site-specific.md#mc-ss-data-handling).

### How long it takes
<a name="mc-ds-timing"></a>
+  **Validation** – Problems with the input or its permissions usually move the dataset to `CREATE_FAILED` within about a minute.
+  **Build** – A dataset at the 3,000-encounter minimum typically takes about 1 hour to reach `ACTIVE`. The largest inputs, near 50,000 files or 500 MB, can take about 5 hours.
+  **Deletion** – A dataset typically reaches `DELETED` 20 to 40 minutes after `DeleteDataset`. This includes a 15-minute period that lets coding jobs already using the dataset finish.

Poll `GetDataset` about once a minute. More frequent polling doesn’t make the build finish sooner. Immediately after `CreateDataset` returns, `GetDataset` can briefly return `ResourceNotFoundException`. Treat that as still `CREATING` and keep polling.

## Required permissions
<a name="mc-ds-permissions"></a>

Dataset operations need permissions in two places. The caller needs IAM permissions for the Amazon Connect Health actions. The service also acts on Amazon S3 and AWS KMS with the caller’s credentials. So the caller also needs permissions on the S3 locations and any AWS KMS keys that encrypt them.

The following table lists the Amazon S3 and AWS KMS permissions that the caller needs for each location.


| Location | Permissions the caller needs | 
| --- | --- | 
| Input location (`config.medicalCoding.s3InputPath`) |  `s3:GetObject` and `s3:ListBucket`. If the input is encrypted with an AWS KMS key, also `kms:Decrypt`. | 
| Output location (`config.medicalCoding.s3OutputPath`) |  `s3:PutObject`. If the output is encrypted with an AWS KMS key, also `kms:GenerateDataKey`. | 
| Evaluation file (`artifacts.medicalCoding.evaluationS3Uri`) | To read the file, `s3:GetObject`. | 
| The domain’s customer managed AWS KMS key, if the domain has one | For `CreateDataset`: `kms:DescribeKey`, `kms:CreateGrant`, `kms:Decrypt`, and `kms:GenerateDataKey`. Before it copies any data, `CreateDataset` checks with your credentials that you’re allowed each operation that the dataset’s grants use. The service creates the grants on the key to encrypt the dataset, and retires them when you delete it. You can find the grants with `ListGrants`. Each grant name starts with `medical-coding-dataset-` followed by the dataset ID. | 

The input and output buckets must be owned by the account that owns the dataset, and must be in the same AWS Region as the domain. The input and output paths must not overlap.

The dataset ARN has the form `arn:aws:health-agent:<region>:<account-id>:domain/<domain-id>/dataset/<dataset-id>`. For an example policy, see [Example 8: Allow users to manage medical coding datasets and submit feedback](security-iam.md#iam-example-medical-coding-datasets).

The IAM actions are `health-agent:CreateDataset`, `health-agent:GetDataset`, `health-agent:ListDatasets`, and `health-agent:DeleteDataset`. `CreateDataset`, `GetDataset`, and `DeleteDataset` require permission on both the domain and the dataset. `ListDatasets` requires permission on the domain only.

To code against a dataset, the caller needs the `StartMedicalCodingJob` permission. No IAM permission on the dataset itself is required. The service checks that the dataset belongs to the caller’s account and to the job’s domain.

If the domain uses a customer managed AWS KMS key, the caller of `StartMedicalCodingJob` also needs `kms:Decrypt` on the key for the dataset’s storage, and `kms:ListGrants` on the key. Before a job uses the dataset, the service checks with the caller’s credentials that the caller can decrypt the dataset and that the dataset’s `-read` grant is still on the key. If you revoke that grant, disable the key, or remove the caller’s permission to use it, new coding jobs that name the dataset fail with `AccessDeniedException`. Jobs that are already running finish.

## Create a dataset
<a name="mc-ds-create"></a>

To create a dataset, call `CreateDataset`. The service copies your input once, at create time, and builds the dataset asynchronously. The request takes the following parameters.


| Parameter | Required | Description | 
| --- | --- | --- | 
|  `domainId` (request path) | Yes | The domain that the dataset belongs to. | 
|  `name`  | Yes | A human-readable name, 1 to 1,028 characters. The name can’t contain the following characters: `"` `%` `&` `'` `(` `)` `;` `<` `=` `>`. | 
|  `config.medicalCoding.s3InputPath`  | Yes | The S3 location of your coded encounters. See [Preparing coded encounters for site-specific coding](mc-ss-prepare.md). | 
|  `config.medicalCoding.s3OutputPath`  | Yes | The S3 location where the service writes the dataset’s evaluation scores. | 
|  `clientToken`  | No | A unique token for idempotent retries, 1 to 128 printable ASCII characters with no spaces. The SDKs generate one if you don’t provide it. | 

The `config` object accepts one feature member. For medical coding, that member is `medicalCoding`, and the service sets the dataset `type` to `MEDICAL_CODING`.

The following example shows a `CreateDataset` request body:

```json
{
  "name": "family-medicine-2025",
  "config": {
    "medicalCoding": {
      "s3InputPath": "s3://amzn-s3-demo-bucket/coding-datasets/family-medicine-2025/input/",
      "s3OutputPath": "s3://amzn-s3-demo-bucket/coding-datasets/family-medicine-2025/output/"
    }
  },
  "clientToken": "dataset-family-medicine-2025"
}
```

The response returns the following fields:
+  `arn` – The ARN of the dataset
+  `datasetId` – The dataset identifier, up to 64 lowercase letters and digits. The service generates it.
+  `type` – `MEDICAL_CODING` 
+  `status` – `CREATING` 
+  `createdAt` – The date and time that the dataset was created

If you exceed the dataset quota, `CreateDataset` returns `ServiceQuotaExceededException`. Datasets in `CREATE_FAILED` still count toward the quota until they reach `DELETED`. See [Dataset lifecycle](#mc-ds-lifecycle).

For the input limits that `CreateDataset` enforces, such as the minimum number of encounters and the size of the input, see [How much data to provide](mc-ss-prepare.md#mc-ss-prepare-volume).

Each domain can have up to 2 medical coding datasets. The quota isn’t adjustable. If you exceed it, the message is `A domain can have at most 2 MEDICAL_CODING datasets`.

 `CreateDataset` returns `ConflictException` if you reuse a `clientToken` with different parameters. A retry with the same `clientToken` and the same parameters returns the existing dataset. Dataset names don’t have to be unique.

 `CreateDataset` doesn’t check your Amazon S3 and AWS KMS permissions before it returns. The service checks them when it starts the build. If a check fails, the dataset moves to `CREATE_FAILED`, and `statusDetails` describes the problem. For the messages, see [Dataset issues](mc-troubleshooting.md#mc-ts-datasets).

## Check a dataset’s status
<a name="mc-ds-get"></a>

To check the build, call `GetDataset` with the domain ID and the `datasetId`. The response returns the following fields:


| Field | Description | 
| --- | --- | 
|  `arn`  | The ARN of the dataset. | 
|  `datasetId`  | The dataset identifier. | 
|  `name`  | The name that you provided at create time. | 
|  `type`  |  `MEDICAL_CODING`. | 
|  `config`  | The input and output locations that you provided at create time. | 
|  `status`  | The lifecycle status. See [Dataset lifecycle](#mc-ds-lifecycle). | 
|  `statusDetails`  | Details about the status, such as why the dataset failed to build or delete. Present only when there are details to report. | 
|  `artifacts`  | Results of the build, such as the location of the evaluation scores. Absent until the build completes. | 
|  `createdAt`  | The date and time that the dataset was created. | 
|  `updatedAt`  | The date and time that the dataset was last modified. | 

Poll `GetDataset` until `status` is `ACTIVE` or `CREATE_FAILED`. If the dataset is `DELETED`, `GetDataset` returns `ResourceNotFoundException`.

## Review evaluation results
<a name="mc-ds-evaluation"></a>

After the dataset is built, the service writes evaluation scores to `<s3OutputPath>/<datasetId>/score.json`. `GetDataset` returns the location of the file in `artifacts.medicalCoding.evaluationS3Uri`. The service writes the file with your credentials, so it’s an object in your bucket.

To produce the scores, the service sets aside 10 percent of your encounters, up to 1,000, as a test set. It codes each test note twice, once with your dataset and once with the generalized knowledge base, and compares both sets of codes with the codes you submitted. The file reports both results side by side, so you can see whether your dataset improves on the standard behavior.

The following example shows the `artifacts` object in a `GetDataset` response:

```json
{
  "artifacts": {
    "medicalCoding": {
      "evaluationS3Uri": "s3://amzn-s3-demo-bucket/coding-datasets/family-medicine-2025/output/a1b2c3d4e5f6g7h8i9j0k/score.json"
    }
  }
}
```

The file contains the following top-level fields.


| Field | Description | 
| --- | --- | 
|  `notes`  | The number of test notes. | 
|  `scoredNotes`  | The number of test notes that were scored. | 
|  `failedNotes`  | The number of test notes that couldn’t be scored, because coding or the defensibility review failed with either knowledge base. These notes are excluded from both sets of results. | 
|  `customerKnowledgeBase`  | Scores for coding with your dataset. | 
|  `generalizedKnowledgeBase`  | Scores for coding with the generalized knowledge base. | 

Each of `customerKnowledgeBase` and `generalizedKnowledgeBase` contains the following fields.


| Field | Description | 
| --- | --- | 
|  `f1Score`  | Code match, from 0 to 1. The F1 score of the suggested codes against your submitted codes, across ICD-10-CM and CPT codes together. A suggested code counts as a match when your submitted codes for the same note include it. | 
|  `defensibilityScore`  | Audit defensibility, from 0 to 1. The share of suggested codes that an automated reviewer judged defensible from the documentation, out of the codes it reviewed. Absent when the reviewer didn’t judge any codes. | 
|  `f1BySystem`  | Code match for `icd10` and `cpt` separately, each with `precision`, `recall`, `f1`, `exactMatch`, `notes`, and `codes`. Also includes `cptF1WithOneIcdCorrect`. | 
|  `defensibilityBySystem`  | Audit defensibility for `icd10` and `cpt` separately, each with `codes`, `defensible`, `notReviewed`, and `score`. | 

Low scores don’t stop the dataset from becoming `ACTIVE`. Review the scores before you use the dataset in production jobs, and compare `customerKnowledgeBase` with `generalizedKnowledgeBase` to decide whether to use it.

## Use a dataset in a coding job
<a name="mc-ds-use"></a>

To code against a dataset, include its `datasetId` in the `StartMedicalCodingJob` request. The dataset must be `ACTIVE` and in the same domain as the job. When you omit `datasetId`, the job uses the generalized knowledge base.

The following example request body uses synthetic clinical text and codes against a dataset.

```json
{
  "clientToken": "encounter-20260311-000456",
  "datasetId": "a1b2c3d4e5f6g7h8i9j0k",
  "text": "Follow-up of type 2 diabetes mellitus and hypertension; new complaint of right knee pain for three weeks. ... Total time spent on this encounter, including review of records and counseling: 30 minutes.",
  "encounterContext": {
    "encounterType": "IN_PERSON",
    "encounterReason": "Diabetes and hypertension follow-up, right knee pain",
    "afterHours": false,
    "encounterDate": "2026-03-11",
    "encounterDurationMinutes": 30
  },
  "patientContext": {
    "sex": "FEMALE",
    "status": "ESTABLISHED",
    "dateOfBirth": "1967-08-21"
  },
  "outputDataConfig": {
    "s3OutputPath": "s3://amzn-s3-demo-bucket/medical-coding/"
  }
}
```

The job runs and returns results the same way as any other coding job. For all request fields, see [Medical coding inputs](mc-inputs.md).

If the request names a dataset that can’t be used, `StartMedicalCodingJob` returns an error. It never falls back to the generalized knowledge base.


| Dataset state | Error | Message | 
| --- | --- | --- | 
| Doesn’t exist, is deleted, or is in another account or domain |  `ResourceNotFoundException`  |  `Dataset <datasetId> was not found in this domain.`  | 
|  `CREATING`  |  `ConflictException`  |  `Dataset <datasetId> is still being created. Retry when its status is ACTIVE.`  | 
|  `CREATE_FAILED`, `DELETING`, or `DELETE_FAILED`  |  `ValidationException`  |  `Dataset <datasetId> cannot be used for medical coding because its status is <status>.`  | 
| Not a medical coding dataset |  `ValidationException`  |  `Dataset <datasetId> cannot be used for medical coding.`  | 

On a domain with a customer managed AWS KMS key, `StartMedicalCodingJob` also returns `AccessDeniedException`, and doesn’t create the job, in these cases: the caller can’t decrypt the dataset, the caller lacks `kms:ListGrants` on the key, or the dataset’s `-read` grant was revoked. See [Required permissions](#mc-ds-permissions).

 `GetMedicalCodingJob` returns the `datasetId` that the job used. The field is absent when the job used the generalized knowledge base.

## List datasets
<a name="mc-ds-list"></a>

To list the datasets in a domain, call `ListDatasets`. The operation takes the following optional parameters:
+  `type` – Return only datasets of this type, such as `MEDICAL_CODING`.
+  `maxResults` – The maximum number of datasets to return in one page, from 1 to 100. The default is 100.
+  `nextToken` – The pagination token from a previous `ListDatasets` response.

The response returns an `items` array of dataset summaries, and a `nextToken` when more results are available. Each summary includes `arn`, `datasetId`, `name`, `type`, `status`, `statusDetails` (when present), `createdAt`, and `updatedAt`. `ListDatasets` doesn’t return datasets in `DELETED`.

The order of results isn’t specified. If you need a specific order, sort the results by `createdAt` in your application.

## Replace a dataset with new data
<a name="mc-ds-replace"></a>

Datasets are immutable, so you refresh reference data by creating a new dataset.

**To replace a dataset with new data**

1. Upload the updated coded encounters to a new S3 input location.

1. Call `CreateDataset` with the new input location.

1. Poll `GetDataset` until the new dataset is `ACTIVE`.

1. Review the evaluation scores for the new dataset.

1. Change your `StartMedicalCodingJob` requests to use the new `datasetId`.

1. Delete the previous dataset with `DeleteDataset`.

Because a domain can have at most 2 medical coding datasets, you need a free slot to create the new one. If the domain already has 2 datasets, including any in `CREATE_FAILED`, delete one and wait until it reaches `DELETED` before you start.

## Delete a dataset
<a name="mc-ds-delete"></a>

To delete a dataset, call `DeleteDataset` with the domain ID and the `datasetId`. The operation returns the dataset’s `arn`, `datasetId`, and `status`, which is `DELETING` once the service accepts the request.

Deletion works as follows:
+ You can delete a dataset that is `ACTIVE`, `CREATE_FAILED`, or `DELETE_FAILED`. While a dataset is `CREATING`, `DeleteDataset` returns `ConflictException`.
+  `DeleteDataset` is idempotent. A repeat call while the dataset is `DELETING` returns its current state. After the dataset is `DELETED`, a call returns `ResourceNotFoundException`.
+ If the dataset moves to `DELETE_FAILED`, call `DeleteDataset` again to finish.
+ Coding jobs that already use the dataset complete. The service rejects new jobs that name the dataset.

 `DeleteDataset` removes the resources that the service provisioned for the dataset and the service-managed copy of your encounters. It doesn’t touch the objects in your own `s3InputPath`, or the evaluation scores file in your `s3OutputPath`. Those remain until you delete them. For details, see [How your dataset data is stored and used](mc-site-specific.md#mc-ss-data-handling).