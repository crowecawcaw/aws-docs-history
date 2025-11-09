Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Outcomes

An outcome is the result of a fraud prediction. You can create an outcome for each possible fraud prediction result. For
example, you might want outcomes to represent risk levels (high_risk, medium_risk, and low_risk) or actions
(approve, review). After an outcome is created, you can add one or more outcomes to a rule. As part of the [GetEventPrediction](../api/API_GetEventPrediction.md "../api/API_GetEventPrediction.md") response, Amazon Fraud Detector returns the defined outcomes for any matched rule.
