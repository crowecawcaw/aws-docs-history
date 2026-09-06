

End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html). 

# Monitoring AWS re:Post Private with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor AWS re:Post Private using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months so that you can access historical information and gain a better perspective on how your web application or service is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

The re:Post Private service reports the following metrics in the `AWS/rePostPrivate` namespace.


| Metric | Description | 
| --- | --- | 
| `NumberOfSpaces` | The number of private re:Posts in the current account.<br />Units: Count | 
| `NumberOfUsers` | The number of users in a private re:Post. This metric uses spaceId as a dimension.<br />Units: Count | 
| `ContentSize` | The amount of content in a private re:Post. This metric uses spaceId as a dimension.<br />Units: Bytes | 

The following dimensions are supported for the re:Post Private metrics.


|  Dimension  |  Description  | 
| --- | --- | 
|  spaceId  | The unique identifier for the private re:Post. | 