# Request and response structure for image

generation

###### Image generation

The following examples present different image generation use cases. Each example provides
an explanation of the fields that are used for the image generation.

Text-to-image request

```
`{
 "taskType": "TEXT_IMAGE",
 "textToImageParams": {
 "text": `string`,
 "negativeText": `string`,
 "style": "3D_ANIMATED_FAMILY_FILM" |
 "DESIGN_SKETCH" | "FLAT_VECTOR_ILLUSTRATION" |
 "GRAPHIC_NOVEL_ILLUSTRATION" | "MAXIMALISM" |
 "MIDCENTURY_RETRO" | "PHOTOREALISM" |
 "SOFT_DIGITAL_PAINTING"
 },
 "imageGenerationConfig": {
 "width": `int`,
 "height": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`,
 "numberOfImages": `int`
 }
}`

```

The following `textToImageParams` fields are used in this request:

- `text` (Required) – A text prompt to generate the image. The prompt
  must be 1-1024 characters in length.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.
- `style` (Optional) – Specifies the style that is used to generate this image. For more information, see [Visual Styles](image-gen-styles.md "image-gen-styles.md").

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

Text-to-image request with image conditioning

```
`{
 "taskType": "TEXT_IMAGE",
 "textToImageParams": {
 "conditionImage": `string` (Base64 encoded image),
 "controlMode": "CANNY_EDGE" | "SEGMENTATION",
 "controlStrength": `float`,
 "text": `string`,
 "negativeText": `string`,
 "style": "3D_ANIMATED_FAMILY_FILM" |
 "DESIGN_SKETCH" | "FLAT_VECTOR_ILLUSTRATION" |
 "GRAPHIC_NOVEL_ILLUSTRATION" | "MAXIMALISM" |
 "MIDCENTURY_RETRO" | "PHOTOREALISM" |
 "SOFT_DIGITAL_PAINTING"
 },
 "imageGenerationConfig": {
 "width": `int`,
 "height": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`,
 "numberOfImages": `int`
 }
}`

```

The following `textToImageParams` fields are used in this request:

- `conditionImage` (Required) – A JPEG or PNG image that guides the
  layout and composition of the generated image. The image must be formatted as a Base64
  string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.
- `controlMode` (Optional) – Specifies what conditioning mode is be used.
  The default value is "CANNY_EDGE".
  - `CANNY_EDGE` – Elements of the generated image will follow the
    prominent contours, or "edges", of the condition image closely.
  - `SEGMENTATION` – The condition image will be automatically analyzed
    to identify prominent content shapes. This analysis results in a segmentation mask
    which guides the generation, resulting in a generated image that closely follows
    the layout of the condition image but allows the model more freedom within the
    bounds of each content area.

- `controlStrength` (Optional) – Specifies how similar the layout and
  composition of the generated image should be to the `conditionImage`. The
  range is 0 to 1.0, and lower values introduce more randomness. The default value is
  0.7.
- `text` (Required) – A text prompt to generate the image. The prompt
  must be 1-1024 characters in length.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.
- `style` (Optional) – Specifies the style that is used to generate this image. For more information, see [Visual Styles](image-gen-styles.md "image-gen-styles.md").

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

Color guided image generation request

```
`{
 "taskType": "COLOR_GUIDED_GENERATION",
 "colorGuidedGenerationParams": {
 "colors": `string[]` (list of hexadecimal color values),
 "referenceImage": `string` (Base64 encoded image),
 "text": `string`,
 "negativeText": `string`
 },
 "imageGenerationConfig": {
 "width": `int`,
 "height": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`,
 "numberOfImages": `int`
 }
}`

```

The following `colorGuidedGenerationParams` fields are used in this
request:

- `colors` (Required) – A list of up to 10 color codes that define the
  desired color palette for your image. Expressed as hexadecimal values in the form
  “#RRGGBB”. For example, "#00FF00" is pure green and "#FCF2AB" is a warm yellow. The
  `colors` list has the strongest effect when a `referenceImage`
  is not provided. Otherwise, the colors in the list and the colors from the reference
  image will both be used in the final output.
- `referenceImage` (Optional) – A JPEG or PNG image to use as a subject
  and style reference. The colors of the image will also be incorporated into you final
  output, along with the colors in from the `colors` list. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for
  additional requirements.
- `text` (Required) – A text prompt to generate the image. The prompt
  must be 1-1024 characters in length.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

Image variation request

```
`{
 "taskType": "IMAGE_VARIATION",
 "imageVariationParams": {
 "images": `string[]` (list of Base64 encoded images),
 "similarityStrength": `float`,
 "text": `string`,
 "negativeText": `string`
 },
 "imageGenerationConfig": {
 "height": `int`,
 "width": `int`,
 "cfgScale": `float`,
 "seed": `int`,
 "numberOfImages": `int`
 }
}`

```

The following `imageVariationParams` fields are used in this
request:

- `images` (Required) - A list of 1–5 images to use as references. Each
  must be in JPEG or PNG format and encoded as Base64 strings. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for
  additional requirements.
- `similarityStrength` (Optional) – Specifies how similar the generated
  image should be to the input images. Valid values are betweeen 0.2-1.0 with lower
  values used to introduce more randomness.
- `text` (Required) – A text prompt to generate the image. The prompt
  must be 1-1024 characters in length. If you omit this field, the model will remove
  elements inside the masked area. They will be replaced with a seamless extension of
  the image background.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

###### Image editing

The following examples present different image editing use cases. Each example provides
an explanation of the fields that are used to edit the image.

Inpainting request

```
`{
 "taskType": "INPAINTING",
 "inPaintingParams": {
 "image": `string` (Base64 encoded image),
 "maskPrompt": `string`,
 "maskImage": `string` (Base64 encoded image),
 "text": `string`,
 "negativeText": `string`
 },
 "imageGenerationConfig": {
 "numberOfImages": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`
 }
}`

```

The following `inPaintingParams` fields are used in this request:

- `image` (Required) - The JPEG or PNG that you want to modify, formatted
  as a Base64 string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.
- `maskPrompt` or `maskImage` (Required) – You must specify
  either the `maskPrompt` or the `maskImage` parameter, but not
  both.

The `maskPrompt` is a natural language text prompt that describes the
regions of the image to edit.

The `maskImage` is an image that defines the areas of the image to
edit. The mask image must be the same size as the input image. Areas to be edited are
shaded pure black and areas to ignore are shaded pure white. No other colors are
allowed in the mask image.

Note that inpainting and outpainting requests are opposites in regard to the color requirements of the mask images.

- `text` (Required) – A text prompt that describes what to generate
  within the masked region. The prompt must be 1-1024 characters in length. If you omit
  this field, the model will remove elements inside the masked area. They will be
  replaced with a seamless extension of the image background.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

Outpainting request

```
`{
 "taskType": "OUTPAINTING",
 "outPaintingParams": {
 "image": `string` (Base64 encoded image),
 "maskPrompt": `string`,
 "maskImage": `string` (Base64 encoded image),
 "outPaintingMode": "DEFAULT" | "PRECISE",
 "text": `string`,
 "negativeText": `string`
 },
 "imageGenerationConfig": {
 "numberOfImages": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`
 }
}`

```

The following `outPaintingParams` fields are used in this request:

- `image` (Required) - The JPEG or PNG that you want to modify, formatted
  as a Base64 string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.
- `maskPrompt` or `maskImage` (Required) – You must specify
  either the `maskPrompt` or the `maskImage` parameter, but not
  both.

The `maskPrompt` is a natural language text prompt that describes the
regions of the image to edit.

The `maskImage` is an image that defines the areas of the image to
edit. The mask image must be the same size as the input image. Areas to be edited are
shaded pure black and areas to ignore are shaded pure white. No other colors are
allowed in the mask image.

Note that inpainting and outpainting requests are opposites in regard to the color requirements of the mask images.

- `outPaintingMode` - Determines how the mask that you provide is
  interpreted.

Use `DEFAULT` to transition smoothly between the masked area and the
non-masked area. Some of the original pixels are used as the starting point for the
new background. This mode is generally better when you want the new background to use
similar colors as the original background. However, you can get a halo effect if your
prompt calls for a new background that is significantly different than the original
background.

Use `PRECISE` to strictly adhere to the mask boundaries. This mode is
generally better when you are making significant changes to the background.

- `text` (Required) – A text prompt that describes what to generate
  within the masked region. The prompt must be 1-1024 characters in length. If you omit
  this field, the model will remove elements inside the masked area. They will be
  replaced with a seamless extension of the image background.
- `negativeText` (Optional) – A text prompt to define what not to include
  in the image. This value must be 1-1024 characters in length.

###### Note

Avoid using negating words (“no”, “not”, “without”, etc.) in your `text` and
`negativeText` values. For example, if you do not want mirrors in an image,
instead of including "no mirrors" or "without mirrors" in the `text` field, use the
word "mirrors" in the `negativeText` field.

Background removal request

```
`{
 "taskType": "BACKGROUND_REMOVAL",
 "backgroundRemovalParams": {
 "image": `string` (Base64 encoded image)
 }
}`

```

The following `backgroundRemovalParams` field is used in this
request:

- `image` (Required) – The JPEG or PNG that you want to modify, formatted
  as a Base64 string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.

The `BACKGROUND_REMOVAL` task will return a PNG image with full 8-bit
transparency. This format gives you smooth, clean isolation of the foreground objects and
makes it easy to composite the image with other elements in an image editing app,
presentation, or website. The background can easily be changed to a solid color using
simple custom code.

Virtual try-on

```
`{
 "taskType": "VIRTUAL_TRY_ON",
 "virtualTryOnParams": {
 "sourceImage": `string` (Base64 encoded image),
 "referenceImage": `string` (Base64 encoded image),
 "maskType": "IMAGE" | "GARMENT" | "PROMPT",
 "imageBasedMask":{
 "maskImage": `string` (Base64 encoded image),
 },
 "garmentBasedMask":{
 "maskShape": "CONTOUR" | "BOUNDING_BOX" | "DEFAULT",
 "garmentClass": "UPPER_BODY" | "LOWER_BODY" |
 "FULL_BODY" | "FOOTWEAR" | "LONG_SLEEVE_SHIRT" |
 "SHORT_SLEEVE_SHIRT" | "NO_SLEEVE_SHIRT" |
 "OTHER_UPPER_BODY" | "LONG_PANTS" | "SHORT_PANTS" |
 "OTHER_LOWER_BODY" | "LONG_DRESS" | "SHORT_DRESS" |
 "FULL_BODY_OUTFIT" | "OTHER_FULL_BODY" | "SHOES" |
 "BOOTS" | "OTHER_FOOTWEAR",
 "garmentStyling":{
 "longSleeveStyle": "SLEEVE_DOWN" | "SLEEVE_UP",
 "tuckingStyle": "UNTUCKED" | "TUCKED",
 "outerLayerStyle": "CLOSED" | "OPEN",
 }
 },
 "promptBasedMask":{
 "maskShape": "BOUNDING_BOX" | "CONTOUR" | "DEFAULT",
 "maskPrompt": `string`,
 },
 "maskExclusions": {
 "preserveBodyPose": "ON" | "OFF" | "DEFAULT",
 "preserveHands": "ON" | "OFF" | "DEFAULT",
 "preserveFace": "OFF" | "ON" | "DEFAULT"
 },
 "mergeStyle" : "BALANCED" | "SEAMLESS" | "DETAILED" ,
 "returnMask": boolean,
 },
 "imageGenerationConfig": {
 "numberOfImages": `int`,
 "quality": "standard" | "premium",
 "cfgScale": `float`,
 "seed": `int`
 }
}`
```

The following `virtualTryOnParams` fields are used in this
request:

- `sourceImage` (Required) – The JPEG or PNG that you want to modify, formatted
  as a Base64 string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.
- `referenceImage` (Required) – The JPEG or PNG that contains the object that you want to superimpose onto the source image, formatted
  as a Base64 string. See [Input images for image generation](image-gen-access.md#image-gen-input-images "image-gen-access.md#image-gen-input-images") for additional requirements.
- `maskType` (Required) – Specifies whether the mask is provided as an image, prompt, or garment mask.
- `imageBasedMask` – Required when `maskType` is `"IMAGE"`.

The `maskImage` is an image that defines the areas of the image to
edit. The mask image must be the same size as the input image. Areas to be edited are
shaded pure black and areas to ignore are shaded pure white. No other colors are
allowed in the mask image.

- `garmentBasedMask` – Required when `maskType` is `"GARMENT"`.
  - `maskShape` (Optional) – Defines the shape of the mask bounding box. The shape and size of the bounding box can have an affect on how the reference image is transferred to the source image.
  - `garmentClass` (Required) – Defines the article of clothing that is being transferred. This parameter allows the model focus on specific parts of the reference image that you want to transfer.
  - `garmentStyling` (Optional) – Provides styling cues to the model for certain articles of clothing. The `longSleeveStyle` and `tuckingStyle` parameters apply only to upper body garments. The `outerLayerStyle` parameter applies only to outer layer, upper body garments.

- `promptBasedMask` (Required) – Required when `maskType` is `"PROMPT"`.
  - `maskShape` (Optional) – Defines the shape of the mask bounding box. The shape and size of the bounding box can have an affect on how the reference image is transferred to source image.
  - `maskPrompt` (Required) – A natural language text prompt that describes the
    regions of the image to edit.

- `maskExclusions` (Optional) – When a person is detected in the source image, these parameters determine whether their body pose, hands, and face should be kept in the output image or regenerated.
- `mergeStyle` (Optional) – Determines how the source and reference images are stitched together. Each merge style takes a different approach to how it stitches the elements together to create the final image, each with its own benefits and tradeoffs.
  - `"BALANCED"` - Protects any non-masked pixels in the original image, ensuring they remain 100% accurate to the original. In some cases, there will be a slight perceptible color or texture mismatch in the output image that presents as a kind of “ghost” image of the mask shape. This is most likely to occur when the image features a person standing against a solid color or uniformly textured background. To avoid this, you can use the `"SEAMLESS"` merge style instead.
  - `"SEAMLESS"` - Ensures that there will never be a noticeable seam between the masked and non-masked images areas in the final image. The tradeoff is that this mode results in all pixels in the image changing slightly and can sometimes diminish fine-grained details in the non-masked areas of the image.
  - `"DETAILED"` - Can greatly improve fine-grained details like logos and text, especially when the masked area is relatively small compared to the overall image. The model achieves this by performing inpainting on a tightly cropped, higher resolution version of the original image that only includes the masked area. It then merges the result back into the original image. As with using `"BALANCED"` mode, this mode can sometimes result in a visible seam.

- `returnMask` (Optional) – Specifies whether the mask image is returned with the output image.

###### Response body

The response body will contain one or more of the following fields:

```
{
    "images": "images": string[] (list of Base64 encoded images),
    "maskImage": string (Base64 encoded image),
    "error": string
}

```

- `images` – When successful, a list of Base64-encoded strings that represent each
  image that was generated is returned. This list does not always contain the same
  number of images that you requested. Individual images might be blocked after
  generation if they do not align with the AWS Responsible AI (RAI) content moderation
  policy. Only images that align with the RAI policy are returned.
- `maskImage` - When you specified that the mask image should be returned with the output, this is where it is returned.
- `error` – If any image does not align with the RAI policy, this field is returned.
  Otherwise, this field is omitted from the response.
  The `imageGenerationConfig` field is common to all task types except
  `BACKGROUND_REMOVAL`. It is optional and contains the following fields. If you omit
  this object, the default configurations are used.

- `width` and `height` (Optional) – Define the size and aspect ratio
  of the generated image. Both default to 1024.

The `width` and `height` values should not be provided for the `"INPAINTING"`, `"OUTPAINTING"`, or `"VIRTUAL_TRY_ON"` task types.

For the full list of supported resolutions,
see [Supported image resolutions](image-gen-access.md#image-gen-resolutions "image-gen-access.md#image-gen-resolutions").

- `quality` (Optional) - Specifies the quality to use when generating the image

* "standard" (default) or "premium".

- `cfgScale` (Optional) – Specifies how strictly the model should
  adhere to the prompt. Values range from 1.1-10, inclusive, and the default value is 6.5.
  - Low values (1.1-3) - More creative freedom for the AI, potentially more aesthetic, but low contrast and less prompt-adherent results
  - Medium values (4-7) - Balanced approach, typically recommended for most generations
  - High values (8-10) - Strict prompt adherence, which can produce more precise results but sometimes at the cost of natural aesthetics and increased color saturation

- `numberOfImages` (Optional) – The number of images to generate.

| Minimum | Maximum       | Default |
| ------- | ------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1       | 5             | 1       | <br>• `seed` (Optional) – Determines the initial noise setting for the generation process. Changing the seed value while leaving all other parameters the same will produce a totally new image that still adheres to your prompt, dimensions, and other settings. It is common to experiment with a variety of seed values to find the perfect image.                                                                                                                   |
| Minimum | Maximum       | Default |
| ---     | ---           | ---     |
| 0       | 2,147,483,646 | 12      | ###### Important Resolution (`width` and `height`), `numberOfImages`, and `quality` all have an impact on the time it takes for generation to complete. The AWS SDK has a default `read_timeout` of 60 seconds which can easily be exceeded when using higher values for these parameters. Therefore, it is recommended that you increase the `read_timeout` of your invocation calls to at least 5 minutes (300 seconds). The code examples demonstrate how to do this. |
