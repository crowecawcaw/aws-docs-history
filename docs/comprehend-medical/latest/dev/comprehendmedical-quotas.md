# Guidelines and quotas

Keep the following information in mind when using Amazon Comprehend Medical.

###### Note

- Amazon Comprehend Medical supports character encoding in UTF-8 English (EN).
- Amazon Comprehend Medical does not allow sequential forward slash characters (`//`) in file paths for async jobs.

## Important notice

Amazon Comprehend Medical is not a substitute for professional medical advice, diagnosis, or treatment. Amazon Comprehend Medical provides confidence scores that indicate the level of confidence in the accuracy of the detected entities. Identify the right confidence threshold for your use case, and use high confidence thresholds in situations that require high accuracy. For certain use cases, results should be reviewed and verified by appropriately trained human reviewers. Use Amazon Comprehend Medical in patient care scenarios only after trained medical professionals have reviewed results for accuracy and sound medical judgment.

## Supported regions

For a list of AWS Regions where Amazon Comprehend Medical is available, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md#comprehend-med_region "../../../general/latest/gr/rande.md#comprehend-med_region") in the _Amazon Web Services General Reference_.

## Throttling

For information about throttling and quotas for Amazon Comprehend Medical, and to request a quota
increase, see [AWS
Service Quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

## Overall quotas

Amazon Comprehend Medical real time (sync) analysis operations have the following quotas:

| Resource                                                                                                                                                                                                                                                                                                                                              | Default    |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Transactions per second (TPS) for the `DetectEntities-v2`, `DetectEntities`, `DetectPHI`, `InferRxNorm`, and `InferICD10CM` operations                                                                                                                                                                                                                | 40 TPS     |
| Transactions per second (TPS) for the `InferSNOMEDCT` operation                                                                                                                                                                                                                                                                                       | 2 TPS      |
| Characters per second (CPS) for the `DetectEntities-v2`, `DetectEntities`, `DetectPHI`, `InferRxNorm`, and `InferICD10CM` operations                                                                                                                                                                                                                  | 40,000 CPS |
| Characters per second (CPS) for the `InferSNOMEDCT` operation                                                                                                                                                                                                                                                                                         | 5,000 CPS  |
| Maximum document size (UTF-8 characters) for the `DetectEntities`, `DetectEntities-v2`, and `DetectPHI` operations                                                                                                                                                                                                                                    | 20 KB      |
| Maximum document size (UTF-8 characters) for the `InferICD10-CM` and `InferRxNorm` operations                                                                                                                                                                                                                                                         | 10 KB      |
| Maximum document size (UTF-8 characters) for the `InferSNOMEDCT` operation                                                                                                                                                                                                                                                                            | 5 KB       | Amazon Comprehend Medical batch analysis (async) operations have the following quotas:                                                                             |
| Description                                                                                                                                                                                                                                                                                                                                           | Quota      |
| ---                                                                                                                                                                                                                                                                                                                                                   | ---        |
| Transactions per second (TPS) for the `StartEntitiesDetectionV2Job`, `StartPHIDetectionJob`, `StopEntitiesDetectionV2Job`, `StopPHIDetectionJob`, `StartICD10CMInferenceJob`, `StartRxNormInferenceJob`, `StopICD10CMInferenceJob`, `StopRxNormInferenceJob`, `StartSNOMEDCTnferenceJob` and `StopSNOMEDCTnferenceJob` operations                     | 5 TPS      |
| Transactions per second (TPS) for the `ListEntitiesDetectionV2Jobs`, `ListPHIDetectionJobs`, `DescribeEntitiesDetectionV2Job`, `DescribePHIDetectionJob`, `ListICD10CMInferenceJobs`, `ListRxNormInferenceJobs`, `DescribeICD10CMInferenceJob`, `DescribeRxNormInferenceJob`, `ListSNOMEDCTnferenceJobs` and `DescribeSNOMEDCTnferenceJob` operations | 10 TPS     |
| Maximum individual file size for batch jobs for all operations                                                                                                                                                                                                                                                                                        | 70 KB      |
| Maximum number of individual files in a batch job                                                                                                                                                                                                                                                                                                     | 5000000    |
| Maximum size of batch jobs (sum total of all files submitted in a batch job)                                                                                                                                                                                                                                                                          | 1 GB       |
| Maximum number of active running batch jobs for each operation                                                                                                                                                                                                                                                                                        | 10 jobs    | If your text is larger than the character quotas, use [segment.py](samples/segment.py.md "samples/segment.py.md") to create smaller segments that can be analyzed. |
