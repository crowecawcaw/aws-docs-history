

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Update rule
<a name="update-rule"></a>

You can update a rule anytime by adding or updating the rule description, updating the rule expression, or adding or removing the outcome for the rule. When you update a rule a new rule version is created.

You can update a rule in the Amazon Fraud Detector console, using the [update-rule-version](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-rule-version.html) command, using the [UpdateRuleVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateRuleVersion.html) API, or using the using the AWS SDK.

After you have updated the rule, make sure to update your detector version to use the new rule version.

## Update rule in the Amazon Fraud Detector console
<a name="update-rule-console"></a>

**To update a rule,**

1. Open the [AWS Management Console](https://console.aws.amazon.com) and sign in to your account. Navigate to Amazon Fraud Detector.

1. In the left navigation pane, choose **Detectors**.

1. In the **Detectors** pane, select the detector that is associated with the rule you want to update.

1. In your detector page, choose **Associated rules** tab and select the rule you want to update.

1. In your rule page, choose **Actions** and select **Create version**.

1. Note that the version has changed. Enter updated description, expression, or outcome.

1. Choose **Save new version**

## Update rule using the AWS SDK for Python (Boto3)
<a name="update-rule-sdk"></a>

The following example code uses the [UpdateRuleVersion](https://docs.aws.amazon.com/frauddetector/latest/api/API_UpdateRuleVersion.html) API to update the threshold for the rule `high_risk` from 900 to 950. This rule is associated with the detector `payments_detector`.

```
fraudDetector.update_rule_version(
rule = {
    'detectorId' : 'payments_detector',
    'ruleId' : 'high_risk',
    'ruleVersion' : '1'
},
expression = '$sample_fraud_detection_model_insightscore > 950',
language = 'DETECTORPL',
outcomes = ['verify_customer']
)
```