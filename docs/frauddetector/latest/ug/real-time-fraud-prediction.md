Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Real time prediction

You can evaluate online activities for fraud in real time by calling `GetEventPrediction` API. You provide information about a single event in
each request and synchronously receive a model score and an outcome based on the fraud prediction logic associated with the specified detector.

## How real time fraud prediction works

The `GetEventPrediction` API uses a specified detector version to evaluate the event metadata provided for the event. During the evaluation,
Amazon Fraud Detector first generates model scores for models that are added to the detector version, then passes the results to the rules for evaluation. The rules are
executed as specified by the rule execution mode (see [Create a detector version](create-a-detector-version.md "create-a-detector-version.md")).
As part of the response, Amazon Fraud Detector provides model scores as well as any outcomes associated to the matched rules.

## Getting real time fraud prediction

To get real time fraud predictions, make sure you have created and published a detector that contains your fraud prediction model and rules, or simply a ruleset.

You can get fraud prediction for an event in real time by calling the [GetEventPrediction](../api/API_GetEventPrediction.md "../api/API_GetEventPrediction.md") API
operation using the AWS Command Line Interface (AWS CLI) or one of the Amazon Fraud Detector SDKs.

To use the API, supply information of a single event with each request. As part of the request you must specify `detectorId` that Amazon Fraud Detector will use to evaluate the event. You can optionally specify a `detectorVersionId`.
If a `detectorVersionId` is not specified, Amazon Fraud Detector will use the `ACTIVE` version of the detector.

You can optionally send data to invoke an SageMaker AI model by passing the data in the field `externalModelEndpointBlobs`.

### Get a fraud prediction using the AWS SDK for Python (Boto3)

To generate a fraud prediction, call the `GetEventPrediction` API. The example below assumes you have completed [Part B: Generate fraud predictions](part-b.md "part-b.md"). As part of the response, you will receive a model score as well as any matched rules and corresponding outcomes. You can find additional examples of `GetEventPrediction` requests on the [aws-fraud-detector-samples GitHub repository](https://github.com/aws-samples/aws-fraud-detector-samples "https://github.com/aws-samples/aws-fraud-detector-samples").

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
    'email_address' : 'johndoe@exampledomain.com',
    'ip_address' : '1.2.3.4'
}
)

```
