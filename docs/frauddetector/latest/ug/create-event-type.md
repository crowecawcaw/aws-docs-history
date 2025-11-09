Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create an event type

Before you create your fraud detection model, you must first create an event type. Creating an event type involves defining your business activity (event) to evaluate for fraud. Defining the event involves
identifying the event variables in your dataset to include for fraud evaluation, specifying the entity initiating event, and the labels that classify the event.

**Prerequisites for creating an event type**

Before you start to create your event type, make sure that you have completed the following:

- Used the [Data models explorer](create-event-dataset.md#data-models-explorer "create-event-dataset.md#data-models-explorer") tool
  to gain insights into the data elements required by Amazon Fraud Detector to create your fraud detection model.
- Used the insights you got from the Data Models Explorer to create your event dataset and have uploaded your dataset to Amazon S3 bucket.
- Created [Variables](variables.md "variables.md"), [Entity](entity.md "entity.md"),
  and [Labels](labels.md "labels.md") you want Amazon Fraud Detector to use for creating a fraud detection model for this event.
  Make sure that the variables, entity type, and labels you created are included in your event dataset.
  You can create your event type in the Amazon Fraud Detector console, using the API, using the AWS CLI, or using the AWS SDK.

## Create event type in the Amazon Fraud Detector console

###### To create an event type,

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose
   **Events**.
3. In the **Events type** page, choose
   **Create**.
4. Under **Event type details,**,
   1. In the **Name**, enter the name of your event.
   2. In the **Description**, optionally, enter a description.
   3. In the **Entity**, select the entity type you created for your event.

5. Under **Event variables**,
   1. In the **Choose how to define this event's variables**,
      - If you have already created your event variables for this event, select **Select variables from your variable list** and
        in the **Variables**, select the variables you created for this event.
      - If you have not created variables for this event, select **Select variables from a training dataset**,
        - In the **IAM role** select the IAM Role you want Amazon Fraud Detector to use to access the Amazon S3 bucket that contains your dataset
        - In the **Data location** enter the path to your dataset location. Use the `S3 URI` path that is
          similar to this: `S3://`your-bucket-name`/`example
          dataset filename`.csv`.
        - Choose **Upload**.
        - Under **Variables**, all the event variable names that Amazon Fraud Detector has extracted from your dataset file is displayed.

        If you want the variable to be included for detecting fraud, in the **Variable type**, select the variable type. Choose **Remove**
        to remove the variables from being included for fraud detection. Repeat this step for each variable in the list.

6. Under **Labels (optional)**, in the **Labels**, select the labels you created for this event.
   Make sure to select one label each for fraudulent and legitimate events.
7. If you want to setup automatic downstream processing for this event, under **Event orchestration with Amazon EventBridge - optional**, turn on **Enable event orchestration with Amazon EventBridge**.
   For more information about event orchestration, see [Event orchestration](event-orchestration.md "event-orchestration.md").

###### Note

You can also enable event orchestration later after creating your event type. 8. Choose **Create event type**.

## Create an event type using the AWS SDK for Python (Boto3)

The following example shows a sample request for the `PutEventType` API. The example assumes you have created the variables `ip_address` and `email_address`, the labels `legit` and `fraud`, and the entity type `sample_customer`. For information about how to create these resources, see [Resources](create-resources.md "create-resources.md").

###### Note

You must first create variables, entity types, and labels prior to adding them to the event type.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_event_type (
name = 'sample_registration',
eventVariables = ['ip_address', 'email_address'],
labels = ['legit', 'fraud'],
entityTypes = ['sample_customer'])

```
