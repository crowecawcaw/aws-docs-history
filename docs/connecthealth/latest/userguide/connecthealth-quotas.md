

# Quotas for Amazon Connect Health

Amazon Connect Health enforces service quotas that govern how AI agents operate within your deployment. These include limits on patient engagement configuration and runtime, such as decision tree and knowledge base file sizes, visit-type restrictions, and escalation thresholds. For these limits, see [Patient engagement](patient-engagement-overview.md). These quotas help keep the service stable and performance consistent across customers.

If your operational scale requires higher limits, for example for health systems with high concurrent call volumes, you can submit limit increase requests through AWS Support.

In addition to Amazon Connect Health quotas, you are also subject to the default [service quotas of Amazon Connect Customer](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html). If you are deploying at scale, review and request increases for Amazon Connect Customer service quotas as needed.

## Service quotas
<a name="quotas-service-quotas"></a>

The following quotas apply to Amazon Connect Health resources.


| Quota name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Concurrent streaming sessions | 10 | Yes | The maximum number of concurrent streaming sessions for Ambient Streaming per account. | 
| Concurrent Patient Insight jobs | 25 | Yes | The maximum number of concurrent Patient Insight jobs per domain. | 
| Domains per account | 10 | No | The maximum number of domains per account. | 
| Medical coding datasets per domain | 2 | No | The maximum number of medical coding datasets per domain. Every dataset that isn’t `DELETED` counts, including datasets in `CREATE_FAILED`. | 
| Encounters per medical coding dataset | 3,000 minimum | No | The minimum number of valid coded encounters required to build a site-specific medical coding dataset. There is no fixed maximum. See [How much data to provide](mc-ss-prepare.md#mc-ss-prepare-volume). | 
| Input size per medical coding dataset | 500 MB | No | The maximum total size of the encounter files at `s3InputPath`. | 
| Input files per medical coding dataset | 50,000 | No | The maximum number of encounter files at `s3InputPath`. | 
| Clinical note size in a medical coding dataset | 100 KB | No | The maximum size of a single clinical note in a dataset encounter record. | 

## Patient engagement
<a name="connecthealth-pe-quotas"></a>

The following quotas apply to patient engagement agents and their configuration.


| Quota name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Decision tree file size | 4 MB | No | The maximum size of a decision tree PDF file per capability. | 
| Knowledge base file size | 50 MB | No | The maximum size of a knowledge base document per file. | 
| Visit types for cancellation and rescheduling | 100 | No | The maximum number of visit types in the cancellation and rescheduling allow list per capability. | 
| Escalation threshold range | 2 | No | The number of retries, and the number of off-topic redirects, before the agent escalates. Each threshold accepts a value from 1 to 10 and defaults to 2. | 

## API throttling quotas
<a name="quotas-api-throttling-quotas"></a>

The following table lists the default API throttling quotas for Amazon Connect Health, measured in transactions per second (TPS) per account and AWS Region.


| Quota name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
|  `StartMedicalScribeListeningSession`  | 2 | Yes | The maximum number of `StartMedicalScribeListeningSession` requests per second. | 
|  `GetMedicalScribeListeningSession`  | 10 | Yes | The maximum number of `GetMedicalScribeListeningSession` requests per second. | 
|  `StartPatientInsightsJob`  | 5 | Yes | The maximum number of `StartPatientInsightsJob` requests per second. | 
|  `GetPatientInsightsJob`  | 10 | Yes | The maximum number of `GetPatientInsightsJob` requests per second. | 
|  `StartMedicalCodingJob`  | 5 | Yes | The maximum number of `StartMedicalCodingJob` requests per second. To request an increase, contact your AWS account team. | 
|  `GetMedicalCodingJob`  | 10 | Yes | The maximum number of `GetMedicalCodingJob` requests per second. To request an increase, contact your AWS account team. | 
|  `CreateDataset`  | 5 | Yes | The maximum number of `CreateDataset` requests per second. To request an increase, contact your AWS account team. | 
|  `GetDataset`  | 10 | Yes | The maximum number of `GetDataset` requests per second. To request an increase, contact your AWS account team. | 
|  `ListDatasets`  | 10 | Yes | The maximum number of `ListDatasets` requests per second. To request an increase, contact your AWS account team. | 
|  `DeleteDataset`  | 5 | Yes | The maximum number of `DeleteDataset` requests per second. To request an increase, contact your AWS account team. | 
|  `SubmitFeedback`  | 5 | Yes | The maximum number of `SubmitFeedback` requests per second. To request an increase, contact your AWS account team. | 
|  `ListDomain`  | 5 | Yes | The maximum number of `ListDomain` requests per second. | 
|  `GetDomain`  | 5 | Yes | The maximum number of `GetDomain` requests per second. | 
|  `CreateDomain`  | 1 | Yes | The maximum number of `CreateDomain` requests per second. | 
|  `DeleteDomain`  | 1 | Yes | The maximum number of `DeleteDomain` requests per second. | 
|  `CreateSubscription`  | 1 | Yes | The maximum number of `CreateSubscription` requests per second. | 
|  `GetSubscription`  | 5 | Yes | The maximum number of `GetSubscription` requests per second. | 
|  `ListSubscriptions`  | 5 | Yes | The maximum number of `ListSubscriptions` requests per second. | 
|  `ActivateSubscription`  | 1 | Yes | The maximum number of `ActivateSubscription` requests per second. | 
|  `DeactivateSubscription`  | 1 | Yes | The maximum number of `DeactivateSubscription` requests per second. | 