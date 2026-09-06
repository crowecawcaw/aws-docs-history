

# Actions, resources, and condition keys for Amazon Rekognition
<a name="list_rekognition"></a>

Amazon Rekognition (service prefix: `rekognition`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/rekognition/latest/APIReference/).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/rekognition/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/rekognition/latest/dg/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/rekognition/rekognition.json) for this service.

**Topics**
+ [API operations defined by Amazon Rekognition](#list_rekognition-operations)
+ [Actions defined by Amazon Rekognition](#list_rekognition-actions-as-permissions)
+ [Resource types defined by Amazon Rekognition](#list_rekognition-resources-for-iam-policies)
+ [Condition keys for Amazon Rekognition](#list_rekognition-policy-keys)

## API operations defined by Amazon Rekognition
<a name="list_rekognition-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_rekognition-actions-as-permissions).




- **   AssociateFaces  **
  - **IAM action:**  [rekognition:AssociateFaces](#list_rekognition-action-AssociateFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CompareFaces  **
  - **IAM action:**  [rekognition:CompareFaces](#list_rekognition-action-CompareFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   CopyProjectVersion  **
  - **IAM action:**  [rekognition:CopyProjectVersion](#list_rekognition-action-CopyProjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:CreateProjectVersion](#list_rekognition-action-CreateProjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateCollection  **
  - **IAM action:**  [rekognition:CreateCollection](#list_rekognition-action-CreateCollection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateDataset  **
  - **IAM action:**  [rekognition:CreateDataset](#list_rekognition-action-CreateDataset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:ListDatasetEntries](#list_rekognition-action-ListDatasetEntries)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateFaceLivenessSession  **
  - **IAM action:**  [rekognition:CreateFaceLivenessSession](#list_rekognition-action-CreateFaceLivenessSession) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProject  **
  - **IAM action:**  [rekognition:CreateProject](#list_rekognition-action-CreateProject)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProjectVersion  **
  - **IAM action:**  [rekognition:CreateProjectVersion](#list_rekognition-action-CreateProjectVersion)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateStreamProcessor  **
  - **IAM action:**  [rekognition:CreateStreamProcessor](#list_rekognition-action-CreateStreamProcessor)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   CreateUser  **
  - **IAM action:**  [rekognition:CreateUser](#list_rekognition-action-CreateUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteCollection  **
  - **IAM action:**  [rekognition:DeleteCollection](#list_rekognition-action-DeleteCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataset  **
  - **IAM action:**  [rekognition:DeleteDataset](#list_rekognition-action-DeleteDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteFaces  **
  - **IAM action:**  [rekognition:DeleteFaces](#list_rekognition-action-DeleteFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProject  **
  - **IAM action:**  [rekognition:DeleteProject](#list_rekognition-action-DeleteProject) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProjectPolicy  **
  - **IAM action:**  [rekognition:DeleteProjectPolicy](#list_rekognition-action-DeleteProjectPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProjectVersion  **
  - **IAM action:**  [rekognition:DeleteProjectVersion](#list_rekognition-action-DeleteProjectVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteStreamProcessor  **
  - **IAM action:**  [rekognition:DeleteStreamProcessor](#list_rekognition-action-DeleteStreamProcessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteUser  **
  - **IAM action:**  [rekognition:DeleteUser](#list_rekognition-action-DeleteUser) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeCollection  **
  - **IAM action:**  [rekognition:DescribeCollection](#list_rekognition-action-DescribeCollection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDataset  **
  - **IAM action:**  [rekognition:DescribeDataset](#list_rekognition-action-DescribeDataset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProjectVersions  **
  - **IAM action:**  [rekognition:DescribeProjectVersions](#list_rekognition-action-DescribeProjectVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeProjects  **
  - **IAM action:**  [rekognition:DescribeProjects](#list_rekognition-action-DescribeProjects) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeStreamProcessor  **
  - **IAM action:**  [rekognition:DescribeStreamProcessor](#list_rekognition-action-DescribeStreamProcessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectCustomLabels  **
  - **IAM action:**  [rekognition:DetectCustomLabels](#list_rekognition-action-DetectCustomLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectFaces  **
  - **IAM action:**  [rekognition:DetectFaces](#list_rekognition-action-DetectFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectLabels  **
  - **IAM action:**  [rekognition:DetectLabels](#list_rekognition-action-DetectLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectModerationLabels  **
  - **IAM action:**  [rekognition:DetectModerationLabels](#list_rekognition-action-DetectModerationLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectProtectiveEquipment  **
  - **IAM action:**  [rekognition:DetectProtectiveEquipment](#list_rekognition-action-DetectProtectiveEquipment) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DetectText  **
  - **IAM action:**  [rekognition:DetectText](#list_rekognition-action-DetectText) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DisassociateFaces  **
  - **IAM action:**  [rekognition:DisassociateFaces](#list_rekognition-action-DisassociateFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DistributeDatasetEntries  **
  - **IAM action:**  [rekognition:DistributeDatasetEntries](#list_rekognition-action-DistributeDatasetEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCelebrityInfo  **
  - **IAM action:**  [rekognition:GetCelebrityInfo](#list_rekognition-action-GetCelebrityInfo) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCelebrityRecognition  **
  - **IAM action:**  [rekognition:GetCelebrityRecognition](#list_rekognition-action-GetCelebrityRecognition) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContentModeration  **
  - **IAM action:**  [rekognition:GetContentModeration](#list_rekognition-action-GetContentModeration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFaceDetection  **
  - **IAM action:**  [rekognition:GetFaceDetection](#list_rekognition-action-GetFaceDetection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFaceLivenessSessionResults  **
  - **IAM action:**  [rekognition:GetFaceLivenessSessionResults](#list_rekognition-action-GetFaceLivenessSessionResults) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetFaceSearch  **
  - **IAM action:**  [rekognition:GetFaceSearch](#list_rekognition-action-GetFaceSearch) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLabelDetection  **
  - **IAM action:**  [rekognition:GetLabelDetection](#list_rekognition-action-GetLabelDetection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMediaAnalysisJob  **
  - **IAM action:**  [rekognition:GetMediaAnalysisJob](#list_rekognition-action-GetMediaAnalysisJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPersonTracking  **
  - **IAM action:**  [rekognition:GetPersonTracking](#list_rekognition-action-GetPersonTracking) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSegmentDetection  **
  - **IAM action:**  [rekognition:GetSegmentDetection](#list_rekognition-action-GetSegmentDetection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetTextDetection  **
  - **IAM action:**  [rekognition:GetTextDetection](#list_rekognition-action-GetTextDetection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   IndexFaces  **
  - **IAM action:**  [rekognition:IndexFaces](#list_rekognition-action-IndexFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListCollections  **
  - **IAM action:**  [rekognition:ListCollections](#list_rekognition-action-ListCollections) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasetEntries  **
  - **IAM action:**  [rekognition:ListDatasetEntries](#list_rekognition-action-ListDatasetEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDatasetLabels  **
  - **IAM action:**  [rekognition:ListDatasetLabels](#list_rekognition-action-ListDatasetLabels) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFaces  **
  - **IAM action:**  [rekognition:ListFaces](#list_rekognition-action-ListFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListMediaAnalysisJobs  **
  - **IAM action:**  [rekognition:ListMediaAnalysisJobs](#list_rekognition-action-ListMediaAnalysisJobs) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListProjectPolicies  **
  - **IAM action:**  [rekognition:ListProjectPolicies](#list_rekognition-action-ListProjectPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListStreamProcessors  **
  - **IAM action:**  [rekognition:ListStreamProcessors](#list_rekognition-action-ListStreamProcessors) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [rekognition:ListTagsForResource](#list_rekognition-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListUsers  **
  - **IAM action:**  [rekognition:ListUsers](#list_rekognition-action-ListUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutProjectPolicy  **
  - **IAM action:**  [rekognition:PutProjectPolicy](#list_rekognition-action-PutProjectPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RecognizeCelebrities  **
  - **IAM action:**  [rekognition:RecognizeCelebrities](#list_rekognition-action-RecognizeCelebrities) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchFaces  **
  - **IAM action:**  [rekognition:SearchFaces](#list_rekognition-action-SearchFaces) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchFacesByImage  **
  - **IAM action:**  [rekognition:SearchFacesByImage](#list_rekognition-action-SearchFacesByImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchUsers  **
  - **IAM action:**  [rekognition:SearchUsers](#list_rekognition-action-SearchUsers) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   SearchUsersByImage  **
  - **IAM action:**  [rekognition:SearchUsersByImage](#list_rekognition-action-SearchUsersByImage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartCelebrityRecognition  **
  - **IAM action:**  [rekognition:StartCelebrityRecognition](#list_rekognition-action-StartCelebrityRecognition)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartContentModeration  **
  - **IAM action:**  [rekognition:StartContentModeration](#list_rekognition-action-StartContentModeration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartFaceDetection  **
  - **IAM action:**  [rekognition:StartFaceDetection](#list_rekognition-action-StartFaceDetection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartFaceSearch  **
  - **IAM action:**  [rekognition:StartFaceSearch](#list_rekognition-action-StartFaceSearch)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartLabelDetection  **
  - **IAM action:**  [rekognition:StartLabelDetection](#list_rekognition-action-StartLabelDetection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartMediaAnalysisJob  **
  - **IAM action:**  [rekognition:StartMediaAnalysisJob](#list_rekognition-action-StartMediaAnalysisJob) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPersonTracking  **
  - **IAM action:**  [rekognition:StartPersonTracking](#list_rekognition-action-StartPersonTracking)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartProjectVersion  **
  - **IAM action:**  [rekognition:StartProjectVersion](#list_rekognition-action-StartProjectVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartSegmentDetection  **
  - **IAM action:**  [rekognition:StartSegmentDetection](#list_rekognition-action-StartSegmentDetection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StartStreamProcessor  **
  - **IAM action:**  [rekognition:StartStreamProcessor](#list_rekognition-action-StartStreamProcessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartTextDetection  **
  - **IAM action:**  [rekognition:StartTextDetection](#list_rekognition-action-StartTextDetection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** rekognition.amazonaws.com / **Access level:** Write

- **   StopProjectVersion  **
  - **IAM action:**  [rekognition:StopProjectVersion](#list_rekognition-action-StopProjectVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopStreamProcessor  **
  - **IAM action:**  [rekognition:StopStreamProcessor](#list_rekognition-action-StopStreamProcessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [rekognition:TagResource](#list_rekognition-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [rekognition:UntagResource](#list_rekognition-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateDatasetEntries  **
  - **IAM action:**  [rekognition:UpdateDatasetEntries](#list_rekognition-action-UpdateDatasetEntries) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateStreamProcessor  **
  - **IAM action:**  [rekognition:UpdateStreamProcessor](#list_rekognition-action-UpdateStreamProcessor) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by Amazon Rekognition
<a name="list_rekognition-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html)  **
  - **Description:** Grants permission to associate multiple individual faces with a single user
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html)  **
  - **Description:** Grants permission to compare faces in the source input image with each face detected in the target input image
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [CopyProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CopyProjectVersion.html)  **
  - **Description:** Grants permission to copy an existing model version to a new model version
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [projectversion\*](#list_rekognition-resource-projectversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html)  **
  - **Description:** Grants permission to create a collection in an AWS Region
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateDataset.html)  **
  - **Description:** Grants permission to create a new Amazon Rekognition Custom Labels dataset
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateFaceLivenessSession.html)  **
  - **Description:** Grants permission to create a face liveness session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateProject](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html)  **
  - **Description:** Grants permission to create an Amazon Rekognition Custom Labels project
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html)  **
  - **Description:** Grants permission to begin training a new version of a model 
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html)  **
  - **Description:** Grants permission to create an Amazon Rekognition stream processor
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Write

- **   [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html)  **
  - **Description:** Grants permission to create a new user in a collection using a unique user ID you provide
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html)  **
  - **Description:** Grants permission to delete the specified collection
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteDataset.html)  **
  - **Description:** Grants permission to delete an existing Amazon Rekognition Custom Labels dataset
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html)  **
  - **Description:** Grants permission to delete faces from a collection
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProject](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProject.html)  **
  - **Description:** Grants permission to delete a project
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProjectPolicy](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectPolicy.html)  **
  - **Description:** Grants permission to delete a resource policy attached to a project
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectVersion.html)  **
  - **Description:** Grants permission to delete a model
  - **Resource types (\*required):** [projectversion\*](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteStreamProcessor.html)  **
  - **Description:** Grants permission to delete the specified stream processor
  - **Resource types (\*required):** [streamprocessor\*](#list_rekognition-resource-streamprocessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html)  **
  - **Description:** Grants permission to delete a user from a collection based on the provided user ID
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html)  **
  - **Description:** Grants permission to read details about a collection
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeDataset.html)  **
  - **Description:** Grants permission to describe an Amazon Rekognition Custom Labels dataset
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProjectVersions](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions.html)  **
  - **Description:** Grants permission to list the versions of a model in an Amazon Rekognition Custom Labels project
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeProjects](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjects.html)  **
  - **Description:** Grants permission to list Amazon Rekognition Custom Labels projects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeStreamProcessor.html)  **
  - **Description:** Grants permission to get information about the specified stream processor
  - **Resource types (\*required):** [streamprocessor\*](#list_rekognition-resource-streamprocessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html)  **
  - **Description:** Grants permission to detect custom labels in a supplied image
  - **Resource types (\*required):** [projectversion\*](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)  **
  - **Description:** Grants permission to detect human faces within an image provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html)  **
  - **Description:** Grants permission to detect instances of real-world labels within an image provided as input
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html)  **
  - **Description:** Grants permission to detect moderation labels within the input image
  - **Resource types (\*required):** [projectversion](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html)  **
  - **Description:** Grants permission to detect Personal Protective Equipment in the input image
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html)  **
  - **Description:** Grants permission to detect text in the input image and convert it into machine-readable text
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html)  **
  - **Description:** Grants permission to remove the association between a user ID and a face ID
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DistributeDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DistributeDatasetEntries.html)  **
  - **Description:** Grants permission to distribute the entries in a training dataset across the training dataset and the test dataset for a project
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCelebrityInfo](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html)  **
  - **Description:** Grants permission to read the name, and additional information, of a celebrity
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityRecognition.html)  **
  - **Description:** Grants permission to read the celebrity recognition results found in a stored video by an asynchronous celebrity recognition job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetContentModeration.html)  **
  - **Description:** Grants permission to read the content moderation analysis results found in a stored video by an asynchronous content moderation job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html)  **
  - **Description:** Grants permission to read the faces detection results found in a stored video by an asynchronous face detection job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFaceLivenessSessionResults](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceLivenessSessionResults.html)  **
  - **Description:** Grants permission to get results of a face liveness session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceSearch.html)  **
  - **Description:** Grants permission to read the matching collection faces found in a stored video by an asynchronous face search job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html)  **
  - **Description:** Grants permission to read the label detected resuls found in a stored video by an asynchronous label detection job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetMediaAnalysisJob.html)  **
  - **Description:** Grants permission to read the reference to job results in S3 and additional information about a media analysis job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html)  **
  - **Description:** Grants permission to read the list of persons detected in a stored video by an asynchronous person tracking job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html)  **
  - **Description:** Grants permission to get the vdeo segments found in a stored video by an asynchronous segment detection job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetTextDetection.html)  **
  - **Description:** Grants permission to get the text found in a stored video by an asynchronous text detection job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html)  **
  - **Description:** Grants permission to update an existing collection with faces detected in the input image
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html)  **
  - **Description:** Grants permission to read the collection Id's in your account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetEntries.html)  **
  - **Description:** Grants permission to list the dataset entries in an existing Amazon Rekognition Custom Labels dataset
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListDatasetLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetLabels.html)  **
  - **Description:** Grants permission to list the labels in a dataset
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html)  **
  - **Description:** Grants permission to read metadata for faces in the specificed collection
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListMediaAnalysisJobs](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListMediaAnalysisJobs.html)  **
  - **Description:** Grants permission to read the list of media analysis jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListProjectPolicies](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListProjectPolicies.html)  **
  - **Description:** Grants permission to list the resource policies attached to a project
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListStreamProcessors](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListStreamProcessors.html)  **
  - **Description:** Grants permission to get a list of your stream processors
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to return a list of tags associated with a resource
  - **Resource types (\*required):** [collection](#list_rekognition-resource-collection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [dataset](#list_rekognition-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [project](#list_rekognition-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [projectversion](#list_rekognition-resource-projectversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [streamprocessor](#list_rekognition-resource-streamprocessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html)  **
  - **Description:** Grants permission to list UserIds and the UserStatus
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutProjectPolicy](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PutProjectPolicy.html)  **
  - **Description:** Grants permission to attach a resource policy to a project
  - **Resource types (\*required):** [project\*](#list_rekognition-resource-project)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html)  **
  - **Description:** Grants permission to detect celebrities in the input image
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html)  **
  - **Description:** Grants permission to search the specificed collection for the supplied face ID
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html)  **
  - **Description:** Grants permission to search the specificed collection for the largest face in the input image
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html)  **
  - **Description:** Grants permission to search the specificed collection for user match result with given either face ID or user ID
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html)  **
  - **Description:** Grants permission to search the specificed collection for user match result by using the largest face in the input image
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html)  **
  - **Description:** Grants permission to start the asynchronous recognition of celebrities in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html)  **
  - **Description:** Grants permission to start asynchronous detection of explicit or suggestive adult content in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html)  **
  - **Description:** Grants permission to start asynchronous detection of faces in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html)  **
  - **Description:** Grants permission to start streaming video for a face liveness session
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html)  **
  - **Description:** Grants permission to start an asynchronous search for faces in a collection that match the faces of persons detected in a stored video
  - **Resource types (\*required):** [collection\*](#list_rekognition-resource-collection)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html)  **
  - **Description:** Grants permission to start asynchronous detection of labels in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html)  **
  - **Description:** Grants permission to start a media analysis job
  - **Resource types (\*required):** [projectversion](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html)  **
  - **Description:** Grants permission to start the asynchronous tracking of persons in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartProjectVersion.html)  **
  - **Description:** Grants permission to start running a model version
  - **Resource types (\*required):** [projectversion\*](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html)  **
  - **Description:** Grants permission to start the asynchronous detection of segments in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html)  **
  - **Description:** Grants permission to start running a stream processor
  - **Resource types (\*required):** [streamprocessor\*](#list_rekognition-resource-streamprocessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetection.html)  **
  - **Description:** Grants permission to start the asynchronous detection of text in a stored video
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [StopProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopProjectVersion.html)  **
  - **Description:** Grants permission to stop a running model version
  - **Resource types (\*required):** [projectversion\*](#list_rekognition-resource-projectversion)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopStreamProcessor.html)  **
  - **Description:** Grants permission to stop a running stream processor
  - **Resource types (\*required):** [streamprocessor\*](#list_rekognition-resource-streamprocessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add one or more tags to a resource
  - **Resource types (\*required):** [collection](#list_rekognition-resource-collection) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_rekognition-resource-dataset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_rekognition-resource-project) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [projectversion](#list_rekognition-resource-projectversion) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [streamprocessor](#list_rekognition-resource-streamprocessor) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_rekognition-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove one or more tags from a resource
  - **Resource types (\*required):** [collection](#list_rekognition-resource-collection) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [dataset](#list_rekognition-resource-dataset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [project](#list_rekognition-resource-project) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [projectversion](#list_rekognition-resource-projectversion) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Resource types (\*required):** [streamprocessor](#list_rekognition-resource-streamprocessor) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_rekognition-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateDatasetEntries.html)  **
  - **Description:** Grants permission to add or update one or more JSON Lines (entries) in a dataset
  - **Resource types (\*required):** [dataset\*](#list_rekognition-resource-dataset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateStreamProcessor.html)  **
  - **Description:** Grants permission to modify properties for a stream processor
  - **Resource types (\*required):** [streamprocessor\*](#list_rekognition-resource-streamprocessor)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon Rekognition
<a name="list_rekognition-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [collection](https://docs.aws.amazon.com/rekognition/latest/dg/collections.html)  | arn:${Partition}:rekognition:${Region}:${Account}:collection/${CollectionId} | [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_) | 
|  [dataset](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/creating-datasets.html)  | arn:${Partition}:rekognition:${Region}:${Account}:project/${ProjectName}/dataset/${DatasetType}/${CreationTimestamp} | [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_) | 
|  [project](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/mp-create-project.html)  | arn:${Partition}:rekognition:${Region}:${Account}:project/${ProjectName}/${CreationTimestamp} | [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_) | 
|  [projectversion](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/training-model.html)  | arn:${Partition}:rekognition:${Region}:${Account}:project/${ProjectName}/version/${VersionName}/${CreationTimestamp} | [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_) | 
|  [streamprocessor](https://docs.aws.amazon.com/rekognition/latest/dg/streaming-video.html)  | arn:${Partition}:rekognition:${Region}:${Account}:streamprocessor/${StreamprocessorId} | [aws:ResourceTag/${TagKey}](#list_rekognition-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon Rekognition
<a name="list_rekognition-policy-keys"></a>

Amazon Rekognition defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by tag keys that are passed in the request | ArrayOfString | 