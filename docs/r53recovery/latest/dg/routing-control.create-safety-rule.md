# Creating a safety rule on the console

The steps in this section explain how to create a safety rule on the ARC console. The steps are similar
whether you create an assertion rule or a gating rule. The differences are noted in the procedure.

To learn about using recovery and routing control API operations with Amazon Application Recovery Controller (ARC), see
[Routing control API operations](actions.routing-control.md "actions.routing-control.md").

# To create a safety rule

1. Open the ARC console at [https://console.aws.amazon.com/route53recovery/home#/dashboard](https://console.aws.amazon.com/route53recovery/home#/dashboard "https://console.aws.amazon.com/route53recovery/home#/dashboard").
2. Choose **Routing control**.
3. On the **Routing control** page, choose a control panel.
4. On the control panel details page, choose **Action**, and then choose **Add safety rule**.
5. Choose a type of rule to add: **Assertion rule** or **Gating rule**.
6. Choose a name and, optionally, change the wait period.
7. Specify the configuration options for the safety rule.

   - For an assertion rule, specify the asserted routing controls.
   - For a gating rule, specify the gating routing control and target routing controls.
     For both rules, specify the rule configuration by choosing the type and threshold, and whether the rule is inverted.

###### Note

To learn more about specifying an assertion rule, see the information provided for
[AssertionRule](../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-assertionrule "../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-assertionrule")
operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller.
To learn more about specifying a gating rule, see the information provided for the
[GatingRule](../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-gatingrule "../../../recovery-cluster/latest/api/safetyrule.md#safetyrule-model-gatingrule")
operation in the Routing Control API Reference Guide for Amazon Application Recovery Controller. 8. Choose **Create**.
