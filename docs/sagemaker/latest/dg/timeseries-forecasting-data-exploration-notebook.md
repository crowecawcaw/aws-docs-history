

# Amazon SageMaker Autopilot data exploration notebook
<a name="timeseries-forecasting-data-exploration-notebook"></a>

Amazon SageMaker Autopilot cleans and pre-processes your dataset automatically. To help users understand their data, uncover patterns, relationships, and anomalies about the time-series, Amazon SageMaker Autopilot generates a **data exploration** static report in the form of a notebook for users to reference.

The data exploration notebook is generated for every Autopilot job. The report is stored in an Amazon S3 bucket and can be accessed from the job output path.

You can find the Amazon S3 prefix to the data exploration notebook in the response to `[DescribeAutoMLJobV2](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html)` at `[AutoMLJobArtifacts.DataExplorationNotebookLocation](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeAutoMLJobV2.html#sagemaker-DescribeAutoMLJobV2-response-AutoMLJobArtifacts)`.