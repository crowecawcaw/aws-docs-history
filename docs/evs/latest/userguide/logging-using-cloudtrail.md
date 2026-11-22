

# Log API calls with CloudTrail

Amazon Elastic VMware Service is integrated with AWS CloudTrail, a service that records the actions that an IAM user, an IAM role, or an AWS service takes in Amazon EVS. With the information that CloudTrail collects, you can find the request that was made to Amazon EVS, who made it, when, and from which IP address.

CloudTrail captures all AWS API calls for Amazon EVS as events. These include calls from the Amazon EVS console and calls from your code to the Amazon EVS API operations. To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

**Note**  
Amazon EVS doesn’t log user activity for components outside AWS, such as activity within your VMware Cloud Foundation (VCF) environment.

VMware consoles such as the vSphere Client and NSX Manager log these activities. For centralized VCF logging with a VCF monitoring solution such as VCF Operations, see [Monitor hosts and VCF](monitor-observability.md).

## Amazon EVS information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is turned on in your AWS account when you create the account. When activity occurs in Amazon EVS, CloudTrail records it in an event, together with the events of other AWS services, in **Event history**. You can view, search, and download recent events in your AWS account, even if you don’t create a trail. For more information, see [Working with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the * AWS CloudTrail User Guide*.

For an ongoing record of events in your AWS account, including events for Amazon EVS, create a trail. A *trail* delivers log files to an Amazon S3 bucket that you specify. By default, a trail that you create in the console applies to all AWS Regions in the partition. You can also configure other AWS services to analyze and act on the event data that CloudTrail collects. For more information, see the following topics in the * AWS CloudTrail User Guide*.
+  [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations) 
+  [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) 
+  [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

CloudTrail logs all Amazon EVS actions. The actions are documented in the [Amazon Elastic VMware Service API Reference](https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html). For example, calls to the `CreateEnvironment`, `GetEnvironment`, and `DeleteEnvironment` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or IAM user credentials.
+ Whether the request was made with temporary security credentials for a role or a federated user.
+ Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the * AWS CloudTrail User Guide*.

## Find Amazon EVS events
<a name="cloudtrail-find-evs-events"></a>

To list recent Amazon EVS events in **Event history** with the AWS CLI, filter on the event source. Replace `<region-code>` with the Region where you created the environment.

```bash
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventSource,AttributeValue=evs.amazonaws.com \
    --max-results 20 \
    --region <region-code>
```

To find who deleted a host, filter on the event name, for example `DeleteEnvironmentHost`. Replace `<region-code>` with the Region where you created the environment.

```bash
aws cloudtrail lookup-events \
    --lookup-attributes AttributeKey=EventName,AttributeValue=DeleteEnvironmentHost \
    --region <region-code>
```

## Understanding Amazon EVS log file entries
<a name="understanding-service-name-entries"></a>

CloudTrail log files contain one or more log entries. An event represents a single request from any source. It includes information about the requested action, the date and time of the action, the request parameters, and other details. CloudTrail log files aren’t an ordered stack trace of the public API calls, so the entries don’t appear in any specific order.