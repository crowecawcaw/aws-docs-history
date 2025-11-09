Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Tutorial: Get started using the AWS SDK for Python (Boto3)

This tutorial describes how to build and train an Amazon Fraud Detector model and then using this model to
generate real-time fraud predictions using the AWS SDK for Python (Boto3). The model is trained using the
account registration example data file that you upload to Amazon S3 bucket.

By the end of this tutorial, you complete the following actions:

- Build and train an Amazon Fraud Detector model
- Generate real-time fraud predictions

## Prerequisites

The following are prerequisite steps for this tutorial.

- Completed [Set up for Amazon Fraud Detector](set-up.md "set-up.md").

If you have already [Set up AWS SDK](set-up.md#set-up-sdk "set-up.md#set-up-sdk"), make sure that you're using Boto3 SDK version 1.14.29 or higher.

- Followed instructions to [Get and upload example dataset](step-1-get-s3-data.md "step-1-get-s3-data.md") file that's required for this tutorial.

## Get started

Boto is the Amazon Web Services (AWS) SDK for Python. You can use it to create, configure,
and manage AWS services. For instructions on how to install Boto3, see [AWS SDK
for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html "https://boto3.amazonaws.com/v1/documentation/api/latest/index.html").

After you install AWS SDK for Python (Boto3), run the following Python example command to
confirm that your environment is configured correctly. If your environment is
configured correctly, the response contains a list of detectors. If no detectors
were created, the list is empty.

```
import boto3
fraudDetector = boto3.client('frauddetector')

response = fraudDetector.get_detectors()
print(response)

```

In this step, you create resources that are used to define model, event, and
rules.

#### Create variable

A variable is a data element from your dataset that you want to use to create
event type, model, and rules.

In the following example,the [CreateVariable](../api/API_CreateVariable.md "../api/API_CreateVariable.md") API is
used to create two variables. The variables are `email_address` and
`ip_address`. Assign them to the corresponding variable types:
`EMAIL_ADDRESS` and `IP_ADDRESS`. These variables are part of the example dataset you uploaded.
When you specify the variable type, Amazon Fraud Detector interprets the variable during model
training and when getting predictions. Only variables with an associated
variable type can be used for model training.

```
import boto3
fraudDetector = boto3.client('frauddetector')

 #Create variable email_address
fraudDetector.create_variable(
    name = 'email_address',
    variableType = 'EMAIL_ADDRESS',
    dataSource = 'EVENT',
    dataType = 'STRING',
    defaultValue = '<unknown>'
)

#Create variable ip_address
fraudDetector.create_variable(
    name = 'ip_address',
    variableType = 'IP_ADDRESS',
    dataSource = 'EVENT',
    dataType = 'STRING',
    defaultValue = '<unknown>'
)

```

#### Create entity type

An entity represents who is performing the event and an entity type classifies
the entity. Example classifications include _customer_,
_merchant_, or _account_.

In the following example, [PutEntityType](../api/API_PutEntityType.md "../api/API_PutEntityType.md") API is used to create a
`sample_customer` entity type.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_entity_type(
   name = 'sample_customer',
   description = 'sample customer entity type'
)


```

#### Create label

A label classifies an event as fraudulent or legitimate and is used to train
the fraud detection model. The model learns to classify events using these label
values.

In the following example, the [Putlabel](../api/API_PutLabel.md "../api/API_PutLabel.md") API is used to create two
labels, `fraud` and `legit`.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_label(
    name = 'fraud',
    description = 'label for fraud events'
)

fraudDetector.put_label(
    name = 'legit',
    description = 'label for legitimate events'
)

```

With Amazon Fraud Detector, you build models that evaluate risks and generate fraud predictions
for individual events. An event type defines the structure of an individual event.

In the following example, the [PutEventType](../api/API_PutEventType.md "../api/API_PutEventType.md") API is used to create an
event type `sample_registration`. You define the event type by specifying
the variables (`email_address`,`ip_address`), entity type
(`sample_customer`), and labels (`fraud`,
`legit`) that you created in the previous step.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_event_type (
     name = 'sample_registration',
     eventVariables = ['ip_address', 'email_address'],
     labels = ['legit', 'fraud'],
     entityTypes = ['sample_customer'])

```

Amazon Fraud Detector trains models to learn to detect fraud for a specific event type. In the
previous step, you created the event type. In this step, you create and train a
model for the event type. The model acts as a container for your model versions.
Each time you train a model, a new version is created.

Use following example codes to create and train an Online Fraud Insights model.
This model is called `sample_fraud_detection_model`. It's for the event
type `sample_registration` using the account registration example dataset
that you uploaded to Amazon S3.

For more information about different model types that Amazon Fraud Detector supports, see [Choose a model type](choosing-model-type.md "choosing-model-type.md").

**Create a model**

In the following example, the [CreateModel](../api/API_CreateModel.md "../api/API_CreateModel.md") API is used to create a
model.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_model (
       modelId = 'sample_fraud_detection_model',
       eventTypeName = 'sample_registration',
       modelType = 'ONLINE_FRAUD_INSIGHTS')

```

**Train a model**

In the following example, the [CreateModelVersion](../api/API_CreateModelVersion.md "../api/API_CreateModelVersion.md") API is used to train
the model. Specify `'EXTERNAL_EVENTS'` for the
`trainingDataSource` and the Amazon S3 location where you stored your
example dataset and the _RoleArn_ of the Amazon S3 bucket for
`externalEventsDetail`. For `trainingDataSchema`
parameter, specify how Amazon Fraud Detector interprets the example data. More specifically, specify
which variables to include and how to classify the event labels.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_model_version (
         modelId = 'sample_fraud_detection_model',
         modelType = 'ONLINE_FRAUD_INSIGHTS',
         trainingDataSource = 'EXTERNAL_EVENTS',
         trainingDataSchema = {
            'modelVariables' : ['ip_address', 'email_address'],
            'labelSchema' : {
               'labelMapper' : {
                   'FRAUD' : ['fraud'],
                   'LEGIT' : ['legit']
        }
    }
},
         externalEventsDetail = {
              'dataLocation' : 's3://`amzn-s3-demo-bucket`/`your-example-data-filename`.csv',
              'dataAccessRoleArn' : '`role_arn`'
}
)

```

You can train your model multiple times. Each time that you train a model, a new
version is created. After model training is complete, the model version status
updates to `TRAINING_COMPLETE`. You can review the model performance
score and other model performance metrics.

**Review model performance**

An important step in using Amazon Fraud Detector is to assess the accuracy of your model using
model scores and performance metrics. After model training is complete, Amazon Fraud Detector
validates model performance using the 15% of your data that wasn't used to train the
model. It generates a model performance score and other performance metrics.

Use the [DescribeModelVersions](../api/API_DescribeModelVersions.md "../api/API_DescribeModelVersions.md") API to review model performance. Look
at the **Model performance** overall score and all other metrics
generated by Amazon Fraud Detector for this model.

To learn more about the model performance score and performance metrics, see [Model scores](model-scores.md "model-scores.md") and [Model performance metrics](training-performance-metrics.md "training-performance-metrics.md").

You can expect all your trained Amazon Fraud Detector models to have real-world fraud detection
performance metrics, which are similar to the metrics in this tutorial.

**Deploy a model**

After you reviewed the performance metrics of your trained model, deploy the model
and make it available to Amazon Fraud Detector to generate fraud predictions. To deploy the trained
model, use the [UpdateModelVersionStatus](../api/API_UpdateModelVersionStatus.md "../api/API_UpdateModelVersionStatus.md") API. In the following example,
it's used to update the model version status to ACTIVE.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_model_version_status (
     modelId = 'sample_fraud_detection_model',
     modelType = 'ONLINE_FRAUD_INSIGHTS',
     modelVersionNumber = '1.00',
     status = 'ACTIVE'
)

```

A detector contains the detection logic, such as the models and rules. This logic
is for a particular event that you want to evaluate for fraud. A rule is a condition
that you specify to tell Amazon Fraud Detector how to interpret variable values during prediction.
And outcome is the result of a fraud prediction. A detector can have multiple
versions with each version having a status of _DRAFT_,
_ACTIVE_, or _INACTIVE_. A detector
version must have at least one rule that's associated with it.

Use the following example codes to create detector, rules, outcome, and to publish
the detector.

**Create a detector**

In the following example, the [PutDetector](../api/API_PutDetector.md "../api/API_PutDetector.md") API is used to create a
`sample_detector` detector for `sample_registration` event
type.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_detector (
     detectorId = 'sample_detector',
     eventTypeName = 'sample_registration'
)

```

**Create outcomes**

Outcomes are created for each possible fraud prediction result. In the following
example, the [PutOutcome](../api/API_PutOutcome.md "../api/API_PutOutcome.md") API is used to create three outcomes -
`verify_customer`, `review`, and `approve`.
These outcomes are later assigned to rules.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.put_outcome(
     name = 'verify_customer',
     description = 'this outcome initiates a verification workflow'
    )

fraudDetector.put_outcome(
     name = 'review',
     description = 'this outcome sidelines event for review'
    )

fraudDetector.put_outcome(
     name = 'approve',
     description = 'this outcome approves the event'
)


```

**Create rules**

Rule consists of one or more variables from your dataset, a logic
expression, and one or more outcomes.

In the following example, the [CreateRule](../api/API_CreateRule.md "../api/API_CreateRule.md") API is used to create three
different rules: `high_risk`, `medium_risk`, and
`low_risk`. Create rule expressions to compare the model performance
score `sample_fraud_detection_model_insightscore` value against various
thresholds. This is to determine the level of risk for an event and assign outcome
that was defined in the previous step.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_rule(
     ruleId = 'high_fraud_risk',
     detectorId = 'sample_detector',
     expression = '$sample_fraud_detection_model_insightscore > 900',
     language = 'DETECTORPL',
     outcomes = ['verify_customer']
     )

fraudDetector.create_rule(
     ruleId = 'medium_fraud_risk',
     detectorId = 'sample_detector',
     expression = '$sample_fraud_detection_model_insightscore <= 900 and $sample_fraud_detection_model_insightscore > 700',
     language = 'DETECTORPL',
     outcomes = ['review']
     )

fraudDetector.create_rule(
     ruleId = 'low_fraud_risk',
     detectorId = 'sample_detector',
     expression = '$sample_fraud_detection_model_insightscore <= 700',
     language = 'DETECTORPL',
     outcomes = ['approve']
     )


```

**Create a detector version**

A detector version defines model and rules that are used to get fraud
prediction.

In the following example, the [CreateDetectorVersion](../api/API_CreateDetectorVersion.md "../api/API_CreateDetectorVersion.md") API is used to
create a detector version. It does this by providing model version details, rules,
and a rule execution mode FIRST_MATCHED. A rule execution mode specifies the
sequence for evaluating rules. The rule execution mode FIRST_MATCHED specifies that
the rules are evaluated sequentially, first to last, stopping at first matched
rule.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_detector_version(
      detectorId = 'sample_detector',
      rules = [{
          'detectorId' : 'sample_detector',
          'ruleId' : 'high_fraud_risk',
          'ruleVersion' : '1'
},
{
          'detectorId' : 'sample_detector',
          'ruleId' : 'medium_fraud_risk',
          'ruleVersion' : '1'
},
{
          'detectorId' : 'sample_detector',
          'ruleId' : 'low_fraud_risk',
          'ruleVersion' : '1'
}
],
      modelVersions = [{
          'modelId' : 'sample_fraud_detection_model',
          'modelType': 'ONLINE_FRAUD_INSIGHTS',
          'modelVersionNumber' : '1.00'
}      ],
      ruleExecutionMode = 'FIRST_MATCHED'
)


```

The last step of this tutorial uses the detector `sample_detector`
created in the previous step to generate fraud predictions for
`sample_registration` event type in real time. The detector evaluates
the example data that's uploaded to Amazon S3. The response includes model performance
scores as well as any outcomes that are associated to the matched rules.

In the following example, the [GetEventPrediction](../api/API_GetEventPrediction.md "../api/API_GetEventPrediction.md") API is used to
provide data from a single account registration with each request. For this
tutorial, take data (email_address and ip_address) from the account registration
example data file. Each line (row) after the top header line represents data from a
single account registration event.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.get_event_prediction(
      detectorId = 'sample_detector',
      eventId = '802454d3-f7d8-482d-97e8-c4b6db9a0428',
      eventTypeName = 'sample_registration',
      eventTimestamp = '2020-07-13T23:18:21Z',
      entities = [{'entityType':'sample_customer', 'entityId':'12345'}],
 eventVariables = {
      'email_address': 'johndoe@exampledomain.com',
      'ip_address': '1.2.3.4'
}
)

```

After you completed this tutorial, you did the following:

- Uploaded an example event dataset to Amazon S3.
- Created variables, entities, and labels that are used to create and train
  a model.
- Created and trained a model using the example dataset.
- Viewed the model performance score and other performance metrics that
  Amazon Fraud Detector generated.
- Deployed the fraud detection model.
- Created a detector and added the deployed model.
- Added rules, the rule execution order, and outcomes to the
  detector.
- Created detector version.
- Tested the detector by providing different inputs and checking if the
  rules and rule execution order worked as expected.

## (Optional) Explore the Amazon Fraud Detector APIs with a

Jupyter (iPython) Notebook

For more examples for how to use the Amazon Fraud Detector APIs, see [aws-fraud-detector-samples GitHub repository](https://github.com/aws-samples/aws-fraud-detector-samples "https://github.com/aws-samples/aws-fraud-detector-samples"). The topics that the
notebooks cover include both building models and detectors using the Amazon Fraud Detector APIs and
making batch fraud prediction requests using the `GetEventPrediction`
API.
