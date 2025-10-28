# Logging and monitoring for readiness check in Amazon Application Recovery Controller (ARC)

You can use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring readiness check in Amazon Application Recovery Controller (ARC), to analyze
patterns and help troubleshoot issues.

###### Note

You must view CloudWatch metrics and logs for ARC in the US West (Oregon) Region, both in the
console and when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region
for your command by including the following parameter: `--region us-west-2`.

###### Topics

- [Using Amazon CloudWatch with readiness check in ARC](cloudwatch-readiness.md "cloudwatch-readiness.md")
- [Logging readiness check API calls using AWS CloudTrail](cloudtrail-readiness.md "cloudtrail-readiness.md")
- [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md "eventbridge-readiness.md")
