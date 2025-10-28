# Configuring a model algorithm in

AWS Clean Rooms ML

After you have [created a container training image](../../../sagemaker/latest/dg/docker-containers.md "../../../sagemaker/latest/dg/docker-containers.md"), you must configure
your model algorithm. Configuring a model algorithm makes it available for association
to a collaboration.

The following image shows configuring a model algorithm as a step that happens after
you create the container training image and before you associate it with the
collaboration.

![An overview of how to contribute a custom ML model.](images/bringMLModelCollaboration.png)

Console

###### To configure a custom ML model algorithm (console)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose **Custom ML
   models**.
3. On the **Custom ML models** page, choose
   **Configure model algorithm**.
4. On the **Configure model algorithm** page, for
   **Model algorithm details**, enter a
   **Name** and optional
   **Description**.
5. If you want to perform model training, for **Training
   image ECR container details**,
   1. Select the **Specify training image URI**
      checkbox.
   2. Select the **Repository** that has the
      training model, inference container, or both, from the
      dropdown list.
   3. Select the **Image**.
   4. (Optional) Enter the **Value** for the
      **Entrypoints** to access the training
      image.
   5. (Optional) Enter the **Value** for the
      **Arguments**.

6. (Optional) If you want to report model metrics, for
   **Training metrics**, enter the
   **Name** of the metrics and the
   **Regex** statement that will search the output
   logs to find the metric.
7. If you want to perform model inference, for **Inference
   image ECR container details**,
   1. Select the **Specify inference image
      URI** checkbox.
   2. Select the **Repository** from the
      dropdown list.
   3. Select the **Image**.

8. For **Service access**, choose the
   **Existing service role name** that will be
   used to access this table.
9. For **Encryption**, choose the
   **Customize encryption settings** to specify
   your own KMS key and related information. Otherwise, Clean Rooms ML will
   manage the encryption.
10. If you want to enable **Tags**, choose
    **Add new tag** and then enter the
    **Key** and **Value**
    pair.
11. Choose **Configure model algorithm**.

API
To configure a custom ML model algorithm (API)

1.  Create a SageMaker AI compatible docker image. Clean Rooms ML only supports SageMaker AI
    compatible docker images.
2.  After you have created a SageMaker AI compatible docker image, use Amazon ECR
    to create a training image. Follow the directions in [Amazon Elastic Container Registry User Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md")
    to create a container training image.
3.  Configure the model algorithm for use in Clean Rooms ML. You must give
    the following information:

        * The Amazon ECR repository link and additional arguments to
         train the model and run inference. Clean Rooms ML supports running
         batch transform jobs on an inference container.
        * A service access role that allows Clean Rooms ML to access the
         repository.
        * (Optional) An inference container. Although you can
         provide this in a separate configured model algorithm, we
         recommend that you provide it in this step so that both the
         training and inference container are managed as part of the
         same resource.

    Run the following code with your specific parameters.

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.create_configured_model_algorithm(
 name='`configured_model_algorithm_name`',
 trainingContainerConfig={
 'imageUri': 'account.dkr.ecr.`region`.amazonaws.com/`image_name`:`tag`',
 'metricDefinitions': [
 {
 'name': '`custom_metric_name_1`',
 'regex': '`custom_metric_regex_1`'
 }
 ]
 },
 inferenceContainerConfig={
 'imageUri':'account.dkr.ecr.`region`.amazonaws.com/`image_name`:`tag`',
 }
 roleArn='arn:aws:iam::`account`:`role`/`role_name`'
)`
```
