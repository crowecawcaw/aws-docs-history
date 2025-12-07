# Accessing and analyzing

evaluation results

After your evaluation job completes successfully, you can access and analyze the results
using the information in this section. Based on the `output_s3_path` (such as
`s3://output_path/`) defined in the recipe, the output structure is the
following:

```
job_name/
├── eval-result/
│    └── results_[timestamp].json
│    └── inference_output.jsonl (only present for gen_qa)
│    └── details/
│        └── model/
│            └── execution-date-time/
│                └──details_task_name_#_datetime.parquet
└── tensorboard-results/
    └── eval/
        └── events.out.tfevents.[timestamp]
```

Metrics results are stored in the specified S3 output location
`s3://output_path/job_name/eval-result/result-timestamp.json`.

Tensorboard results are stored in the S3 path
`s3://output_path/job_name/eval-tensorboard-result/eval/event.out.tfevents.epoch+ip`.

All inference outputs, except for `llm_judge` and `strong_reject`,
are stored in the S3 path:
`s3://output_path/job_name/eval-result/details/model/taskname.parquet`.

For `gen_qa`, the `inference_output.jsonl` file contains the
following fields for each JSON object:

- prompt - The final prompt submitted to the model
- inference - The raw inference output from the model
- gold - The target response from the input dataset
- metadata - The metadata string from the input dataset if provided
  To visualize your evaluation metrics in Tensorboard, complete the following
  steps:

1. Navigate to SageMaker AI Tensorboard.
2. Select **S3 folders**.
3. Add your S3 folder path, for example
   `s3://output_path/job-name/eval-tensorboard-result/eval`.
4. Wait for synchronization to complete.
   The time series, scalars, and text visualizations are available.

We recommend the following best practices:

- Keep your output paths organized by model and benchmark type.
- Maintain consistent naming conventions for easy tracking.
- Save extracted results in a secure location.
- Monitor TensorBoard sync status for successful data loading.
  You can find HyperPod job error logs in the CloudWatch log group
  `/aws/sagemaker/Clusters/cluster-id`.
