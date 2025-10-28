# Creating a trained model in AWS Clean Rooms ML

Prerequisites:

- An AWS account with access to AWS Clean Rooms
- A collaboration set up in AWS Clean Rooms
- A configured model algorithm associated with the collaboration
- At least one configured ML input channel
- Appropriate permissions to create and manage ML models in the
  collaboration
  After you have associated the configured model algorithm to a collaboration, then
  created and configured an ML input channel, you are ready to create a trained model. A
  _trained model_ is used by members of a
  collaboration to jointly analyze their data.

You can create a trained model using the following procedure.

Alternatively, you can use incremental training to improve an existing model with new
data, or distributed training to train models across multiple compute instances.

###### Topics

- [Using incremental training in
  AWS Clean Rooms ML](use-incremental-training.md "use-incremental-training.md")
- [Using distributed training in
  AWS Clean Rooms ML](use-distributed-training.md "use-distributed-training.md")

Console

###### To create a trained model (console)

1.  Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2.  In the left navigation pane, choose
    **Collaborations**.
3.  On the **Collaborations** page, choose the
    collaboration where you want to create a trained model.
4.  After the collaboration opens, choose the **ML
    models** tab.
5.  Under **Custom ML models**, in the
    **Trained models** section, choose
    **Create trained model**.
6.  On the **Create trained model** page, for
    **Associated model algorithm**, specify the
    algorithm.
7.  For **Trained model details**, enter the
    following:
    1. For **Name**, enter a unique name for the
       model in the collaboration.
    2. (Optional) For **Description**, enter a
       description of the trained model.
    3. For **Training data input mode**, choose
       one of the following:
       - Select **File** if you have a
         smaller dataset that can fit on the ML storage
         volume and you prefer traditional file system access
         for your training script.
       - Select **Pipe** for large
         datasets to stream data directly from S3, avoiding
         the need to download everything to disk, which can
         improve training speed and reduce storage
         requirements.
       - Select **FastFile** if you want
         to combine the benefits of streaming from S3 with
         file system access, especially for sequentially read
         data or when dealing with fewer files for faster
         startup times.

8.  For **ML input channel details**, do the
    following:
    1. For **ML input channel**, specify the ML
       input channel that provides data to the model algorithm.

    To add another channel, choose **Add another ML
    input channel**. You can add up to 19
    additional ML input channels. 2. For **Channel name**, enter the name of
    the ML input channel. 3. For **Amazon S3 data distribution type**,
    choose one of the following:

        * Select **Fully replicated** to
         give each training instance with a complete copy of
         your dataset. This works best when your dataset is
         small enough to fit in memory or when each instance
         needs access to all data.
        * Select **Sharded by S3 key** to
         divide your dataset across training instances based
         on S3 keys. Each instance receives about 1/n of the
         total S3 objects, where 'n' is the number of
         instances. This works best for large datasets that
         you want to process in parallel.

    ###### Note

    Consider your dataset size and training requirements
    when selecting a distribution type. **Fully
    replicated** provides complete data access
    but requires more storage, while **Sharded by S3
    key** enables distributed processing of
    large datasets.

9.  For **Maximum training duration**, choose the
    maximum amount of time you want to train your model.
10. For **Hyperparameters**, specify any
    algorithm-specific parameters and their intended values.
    Hyperparameters are specific to the model being trained and are used
    to fine-tune model training.
11. For **Environment variables**, specify any
    algorithm-specific variables and their intended values. Environment
    variables are set in the Docker container.
12. For **Encryption**, to use a custom
    AWS KMS key, select the **Encrypt secret with a custom
    KMS key** checkbox.
13. For **EC2 Resource configuration**, specify
    information about the compute resources that are used for model
    training.
    1. For **Instance type**, choose the type of
       instance you want to run.
    2. For **Instance count**, enter the number
       of instances.
    3. For **Volume size in GB**, enter the ML
       storage volume size.

14. Choose **Create trained model**.

API
To create a trained model (API)

The member with the ability to train a model starts training by selecting
the ML input channel and the model algorithm.

Run the following code with your specific parameters:

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.create_trained_model(
 membershipIdentifier= '`membership_id`',
 configuredModelAlgorithmAssociationArn = 'arn:aws:cleanrooms-ml:`region`:`account`:`membership`/membershipIdentifier/configured-model-algorithm-association/`identifier`',
 name='`trained_model_name`',
 resourceConfig={
 'instanceType': "ml.m5.xlarge",
 'volumeSizeInGB': 1
 },
 dataChannels=[
 {
 "mlInputChannelArn": channel_arn_1,
 "channelName": "`channel_name`"
 },
 {
 "mlInputChannelArn": channel_arn_2,
 "channelName": "`channel_name`"
 }
 ]
)`
```

###### Note

After the trained model is created, you can't edit it. To make changes, delete the
trained model and create a new one.
