

# Logging Amazon Comprehend API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon Comprehend is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Comprehend. CloudTrail captures API calls for Amazon Comprehend as events. The calls captured include calls from the Amazon Comprehend console and code calls to the Amazon Comprehend API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Comprehend. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Comprehend, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Amazon Comprehend information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When supported event activity occurs in Amazon Comprehend, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Amazon Comprehend, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Amazon Comprehend supports logging the following actions as events in CloudTrail log files:
+  [BatchDetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectDominantLanguage.html)
+  [BatchDetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectEntities.html)
+  [BatchDetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectKeyPhrases.html)
+  [BatchDetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectSentiment.html)
+  [BatchDetectSyntax](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectSyntax.html)
+  [ClassifyDocument](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ClassifyDocument.html)
+  [CreateDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDocumentClassifier.html)
+  [CreateEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateEndpoint.html)
+  [CreateEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateEntityRecognizer.html)
+  [DeleteDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteDocumentClassifier.html)
+  [DeleteEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteEndpoint.html)
+  [DeleteEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteEntityRecognizer.html)
+  [DescribeDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassificationJob.html)
+  [DescribeDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassifier.html) 
+  [DescribeDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDominantLanguageDetectionJob.html) 
+  [DescribeEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEndpoint.html)
+  [DescribeEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEntitiesDetectionJob.html) 
+  [DescribeEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEntityRecognizer.html) 
+  [DescribeKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeKeyPhrasesDetectionJob.html) 
+  [DescribePiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribePiiEntitiesDetectionJob.html) 
+  [DescribeSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeSentimentDetectionJob.html) 
+  [DescribeTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeTargetedSentimentDetectionJob.html) 
+  [DescribeTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeTopicsDetectionJob.html) 
+  [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectDominantLanguage.html)
+ [DetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectEntities.html)
+ [DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectKeyPhrases.html)
+ [DetectPiiEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectPiiEntities.html)
+ [DetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSentiment.html)
+ [DetectSyntax](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSyntax.html)
+  [ListDocumentClassificationJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassificationJobs.html) 
+  [ListDocumentClassifiers](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassifiers.html) 
+  [ListDominantLanguageDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDominantLanguageDetectionJobs.html) 
+  [ListEndpoints](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEndpoints.html)
+  [ListEntitiesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEntitiesDetectionJobs.html) 
+  [ListEntityRecognizers](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEntityRecognizers.html) 
+  [ListKeyPhrasesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListKeyPhrasesDetectionJobs.html) 
+  [ListPiiEntitiesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListPiiEntitiesDetectionJobs.html) 
+  [ListSentimentDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListSentimentDetectionJobs.html) 
+  [ListTargetedSentimentDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTargetedSentimentDetectionJobs.html) 
+  [ListTagsForResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTagsForResource.html) 
+  [ListTopicsDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTopicsDetectionJobs.html) 
+  [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html) 
+  [StartDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDominantLanguageDetectionJob.html) 
+  [StartEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEntitiesDetectionJob.html) 
+  [StartKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartKeyPhrasesDetectionJob.html) 
+  [StartPiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartPiiEntitiesDetectionJob.html) 
+  [StartSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartSentimentDetectionJob.html)
+  [StartTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTargetedSentimentDetectionJob.html)
+  [StartTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTopicsDetectionJob.html) 
+  [StopDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopDominantLanguageDetectionJob.html) 
+  [StopEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopEntitiesDetectionJob.html) 
+  [StopKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopKeyPhrasesDetectionJob.html) 
+  [StopPiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopPiiEntitiesDetectionJob.html) 
+  [StopSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopSentimentDetectionJob.html) 
+  [StopTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTargetedSentimentDetectionJob.html) 
+  [StopTrainingDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTrainingDocumentClassifier.html) 
+  [StopTrainingEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTrainingEntityRecognizer.html)
+  [TagResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_TagResource.html)
+  [UntagResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_UntagResource.html)
+  [UpdateEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_UpdateEndpoint.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with the root user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Example: Amazon Comprehend log file entries
<a name="understanding-service-name-entries"></a>

 A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `ClassifyDocument` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AROAICFHPEXAMPLE",
        "arn": "arn:aws:iam::12345678910:user/myadmin2",
        "accountId": "12345678910",
        "accessKeyId": "ASIA3VZEXAMPLE",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2023-10-19T14:22:09Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2023-10-19T17:31:20Z",
    "eventSource": "comprehend.amazonaws.com",
    "eventName": "ClassifyDocument",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "3.21.185.237",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/115.0",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "fd916e66-caac-46c9-a1fc-81a0ef33e61b",
    "eventID": "535ca22b-b3a3-4c13-b2c5-bf51ab082794",
    "readOnly": false,
    "resources": [
        {
            "accountId": "12345678910",
            "type": "AWS::Comprehend::DocumentClassifierEndpoint",
            "ARN": "arn:aws:comprehend:us-east-2:12345678910:document-classifier-endpoint/endpointExample"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "12345678910"
}
```