

# Viewing metrics for Amazon SES email receiving
<a name="receiving-email-metrics"></a>

If you've enabled email receiving in Amazon SES and you've created receipt rules for your email, you can view the metrics for those receipt rule sets and rules using Amazon CloudWatch.

In the CloudWatch console, you'll find the metrics under **Metrics** > **All metrics** > **SES** > **Receipt Rule Set Metrics** and **Receipt Rule Metrics**.

**Note**  
**Receipt Rule Set Metrics** and **Receipt Rule Metrics** will not appear under **SES** if you have not yet:  
[enabled email receiving](receiving-email-setting-up.md)
[created any receipt rules](receiving-email-receipt-rules-console-walkthrough.md)
received any mail that would match any of your rules.

The following message metrics are available:
+ **Message receiving**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/ses/latest/dg/receiving-email-metrics.html)
+ **Message publishing**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/ses/latest/dg/receiving-email-metrics.html)

**Note**  
In the preceding tables, the term *applies* means that the sender is not blocklisted by IP Filters or is on SES's internal blocklist, and the rule has matching recipient conditions and matching TLS policy.
Publish failure errors can occur, for example, if you deleted or revoked permissions to an Amazon S3 bucket, Amazon SNS topic, or Lambda function that an action in one of your receipt rules was configured to use.
Because only one rule set can be active at a time, SES publishes an aggregate metric displayed as *RuleSetName:[Active]* for all rules sets that were active for the time range you select in CloudWatch. This has the advantage of letting you freely change rule sets without any change to your alarming setup.

**Important**  
Changes you make to fix your receipt rule set will apply only to emails that Amazon SES receives after the update. Emails are always evaluated against the receipt rule set that was in place at the time the email was received.

Metrics for an SES *receipt rule set* displayed in the CloudWatch console.

![Receipt rule set metrics in CloudWatch.](http://docs.aws.amazon.com/ses/latest/dg/images/inbound_cloudwatch_rule_set_metrics.png)


Metrics for an SES *receipt rule* displayed in the CloudWatch console.

![Receipt rule metrics in CloudWatch.](http://docs.aws.amazon.com/ses/latest/dg/images/inbound_cloudwatch_rule_metrics.png)
