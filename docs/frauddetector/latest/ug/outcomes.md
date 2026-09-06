

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Outcomes
<a name="outcomes"></a>

An outcome is the result of a fraud prediction. You can create an outcome for each possible fraud prediction result. For example, you might want outcomes to represent risk levels (high\_risk, medium\_risk, and low\_risk) or actions (approve, review). After an outcome is created, you can add one or more outcomes to a rule. As part of the [GetEventPrediction](https://docs.aws.amazon.com/frauddetector/latest/api/API_GetEventPrediction.html) response, Amazon Fraud Detector returns the defined outcomes for any matched rule.