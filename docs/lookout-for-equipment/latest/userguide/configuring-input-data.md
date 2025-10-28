On October 7, 2026, AWS will discontinue support for
Amazon Lookout for Equipment. After October 7, 2026, you will no longer be
able to access the Lookout for Equipment console or resources. For more
information,
[see the following](https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/ "https://aws.amazon.com/blogs/machine-learning/preserve-access-and-explore-alternatives-for-amazon-lookout-for-equipment/").

# Configuring your input data

## Choosing your training and

evaluation settings.

You can use Lookout for Equipment to train a model in one of the following ways:

- **Training set, no evaluation set, and no
  labels**

The data you have ingested so far becomes, in its entirety, the entire
basis for creating the model. Lookout for Equipment gets its concept of normal equipment
behavior (and abnormal behavior?) from the one set of data that has been
ingested. All of the data uploaded during the ingestion phase becomes
training data, no labeled data is used in the model training process. No
data is designated for evaluating the model. Once the model has been
created, its first use will be in production, on the real-time data
streaming from your equipment.

This setup requires the least amount of time and effort. But in the long
run, a model set up this way may be less accurate than using one of the
mehtods below.

- **Training set, evaluation set, and no
  labels**

You divide the data you've uploaded so far (during the ingestion phase)
into two parts: training data and evaluation data. Lookout for Equipment uses the training
data to learn about normal (and abnormal?) behavior for your equipment.
Then, Lookout for Equipment puts the model to the test on the evaluation data. You examine
the model's performance on the evaluation data, and on that basis, you
decide if the model is useful. You don't give Lookout for Equipment any direct indication of
what you consider to be anomalous behavior for your equipment.

- **Training set, no evaluation set, and
  labels**

You don't divide the ingested data into training data and evaluation data.
It's all training data. But you do provide labeled data that indicates
anomalous behavior.

- Training set, evaluation set, and labels

You identify some of the ingested data as training data, and the rest of
it as evaluation data. You also provide labeled data that indicates periods
of anomalous behavior. This option may be the most work to set up in the
short term, but it may lead to a more accurate model in the long
term.

## Training, evaluating, and

sampling

Now you'll need to decide how to split up your data between the training subset
and the evaluation subset. The bigger the training set, the more data contributes to
building your model. The bigger the evaluation set, the more chances you’ll get to
see how your model functions before you deploy it to production. A common breakdown
is 80% training and 20% evaluation.

1. Choose the time range indicating your training data subset.
2. Choose the time range indicating your evaluation data subset.
3. Choose your sample rate. This is the rate at which the data will be
   sampled. A lower sample rate means that less data will be used, but the
   model will build faster. A higher sample rate means that more data will be
   used, but the model will take longer to build.
4. Enter your off-time indicators (optional).

When your asset is off, Lookout for Equipment may interpret the absence of data as a
beharioral anomaly (or as normal behavior). In order to prevent this, it's
helpful to give Lookout for Equipment a clear indicator of whether or not your asset has
been turned off. Choose one particular sensor whose status is indicative of
whether your asset is active.

Now that you've configured your input data, the next step is to decide whether or not to use [data labels](labeling-data.md "labeling-data.md").

If you already know that you do not want to label your data, you can skip ahead to [Starting the training process](reviewing-settings.md "reviewing-settings.md").
