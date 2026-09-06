

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Setting up notifications or triggering actions based on Parameter Store events
<a name="sysman-paramstore-cwe"></a>

You can use Amazon EventBridge and Amazon Simple Notification Service (Amazon SNS) to notify you about changes to AWS Systems Manager parameters. Events are emitted on a best effort basis. For example, you can create rules that do the following:
+ Notify you when a parameter or a parameter label version is created, updated, or deleted.
+ Notify you of changes or status related to parameter policies, such as when a parameter expires, is going to expire, or hasn't changed for a specified period of time.
**Note**  
Parameter policies are available for parameters that use the advanced parameters tier. Charges apply. For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md) and [Choosing parameter tiers in Parameter Store](parameter-store-advanced-parameters.md).
+ Initiate other actions on a target for specific parameter events. For example, you can run an AWS Lambda function to recreate a parameter automatically when it expires or is deleted. You can set up a notification to invoke a Lambda function when a parameter that stores an approved AMI ID is updated. The Lambda function can update a launch template or start a deployment workflow that uses the new AMI ID.

EventBridge also supports running Run Command commands and Automation executions, and actions in many other AWS services. Run Command and Automation are both tools in AWS Systems Manager. For more information, see the *[Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)*.

**Before You Begin**  
Create any resources you need to specify the target action for the rule you create. For example, if the rule you create is for sending a notification, first create an Amazon SNS topic. For more information, see [Getting started with Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-getting-started.html) in the *Amazon Simple Notification Service Developer Guide*.

## Configuring EventBridge rules for parameters and parameter policies
<a name="cwe-parameter-changes"></a>

This topic explains the following:
+ How to create an EventBridge rule that invokes a target based on events that happen to one or more parameters in your AWS account.
+ How to create EventBridge rules that invoke targets based on events that happen to one or more parameter policies in your AWS account. When you create an advanced parameter, you specify when a parameter expires, when to receive notification before a parameter expires, and how long to wait before notification should be sent that a parameter hasn't changed. You set up notification for these events using the following procedure. For more information, see [Assigning parameter policies in Parameter Store](parameter-store-policies.md) and [Choosing parameter tiers in Parameter Store](parameter-store-advanced-parameters.md).

**To configure an EventBridge rule for a Systems Manager parameter or parameter policy**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Choose **EventBridge Rule with event pattern** and then **Create rule**.

1. Choose **Advanced builder** if it is not already selected.

1. Enter a name and description for the rule. Then choose **Next**.

   A rule can't have the same name as another rule in the same Region and on the same event bus.

1. For **Event bus**, choose the event bus that you want to associate with this rule. If you want this rule to initiate on matching events that come from your own AWS account, select **default**. When an AWS service in your account emits an event, it always goes to your account’s default event bus. 

1. For **Rule type**, leave the default **Rule with an event pattern** selected.

1. Choose **Next**.

1. For **Event source**, leave the default **AWS events or EventBridge partner events** selected. You can skip the **Sample event** section.

1. For **Event pattern**, do the following:
   + Choose **Custom patterns (JSON editor)**.
   + For **Event pattern**, paste one of the following content in the box, depending on whether you are creating a rule for a parameter or a parameter policy:

------
#### [ Parameter ]

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
                 "{{parameter-1-name}}",
                 "/{{parameter-2-name}}/{{level-2}}",
                 "/{{parameter-3-name}}/{{level-2}}/{{level-3}}"
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

------
#### [ Parameter policy ]

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
                 "{{parameter-1-name}}",
                 "/{{parameter-2-name}}/{{level-2}}",
                 "/{{parameter-3-name}}/{{level-2}}/{{level-3}}"
             ],
             "policy-type": [
                 "Expiration",
                 "ExpirationNotification",
                 "NoChangeNotification"
             ]
         }
     }
     ```

------
   + Modify the contents for the parameters and the operations you want to act on, as shown in the following samples. 

------
#### [ Parameter ]

     With this example, an action is taken when either of the parameters named /`Oncall` and `/Project/Teamlead` are updated:

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

------
#### [ Parameter policy ]

     With this example, an action is taken whenever the parameter named /`OncallDuties` expires and is deleted:

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

------

1. Choose **Next**.

1. For **Target 1**, choose a target type and a supported resource. For example, if you choose **AWS service** and then **SNS topic**, make a selection for **Topic**. If you choose **CodePipeline**, enter a pipeline ARN for **Pipeline ARN**. Provide additional configuration values as required.
**Tip**  
Choose **Add another target** if you require additional targets for the rule.

1. Choose **Next**.

1. (Optional) Enter one or more tags for the rule. For more information, see [Amazon EventBridge tags](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tagging.html) in the *Amazon EventBridge User Guide*.

1. Choose **Next**.

1. Choose **Create rule**.

**More information**  
+ [Use parameter labels for easy configuration update across environments](https://aws.amazon.com/blogs/mt/use-parameter-labels-for-easy-configuration-update-across-environments/)
+ [Tutorial: Use EventBridge to relay events to AWS Systems Manager  Run Command](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ec2-run-command.html) in the *Amazon EventBridge User Guide*
+ [Tutorial: Set AWS Systems Manager Automation as an EventBridge target](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-ssm-automation-as-target.html) in the *Amazon EventBridge User Guide*