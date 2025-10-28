Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Build a model

Amazon Fraud Detector models learn to detect fraud for a specific event type. In Amazon Fraud Detector, you first create a model, which acts as a container for your model versions. Each time you train a model, a new version is created. For details on how to create and train a model using the AWS Console see [Step 3: Create model](part-a.md#step-3-create-new-ml-model "part-a.md#step-3-create-new-ml-model").

Each model has a corresponding model score variable. Amazon Fraud Detector creates this variable on your behalf when you create a model. You can use this variable in your rule expressions to interpret your model scores during a fraud evaluation.

## Train and deploy a model using the AWS SDK for Python (Boto3)

A model version is created by calling the `CreateModel` and `CreateModelVersion` operations. `CreateModel` initiates the model, which acts as a container for your model versions. `CreateModelVersion` starts the training process, which results in a specific version of the model. A new version of the solution is created each time you call `CreateModelVersion`.

The following example shows a sample request for the `CreateModel` API. This example creates _Online Fraud Insights_ model type and assumes you have created an event type `sample_registration`.
For additional details about creating an event type, see [Create an event type](create-event-type.md "create-event-type.md").

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_model (
modelId = 'sample_fraud_detection_model',
eventTypeName = 'sample_registration',
modelType = 'ONLINE_FRAUD_INSIGHTS')

```

Train your first version using the [CreateModelVersion](../api/API_CreateModelVersion.md "../api/API_CreateModelVersion.md") API.

For the `TrainingDataSource` and `ExternalEventsDetail` specify the source and Amazon S3 location of the training data set. For the `TrainingDataSchema`
specify how Amazon Fraud Detector should interpret the training data, specifically which event variables to include and how to classify the event labels. By default, Amazon Fraud Detector ignores the
unlabeled events. This example code uses `AUTO` for `unlabeledEventsTreatment` to specify that Amazon Fraud Detector decides how to use the unlabeled events.

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
       unlabeledEventsTreatment = 'AUTO'
    }
},
externalEventsDetail = {
    'dataLocation' : 's3://bucket/file.csv',
    'dataAccessRoleArn' : 'role_arn'
}
)

```

A successful request will result in a new model version with status `TRAINING_IN_PROGRESS`. At any point during the training, you can cancel the training by calling `UpdateModelVersionStatus` and updating the status to `TRAINING_CANCELLED`. Once training is complete, the model version status will update to `TRAINING_COMPLETE`. You can review model performance using the Amazon Fraud Detector console or by calling `DescribeModelVersions`. For more information on how to interpret model scores and performance, see [Model scores](model-scores.md "model-scores.md") and [Model performance metrics](training-performance-metrics.md "training-performance-metrics.md").

After reviewing the model performance, activate the model to make it available to use by Detectors in real-time fraud predictions. Amazon Fraud Detector will deploy the model in multiple availability zones for redundancy with auto-scaling turned on to ensure the model scales with the number of fraud predictions you are making. To activate the model, call the `UpdateModelVersionStatus` API and update the status to `ACTIVE`.

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
