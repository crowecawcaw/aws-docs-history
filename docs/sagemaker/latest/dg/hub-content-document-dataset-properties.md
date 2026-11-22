

# DataSet properties

The `HubContentDocument` for the `DataSet` HubContentType contains the metadata that describes a dataset stored in a SageMaker hub, including its file format, Amazon S3 location, validation results, and generation and job metadata, for both bring your own data (BYOD) and synthetic data generation (SDG) datasets. Use this metadata to evaluate and compare datasets and to make informed decisions about which dataset best fits your use case.

When calling the [DescribeHubContent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeHubContent.html) operation for a dataset, the response includes a `HubContentDocument` field, returned as a JSON-formatted string. This section describes the properties of that document for the `DataSet` HubContentType so that it can be more easily interpreted.

Parse the `HubContentDocument` string as JSON to read the properties described here. Property names use PascalCase. A document contains only the properties that apply to the dataset, so most properties are optional.

The `DatasetFileFormat` property is always required. For a BYOD dataset (when `DatasetType` is not `SyntheticDataGeneration`), `DatasetS3Bucket` and `DatasetS3Prefix` are also required. All other properties are optional and appear only when they apply to the dataset.

**Creating a dataset triggers automatic data validation**  
When you create a dataset, SageMaker automatically runs a `DataQualityEvaluation` job that validates the data against the declared `DatasetFileFormat`. SageMaker performs this validation at no charge to you.

<a name="hub-content-document-dataset-schema-top-level"></a>**Top-level properties**

The following table lists the top-level properties of the dataset `HubContentDocument`.


| Property | Type | Description | 
| --- | --- | --- | 
| `DatasetFileFormat` | `enum` | The format of the dataset files. Required for all dataset types. Valid values: Bedrock\_Converse, HF\_Prompt\_Completion, HF\_Preference, Verl, Nova\_PPO, Nova\_CPT, OpenAI\_Messages, SageMaker\_Eval, Nova\_RLVR, Nova\_DPO, MTRL, Custom.<br />**Required** | 
| `DatasetType` | `enum` | An optional type discriminator. Valid values are SyntheticDataGeneration or BYOD.<br />**Optional** | 
| `DatasetS3Bucket` | `string` | The S3 bucket name. Required for a BYOD dataset (when DatasetType is not SyntheticDataGeneration).<br />**Required for BYOD** | 
| `DatasetS3Prefix` | `string` | The S3 prefix path within the bucket. Required for a BYOD dataset (when DatasetType is not SyntheticDataGeneration).<br />**Required for BYOD** | 
| `DatasetS3Uri` | `S3Uri` | The S3 URI of the generated dataset file.<br />**Optional** | 
| `SpecS3Uri` | `S3Uri` | The S3 URI of the dataset specification document.<br />**Optional** | 
| `ValidationRoleArn` | `IamRoleArn` | The IAM role used to run dataset validation.<br />**Optional** | 
| `ValidationReportS3Uri` | `S3Uri` | The S3 URI of the validation report.<br />**Optional** | 
| `TransformationReportS3Uri` | `S3Uri` | The S3 URI of the transformation execution report.<br />**Optional** | 
| `TransformationCodeS3Uri` | `S3Uri` | The S3 URI of the generated transformation code (transformer.py) produced by a DataTransformation code-generation job.<br />**Optional** | 
| `CodeArtifacts` | `object` | The generator and verifier code artifacts.<br />**Optional** | 
| `NumRequestedSamples` | `int >= 1` | The number of samples requested for generation.<br />**Optional** | 
| `NumValidSamples` | `int >= 0` | The number of samples that passed validation.<br />**Optional** | 
| `DatasetJobArn` | `string` | The ARN of the synthetic data generation (SDG) job that created this dataset.<br />**Optional** | 
| `TransformationJobArn` | `string` | The ARN of the DataTransformation job that created this dataset.<br />**Optional** | 
| `MlflowConfig` | `object` | The MLflow configuration.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata` | `object` | The generation history and job configuration.<br />**Optional** | 
| `DataQualityMetadata` | `object[]` | An array of data quality evaluation metadata entries. Each entry points to an index file (MetadataS3Uri) that lists the individual report URIs.<br />**Optional** | 
| `JobMetadata` | `object[]` | An array of dataset job metadata entries, one for each dataset job that produced or evaluated this dataset. Each entry points to an index file with that job's output report URIs; it records which job wrote it but is not service-attested.<br />**Optional** | 
| `ValidationManifest` | `object` | The results of automatic dataset validation, including record counts, failure details, and detected features. Read-only: the service populates it when validation runs; you cannot set it directly.<br />**Optional** | 
| `ContentMetadata` | `object` | Metadata for datasets extracted from SageMaker Feature Store, used for lineage tracking between feature groups and training jobs.<br />**Optional** | 
| `Metadata` | `object` | Optional key-value pairs that describe the dataset. Keys are 1–128 characters; each value is a string, number, boolean, object, or an array of those. Up to 50 properties.<br />**Optional** | 

<a name="hub-content-document-dataset-schema-nested"></a>**Nested properties**

The following table lists the properties nested inside the object and array properties in the preceding table. A nested property marked as required is required only when its parent property is present.


| Property path | Type | Description | 
| --- | --- | --- | 
| `CodeArtifacts.GenerationCodeS3Uri` | `S3 URI` | The S3 URI of the generator script.<br />**Required** | 
| `CodeArtifacts.VerifiersCodeS3Uri` | `S3 URI` | The S3 URI of the verifier script.<br />**Required** | 
| `MlflowConfig.MlflowResourceArn` | `string` | The ARN of the MLflow app resource.<br />**Required** | 
| `MlflowConfig.MlflowExperimentName` | `string` | The name of the MLflow experiment associated with this dataset.<br />**Required** | 
| `SyntheticDataGenerationJobMetadata.InputDataS3Uri` | `S3 URI` | The S3 URI of the seed/contextual data and documents used for generation.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.SampleGenerationStrategy` | `enum RoundRobin \| Jury` | How the sample generation models were combined. RoundRobin (default) assigns each sample to one model; Jury sends every sample to all models and keeps the majority response. Default is RoundRobin.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig` | `object` | The large language model (LLM) configuration for generation and verification. Each model config accepts a model ID hosted on Amazon Bedrock.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleGenerationModelConfigs` | `array` | Configurations for the LLMs used for sample generation (1–5). When multiple models are specified, generation requests are distributed across them in round-robin.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleGenerationModelConfigs[].ModelId` | `string` | The Bedrock model ID used for sample generation.<br />**Required** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleGenerationModelConfigs[].TargetTokensPerMinute` | `integer` | The best-effort target token-per-minute throughput limit for sample generation; actual usage might briefly exceed it.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleVerificationModelConfigs` | `array` | Configurations for the LLMs used for verification (1–10).<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleVerificationModelConfigs[].ModelId` | `string` | The Bedrock model ID used for verification.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.SampleVerificationModelConfigs[].TargetTokensPerMinute` | `integer` | The best-effort target token-per-minute throughput limit for verification.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.CodeGenerationModelConfig` | `object` | The configuration for the LLM used for code generation. Only Anthropic Claude Sonnet and Opus models are supported.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.CodeGenerationModelConfig.ModelId` | `string` | The Bedrock model ID used for code generation.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.ModelConfig.CodeGenerationModelConfig.TargetTokensPerMinute` | `integer` | The best-effort target token-per-minute throughput limit for code generation.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.SyntheticDataGenerationEngineVersion` | `string` | The version of the generation engine.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.CreatedAt` | `string (date-time)` | The timestamp when the generation job completed.<br />**Optional** | 
| `SyntheticDataGenerationJobMetadata.CustomerFacingMessage` | `string` | A human-readable summary of the generation outcome.<br />**Optional** | 
| `DataQualityMetadata[].MetadataS3Uri` | `S3 URI` | The S3 URI of the data quality index file that lists the individual report URIs (aggregate, record-level, recommendations).<br />**Required** | 
| `DataQualityMetadata[].CreatedAt` | `string (date-time)` | The timestamp when the data quality evaluation was created.<br />**Required** | 
| `DataQualityMetadata[].EvaluationName` | `string` | A human-readable name for this evaluation run.<br />**Required** | 
| `JobMetadata[].MetadataS3Uri` | `S3 URI` | The S3 URI of the job's index file that lists its individual report URIs.<br />**Required** | 
| `JobMetadata[].CreatedAt` | `string (date-time)` | The timestamp when the job completed.<br />**Required** | 
| `JobMetadata[].JobName` | `string` | The name of the dataset job that wrote this entry.<br />**Required** | 
| `JobMetadata[].JobType` | `enum SyntheticDataGeneration \| DataQualityEvaluation \| DataTransformation \| GapAnalysis` | The category of the dataset job that wrote this entry.<br />**Required** | 
| `ValidationManifest.JobStatus` | `enum IN_PROGRESS \| COMPLETED \| ERROR \| SKIPPED` | The status of the validation run. IN\_PROGRESS: Validation is running. COMPLETED: Results are available. ERROR: Validation could not complete (see FailureReason and Retryable). SKIPPED: No validation job ran for this version.<br />**Required** | 
| `ValidationManifest.Retryable` | `boolean` | Specifies whether the error is transient and a retry might succeed. Applies when JobStatus is ERROR; if false, the error requires customer action.<br />**Optional** | 
| `ValidationManifest.FailureReason` | `string` | Present when JobStatus is ERROR. A human-readable description of the scan-level condition that prevented validation.<br />**Optional** | 
| `ValidationManifest.ValidatedAt` | `string (date-time)` | The timestamp when validation completed.<br />**Optional** | 
| `ValidationManifest.ValidationJobArn` | `string` | The ARN of the validation job that produced this result.<br />**Optional** | 
| `ValidationManifest.Modality` | `enum TEXT` | The data modality of the dataset.<br />**Optional** | 
| `ValidationManifest.RecordCount` | `integer` | The total number of records in the dataset.<br />**Optional** | 
| `ValidationManifest.ValidRecords` | `integer` | The number of records that passed validation.<br />**Optional** | 
| `ValidationManifest.FailedRecords` | `integer` | The number of records that failed validation.<br />**Optional** | 
| `ValidationManifest.FailureRate` | `number` | The fraction of records that failed validation (FailedRecords/RecordCount), from 0 to 1.<br />**Optional** | 
| `ValidationManifest.SummaryByReason` | `array` | Failure counts grouped by reason code.<br />**Optional** | 
| `ValidationManifest.SummaryByReason[].ReasonCode` | `string` | The code identifying the type of validation failure.<br />**Required** | 
| `ValidationManifest.SummaryByReason[].Message` | `string` | A human-readable description of the failure.<br />**Optional** | 
| `ValidationManifest.SummaryByReason[].Count` | `integer` | The number of records with this failure.<br />**Required** | 
| `ValidationManifest.Features` | `object` | Detected dataset features such as schema shape, field presence rates, and structure observations.<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices` | `object` | The indices of records that failed validation, with an inline preview and an S3 reference to the full list.<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices.S3Uri` | `S3 URI` | The S3 URI of the complete list of failed record indices.<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices.Count` | `integer` | The total number of failed record indices.<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices.Preview` | `integer[]` | An inline preview of failed record indices (up to 500).<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices.PreviewTruncated` | `boolean` | Specifies whether the full list exceeds the inline preview limit.<br />**Optional** | 
| `ValidationManifest.FailedRecordIndices.FailuresS3Uri` | `S3 URI` | The S3 URI of per-record failure details.<br />**Optional** | 
| `ContentMetadata.SourceFeatureGroups` | `string[]` | The ARNs of the feature groups that contributed data to this dataset extraction (1–50).<br />**Required** | 
| `ContentMetadata.ExtractionMethod` | `enum FeatureStoreDatasetBuilder` | The method used to extract data from Feature Store.<br />**Optional** | 
| `ContentMetadata.AthenaQueryExecutionId` | `string` | The Athena query execution ID that produced the dataset CSV.<br />**Optional** | 
| `Metadata[key]` | `string \| number \| boolean \| object \| array` | A single key-value entry describing the dataset. Keys are 1–128 characters.<br />**Optional** | 