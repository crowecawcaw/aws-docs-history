

# Actions, resources, and condition keys for Amazon Comprehend
<a name="list_comprehend"></a>

Amazon Comprehend (service prefix: `comprehend`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/comprehend/latest/dg/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/comprehend/latest/APIReference/welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/comprehend/latest/dg/auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/comprehend/comprehend.json) for this service.

**Topics**
+ [API operations defined by Amazon Comprehend](#list_comprehend-operations)
+ [Actions defined by Amazon Comprehend](#list_comprehend-actions-as-permissions)
+ [Resource types defined by Amazon Comprehend](#list_comprehend-resources-for-iam-policies)
+ [Condition keys for Amazon Comprehend](#list_comprehend-policy-keys)

## API operations defined by Amazon Comprehend
<a name="list_comprehend-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_comprehend-actions-as-permissions).




- **   BatchDetectDominantLanguage  **
  - **IAM action:**  [comprehend:BatchDetectDominantLanguage](#list_comprehend-action-BatchDetectDominantLanguage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDetectEntities  **
  - **IAM action:**  [comprehend:BatchDetectEntities](#list_comprehend-action-BatchDetectEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDetectKeyPhrases  **
  - **IAM action:**  [comprehend:BatchDetectKeyPhrases](#list_comprehend-action-BatchDetectKeyPhrases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDetectSentiment  **
  - **IAM action:**  [comprehend:BatchDetectSentiment](#list_comprehend-action-BatchDetectSentiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDetectSyntax  **
  - **IAM action:**  [comprehend:BatchDetectSyntax](#list_comprehend-action-BatchDetectSyntax) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   BatchDetectTargetedSentiment  **
  - **IAM action:**  [comprehend:BatchDetectTargetedSentiment](#list_comprehend-action-BatchDetectTargetedSentiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ClassifyDocument  **
  - **IAM action:**  [comprehend:ClassifyDocument](#list_comprehend-action-ClassifyDocument) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ContainsPiiEntities  **
  - **IAM action:**  [comprehend:ContainsPiiEntities](#list_comprehend-action-ContainsPiiEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CreateDataset  **
  - **IAM action:**  [comprehend:CreateDataset](#list_comprehend-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDocumentClassifier  **
  - **IAM action:**  [comprehend:CreateDocumentClassifier](#list_comprehend-action-CreateDocumentClassifier)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   CreateEndpoint  **
  - **IAM action:**  [comprehend:CreateEndpoint](#list_comprehend-action-CreateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   CreateEntityRecognizer  **
  - **IAM action:**  [comprehend:CreateEntityRecognizer](#list_comprehend-action-CreateEntityRecognizer)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   CreateFlywheel  **
  - **IAM action:**  [comprehend:CreateFlywheel](#list_comprehend-action-CreateFlywheel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   DeleteDocumentClassifier  **
  - **IAM action:**  [comprehend:DeleteDocumentClassifier](#list_comprehend-action-DeleteDocumentClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEndpoint  **
  - **IAM action:**  [comprehend:DeleteEndpoint](#list_comprehend-action-DeleteEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteEntityRecognizer  **
  - **IAM action:**  [comprehend:DeleteEntityRecognizer](#list_comprehend-action-DeleteEntityRecognizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFlywheel  **
  - **IAM action:**  [comprehend:DeleteFlywheel](#list_comprehend-action-DeleteFlywheel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourcePolicy  **
  - **IAM action:**  [comprehend:DeleteResourcePolicy](#list_comprehend-action-DeleteResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataset  **
  - **IAM action:**  [comprehend:DescribeDataset](#list_comprehend-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDocumentClassificationJob  **
  - **IAM action:**  [comprehend:DescribeDocumentClassificationJob](#list_comprehend-action-DescribeDocumentClassificationJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDocumentClassifier  **
  - **IAM action:**  [comprehend:DescribeDocumentClassifier](#list_comprehend-action-DescribeDocumentClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDominantLanguageDetectionJob  **
  - **IAM action:**  [comprehend:DescribeDominantLanguageDetectionJob](#list_comprehend-action-DescribeDominantLanguageDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEndpoint  **
  - **IAM action:**  [comprehend:DescribeEndpoint](#list_comprehend-action-DescribeEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:DescribeEntitiesDetectionJob](#list_comprehend-action-DescribeEntitiesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEntityRecognizer  **
  - **IAM action:**  [comprehend:DescribeEntityRecognizer](#list_comprehend-action-DescribeEntityRecognizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeEventsDetectionJob  **
  - **IAM action:**  [comprehend:DescribeEventsDetectionJob](#list_comprehend-action-DescribeEventsDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlywheel  **
  - **IAM action:**  [comprehend:DescribeFlywheel](#list_comprehend-action-DescribeFlywheel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeFlywheelIteration  **
  - **IAM action:**  [comprehend:DescribeFlywheelIteration](#list_comprehend-action-DescribeFlywheelIteration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeKeyPhrasesDetectionJob  **
  - **IAM action:**  [comprehend:DescribeKeyPhrasesDetectionJob](#list_comprehend-action-DescribeKeyPhrasesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribePiiEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:DescribePiiEntitiesDetectionJob](#list_comprehend-action-DescribePiiEntitiesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeResourcePolicy  **
  - **IAM action:**  [comprehend:DescribeResourcePolicy](#list_comprehend-action-DescribeResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeSentimentDetectionJob  **
  - **IAM action:**  [comprehend:DescribeSentimentDetectionJob](#list_comprehend-action-DescribeSentimentDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTargetedSentimentDetectionJob  **
  - **IAM action:**  [comprehend:DescribeTargetedSentimentDetectionJob](#list_comprehend-action-DescribeTargetedSentimentDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeTopicsDetectionJob  **
  - **IAM action:**  [comprehend:DescribeTopicsDetectionJob](#list_comprehend-action-DescribeTopicsDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectDominantLanguage  **
  - **IAM action:**  [comprehend:DetectDominantLanguage](#list_comprehend-action-DetectDominantLanguage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectEntities  **
  - **IAM action:**  [comprehend:DetectEntities](#list_comprehend-action-DetectEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectKeyPhrases  **
  - **IAM action:**  [comprehend:DetectKeyPhrases](#list_comprehend-action-DetectKeyPhrases) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectPiiEntities  **
  - **IAM action:**  [comprehend:DetectPiiEntities](#list_comprehend-action-DetectPiiEntities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectSentiment  **
  - **IAM action:**  [comprehend:DetectSentiment](#list_comprehend-action-DetectSentiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectSyntax  **
  - **IAM action:**  [comprehend:DetectSyntax](#list_comprehend-action-DetectSyntax) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectTargetedSentiment  **
  - **IAM action:**  [comprehend:DetectTargetedSentiment](#list_comprehend-action-DetectTargetedSentiment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectToxicContent  **
  - **IAM action:**  [comprehend:DetectToxicContent](#list_comprehend-action-DetectToxicContent) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ImportModel  **
  - **IAM action:**  [comprehend:ImportModel](#list_comprehend-action-ImportModel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   ListDatasets  **
  - **IAM action:**  [comprehend:ListDatasets](#list_comprehend-action-ListDatasets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDocumentClassificationJobs  **
  - **IAM action:**  [comprehend:ListDocumentClassificationJobs](#list_comprehend-action-ListDocumentClassificationJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDocumentClassifierSummaries  **
  - **IAM action:**  [comprehend:ListDocumentClassifierSummaries](#list_comprehend-action-ListDocumentClassifierSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDocumentClassifiers  **
  - **IAM action:**  [comprehend:ListDocumentClassifiers](#list_comprehend-action-ListDocumentClassifiers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDominantLanguageDetectionJobs  **
  - **IAM action:**  [comprehend:ListDominantLanguageDetectionJobs](#list_comprehend-action-ListDominantLanguageDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEndpoints  **
  - **IAM action:**  [comprehend:ListEndpoints](#list_comprehend-action-ListEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEntitiesDetectionJobs  **
  - **IAM action:**  [comprehend:ListEntitiesDetectionJobs](#list_comprehend-action-ListEntitiesDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEntityRecognizerSummaries  **
  - **IAM action:**  [comprehend:ListEntityRecognizerSummaries](#list_comprehend-action-ListEntityRecognizerSummaries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEntityRecognizers  **
  - **IAM action:**  [comprehend:ListEntityRecognizers](#list_comprehend-action-ListEntityRecognizers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListEventsDetectionJobs  **
  - **IAM action:**  [comprehend:ListEventsDetectionJobs](#list_comprehend-action-ListEventsDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFlywheelIterationHistory  **
  - **IAM action:**  [comprehend:ListFlywheelIterationHistory](#list_comprehend-action-ListFlywheelIterationHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFlywheels  **
  - **IAM action:**  [comprehend:ListFlywheels](#list_comprehend-action-ListFlywheels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListKeyPhrasesDetectionJobs  **
  - **IAM action:**  [comprehend:ListKeyPhrasesDetectionJobs](#list_comprehend-action-ListKeyPhrasesDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListPiiEntitiesDetectionJobs  **
  - **IAM action:**  [comprehend:ListPiiEntitiesDetectionJobs](#list_comprehend-action-ListPiiEntitiesDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListSentimentDetectionJobs  **
  - **IAM action:**  [comprehend:ListSentimentDetectionJobs](#list_comprehend-action-ListSentimentDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTagsForResource  **
  - **IAM action:**  [comprehend:ListTagsForResource](#list_comprehend-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTargetedSentimentDetectionJobs  **
  - **IAM action:**  [comprehend:ListTargetedSentimentDetectionJobs](#list_comprehend-action-ListTargetedSentimentDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTopicsDetectionJobs  **
  - **IAM action:**  [comprehend:ListTopicsDetectionJobs](#list_comprehend-action-ListTopicsDetectionJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutResourcePolicy  **
  - **IAM action:**  [comprehend:PutResourcePolicy](#list_comprehend-action-PutResourcePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartDocumentClassificationJob  **
  - **IAM action:**  [comprehend:StartDocumentClassificationJob](#list_comprehend-action-StartDocumentClassificationJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartDominantLanguageDetectionJob  **
  - **IAM action:**  [comprehend:StartDominantLanguageDetectionJob](#list_comprehend-action-StartDominantLanguageDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:StartEntitiesDetectionJob](#list_comprehend-action-StartEntitiesDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartEventsDetectionJob  **
  - **IAM action:**  [comprehend:StartEventsDetectionJob](#list_comprehend-action-StartEventsDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartFlywheelIteration  **
  - **IAM action:**  [comprehend:StartFlywheelIteration](#list_comprehend-action-StartFlywheelIteration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartKeyPhrasesDetectionJob  **
  - **IAM action:**  [comprehend:StartKeyPhrasesDetectionJob](#list_comprehend-action-StartKeyPhrasesDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartPiiEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:StartPiiEntitiesDetectionJob](#list_comprehend-action-StartPiiEntitiesDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartSentimentDetectionJob  **
  - **IAM action:**  [comprehend:StartSentimentDetectionJob](#list_comprehend-action-StartSentimentDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartTargetedSentimentDetectionJob  **
  - **IAM action:**  [comprehend:StartTargetedSentimentDetectionJob](#list_comprehend-action-StartTargetedSentimentDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StartTopicsDetectionJob  **
  - **IAM action:**  [comprehend:StartTopicsDetectionJob](#list_comprehend-action-StartTopicsDetectionJob)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   StopDominantLanguageDetectionJob  **
  - **IAM action:**  [comprehend:StopDominantLanguageDetectionJob](#list_comprehend-action-StopDominantLanguageDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:StopEntitiesDetectionJob](#list_comprehend-action-StopEntitiesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopEventsDetectionJob  **
  - **IAM action:**  [comprehend:StopEventsDetectionJob](#list_comprehend-action-StopEventsDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopKeyPhrasesDetectionJob  **
  - **IAM action:**  [comprehend:StopKeyPhrasesDetectionJob](#list_comprehend-action-StopKeyPhrasesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopPiiEntitiesDetectionJob  **
  - **IAM action:**  [comprehend:StopPiiEntitiesDetectionJob](#list_comprehend-action-StopPiiEntitiesDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopSentimentDetectionJob  **
  - **IAM action:**  [comprehend:StopSentimentDetectionJob](#list_comprehend-action-StopSentimentDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTargetedSentimentDetectionJob  **
  - **IAM action:**  [comprehend:StopTargetedSentimentDetectionJob](#list_comprehend-action-StopTargetedSentimentDetectionJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTrainingDocumentClassifier  **
  - **IAM action:**  [comprehend:StopTrainingDocumentClassifier](#list_comprehend-action-StopTrainingDocumentClassifier) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopTrainingEntityRecognizer  **
  - **IAM action:**  [comprehend:StopTrainingEntityRecognizer](#list_comprehend-action-StopTrainingEntityRecognizer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [comprehend:TagResource](#list_comprehend-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [comprehend:UntagResource](#list_comprehend-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateEndpoint  **
  - **IAM action:**  [comprehend:UpdateEndpoint](#list_comprehend-action-UpdateEndpoint)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write

- **   UpdateFlywheel  **
  - **IAM action:**  [comprehend:UpdateFlywheel](#list_comprehend-action-UpdateFlywheel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** comprehend.amazonaws.com / **Access level:** Write



## Actions defined by Amazon Comprehend
<a name="list_comprehend-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [BatchDetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectDominantLanguage.html)  **
  - **Description:** Grants permission to detect the language or languages present in the list of text documents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchDetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectEntities.html)  **
  - **Description:** Grants permission to detect the named entities ("People", "Places", "Locations", etc) within the given list of text documents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchDetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectKeyPhrases.html)  **
  - **Description:** Grants permission to detect the phrases in the list of text documents that are most indicative of the content
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchDetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectSentiment.html)  **
  - **Description:** Grants permission to detect the sentiment of a text in the list of documents (Positive, Negative, Neutral, or Mixed)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchDetectSyntax](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectSyntax.html)  **
  - **Description:** Grants permission to detect syntactic information (like Part of Speech, Tokens) in a list of text documents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [BatchDetectTargetedSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_BatchDetectTargetedSentiment.html)  **
  - **Description:** Grants permission to detect the sentiments associated with specific entities (such as brands or products) within the given list of text documents
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ClassifyDocument](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ClassifyDocument.html)  **
  - **Description:** Grants permission to create a new document classification request to analyze a single document in real-time, using a previously created and trained custom model and an endpoint
  - **Resource types (\*required):** [document-classifier-endpoint\*](#list_comprehend-resource-document-classifier-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ContainsPiiEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ContainsPiiEntities.html)  **
  - **Description:** Grants permission to classify the personally identifiable information within given documents in real-time
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CreateDataset](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a new dataset within a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDocumentClassifier.html)  **
  - **Description:** Grants permission to create a new document classifier that you can use to categorize documents
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [CreateEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateEndpoint.html)  **
  - **Description:** Grants permission to create a model-specific endpoint for synchronous inference for a previously trained custom model
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document-classifier-endpoint\*](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer-endpoint\*](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateEntityRecognizer.html)  **
  - **Description:** Grants permission to create an entity recognizer using submitted files
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [CreateFlywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateFlywheel.html)  **
  - **Description:** Grants permission to create a new flywheel that you can use to train model versions
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:DataLakeKmsKey](#list_comprehend-comprehend_DataLakeKmsKey)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [DeleteDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteDocumentClassifier.html)  **
  - **Description:** Grants permission to delete a previously created document classifier
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteEndpoint.html)  **
  - **Description:** Grants permission to delete a model-specific endpoint for a previously-trained custom model. All endpoints must be deleted in order for the model to be deleted
  - **Resource types (\*required):** [document-classifier-endpoint\*](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer-endpoint\*](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteEntityRecognizer.html)  **
  - **Description:** Grants permission to delete a submitted entity recognizer
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFlywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteFlywheel.html)  **
  - **Description:** Grants permission to Delete a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourcePolicy](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DeleteResourcePolicy.html)  **
  - **Description:** Grants permission to remove policy on resource
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDataset](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Grants permission to get the properties associated with a dataset
  - **Resource types (\*required):** [flywheel-dataset\*](#list_comprehend-resource-flywheel-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassificationJob.html)  **
  - **Description:** Grants permission to get the properties associated with a document classification job
  - **Resource types (\*required):** [document-classification-job\*](#list_comprehend-resource-document-classification-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDocumentClassifier.html)  **
  - **Description:** Grants permission to get the properties associated with a document classifier
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeDominantLanguageDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a dominant language detection job
  - **Resource types (\*required):** [dominant-language-detection-job\*](#list_comprehend-resource-dominant-language-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEndpoint.html)  **
  - **Description:** Grants permission to get the properties associated with a specific endpoint. Use this operation to get the status of an endpoint
  - **Resource types (\*required):** [document-classifier-endpoint\*](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer-endpoint\*](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with an entities detection job
  - **Resource types (\*required):** [entities-detection-job\*](#list_comprehend-resource-entities-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEntityRecognizer.html)  **
  - **Description:** Grants permission to provide details about an entity recognizer including status, S3 buckets containing training data, recognizer metadata, metrics, and so on
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeEventsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeEventsDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with an Events detection job
  - **Resource types (\*required):** [events-detection-job\*](#list_comprehend-resource-events-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeFlywheel.html)  **
  - **Description:** Grants permission to get the properties associated with a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeFlywheelIteration](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeFlywheelIteration.html)  **
  - **Description:** Grants permission to get the properties associated with a flywheel iteration for a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[comprehend:FlywheelIterationId](#list_comprehend-comprehend_FlywheelIterationId)
  - **Access level:** Read

- **   [DescribeKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeKeyPhrasesDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a key phrases detection job
  - **Resource types (\*required):** [key-phrases-detection-job\*](#list_comprehend-resource-key-phrases-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribePiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribePiiEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a PII entities detection job
  - **Resource types (\*required):** [pii-entities-detection-job\*](#list_comprehend-resource-pii-entities-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeResourcePolicy](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeResourcePolicy.html)  **
  - **Description:** Grants permission to read attached policy on resource
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeSentimentDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a sentiment detection job
  - **Resource types (\*required):** [sentiment-detection-job\*](#list_comprehend-resource-sentiment-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeTargetedSentimentDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a targeted sentiment detection job
  - **Resource types (\*required):** [targeted-sentiment-detection-job\*](#list_comprehend-resource-targeted-sentiment-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DescribeTopicsDetectionJob.html)  **
  - **Description:** Grants permission to get the properties associated with a topic detection job
  - **Resource types (\*required):** [topics-detection-job\*](#list_comprehend-resource-topics-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectDominantLanguage](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectDominantLanguage.html)  **
  - **Description:** Grants permission to detect the language or languages present in the text
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectEntities.html)  **
  - **Description:** Grants permission to detect the named entities ("People", "Places", "Locations", etc) within the given text document
  - **Resource types (\*required):** [entity-recognizer-endpoint](#list_comprehend-resource-entity-recognizer-endpoint)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectKeyPhrases](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectKeyPhrases.html)  **
  - **Description:** Grants permission to detect the phrases in the text that are most indicative of the content
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectPiiEntities](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectPiiEntities.html)  **
  - **Description:** Grants permission to detect the personally identifiable information entities ("Name", "SSN", "PIN", etc) within the given text document
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSentiment.html)  **
  - **Description:** Grants permission to detect the sentiment of a text in a document (Positive, Negative, Neutral, or Mixed)
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectSyntax](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectSyntax.html)  **
  - **Description:** Grants permission to detect syntactic information (like Part of Speech, Tokens) in a text document
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectTargetedSentiment](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectTargetedSentiment.html)  **
  - **Description:** Grants permission to detect the sentiments associated with specific entities (such as brands or products) in a document
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectToxicContent](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_DetectToxicContent.html)  **
  - **Description:** Grants permission to detect toxic content within the given list of text segments
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ImportModel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ImportModel.html)  **
  - **Description:** Grants permission to import a trained Comprehend model
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)
  - **Access level:** Write

- **   [ListDatasets](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDatasets.html)  **
  - **Description:** Grants permission to get a list of the Datasets associated with a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDocumentClassificationJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassificationJobs.html)  **
  - **Description:** Grants permission to get a list of the document classification jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDocumentClassifierSummaries](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassifierSummaries.html)  **
  - **Description:** Grants permission to get a list of summaries of the document classifiers that you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDocumentClassifiers](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDocumentClassifiers.html)  **
  - **Description:** Grants permission to get a list of the document classifiers that you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDominantLanguageDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListDominantLanguageDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of the dominant language detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEndpoints](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEndpoints.html)  **
  - **Description:** Grants permission to get a list of all existing endpoints that you've created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEntitiesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEntitiesDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of the entity detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEntityRecognizerSummaries](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEntityRecognizerSummaries.html)  **
  - **Description:** Grants permission to get a list of summaries for the entity recognizers that you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEntityRecognizers](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEntityRecognizers.html)  **
  - **Description:** Grants permission to get a list of the properties of all entity recognizers that you created, including recognizers currently in training
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListEventsDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListEventsDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of Events detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFlywheelIterationHistory](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListFlywheelIterationHistory.html)  **
  - **Description:** Grants permission to get a list of iterations associated for a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFlywheels](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListFlywheels.html)  **
  - **Description:** Grants permission to get a list of the flywheels that you have created
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListKeyPhrasesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListKeyPhrasesDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of key phrase detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListPiiEntitiesDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListPiiEntitiesDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of PII entities detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListSentimentDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListSentimentDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of sentiment detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTagsForResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** [document-classification-job](#list_comprehend-resource-document-classification-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [document-classifier-endpoint](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dominant-language-detection-job](#list_comprehend-resource-dominant-language-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entities-detection-job](#list_comprehend-resource-entities-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer-endpoint](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [events-detection-job](#list_comprehend-resource-events-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel-dataset](#list_comprehend-resource-flywheel-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [key-phrases-detection-job](#list_comprehend-resource-key-phrases-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [pii-entities-detection-job](#list_comprehend-resource-pii-entities-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [sentiment-detection-job](#list_comprehend-resource-sentiment-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [targeted-sentiment-detection-job](#list_comprehend-resource-targeted-sentiment-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [topics-detection-job](#list_comprehend-resource-topics-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTargetedSentimentDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTargetedSentimentDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of targeted sentiment detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListTopicsDetectionJobs](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_ListTopicsDetectionJobs.html)  **
  - **Description:** Grants permission to get a list of the topic detection jobs that you have submitted
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [PutResourcePolicy](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_PutResourcePolicy.html)  **
  - **Description:** Grants permission to attach policy to resource
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDocumentClassificationJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html)  **
  - **Description:** Grants permission to start an asynchronous document classification job
  - **Resource types (\*required):** [document-classification-job\*](#list_comprehend-resource-document-classification-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDominantLanguageDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous dominant language detection job for a collection of documents
  - **Resource types (\*required):** [dominant-language-detection-job\*](#list_comprehend-resource-dominant-language-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [StartEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous entity detection job for a collection of documents
  - **Resource types (\*required):** [entities-detection-job\*](#list_comprehend-resource-entities-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartEventsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEventsDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous Events detection job for a collection of documents
  - **Resource types (\*required):** [events-detection-job\*](#list_comprehend-resource-events-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)
  - **Access level:** Write

- **   [StartFlywheelIteration](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartFlywheelIteration.html)  **
  - **Description:** Grants permission to start a flywheel iteration for a flywheel
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartKeyPhrasesDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous key phrase detection job for a collection of documents
  - **Resource types (\*required):** [key-phrases-detection-job\*](#list_comprehend-resource-key-phrases-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [StartPiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartPiiEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous PII entities detection job for a collection of documents
  - **Resource types (\*required):** [pii-entities-detection-job\*](#list_comprehend-resource-pii-entities-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)
  - **Access level:** Write

- **   [StartSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartSentimentDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous sentiment detection job for a collection of documents
  - **Resource types (\*required):** [sentiment-detection-job\*](#list_comprehend-resource-sentiment-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [StartTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTargetedSentimentDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous targeted sentiment detection job for a collection of documents
  - **Resource types (\*required):** [targeted-sentiment-detection-job\*](#list_comprehend-resource-targeted-sentiment-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [StartTopicsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTopicsDetectionJob.html)  **
  - **Description:** Grants permission to start an asynchronous job to detect the most common topics in the collection of documents and the phrases associated with each topic
  - **Resource types (\*required):** [topics-detection-job\*](#list_comprehend-resource-topics-detection-job)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)<br />[comprehend:OutputKmsKey](#list_comprehend-comprehend_OutputKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write

- **   [StopDominantLanguageDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopDominantLanguageDetectionJob.html)  **
  - **Description:** Grants permission to stop a dominant language detection job
  - **Resource types (\*required):** [dominant-language-detection-job\*](#list_comprehend-resource-dominant-language-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to stop an entity detection job
  - **Resource types (\*required):** [entities-detection-job\*](#list_comprehend-resource-entities-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopEventsDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopEventsDetectionJob.html)  **
  - **Description:** Grants permission to stop an Events detection job
  - **Resource types (\*required):** [events-detection-job\*](#list_comprehend-resource-events-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopKeyPhrasesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopKeyPhrasesDetectionJob.html)  **
  - **Description:** Grants permission to stop a key phrase detection job
  - **Resource types (\*required):** [key-phrases-detection-job\*](#list_comprehend-resource-key-phrases-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopPiiEntitiesDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopPiiEntitiesDetectionJob.html)  **
  - **Description:** Grants permission to stop a PII entities detection job
  - **Resource types (\*required):** [pii-entities-detection-job\*](#list_comprehend-resource-pii-entities-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopSentimentDetectionJob.html)  **
  - **Description:** Grants permission to stop a sentiment detection job
  - **Resource types (\*required):** [sentiment-detection-job\*](#list_comprehend-resource-sentiment-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTargetedSentimentDetectionJob](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTargetedSentimentDetectionJob.html)  **
  - **Description:** Grants permission to stop a targeted sentiment detection job
  - **Resource types (\*required):** [targeted-sentiment-detection-job\*](#list_comprehend-resource-targeted-sentiment-detection-job)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTrainingDocumentClassifier](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTrainingDocumentClassifier.html)  **
  - **Description:** Grants permission to stop a previously created document classifier training job
  - **Resource types (\*required):** [document-classifier\*](#list_comprehend-resource-document-classifier)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopTrainingEntityRecognizer](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StopTrainingEntityRecognizer.html)  **
  - **Description:** Grants permission to stop a previously created entity recognizer training job
  - **Resource types (\*required):** [entity-recognizer\*](#list_comprehend-resource-entity-recognizer)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource with given key value pairs
  - **Resource types (\*required):** [document-classification-job](#list_comprehend-resource-document-classification-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [document-classifier-endpoint](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [dominant-language-detection-job](#list_comprehend-resource-dominant-language-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entities-detection-job](#list_comprehend-resource-entities-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entity-recognizer-endpoint](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [events-detection-job](#list_comprehend-resource-events-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [flywheel-dataset](#list_comprehend-resource-flywheel-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [key-phrases-detection-job](#list_comprehend-resource-key-phrases-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [pii-entities-detection-job](#list_comprehend-resource-pii-entities-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [sentiment-detection-job](#list_comprehend-resource-sentiment-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [targeted-sentiment-detection-job](#list_comprehend-resource-targeted-sentiment-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [topics-detection-job](#list_comprehend-resource-topics-detection-job) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_comprehend-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource with given key
  - **Resource types (\*required):** [document-classification-job](#list_comprehend-resource-document-classification-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [document-classifier-endpoint](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [dominant-language-detection-job](#list_comprehend-resource-dominant-language-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entities-detection-job](#list_comprehend-resource-entities-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [entity-recognizer-endpoint](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [events-detection-job](#list_comprehend-resource-events-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [flywheel-dataset](#list_comprehend-resource-flywheel-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [key-phrases-detection-job](#list_comprehend-resource-key-phrases-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [pii-entities-detection-job](#list_comprehend-resource-pii-entities-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [sentiment-detection-job](#list_comprehend-resource-sentiment-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [targeted-sentiment-detection-job](#list_comprehend-resource-targeted-sentiment-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Resource types (\*required):** [topics-detection-job](#list_comprehend-resource-topics-detection-job) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_comprehend-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateEndpoint](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_UpdateEndpoint.html)  **
  - **Description:** Grants permission to update information about the specified endpoint
  - **Resource types (\*required):** [document-classifier-endpoint\*](#list_comprehend-resource-document-classifier-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer-endpoint\*](#list_comprehend-resource-entity-recognizer-endpoint) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateFlywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_UpdateFlywheel.html)  **
  - **Description:** Grants permission to Update a flywheel's configuration
  - **Resource types (\*required):** [document-classifier](#list_comprehend-resource-document-classifier) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [entity-recognizer](#list_comprehend-resource-entity-recognizer) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [flywheel\*](#list_comprehend-resource-flywheel) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_)<br />[comprehend:ModelKmsKey](#list_comprehend-comprehend_ModelKmsKey)<br />[comprehend:VolumeKmsKey](#list_comprehend-comprehend_VolumeKmsKey)<br />[comprehend:VpcSecurityGroupIds](#list_comprehend-comprehend_VpcSecurityGroupIds)<br />[comprehend:VpcSubnets](#list_comprehend-comprehend_VpcSubnets)
  - **Access level:** Write



## Resource types defined by Amazon Comprehend
<a name="list_comprehend-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [document-classification-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDocumentClassificationJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:document-classification-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [document-classifier](https://docs.aws.amazon.com/comprehend/latest/dg/how-document-classification-training.html)  | arn:${Partition}:comprehend:${Region}:${Account}:document-classifier/${DocumentClassifierName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [document-classifier-endpoint](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)  | arn:${Partition}:comprehend:${Region}:${Account}:document-classifier-endpoint/${DocumentClassifierEndpointName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [dominant-language-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartDominantLanguageDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:dominant-language-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [entities-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEntitiesDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:entities-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [entity-recognizer](https://docs.aws.amazon.com/comprehend/latest/dg/training-recognizers.html)  | arn:${Partition}:comprehend:${Region}:${Account}:entity-recognizer/${EntityRecognizerName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [entity-recognizer-endpoint](https://docs.aws.amazon.com/comprehend/latest/dg/manage-endpoints.html)  | arn:${Partition}:comprehend:${Region}:${Account}:entity-recognizer-endpoint/${EntityRecognizerEndpointName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [events-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartEventsDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:events-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [flywheel](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateFlywheel.html)  | arn:${Partition}:comprehend:${Region}:${Account}:flywheel/${FlywheelName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [flywheel-dataset](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_CreateDataset.html)  | arn:${Partition}:comprehend:${Region}:${Account}:flywheel/${FlywheelName}/dataset/${DatasetName} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [key-phrases-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartKeyPhrasesDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:key-phrases-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [pii-entities-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartPiiEntitiesDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:pii-entities-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [sentiment-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartSentimentDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:sentiment-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [targeted-sentiment-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTargetedSentimentDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:targeted-sentiment-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 
|  [topics-detection-job](https://docs.aws.amazon.com/comprehend/latest/APIReference/API_StartTopicsDetectionJob.html)  | arn:${Partition}:comprehend:${Region}:${Account}:topics-detection-job/${JobId} | [aws:ResourceTag/${TagKey}](#list_comprehend-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Comprehend
<a name="list_comprehend-policy-keys"></a>

Amazon Comprehend defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag values present in a resource creation request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring tag value associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-globally-available)  | Filters access by requiring the presence of mandatory tags in the request | ArrayOfString | 
|   [comprehend:DataLakeKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the DataLake Kms Key associated with the flywheel resource in the request | ARN | 
|   [comprehend:FlywheelIterationId](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by particular Iteration Id for a flywheel | String | 
|   [comprehend:ModelKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the model KMS key associated with the resource in the request | ARN | 
|   [comprehend:OutputKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the output KMS key associated with the resource in the request | ARN | 
|   [comprehend:VolumeKmsKey](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the volume KMS key associated with the resource in the request | ARN | 
|   [comprehend:VpcSecurityGroupIds](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the list of all VPC security group ids associated with the resource in the request | ArrayOfString | 
|   [comprehend:VpcSubnets](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncomprehend.html#amazoncomprehend-policy-keys)  | Filters access by the list of all VPC subnets associated with the resource in the request | ArrayOfString | 