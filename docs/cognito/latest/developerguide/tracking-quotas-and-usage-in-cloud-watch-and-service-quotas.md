

# Tracking quotas and usage in CloudWatch and Service Quotas
<a name="tracking-quotas-and-usage-in-cloud-watch-and-service-quotas"></a>

You can monitor Amazon Cognito user pools using Amazon CloudWatch or using Service Quotas. You can also monitor identity pools usage in Service Quotas. CloudWatch collects raw data and processes it into readable, near real-time metrics. In CloudWatch, you can set alarms that watch for certain thresholds and send notifications or take actions when those thresholds are met. To create a CloudWatch alarm for a service quota, see [Create a CloudWatch alarm](https://docs.aws.amazon.com/cognito/latest/developerguide/limits.html#create-a-cloud-watch-alarm). Amazon Cognito metrics are available at five minute intervals. For more information about retention periods in CloudWatch, visit the [Amazon CloudWatch FAQ page.](https://aws.amazon.com/cloudwatch/faqs) 

 You can use Service Quotas to view and manage your Amazon Cognito user pools and identity pools quota usage. The Service Quotas console has three features: view service quotas, request a service quota increase, and view current utilization. You can use the first feature to view quotas and see whether the quota is adjustable. You can use the second feature to request a Service Quotas increase. You can use the last feature to view quota utilization. This feature is only available after your account has been active for a while. For more information on viewing quotas in the Service Quotas console, see [Viewing Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/gs-request-quota.html). 

**Note**  
Amazon Cognito metrics are available at 5 minute intervals. For more information about retention periods in CloudWatch, visit the [Amazon CloudWatch FAQ page](https://aws.amazon.com/cloudwatch/faqs/).

If you are signed in to an AWS account that is set up as a monitoring account in CloudWatch cross-account observability, you can use that monitoring account to visualize service quotas and set alarms for metrics in the source accounts that are linked to that monitoring account. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

**Topics**
+ [User pool metrics in CloudWatch](metrics-for-cognito-user-pools.md)
+ [Metrics in Service Quotas](use-the-service-quota-console-to-track-metrics.md)