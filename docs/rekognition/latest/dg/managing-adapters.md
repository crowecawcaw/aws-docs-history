

# Managing adapters with the AWS CLI and SDKs
<a name="managing-adapters"></a>

 Rekognition lets you make use of multiple features that leverage pre-trained computer vision models. With these models you can carry out tasks like label detection and content moderation. You can also customize these certain models using an adapter. 

You can make use of Rekognition’s project creation and project management APIs (like [CreateProject](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html) and [CreateProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html)) to create and train adapters. The following pages describe how to use the API operations to create, train, and manage your adapters, using the AWS Console, your chosen AWS SDK, or the AWS CLI. 

After you train an adapter you can use it when running inference with supported features. Currently, adapters are supported when using the Content Moderation feature.

When you train an adapter using an AWS SDK you must provide your ground-truth labels (image annotations) in the form of a manifest file. Alternatively, you can use the Rekognition Console to create and train an adapter.

**Note**  
 Adapters cannot be copied. Only Rekognition Custom Labels project versions can be copied. 

**Topics**
+ [Adapter statuses](#managing-adapters-project-versions-statuses)
+ [Creating a project](managing-adapters-create-project.md)
+ [Describing projects](managing-adapters-describe-projects.md)
+ [Deleting a project](managing-adapters-delete-project.md)
+ [Creating a project version](managing-adapters-create-project-version.md)
+ [Describing a project version](managing-adapters-describe-project.md)
+ [Deleting a project version](managing-adapters-delete-project-version.md)

## Adapter statuses
<a name="managing-adapters-project-versions-statuses"></a>

Custom Moderation adapter (project versions) can be in one of the following statuses: 
+ TRAINING\_IN\_PROGRESS - The adapter is in the process of training on the files you provided as training documents.
+ TRAINING\_COMPLETED - The adapter has successfully completed training and is ready for you to review its performance. 
+ TRAINING\_FAILED - The adapter has failed to complete its training for some reason, review the output manifest file and output manifest summary for information on the cause of the failure.
+ DELETING - The adapter is in the process of being deleted.
+ DEPRECATED - The adapter was trained on an older version of the Content Moderation base model. It is in a grace period and it will expire within 60 to 90 days of the release of the new base model version. During the grace period, you can still use the adapter for inference with [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) or [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html) API operations. Refer to Custom Moderation Console for the expiry date of your adapters.
+ EXPIRED - The adapter was trained on an older version of the Content Moderation base model and it can no longer be used to obtain custom results with the DetectModerationLabels or StartMediaAnalysisJob API operations. If an Expired adapter is specified in an inference request, it will be ignored and the response is returned from the most recent version of the Custom Moderation base model instead. 