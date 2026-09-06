

# Automation rules in EventBridge
<a name="securityhub-v2-eventbridge-automations"></a>

 You can use automation rules in Amazon EventBridge to respond to Security Hub findings. Security Hub sends findings to EventBridge as events in near real time. You can write basic rules that indicate what automated actions to take when an event matches a rule. Actions that can be automatically triggered include the following: 
+  Configuring an API destination in EventBridge. 
+  Invoking Amazon EC2 run commands 
+  Invoking Lambda functions 
+  Invoking Step Functions state machines 
+  Notifying an Amazon SNS topic or an Amazon SQS queue 
+  Relaying events to Kinesis Data Streams 
+  Sending a finding to a third-party ticketing, chat, SIEM, or incident response and management tool 
+  [Sending an event to an EventBridge bus in another AWS account](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account-custom-bus-source.html) 

 Security Hub sends new findings and updated findings to EventBridge as events. Then you configure EventBridge rules to respond to each Security Hub event. For more information, see [What is EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) in the *EventBridge User Guide*. 

**Note**  
 If you have EventBridge rules defined for findings in Security Hub CSPM, the rules could overlap with rules defined for Security Hub. To avoid sending duplicate findings, evaluate the rules you have defined for Security Hub CSPM to determine if they overlap with rules you have defined for Security Hub. Where applicable, disable any Security Hub CSPM rules that are replaced by Security Hub rules. 

**Note**  
 As a best practice, make sure users with permission to access EventBridge use AWS Identity and Access Management policies that grant the minimum required permissions. For more information, see [EventBridge and AWS Identity and Access Management](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-iam.html) in the *EventBridge User Guide*. 