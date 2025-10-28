# Running inference on a trained model in

AWS Clean Rooms ML

Members with the ability to run queries can also initiate inference job once the
training job is complete. They pick the inference dataset against which they want to run
inference and reference the trained model outputs that they’d like to run inference
container with.

The member who will receive inference output must be granted the member ability
`CAN_RECEIVE_INFERENCE_OUTPUT`.

Console

###### To create a model inference job (console)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. On the **Collaborations** page, choose the
   collaboration that contains the custom model that you want to create
   an inference job on.
4. After the collaboration opens, choose the **ML
   Models** tab, then choose your model from the
   **Custom trained model** table.
5. On the custom trained model details page, click **Start
   inference job**.
6. For **Start inference job**, for
   **Inference job details**, enter a
   **Name** and optional
   **Description**.

Enter the following information:

    * **Associated model algorithm** - The
     associated model algorithm that is used during the inference
     job.
    * **ML input channel details** - The ML
     input channel that will provide the data for this inference
     job.
    * **Transform resources** - The compute
     instance that is used to perform the transform function of
     the inference job.
    * **Output configuration** - Who will
     receive the inference job output and the MIME type of the
     output.
    * **Encryption** - choose the
     **Customize encryption settings** to
     specify your own KMS key and related information.
     Otherwise, Clean Rooms ML will manage the encryption.
    * **Transform job details** - The maximum
     payload of the inference job, in MB.
    * **Environment variables** - Any
     environment variables necessary to access the inference job
     container image.

7. Choose **Start inference job**.

The results are exported to the following path in the Amazon S3
location that was specified in the ML configuration:
`yourSpecifiedS3Path/collaborationIdentifier/trainedModelName/callerAccountId/jobName`.

API
To create a model inference job (API)

Initiate the inference job by running the following code:

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.start_trained_model_inference_job(
 name="inference_job",
 membershipIdentifier='`membership_id`',
 trainedModelArn='arn:aws:cleanrooms-ml:`region`:`account`:`membership`/membershipIdentifier/trained-model/`identifier`',

 dataSource={
 "mlInputChannelArn": 'channel_arn_3'
 },
 resourceConfig={'instanceType': 'ml.m5.xlarge'},
 outputConfiguration={
 'accept': 'text/csv',
 'members': [
 {
 "accountId": '`member_account_id`'
 }
 ]
 }
)`
```

The results are exported to the following path in the Amazon S3 location that
was specified in the ML configuration:
`yourSpecifiedS3Path/collaborationIdentifier/trainedModelName/callerAccountId/jobName`.
