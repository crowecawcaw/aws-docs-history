# Meeting compliance requirements with
 S3 Replication Time Control

S3 Replication Time Control (S3 RTC) helps you meet compliance or business requirements for data replication and
 provides visibility into Amazon S3 replication times. S3 RTC replicates most objects that you
 upload to Amazon S3 in seconds, and 99.9 percent of those objects within 15 minutes. 

By default, S3 RTC includes two ways to track the progress of replication: 


* **S3 Replication metrics** – You can use
 S3 Replication metrics to monitor the total number of S3 API operations that are pending
 replication, the total size of objects pending replication, the maximum replication
 time to the destination Region, and the total number of operations that failed
 replication. You can then monitor each dataset that you replicate separately. You
 can also enable S3 Replication metrics independently of S3 RTC. For more information,
 see [Using S3 Replication metrics](repl-metrics.md "repl-metrics.md").


Replication rules with S3 Replication Time Control (S3 RTC) enabled publish S3 Replication metrics. Replication
 metrics are available within 15 minutes of enabling S3 RTC. Replication metrics
 are available through the Amazon S3 console, the Amazon S3 API, the AWS SDKs, the
 AWS Command Line Interface (AWS CLI), and Amazon CloudWatch. For more information about CloudWatch metrics, see [Monitoring metrics with Amazon CloudWatch](cloudwatch-monitoring.md "cloudwatch-monitoring.md"). For
 more information about viewing replication metrics through the Amazon S3 console, see
 [Viewing replication metrics](repl-metrics.md#viewing-replication-metrics "repl-metrics.md#viewing-replication-metrics").


S3 Replication metrics are billed at the same rate as Amazon CloudWatch custom metrics. For
 information, see [Amazon CloudWatch
 pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
* **Amazon S3 Event Notifications** – S3 RTC
 provides `OperationMissedThreshold` and
 `OperationReplicatedAfterThreshold` events that notify the bucket
 owner if object replication exceeds or occurs after the 15-minute threshold. With
 S3 RTC, Amazon S3 Event Notifications can notify you in the rare instance when objects
 don't replicate within 15 minutes and when those objects replicate after the
 15-minute threshold. 


Replication events are available within 15 minutes of enabling S3 RTC. Amazon S3 Event
 Notifications are available through Amazon SQS, Amazon SNS, or AWS Lambda. For more
 information, see [Receiving replication failure events with Amazon S3
 Event Notifications](replication-metrics-events.md "replication-metrics-events.md").
 


## Best practices and guidelines for
 S3 RTC


When replicating data in Amazon S3 with S3 Replication Time Control (S3 RTC) enabled, follow these best practice
 guidelines to optimize replication performance for your workloads. 


###### Topics

* [Amazon S3 Replication and request rate
 performance guidelines](#rtc-request-rate-performance "#rtc-request-rate-performance")
* [Estimating your replication
 request rates](#estimating-replication-request-rates "#estimating-replication-request-rates")
* [Exceeding S3 RTC data transfer
 rate quotas](#exceed-rtc-data-transfer-limits "#exceed-rtc-data-transfer-limits")
* [AWS KMS encrypted object
 replication request rates](#kms-object-replication-request-rates "#kms-object-replication-request-rates")

### Amazon S3 Replication and request rate
 performance guidelines


When uploading and retrieving storage from Amazon S3, your applications can achieve
 thousands of transactions per second in request performance. For example, an
 application can achieve at least 3,500
 `PUT`/`COPY`/`POST`/`DELETE` or
 5,500 `GET`/`HEAD` requests per second per prefix in an S3
 bucket, including the requests that S3 Replication makes on your behalf. There are
 no limits to the number of prefixes in a bucket. You can increase your read or write
 performance by parallelizing reads. For example, if you create 10 prefixes in an S3
 bucket to parallelize reads, you can scale your read performance to 55,000 read
 requests per second. 


Amazon S3 automatically scales in response to sustained request rates above these
 guidelines, or sustained request rates concurrent with `LIST` requests.
 While Amazon S3 is internally optimizing for the new request rate, you might receive HTTP
 503 request responses temporarily until the optimization is complete. This behavior
 might occur with increases in request per second rates, or when you first enable
 S3 RTC. During these periods, your replication latency might increase. The
 S3 RTC service level agreement (SLA) doesn’t apply to time periods when Amazon S3
 performance guidelines on requests per second are exceeded. 


The S3 RTC SLA also doesn't apply during time periods where your replication
 data transfer rate exceeds the default 1 gigabit per second (Gbps) quota. If you
 expect your replication transfer rate to exceed 1 Gbps, you can contact
 [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") or use [Service
 Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html") to request an increase in your replication transfer rate quota. 


### Estimating your replication
 request rates


Your total request rate including the requests that Amazon S3 replication makes on your
 behalf must be within the Amazon S3 request rate guidelines for both the replication
 source and destination buckets. For each object replicated, Amazon S3 replication makes
 up to five `GET`/`HEAD` requests and one `PUT`
 request to the source bucket, and one `PUT` request to each destination
 bucket.


For example, if you expect to replicate 100 objects per second, Amazon S3 replication
 might perform an additional 100 `PUT` requests on your behalf for a total
 of 200 `PUT` requests per second to the source S3 bucket. Amazon S3
 replication also might perform up to 500 `GET`/`HEAD` requests
 (5 `GET`/`HEAD` requests for each object that's replicated.) 


###### Note

You incur costs for only one `PUT` request per object replicated.
 For more information, see the pricing information in the [Amazon S3 FAQs about
 replication](https://aws.amazon.com/s3/faqs/#Replication "https://aws.amazon.com/s3/faqs/#Replication"). 


### Exceeding S3 RTC data transfer
 rate quotas


If you expect your S3 RTC data transfer rate to exceed the default 1 Gbps quota,
 contact [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") or use [Service
 Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html") to request an increase in your replication transfer rate quota. 


### AWS KMS encrypted object
 replication request rates


When you replicate objects that are encrypted with server-side encryption with
 AWS Key Management Service (AWS KMS) keys (SSE-KMS), AWS KMS requests per second quotas apply. AWS KMS
 might reject an otherwise valid request because your request rate exceeds the quota
 for the number of requests per second. When a request is throttled, AWS KMS returns a
 `ThrottlingException` error. The AWS KMS request rate quota applies to
 requests that you make directly and to requests made by Amazon S3 replication on your
 behalf. 


For example, if you expect to replicate 1,000 objects per second, you can subtract
 2,000 requests from your AWS KMS request rate quota. The resulting request rate per
 second is available for your AWS KMS workloads excluding replication. You can use
 [AWS KMS request metrics in
 Amazon CloudWatch](https://docs.aws.amazon.com/kms/latest/developerguide/monitoring-cloudwatch.html "https://docs.aws.amazon.com/kms/latest/developerguide/monitoring-cloudwatch.html") to monitor the total AWS KMS request rate on your
 AWS account.


To request an increase to your AWS KMS requests per second quota, contact
 [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/") or use [Service
 Quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html "https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html"). 


## Enabling S3 Replication Time Control


You can start using S3 Replication Time Control (S3 RTC) with a new or existing replication rule. You can choose
 to apply your replication rule to an entire bucket, or to objects with a specific prefix or
 tag. When you enable S3 RTC, S3 Replication metrics are also enabled on your replication rule. 


You can configure S3 RTC by using the Amazon S3 console, the Amazon S3 API, the AWS SDKs,
 and the AWS Command Line Interface (AWS CLI).


###### Topics


For step-by-step instructions, see [Configuring replication for buckets in the same
 account](replication-walkthrough1.md "replication-walkthrough1.md"). This topic provides instructions for
 enabling S3 RTC in your replication configuration when the source and destination
 buckets are owned by the same and different AWS accounts.

To use the AWS CLI to replicate objects with S3 RTC enabled, you create buckets,
 enable versioning on the buckets, create an IAM role that gives Amazon S3 permission to
 replicate objects, and add the replication configuration to the source bucket. The
 replication configuration must have S3 RTC enabled, as shown in the following
 example. 

For step-by-step instructions for setting up your replication configuration by
 using the AWS CLI, see [Configuring replication for buckets in the same
 account](replication-walkthrough1.md "replication-walkthrough1.md").

The following example replication configuration enables and sets the
 `ReplicationTime` and `EventThreshold` values for a
 replication rule. Enabling and setting these values enables S3 RTC on the
 rule.


```
{
    "Rules": [
        {
            "Status": "Enabled",
            "Filter": {
                "Prefix": "`Tax`"
            },
            "DeleteMarkerReplication": {
                "Status": "Disabled"
            },
            "Destination": {
                "Bucket": "arn:aws:s3:::`amzn-s3-demo-destination-bucket`",
                "Metrics": {
                    "Status": "Enabled",
                    "EventThreshold": {
                        "Minutes": 15
                    }
                },
                "ReplicationTime": {
                    "Status": "Enabled",
                    "Time": {
                        "Minutes": 15
                    }
                }
            },
            "Priority": 1
        }
    ],
    "Role": "`IAM-Role-ARN`"
}
```
###### Important


`Metrics:EventThreshold:Minutes` and
 `ReplicationTime:Time:Minutes` can only have
 `15` as a valid value. 

 The following Java example adds replication configuration with S3 Replication Time Control (S3 RTC)
 enabled.


```
import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.model.DeleteMarkerReplication;
import software.amazon.awssdk.services.s3.model.Destination;
import software.amazon.awssdk.services.s3.model.Metrics;
import software.amazon.awssdk.services.s3.model.MetricsStatus;
import software.amazon.awssdk.services.s3.model.PutBucketReplicationRequest;
import software.amazon.awssdk.services.s3.model.ReplicationConfiguration;
import software.amazon.awssdk.services.s3.model.ReplicationRule;
import software.amazon.awssdk.services.s3.model.ReplicationRuleFilter;
import software.amazon.awssdk.services.s3.model.ReplicationTime;
import software.amazon.awssdk.services.s3.model.ReplicationTimeStatus;
import software.amazon.awssdk.services.s3.model.ReplicationTimeValue;

public class Main {

  public static void main(String[] args) {
    S3Client s3 = S3Client.builder()
      .region(Region.US_EAST_1)
      .credentialsProvider(() -> AwsBasicCredentials.create(
          "AWS_ACCESS_KEY_ID",
          "AWS_SECRET_ACCESS_KEY")
      )
      .build();

    ReplicationConfiguration replicationConfig = ReplicationConfiguration
      .builder()
      .rules(
          ReplicationRule
            .builder()
            .status("Enabled")
            .priority(1)
            .deleteMarkerReplication(
                DeleteMarkerReplication
                    .builder()
                    .status("Disabled")
                    .build()
            )
            .destination(
                Destination
                    .builder()
                    .bucket("destination_bucket_arn")
                    .replicationTime(
                        ReplicationTime.builder().time(
                            ReplicationTimeValue.builder().minutes(15).build()
                        ).status(
                            ReplicationTimeStatus.ENABLED
                        ).build()
                    )
                    .metrics(
                        Metrics.builder().eventThreshold(
                            ReplicationTimeValue.builder().minutes(15).build()
                        ).status(
                            MetricsStatus.ENABLED
                        ).build()
                    )
                    .build()
            )
            .filter(
                ReplicationRuleFilter
                    .builder()
                    .prefix("testtest")
                    .build()
            )
        .build())
        .role("role_arn")
        .build();

    // Put replication configuration
    PutBucketReplicationRequest putBucketReplicationRequest = PutBucketReplicationRequest
      .builder()
      .bucket("source_bucket")
      .replicationConfiguration(replicationConfig)
      .build();

    s3.putBucketReplication(putBucketReplicationRequest);
  }
}
            
```
