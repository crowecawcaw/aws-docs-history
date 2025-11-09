# Understanding Rekognition's types of analysis

The following are the types of analysis that the Amazon Rekognition Image API and Amazon Rekognition Video API can
perform. For information about the APIs, see [Understanding Rekognition's image
and video operations](how-it-works-operations-intro.md "how-it-works-operations-intro.md").

The following table lists the operations you need to use with respect to the type of
media you're working with and your use case:

| Use Case                                                                                                                                                | Media Type                                                                               | Operations                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Moderating content](moderation.md "moderation.md")                                                                                                     | Images                                                                                   | [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md"), [StartMediaAnalysisJob](../APIReference/API_StartMediaAnalysisJob.md "../APIReference/API_StartMediaAnalysisJob.md"), [GetMediaAnalysisJob](../APIReference/API_GetMediaAnalysisJob.md "../APIReference/API_GetMediaAnalysisJob.md"), [ListMediaAnalysisJobs](../APIReference/API_ListMediaAnalysisJobs.md "../APIReference/API_ListMediaAnalysisJobs.md")                                                                                                                        |
|                                                                                                                                                         | Stored video                                                                             | [StartContentModeration](../APIReference/API_StartContentModeration.md "../APIReference/API_StartContentModeration.md"), [GetContentModeration](../APIReference/API_GetContentModeration.md "../APIReference/API_GetContentModeration.md")                                                                                                                                                                                                                                                                                                                                                                 |
| Identity verification                                                                                                                                   | [Images](collections.md "collections.md")                                                | [CreateCollection](../APIReference/API_CreateCollection.md "../APIReference/API_CreateCollection.md"), [CreateUser](../APIReference/API_CreateUser.md "../APIReference/API_CreateUser.md"), [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md"), [AssociateFaces](../APIReference/API_AssociateFaces.md "../APIReference/API_AssociateFaces.md"), [SearchFacesByImage](../APIReference/API_SearchFacesByImage.md "../APIReference/API_SearchFacesByImage.md"), [SearchUsersByImage](../APIReference/API_SearchUsersByImage.md "../APIReference/API_SearchUsersByImage.md") |
|                                                                                                                                                         | [Stored<br>video](procedure-person-search-videos.md "procedure-person-search-videos.md") | [CreateCollection](../APIReference/API_CreateCollection.md "../APIReference/API_CreateCollection.md"), [IndexFaces](../APIReference/API_IndexFaces.md "../APIReference/API_IndexFaces.md"), [StartFaceSearch](../APIReference/API_StartFaceSearch.md "../APIReference/API_StartFaceSearch.md"), [GetFaceSearch](../APIReference/API_GetFaceSearch.md "../APIReference/API_GetFaceSearch.md")                                                                                                                                                                                                               |
|                                                                                                                                                         | Streaming video ([Detecting face liveness](face-liveness.md "face-liveness.md"))         | [CreateFaceLivenessSession](../APIReference/API_CreateFaceLivenessSession.md "../APIReference/API_CreateFaceLivenessSession.md"), [StartFaceLivenessSession](../APIReference/API_StartFaceLivenessSession.md "../APIReference/API_StartFaceLivenessSession.md"), [GetFaceLivenessSessionResults](../APIReference/API_GetFaceLivenessSessionResults.md "../APIReference/API_GetFaceLivenessSessionResults.md"),                                                                                                                                                                                             |
| [Facial analysis](faces.md "faces.md")                                                                                                                  | Images                                                                                   | [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md"), [CompareFaces](../APIReference/API_CompareFaces.md "../APIReference/API_CompareFaces.md")                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                         | Stored video                                                                             | [StartFaceDetection](../APIReference/API_StartFaceDetection.md "../APIReference/API_StartFaceDetection.md"), [GetFaceDetection](../APIReference/API_GetFaceDetection.md "../APIReference/API_GetFaceDetection.md")                                                                                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                         | Streaming video                                                                          | [CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md"), [StartStreamProcessor](../APIReference/API_StartStreamProcessor.md "../APIReference/API_StartStreamProcessor.md")                                                                                                                                                                                                                                                                                                                                                                    |
| [Object and activity recognition](labels.md "labels.md")                                                                                                | Images                                                                                   | [DetectLabels](../APIReference/API_DetectLabels.md "../APIReference/API_DetectLabels.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                                                                                                                                         | Stored videos                                                                            | [StartLabelDetection](../APIReference/API_StartLabelDetection.md "../APIReference/API_StartLabelDetection.md"), [GetLabelDetection](../APIReference/API_GetLabelDetection.md "../APIReference/API_GetLabelDetection.md")                                                                                                                                                                                                                                                                                                                                                                                   |
| [Connected Home](https://github.com/aws-samples/rekognition-streaming-video-events "https://github.com/aws-samples/rekognition-streaming-video-events") | Streaming Video                                                                          | [StartStreamProcessor](../APIReference/API_StartStreamProcessor.md "../APIReference/API_StartStreamProcessor.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Media Analysis](segments.md "segments.md")                                                                                                             | Stored video                                                                             | [StartSegmentDetection](../APIReference/API_StartSegmentDetection.md "../APIReference/API_StartSegmentDetection.md"), [GetSegmentDetection](../APIReference/API_GetSegmentDetection.md "../APIReference/API_GetSegmentDetection.md")                                                                                                                                                                                                                                                                                                                                                                       |
| [Workplace safety](ppe-detection.md "ppe-detection.md")                                                                                                 | Images                                                                                   | [DetectProtectiveEquipment](../APIReference/API_DetectProtectiveEquipment.md "../APIReference/API_DetectProtectiveEquipment.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [Text detection](text-detection.md "text-detection.md")                                                                                                 | Images                                                                                   | [DetectText](../APIReference/API_DetectText.md "../APIReference/API_DetectText.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                                                                                                                                                         | Video                                                                                    | [StartTextDetection](../APIReference/API_StartTextDetection.md "../APIReference/API_StartTextDetection.md"), [GetTextDetection](../APIReference/API_GetTextDetection.md "../APIReference/API_GetTextDetection.md")                                                                                                                                                                                                                                                                                                                                                                                         |
| [People pathing](persons.md "persons.md")                                                                                                               | Video                                                                                    | [StartPersonTracking](../APIReference/API_StartPersonTracking.md "../APIReference/API_StartPersonTracking.md"), [GetPersonTracking](../APIReference/API_GetPersonTracking.md "../APIReference/API_GetPersonTracking.md")                                                                                                                                                                                                                                                                                                                                                                                   |
| [Celebrity recognition](celebrities.md "celebrities.md")                                                                                                | Images                                                                                   | [RecognizeCelebrities](../APIReference/API_RecognizeCelebrities.md "../APIReference/API_RecognizeCelebrities.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                         | Video                                                                                    | [StartCelebrityRecognition](../APIReference/API_StartCelebrityRecognition.md "../APIReference/API_StartCelebrityRecognition.md"), [GetCelebrityRecognition](../APIReference/API_GetCelebrityRecognition.md "../APIReference/API_GetCelebrityRecognition.md")                                                                                                                                                                                                                                                                                                                                               |
| [Custom label detection](../customlabels-dg/what-is.md "../customlabels-dg/what-is.md")                                                                 | Images                                                                                   | [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                         | Model training                                                                           | [See Custom Labels developer guide](../customlabels-dg/what-is.md "../customlabels-dg/what-is.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Labels

A _label_ refers to any of the following: objects (for example,
flower, tree, or table), events (for example, a wedding, graduation, or birthday
party), concepts (for example, a landscape, evening, and nature) or activities (for
example, running or playing basketball). Amazon Rekognition can detect labels in images and
videos. For more information, see [Detecting objects and concepts](labels.md "labels.md").

Rekognition can detect a large list of labels in image and stored video. Rekognition can also
detect a small number of labels in streaming video.

Use the following operations to detect labels based on your use case:

- To detect labels in images: Use [DetectLabels](../APIReference/API_DetectLabels.md "../APIReference/API_DetectLabels.md"). You can identify image properties like dominant
  image colors and image quality. To achieve this, use [DetectLabels](../APIReference/API_DetectLabels.md "../APIReference/API_DetectLabels.md") with `IMAGE_PROPERTIES` as input
  parameter.
- To detect labels in stored videos: Use [StartLabelDetection](../APIReference/API_StartLabelDetection.md "../APIReference/API_StartLabelDetection.md"). Detection of dominant image colors and
  image quality is not supported for stored video.
- To detect labels in streaming video: Use [CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md"). Detection of dominant image colors and
  image quality is not supported for streaming video.

You can specify what types of labels you want returned for both image and stored
video label detection by using inclusive and exclusive filtering options.

## Custom labels

Amazon Rekognition Custom Labels can identify the objects and scenes in images that are
specific to your business needs by training a machine learning model. For example,
you can train a model to detect logos or detect engineering machine parts on an
assembly line.

###### Note

For information about Amazon Rekognition Custom Labels, see the [Amazon Rekognition Custom Labels Developer Guide](../customlabels-dg/what-is.md "../customlabels-dg/what-is.md").

Amazon Rekognition provides a console that you use to create, train, evaluate, and run a
machine learning model. For more information, see [Getting Started with Amazon Rekognition Custom Labels](../customlabels-dg/gs-introduction.md "../customlabels-dg/gs-introduction.md") in the
_Amazon Rekognition Custom Labels Develope Guide_. You can also use
the Amazon Rekognition Custom Labels API to train and run a model. For more information, see
[Getting Started with the Amazon Rekognition Custom Labels SDK](../customlabels-dg/gs-cli.md "../customlabels-dg/gs-cli.md") in the
_Amazon Rekognition CustomLabels Developer Guide_.

To analyze images using a trained model, use [DetectCustomLabels](../APIReference/API_DetectCustomLabels.md "../APIReference/API_DetectCustomLabels.md").

## Face Liveness Detection

Amazon Rekognition Face Liveness can help you verify that a user going through face-based
identity verification is physically present in front of the camera and isn’t a bad
actor spoofing the user's face. It detects spoof attacks that are presented to a
camera and attacks that bypass a camera. A user can complete a Face Liveness check
by taking a short video selfie, and a Liveness score is returned for the check. Face
Liveness is determined with a probabilistic calculation and a confidence score
(between 0–100) is returned after the check. The higher the score, the
greater the confidence that the person taking the check is live.

For more information regarding Face Liveness, see [Detecting face liveness](face-liveness.md "face-liveness.md").

## Facial detection and analysis

Amazon Rekognition can detect faces in images and stored videos. With Amazon Rekognition, you can
get information about:

- Where faces are detected in an image or video
- Facial landmarks such as the position of eyes
- The presence of facial occlusion in images
- Detected emotions, such as happy or sad
- Eye gaze direction of a person’s gaze in images

You can also interpret and demographic information such as gender or age. You can
compare a face in an image with faces detected in another image. Information about
faces can also be stored for later retrieval. For more information, see [Detecting and analyzing faces](faces.md "faces.md").

To detect faces in images, use [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md").
To detect faces in stored videos, use [StartFaceDetection](../APIReference/API_StartFaceDetection.md "../APIReference/API_StartFaceDetection.md").

## Face search

Amazon Rekognition can search for faces. Facial information is indexed into a container
known as a collection. Face information in the collection can then be matched with
faces detected in images, stored videos, and streaming video. For more information,
[Searching faces in a collection](collections.md "collections.md").

To search for known faces in images, use [DetectFaces](../APIReference/API_DetectFaces.md "../APIReference/API_DetectFaces.md").
To search for known faces in stored videos, use [StartFaceDetection](../APIReference/API_StartFaceDetection.md "../APIReference/API_StartFaceDetection.md"). To search for known faces in streaming videos, use
[CreateStreamProcessor](../APIReference/API_CreateStreamProcessor.md "../APIReference/API_CreateStreamProcessor.md").

## People paths

Amazon Rekognition can track the paths of people detected in a stored video. Amazon Rekognition Video
provides path tracking, face details, and in-frame location information for people
detected in a video. For more information, see [People pathing](persons.md "persons.md").

To detect people in stored videos, use [StartPersonTracking](../APIReference/API_StartPersonTracking.md "../APIReference/API_StartPersonTracking.md").

## Personal Protective Equipment

Amazon Rekognition can detect Personal Protective Equipment (PPE) worn by persons detected
in an image. Amazon Rekognition detects face covers, hand covers, and head covers. Amazon Rekognition
predicts if an item of PPE covers the appropriate body part. You can also get
bounding boxes for detected persons and PPE items. For more information, see [Detecting personal protective equipment](ppe-detection.md "ppe-detection.md").

To detect PPE in images, use [DetectProtectiveEquipment](../APIReference/API_DetectProtectiveEquipment.md "../APIReference/API_DetectProtectiveEquipment.md").

## Celebrities

Amazon Rekognition can recognize thousands of celebrities in images and stored videos. You
can get information about where a celebrity's face is located on an image, facial
landmarks, and the pose of a celebrity's face. You can get tracking information for
celebrities as they appear throughout a stored video. You can also get further
information about a recognized celebrity, like the emotion expressed, and
presentation of gender. For more information, see [Recognizing celebrities](celebrities.md "celebrities.md").

To recognize celebrities in images, use [RecognizeCelebrities](../APIReference/API_RecognizeCelebrities.md "../APIReference/API_RecognizeCelebrities.md"). To recognize celebrities in stored videos, use
[StartCelebrityRecognition](../APIReference/API_StartCelebrityRecognition.md "../APIReference/API_StartCelebrityRecognition.md").

## Text detection

Amazon Rekognition Text in Image can detect text in images and convert it into
machine-readable text. For more information, see [Detecting text](text-detection.md "text-detection.md").

To detect text in images, use [DetectText](../APIReference/API_DetectText.md "../APIReference/API_DetectText.md").

## Inappropriate or offensive content

Amazon Rekognition can analyze images and stored videos for adult and violent content. For
more information, see [Moderating content](moderation.md "moderation.md").

To detect unsafe images, use [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md"). To detect unsafe stored videos, use [StartContentModeration](../APIReference/API_StartContentModeration.md "../APIReference/API_StartContentModeration.md").

## Customization

Certain image analysis APIs offered by Rekognition allow you to enhance the accuracy of
deep learning models by creating custom adapters trained on your own data. Adapters
are components that plug-in to Rekognition's pre-trained deep learning model, enhancing
it’s accuracy with domain knowledge based on your images. You train an adapter to
meet your needs by providing and annotating sample images.

After you create an adapter, you’re provided with an AdapterId. You can provide
this AdapterId to an operation to specify that you want to use the adapter you’ve
created. For example, you provide the AdapterId to the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md") API for synchronous image analysis. Providing
the AdapterId as part of the request and Rekognition will automatically use it to enhance
predictions for your images. This allows you to leverage the capabilities of Rekognition
while customizing it to fit your needs.

You also have the option to obtain predictions for images in bulk with the [StartMediaAnalysisJob](../APIReference/API_StartMediaAnalysisJob.md "../APIReference/API_StartMediaAnalysisJob.md") API. See
[Bulk analysis](bulk-analysis.md "bulk-analysis.md") for more information.

You can assess the accuracy of Rekognition’s operations by uploading images to the
Rekognition console and running analysis on these images. Rekognition will annotate
your images using the selected feature, and you can then review the predictions,
using the verified predictions to determine which labels would benefit from creating
an adapter.

Currently you can use adapters with the [DetectModerationLabels](../APIReference/API_DetectModerationLabels.md "../APIReference/API_DetectModerationLabels.md"). For more information on creating and using
adapters, see [Enhancing accuracy with Custom
Moderation](moderation-custom-moderation.md "moderation-custom-moderation.md").

## Bulk analysis

Rekognition Bulk Analysis lets you process a large collection of images asynchronously
by using a manifest file along with the [StartMediaAnalysisJob](../APIReference/API_StartMediaAnalysisJob.md "../APIReference/API_StartMediaAnalysisJob.md") operation. See [Bulk analysis](bulk-analysis.md "bulk-analysis.md") for more
information.
