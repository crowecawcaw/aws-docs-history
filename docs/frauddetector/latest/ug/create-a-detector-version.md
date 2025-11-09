Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create a detector version

A detector version defines the rules, rule execution order, and optionally a model version, that will be used as part of the request for generating fraud predictions. You can add any of the rules defined within a detector to the detector version. You can also add any model trained on the evaluated event type.

Each detector version has a status of `DRAFT`, `ACTIVE`, or `INACTIVE`. Only one detector version can be in `ACTIVE` status at a time. During the `GetEventPrediction` request, Amazon Fraud Detector will use the `ACTIVE` detector if no `DetectorVersion` is specified.

## Rule execution mode

Amazon Fraud Detector supports two different rule execution modes: `FIRST_MATCHED` and `ALL_MATCHED`.

- If the rule execution mode is `FIRST_MATCHED`, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud Detector then provides the outcomes for that single rule. If a rule evaluates to false (not matched), the next rule in the list is evaluated.
- If the rule execution mode is `ALL_MATCHED`, then all rules in an evaluation are executed in parallel, regardless of their order. Amazon Fraud Detector executes all rules and returns the defined outcomes for every matched rule.

## Create a detector version using the AWS SDK for Python (Boto3)

The following example shows a sample request for the `CreateDetectorVersion` API.
The rule execution mode is set to `FIRST_MATCHED`, therefore Amazon Fraud Detector will evaluate rules sequentially, first to last, stopping at the first matched rule.
Amazon Fraud Detector then provides the outcomes for that single rule during the `GetEventPrediction response`.

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
}],
ruleExecutionMode = 'FIRST_MATCHED'
)

```

To update the status of a detector version, use the `UpdateDetectorVersionStatus` API.
The following example updates the detector version status from `DRAFT` to `ACTIVE`.
During a `GetEventPrediction` request, if a detector ID is not specified,
Amazon Fraud Detector will use the `ACTIVE` version of the detector.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.update_detector_version_status(
detectorId = 'sample_detector',
detectorVersionId = '1',
status = 'ACTIVE'
)

```
