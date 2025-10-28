Amazon Fraud Detector will no longer be open to new customers starting November 7, 2025. If you would like to use Amazon Fraud Detector,
sign up prior to that date. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Create rules

You can create rules in Amazon Fraud Detector console, using the [create-rule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-rule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-rule.html") command,
using the [CreateRule](../api/API_CreateRule.md "../api/API_CreateRule.md") API, or using the AWS SDK for Python (Boto3).

Each rule must contain a single expression that captures your business logic. All expressions must evaluate to a Boolean value (true or false)
and be less than 4,000 characters in length. If-else type conditions are not supported. All variables used in the expression must be predefined in the evaluated event type.
Similarly, all lists used in the expression must be predefined, associated with a varible type, and be populated with entries.

The following example creates a rule `high_risk` for an existing detector `payments_detector`. The rule associates an expression and an outcome `verify_customer` with the rule.

**Prerequisites**

To follow the steps mentioned below, make sure that you complete the following before you proceed with creating rules:

- [Create a detector](create-a-detector.md "create-a-detector.md")
- [Create an outcome](create-an-outcome.md "create-an-outcome.md")
  If you are creating a detector, rule, and outcome for your use case, replace the example detector name, rule name, rule expression and outcome
  name with the names and expressions relevant to your use case.

## Create a new rule in the Amazon Fraud Detector console

1. Open the [AWS
   Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com") and sign in to your account.
   Navigate to Amazon Fraud Detector.
2. In the left navigation pane, choose **Detectors** and select the detector you created for your use case, example **payments_detector**.
3. In the **payments_detector** page, choose **Associated rules** tab and then choose **Create rule**.
4. In the **New rule** page, enter the following:
   1. In the **Name**, enter a name for the rule, example `high_risk`
   2. In the **Description - optional**, optionally enter a rule description, example, `This rule captures events with a high ML model
score`
   3. In the **Expression**, enter a rule expression for your use case using the **Expression quick reference guide**. Example `$sample_fraud_detection_model_insightscore >900`
   4. In the **Outcomes**, choose the outcome you created for your use case, example **verify_customer**. An outcome is the result from a fraud
      prediction and is returned if the rule matches during an evaluation.

5. Choose **Save rule**

You created a new rule for your detector. This is the version 1 of the rule which Amazon Fraud Detector automatically makes it available for the detector to use.

## Create a rule using the AWS SDK for Python (Boto3)

The following example code uses [CreateRule](../api/API_CreateRule.md "../api/API_CreateRule.md") API to create a rule `high_risk`
for an existing detector `payments_detector`. The example code also adds a rule expression and an outcome `verify_customer` to the rule.

**Prerequisites**

To use the example code, make sure that you have complete the following before you proceed with creating rules:

- [Create a detector](create-a-detector.md "create-a-detector.md")
- [Create an outcome](create-an-outcome.md "create-an-outcome.md")

If you are creating a detector, rule, and outcome for your use case, replace the example detector name, rule name, rule expression and outcome
name with names and expression relevant to your use case.

```
import boto3
fraudDetector = boto3.client('frauddetector')

fraudDetector.create_rule(
ruleId = 'high_risk',
detectorId = 'payments_detector',
expression = '$sample_fraud_detection_model_insightscore > 900',
language = 'DETECTORPL',
outcomes = ['verify_customer']
)

```

You have created the version 1 of the rule which Amazon Fraud Detector automatically makes it available for the detector to use.
