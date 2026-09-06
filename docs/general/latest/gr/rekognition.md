

# Amazon Rekognition endpoints and quotas
<a name="rekognition"></a>

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints. Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md).

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For more information, see [AWS service quotas](aws_service_limits.md).

The following are the service endpoints and service quotas for this service.

## Service endpoints
<a name="rekognition_region"></a>

 Amazon Rekognition API operations (excluding streaming API operations) are available at the following regions and endpoints: 


| Region Name | Region | Endpoint | Protocol | 
| --- | --- | --- | --- | 
| US East (Ohio) | us-east-2 |  rekognition.us-east-2.amazonaws.com <br /> rekognition.us-east-2.api.aws <br /> rekognition-fips.us-east-2.amazonaws.com <br /> rekognition-fips.us-east-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US East (N. Virginia) | us-east-1 |  rekognition.us-east-1.amazonaws.com <br /> rekognition-fips.us-east-1.amazonaws.com <br /> rekognition.us-east-1.api.aws <br /> rekognition-fips.us-east-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (N. California) | us-west-1 |  rekognition.us-west-1.amazonaws.com <br /> rekognition.us-west-1.api.aws <br /> rekognition-fips.us-west-1.api.aws <br /> rekognition-fips.us-west-1.amazonaws.com  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| US West (Oregon) | us-west-2 |  rekognition.us-west-2.amazonaws.com <br /> rekognition-fips.us-west-2.amazonaws.com <br /> rekognition.us-west-2.api.aws <br /> rekognition-fips.us-west-2.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Asia Pacific (Malaysia) | ap-southeast-5 |  rekognition.ap-southeast-5.amazonaws.com <br /> rekognition.ap-southeast-5.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Mumbai) | ap-south-1 |  rekognition.ap-south-1.amazonaws.com <br /> rekognition.ap-south-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Seoul) | ap-northeast-2 |  rekognition.ap-northeast-2.amazonaws.com <br /> rekognition.ap-northeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Singapore) | ap-southeast-1 |  rekognition.ap-southeast-1.amazonaws.com <br /> rekognition.ap-southeast-1.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Sydney) | ap-southeast-2 |  rekognition.ap-southeast-2.amazonaws.com <br /> rekognition.ap-southeast-2.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Thailand) | ap-southeast-7 |  rekognition.ap-southeast-7.amazonaws.com <br /> rekognition.ap-southeast-7.api.aws  | HTTPS<br />HTTPS | 
| Asia Pacific (Tokyo) | ap-northeast-1 |  rekognition.ap-northeast-1.amazonaws.com <br /> rekognition.ap-northeast-1.api.aws  | HTTPS<br />HTTPS | 
| Canada (Central) | ca-central-1 |  rekognition.ca-central-1.amazonaws.com <br /> rekognition.ca-central-1.api.aws <br /> rekognition-fips.ca-central-1.amazonaws.com <br /> rekognition-fips.ca-central-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 
| Europe (Frankfurt) | eu-central-1 |  rekognition.eu-central-1.amazonaws.com <br /> rekognition.eu-central-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (Ireland) | eu-west-1 |  rekognition.eu-west-1.amazonaws.com <br /> rekognition.eu-west-1.api.aws  | HTTPS<br />HTTPS | 
| Europe (London) | eu-west-2 |  rekognition.eu-west-2.amazonaws.com <br /> rekognition.eu-west-2.api.aws  | HTTPS<br />HTTPS | 
| Europe (Spain) | eu-south-2 |  rekognition.eu-south-2.amazonaws.com <br /> rekognition.eu-south-2.api.aws  | HTTPS<br />HTTPS | 
| Israel (Tel Aviv) | il-central-1 |  rekognition.il-central-1.amazonaws.com <br /> rekognition.il-central-1.api.aws  | HTTPS<br />HTTPS | 
| South America (São Paulo) | sa-east-1 |  rekognition.sa-east-1.amazonaws.com <br /> rekognition.sa-east-1.api.aws  | HTTPS<br />HTTPS | 
|  AWS GovCloud (US-West) | us-gov-west-1 |  rekognition.us-gov-west-1.amazonaws.com <br /> rekognition-fips.us-gov-west-1.api.aws <br /> rekognition-fips.us-gov-west-1.amazonaws.com <br /> rekognition.us-gov-west-1.api.aws  | HTTPS<br />HTTPS<br />HTTPS<br />HTTPS | 

### Amazon Rekognition Streaming Endpoints
<a name="regions-streaming-service-endpoints"></a>

The Amazon Rekognition streaming API operations are available at the following regions and endpoints:


| 
| 
| Region Name | Region | Endpoint | Protocol | 
| --- |--- |--- |--- |
| US East (N. Virginia) | us-east-1 | streaming-rekognition.us-east-1.amazonaws.com streaming-rekognition-fips.us-east-1.amazonaws.com | WSSWSS | 
| US West (Oregon) | us-west-2 | streaming-rekognition.us-west-2.amazonaws.com streaming-rekognition-fips.us-west-2.amazonaws.com | WSSWSS | 
| Asia Pacific (Mumbai) | ap-south-1 | streaming-rekognition.ap-south-1.amazonaws.com | WSS | 
| Asia Pacific (Tokyo) | ap-northeast-1 | streaming-rekognition.ap-northeast-1.amazonaws.com | WSS | 
| Europe (Ireland) | eu-west-1 | streaming-rekognition.eu-west-1.amazonaws.com  | WSS | 
| South America (São Paulo) | sa-east-1 | streaming-rekognition.sa-east-1.amazonaws.com | WSS | 
| Asia Pacific (Malaysia) | ap-southeast-5 | streaming-rekognition.ap-southeast-5.amazonaws.com | WSS | 
| Asia Pacific (Thailand) | ap-southeast-7 | streaming-rekognition.ap-southeast-7.amazonaws.com | WSS | 

**Note**  
Some regions only support certain Amazon Rekognition feature or operations. See the sections below for information on these differences.

The following are differences for certain Amazon Rekognition features and AWS Regions.

### Amazon Rekognition Video streaming API
<a name="regions-streaming-video"></a>

The Amazon Rekognition Video streaming API is available in the following regions, depending on the specified Settings when creating a StreamProcessor.

Label Detection (ConnectedHome) API:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Mumbai)
+ Europe (Ireland)

Face Search (FaceSearch) API:
+ US East (N. Virginia)
+ US West (Oregon)
+ Asia Pacific (Tokyo)
+ Europe (Frankfurt)
+ Europe (Ireland)

### Amazon Rekognition Custom Labels
<a name="endpoints-custom-labels"></a>

Amazon Rekognition Custom Labels is available in the following Regions only.
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Frankfurt)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Asia Pacific (Seoul)

### Canada (Central) Region
<a name="endpoints-ca-central-1"></a>

The Canada (Central) Region supports the following operations only.
+ [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html)
+ [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html)
+ [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html)
+ [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html)
+ [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html)
+ [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html)
+ [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)
+ [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html)
+ [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html)
+ [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html)
+ [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html)
+ [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html)
+ [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html)
+ [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html)
+ [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html)
+ [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html)
+ [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html)
+ [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html)

**Note**  
These operations are only available through use of the AWS CLI or SDK, as the Canada (Central) Region doesn't currently provide a console experience for these operations.

### Israel (Tel Aviv) Region
<a name="endpoints-tlv"></a>

The Israel (Tel Aviv) Region supports only the following operations for the following features.



| Feature | Operations | 
| --- | --- | 
| Face detection | [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html) | 
| Face comparison | [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html) | 
| Face search | [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html), [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html), [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html), [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html), [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html), [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html), [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html), [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html), [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html), [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html), [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html), [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html), [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html), [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html), [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html), [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html), [TagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UntagResource.html), [ListTagsForResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListTagsForResource.html) | 
| Label detection | [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) | 
| Moderation | [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) | 
| Text detection | [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) | 

## Service quotas
<a name="limits_rekognition"></a>

The quotas listed on this page are defaults. You can request a quota increase for Amazon Rekognition using the AWS Support Center. To request a quota increase for a Amazon Rekognition Transactions Per Second (TPS) limit, follow the instructions at [Default quotas](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html#changeable-quotas) in the *Amazon Rekognition Developer Guide*.

Quotas increases affect only the specific API operation for the Region in which you make the request. Other API operations and Regions are not affected.


| Resource | Default | 
| --- | --- | 
| Transactions per second per account for individual Amazon Rekognition Image data plane operations:+  [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) <br />+  [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) <br />+  [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) <br />+  [GetCelebrityInfo](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityInfo.html) <br />+  [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html) <br />+  [ListFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListFaces.html) <br />+  [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html) <br />+  [SearchFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFaces.html) <br />+  [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html) <br />+  [SearchUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html) <br />+  [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html)  |  +  US East (Ohio) Region – 5 <br />+  US East (N. Virginia) Region – 50  <br />+  US West (N. California) Region – 5  <br />+  US West (Oregon) Region – 50  <br />+  Asia Pacific (Mumbai) Region – 5  <br />+  Asia Pacific (Seoul) Region – 5  <br />+  Asia Pacific (Singapore) Region – 5  <br />+  Asia Pacific (Sydney) Region – 5 <br />+  Asia Pacific (Tokyo) Region – 5  <br />+  Canada (Central) – 5 (For supported operations, see [Canada (Central) Region](#endpoints-ca-central-1)).  <br />+  Europe (Frankfurt) Region – 5 <br />+  Europe (Spain) Region – 5 <br />+  South America (São Paulo) Region – 5 <br />+  Asia Pacific (Malaysia) Region – 5 <br />+  Asia Pacific (Thailand) Region – 5 <br />+  Europe (Ireland) Region – 50 <br />+  Europe (London) Region – 5 <br />+  Israel (Tel Aviv) Region – 5 (For supported operations, see [Israel (Tel Aviv) Region](#endpoints-tlv)) <br />+  AWS GovCloud (US-West) – 5   | 
| Transactions per second per account for individual Amazon Rekognition Image data plane operations:+  [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html) <br />+  [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html)  |  +  US East (Ohio) Region – 25 <br />+  US East (N. Virginia) Region – 100  <br />+  US West (N. California) Region – 25  <br />+  US West (Oregon) Region – 100  <br />+  Asia Pacific (Mumbai) Region – 25  <br />+  Asia Pacific (Seoul) Region – 25  <br />+  Asia Pacific (Singapore) Region – 25  <br />+  Asia Pacific (Sydney) Region – 25 <br />+  Asia Pacific (Tokyo) Region – 25  <br />+  Canada (Central) – 25 (For supported operations, see [Canada (Central) Region](#endpoints-ca-central-1)).  <br />+  Europe (Frankfurt) Region – 25 <br />+  Europe (Spain) Region – 25 <br />+  South America (São Paulo) Region – 25 <br />+  Asia Pacific (Malaysia) Region – 25 <br />+  Asia Pacific (Thailand) Region – 25 <br />+  Europe (Ireland) Region – 100 <br />+  Europe (London) Region – 25 <br />+  Israel (Tel Aviv) Region – 25 (For supported operations, see [Israel (Tel Aviv) Region](#endpoints-tlv))  <br />+  AWS GovCloud (US-West) – 25   | 
|  Transactions per second per account for the Amazon Rekognition Image data plane operation:+  [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html) <br />+  [DisassociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html)  | In each Region that Amazon Rekognition Image supports – 5 | 
| Transactions per second per account for the personal protective equipment data plane operation:+  [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html)  | In each Region that Amazon Rekognition Image supports – 5 | 
| Transactions per second per account for individual Amazon Rekognition Image control plane operations:+  [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html) <br />+  [DeleteCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteCollection.html) <br />+  [DeleteFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteFaces.html) <br />+  [DescribeCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeCollection.html) <br />+  [ListCollections](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListCollections.html) <br />+  [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html) <br />+  [DeleteUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteUser.html) <br />+  [ListUsers](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html)  | In each Region that Amazon Rekognition Image supports – 5 | 
| Transactions per second per account for individual stored video start operations:+  [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html) <br />+  [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html) <br />+  [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html) <br />+  [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html) <br />+  [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html) <br />+  [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html) <br />+  [StartTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetection.html) <br />+  [StartSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html)  | In each Region that Amazon Rekognition Video supports – 5<br />`StartCelebrityRecognition` is not available in AWS GovCloud (US). | 
| Transactions per second per account for individual Amazon Rekognition Video stored video get operations:+  [GetCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityRecognition.html) <br />+  [GetContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetContentModeration.html) <br />+  [GetFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html) <br />+  [GetFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceSearch.html) <br />+  [GetLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html) <br />+  [GetPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html) <br />+  [GetTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetTextDetection.html) <br />+  [GetSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html)  |  +  US East (Ohio) Region – 5 <br />+  US East (N. Virginia) Region – 20  <br />+  US West (N. California) Region – 5  <br />+  US West (Oregon) Region – 20  <br />+  Asia Pacific (Mumbai) Region – 5  <br />+  Asia Pacific (Seoul) Region – 5  <br />+  Asia Pacific (Singapore) Region – 5  <br />+  Asia Pacific (Sydney) Region – 5 <br />+  Asia Pacific (Tokyo) Region – 5  <br />+  Europe (Frankfurt) Region – 5 <br />+  South America (São Paulo) Region – 5 <br />+  Asia Pacific (Malaysia) Region – 5 <br />+  Asia Pacific (Thailand) Region – 5 <br />+  Europe (Ireland) Region – 20 <br />+  Europe (London) Region – 5 <br />+  AWS GovCloud (US-West) – 20 (`GetCelebrityRecognition` is not available in this Region.)   | 
| Maximum number of concurrent stored video jobs per account | 20 | 
| Transactions per second per account for individual bulk analysis start operations: [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html)  | In each Region that Amazon Rekognition bulk analysis supports: 5 | 
| Transactions per second per account for individual bulk analysis list operations: [ListMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListMediaAnalysisJob.html)  | In each Region that Amazon Rekognition bulk analysis supports: 5 | 
| Transactions per second per account for individual bulk analysis get operations: [GetMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetMediaAnalysisJob.html) | In each Region that Amazon Rekognition bulk analysis supports: 20 | 
| Maximum number of concurrent bulk analysis jobs per account, with regard to region: |  +  US East (N. Virginia) Region – 20  <br />+  US East (Ohio) Region – 5  <br />+  US West (Oregon) Region – 20  <br />+  Europe (Ireland) Region – 20 <br />+  Asia Pacific (Mumbai) Region – 5  <br />+  Asia Pacific (Seoul) Region – 5  <br />+  Asia Pacific (Singapore) Region – 5  <br />+  Asia Pacific (Sydney) Region – 5 <br />+  Asia Pacific (Tokyo) Region – 5  <br />+  Europe (Frankfurt) Region – 5 <br />+  Europe (London) Region – 5   | 
| Maximum number of streaming video stream processors per account that can simultaneously exist  | In each Region that Amazon Rekognition Video supports – 10,000 | 
| Maximum number of face search stream processors per account that can be processed concurrently | In each Region that Amazon Rekognition Video supports face search stream processors – 10 | 
| Maximum number of label detection stream processors per account that can be processed concurrently |  +  US East (N. Virginia) – 200 <br />+  US East (Ohio) – 40 <br />+  US West (Oregon) – 200 <br />+  Asia Pacific (Mumbai) – 40 <br />+  Europe (Ireland) – 40   | 
| Transactions per second per account for individual streaming video operations:+  [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html) <br />+  [DeleteStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteStreamProcessor.html) <br />+  [DescribeStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeStreamProcessor.html) <br />+  [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html) <br />+  [UpdateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateStreamProcessor.html)  | In each Region that Amazon Rekognition Video supports – 20 | 
| Transactions per second per account for stop streaming video operations:+  [StopStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/dg/API_StopStreamProcessor.html)  | In each Region that Amazon Rekognition Video supports – 1 | 
| Transactions per second per account for Amazon Rekognition Face Liveness API operations:+  [CreateFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateFaceLivenessSession.html) <br />+   [GetFaceLivenessSessionResults](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceLivenessSessionResults.html) <br />+  [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html)  |  +  US East (N. Virginia) – 25 <br />+  Europe (Ireland) – 5 <br />+  US West (Oregon) – 25 <br />+  Asia Pacific (Mumbai) – 5 <br />+  Asia Pacific (Tokyo) Region – 5  <br />+  South America (São Paulo) Region – 5 <br />+  Asia Pacific (Malaysia) Region – 5 <br />+  Asia Pacific (Thailand) Region – 5   | 
| Number of concurrent Amazon Rekognition Face Liveness sessions per account, created with [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_rekognitionstreaming_StartFaceLivenessSession.html).  To determine your required concurrent sessions quota, multiply the estimated session length by your estimated TPS. (Ex. 10 seconds x 5 TPS = 50).  |  +  US East (N. Virginia) – 75 <br />+  Europe (Ireland) – 15 <br />+  US West (Oregon) – 75 <br />+  Asia Pacific (Mumbai) – 15 <br />+  Asia Pacific (Tokyo) Region – 15  <br />+  South America (São Paulo) Region – 15 <br />+  Asia Pacific (Malaysia) Region – 15 <br />+  Asia Pacific (Thailand) Region – 15   | 
| Transactions per second per account for list streaming video operations:+  [ListStreamProcessors](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListStreamProcessors.html)  | In each Region that Amazon Rekognition Video supports – 5 | 
| Transactions per second per account for resource tagging operations:+  [ListTagsForResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListTagsForResource.html) <br />+  [TagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_TagResource.html) <br />+  [UntagResource](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UntagResource.html)  | In each Region that Amazon Rekognition Image supports – 10 | 
| Transactions per second per account for individual Amazon Rekognition Custom Label data plane operations:+  [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html)  | In all Regions that Amazon Rekognition Custom Labels supports – 50  | 
| Transactions per second per account for individual Amazon Rekognition Custom Labels control plane operations:+  [CopyProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CopyProjectVersion.html) <br />+  [CreateDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateDataset.html) <br />+  [CreateProject](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProject.html) <br />+  [CreateProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateProjectVersion.html) <br />+  [DeleteDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteDataset.html) <br />+  [DeleteProject](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProject.html) <br />+  [DeleteProjectPolicy](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectPolicy.html) <br />+  [DeleteProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DeleteProjectVersion.html) <br />+  [DescribeDataset](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeDataset.html) <br />+  [DescribeProjects](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjects.html) <br />+  [DescribeProjectVersions](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DescribeProjectVersions.html) <br />+  [DistributeDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DistributeDatasetEntries.html) <br />+  [ListDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetEntries.html) <br />+  [ListDatasetLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListDatasetLabels.html) <br />+  [ListProjectPolicies](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListProjectPolicies.html) <br />+  [PutProjectPolicy](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_PutProjectPolicy.html) <br />+  [StartProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartProjectVersion.html) <br />+  [StopProjectVersion](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StopProjectVersion.html) <br />+  [UpdateDatasetEntries](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_UpdateDatasetEntries.html)  | In each Region that Amazon Rekognition Custom Labels supports – 5 | 
| Maximum number of Amazon Rekognition Custom Labels projects per account. | 100 | 
| Maximum number of Amazon Rekognition Custom Labels models per project. | 100 | 
| Maximum number of concurrent Amazon Rekognition Custom Labels training jobs per account. |  +  All Regions except Asia Pacific (Sydney) – 2 <br />+  Asia Pacific (Sydney) – 1   | 
| Maximum number of concurrently running Amazon Rekognition Custom Labels models per account. | 2 | 
| Maximum inference units per started model. | 5 | 
| Maximum number of images per dataset. | 250,000 | 

For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html) in the *Amazon Rekognition Developer Guide*.