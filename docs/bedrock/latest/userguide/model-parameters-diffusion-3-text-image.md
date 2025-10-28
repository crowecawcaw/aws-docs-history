# Stability.ai Stable Diffusion 3

The Stable Diffusion 3 models and Stable Image Core model have the following inference parameters and
model responses for making inference calls.

## Stable Diffusion 3 Large request and response

The request body is passed in the `body` field of a request to
[InvokeModel](../APIReference/API_runtime_InvokeModel.md "../APIReference/API_runtime_InvokeModel.md") or [InvokeModelWithResponseStream](../APIReference/API_runtime_InvokeModelWithResponseStream.md "../APIReference/API_runtime_InvokeModelWithResponseStream.md").

**Model invocation request body field**

When you make an InvokeModel call using a Stable Diffusion 3 Large model, fill the
body field with a JSON object that looks like the below.

```
{
    'prompt': 'Create an image of a panda'
}
```

**Model invocation responses body field**

When you make an `InvokeModel` call using a Stable Diffusion 3 Large model, the response looks like the below

```
{
    'seeds': [2130420379],
    "finish_reasons":[null],
    "images":["..."]
}
```

A response with a finish reason that is not `null`, will look like the below:

```
{
    "finish_reasons":["Filter reason: prompt"]
}
```

- **seeds** – (string) List of seeds used to
  generate images for the model.
- **finish_reasons** – Enum indicating whether the
  request was filtered or not. `null` will indicate that the request was successful. Current possible values: `"Filter reason: prompt", "Filter reason: output image", "Filter reason: input image", "Inference error", null`.
- **images** – A list of generated images in base64 string format.

For more information,
see [https://platform.us.stability.ai/docs/api-reference#tag/v1generation](https://platform.us.stability.ai/docs/api-reference#tag/v1generation "https://platform.us.stability.ai/docs/api-reference#tag/v1generation").

Text to image
The Stability.ai Stable Diffusion 3 Large model has the following
inference parameters for a text-to-image inference call.

- **prompt** – (string)
  What you wish to see in the output image. A strong, descriptive prompt
  that clearly defines elements, colors, and subjects will lead to better
  results.

| Minimum | Maximum |
| ------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0       | 10,000  | **Optional fields** <br>• **aspect_ratio** – (string) Controls the aspect ratio of the generated image. This parameter is only valid for text-to-image requests. Default 1:1. Enum: 16:9, 1:1, 21:9, 2:3, 3:2, 4:5, 5:4, 9:16, 9:21. <br>• **mode** – Controls whether this is a text-to-image or image-to-image generation, which affects which parameters are required. Default: text-to-image. Enum: `image-to-image`, `text-to-image`. <br>• **output_format** – Specifies the format of the output image. Supported formats: JPEG, PNG. Supported dimensions: height 640 to 1,536 px, width 640 to 1,536 px. <br>• **seed** – (number) A specific value that is used to guide the 'randomness' of the generation. (Omit this parameter or pass 0 to use a random seed.) Range: 0 to 4294967295. <br>• **negative_prompt** – Keywords of what you do not wish to see in the output image. Max: 10.000 characters. `import boto3 import json import base64 import io from PIL import Image bedrock = boto3.client('bedrock-runtime', region_name='us-west-2') response = bedrock.invoke_model( modelId='us.stability.sd3-large-v1:0', body=json.dumps({ 'prompt': 'A car made out of vegetables.' }) ) output_body = json.loads(response["body"].read().decode("utf-8")) base64_output_image = output_body["images"][0] image_data = base64.b64decode(base64_output_image) image = Image.open(io.BytesIO(image_data)) image.save("image.png")` Image to image The Stability.ai Stable Diffusion 3 Large model has the following inference parameters for a image-to-image inference call. **text_prompts** (Required) – An array of text prompts to use for generation. Each element is a JSON object that contains a prompt and a weight for the prompt. <br>• **prompt** – (string) What you wish to see in the output image. A strong, descriptive prompt that clearly defines elements, colors, and subjects will lead to better results.                                                                                                                                                                                                                                                                                                                      |
| Minimum | Maximum |
| ---     | ---     |
| 0       | 10,000  | <br>• **image** – String in base64 format. The image to use as the starting point for the generation. Supported formats: JPEG, PNG, WEBP (WEBP not supported in console), Supported dimensions: Width: 640 - 1536 px, Height: 640 - 1536 px. <br>• **strength** – Numerical. Sometimes referred to as denoising, this parameter controls how much influence the image parameter has on the generated image. A value of 0 would yield an image that is identical to the input. A value of 1 would be as if you passed in no image at all. Range: [0, 1] <br>• **mode** – must be set to `image-to-image`. **Optional fields** <br>• **aspect_ratio** – (string) Controls the aspect ratio of the generated image. This parameter is only valid for text-to-image requests. Default 1:1. Enum: 16:9, 1:1, 21:9, 2:3, 3:2, 4:5, 5:4, 9:16, 9:21. <br>• **mode** – Controls whether this is a text-to-image or image-to-image generation, which affects which parameters are required. Default: text-to-image. Enum: `image-to-image`, `text-to-image`. <br>• **output_format** – Specifies the format of the output image. Supported formats: JPEG, PNG. Supported dimensions: height 640 to 1,536 px, width 640 to 1,536 px. <br>• **seed** – (number) A specific value that is used to guide the 'randomness' of the generation. (Omit this parameter or pass 0 to use a random seed.) Range: 0 to 4294967295. <br>• **negative_prompt** – Keywords of what you do not wish to see in the output image. Max: 10.000 characters. `import boto3 import json import base64 import io from PIL import Image bedrock = boto3.client('bedrock-runtime', region_name='us-west-2') file_path = 'input_image.png' image_bytes = open(file_path, "rb").read() base64_image = base64.b64encode(image_bytes).decode("utf-8") response = bedrock.invoke_model( modelId='us.stability.sd3-large-v1:0', body=json.dumps({ 'prompt': 'A car made out of fruits', 'image': base64_image, 'strength': 0.75, 'mode': 'image-to-image' }) ) output_body = json.loads(response["body"].read().decode("utf-8")) base64_output_image = output_body["images"][0] image_data = base64.b64decode(base64_output_image) image = Image.open(io.BytesIO(image_data)) image.save("output_image.png")` |
