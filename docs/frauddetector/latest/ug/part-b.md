Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Part B: Generate fraud predictions

Fraud prediction is an evaluation of fraud for a business activity (event). Amazon Fraud Detector
uses detectors to generate fraud prediction. A detector contains detection logic,
such as models and rules, for a specific event that you want to evaluate for fraud.
Detection logic uses rules to tell Amazon Fraud Detector how to interpret the data associated with
the model. In this tutorial, you evaluate the account registration event using the
account registration example dataset that you uploaded earlier.

In Part A, you created, trained, and deployed your model. In Part B, you build a
detector for the `sample_registration` event type, add the deployed
model, create rules and a rule execution order, and then create and activate a
version of the detector that you use to generate fraud predictions.

###### To create detector

1. In the left navigation pane of the Amazon Fraud Detector console, choose
   **Detectors**.
2. Choose **Create detector**.
3. In the **Define detector details** page, enter
   `sample_detector` for detector name. Optionally,
   enter a description for the detector, such as `my sample fraud
detector`.
4. For **Event Type**, select
   **sample_registration**. This is the event that
   you created in Part A of this tutorial.
5. Choose **Next**.
   If you completed Part A of this tutorial, then you likely already have an
   Amazon Fraud Detector model that's available to add to your detector. If you didn't already
   create a model, go to Part A and complete the steps to create, train, and
   deploy a model and then continue with Part B.

6. In the **Add model - optional**, choose
   **Add Model**.
7. In the **Add model** page, for **Select
   model**, choose the Amazon Fraud Detector model name that you deployed
   earlier. For **Select version**, choose the model
   version of the deployed model.
8. Choose **Add model**.
9. Choose **Next**.
   A rule is a condition that tells Amazon Fraud Detector how to interpret model performance
   score when evaluating for fraud prediction. For this tutorial, you create
   three rules: `high_fraud_risk`, `medium_fraud_risk`,
   and `low_fraud_risk`.

10. In the **Add rules** page, under **Define
    a rule**, enter `high_fraud_risk` for the
    rule name and under **Description - optional**,
    enter `This rule captures events with a high ML model
score` as the description for the rule.
11. In **Expression**, enter the following rule
    expression using the Amazon Fraud Detector simpliﬁed rule expression
    language:

`$sample_fraud_detection_model_insightscore >
 900` 3. In **Outcomes**, choose **Create a new
outcome**. An outcome is the result from a fraud
prediction and is returned if the rule matches during an evaluation. 4. In **Create a new outcome**, enter
`verify_customer` as the outcome name. Optionally,
enter a description. 5. Choose **Save outcome**. 6. Choose **Add rule** to run the rule validation
checker and save the rule. After it's created, Amazon Fraud Detector makes the rule
available for use in your detector. 7. Choose **Add another rule**, and then choose the
**Create rule** tab. 8. Repeat this process twice more to create your
`medium_fraud_risk` and `low_fraud_risk`
rules using the following rule details:

    * medium\_fraud\_risk


    Rule name: `medium_fraud_risk`


    Outcome: `review`


    Expression:


    `$sample_fraud_detection_model_insightscore <= 900
     and`


    `$sample_fraud_detection_model_insightscore >
     700`
    * low\_fraud\_risk


    Rule name: `low_fraud_risk`


    Outcome: `approve`


    Expression:


    `$sample_fraud_detection_model_insightscore <=
     700`

These values are examples used for this tutorial. When you create
rules for your own detector, use values that are appropriate for
your model and your use case, 9. After you have created all three rules, choose
**Next**.

For more information about creating and writing rules, see [Rules](rules.md "rules.md") and
[Rule language reference](rule-language-reference.md "rule-language-reference.md").
The rule execution mode for the rules that are included in the detector
determines if all the rules you define are evaluated, or if rule evaluation
stops at the first matched rule. And the rule order determines the order
that you want the rule to be run in.

The default rule execution mode is `FIRST_MATCHED`.

**First matched**

First matched rule execution mode returns the outcomes for the
first matching rule based on defined rule order. If you specify
`FIRST_MATCHED`, Amazon Fraud Detector evaluates rules
sequentially, first to last, stopping at the first matched rule.
Amazon Fraud Detector then provides the outcomes for that single rule.

The order that you run rules in can affect the resulting fraud
prediction outcome. After you have created your rules, re-order
the rules to run them in the desired order by following these
steps:

If your `high_fraud_risk` rule isn't already on the
top of your rule list, choose **Order**, and
then choose **1**. This moves
`high_fraud_risk` to the first position.

Repeat this process so that your
`medium_fraud_risk` rule is in the second
position and your `low_fraud_risk` rule is in the
third position.

**All matched**

All matched rule execution mode returns outcomes for all
matched rules, regardless of rule order. If you specify
`ALL_MATCHED`, Amazon Fraud Detector evaluates all rules and
returns the outcomes for all matched rules.

Select `FIRST_MATCHED` for this tutorial and then choose
**Next**.

A detector version defines the specific models and rules that are used for
generating fraud predictions.

1. In the **Review and create** page, review the
   detector details, models, and rules that you configured. If you need
   to make any changes, choose **Edit** next to the
   corresponding section.
2. Choose **Create detector**. After it's created,
   the ﬁrst version of your detector appears in the Detector versions
   table with `Draft` status.

You use the **Draft** version to test your
Detector.
In the Amazon Fraud Detector console, you can test the logic of your detector using a mock
data with the **Run test** feature. For this tutorial, you
can use account registration data from the example dataset.

1. Scroll to **Run test** at the bottom of the
   **Detector version details** page.
2. For **Event metadata**, enter a timestamp of when
   the event occurred and enter a unique identifier for the entity
   performing the event. For this tutorial, select a date from the date
   picker for timestamp, and enter “1234” for the Entity ID.
3. For **Event variable**, enter the variable values
   that you want to test. For this tutorial, you only need the
   `ip_address` and `email_address` fields.
   This is because they are the inputs that are used to train your
   Amazon Fraud Detector model. You can use the following example values. This assumes
   that you used the suggested variable names:
   - ip_address: `205.251.233.178`
   - email_address: `johndoe@exampledomain.com`

4. Choose **Run test**.
5. Amazon Fraud Detector returns the fraud prediction outcome based on the rule
   execution mode. If the rule execution mode is
   `FIRST_MATCHED`, the returned outcome corresponds to
   the first rule that matched. The first rule is the rule with the
   highest priority. It's matched if it's evaluated as true. If the
   rule execution mode is `ALL_MATCHED`, the returned
   outcome corresponds to all rules that matched. That means that
   they're all evaluated to be true. Amazon Fraud Detector also returns the model score
   for any models added to your detector.

You can change the inputs and run couple of tests to see different
outcomes. You can use the _ip_address_ and
_email_address_ values from your example
dataset for the tests and check if the outcomes are as
expected. 6. When you're satisfied with how the detector is working, promote it
from `Draft` to `Active`. Doing so makes the
detector available for use in real-time fraud detection.

On the **Detector version details** page, choose
**Actions**, **Publish**,
**Publish version**. This changes the status of
the detector from **Draft** to
**Active.**

At this point, your model and the associated detector logic are
ready to evaluate online activities for fraud in real time using the
Amazon Fraud Detector `GetEventPrediction` API. You can also evaluate
events offline using a CSV input file and the
`CreateBatchPredictionJob` API. For more information
about fraud prediction, see [Fraud predictions](getting-fraud-predictions.md "getting-fraud-predictions.md")
By completing this tutorial, you did the following:

- Uploaded an example event dataset to Amazon S3.
- Created and trained an Amazon Fraud Detector fraud detection model using the
  example dataset.
- Viewed the model performance score and other performance metrics
  that Amazon Fraud Detector generated.
- Deployed the fraud detection model.
- Created a detector and added the deployed model.
- Added rules, the rule execution order, and outcomes to the
  detector.
- Tested the detector by providing different inputs and checking if
  the rules and rule execution order worked as expected.
- Activated the detector by publishing it.
