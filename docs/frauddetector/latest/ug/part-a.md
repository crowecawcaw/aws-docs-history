

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Part A: Build, train, and deploy an Amazon Fraud Detector model
<a name="part-a"></a>

In part A, you define your business use case, define your event, build a model, train the model, evaluate model's performance, and deploy the model.

## Step 1: Choose your business use case
<a name="choose-business-use-case"></a>
+ In this step, you use the **data models explorer** to match your business use case with the fraud detection model types supported by Amazon Fraud Detector. Data models explorer is a tool integrated with the Amazon Fraud Detector console that recommends a model type to use for creating and training a fraud detection model for your business use case. Data models explorer also provides insights into the mandatory, recommended, and optional data elements you will require to include in your dataset. The dataset will be used to create and train your fraud detection model.

  For the purpose of this tutorial, your business use case is new account registrations. After you specify your business use case, the data models explorer will recommend a model type for creating a fraud detection model and will also provide you with a list of data elements you will need to create your dataset. Since you have already uploaded a sample dataset containing data from new account registrations, you do not need to create a new dataset.

  1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

  1. In the left navigation pane, choose **Data models explorer**.

  1. In the **Data models explorer** page, under **Business use case**, select **New account fraud**.

  1. Amazon Fraud Detector displays the recommended model type to use to create a fraud detection model for the selected business use case. The model type defines the algorithms, enrichments, and transformations Amazon Fraud Detector will use to train your fraud detection model.

     Make a note of the recommended model type. You will need this later when you create your model.

  1. The **Data model insights** pane provides insight into the mandatory and recommended data elements required to create and train a fraud detection model. 

     Take a look at the sample dataset you downloaded and make sure that it has all the mandatory and some recommended data elements listed in the table. 

     Later when you create a model for your specific business use case, you will use the insights provided to create your dataset.

## Step 2: Create event type
<a name="define-event"></a>
+ In this step, you define the business activity (event) to evaluate for fraud. Defining the event involves setting the variables that are in your dataset, the entity initiating event, and the labels that classify the event. For this tutorial, you define the account registration event.

  1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

  1. In the left navigation pane, choose **Events**.

  1. In the **Events type** page, choose **Create**.

  1. Under **Event type details**, enter `sample_registration` as the event type name and, optionally, enter a description of the event.

  1. For **Entity**, choose **Create entity**.

  1. In the **Create entity** page, enter `sample_customer` as the entity type name. Optionally, enter a description of the entity type.

  1. Choose **Create entity**.

  1. Under **Event variables**, for **Choose how to define this event's variables**, choose **Select variables from a training dataset**.

  1. For **IAM role**, choose **Create IAM role**.

  1. In the **Create IAM role** page, enter the name of the S3 bucket that you uploaded your example data to and choose **Create role**.

  1. In **Data location**, enter the path to your example data. This is the `S3 URI` path that you saved after uploading the example data. The path is similar to this: `S3://{{your-bucket-name}}/{{example dataset filename}}.csv`. 

  1. Choose **Upload**.

     Amazon Fraud Detector extracts the headers from your example data file and maps them with a variable type. The mapping is displayed in the console.

  1. Under **Labels - optional**, for **Labels**, choose **Create new labels**.

  1. In **Create label** page, enter `fraud` as the name. This label corresponds to the value that represents the fraudulent account registration in the example dataset. 

  1. Choose **Create label**.

  1. Create a second label, then enter `legit` as the name. This label corresponds to the value that represents the legitimate account registration in the example dataset.

  1. Choose **Create event type**.

## Step 3: Create model
<a name="step-3-create-new-ml-model"></a>

1. On the **Models** page, choose **Add model**, and then choose **Create model**.

1. For **Step 1 – Define model details**, enter `sample_fraud_detection_model` as the model name. Optionally, add a description of the model.

1. For **Model Type**, choose the **Online Fraud Insights** model. 

1. For **Event type**, choose **sample\_registration**. This is the event type that you created in Step 1.

1. In **Historical event data**, 

   1. In **Event data source**, choose **Event data stored in S3**.

   1. For **IAM role**, select the role that you created in Step 1.

   1. In **Training data location**, enter the S3 URI path to your example data file.

1. Choose **Next**.

## Step 4: Train model
<a name="step-4-training-data-assign-perms"></a>

1. In **Model inputs**, leave all checkboxes checked. By default, Amazon Fraud Detector uses all variables from your historical event dataset as model inputs.

1. In **Label classification**, for **Fraud labels** choose **fraud** as this label corresponds to the value that represents fraudulent events in the example dataset. For **Legitimate labels**, choose **legit** as this label corresponds to the value that represents legitimate events in the example dataset. 

1. For the **Unlabeled events treatment**, keep the default selection **Ignore unlabeled events** for this example dataset.

1. Choose **Next**.

1. After reviewing, choose **Create and train model**. Amazon Fraud Detector creates a model and begins to train a new version of the model.

   In **Model versions** the **Status** column indicates the status of model training. Model training that uses the example dataset takes approximately 45 minutes to complete. The status changes to **Ready to deploy** after model training is complete.