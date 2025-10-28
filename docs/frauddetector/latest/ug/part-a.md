Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Part A: Build, train, and deploy an Amazon Fraud Detector model

In part A, you define your business use case, define your event, build a model, train the model, evaluate model's performance, and deploy the model.

- In this step, you use the **data models explorer** to match your business use case with the fraud detection
  model types supported by Amazon Fraud Detector. Data models explorer is a tool integrated with the Amazon Fraud Detector console that recommends a model type to use for creating
  and training a fraud detection model for your business use case. Data models explorer also provides insights into the mandatory, recommended, and
  optional data elements you will require to include in your dataset. The dataset will be used to create and train your fraud detection model.

For the purpose of this tutorial, your business use case is new account registrations. After you specify your business use case, the data
models explorer will recommend a model type for creating a fraud detection model and will also provide you with a list of data elements you will
need to create your dataset. Since you have already uploaded a sample dataset containing data from new account registrations, you do not need to
create a new dataset.

    1. Open the [AWS
     Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
     Navigate to Amazon Fraud Detector.
    2. In the left navigation pane, choose
     **Data models explorer**.
    3. In the **Data models explorer** page, under **Business use case**, select **New account fraud**.
    4. Amazon Fraud Detector displays the recommended model type to use to create a fraud detection model for the selected business use case.
     The model type defines the algorithms, enrichments, and transformations Amazon Fraud Detector will use to train your fraud detection model.


    Make a note of the recommended model type. You will need this later when you create your model.
    5. The **Data model insights** pane provides insight into the mandatory and recommended data elements required to create and train a fraud detection model.



    Take a look at the sample dataset you downloaded and make sure that it has all the mandatory and some recommended data elements listed in the table.


    Later when you create a model for your specific business use case, you will use the insights provided to create your dataset.

- In this step, you define the business activity (event) to evaluate for fraud. Defining the event involves
  setting the variables that are in your dataset, the entity initiating event, and the labels that classify the event.
  For this tutorial, you define the account registration event.
  1.  Open the [AWS
      Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
      Navigate to Amazon Fraud Detector.
  2.  In the left navigation pane, choose
      **Events**.
  3.  In the **Events type** page, choose
      **Create**.
  4.  Under **Event type details**, enter
      `sample_registration` as the event type name
      and, optionally, enter a description of the event.
  5.  For **Entity**, choose **Create
      entity**.
  6.  In the **Create entity** page, enter
      `sample_customer` as the entity type name.
      Optionally, enter a description of the entity type.
  7.  Choose **Create entity**.
  8.  Under **Event variables**, for
      **Choose how to define this event's
      variables**, choose **Select variables
      from a training dataset**.
  9.  For **IAM role**, choose **Create
      IAM role**.
  10. In the **Create IAM role** page, enter
      the name of the S3 bucket that you uploaded your example
      data to and choose **Create role**.
  11. In **Data location**, enter the path to
      your example data. This is the `S3 URI` path that
      you saved after uploading the example data. The path is
      similar to this:
      `S3://`your-bucket-name`/`example
      dataset filename`.csv`.
  12. Choose **Upload**.

  Amazon Fraud Detector extracts the headers from your example data file and
  maps them with a variable type. The mapping is displayed in
  the console. 13. Under **Labels - optional**, for
  **Labels**, choose **Create new
  labels**. 14. In **Create label** page, enter
  `fraud` as the name. This label corresponds
  to the value that represents the fraudulent account
  registration in the example dataset. 15. Choose **Create label**. 16. Create a second label, then enter `legit` as
  the name. This label corresponds to the value that
  represents the legitimate account registration in the
  example dataset. 17. Choose **Create event type**.

1. On the **Models** page, choose **Add
   model**, and then choose **Create
   model**.
2. For **Step 1 – Define model details**, enter
   `sample_fraud_detection_model` as the model name.
   Optionally, add a description of the model.
3. For **Model Type**, choose the **Online
   Fraud Insights** model.
4. For **Event type**, choose
   **sample_registration**. This is the event type
   that you created in Step 1.
5. In **Historical event data**,
   1. In **Event data source**, choose
      **Event data stored in S3**.
   2. For **IAM role**, select the role that
      you created in Step 1.
   3. In **Training data location**, enter the
      S3 URI path to your example data file.

6. Choose **Next**.
7. In **Model inputs**, leave all checkboxes
   checked. By default, Amazon Fraud Detector uses all variables from your historical
   event dataset as model inputs.
8. In **Label classification**, for **Fraud
   labels** choose **fraud** as this
   label corresponds to the value that represents fraudulent events in
   the example dataset. For **Legitimate labels**,
   choose **legit** as this label corresponds to the
   value that represents legitimate events in the example dataset.
9. For the **Unlabeled events treatment**, keep the default selection **Ignore unlabeled events**
   for this example dataset.
10. Choose **Next**.
11. After reviewing, choose **Create and train
    model**. Amazon Fraud Detector creates a model and begins to train a new
    version of the model.

In **Model versions** the
**Status** column indicates the status of model
training. Model training that uses the example dataset takes
approximately 45 minutes to complete. The status changes to
**Ready to deploy** after model training is
complete.
An important step in using Amazon Fraud Detector is to assess the accuracy of your model
using model scores and performance metrics. After model training is
complete, Amazon Fraud Detector validates model performance using the 15% of your data that
wasn't used to train the model and generates a model performance score and
other performance metrics.

1. To view model's performance,
   1. In the left navigation pane of the Amazon Fraud Detector console, choose
      **Models**.
   2. In the **Models** page, choose the model
      that you just trained
      (**sample_fraud_detection_model**), and
      then choose **1.0**. This is the version
      Amazon Fraud Detector created of your model.

2. Look at the **Model performance** overall score
   and all other metrics that Amazon Fraud Detector generated for this model.

To learn more about the model performance score and performance
metrics on this page, see [Model scores](model-scores.md "model-scores.md") and [Model performance metrics](training-performance-metrics.md "training-performance-metrics.md").

You can expect all your trained Amazon Fraud Detector models to have real-world
fraud detection performance metrics that are similar to the
performance metrics that you see for the model in this
tutorial.
After you reviewed the performance metrics of your trained model and are
ready to use it generate fraud predictions, you can deploy the model.

1. In left navigation pane of the Amazon Fraud Detector console, choose
   **Models**.
2. In the **Models** page, choose
   **sample_fraud_detection_model**, and then
   choose the specific model version that you want to deploy. For this
   tutorial, choose **1.0**.
3. On the **Model version** page, choose
   **Actions** and then choose **Deploy
   model version**.
4. In the **Model versions**, the
   **Status** shows the status of the deployment.
   The status changes to **Active** after the
   deployment completes. This indicates that the model version is
   activated and available to generate fraud predictions. Continue with
   [Part B: Generate fraud predictions](part-b.md "part-b.md") to complete
   steps for generating fraud predictions.
