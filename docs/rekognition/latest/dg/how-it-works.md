# How Amazon Rekognition works

Amazon Rekognition provides two API sets for visual analysis:

- Amazon Rekognition Image for image analysis
- Amazon Rekognition Video for video analysis
  **Image analysis**

With Amazon Rekognition Image your applications can:

- Detect objects, scenes, and concepts in images
- Recognize celebrities
- Detect text in a variety of languages
- Detect explicit, inappropriate, or violent content or images
- Detect, analyze, and compare faces and facial attributes like age and
  emotions
- Detect the presence of PPE
  Use cases include enhancing photo apps, cataloging images, and moderating content.

**Video analysis**

With Amazon Rekognition Video, your applications can:

- Track people and objects across video frames
- Recognize objects
- Recognize celebrities
- Search stored and streaming video for persons of interest
- Analyze faces for attributes like age and emotions
- Detect explicit, inappropriate, or violent content or images
- Aggregate and sort analysis results by timestamps and segments
- Detect people, pets, and packages in streaming video
  Use cases include video analysis, cataloging videos, and filtering inappropriate
  content.

**Key features**

- Powerful deep learning analysis
- High accuracy detection for objects, scenes, faces, text
- Easy to use API for integrating into apps
- Customizable models tuned to your data
- Scalable analysis of media libraries
  Amazon Rekognition lets you enhance the accuracy of certain deep learning models by training a
  custom adapter. For example, with Amazon Rekognition Custom Moderation, you can adapt Amazon Rekognition ’s
  base image analysis model by training a custom adapter with your images. See [Enhancing accuracy with Custom Moderation](moderation-custom-moderation.md "moderation-custom-moderation.md") for more information.

The following sections cover the types of analysis that Amazon Rekognition provides and an overview
of Amazon Rekognition Image and Amazon Rekognition Video operations. Also covered is the difference between non-storage and
storage operations.

To demo the Amazon Rekognition APIs, you can see [Step
3: Getting started using the AWS CLI and AWS SDK API](get-started-exercise.md "get-started-exercise.md"), which covers trying out
Rekognition in the AWS console.

###### Topics

- [Understanding Rekognition's types of analysis](how-it-works-types.md "how-it-works-types.md")
- [Understanding Rekognition's image
  and video operations](how-it-works-operations-intro.md "how-it-works-operations-intro.md")
- [Understanding non-storage and storage
  API operations](how-it-works-storage-non-storage.md "how-it-works-storage-non-storage.md")
- [Understanding model versioning](face-detection-model.md "face-detection-model.md")
