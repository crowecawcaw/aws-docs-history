# Stop your inference

recommendation

You might want to stop a job that is currently running if you began a job by
mistake or no longer need to run the job. Stop your Inference Recommender inference recommendation
jobs programmatically with the `StopInferenceRecommendationsJob` API or
with Studio Classic.

AWS SDK for Python (Boto3)
Specify the name of the inference recommendation job for the
`JobName` field:

```
sagemaker_client.stop_inference_recommendations_job(
                                    JobName=`'<INSERT>'`
                                    )
```

AWS CLI
Specify the job name of the inference recommendation job for the
`job-name` flag:

```
aws sagemaker stop-inference-recommendations-job --job-name `<job-name>`
```

Amazon SageMaker Studio Classic
Close the tab in which you initiated the inference recommendation to
stop your Inference Recommender inference recommendation.

SageMaker AI console
To stop your instance recommendation job through the SageMaker AI console, do
the following:

1. Go to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. In the left navigation pane, choose
   **Inference**, and then choose
   **Inference recommender**.
3. On the **Inference recommender jobs** page,
   select your instance recommendation job.
4. Choose **Stop job**.
5. In the dialog box that pops up, choose
   **Confirm**.

After stopping your job, the job’s **Status** should
change to **Stopping**.
