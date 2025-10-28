# Monitoring AWS Config with Amazon EventBridge

Amazon EventBridge delivers a near real-time stream of system events that describe changes in AWS
resources. Use Amazon EventBridge to detect and react to changes in the status of AWS Config events.

You can create a rule that runs whenever there is a state transition, or when there is a
transition to one or more states that are of interest. Then, based on rules you create,
Amazon EventBridge invokes one or more target actions when an event matches the values you specify in
a rule. Depending on the type of event, you might want to send notifications, capture event
information, take corrective action, initiate events, or take other actions.

Before you create event rules for AWS Config, however, you should do the following:

- Familiarize yourself with events, rules, and targets in EventBridge. For more
  information, see [What Is
  Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- For more information about how to get started with EventBridge and set up rules, see
  [Getting started with
  Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").
- Create the target or targets you will use in your event rules.

###### Topics

- [Considerations](#monitor-config-with-cloudwatchevents-considerations "#monitor-config-with-cloudwatchevents-considerations")
- [Amazon EventBridge format for AWS Config](#cloudwatch-event-format-for-awsconfig "#cloudwatch-event-format-for-awsconfig")
- [Creating Amazon EventBridge Rule for
  AWS Config](#create-cloudwatch-events-rule-for-awsconfig "#create-cloudwatch-events-rule-for-awsconfig")

## Considerations

You will not receive alerts through EventBridge for the following resource types if you are not recording them with AWS Config:

- `AWS::ACM::Certificate`
- `AWS::CloudTrail::Trail`
- `AWS::CloudWatch::Alarm`
- `AWS::EC2::CustomerGateway`
- `AWS::EC2::EIP`
- `AWS::EC2::Host`
- `AWS::EC2::Instance`
- `AWS::EC2::InternetGateway`
- `AWS::EC2::NetworkAcl`
- `AWS::EC2::NetworkInterface`
- `AWS::EC2::RouteTable`
- `AWS::EC2::SecurityGroup`
- `AWS::EC2::Subnet`
- `AWS::EC2::VPC`
- `AWS::EC2::VPNConnection`
- `AWS::EC2::VPNGateway`
- `AWS::EC2::Volume`
- `AWS::ElasticLoadBalancingV2::LoadBalancer`
- `AWS::IAM::Group`
- `AWS::IAM::Policy`
- `AWS::IAM::Role`
- `AWS::IAM::User`
- `AWS::RDS::DBInstance`
- `AWS::RDS::DBSecurityGroup`
- `AWS::RDS::DBSnapshot`
- `AWS::RDS::DBSubnetGroup`
- `AWS::RDS::EventSubscription`
- `AWS::Redshift::Cluster`
- `AWS::Redshift::ClusterParameterGroup`
- `AWS::Redshift::ClusterSecurityGroup`
- `AWS::Redshift::ClusterSnapshot`
- `AWS::Redshift::ClusterSubnetGroup`
- `AWS::Redshift::EventSubscription`
- `AWS::S3::Bucket`

## Amazon EventBridge format for AWS Config

The EventBridge [event](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") for AWS Config has the
following format:

```

          {
             "version": "0",
             "id": "cd4d811e-ab12-322b-8255-872ce65b1bc8",
             "detail-type": "`event type`",
             "source": "aws.config",
             "account": "111122223333",
             "time": "2018-03-22T00:38:11Z",
             "region": "us-east-1",
             "resources": [
                `resources`
             ],
             "detail": {
                `specific message type`
             }
          }

```

## Creating Amazon EventBridge Rule for

AWS Config

Use the following steps to create an EventBridge rule that triggers on an event emitted by
AWS Config. Events are emitted on a best effort basis.

1. In the navigation pane, choose **Rules**.
2. Choose **Create rule**.
3. Enter a name and description for the rule.

A rule can't have the same name as another rule in the same Region and on the
same event bus.

###### Note

An event bus receives events from a source, uses rules to evaluate them, applies any
configured input transformation, and routes them to the appropriate
target(s). Your account's default event bus receives events from
AWS services. A custom event bus can receive events from your custom
applications and services. A partner event bus receives events from an event
source created by an SaaS partner. These events come from the partners
services or applications. For more information, see [Event buses in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md") in the _Amazon EventBridge User Guide_. 4. For **Rule type**, choose **Rule with an event pattern**. 5. For **Event source**, choose **AWS events or EventBridge partner events**. 6. (Optional) For **Sample event type**, choose **AWS
events**. 7. (Optional) For **Sample events**, choose the event type that
triggers the rule:

    * Choose **AWS API Call from CloudTrail** to base
     rules on API calls made to this service. For more information about
     creating this type of rule, see [Tutorial: Create an
     Amazon EventBridge rule for AWS CloudTrail API calls](../../../eventbridge/latest/userguide/eb-ct-api-tutorial.md "../../../eventbridge/latest/userguide/eb-ct-api-tutorial.md").
    * Choose **Config Configuration Item Change** to get
     notifications when a resource in your account changes.


    As described in these support articles, you can use EventBridge to receive
     custom email notifications when a resource is created or deleted, [How can I receive custom email notifications when a resource is
     created in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-created/ "https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-created/") and [How can I receive custom email notifications when a resource is
     deleted in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-deleted/ "https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-deleted/").
    * Choose **Config Rules Compliance Change** to get
     notifications when a compliance check to your rules fails.


    As described in this support article, you can use EventBridge to receive
     custom email notifications when a resource is noncompliant,
     [How can I be notified when an AWS resource is noncompliant using
     AWS Config?](https://repost.aws/knowledge-center/config-resource-non-compliant "https://repost.aws/knowledge-center/config-resource-non-compliant").
    * Choose **Config Rules Re-evaluation Status** to get
     reevaluation status notifications.
    * Choose **Config Configuration Snapshot Delivery
     Status** to get configuration snapshot delivery status
     notifications.
    * Choose **Config Configuration History Delivery
     Status** to get configuration history delivery status
     notifications.

8. For **Creation method**, choose **Use pattern form**.
9. For **Event source**, choose **AWS services**.
10. For **AWS service**, choose
    **Config**.
11. For **Event type**, choose the event type that triggers the
    rule:
    - Choose **All Events** to make a rule that applies to
      all AWS services. If you choose this option, you cannot choose
      specific message types, rule names, resource types, or resource
      IDs.
    - Choose **AWS API Call from CloudTrail** to base
      rules on API calls made to this service. For more information about
      creating this type of rule, see [Tutorial: Create an
      Amazon EventBridge rule for AWS CloudTrail API calls](../../../eventbridge/latest/userguide/eb-ct-api-tutorial.md "../../../eventbridge/latest/userguide/eb-ct-api-tutorial.md").
    - Choose **Config Configuration Item Change** to get
      notifications when a resource in your account changes.

    As described in these support articles, you can use EventBridge to receive
    custom email notifications when a resource is created or deleted, [How can I receive custom email notifications when a resource is
    created in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-created/ "https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-created/") and [How can I receive custom email notifications when a resource is
    deleted in my AWS account using AWS Config service?](https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-deleted/ "https://aws.amazon.com/premiumsupport/knowledge-center/config-email-resource-deleted/").
    - Choose **Config Rules Compliance Change** to get
      notifications when a compliance check to your rules fails.

    As described in this support article, you can use EventBridge to receive
    custom email notifications when a resource is noncompliant, [How can I be notified when an AWS resource is noncompliant using
    AWS Config?](https://repost.aws/knowledge-center/config-resource-non-compliant "https://repost.aws/knowledge-center/config-resource-non-compliant").
    - Choose **Config Rules Re-evaluation Status** to get
      reevaluation status notifications.
    - Choose **Config Configuration Snapshot Delivery
      Status** to get configuration snapshot delivery status
      notifications.
    - Choose **Config Configuration History Delivery
      Status** to get configuration history delivery status
      notifications.

12. Choose **Any message type** to receive notifications of any
    type. Choose **Specific message type(s)** to receive the
    following types of notifications:
    - If you choose
      **ConfigurationItemChangeNotification**, you receive
      messages when the configuration of a resource that AWS Config evaluates has changed.
    - If you choose **ComplianceChangeNotification**, you
      receive messages when the compliance type of a resource that AWS Config
      evaluates has changed.
    - If you choose **ConfigRulesEvaluationStarted**, you
      receive messages when AWS Config starts evaluating your rule against the
      specified resources.
    - If you choose
      **ConfigurationSnapshotDeliveryCompleted**, you
      receive messages when AWS Config successfully delivers the configuration
      snapshot to your Amazon S3 bucket.
    - If you choose
      **ConfigurationSnapshotDeliveryFailed**, you receive
      messages when AWS Config fails to deliver the configuration snapshot to your
      Amazon S3 bucket.
    - If you choose
      **ConfigurationSnapshotDeliveryStarted**, you
      receive messages when AWS Config starts delivering the configuration snapshot
      to your Amazon S3 bucket.
    - If you choose
      **ConfigurationHistoryDeliveryCompleted**, you
      receive messages when AWS Config successfully delivers the configuration
      history to your Amazon S3 bucket.

13. If you chose a specific event type from the **Event Type**
    dropdown list, choose **Any resource type** to make a rule that
    applies to all AWS Config supported resource types.

Or choose **Specific resource type(s)**, and then type the
AWS Config supported resource type (for example,
`AWS::EC2::Instance`). 14. If you chose a specific event type from the **Event Type**
dropdown list, choose **Any resource ID** to include any AWS Config
supported resource ID.

Or choose **Specific resource ID(s)**, and then type the AWS Config
supported resource ID (for example, `i-04606de676e635647`). 15. If you chose a specific event type from the **Event Type**
dropdown list, choose **Any rule name** to include any AWS Config
supported rule.

Or choose **Specific rule name(s)**, and then type the AWS Config
supported rule (for example, **required-tags**). 16. For **Select target(s)**, choose the type of target you have
prepared to use with this rule, and then configure any additional options
required by that type. 17. The fields displayed vary depending on the service you choose. Enter
information specific to this target type as needed. 18. For many target types, EventBridge needs permissions to send events to the target. In
these cases, EventBridge can create the IAM role needed for your rule to run.

    * To create an IAM role automatically, choose **Create a new
     role for this specific resource**.
    * To use an IAM role that you created earlier, choose **Use
     existing role**.

19. (Optional) Choose **Add target** to add another target for
    this rule.
20. (Optional) Enter one or more tags for the rule. For more information, see
    [Amazon EventBridge tags](../../../eventbridge/latest/userguide/eb-tagging.md "../../../eventbridge/latest/userguide/eb-tagging.md").
21. Review your rule setup to make sure it meets your event-monitoring
    requirements.
22. Choose **Create** to confirm your selection.
