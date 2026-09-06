

# Creating a safety rule on the console
<a name="routing-control.create-safety-rule"></a>

The steps in this section explain how to create a safety rule on the ARC console. The steps are similar whether you create an assertion rule or a gating rule. The differences are noted in the procedure.

To learn about using recovery and routing control API operations with Amazon Application Recovery Controller (ARC), see [Routing control API operations](actions.routing-control.md).

# To create a safety rule


1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard). 

1. Choose **Routing control**.

1. On the **Routing control** page, choose a control panel.

1. On the control panel details page, choose **Action**, and then choose **Add safety rule**.

1. Choose a type of rule to add: **Assertion rule** or **Gating rule**.

1. Choose a name and, optionally, change the wait period.

1. Specify the configuration options for the safety rule.
   + For an assertion rule, specify the asserted routing controls.
   + For a gating rule, specify the gating routing control and target routing controls.

   For both rules, specify the rule configuration by choosing the type and threshold, and whether the rule is inverted.
**Note**  
To learn more about specifying an assertion rule, see the information provided for [AssertionRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-assertionrule) operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller. To learn more about specifying a gating rule, see the information provided for the [GatingRule](https://docs.aws.amazon.com/recovery-cluster/latest/api/safetyrule.html#safetyrule-model-gatingrule) operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller.

1. Choose **Create**.