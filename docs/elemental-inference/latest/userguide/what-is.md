

# What Is Elemental Inference?
<a name="what-is"></a>

AWS Elemental Inference is a real-time service that lets you easily apply machine learning models to video, audio, and image content for automated analysis, classification, and insights generation. Features include smart crop, event clipping, smart subtitles, and contextual metadata. Smart subtitles uses automatic speech recognition (ASR) to generate TTML subtitles from audio in your source media. Contextual metadata uses AI to classify video content at the shot level and at the scene level. These classifications enable contextual ad targeting.

You can also add your own analysis to a feed by using a function, which runs a prompt that you write against an Amazon Bedrock model that you choose, or reshapes metadata that Elemental Inference has already produced. A function runs alongside the other features on a feed and publishes its result with their metadata. Elemental Inference invokes the model in your own AWS account. For more information, see [Using functions in Elemental Inference](functions.md).

To preview smart cropping on a recorded video without setting up a live feed, use the Elemental Inference playground. For more information, see [Using the Elemental Inference playground](playground.md).

**Topics**
+ [Accessing Elemental Inference](what-is-accessing.md)