# Generate an image with the Amazon Bedrock image and video playground

The image and video playground is an interactive environment that lets you
specify actions that generate and manipulate images using natural language
prompts, reference images, and suitable Amazon Bedrock models.

## Actions for generating images

Within the image playground, you use an _action_ to specify the image
generation task that you want the model to do, such as replacing the background of an existing
image. The actions that are available depends on the model you use.

- **Generate image** —
  [Generates a new
  image](bedrock-image-playground-generate-image.md "bedrock-image-playground-generate-image.md") from a
  prompt that you enter.
- **Generate variations** — Use a prompt to generate a
  [variation of an existing image](bedrock-image-playground-generate-variations.md "bedrock-image-playground-generate-variations.md").
- **Remove object** —
  [Removes an object](bedrock-image-playground-remove-object.md "bedrock-image-playground-remove-object.md") from an image you supply.
- **Replace background** —
  [Replaces the
  background](bedrock-image-playground-replace-background.md "bedrock-image-playground-replace-background.md") of an
  image with a new background.
- **Replace object** —
  [Replaces an
  object](bedrock-image-playground-replace-object.md "bedrock-image-playground-replace-object.md") in an image
  with a different object.
- **Edit image sandbox** — An [image sandbox](bedrock-image-playground-image-sandbox.md "bedrock-image-playground-image-sandbox.md") that
  you can use to expiriment with Stable Diffusion XL models.

Some actions, such as generate variation, require a reference image that a model uses
to generate a new image. An action might require you to use a mask tool to draw a
bounding box around an area of the reference image, such as when you define an object
that you want to remove with the remove object action.

## Configuration options

You can influence how a model generates an image by configuring the following options. The
configuration changes you can make depends on the action you choose.

### Negative prompt

A set of words or phrases that that tells the model what not to include in the image that it
generates. For example, you can use the term _-lowres_ to avoid generating
low-resolution or blurry images.

### Reference image

In certain actions, such as generate variations or replace background, you specify
a reference image that the model uses to process the action.

### Response image

You can specify the image dimensions, orientation, and number of
images to generate.

### Advanced configuration options

You can make advanced configuration changes that how the model generates images. All models
image generation models support the following:

- **Prompt strength** — Prompt strength is a numerical
  value that determines how strongly a model should adhere to the given text prompt. A higher
  prompt strength means the model will try to closely follow and prioritize the text description
  provided in the prompt when generating the image. Lower prompt strengths allow the model more
  creative freedom to deviate from the prompt.
- **Seed** — A seed is numeric value that a model uses
  to seed a random number generator. The model uses the seed as a starting point for creating random
  patterns during image generation. This initial randomness
  influences things like the exact positioning, colors, textures, and compositions present in the
  image that the model generates.
- **Similarity strength** — If you use
  the _Generate variations_ action with a Titan Image Generator G1 V1 or
  a Titan Image Generator G1 V2 model, you can also configure the _Similarity
  Strength_ advanced configuration. Similarity Strength
  specifies how similar the generated image should be to the input image. Use
  a lower value to introduce more randomness into the generated image.
- **Generate step** — If you use a
  Stable Diffusion XL model, you can configure the _Generate step_
  advanced configuration. Generate step determines how many times the image is
  sampled. More steps can result in a more accurate result.

###### Topics
