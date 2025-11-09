# Rerun a run in HealthOmics

For runs you haven't deleted yet, use the console or API to rerun the run. For runs that youv'e deleted,
use the HealthOmics **rerun** tool.

###### Topics

- [Rerun a run using the console](#rerun-a-run-console "#rerun-a-run-console")
- [Rerun a run using the API](#rerun-a-run-api "#rerun-a-run-api")
- [Using the Rerun tool](#rerun-tool "#rerun-tool")

## Rerun a run using the console

From the console, follow these steps to rerun a run:

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, select the run to rerun.
4. From the action menu above the table, choose **Re-run**.

## Rerun a run using the API

Use the **StartRun** API operation to rerun an existing run. Provide the
following required inputs:

- A service role ARN (`roleArn`).
- The ID of the run to duplicate (`runId`).
- An Amazon S3 location where the run saves the run outputs
  (`outputUri`).

```
aws omics start-run
     --run-id ``run id`` \
     --role-arn arn:aws:iam::1234567892012:role/service-role/OmicsWorkflow-20221004T164236 \
     --output-uri s3://workflow-output-b6f2fce1
```

## Using the Rerun tool

For a deleted run, you can download and use the HealthOmics **rerun** tool to rerun the run. The tool
retrieves run information from the CloudWatch Logs manifest. Download the **rerun** tool from the [HealthOmics Tool GitHub repository](https://github.com/awslabs/amazon-omics-tools " https://github.com/awslabs/amazon-omics-tools").

The following example shows how to use the **rerun** tool.

```
aws-healthomics-rerun 9876543
```

If the run exists in CloudWatch, you receive a response similar to the following example output. If the workflow no
longer exists, you receive an error message.

```
Original request:
{
  "workflowId": "9679729",
  "roleArn": "arn:aws:iam::123456789012:role/DemoRole",
  "name": "sample_rerun",
  "parameters": {
    "image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/default:latest",
    "file1": "omics://123456789012.storage.us-west-2.amazonaws.com/8647780323/readSet/6389608538"
  },
  "outputUri": "s3://workflow-output-bcf2fcb1"
}
StartRun request:
{
  "workflowId": "9679729",
  "roleArn": "arn:aws:iam::123456789012:role/DemoRole",
  "name": "new test",
  "parameters": {
    "image": "123456789012.dkr.ecr.us-west-2.amazonaws.com/default:latest",
    "file1": "omics://123456789012.storage.us-west-2.amazonaws.com/8647780323/readSet/6389608538"
  },
  "outputUri": "s3://workflow-output-bcf2fcb1"
}
StartRun response:
{
  "arn": "arn:aws:omics:us-west-2:123456789012:run/9171779",
  "id": "9171779",
  "status": "PENDING",
  "tags": {}
}
```
