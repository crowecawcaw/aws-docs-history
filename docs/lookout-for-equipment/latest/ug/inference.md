On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Scheduling inference

###### Note

You can also schedule inference [with the
AWS SDK for Python (Boto)](SDK-examples.md#create-model-sdk "SDK-examples.md#create-model-sdk").

## Starting inference

After you create a model, you can use it to monitor your asset in real time. To use
your model to monitor your asset, you do the following.

To schedule inference, you specify the model, the schedule, the Amazon S3 location of
where the model is reading the data, and where it outputs the results of the
inference.

1. Sign in to AWS Management Console and open the Amazon Lookout for Equipment console at [Amazon Lookout for Equipment
   console](https://console.aws.amazon.com/lookoutequipment/home "https://console.aws.amazon.com/lookoutequipment/home").
2. Choose **Models**. Then choose the model that monitors your
   asset.
3. Choose **Schedule inference**.
4. For **Inference schedule name**, specify the name for the
   inference schedule.
5. For **Model**, choose the model that is monitoring the data
   coming from your asset.
6. For **S3 location** under **Input data**,
   specify the Amazon S3 location of the input data coming from the asset.
7. For **Data upload frequency**, specify how often your asset
   sends the data to the Amazon S3 bucket.
8. For **S3 location** under **Output data**,
   specify the Amazon S3 location to store the output of the inference results.
9. For **IAM role** under **Access
   Permissions**, specify the IAM role that provides Amazon Lookout for Equipment with
   access to your data in Amazon S3.
10. Choose **Schedule inference**.
