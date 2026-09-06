

# Monitor Amazon EMR application status with CloudWatch integration
<a name="enhanced-custom-metrics-application-status"></a>

When you integrate CloudWatch with Amazon EMR, you can track critical statuses for applications like HiveServer2. You can publish status to CloudWatch custom metrics and configure alerts for service unavailability. 

Specifically, you can create a script to monitor Amazon EMR applications like YARN ResourceManager and HiveServer2 on a primary node. See [Publish and monitor an Amazon EMR application status with CloudWatch integration](https://repost.aws/knowledge-center/emr-publish-monitor-service-status) in the *re:Post Knowledge Center* for details on how to configure this use case.