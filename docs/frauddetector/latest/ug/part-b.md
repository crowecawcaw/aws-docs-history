

Amazon Fraud Detector is no longer open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker, AutoGluon, and AWS WAF.

# Part B: Generate fraud predictions
<a name="part-b"></a>

Fraud prediction is an evaluation of fraud for a business activity (event). Amazon Fraud Detector uses detectors to generate fraud prediction. A detector contains detection logic, such as models and rules, for a specific event that you want to evaluate for fraud. Detection logic uses rules to tell Amazon Fraud Detector how to interpret the data associated with the model. In this tutorial, you evaluate the account registration event using the account registration example dataset that you uploaded earlier. 

In Part A, you created, trained, and deployed your model. In Part B, you build a detector for the `sample_registration` event type, add the deployed model, create rules and a rule execution order, and then create and activate a version of the detector that you use to generate fraud predictions.

## Step 1: Build detector
<a name="step-1-create-app"></a>

**To create detector**

1. In the left navigation pane of the Amazon Fraud Detector console, choose **Detectors**.

1. Choose **Create detector**.

1. In the **Define detector details** page, enter `sample_detector` for detector name. Optionally, enter a description for the detector, such as `my sample fraud detector`.

1. For **Event Type**, select **sample\_registration**. This is the event that you created in Part A of this tutorial. 

1. Choose **Next**. 

## Step 2: Add model
<a name="add-model-detector"></a>

If you completed Part A of this tutorial, then you likely already have an Amazon Fraud Detector model that's available to add to your detector. If you didn't already create a model, go to Part A and complete the steps to create, train, and deploy a model and then continue with Part B. 

1. In the **Add model - optional**, choose **Add Model**.

1. In the **Add model** page, for **Select model**, choose the Amazon Fraud Detector model name that you deployed earlier. For **Select version**, choose the model version of the deployed model.

1. Choose **Add model**.

1. Choose **Next**.

## Step 3: Add rules
<a name="add-rules-to-detector"></a>

A rule is a condition that tells Amazon Fraud Detector how to interpret model performance score when evaluating for fraud prediction. For this tutorial, you create three rules: `high_fraud_risk`, `medium_fraud_risk`, and `low_fraud_risk`.

1. In the **Add rules** page, under **Define a rule**, enter `high_fraud_risk` for the rule name and under **Description - optional**, enter **This rule captures events with a high ML model score** as the description for the rule.

1. In **Expression**, enter the following rule expression using the Amazon Fraud Detector simpliﬁed rule expression language:

   `$sample_fraud_detection_model_insightscore > 900`

1. In **Outcomes**, choose **Create a new outcome**. An outcome is the result from a fraud prediction and is returned if the rule matches during an evaluation. 

1. In **Create a new outcome**, enter `verify_customer` as the outcome name. Optionally, enter a description.

1. Choose **Save outcome**. 

1. Choose **Add rule** to run the rule validation checker and save the rule. After it's created, Amazon Fraud Detector makes the rule available for use in your detector.

1. Choose **Add another rule**, and then choose the **Create rule** tab. 

1. Repeat this process twice more to create your `medium_fraud_risk` and `low_fraud_risk` rules using the following rule details: 
   + medium\_fraud\_risk

     Rule name: `medium_fraud_risk`

     Outcome: `review`

     Expression:

     `$sample_fraud_detection_model_insightscore <= 900 and`

     `$sample_fraud_detection_model_insightscore > 700`
   + low\_fraud\_risk

     Rule name: `low_fraud_risk`

     Outcome: `approve`

     Expression:

     `$sample_fraud_detection_model_insightscore <= 700`

   These values are examples used for this tutorial. When you create rules for your own detector, use values that are appropriate for your model and your use case,

1. After you have created all three rules, choose **Next**. 

   For more information about creating and writing rules, see [Rules](rules.md) and [Rule language reference](rule-language-reference.md).

## Step 4: Configure rule execution and rule order
<a name="get-start-define-rule-order"></a>

The rule execution mode for the rules that are included in the detector determines if all the rules you define are evaluated, or if rule evaluation stops at the first matched rule. And the rule order determines the order that you want the rule to be run in. 

The default rule execution mode is `FIRST_MATCHED`. 

**First matched**  
First matched rule execution mode returns the outcomes for the first matching rule based on defined rule order. If you specify `FIRST_MATCHED`, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud Detector then provides the outcomes for that single rule.   
The order that you run rules in can affect the resulting fraud prediction outcome. After you have created your rules, re-order the rules to run them in the desired order by following these steps:   
If your `high_fraud_risk` rule isn't already on the top of your rule list, choose **Order**, and then choose **1**. This moves `high_fraud_risk` to the first position.  
Repeat this process so that your `medium_fraud_risk` rule is in the second position and your `low_fraud_risk` rule is in the third position.

**All matched**  
All matched rule execution mode returns outcomes for all matched rules, regardless of rule order. If you specify `ALL_MATCHED`, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules.

Select `FIRST_MATCHED` for this tutorial and then choose **Next**.