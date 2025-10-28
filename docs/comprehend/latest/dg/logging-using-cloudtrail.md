# Logging Amazon Comprehend API calls with

AWS CloudTrail

Amazon Comprehend is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in Amazon Comprehend. CloudTrail captures API calls for
Amazon Comprehend as events. The calls captured include calls from the Amazon Comprehend console and
code calls to the Amazon Comprehend API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Comprehend. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to Amazon Comprehend, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## Amazon Comprehend information in

CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported
event activity occurs in Amazon Comprehend, that activity is recorded in a CloudTrail event along
with other AWS service events in **Event history**. You can view,
search, and download recent events in your AWS account. For more information, see
[Viewing events with CloudTrail event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for
Amazon Comprehend, create a trail. A _trail_ enables CloudTrail to deliver log
files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail
applies to all AWS Regions. The trail logs events from all Regions in the AWS
partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally,
you can configure other AWS services to further analyze and act upon the event data
collected in CloudTrail logs. For more information, see the following:

- [Overview
  for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Amazon Comprehend supports logging the following actions as events in CloudTrail log
files:

- [BatchDetectDominantLanguage](../APIReference/API_BatchDetectDominantLanguage.md "../APIReference/API_BatchDetectDominantLanguage.md")
- [BatchDetectEntities](../APIReference/API_BatchDetectEntities.md "../APIReference/API_BatchDetectEntities.md")
- [BatchDetectKeyPhrases](../APIReference/API_BatchDetectKeyPhrases.md "../APIReference/API_BatchDetectKeyPhrases.md")
- [BatchDetectSentiment](../APIReference/API_BatchDetectSentiment.md "../APIReference/API_BatchDetectSentiment.md")
- [BatchDetectSyntax](../APIReference/API_BatchDetectSyntax.md "../APIReference/API_BatchDetectSyntax.md")
- [ClassifyDocument](../APIReference/API_ClassifyDocument.md "../APIReference/API_ClassifyDocument.md")
- [CreateDocumentClassifier](../APIReference/API_CreateDocumentClassifier.md "../APIReference/API_CreateDocumentClassifier.md")
- [CreateEndpoint](../APIReference/API_CreateEndpoint.md "../APIReference/API_CreateEndpoint.md")
- [CreateEntityRecognizer](../APIReference/API_CreateEntityRecognizer.md "../APIReference/API_CreateEntityRecognizer.md")
- [DeleteDocumentClassifier](../APIReference/API_DeleteDocumentClassifier.md "../APIReference/API_DeleteDocumentClassifier.md")
- [DeleteEndpoint](../APIReference/API_DeleteEndpoint.md "../APIReference/API_DeleteEndpoint.md")
- [DeleteEntityRecognizer](../APIReference/API_DeleteEntityRecognizer.md "../APIReference/API_DeleteEntityRecognizer.md")
- [DescribeDocumentClassificationJob](../APIReference/API_DescribeDocumentClassificationJob.md "../APIReference/API_DescribeDocumentClassificationJob.md")
- [DescribeDocumentClassifier](../APIReference/API_DescribeDocumentClassifier.md "../APIReference/API_DescribeDocumentClassifier.md")
- [DescribeDominantLanguageDetectionJob](../APIReference/API_DescribeDominantLanguageDetectionJob.md "../APIReference/API_DescribeDominantLanguageDetectionJob.md")
- [DescribeEndpoint](../APIReference/API_DescribeEndpoint.md "../APIReference/API_DescribeEndpoint.md")
- [DescribeEntitiesDetectionJob](../APIReference/API_DescribeEntitiesDetectionJob.md "../APIReference/API_DescribeEntitiesDetectionJob.md")
- [DescribeEntityRecognizer](../APIReference/API_DescribeEntityRecognizer.md "../APIReference/API_DescribeEntityRecognizer.md")
- [DescribeKeyPhrasesDetectionJob](../APIReference/API_DescribeKeyPhrasesDetectionJob.md "../APIReference/API_DescribeKeyPhrasesDetectionJob.md")
- [DescribePiiEntitiesDetectionJob](../APIReference/API_DescribePiiEntitiesDetectionJob.md "../APIReference/API_DescribePiiEntitiesDetectionJob.md")
- [DescribeSentimentDetectionJob](../APIReference/API_DescribeSentimentDetectionJob.md "../APIReference/API_DescribeSentimentDetectionJob.md")
- [DescribeTargetedSentimentDetectionJob](../APIReference/API_DescribeTargetedSentimentDetectionJob.md "../APIReference/API_DescribeTargetedSentimentDetectionJob.md")
- [DescribeTopicsDetectionJob](../APIReference/API_DescribeTopicsDetectionJob.md "../APIReference/API_DescribeTopicsDetectionJob.md")
- [DetectDominantLanguage](../APIReference/API_DetectDominantLanguage.md "../APIReference/API_DetectDominantLanguage.md")
- [DetectEntities](../APIReference/API_DetectEntities.md "../APIReference/API_DetectEntities.md")
- [DetectKeyPhrases](../APIReference/API_DetectKeyPhrases.md "../APIReference/API_DetectKeyPhrases.md")
- [DetectPiiEntities](../APIReference/API_DetectPiiEntities.md "../APIReference/API_DetectPiiEntities.md")
- [DetectSentiment](../APIReference/API_DetectSentiment.md "../APIReference/API_DetectSentiment.md")
- [DetectSyntax](../APIReference/API_DetectSyntax.md "../APIReference/API_DetectSyntax.md")
- [ListDocumentClassificationJobs](../APIReference/API_ListDocumentClassificationJobs.md "../APIReference/API_ListDocumentClassificationJobs.md")
- [ListDocumentClassifiers](../APIReference/API_ListDocumentClassifiers.md "../APIReference/API_ListDocumentClassifiers.md")
- [ListDominantLanguageDetectionJobs](../APIReference/API_ListDominantLanguageDetectionJobs.md "../APIReference/API_ListDominantLanguageDetectionJobs.md")
- [ListEndpoints](../APIReference/API_ListEndpoints.md "../APIReference/API_ListEndpoints.md")
- [ListEntitiesDetectionJobs](../APIReference/API_ListEntitiesDetectionJobs.md "../APIReference/API_ListEntitiesDetectionJobs.md")
- [ListEntityRecognizers](../APIReference/API_ListEntityRecognizers.md "../APIReference/API_ListEntityRecognizers.md")
- [ListKeyPhrasesDetectionJobs](../APIReference/API_ListKeyPhrasesDetectionJobs.md "../APIReference/API_ListKeyPhrasesDetectionJobs.md")
- [ListPiiEntitiesDetectionJobs](../APIReference/API_ListPiiEntitiesDetectionJobs.md "../APIReference/API_ListPiiEntitiesDetectionJobs.md")
- [ListSentimentDetectionJobs](../APIReference/API_ListSentimentDetectionJobs.md "../APIReference/API_ListSentimentDetectionJobs.md")
- [ListTargetedSentimentDetectionJobs](../APIReference/API_ListTargetedSentimentDetectionJobs.md "../APIReference/API_ListTargetedSentimentDetectionJobs.md")
- [ListTagsForResource](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md")
- [ListTopicsDetectionJobs](../APIReference/API_ListTopicsDetectionJobs.md "../APIReference/API_ListTopicsDetectionJobs.md")
- [StartDocumentClassificationJob](../APIReference/API_StartDocumentClassificationJob.md "../APIReference/API_StartDocumentClassificationJob.md")
- [StartDominantLanguageDetectionJob](../APIReference/API_StartDominantLanguageDetectionJob.md "../APIReference/API_StartDominantLanguageDetectionJob.md")
- [StartEntitiesDetectionJob](../APIReference/API_StartEntitiesDetectionJob.md "../APIReference/API_StartEntitiesDetectionJob.md")
- [StartKeyPhrasesDetectionJob](../APIReference/API_StartKeyPhrasesDetectionJob.md "../APIReference/API_StartKeyPhrasesDetectionJob.md")
- [StartPiiEntitiesDetectionJob](../APIReference/API_StartPiiEntitiesDetectionJob.md "../APIReference/API_StartPiiEntitiesDetectionJob.md")
- [StartSentimentDetectionJob](../APIReference/API_StartSentimentDetectionJob.md "../APIReference/API_StartSentimentDetectionJob.md")
- [StartTargetedSentimentDetectionJob](../APIReference/API_StartTargetedSentimentDetectionJob.md "../APIReference/API_StartTargetedSentimentDetectionJob.md")
- [StartTopicsDetectionJob](../APIReference/API_StartTopicsDetectionJob.md "../APIReference/API_StartTopicsDetectionJob.md")
- [StopDominantLanguageDetectionJob](../APIReference/API_StopDominantLanguageDetectionJob.md "../APIReference/API_StopDominantLanguageDetectionJob.md")
- [StopEntitiesDetectionJob](../APIReference/API_StopEntitiesDetectionJob.md "../APIReference/API_StopEntitiesDetectionJob.md")
- [StopKeyPhrasesDetectionJob](../APIReference/API_StopKeyPhrasesDetectionJob.md "../APIReference/API_StopKeyPhrasesDetectionJob.md")
- [StopPiiEntitiesDetectionJob](../APIReference/API_StopPiiEntitiesDetectionJob.md "../APIReference/API_StopPiiEntitiesDetectionJob.md")
- [StopSentimentDetectionJob](../APIReference/API_StopSentimentDetectionJob.md "../APIReference/API_StopSentimentDetectionJob.md")
- [StopTargetedSentimentDetectionJob](../APIReference/API_StopTargetedSentimentDetectionJob.md "../APIReference/API_StopTargetedSentimentDetectionJob.md")
- [StopTrainingDocumentClassifier](../APIReference/API_StopTrainingDocumentClassifier.md "../APIReference/API_StopTrainingDocumentClassifier.md")
- [StopTrainingEntityRecognizer](../APIReference/API_StopTrainingEntityRecognizer.md "../APIReference/API_StopTrainingEntityRecognizer.md")
- [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [UpdateEndpoint](../APIReference/API_UpdateEndpoint.md "../APIReference/API_UpdateEndpoint.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with the root user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: Amazon Comprehend log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the requested
action, the date and time of the action, request parameters, and so on. CloudTrail log files
aren't an ordered stack trace of the public API calls, so they don't appear in any
specific order.

The following example shows a CloudTrail log entry that demonstrates the
`ClassifyDocument` action.

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
