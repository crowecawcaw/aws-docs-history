# Send S3 event notifications to Amazon EventBridge using an AWS SDK

The following code example shows how to enable a bucket to send S3 event notifications to EventBridge and route notifications to an Amazon SNS topic and Amazon SQS queue.


Java


**SDK for Java 2.x**

###### Note


 There's more on GitHub. Find the complete example and learn how to set up and run in the
 [AWS Code
 Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/s3#code-examples").
 



```
    /** This method configures a bucket to send events to AWS EventBridge and creates a rule
     * to route the S3 object created events to a topic and a queue.
     *
     * @param bucketName Name of existing bucket
     * @param topicArn ARN of existing topic to receive S3 event notifications
     * @param queueArn ARN of existing queue to receive S3 event notifications
     *
     *  An AWS CloudFormation stack sets up the bucket, queue, topic before the method runs.
     */
    public static String setBucketNotificationToEventBridge(String bucketName, String topicArn, String queueArn) {
        try {
            // Enable bucket to emit S3 Event notifications to EventBridge.
            s3Client.putBucketNotificationConfiguration(b -> b
                    .bucket(bucketName)
                    .notificationConfiguration(b1 -> b1
                            .eventBridgeConfiguration(
                                    SdkBuilder::build)
                    ).build()).join();

            // Create an EventBridge rule to route Object Created notifications.
            PutRuleRequest putRuleRequest = PutRuleRequest.builder()
                    .name(RULE_NAME)
                    .eventPattern("""
                            {
                              "source": ["aws.s3"],
                              "detail-type": ["Object Created"],
                              "detail": {
                                "bucket": {
                                  "name": ["%s"]
                                }
                              }
                            }
                            """.formatted(bucketName))
                    .build();

            // Add the rule to the default event bus.
            PutRuleResponse putRuleResponse = eventBridgeClient.putRule(putRuleRequest)
                    .whenComplete((r, t) -> {
                        if (t != null) {
                            logger.error("Error creating event bus rule: " + t.getMessage(), t);
                            throw new RuntimeException(t.getCause().getMessage(), t);
                        }
                        logger.info("Event bus rule creation request sent successfully. ARN is: {}", r.ruleArn());
                    }).join();

            // Add the existing SNS topic and SQS queue as targets to the rule.
            eventBridgeClient.putTargets(b -> b
                    .eventBusName("default")
                    .rule(RULE_NAME)
                    .targets(List.of (
                            Target.builder()
                                    .arn(queueArn)
                                    .id("Queue")
                                    .build(),
                            Target.builder()
                                    .arn(topicArn)
                                    .id("Topic")
                                    .build())
                            )
                    ).join();
            return putRuleResponse.ruleArn();
        } catch (S3Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return null;
    }


```


* For API details, see the following topics in *AWS SDK for Java 2.x API Reference*.




	+ [PutBucketNotificationConfiguration](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotificationConfiguration "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/PutBucketNotificationConfiguration")
	+ [PutRule](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutRule "https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutRule")
	+ [PutTargets](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutTargets "https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/PutTargets")




For a complete list of AWS SDK developer guides and code examples, see
 [Developing with Amazon S3 using the AWS SDKs](sdk-general-information-section.md "sdk-general-information-section.md").
 This topic also includes information about getting started and details about previous SDK versions.
