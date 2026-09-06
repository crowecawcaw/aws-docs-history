

# Logging and monitoring for readiness check in Amazon Application Recovery Controller (ARC)
<a name="monitoring-readiness"></a>

**Note**  
The readiness check feature in Amazon Application Recovery Controller (ARC) is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [Amazon Application Recovery Controller (ARC) readiness check availability change](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-readiness-availability-change.html).

You can use Amazon CloudWatch, AWS CloudTrail, and Amazon EventBridge for monitoring readiness check in Amazon Application Recovery Controller (ARC), to analyze patterns and help troubleshoot issues.

**Note**  
You must view CloudWatch metrics and logs for ARC in the US West (Oregon) Region, both in the console and when using the AWS CLI. When you use the AWS CLI, specify the US West (Oregon) Region for your command by including the following parameter: `--region us-west-2`.

**Topics**
+ [Using Amazon CloudWatch with readiness check in ARC](cloudwatch-readiness.md)
+ [Logging readiness check API calls using AWS CloudTrail](cloudtrail-readiness.md)
+ [Using readiness check in ARC with Amazon EventBridge](eventbridge-readiness.md)