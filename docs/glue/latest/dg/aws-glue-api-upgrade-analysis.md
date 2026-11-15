

# Upgrade analysis
<a name="aws-glue-api-upgrade-analysis"></a>

The Upgrade analysis API includes operations for viewing, resuming, and stopping upgrade analyses for jobs in AWS Glue.

## Operations
<a name="aws-glue-api-upgrade-analysis-actions"></a>
+ [GetJobUpgradeAnalysis action (Python: get\_job\_upgrade\_analysis)](#aws-glue-api-upgrade-analysis-GetJobUpgradeAnalysis)
+ [StartJobUpgradeAnalysis action (Python: start\_job\_upgrade\_analysis)](#aws-glue-api-upgrade-analysis-StartJobUpgradeAnalysis)
+ [StopJobUpgradeAnalysis action (Python: stop\_job\_upgrade\_analysis)](#aws-glue-api-upgrade-analysis-StopJobUpgradeAnalysis)

## GetJobUpgradeAnalysis action (Python: get\_job\_upgrade\_analysis)
<a name="aws-glue-api-upgrade-analysis-GetJobUpgradeAnalysis"></a>

Retrieves the current status and results of an upgrade analysis.

**Request**
+ `analysisId` – *Required:* UTF-8 string, not less than 39 or more than 39 bytes long, matching the [Custom string pattern #80](aws-glue-api-common.md#regex_80).

  The unique identifier of the upgrade analysis to retrieve.
+ `jobName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the job associated with the analysis.

**Response**
+ `jobName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the job associated with this analysis.
+ `analysisId` – *Required:* UTF-8 string, not less than 39 or more than 39 bytes long, matching the [Custom string pattern #80](aws-glue-api-common.md#regex_80).

  The unique identifier of the upgrade analysis.
+ `status` – *Required:* UTF-8 string (valid values: `OBSERVING` \| `WAITING_FOR_CONSENT` \| `UPGRADING` \| `SUCCEEDED` \| `FAILED` \| `TIMEOUT` \| `STOPPED`).

  The current status of the analysis.
+ `sourceVersion` – UTF-8 string.

  The AWS Glue version the job was running before the upgrade, for example `4.0`.
+ `targetVersion` – *Required:* UTF-8 string.

  The AWS Glue version the job will be upgraded to, for example `6.0`.
+ `analysisType` – UTF-8 string (valid values: `AUTO_UPGRADE`).

  The type of upgrade analysis. For auto-upgrade jobs, this value is `AUTO_UPGRADE`.
+ `autoUpgradeEvaluationSummary` – UTF-8 string.

  A presigned URL for downloading the auto upgrade evaluation summary for the analysis. Available once the analysis reaches a terminal status (`SUCCEEDED` or `FAILED`). The URL expires after 1 hour. Calling `GetJobUpgradeAnalysis` again returns a new URL.
+ `errorMessage` – UTF-8 string.

  The reason the analysis did not complete.
+ `autoUpgradeEligibilitySummary` – UTF-8 string.

  A presigned URL for downloading the auto upgrade eligibility summary, which lists the compatibility results for the job. Available once the analysis reaches `WAITING_FOR_CONSENT` and in all subsequent states. The URL expires after 1 hour. Calling `GetJobUpgradeAnalysis` again returns a new URL.

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `OperationNotSupportedException`
+ `AccessDeniedException`
+ `InternalServiceException`

## StartJobUpgradeAnalysis action (Python: start\_job\_upgrade\_analysis)
<a name="aws-glue-api-upgrade-analysis-StartJobUpgradeAnalysis"></a>

Resumes an analysis that is waiting for upgrade consent.

**Request**
+ `jobName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the job associated with the analysis to resume.
+ `analysisId` – UTF-8 string, not less than 39 or more than 39 bytes long, matching the [Custom string pattern #80](aws-glue-api-common.md#regex_80).

  The unique identifier of the upgrade analysis. The analysis must be in `WAITING_FOR_CONSENT` status.
+ `upgradeConsent` – UTF-8 string (valid values: `APPROVE` \| `DECLINE`).

  The customer's decision on whether to proceed with the upgrade.

**Response**
+ `analysisId` – UTF-8 string, not less than 39 or more than 39 bytes long, matching the [Custom string pattern #80](aws-glue-api-common.md#regex_80).

  The unique identifier of the upgrade analysis.
+ `jobName` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the job associated with this analysis.

**Errors**
+ `ResourceNumberLimitExceededException`
+ `InvalidInputException`
+ `ValidationException`
+ `EntityNotFoundException`
+ `OperationNotSupportedException`
+ `AccessDeniedException`
+ `InternalServiceException`

## StopJobUpgradeAnalysis action (Python: stop\_job\_upgrade\_analysis)
<a name="aws-glue-api-upgrade-analysis-StopJobUpgradeAnalysis"></a>

Stops an in-progress upgrade analysis.

**Request**
+ `jobName` – *Required:* UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](aws-glue-api-common.md#aws-glue-api-regex-oneLine).

  The name of the job associated with the analysis.
+ `analysisId` – *Required:* UTF-8 string, not less than 39 or more than 39 bytes long, matching the [Custom string pattern #80](aws-glue-api-common.md#regex_80).

  The unique identifier of the analysis to stop.

**Response**
+ *No Response parameters.*

**Errors**
+ `InvalidInputException`
+ `EntityNotFoundException`
+ `OperationNotSupportedException`
+ `ThrottlingException`
+ `AccessDeniedException`
+ `InternalServiceException`