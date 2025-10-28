# Configure video generation

To configure video generation, you choose a model to use and set optionally
settings that influence the output of the model. Currently Amazon Bedrock in SageMaker Unified Studio supports
video generation with Amazon Nova models. If you don't make any
configuration changes, the playground uses the default values for the model.

## Amazon Nova model settings

With Amazon Nova models, you can set the following configurations:

- **Start image** – (Optional) A
  reference image that model uses as a starting point for the video. The image
  dimensions must be 1280x720 pixels. If you supply an image with
  different dimensions, the playground resizes the image to 1280x720
  pixels.
- **Seed** – (Optional) Initializes the random
  number generator used in the video generation process. Higher seed values
  don't correlate with any particular quality or characteristic in the output.
  Instead, use different seed values options to explore differing variations
  of output, either with or without the same prompt. Repeatedly using the same
  seed value and prompt creates the exact same video.

For more information, see the [Amazon Nova
guide](../../../nova/latest/userguide.md "../../../nova/latest/userguide.md").
