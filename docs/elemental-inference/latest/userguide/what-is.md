

# What Is Elemental Inference?

AWS Elemental Inference is a real-time service that applies machine learning models to your video, audio, and image content. You can use Elemental Inference to analyze and classify your content, and to generate insights from it. Elemental Inference has the following features:
+ **Smart crop** – Identifies the regions of interest in your video frames.
+ **Event clipping** – Detects notable events in your content, so that you can extract them as clips.
+ **Smart subtitles** – Uses automatic speech recognition (ASR) to generate Timed Text Markup Language (TTML) subtitles from the audio in your source media.
+ **Contextual metadata** – Classifies your video content at the shot level and at the scene level. You can use these classifications to target ads to the content that a viewer is watching. For more information about contextual metadata, see [Querying contextual metadata](query-metadata-query.md#query-metadata-contextual).
+ **Customer decisions** – Makes your own yes-or-no and multiple-choice decisions about each shot or scene that contextual metadata analyzes. For more information, see [Customer decisions for contextual metadata in Elemental Inference](custom-questions.md).
+ **Functions** – Runs a prompt that you write against an Amazon Bedrock model that you choose, or reshapes the metadata that Elemental Inference has already produced. Elemental Inference invokes the model in your own AWS account and publishes the result with the metadata from the other features. For more information about functions, see [Using functions in Elemental Inference](functions.md).

To preview smart cropping on its own, or together with event clipping, smart subtitles, and contextual metadata, on a recorded video without setting up a live feed, use the Elemental Inference playground. For more information about the playground, see [Using the Elemental Inference playground](playground.md).

**Topics**
+ [Accessing Elemental Inference](what-is-accessing.md)