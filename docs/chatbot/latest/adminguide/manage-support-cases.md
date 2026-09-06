

AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md)

# Managing AWS Support cases from chat channels using Amazon Q Developer in chat applications
<a name="manage-support-cases"></a>

You can use Amazon Q Developer in chat applications to monitor and respond to your AWS Support cases in your Microsoft Teams and Slack chat channels. A support case is a way for you to connect with technical support and get help with AWS service-related technical issues. You can use the on-screen action buttons to interact with your support cases. Actions you can perform include viewing correspondence (case history), resolving your case, and replying to your case. You can create support cases using Amazon Q Developer in chat applications and the AWS Management Console. For more information, see [Creating an AWS Support case using Amazon Q Developer in chat applications](Things-to-know-about-cli.md#create-a-support-case) and [Creating support cases and case management](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html) in the *AWS Support User Guide* respectively.

AWS Support case management in Amazon Q Developer in chat applications is available at no additional cost in Regions where Amazon Q Developer in chat applications is offered.

**Note**  
To interact with support cases in chat channels, you must have a Business, Enterprise On-Ramp, or Enterprise Support plan. If you attempt to take action on a support case without one of these plans, you will receive a `SubscriptionRequiredException` error message. For information about changing your support plan, see [AWS Support](http://aws.amazon.com/premiumsupport/).

## Prerequisities
<a name="support-case-prereq"></a>

To manage your support cases in your chat channels, you must:
+ Create an Amazon EventBridge rule for AWS Support case events and choose an Amazon SNS topic as your target. For more information, see [Creating an EventBridge rule for AWS Support cases](https://docs.aws.amazon.com/awssupport/latest/user/event-bridge-support.html#creating-event-bridge-events-rule-for-aws-support) in the *AWS Support User Guide*. 
  + Subscribe that Amazon SNS topic to your Amazon Q Developer in chat applications configuration. For more information, see [Tutorial: Subscribing an Amazon SNS topic to Amazon Q Developer in chat applications](subscribe-sns-topic.md). 
+ Add the managed role [`AWSSupportAccess`](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSSupportAccess) to your Amazon Q Developer in chat applications role. For more information, see [Editing an IAM role for Amazon Q Developer in chat applications](editing-iam-roles-for-chatbot.md). 