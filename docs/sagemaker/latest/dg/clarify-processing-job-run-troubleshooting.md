# Troubleshoot SageMaker Clarify Processing

Jobs

If you encounter failures with SageMaker Clarify processing jobs, consult the following scenarios to
help identify the issue.

###### Note

The failure reason and exit message are intended to contain descriptive messages and
exceptions, if encountered, during the run. A common reason for errors is that
parameters are either missing or not valid. If you encounter unclear, confusing, or
misleading messages or are unable to find a solution, submit feedback.

###### Topics

- [Processing job fails to
  finish](#clarify-troubleshooting-job-fails "#clarify-troubleshooting-job-fails")
- [Processing job is taking too long to
  run](#clarify-troubleshooting-job-long "#clarify-troubleshooting-job-long")
- [Processing job finishes
  without results and you get a CloudWatch warning message](#clarify-troubleshooting-no-results-and-warning "#clarify-troubleshooting-no-results-and-warning")
- [Error message
  for invalid analysis configuration](#clarify-troubleshooting-invalid-analysis-configuration "#clarify-troubleshooting-invalid-analysis-configuration")
- [Bias metric
  computation fails for several or all metrics](#clarify-troubleshooting-bias-metric-computation-fails "#clarify-troubleshooting-bias-metric-computation-fails")
- [Mismatch between analysis config and dataset/model input/output](#clarify-troubleshooting-mismatch-analysis-config-and-data-model "#clarify-troubleshooting-mismatch-analysis-config-and-data-model")
- [Model returns 500
  Internal Server Error or container falls back to per-record predictions due to model
  error](#clarify-troubleshooting-500-internal-server-error "#clarify-troubleshooting-500-internal-server-error")
- [Execution role is
  invalid](#clarify-troubleshooting-execution-role-invalid "#clarify-troubleshooting-execution-role-invalid")
- [Failed to download data](#clarify-troubleshooting-data-download "#clarify-troubleshooting-data-download")
- [Could not connect to SageMaker AI](#clarify-troubleshooting-connection "#clarify-troubleshooting-connection")

## Processing job fails to

finish

If the processing job fails to finish, you can try the following:

- Inspect the job logs directly in the notebook where you ran the job in. The
  job logs are located in the output of the notebook cell where you initiated the
  run.
- Inspect the job logs in CloudWatch.
- Add the following line in your notebook to describe the last processing job
  and look for the failure reason and exit message:
  - `clarify_processor.jobs[-1].describe()`

- Run the following AWS CLI; command to describe the processing job and look for
  the failure reason and exit message:
  - `aws sagemaker describe-processing-job —processing-job-name
<processing-job-id>`

## Processing job is taking too long to

run

If your processing job is taking too long to run, use the following ways to find the
root cause.

Check to see if your resource configuration is sufficient to handle your computing
load. To speed up your job, try the following:

- Use a larger instance type. SageMaker Clarify queries the model repeatedly, and a larger
  instance can significantly reduce your computation time. For a list of available
  instances, their memory sizes, bandwidth, and other performance details, see
  [Amazon SageMaker AI
  Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").
- Add more instances. SageMaker Clarify can use multiple instances to explain multiple input
  data points in parallel. To enable parallel computing, set your
  `instance_count` to more than `1` when you call
  `SageMakerClarifyProcessor`. For more information, see [How to run parallel SageMaker Clarify processing
  jobs](clarify-processing-job-run.md#clarify-processing-job-run-spark "clarify-processing-job-run.md#clarify-processing-job-run-spark"). If you increase your
  instance count, monitor the performance of your endpoint to check that it can
  deploy the increased load. For more information, see [Capture data from real-time
  endpoint](model-monitor-data-capture-endpoint.md "model-monitor-data-capture-endpoint.md").
- If you're computing SHapley Additive exPlanations
  (SHAP) values, reduce the `num_samples` parameter
  in your analysis configuration file. The number of samples directly affects the
  following:

      + The size of the synthetic datasets that are sent to your
       endpoint
      + Job runtime

  Reducing the number of samples can also lead to reduced accuracy in estimating
  SHAP values. For more information, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

## Processing job finishes

without results and you get a CloudWatch warning message

If the processing job finishes but no results are found, the CloudWatch logs produce a
warning message that says **`Signal 15 received, cleaning up.`**This
warning indicates that the job was stopped either because a customer request called the
`StopProcessingJob` API, or that the job ran out of the allotted time for
its completion. In the latter case, check the maximum runtime in the job configuration
(`max_runtime_in_seconds`) and increase it as needed.

## Error message

for invalid analysis configuration

- If you get the error message **`Unable to load analysis configuration
as JSON.`**, this means that the analysis configuration input file
  for the processing job does not contain a valid JSON object. Check the validity
  of the JSON object using a JSON linter.
- If you get the error message **`Analysis configuration schema
validation error.`**, this means that the analysis configuration
  input file for the processing job contains unknown fields or invalid types for
  some field values. Review the configuration parameters in the file and
  cross-check them with the parameters listed in the analysis configuration file.
  For more information, see [Analysis Configuration Files](clarify-processing-job-configure-analysis.md "clarify-processing-job-configure-analysis.md").

## Bias metric

computation fails for several or all metrics

If your receive one of the following error messages **`No Label values are
 present in the predicted Label Column, Positive Predicted Index Series contains all
 False values.`** or **`Predicted Label Column series data type is
 not the same as Label Column series.`**, try the following:

- Check that the correct dataset is being used.
- Check whether the dataset size is too small; whether, for example, it contains
  only a few rows. This may cause the model outputs to have the same value or the
  data type is inferred incorrectly.
- Check if the label or facet is treated as continuous or categorical. SageMaker Clarify
  uses heuristics to determine the [`DataType`](https://github.com/aws/amazon-sagemaker-clarify/blob/master/src/smclarify/bias/metrics/common.py#L114) "https://github.com/aws/amazon-sagemaker-clarify/blob/master/src/smclarify/bias/metrics/common.py#L114)"). For post-training bias metrics, the data
  type returned by the model may not match what is in the dataset or SageMaker Clarify may not
  be able to transform it correctly.
  - In the bias report, you should see a single value for categorical
    columns or an interval for continuous columns.
  - For example, if a column has values 0.0 and 1.0 as floats, it will be
    treated as continuous even if there are too few unique values.

## Mismatch between analysis config and dataset/model input/output

- Check that the baseline format in the analysis config is the same as dataset
  format.
- If your receive the error message **`Could not convert string to
float.`**, check that the format is correctly specified. It could
  also indicate that the model predictions have a different format than the label
  column or it could indicate that the configuration for the label or
  probabilities is incorrect.
- If your receive the error message **`Unable to locate the
facet.`** or **`Headers must contain label.`** or
  **`Headers in config do not match with the number of columns in the
dataset.`** or **`Feature names not found.`**,
  check that the headers match the columns.
- If your receive the error message **`Data must contain
features.`**, check the content template for JSON Lines and compare
  it with the dataset sample if available.

## Model returns 500

Internal Server Error or container falls back to per-record predictions due to model
error

If you receive the error message **`Fallback to per-record prediction because
 of model error.`**, this could indicate that model cannot handle the batch
size, or be throttled, or just does not accept the input passed by the container due to
serialization problems. You should review the CloudWatch logs for the SageMaker AI endpoint and
look for error messages or tracebacks. For model throttling cases, it may help to use a
different instance type or increasing the number of instances for the endpoint.

## Execution role is

invalid

This indicates that the role provided is incorrect or missing required permissions.
Check the role and its permissions that were used to configure the processing job and
verify the permission and trust policy for the role.

## Failed to download data

This indicates that job inputs could not be downloaded for the job to start. Check the
bucket name and permissions for the dataset and the configuration inputs.

## Could not connect to SageMaker AI

This indicates that the job could not reach SageMaker AI service endpoints. Check the network
configuration settings for the processing job and verify virtual private cloud (VPC)
configuration.
