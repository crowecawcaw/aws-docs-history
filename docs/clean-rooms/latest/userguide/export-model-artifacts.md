# Exporting model artifacts from

AWS Clean Rooms ML

This task is optional and should be completed when you have assigned the
`CAN_RECEIVE_MODEL_OUTPUT` member ability to a member of the
collaboration.

After model training has completed, the member who trained the model can initiate the
export of model artifacts. The member who trained the model chooses who will receive
model artifacts, provided that member can receive results and a valid ML
configuration.

Console

###### To configure a custom ML model algorithm (console)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. On the **Collaborations** page, choose the
   collaboration that contains the custom model that you want to
   export.
4. After the collaboration opens, choose the **ML
   Models** tab, then choose your model from the
   **Custom trained model** table
5. On the custom trained model details page, click **Export
   model output**.
6. For **Export model output**, for **Export
   model output details**, enter a
   **Name** and optional
   **Description**.

Choose which member will receive the model artifacts in the
**Model output exported to members of
collaboration** drop down list. 7. Choose **Export**.

The results are exported to the following path in the Amazon S3
location that was specified in the ML configuration:
`yourSpecifiedS3Path/collaborationIdentifier/trainedModelName/callerAccountId/jobName`.
Only the **Files to export**, up to the maximum
file size specified, that you selected when associating the
configured model algorithm are exported.

API
To configure a custom ML model algorithm (API)

Initiate the model export by running the following code:

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.start_trained_model_export_job(
 membershipIdentifier='`membership_id`',
 trainedModelArn='arn:aws:cleanrooms-ml:`region`:`account`:`membership`/membershipIdentifier/trained-model/`identifier`',
 outputConfiguration={
 'member': {
 'accountId': '`model_output_receiver_account`'
 }
 },
 name='`export_job_name`'
)`
```

The results are exported to the following path in the Amazon S3 location that
was specified in the ML configuration:
`yourSpecifiedS3Path/collaborationIdentifier/trainedModelName/callerAccountId/jobName`.
Only the `filesToExport`, up to the `maxSize`
specified, that you selected when associating the configured model algorithm
are exported.
