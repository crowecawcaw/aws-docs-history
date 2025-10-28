# Using incremental training in

AWS Clean Rooms ML

Prerequisites:

- An AWS account with access to AWS Clean Rooms
- An existing trained model in a collaboration
- A new or updated dataset for incremental training
- Appropriate permissions to create and manage ML models in the
  collaboration
- Familiarity with the existing model's hyperparameters and configuration
  With incremental training, you can use the artifacts of an existing model and an
  updated dataset to train a new model. Incremental training saves both time and
  resources.

Use incremental training to:

- Train a new model using an expanded dataset that has an underlying pattern
  that wasn't accounted for in the earlier training.
- Train several variants of a model, either with different hyperparameters
  or using different datasets.

Console

###### To run an incremental training job (console)

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. In the left navigation pane, choose
   **Collaborations**.
3. On the **Collaborations** page, choose the
   collaboration in which the model artifacts you want to use for
   incremental training exist.
4. After the collaboration opens, choose the **ML
   models** tab.
5. Under **Custom ML models**, in the
   **Trained models** section, choose the
   radio button next to the trained model you want to incrementally
   train.
6. On the **Overview** page, under
   **Versions**,
   1. Choose the radio button next to the trained model you
      want to incrementally train.
   2. Choose **Train from version**.

7. On the **Create trained model from version**
   page, for **Trained model version**, choose the
   version.

The base model version is automatically selected. You can
change this version if other versions exist. 8. For **Trained model details**, enter the
following:

    1. For **Name**, enter a unique name for
     the model in the collaboration.
    2. (Optional) For **Description**, enter
     a description of the trained model.
    3. For **Training data input mode**,
     choose one of the following:




    	* Select **File** if you have a
    	 smaller dataset that can fit on the ML storage
    	 volume and you prefer traditional file system
    	 access for your training script.
    	* Select **Pipe** for large
    	 datasets to stream data directly from S3, avoiding
    	 the need to download everything to disk, which can
    	 improve training speed and reduce storage
    	 requirements.
    	* Select **FastFile** if you
    	 want to combine the benefits of streaming from S3
    	 with file system access, especially for
    	 sequentially read data or when dealing with fewer
    	 files for faster startup times.
    4. For **Incremental training channel
     name**, enter a name for the incremental
     training channel


    ###### Note

    If you specify the **Incremental training
     channel name** without a version ID, the
     system uses the base model for incremental training.

9.  For **ML input channel details**, do the
    following:
    1. For **ML input channel**, specify the
       ML input channel that provides data to the model
       algorithm.

    To add another channel, choose **Add another
    ML input channel**. You can add up to 19
    additional ML input channels. 2. For **Channel name**, enter the name
    of the ML input channel. 3. For **Amazon S3 data distribution type**,
    choose one of the following:

        * Select **Fully replicated**
         to give each training instance with a complete
         copy of your dataset. This works best when your
         dataset is small enough to fit in memory or when
         each instance needs access to all data.
        * Select **Sharded by S3 key**
         to divide your dataset across training instances
         based on S3 keys. Each instance receives about 1/n
         of the total S3 objects, where 'n' is the number
         of instances. This works best for large datasets
         that you want to process in parallel.

    ###### Note

    Consider your dataset size and training
    requirements when selecting a distribution type.
    **Fully replicated** provides
    complete data access but requires more storage,
    while **Sharded by S3 key** enables
    distributed processing of large datasets.

10. For **Maximum training duration**, choose the
    maximum amount of time you want to train your model.
11. For **Hyperparameters**, specify any
    algorithm-specific parameters and their intended values.
    Hyperparameters are specific to the model being trained and are
    used to fine-tune model training.
12. For **Environment variables**, specify any
    algorithm-specific variables and their intended values.
    Environment variables are set in the Docker container.
13. For **Encryption**, to use a custom
    AWS KMS key, select the **Encrypt secret with a
    custom KMS key** checkbox.
14. For **EC2 Resource configuration**, specify
    information about the compute resources that are used for model
    training.
    1. For **Instance type**, choose the
       type of instance you want to run.
    2. For **Instance count**, enter the
       number of instances.
    3. For **Volume size in GB**, enter the
       ML storage volume size.

15. Choose **Create trained model from version**.

API
To run an incremental training job (API)

Run the following code with your specific parameters:

```
`import boto3
acr_ml_client= boto3.client('cleanroomsml')

acr_ml_client.create_trained_model(
 membershipIdentifier= '`membership_id`',
 configuredModelAlgorithmAssociationArn = 'arn:aws:cleanrooms-ml:`region:account:membership`/membershipIdentifier/configured-model-algorithm-association/`identifier`',
 name='`trained_model_name`',
 resourceConfig={
 'instanceType': 'ml.m5.xlarge',
 'volumeSizeInGB': 1
 },
 incrementalTrainingDataChannels=[
 {
 'trainedModelArn': trained_model_arn,
 'channelName': '`channel_name`'
 },
 ]
 dataChannels=[
 {
 'mlInputChannelArn': channel_arn_1,
 'channelName': '`channel_name`'
 },
 {
 'mlInputChannelArn': channel_arn_2,
 'channelName': '`channel_name`'
 }
 ]
)`
```

###### Note

Limit: Maximum of 20 channels total (including both
`dataChannels` and
`incrementalTrainingDataChannels`).

###### Note

After the trained model is created, you can't edit it. To make changes, delete
the trained model and create a new one.
