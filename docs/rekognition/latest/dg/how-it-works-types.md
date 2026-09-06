

# Understanding Rekognition's types of analysis
<a name="how-it-works-types"></a>

The following are the types of analysis that the Amazon Rekognition Image API and Amazon Rekognition Video API can perform. For information about the APIs, see [Understanding Rekognition's image and video operations](how-it-works-operations-intro.md).

The following table lists the operations you need to use with respect to the type of media you're working with and your use case:



| Use Case | Media Type | Operations | 
| --- | --- | --- | 
|  [Moderating content](moderation.md)  | Images |  [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html), [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html), [GetMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetMediaAnalysisJob.html), [ListMediaAnalysisJobs](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListMediaAnalysisJobs.html)  | 
|  | Stored video | [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html), [GetContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetContentModeration.html)  | 
| Identity verification | [Images](collections.md) | [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html), [CreateUser](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html), [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html), [AssociateFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html), [SearchFacesByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchFacesByImage.html), [SearchUsersByImage](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsersByImage.html) | 
|  | [Stored video](procedure-person-search-videos.md) | [CreateCollection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateCollection.html), [IndexFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_IndexFaces.html), [StartFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceSearch.html), [GetFaceSearch](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceSearch.html) | 
|  | Streaming video ([Detecting face liveness](face-liveness.md)) |  [CreateFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateFaceLivenessSession.html), [StartFaceLivenessSession](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceLivenessSession.html), [GetFaceLivenessSessionResults](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceLivenessSessionResults.html),  | 
| [Facial analysis](faces.md) | Images | [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html), [CompareFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CompareFaces.html) | 
|  | Stored video | [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html), [GetFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetFaceDetection.html) | 
|  | Streaming video | [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html), [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html) | 
| [Object and activity recognition](labels.md) | Images | [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) | 
|  | Stored videos | [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html), [GetLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetLabelDetection.html) | 
| [Connected Home](https://github.com/aws-samples/rekognition-streaming-video-events) | Streaming Video | [StartStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartStreamProcessor.html) | 
| [Media Analysis](segments.md) | Stored video | [StartSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartSegmentDetection.html), [GetSegmentDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetSegmentDetection.html) | 
| [Workplace safety](ppe-detection.md) | Images | [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html) | 
| [Text detection](text-detection.md) | Images | [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html) | 
|  | Video | [StartTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartTextDetection.html), [GetTextDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetTextDetection.html) | 
| [People pathing](persons.md) | Video | [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html), [GetPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetPersonTracking.html) | 
| [Celebrity recognition](celebrities.md) | Images | [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html) | 
|  | Video | [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html), [GetCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_GetCelebrityRecognition.html) | 
| [Custom label detection](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html) | Images | [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html) | 
|  | Model training | [See Custom Labels developer guide](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html) | 

## Labels
<a name="how-it-works-labels-intro"></a>

A *label* refers to any of the following: objects (for example, flower, tree, or table), events (for example, a wedding, graduation, or birthday party), concepts (for example, a landscape, evening, and nature) or activities (for example, running or playing basketball). Amazon Rekognition can detect labels in images and videos. For more information, see [Detecting objects and concepts](labels.md).

Rekognition can detect a large list of labels in image and stored video. Rekognition can also detect a small number of labels in streaming video.

Use the following operations to detect labels based on your use case:
+ To detect labels in images: Use [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html). You can identify image properties like dominant image colors and image quality. To achieve this, use [DetectLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectLabels.html) with `IMAGE_PROPERTIES` as input parameter.
+ To detect labels in stored videos: Use [StartLabelDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartLabelDetection.html). Detection of dominant image colors and image quality is not supported for stored video.
+ To detect labels in streaming video: Use [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html). Detection of dominant image colors and image quality is not supported for streaming video.

You can specify what types of labels you want returned for both image and stored video label detection by using inclusive and exclusive filtering options.

## Custom labels
<a name="how-it-works-custom-labels-intro"></a>

Amazon Rekognition Custom Labels can identify the objects and scenes in images that are specific to your business needs by training a machine learning model. For example, you can train a model to detect logos or detect engineering machine parts on an assembly line.

**Note**  
For information about Amazon Rekognition Custom Labels, see the [Amazon Rekognition Custom Labels Developer Guide](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html).

Amazon Rekognition provides a console that you use to create, train, evaluate, and run a machine learning model. For more information, see [Getting Started with Amazon Rekognition Custom Labels](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-introduction.html) in the *Amazon Rekognition Custom Labels Develope Guide*. You can also use the Amazon Rekognition Custom Labels API to train and run a model. For more information, see [Getting Started with the Amazon Rekognition Custom Labels SDK](https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/gs-cli.html) in the *Amazon Rekognition CustomLabels Developer Guide*.

To analyze images using a trained model, use [DetectCustomLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectCustomLabels.html).

## Face Liveness Detection
<a name="face-liveness-detection"></a>

Amazon Rekognition Face Liveness can help you verify that a user going through face-based identity verification is physically present in front of the camera and isn’t a bad actor spoofing the user's face. It detects spoof attacks that are presented to a camera and attacks that bypass a camera. A user can complete a Face Liveness check by taking a short video selfie, and a Liveness score is returned for the check. Face Liveness is determined with a probabilistic calculation and a confidence score (between 0–100) is returned after the check. The higher the score, the greater the confidence that the person taking the check is live. 

For more information regarding Face Liveness, see [Detecting face liveness](face-liveness.md).

## Facial detection and analysis
<a name="how-it-works-faces-intro"></a>

Amazon Rekognition can detect faces in images and stored videos. With Amazon Rekognition, you can get information about:
+ Where faces are detected in an image or video
+ Facial landmarks such as the position of eyes
+ The presence of facial occlusion in images
+ Detected emotions, such as happy or sad
+ Eye gaze direction of a person’s gaze in images

You can also interpret and demographic information such as gender or age. You can compare a face in an image with faces detected in another image. Information about faces can also be stored for later retrieval. For more information, see [Detecting and analyzing faces](faces.md).

To detect faces in images, use [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html). To detect faces in stored videos, use [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html).

## Face search
<a name="how-it-works-search-faces-intro"></a>

Amazon Rekognition can search for faces. Facial information is indexed into a container known as a collection. Face information in the collection can then be matched with faces detected in images, stored videos, and streaming video. For more information, [Searching faces in a collection](collections.md).

To search for known faces in images, use [DetectFaces](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectFaces.html). To search for known faces in stored videos, use [StartFaceDetection](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartFaceDetection.html). To search for known faces in streaming videos, use [CreateStreamProcessor](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateStreamProcessor.html).

## People paths
<a name="how-it-works-persons-intro"></a>

Amazon Rekognition can track the paths of people detected in a stored video. Amazon Rekognition Video provides path tracking, face details, and in-frame location information for people detected in a video. For more information, see [People pathing](persons.md). 

To detect people in stored videos, use [StartPersonTracking](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartPersonTracking.html).

## Personal Protective Equipment
<a name="how-it-works-ppe-intro"></a>

 Amazon Rekognition can detect Personal Protective Equipment (PPE) worn by persons detected in an image. Amazon Rekognition detects face covers, hand covers, and head covers. Amazon Rekognition predicts if an item of PPE covers the appropriate body part. You can also get bounding boxes for detected persons and PPE items. For more information, see [Detecting personal protective equipment](ppe-detection.md). 

To detect PPE in images, use [DetectProtectiveEquipment](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectProtectiveEquipment.html).

## Celebrities
<a name="how-it-works-celebrities-intro"></a>

 Amazon Rekognition can recognize thousands of celebrities in images and stored videos. You can get information about where a celebrity's face is located on an image, facial landmarks, and the pose of a celebrity's face. You can get tracking information for celebrities as they appear throughout a stored video. You can also get further information about a recognized celebrity, like the emotion expressed, and presentation of gender. For more information, see [Recognizing celebrities](celebrities.md). 

To recognize celebrities in images, use [RecognizeCelebrities](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_RecognizeCelebrities.html). To recognize celebrities in stored videos, use [StartCelebrityRecognition](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartCelebrityRecognition.html).

## Text detection
<a name="how-it-works-text-intro"></a>

Amazon Rekognition Text in Image can detect text in images and convert it into machine-readable text. For more information, see [Detecting text](text-detection.md).

To detect text in images, use [DetectText](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectText.html).

## Inappropriate or offensive content
<a name="how-it-works-moderation-intro"></a>

Amazon Rekognition can analyze images and stored videos for adult and violent content. For more information, see [Moderating content](moderation.md).

To detect unsafe images, use [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html). To detect unsafe stored videos, use [StartContentModeration](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartContentModeration.html).

## Customization
<a name="how-it-works-customization"></a>

Certain image analysis APIs offered by Rekognition allow you to enhance the accuracy of deep learning models by creating custom adapters trained on your own data. Adapters are components that plug-in to Rekognition's pre-trained deep learning model, enhancing it’s accuracy with domain knowledge based on your images. You train an adapter to meet your needs by providing and annotating sample images. 

After you create an adapter, you’re provided with an AdapterId. You can provide this AdapterId to an operation to specify that you want to use the adapter you’ve created. For example, you provide the AdapterId to the [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html) API for synchronous image analysis. Providing the AdapterId as part of the request and Rekognition will automatically use it to enhance predictions for your images. This allows you to leverage the capabilities of Rekognition while customizing it to fit your needs. 

You also have the option to obtain predictions for images in bulk with the [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html) API. See [Bulk analysis](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html) for more information.

You can assess the accuracy of Rekognition’s operations by uploading images to the Rekognition console and running analysis on these images. Rekognition will annotate your images using the selected feature, and you can then review the predictions, using the verified predictions to determine which labels would benefit from creating an adapter.

Currently you can use adapters with the [DetectModerationLabels](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DetectModerationLabels.html). For more information on creating and using adapters, see [Enhancing accuracy with Custom Moderation](moderation-custom-moderation.md).

## Bulk analysis
<a name="how-it-works-bulk"></a>

Rekognition Bulk Analysis lets you process a large collection of images asynchronously by using a manifest file along with the [StartMediaAnalysisJob](https://docs.aws.amazon.com/rekognition/latest/APIReference/API_StartMediaAnalysisJob.html) operation. See [Bulk analysis](https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis.html) for more information.