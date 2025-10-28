# TwelveLabs models

This section describes the request parameters and response fields for TwelveLabs models. Use this information
to make inference calls to TwelveLabs models. The TwelveLabs Pegasus 1.2 model supports [InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") and [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md") (streaming) operations, while the TwelveLabs Marengo Embed 2.7 model supports [StartAsyncInvoke](../APIReference/API_runtime_StartAsyncInvoke.md "../APIReference/API_runtime_StartAsyncInvoke.md") operations.
This section also includes code examples that show how to call TwelveLabs models. To use a model in an inference operation, you need the model ID for the model.
To get the model ID, see [Supported foundation models in Amazon Bedrock](models-supported.md "models-supported.md").

TwelveLabs is a leading provider of multimodal AI models specializing in video understanding and analysis. Their advanced models enable sophisticated video search, analysis, and content generation capabilities through state-of-the-art computer vision and natural language processing technologies. Amazon Bedrock now offers two TwelveLabs models: TwelveLabs Pegasus 1.2, which provides comprehensive video understanding and analysis, and TwelveLabs Marengo Embed 2.7, which generates high-quality embeddings for video, text, audio, and image content. These models empower developers to build applications that can intelligently process, analyze, and derive insights from video data at scale.

**TwelveLabs Pegasus 1.2**

A multimodal model that provides comprehensive video understanding and analysis capabilities, including content recognition, scene detection, and contextual understanding. The model can analyze video content and generate textual descriptions, insights, and answers to questions about the video.

**TwelveLabs Marengo Embed 2.7**

A multimodal embedding model that generates high-quality vector representations of video, text, audio, and image content for similarity search, clustering, and other machine learning tasks. The model supports multiple input modalities and provides specialized embeddings optimized for different use cases.

###### Topics

- [TwelveLabs Pegasus 1.2](model-parameters-pegasus.md "model-parameters-pegasus.md")
- [TwelveLabs Marengo Embed 2.7](model-parameters-marengo.md "model-parameters-marengo.md")
