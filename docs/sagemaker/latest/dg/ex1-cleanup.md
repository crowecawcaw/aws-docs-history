# Clean up Amazon SageMaker notebook instance resources

To avoid incurring unnecessary charges, use the AWS Management Console to delete the endpoints and
resources that you created while running the exercises.

###### Note

Training jobs and logs cannot be deleted and are retained indefinitely.

###### Note

If you plan to explore other exercises in this guide, you might want to keep some
of these resources, such as your notebook instance, S3 bucket, and IAM
role.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/") and delete the following
   resources:
   - The endpoint. Deleting the endpoint also deletes the ML compute
     instance or instances that support it.
     1. Under **Inference**, choose
        **Endpoints**.
     2. Choose the endpoint that you created in the example, choose
        **Actions**, and then choose
        **Delete**.

   - The endpoint configuration.
     1. Under **Inference**, choose
        **Endpoint configurations**.
     2. Choose the endpoint configuration that you created in the
        example, choose **Actions**, and then choose
        **Delete**.

   - The model.
     1. Under **Inference**, choose
        **Models**.
     2. Choose the model that you created in the example, choose
        **Actions**, and then choose
        **Delete**.

   - The notebook instance. Before deleting the notebook instance, stop
     it.
     1. Under **Notebook**, choose **Notebook
        instances**.
     2. Choose the notebook instance that you created in the example,
        choose **Actions**, and then choose
        **Stop**. The notebook instance takes
        several minutes to stop. When the **Status**
        changes to **Stopped**, move on to the next
        step.
     3. Choose **Actions**, and then choose
        **Delete**.

2. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"), and then delete the bucket that
   you created for storing model artifacts and the training dataset.
3. Open the Amazon CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"), and then delete all of
   the log groups that have names starting with
   `/aws/sagemaker/`.
