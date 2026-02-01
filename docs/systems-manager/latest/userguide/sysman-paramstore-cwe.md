• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting up notifications or triggering

actions based on Parameter Store events

The topics in this section explain how to use Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to
notify you about changes to AWS Systems Manager parameters. You can create an EventBridge rule to
notify you when a parameter or a parameter label version is created, updated, or
deleted. Events are emitted on a best effort basis. You can be notified about
changes or status related to parameter policies, such as when a parameter expires,
is going to expire, or hasn't changed for a specified period of time.

###### Note

Parameter policies are available for parameters that use the advanced
parameters tier. Charges apply. For more information, see [Assigning parameter policies in
Parameter Store](parameter-store-policies.md "parameter-store-policies.md") and [Managing parameter
tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md").

The topics in this section also explain how to initiate other actions on a target
for specific parameter events. For example, you can run an AWS Lambda function to
recreate a parameter automatically when it expires or is deleted. You can set up a
notification to invoke a Lambda function when your database password is updated. The
Lambda function can force your database connections to reset or reconnect with the
new password. EventBridge also supports running Run Command commands and Automation
executions, and actions in many other AWS services. Run Command and Automation are
both tools in AWS Systems Manager. For more information, see the
_[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")_.

###### Before You Begin

Create any resources you need to specify the target action for the rule you
create. For example, if the rule you create is for sending a notification, first
create an Amazon SNS topic. For more information, see [Getting
started with Amazon SNS](../../../sns/latest/dg/sns-getting-started.md "../../../sns/latest/dg/sns-getting-started.md") in the
_Amazon Simple Notification Service Developer Guide_.

## Configuring EventBridge rules for parameters

and parameter policies

This topic explains the following:

- How to create an EventBridge rule that invokes a target based on events that
  happen to one or more parameters in your AWS account.
- How to create EventBridge rules that invoke targets based on events that
  happen to one or more parameter policies in your AWS account. When you
  create an advanced parameter, you specify when a parameter expires, when
  to receive notification before a parameter expires, and how long to wait
  before notification should be sent that a parameter hasn't changed. You
  set up notification for these events using the following procedure. For
  more information, see [Assigning parameter policies in
  Parameter Store](parameter-store-policies.md "parameter-store-policies.md") and [Managing parameter
  tiers](parameter-store-advanced-parameters.md "parameter-store-advanced-parameters.md").

###### To configure an EventBridge rule for a Systems Manager parameter or parameter

policy

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**, and then
   choose **Create rule**.

-or-

If the EventBridge home page opens first, choose **Create
rule**. 3. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and
on the same event bus. 4. For **Event bus**, choose the event bus that you want
to associate with this rule. If you want this rule to initiate on
matching events that come from your own AWS account, select
**default** . When an AWS service in your account
emits an event, it always goes to your account’s default event bus. 5. For **Rule type**, leave the default **Rule
with an event pattern** selected. 6. Choose **Next**. 7. For **Event source**, leave the default
**AWS events or EventBridge partner events** selected.
You can skip the **Sample event** section. 8. For **Event pattern**, do the following:

    * Choose **Custom patterns (JSON
     editor)**.
    * For **Event pattern**, paste one of the
     following content in the box, depending on whether you are
     creating a rule for a parameter or a parameter policy:



    Parameter

    ```
    {
        "source": [
            "aws.ssm"
        ],
        "detail-type": [
            "Parameter Store Change"
        ],
        "detail": {
            "name": [
                "`parameter-1-name`",
                "/`parameter-2-name`/`level-2`",
                "/`parameter-3-name`/`level-2`/`level-3`"
            ],
            "operation": [
                "Create",
                "Update",
                "Delete",
                "LabelParameterVersion"
            ]
        }
    }
    ```


    Parameter policy

    ```
    {
        "source": [
            "aws.ssm"
        ],
        "detail-type": [
            "Parameter Store Policy Action"
        ],
        "detail": {
            "parameter-name": [
                "`parameter-1-name`",
                "/`parameter-2-name`/`level-2`",
                "/`parameter-3-name`/`level-2`/`level-3`"
            ],
            "policy-type": [
                "Expiration",
                "ExpirationNotification",
                "NoChangeNotification"
            ]
        }
    }
    ```
    * Modify the contents for the parameters and the operations you
     want to act on, as shown in the following samples.



    Parameter
    With this example, an action is taken when either
     of the parameters named /`Oncall`
     and `/Project/Teamlead` are
     updated:



    ```
    {
        "source": [
            "aws.ssm"
        ],
        "detail-type": [
            "Parameter Store Change"
        ],
        "detail": {
            "name": [
                "/Oncall",
                "/Project/Teamlead"
            ],
            "operation": [
                "Update"
            ]
        }
    }
    ```


    Parameter policy
    With this example, an action is taken whenever the
     parameter named /`OncallDuties`
     expires and is deleted:



    ```
    {
        "source": [
            "aws.ssm"
        ],
        "detail-type": [
            "Parameter Store Policy Action"
        ],
        "detail": {
            "parameter-name": [
                "/OncallDuties"
            ],
            "policy-type": [
                "Expiration"
            ]
        }
    }
    ```

9. Choose **Next**.
10. For **Target 1**, choose a target type and a
    supported resource. For example, if you choose **SNS
    topic**, make a selection for **Topic**.
    If you choose **CodePipeline**, enter a pipeline ARN
    for **Pipeline ARN**. Provide additional configuration
    values as required.

###### Tip

Choose **Add another target** if you require
additional targets for the rule. 11. Choose **Next**. 12. (Optional) Enter one or more tags for the rule. For more information,
see [Amazon EventBridge
tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md") in the _Amazon EventBridge User Guide_. 13. Choose **Next**. 14. Choose **Create rule**.

**More info**

- [Use parameter labels for easy configuration update across
  environments](https://aws.amazon.com/blogs/mt/use-parameter-labels-for-easy-configuration-update-across-environments/ "https://aws.amazon.com/blogs/mt/use-parameter-labels-for-easy-configuration-update-across-environments/")
- [Tutorial: Use EventBridge to relay events to AWS Systems Manager 
  Run Command](../../../eventbridge/latest/userguide/eb-ec2-run-command.md "../../../eventbridge/latest/userguide/eb-ec2-run-command.md") in the _Amazon EventBridge User Guide_
- [Tutorial: Set AWS Systems Manager Automation as an EventBridge
  target](../../../eventbridge/latest/userguide/eb-ssm-automation-as-target.md "../../../eventbridge/latest/userguide/eb-ssm-automation-as-target.md") in the _Amazon EventBridge User Guide_
