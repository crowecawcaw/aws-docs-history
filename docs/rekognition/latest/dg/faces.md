# Detecting and analyzing faces

Amazon Rekognition provides you with APIs you can use to detect and analyze faces in images and
videos. This section provides an overview of the non-storage operations for facial analysis.
These operations include functionalities like detecting facial landmarks, analyzing
emotions, and comparing faces.

Amazon Rekognition can identify facial landmarks (e.g., eye position), detect emotions (e.g.,
happiness or sadness), and other attributes (e.g., glasses presence, face occlusion). When a
face is detected, the system analyzes facial attributes and returns a confidence score for
each attribute.

![Smiling woman wearing sunglasses and driving a vintage yellow car on an open road.](/images/rekognition/latest/dg/images/sample-detect-faces.png)
This section contains examples for both image and video operations.

For more information about using the Rekognition’s image operations, see [Working with images](images.md "images.md").

For more information about using the Rekognition’s video operations, see [Working with stored video analysis operations](video.md "video.md").

Note that these operations are non-storage operations. You can use storage operations and
Face collections to save facial metadata for faces detected in an image. Later you can
search for stored faces in both images and videos. For example, this enables searching for a
specific person in a video. For more information, see [Searching faces in a collection](collections.md "collections.md").

For more information, see the Faces section of [Amazon Rekognition FAQs](https://aws.amazon.com/rekognition/faqs/ "https://aws.amazon.com/rekognition/faqs/").

###### Note

The face detection models used by Amazon Rekognition Image and Amazon Rekognition Video don't support the detection of
faces in cartoon/animated characters or non-human entities. If you want to detect
cartoon characters in images or videos, we recommend using Amazon Rekognition Custom Labels. For
more information, see the [Amazon Rekognition Custom Labels Developer Guide](../customlabels-dg/what-is.md "../customlabels-dg/what-is.md").

###### Topics

- [Overview of face detection and face
  comparison](face-feature-differences.md "face-feature-differences.md")
- [Guidelines on face attributes](guidance-face-attributes.md "guidance-face-attributes.md")
- [Detecting faces in an image](faces-detect-images.md "faces-detect-images.md")
- [Comparing faces in images](faces-comparefaces.md "faces-comparefaces.md")
- [Detecting faces in a stored video](faces-sqs-video.md "faces-sqs-video.md")
