# Working with images

This section covers the types of analysis that Amazon Rekognition Image can perform on images.

- [Object and scene detection](labels.md "labels.md")
- [Face detection and comparison](faces.md "faces.md")
- [Searching faces in a collection](collections.md "collections.md")
- [Celebrity recognition](celebrities.md "celebrities.md")
- [Image moderation](moderation.md "moderation.md")
- [Text in image detection](text-detection.md "text-detection.md")
  These are performed by non-storage API operations where Amazon Rekognition Image
  doesn't persist any information discovered by the operation. No input image bytes are persisted
  by non-storage API operations. For more information, see [Understanding non-storage and storage
  API operations](how-it-works-storage-non-storage.md "how-it-works-storage-non-storage.md").

Amazon Rekognition Image can also store facial metadata in collections for later retrieval. For more information, see
[Searching faces in a collection](collections.md "collections.md").

In this section, you use the Amazon Rekognition Image API operations to analyze images stored in an
Amazon S3 bucket and image bytes loaded from the local file system. This section also covers
getting image orientation information from a .jpg image.

Rekognition only uses RGB channels to perform inference. AWS recommends
users remove the Alpha Channel before using a Display to visually (manually by a human)
inspect the comparison.

###### Topics

- [Image specifications](images-information.md "images-information.md")
- [Analyzing images stored in an Amazon S3 bucket](images-s3.md "images-s3.md")
- [Analyzing an image loaded from a local file system](images-bytes.md "images-bytes.md")
- [Displaying bounding boxes](images-displaying-bounding-boxes.md "images-displaying-bounding-boxes.md")
- [Getting image orientation and bounding box
  coordinates](images-orientation.md "images-orientation.md")
