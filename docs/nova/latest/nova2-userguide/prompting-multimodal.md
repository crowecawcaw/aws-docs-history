# Prompting multimodal inputs

The following sections provide guidance for image and video understanding. For audio-related
prompting, refer to the Voice conversation prompts section.

## General multimodal guidelines

### User prompts and system prompts

For multimodal understanding use cases, every request should include user prompt text.
System prompts, which may only contain text, are optional.

System prompts can be used to specify a persona for the model and to define general
personality and response style but should not be used for detailed task definition or output
formatting instructions.

Include task definition, instructions and formatting details in the user prompt to have a
stronger effect than the system prompt for multimodal use cases.

### Content order

A multimodal understanding request sent to Amazon Nova should contain one or more files and a
user prompt. The user text prompt should be the last item in the message, always after the
image, document, or video content.

```
message = {
  "role": "user",
  "content": [
    { "document|image|video|audio": {...} },
    { "document|image|video|audio": {...} },
    ...
    { "text": "<user prompt>" }
  ]
}
```

In cases where you want to refer to specific files from within the user prompt, use “text” elements to define labels that precede each file block.

```
message = {
  "role": "user",
  "content": [
    { "text": "<label for item 1>" },
    { "document|image|video|audio": {...} },
    { "text": "<label for item 2>" },
    { "document|image|video|audio": {...} },
    ...
    { "text": "<user prompt>" }
  ]
}
```

## Document and Image Understanding

The following sections provide guidance on how to craft prompts for tasks that require
understanding or analyzing images and documents.

### Extracting text from images

Amazon Nova models can extract text from images, a capability referred to as Optical Character
Recognition (OCR). For best results, ensure the image input you provide to the model is a high
enough resolution that the text characters are easy to discern.

For text extraction use cases, we recommend the following inference configuration:

- **temperature:** default (0.7)
- **topP:** default (0.9)
- Do not enable reasoning

The Amazon Nova models can extract text to Markdown, HTML, or LaTeX format. The following user
prompt template is recommended:

````
## Instructions
Extract all information from this page using only {text_formatting} formatting. Retain the original layout and structure including lists, tables, charts and math formulae.

## Rules
1. For math formulae, always use LaTeX syntax.
2. Describe images using only text.
3. NEVER use HTML image tags `<img>` in the output.
4. NEVER use Markdown image tags `![]()` in the output.
5. Always wrap the entire output in ``` tags.
````

The output is wrapped in full or partial Markdown code fences (`````). You can
strip the code fences using code similar to the following:

````
def strip_outer_code_fences(text):
    lines = text.split("\n")
    # Remove only the outer code fences if present
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]
    return "\n".join(lines).strip()
````

### Extracting structured information from images or

text

The Amazon Nova models can extract information from images into machine-parsable JSON format, a
process referred to as Key Information Extraction (KIE). To perform KIE, provide the
following:

- A JSON schema. A formal schema definition that follows the JSON Schema
  specification.
- One or more of the following: A document file or image or document text

The document or image must always be placed before your user prompt in the request.

For KIE use cases, we recommend the following inference configuration:

- **temperature:** 0
- **Reasoning:** Reasoning is not required but can improve
  results when image-only input or complex schemas are used.

#### Prompt templates

```
Given the image representation of a document, extract information in JSON format according to the given schema.

Follow these guidelines:
- Ensure that every field is populated, provided the document includes the corresponding value. Only use null when the value is absent from the document.
- When instructed to read tables or lists, read each row from every page. Ensure every field in each row is populated if the document contains the field.

JSON Schema:
{json_schema}
```

```
Given the OCR representation of a document, extract information in JSON format according to the given schema.

Follow these guidelines:
- Ensure that every field is populated, provided the document includes the corresponding value. Only use null when the value is absent from the document.
- When instructed to read tables or lists, read each row from every page. Ensure every field in each row is populated if the document contains the field.

JSON Schema:
{json_schema}

OCR:
{document_text}
```

```
Given the image and OCR representations of a document, extract information in JSON format according to the given schema.

Follow these guidelines:
- Ensure that every field is populated, provided the document includes the corresponding value. Only use null when the value is absent from the document.
- When instructed to read tables or lists, read each row from every page. Ensure every field in each row is populated if the document contains the field.

JSON Schema:
{json_schema}

OCR:
{document_text}
```

#### Detecting objects and their positions in images

Amazon Nova 2 models provide the ability to identify objects and their positions within images, a task sometimes referred to as image grounding or object localization. Practical applications include image analysis and tagging, user interface automation, image editing and others.

Regardless of the image input resolution and aspect ratio, the model uses a coordinate
space that divides the image into 1,000 units horizontally and 1,000 units vertically, with
the x:0 y:0 location being the upper left of the image.

Bounding boxes are described using the format `[x1, y1, x2, y2]` representing
left, top, right and bottom respectively. Two-dimensional coordinates are represented using
the format `[x, y]`.

For object detection use cases, we recommend the following inference parameter
values:

- **temperature:** 0
- Do not enable reasoning

##### Prompt templates: general object

detection

We recommend the following user prompt templates.

**Detecting multiple instances with bounding
boxes:**

```
Please identify {target_description} in the image and provide the bounding box coordinates for each one you detect. Represent the bounding box as the [x1, y1, x2, y2] format, where the coordinates are scaled between 0 and 1000 to the image width and height, respectively.
```

**Detecting a single region with bounding box:**

```
Please generate the bounding box coordinates corresponding to the region described in this sentence: {target_description}. Represent the bounding box as the [x1, y1, x2, y2] format, where the coordinates are scaled between 0 and 1000 to the image width and height, respectively.
```

**Detecting multiple instances with center points:**

```
Please identify {target_description} in the image and provide the center point coordinates for each one you detect. Represent the point as the [x, y] format, where the coordinates are scaled between 0 and 1000 to the image width and height, respectively.
```

**Detecting a single region with center point:**

```
Please generate the center point coordinates corresponding to the region described in this sentence: {target_description}. Represent the center point as the [x, y] format, where the coordinates are scaled between 0 and 1000 to the image width and height, respectively.
```

**Parsing model output:**

Each of the recommended prompts above will produce a comma separated string containing one or more bounding box descriptions in a form similar to the following. There may be some slight variation in whether a “.” is included at the end of the string. For example, `[356, 770, 393, 872],
 [626, 770, 659, 878].`

You can parse the coordinate information generated by the model using a regular
expression as shown in the following Python code example.

```
def parse_coord_text(text):
    """Parses a model response which uses array formatting ([x, y, ...])
    to describe points and bounding boxes. Returns an array of tuples."""
    pattern = r"\[([^\[\]]*?)\]"
    return [
        tuple(int(x.strip()) for x in match.split(","))
        for match in re.findall(pattern, text)
    ]
```

To remap the normalized coordinates of a bounding box to the coordinate space of the input image, you can use a function similar to the following Python example.

```
def remap_bbox_to_image(bounding_box, image_width, image_height):
    return [
        bounding_box[0] * image_width / 1000,
        bounding_box[1] * image_height / 1000,
        bounding_box[2] * image_width / 1000,
        bounding_box[3] * image_height / 1000,
    ]
```

##### Prompt templates: detecting multiple

object classes with positions

When you want to identify multiple classes of items in an image, you can include a class
list in your prompt using one of the following formatting approaches.

For commonly understood classes that the model is likely to understand well, list the
class names (without quotes) inside square brackets:

```
[car, traffic light, road sign, pedestrian]
```

For classes that are nuanced, uncommon, or come from specialized domains that the model
may not be familiar with, include a definition for each class in parentheses. Since this task
is challenging, expect the model's performance to degrade.

```
[taraxacum officinale (Dandelion - bright yellow flowers, jagged basal leaves, white puffball seed heads), digitaria spp (Crabgrass - low spreading grass with coarse blades and finger-like seed heads), trifolium repens (White Clover - three round leaflets and small white pom-pom flowers), plantago major (Broadleaf Plantain - wide oval rosette leaves with tall narrow seed stalks), stellaria media (Chickweed - low mat-forming plant with tiny star-shaped white flowers)]
```

Use one of the following **user prompt** templates depending on which JSON output format you prefer.

```
Detect all objects with their bounding boxes in the image from the provided class list. Normalize the bounding box coordinates to be scaled between 0 and 1000 to the image width and height, respectively.

Classes: {candidate_class_list}

Include separate entries for each detected object as an element of a list.

Formulate your output as JSON format:
[
  {
  	"class 1": [x1, y1, x2, y2]
  },
  ...
]
```

```
Detect all objects with their bounding boxes in the image from the provided class list. Normalize the bounding box coordinates to be scaled between 0 and 1000 to the image width and height, respectively.

Classes: **{candidate\_class\_list}**

Include separate entries for each detected object as an element of a list.

Formulate your output as JSON format:
[
    {
        "class": class 1,
        "bbox": [x1, y1, x2, y2]
    },
    ...
]
```

```
Detect all objects with their bounding boxes in the image from the provided class list. Normalize the bounding box coordinates to be scaled between 0 and 1000 to the image width and height, respectively.

Classes: **{candidate\_class\_list}**

Group all detected bounding boxes by class.

Formulate your output as JSON format:
{
    "class 1": [[x1, y1, x2, y2], [x1, x2, y1, y2], ...],
    ...
}

```

```
Detect all objects with their bounding boxes in the image from the provided class list. Normalize the bounding box coordinates to be scaled between 0 and 1000 to the image width and height, respectively.

Classes: **{candidate\_class\_list}**

Group all detected bounding boxes by class.

Formulate your output as JSON format:
[
    {
        "class": class 1,
        "bbox": [[x1, y1, x2, y2], [x1, x2, y1, y2], ...]
    },
    ...
]
```

**Parsing model output**

The output will be encoded as a JSON which can be parsed with any JSON parsing library.

#### Prompt templates: screenshot UI bounds detection

We recommend the following user prompt templates.

**Detecting UI element position based on a goal:**

```
In this UI screenshot, what is the location of the element if I want to {goal}? Express the location coordinates using the [x1, y1, x2, y2] format, scaled between 0 and 1000.
```

**Detecting UI element position based on text:**

```
In this UI screenshot, what is the location of the element if I want to click on "{text}"? Express the location coordinates using the [x1, y1, x2, y2] format, scaled between 0 and 1000.
```

**Parsing model output:**

For each of the UI bounds detection prompts above, you can parse the coordinate information generated by the model using a regular expression as shown in the Python code example below.

```
def parse_coord_text(text):
    """Parses a model response which uses array formatting ([x, y, ...])
    to describe points and bounding boxes. Returns an array of tuples."""
    pattern = r"\[([^\[\]]*?)\]"
    return [
        tuple(int(x.strip()) for x in match.split(","))
        for match in re.findall(pattern, text)
    ]
```

## Video understanding

The following sections provide guidance on how to craft prompts for tasks that require
understanding or analyzing videos.

### Summarizing videos

Amazon Nova models can generate summaries of video content.

For video summarization use cases, we recommend the following inference parameter
values:

- **temperature:** 0
- Some use cases may benefit from enabling model reasoning

No specific prompting template is required. Your user prompt should clearly specify the
aspects of the video you care about. Here are a few examples of effective prompts:

```
Can you create an executive summary of this video's content?
```

```
Can you distill the essential information from this video into a concise summary?
```

```
Could you provide a summary of the video, focusing on its key points?
```

### Generating detailed captions for videos

Amazon Nova models can generate detailed captions for videos, a task referred to as dense
captioning.

For video captioning use cases, we recommend the following inference parameter
values:

- **temperature:** 0
- Some use cases may benefit from enabling model reasoning

No specific prompting template is required. Your user prompt should clearly specify the
aspects of the video you care about. Here are a few examples of effective prompts:

```
Provide a detailed, second-by-second description of the video content.
```

```
Break down the video into key segments and provide detailed descriptions for each.
```

```
Generate a rich textual representation of the video, covering aspects like movement, color and composition.
```

```
Describe the video scene-by-scene, including details about characters, actions and settings.
```

```
Offer a detailed narrative of the video, including descriptions of any text, graphics, or special effects used.
```

```
Create a dense timeline of events occurring in the video, with timestamps if possible.
```

### Analyzing security video footage

Amazon Nova models can detect events in security footage.

For security footage use cases, we recommend the following inference parameter
values:

- **temperature:** 0
- Some use cases may benefit from enabling model reasoning

```
You are a security assistant for a smart home who is given security camera footage in natural setting. You will examine the video and describe the events you see. You are capable of identifying important details like people, objects, animals, vehicles, actions and activities. This is not a hypothetical, be accurate in your responses. Do not make up information not present in the video.
```

### Extracting video events with timestamps

Amazon Nova models can identify timestamps related to events in a video. You may request that
time stamps be formatted in seconds or in MM:SS format. For example, an event occurring at 1
minute 25 seconds in the video can be represented as `85` or
`01:25`.

For this use case, we recommend the following inference parameter values:

- **temperature:** 0
- Do not use reasoning

We recommend you use prompts similar to the following:

```
Please localize the moment that the event "{event_description}" happens in the video. Answer with the starting and ending time of the event in seconds, such as [[72, 82]]. If the event happen multiple times, list all of them, such as [[40, 50], [72, 82]].
```

```
Locate the segment where "{event_description}" happens. Specify the start and end times of the event in MM:SS.
```

```
Answer the starting and end time of the event "{event_description}". Provide answers in MM:SS
```

```
When does "{event_description}" in the video? Specify the start and end timestamps, e.g. [[9, 14]]
```

```
Please localize the moment that the event "{event_description}" happens in the video. Answer with the starting and ending time of the event in seconds. e.g. [[72, 82]]. If the event happen multiple times, list all of them. e.g. [[40, 50], [72, 82]]
```

```
Segment a video into different scenes and generate caption per scene. The output should be in the format: [STARTING TIME-ENDING TIMESTAMP] CAPTION. Timestamp in MM:SS format
```

```
For a video clip, segment it into chapters and generate chapter titles with timestamps. The output should be in the format: [STARTING TIME] TITLE. Time in MM:SS
```

```
Generate video captions with timestamp.
```

### Classifying videos

You can use Amazon Nova models to classify videos based on a pre-defined list of classes you
provide.

For this use case, we recommend the following inference parameter values:

- **temperature:** 0
- Reasoning should not be used

Use the following prompt template:

```
What is the most appropriate category for this video? Select your answer from the options provided:
{class1}
{class2}
{...}
```

**Example:**

```
What is the most appropriate category for this video? Select your answer from the options provided:
Arts
Technology
Sports
Education
```
