# SageMaker AI Crowd HTML Elements

The following is a list of Crowd HTML Elements that make building a custom
template easier and provide a familiar UI for workers. These elements are supported in Ground Truth,
Augmented AI, and Mechanical Turk.

A message that alerts the worker to a current situation.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/YzNPdGd "https://codepen.io/sagemaker_crowd_html_elements/pen/YzNPdGd").

The following is an example of a Liquid template that uses the `<crowd-alert>`
element. Copy the following code and save it in a file with the extension `.html`.
Open the file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <div id="errorBox"></div>

  <crowd-keypoint
    src="{{ task.input.taskObject | grant_read_access }}"
    labels="['Item A', 'Item B', 'Item C']"
    header="Please locate the centers of each item."
    name="annotatedResult">
    <short-instructions>
      Describe your task briefly here and give examples
    </short-instructions>
    <full-instructions>
      Give additional instructions and good/bad examples here
    </full-instructions>
  </crowd-keypoint>
</crowd-form>

<script>
  var num_obj = 1;

  document.querySelector('crowd-form').onsubmit = function(e) {
    const keypoints = document.querySelector('crowd-keypoint').value.keypoints || document.querySelector('crowd-keypoint')._submittableValue.keypoints;
    const labels = keypoints.map(function(p) {
      return p.label;
    });

    // 1. Make sure total number of keypoints is correct.
    var original_num_labels = document.getElementsByTagName("crowd-keypoint")[0].getAttribute("labels");

    original_num_labels = original_num_labels.substring(2, original_num_labels.length - 2).split("\",\"");
    var goalNumKeypoints = num_obj*original_num_labels.length;
    if (keypoints.length != goalNumKeypoints) {
      e.preventDefault();
      errorBox.innerHTML = '<crowd-alert type="error" dismissible>You must add all keypoint annotations and use each label only once.</crowd-alert>';
      errorBox.scrollIntoView();
      return;
    }

    // 2. Make sure all labels are unique.
    labelCounts = {};
    for (var i = 0; i < labels.length; i++) {
      if (!labelCounts[labels[i]]) {
        labelCounts[labels[i]] = 0;
      }
      labelCounts[labels[i]]++;
    }
    const goalNumSingleLabel = num_obj;

    const numLabels = Object.keys(labelCounts).length;

    Object.entries(labelCounts).forEach(entry => {
      if (entry[1] != goalNumSingleLabel) {
        e.preventDefault();
        errorBox.innerHTML = '<crowd-alert type="error" dismissible>You must use each label only once.</crowd-alert>';
        errorBox.scrollIntoView();
      }
    })
  };
</script>
```

## Attributes

The following attributes are supported by this element.

### dismissible

A Boolean switch that, if present, allows the message to be closed by the worker.

### type

A string that specifies the type of message to be displayed. The possible values are
"info" (the default), "success", "error", and "warning".

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

An icon that floats over the top right corner of another element to which it is
attached.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/WNRbPwZ "https://codepen.io/sagemaker_crowd_html_elements/pen/WNRbPwZ").

The following is an example of a template that uses the `<crowd-badge>`
element. Copy the following code and save it in a file with the extension `.html`.
Open the file in any browser to preview and interact with this template.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-image-classifier
    name="crowd-image-classifier"
    src="https://unsplash.com/photos/NLUkAA-nDdE"
    header="Choose the correct category for this image."
    categories="['Person', 'Umbrella', 'Chair', 'Dolphin']"
  >
    <full-instructions header="Classification Instructions">
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
    </full-instructions>

    <short-instructions id="short-instructions">
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
      <crowd-badge icon="star" for="short-instructions"/>
    </short-instructions>
  </crowd-image-classifier>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### for

A string that specifies the ID of the element to which the badge is attached.

### icon

A string that specifies the icon to be displayed in the badge. The string must be either
the name of an icon from the open-source _[iron-icons](https://github.com/PolymerElements/iron-icons "https://github.com/PolymerElements/iron-icons")_ set, which is pre-loaded, or the
URL to a custom icon.

This attribute overrides the _label_ attribute.

The following is an example of the syntax that you can use to add an iron-icon to a
`<crowd-badge>` HTML element. Replace
`icon-name` with the name of the icon you'd like to use
from this [Icons
set](https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html "https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html").

```
<crowd-badge icon="`icon-name`" for="short-instructions"/>
```

### label

The text to display in the badge. Three characters or less is recommended because text
that is too large will overflow the badge area. An icon can be displayed instead of text by
setting the _icon_ attribute.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A styled button that represents some action.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNvgG "https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNvgG").

The following is an example of a template that uses the `<crowd-button>`
element. Copy the following code and save it in a file with the extension `.html`.
Open the file in any browser to preview and interact with this template.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-image-classifier
    name="crowd-image-classifier"
    src="https://unsplash.com/photos/NLUkAA-nDdE"
    header="Please select the correct category for this image"
    categories="['Person', 'Umbrella', 'Chair', 'Dolphin']"
  >
    <full-instructions header="Classification Instructions">
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
    </full-instructions>
    <short-instructions>
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
      <crowd-button>
        <iron-icon icon="question-answer"/>
      </crowd-button>
    </short-instructions>
  </crowd-image-classifier>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### disabled

A Boolean switch that, if present, displays the button as disabled and prevents clicks.

### form-action

A switch that either submits its parent [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md") element, if set to "submit", or resets its parent
<crowd-form> element, if set to "reset".

### href

The URL to an online resource. Use this property if you need a link styled as a button.

### icon

A string that specifies the icon to be displayed next to the button's text. The string must
be the name of an icon from the open-source _[iron-icons](https://github.com/PolymerElements/iron-icons "https://github.com/PolymerElements/iron-icons")_ set, which
is pre-loaded. For example, to insert
the [search](https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html "https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html") iron-icon, use the
following:

```
<crowd-button>
    <iron-icon icon="search"/>
</crowd-button>
```

The icon is positioned to either the left or the right of the text, as specified by the
_icon-align_ attribute.

To use a custom icon see **icon-url**.

### icon-align

The left or right position of the icon relative to the button's text. The default is
"left".

### icon-url

A URL to a custom image for the icon. A custom image can be used in place of a standard
icon that is specified by the _icon_ attribute.

### loading

A Boolean switch that, if present, displays the button as being in a loading state. This
attribute has precedence over the _disabled_ attribute if both attributes
are present.

### target

When you use the `href` attribute to make the button act as a hyperlink to a specific URL, the `target` attribute optionally targets a frame or window where the linked URL should load.

### variant

The general style of the button. Use "primary" for primary buttons, "normal" for secondary
buttons, "link" for tertiary buttons, or "icon" to display only the icon without text.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for drawing rectangles on an image and assigning a label to the portion of the
image that is enclosed in each rectangle.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJGad "https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJGad").

The following is an example of a Liquid template that uses the
`<crowd-bounding-box>` element. Copy the following code and save it in a file
with the extension `.html`. Open the file in any browser to preview and interact with
this template. For more examples, see this [GitHub repository](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images").

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-bounding-box
    name="annotatedResult"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Draw bounding boxes around all the cats and dogs in this image"
    labels="['Cat', 'Dog']"
  >
    <full-instructions header="Bounding Box Instructions" >
      <p>Use the bounding box tool to draw boxes around the requested target of interest:</p>
      <ol>
        <li>Draw a rectangle using your mouse over each instance of the target.</li>
        <li>Make sure the box does not cut into the target, leave a 2 - 3 pixel margin</li>
        <li>
          When targets are overlapping, draw a box around each object,
          include all contiguous parts of the target in the box.
          Do not include parts that are completely overlapped by another object.
        </li>
        <li>
          Do not include parts of the target that cannot be seen,
          even though you think you can interpolate the whole shape of the target.
        </li>
        <li>Avoid shadows, they're not considered as a part of the target.</li>
        <li>If the target goes off the screen, label up to the edge of the image.</li>
      </ol>
    </full-instructions>

    <short-instructions>
      Draw boxes around the requested target of interest.
    </short-instructions>
  </crowd-bounding-box>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### initial-value

An array of JSON objects, each of which sets a bounding box when the component is loaded.
Each JSON object in the array contains the following properties.
Bounding boxes set via the `initial-value` property can be adjusted and whether or
not a worker answer was adjusted is tracked via an `initialValueModified` boolean in the worker answer output.

- height – The height of the box in pixels.
- label – The text assigned to the box as part of
  the labeling task. This text must match one of the labels defined in the
  _labels_ attribute of the <crowd-bounding-box> element.
- left – Distance of the top-left corner of the box
  from the left side of the image, measured in pixels.
- top – Distance of the top-left corner of the box
  from the top of the image, measured in pixels.
- width – The width of the box in pixels.

You can extract the bounding box initial value from a manifest file of a previous job in a custom template using the Liquid templating language:

```
initial-value="[
  {% for box in task.input.manifestLine.`label-attribute-name-from-prior-job`.annotations %}
    {% capture class_id %}{{ box.class_id }}{% endcapture %}
    {% assign label = task.input.manifestLine.`label-attribute-name-from-prior-job`-metadata.class-map[class_id] %}
    {
      label: {{label | to_json}},
      left: {{box.left}},
      top: {{box.top}},
      width: {{box.width}},
      height: {{box.height}},
    },
  {% endfor %}
 ]"
```

### labels

A JSON formatted array of strings, each of which is a label that a worker can assign to
the image portion enclosed by a rectangle. **Limit:** 10 labels.

### name

The name of this widget. It's used as a key for the widget's input in the form
output.

### src

The URL of the image on which to draw bounding boxes.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#bounding-box-regions-full-instructions "#bounding-box-regions-full-instructions"), [short-instructions](#bounding-box-regions-short-instructions "#bounding-box-regions-short-instructions")

## Regions

The following regions are required by this element.

### full-instructions

General instructions about how to draw bounding boxes.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### boundingBoxes

An array of JSON objects, each of which specifies a bounding box that has been created by
the worker. Each JSON object in the array contains the following properties.

- height – The height of the box in pixels.
- label – The text assigned to the box as part of
  the labeling task. This text must match one of the labels defined in the
  _labels_ attribute of the <crowd-bounding-box> element.
- left – Distance of the top-left corner of the box
  from the left side of the image, measured in pixels.
- top – Distance of the top-left corner of the box
  from the top of the image, measured in pixels.
- width – The width of the box in pixels.

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

###### Example: Sample Element Outputs

The following are samples of outputs from common use scenarios for this element.

**Single Label, Single Box / Multiple Label, Single Box**

```
[
  {
    "annotatedResult": {
      "boundingBoxes": [
        {
          "height": 401,
          "label": "Dog",
          "left": 243,
          "top": 117,
          "width": 187
        }
      ],
      "inputImageProperties": {
        "height": 533,
        "width": 800
      }
    }
  }
]
```

**Single Label, Multiple Box**

```
[
  {
    "annotatedResult": {
      "boundingBoxes": [
        {
          "height": 401,
          "label": "Dog",
          "left": 243,
          "top": 117,
          "width": 187
        },
        {
          "height": 283,
          "label": "Dog",
          "left": 684,
          "top": 120,
          "width": 116
        }
      ],
      "inputImageProperties": {
        "height": 533,
        "width": 800
      }
    }
  }
]
```

**Multiple Label, Multiple Box**

```
[
  {
    "annotatedResult": {
      "boundingBoxes": [
        {
          "height": 395,
          "label": "Dog",
          "left": 241,
          "top": 125,
          "width": 158
        },
        {
          "height": 298,
          "label": "Cat",
          "left": 699,
          "top": 116,
          "width": 101
        }
      ],
      "inputImageProperties": {
        "height": 533,
        "width": 800
      }
    }
  }
]
```

You could have many labels available, but only the ones that are used appear in the output.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A box with an elevated appearance for displaying information.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/QWdwoxe "https://codepen.io/sagemaker_crowd_html_elements/pen/QWdwoxe").

The following is an example of a template designed for sentiment analysis tasks that uses the
`<crowd-card>` element. Copy the following code and save it in a file with the
extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<style>
  h3 {
    margin-top: 0;
  }

  crowd-card {
    width: 100%;
  }

  .card {
    margin: 10px;
  }

  .left {
    width: 70%;
    margin-right: 10px;
    display: inline-block;
    height: 200px;
  }

  .right {
    width: 20%;
    height: 200px;
    display: inline-block;
  }
</style>

<crowd-form>
  <short-instructions>
    Your short instructions here.
  </short-instructions>

  <full-instructions>
    Your full instructions here.
  </full-instructions>

  <div class="left">
    <h3>What sentiment does this text convey?</h3>
    <crowd-card>
      <div class="card">
        Nothing is great.
      </div>
    </crowd-card>
  </div>

  <div class="right">
    <h3>Select an option</h3>

    <select name="sentiment1" style="font-size: large" required>
      <option value="">(Please select)</option>
      <option>Negative</option>
      <option>Neutral</option>
      <option>Positive</option>
      <option>Text is empty</option>
    </select>
  </div>

  <div class="left">
    <h3>What sentiment does this text convey?</h3>
    <crowd-card>
      <div class="card">
        Everything is great!
      </div>
    </crowd-card>
  </div>

  <div class="right">
    <h3>Select an option</h3>

    <select name="sentiment2" style="font-size: large" required>
      <option value="">(Please select)</option>
      <option>Negative</option>
      <option>Neutral</option>
      <option>Positive</option>
      <option>Text is empty</option>
    </select>
  </div>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### heading

The text displayed at the top of the box.

### image

A URL to an image to be displayed within the box.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A UI component that can be checked or unchecked allowing a user to select multiple options
from a set.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/YzNPgOL "https://codepen.io/sagemaker_crowd_html_elements/pen/YzNPgOL").

The following is an example of a Liquid template that uses the
`<crowd-checkbox>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>

  <p>Find the official website for: <strong>{{ task.input.company }}</strong></p>
  <p>Do not give Yelp pages, LinkedIn pages, etc.</p>
  <p>Include the http:// prefix from the website</p>
  <crowd-input name="website" placeholder="http://example.com"></crowd-input>

  <crowd-checkbox name="website-found">Website Found</crowd-checkbox>

</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### checked

A Boolean switch that, if present, displays the check box as checked.

The following is an example of the syntx used to check a checkbox by default.

```
  <crowd-checkbox name="checkedBox" value="checked" checked>This box is checked</crowd-checkbox>
```

### disabled

A Boolean switch that, if present, displays the check box as disabled and prevents it from being
checked.

The following is an example of the syntax used to disable a checkbox.

```
  <crowd-checkbox name="disabledCheckBox" value="Disabled" disabled>Cannot be selected</crowd-checkbox>
```

### name

A string that is used to identify the answer submitted by the worker. This value will
match a key in the JSON object that specifies the answer.

### required

A Boolean switch that, if present, requires the worker to provide input.

The following is an example of the syntax used to require a checkbox be selected.

```
  <crowd-checkbox name="work_verified" required>Instructions were clear</crowd-checkbox>
```

### value

A string used as the name for the check box state in the output. Defaults to "on" if not
specified.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## Output

Provides a JSON object. The `name` string is the object name and the
`value`string is the property name for a Boolean value based on the check box state;
true if checked, false if not checked.

###### Example: Sample Element Outputs

**Using the same `name` value for multiple boxes.**

```
<!-- INPUT -->
<div><crowd-checkbox name="image_attributes" value="blurry"> Blurry </crowd-checkbox></div>
<div><crowd-checkbox name="image_attributes" value="dim"> Too Dim </crowd-checkbox></div>
<div><crowd-checkbox name="image_attributes" value="exposed"> Too Bright </crowd-checkbox></div>
```

```
//Output with "blurry" and "dim" checked
[
  {
    "image_attributes": {
      "blurry": true,
      "dim": true,
      "exposed": false
    }
  }
]
```

Note that all three color values are properties of a single object.

**Using different `name` values for each box.**

```
<!-- INPUT -->
<div><crowd-checkbox name="Stop" value="Red"> Red </crowd-checkbox></div>
<div><crowd-checkbox name="Slow" value="Yellow"> Yellow </crowd-checkbox></div>
<div><crowd-checkbox name="Go" value="Green"> Green </crowd-checkbox></div>
```

```
//Output with "Red" checked
[
  {
    "Go": {
      "Green": false
    },
    "Slow": {
      "Yellow": false
    },
    "Stop": {
      "Red": true
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for classifying non-image content, such as audio, video, or text.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/KKawYBm "https://codepen.io/sagemaker_crowd_html_elements/pen/KKawYBm").

The following is an example of an HTML worker task template built using
`crowd-classifier`. This example uses the [Liquid template language](https://shopify.github.io/liquid/basics/introduction/ "https://shopify.github.io/liquid/basics/introduction/")
to automate:

- Label categories in the `categories` parameter
- The objects that are being classified in the `classification-target`
  parameter.
  Copy the following code and save it in a file with the extension `.html`. Open the
  file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
    <crowd-classifier
      name="category"
      categories="{{ task.input.labels | to_json | escape }}"
      header="What type of a document is this?"
    >
      <classification-target>
        <iframe style="width: 100%; height: 600px;" src="{{ task.input.taskObject  | grant_read_access }}" type="application/pdf"></iframe>
      </classification-target>

      <full-instructions header="Document Classification Instructions">
        <p>Read the task carefully and inspect the document.</p>
        <p>Choose the appropriate label that best suits the document.</p>
      </full-instructions>

      <short-instructions>
        Please choose the correct category for the document
      </short-instructions>
    </crowd-classifier>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### categories

A JSON formatted array of strings, each of which is a category that a worker can assign
to the text. You should include "other" as a category, otherwise the worker my not be able
to provide an answer.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### name

The name of this widget. It is used as a key for the widget's input in the form
output.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [classification-target](#crowd-classifier-regions-classification-target "#crowd-classifier-regions-classification-target"), [full-instructions](#crowd-classifier-regions-full-instructions "#crowd-classifier-regions-full-instructions"), [short-instructions](#crowd-classifier-regions-short-instructions "#crowd-classifier-regions-short-instructions")

## Regions

The following regions are supported by this element.

### classification-target

The content to be classified by the worker. This can be plain text or HTML. Examples of how the HTML can be used include _but are not limited to_ embedding a video or audio player, embedding a PDF, or performing a comparison of two or more images.

### full-instructions

General instructions about how to do text classification.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The output of this element is an object using the specified `name` value as a property name, and a string from the `categories` as the property's value.

###### Example: Sample Element Outputs

The following is a sample of output from this element.

```
[
  {
    "`<*name*>`": {
      "label": "`<*value*>`"
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for classifying various forms of content—such as audio, video, or
text—into one or more categories. The content to classify is referred to as an
_object_.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaMOm "https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaMOm").

The following is an example of an HTML worker task template built using this
element. Copy the following code and save it in a file with the extension `.html`.
Open the file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
    <crowd-classifier-multi-select
      name="category"
      categories="['Positive', 'Negative', 'Neutral']"
      header="Select the relevant categories"
      exclusion-category="{ text: 'None of the above' }"
    >
      <classification-target>
        {{ task.input.taskObject }}
      </classification-target>

      <full-instructions header="Text Categorization Instructions">
        <p><strong>Positive</strong> sentiment include: joy, excitement, delight</p>
        <p><strong>Negative</strong> sentiment include: anger, sarcasm, anxiety</p>
        <p><strong>Neutral</strong>: neither positive or negative, such as stating a fact</p>
        <p><strong>N/A</strong>: when the text cannot be understood</p>
        <p>When the sentiment is mixed, such as both joy and sadness, choose both labels.</p>
      </full-instructions>

      <short-instructions>
       Choose all categories that are expressed by the text.
      </short-instructions>
    </crowd-classifier-multi-select>
</crowd-form>
```

## Attributes

The following attributes are supported by the
`crowd-classifier-multi-select` element. Each attribute accepts a string
value or string values.

### categories

Required. A JSON-formatted array of strings, each of which is a category that a
worker can assign to the object.

### header

Required. The text to display above the image. This is typically a question or
simple instruction for workers.

### name

Required. The name of this widget. In the form output, the name is used as a key
for the widget's input.

### exclusion-category

Optional. A JSON-formatted string with the following format: `"{ text:
 '`default-value`' }"`. This attribute sets a
default value that workers can choose if none of the labels applies to the object
shown in the worker UI.

## Element Hierarchy

This element has the following parent and child elements:

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [classification-target](sms-ui-template-crowd-classifier.md#crowd-classifier-regions-classification-target "sms-ui-template-crowd-classifier.md#crowd-classifier-regions-classification-target"), [full-instructions](sms-ui-template-crowd-classifier.md#crowd-classifier-regions-full-instructions "sms-ui-template-crowd-classifier.md#crowd-classifier-regions-full-instructions"), [short-instructions](sms-ui-template-crowd-classifier.md#crowd-classifier-regions-short-instructions "sms-ui-template-crowd-classifier.md#crowd-classifier-regions-short-instructions")

## Regions

This element uses the following regions.

### classification-target

The content to be classified by the worker. Content can be plain text or an object
that you specify in the template using HTML. For example, you can use HTML elements
to include a video or audio player, embedding a PDF file, or include a comparison of
two or more images.

### full-instructions

General instructions about how to classify text.

### short-instructions

Important task-specific instructions. These instructions are displayed
prominently.

## Output

The output of this element is an object that uses the specified `name`
value as a property name, and a string from `categories` as the property's
value.

###### Example: Sample Element Outputs

The following is a sample of output from this element.

```
[
  {
    "`<*name*>`": {
        labels: ["label_a", "label_b"]
    }
  }
]
```

## See Also

For more information, see the following:

- [Categorize text with text
  classification (Multi-label)](sms-text-classification-multilabel.md "sms-text-classification-multilabel.md")
- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for labeling words, phrases, or character strings within a longer text. Workers
select a label, and highlight the text that the label applies to.

###### Important: Self-contained Widget

Do not use `<crowd-entity-annotation>` element with the `<crowd-form>` element. It contains its own form submission logic and **Submit** button.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJQrR "https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJQrR").

The following is an example of a template that uses the
`<crowd-entity-annotation>` element. Copy the following code and save it in a
file with the extension `.html`. Open the file in any browser to preview and interact
with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-entity-annotation
  name="crowd-entity-annotation"
  header="Highlight parts of the text below"
  labels="[{'label': 'person', 'shortDisplayName': 'per', 'fullDisplayName': 'Person'}, {'label': 'date', 'shortDisplayName': 'dat', 'fullDisplayName': 'Date'}, {'label': 'company', 'shortDisplayName': 'com', 'fullDisplayName': 'Company'}]"
  text="Amazon SageMaker Ground Truth helps you build highly accurate training datasets for machine learning quickly."
>
  <full-instructions header="Named entity recognition instructions">
    <ol>
      <li><strong>Read</strong> the text carefully.</li>
      <li><strong>Highlight</strong> words, phrases, or sections of the text.</li>
      <li><strong>Choose</strong> the label that best matches what you have highlighted.</li>
      <li>To <strong>change</strong> a label, choose highlighted text and select a new label.</li>
      <li>To <strong>remove</strong> a label from highlighted text, choose the X next to the abbreviated label name on the highlighted text.</li>
      <li>You can select all of a previously highlighted text, but not a portion of it.</li>
    </ol>
  </full-instructions>

  <short-instructions>
    Apply labels to words or phrases.
  </short-instructions>

    <div id="additionalQuestions" style="margin-top: 20px">
      <h3>
        What is the overall subject of this text?
      </h3>
      <crowd-radio-group>
        <crowd-radio-button name="tech" value="tech">Technology</crowd-radio-button>
        <crowd-radio-button name="politics" value="politics">Politics</crowd-radio-button>
      </crowd-radio-group>
    </div>
</crowd-entity-annotation>

<script>
  document.addEventListener('all-crowd-elements-ready', () => {
    document
      .querySelector('crowd-entity-annotation')
      .shadowRoot
      .querySelector('crowd-form')
      .form
      .appendChild(additionalQuestions);
  });
</script>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### initial-value

A JSON formatted array of objects, each of which defines an annotation to apply to the text at initialization. Objects contain a `label` value that matches one in the `labels` attribute, an integer `startOffset` value for labeled span's starting unicode offset, and an integer `endOffset` value for the ending unicode offset.

###### Example

```
[
  {
    label: 'person',
    startOffset: 0,
    endOffset: 16
  },
  ...
]
```

### labels

A JSON formatted array of objects, each of which contains:

- `**label**` (required): The name used to identify entities.
- `**fullDisplayName**` (optional): Used for the label list in the task widget. Defaults to the
  label value if not specified.
- `**shortDisplayName**` (optional): An abbreviation of 3-4 letters to display above selected entities. Defaults to the label value if not specified.

###### shortDisplayName is highly recommended

Values displayed above the selections can overlap and create difficulty managing labeled entities in the workspace. Providing a 3-4 character `shortDisplayName` for each label is highly recommended to prevent overlap and keep the workspace manageable for your workers.

###### Example

```
[
  {
    label: 'person',
    shortDisplayName: 'per',
    fullDisplayName: 'person'
  }
]
```

### name

Serves as the widget's name in the DOM. It is also used as the label attribute name in form output and the output manifest.

### text

The text to be annotated. The templating system escapes quotes and HTML strings by default. If your code is already escaped or partially escaped, see [Variable filters](sms-custom-templates-step2-automate.md#sms-custom-templates-step2-automate-filters "sms-custom-templates-step2-automate.md#sms-custom-templates-step2-automate-filters") for more ways to control escaping.

## Element Hierarchy

This element has the following parent and child elements.

- Child elements: [full-instructions](#entity-annotation-regions-full-instructions "#entity-annotation-regions-full-instructions"), [short-instructions](#entity-annotation-regions-short-instructions "#entity-annotation-regions-short-instructions")

## Regions

The following regions are supported by this element.

### full-instructions

General instructions about how to work with the widget.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### entities

A JSON object that specifies the start, end, and label of an annotation. This object contains the following properties.

- label – The assigned label.
- startOffset – The Unicode offset of the
  beginning of the selected text.
- endOffset – The Unicode offset of the first
  character after the selection.

###### Example: Sample Element Outputs

The following is a sample of the output from this element.

```
{
  "myAnnotatedResult": {
    "entities": [
      {
        "endOffset": 54,
        "label": "person",
        "startOffset": 47
      },
      {
        "endOffset": 97,
        "label": "event",
        "startOffset": 93
      },
      {
        "endOffset": 219,
        "label": "date",
        "startOffset": 212
      },
      {
        "endOffset": 271,
        "label": "location",
        "startOffset": 260
      }
    ]
  }
}
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A floating button with an image in its center.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaJaw "https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaJaw").

The following is an example of a Liquid template designed for image classification that uses
the `<crowd-fab>` element. This template uses JavaScript to enable workers to report
issues with the worker UI. Copy the following code and save it in a file with the extension
`.html`. Open the file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
    <crowd-image-classifier
        src="${image_url}"
        categories="['Cat', 'Dog', 'Bird', 'None of the Above']"
        header="Choose the correct category for the image"
        name="category">


        <short-instructions>
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.</p>
            <p>If there is an issue with the image or tools, please select
              <b>None of the Above</b>, describe the issue in the text box and click the
              button below.</p>
            <crowd-input label="Report an Issue" name="template-issues"></crowd-input>
            <crowd-fab id="button1" icon="report-problem" title="Issue"/>
        </short-instructions>

        <full-instructions header="Classification Instructions">
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.
            Use the <b>None of the Above</b> option if none of the other labels suit the image.</p>
        </full-instructions>

    </crowd-image-classifier>
</crowd-form>

<script>
  [
    button1,
  ].forEach(function(button) {
    button.addEventListener('click', function() {
      document.querySelector('crowd-form').submit();
    });
  });
</script>
```

## Attributes

The following attributes are supported by this element.

### disabled

A Boolean switch that, if present, displays the floating button as disabled and prevents clicks.

### icon

A string that specifies the icon to be displayed in the center of the button. The string
must be either the name of an icon from the open-source _[iron-icons](https://github.com/PolymerElements/iron-icons "https://github.com/PolymerElements/iron-icons")_ set, which is
pre-loaded, or the URL to a custom icon.

The following is an example of the syntax that you can use to add an iron-icon to a
`<crowd-fab>` HTML element. Replace
`icon-name` with the name of the icon you'd like to use
from this [Icons
set](https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html "https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html").

```
<crowd-fab "id="button1" icon="`icon-name`" title="Issue"/>
```

### label

A string consisting of a single character that can be used instead of an icon. Emojis or multiple characters may result in the button displaying an ellipsis instead.

### title

A string that will display as a tool tip when the mouse hovers over the button.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

The form wrapper for all custom tasks. Sets and implements important actions for the proper submission of your form data.

If a [crowd-button](sms-ui-template-crowd-button.md "sms-ui-template-crowd-button.md") of type "submit" is not included inside the
`<crowd-form>` element, it will automatically be appended within the
`<crowd-form>` element.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/oNBgOWa "https://codepen.io/sagemaker_crowd_html_elements/pen/oNBgOWa").

The following is an example of an image classification template that uses the
`<crowd-form>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with
this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
    <crowd-image-classifier
        src="${image_url}"
        categories="['Cat', 'Dog', 'Bird', 'None of the Above']"
        header="Choose the correct category for the image"
        name="category">


        <short-instructions>
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.</p>
        </short-instructions>


        <full-instructions header="Classification Instructions">
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.
            Use the <b>None of the Above</b> option if none of the other labels suit the image.</p>
        </full-instructions>

    </crowd-image-classifier>
</crowd-form>
```

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: none
- Child elements: Any of the [UI Template](sms-ui-template-reference.md "sms-ui-template-reference.md") elements

## Element Events

The `crowd-form` element extends the [standard HTML `form` element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form") and inherits its events, such as `onclick` and `onsubmit`.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A button with an image placed in the center. When the user touches the button, a ripple
effect emanates from the center of the button.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaJXE "https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaJXE").

The following is an example of a Liquid template designed for image classification that uses
the `<crowd-icon-button>` element. This template uses JavaScript to enable workers
to report issues with the worker UI. Copy the following code and save it in a file with the
extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
    <crowd-image-classifier
        src="${image_url}"
        categories="['Cat', 'Dog', 'Bird', 'None of the Above']"
        header="Choose the correct category for the image"
        name="category">


        <short-instructions>
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.</p>
            <p>If there is an issue with the image or tools, please select
              <b>None of the Above</b>, describe the issue in the text box and click the
              button below.</p>
            <crowd-input label="Report an Issue" name="template-issues"/></crowd-input>
            <crowd-icon-button id="button1" icon="report-problem" title="Issue"/>
        </short-instructions>

        <full-instructions header="Classification Instructions">
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.
            Use the <b>None of the Above</b> option if none of the other labels suit the image.</p>
        </full-instructions>

    </crowd-image-classifier>
</crowd-form>

<script>
  [
    button1,
  ].forEach(function(button) {
    button.addEventListener('click', function() {
      document.querySelector('crowd-form').submit();
    });
  });
</script>
```

## Attributes

The following attributes are supported by this element.

### disabled

A Boolean switch that, if present, displays the button as disabled and prevents clicks.

### icon

A string that specifies the icon to be displayed in the center of the button. The string
must be either the name of an icon from the open-source _[iron-icons](https://github.com/PolymerElements/iron-icons "https://github.com/PolymerElements/iron-icons")_ set, which is
pre-loaded, or the URL to a custom icon.

The following is an example of the syntax that you can use to add an iron-icon to a
`<crowd-icon-button>` HTML element. Replace
`icon-name` with the name of the icon you'd like to use
from this [Icons
set](https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html "https://www.webcomponents.org/element/@polymer/iron-icons/demo/demo/index.html").

```
<crowd-icon-button id="button1" icon="`icon-name`" title="Issue"/>
```

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for classifying an image. Use one of the following supported image formats: APNG,
BMP, GIF, ICO, JPEG, PNG, SVG. Images do not have a size limit.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/vYgEvWw "https://codepen.io/sagemaker_crowd_html_elements/pen/vYgEvWw").

The following is an example of an image classification template that uses the
`<crowd-image-classifier>` element. Copy the following code and save it in a
file with the extension `.html`. Open the file in any browser to preview and interact
with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
    <crowd-image-classifier
        src="${image_url}"
        categories="['Cat', 'Dog', 'Bird', 'None of the Above']"
        header="Choose the correct category for the image"
        name="category">


        <short-instructions>
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.</p>
        </short-instructions>


        <full-instructions header="Classification Instructions">
            <p>Read the task carefully and inspect the image.</p>
            <p>Choose the appropriate label that best suits the image.
            Use the <b>None of the Above</b> option if none of the other labels suit the image.</p>
        </full-instructions>

    </crowd-image-classifier>
</crowd-form>
```

## Attributes

The following attributes are required by this element.

### categories

A JSON formatted array of strings, each of which is a category that a worker can assign to
the image. You should include "other" as a category, so that the worker can provide an answer.
You can specify up to 10 categories.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### name

The name of this widget. It is used as a key for the widget's input in the form
output.

### overlay

Information to be overlaid on the source image. This is for verification workflows of
bounding-box, semantic-segmentation, and instance-segmentation tasks.

It is a JSON object containing an object with the name of the task-type in camelCase as the key. That key's value is an object that contains the labels and other necessary information from the previous task.

An example of a `crowd-image-classifier` element with attributes for
verifying a bounding-box task follows:

```
<crowd-image-classifier
    name="boundingBoxClassification"
    header="Rate the quality of the annotations based on the background section
       in the instructions on the left hand side."
    src="https://i.imgur.com/CIPKVJo.jpg"
    categories="['good', 'bad', 'okay']"
    overlay='{
        "boundingBox": {
            labels: ["bird", "cat"],
            value: [
                {
                  height: 284,
                  label: "bird",
                  left: 230,
                  top: 974,
                  width: 223
                },
                {
                  height: 69,
                  label: "bird",
                  left: 79,
                  top: 889,
                  width: 247
                }
            ]
        },
    }'
> ... </crowd-image-classifier>
```

A semantic segmentation verification task would use the `overlay` value as
follows:

```
<crowd-image-classifier
  name='crowd-image-classifier'
  categories='["good", "bad"]'
  src='`URL of image to be classified`'
  header='Please classify'
  overlay='{
    "semanticSegmentation": {
      "labels": ["Cat", "Dog", "Bird", "Cow"],
      "labelMappings": {
        "Bird": {
          "color": "#ff7f0e"
        },
        "Cat": {
          "color": "#2ca02c"
        },
        "Cow": {
          "color": "#d62728"
        },
        "Dog": {
          "color": "#2acf59"
        }
      },
      "src": "`URL of overlay image`",
    }
  }'
> ... </crowd-image-classifier>
```

An instance-segmentation task would use the `overlay` value as
follows:

```
<crowd-image-classifier
  name='crowd-image-classifier'
  categories='["good", "bad"]'
  src='`URL of image to be classified`'
  header='Please classify instances of each category'
  overlay='{
    "instanceSegmentation": {
       "labels": ["Cat", "Dog", "Bird", "Cow"],
       "instances": [
        {
         "color": "#2ca02c",
         "label": "Cat"
        },
        {
         "color": "#1f77b4",
         "label": "Cat"
        },
        {
         "color": "#d62728",
         "label": "Dog"
        }
       ],
       "src": "`URL of overlay image`",
    }
  }'
> ... </crowd-image-classifier>
```

### src

The URL of the image to be classified.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#image-classifier-regions-full-instructions "#image-classifier-regions-full-instructions"), [short-instructions](#image-classifier-regions-short-instructions "#image-classifier-regions-short-instructions"), [worker-comment](#image-classifier-regions-worker-comment "#image-classifier-regions-worker-comment")

## Regions

The following regions are used by this element.

### full-instructions

General instructions for the worker on how to classify an image.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

### worker-comment

Use this in verification workflows when you need workers to explain why they made the choice they did. Use the text between the opening and closing tags to provide instructions for workers on what information should be included in the comment.

It uses the following attributes:

#### header

A phrase with a call to action for leaving a comment. Used as the title text for a modal window where the comment is added.

Optional. Defaults to "Add a comment."

#### link-text

This text appears below the categories in the widget. When clicked, it opens a modal window where the worker may add a comment.

Optional. Defaults to "Add a comment."

#### placeholder

An example text in the comment text area that is overwritten when worker begins to type. This does not appear in output if the worker leaves the field blank.

Optional. Defaults to blank.

## Output

The output of this element is a string that specifies one of the values defined in the
_categories_ attribute of the <crowd-image-classifier> element.

###### Example: Sample Element Outputs

The following is a sample of output from this element.

```
[
  {
    "`<*name*>`": {
      "label": "`<*value*>`"
      "workerComment": "`Comment - if no comment is provided, this field will not be present"`
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for classifying an image into one or more categories. Use one of the following
supported image formats: APNG, BMP, GIF, ICO, JPEG, PNG, SVG. Images do not have a size
limit.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/WNRbWgR "https://codepen.io/sagemaker_crowd_html_elements/pen/WNRbWgR").

The following is an example of an HTML worker task template built using this crowd
element. Copy the following code and save it in a file with the extension
`.html`. Open the file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-image-classifier-multi-select
    name="animals"
    categories="['Cat', 'Dog', 'Horse', 'Pig', 'Bird']"
    src="https://images.unsplash.com/photo-1509205477838-a534e43a849f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1998&q=80"
    header="Please identify the animals in this image"
    exclusion-category="{ text: 'None of the above' }"
  >
    <full-instructions header="Classification Instructions">
      <p>If more than one label applies to the image, select multiple labels.</p>
      <p>If no labels apply, select <b>None of the above</b></p>
    </full-instructions>

    <short-instructions>
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label(s) that best suit the image.</p>
    </short-instructions>
  </crowd-image-classifier-multi-select>
</crowd-form>
```

## Attributes

The following attributes are supported by the
`crowd-image-classifier-multi-select` element. Each attribute accepts a
string value or string values.

### categories

Required. A JSON-formatted array of strings, each of which is a category that a
worker can assign to the image. A worker must choose at least one category and can
choose all categories.

### header

Required. The text to display above the image. This is typically a question or
simple instruction for workers.

### name

Required. The name of this widget. In the form output, the name is used as a key
for the widget's input.

### src

Required. The URL of the image to be classified.

### exclusion-category

Optional. A JSON-formatted string with the following format: `"{ text:
 '`default-value`' }"`. This attribute sets a
default value that workers can choose if none of the labels applies to the image
shown in the worker UI.

## Element Hierarchy

This element has the following parent and child elements:

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](sms-ui-template-crowd-image-classifier.md#image-classifier-regions-full-instructions "sms-ui-template-crowd-image-classifier.md#image-classifier-regions-full-instructions"), [short-instructions](sms-ui-template-crowd-image-classifier.md#image-classifier-regions-short-instructions "sms-ui-template-crowd-image-classifier.md#image-classifier-regions-short-instructions"), [worker-comment](sms-ui-template-crowd-image-classifier.md#image-classifier-regions-worker-comment "sms-ui-template-crowd-image-classifier.md#image-classifier-regions-worker-comment")

## Regions

This element uses the following regions

### full-instructions

General instructions for the worker on how to classify an image.

### short-instructions

Important task-specific instructions. These instructions are displayed
prominently.

## Output

The output of this element is a string that specifies one or more of the values
defined in the `categories` attribute of the
`<crowd-image-classifier-multi-select>` element.

###### Example: Sample Element Outputs

The following is a sample of output from this element.

```
[
  {
    "`<*name*>`": {
        labels: ["label_a", "label_b"]
    }
  }
]
```

## See Also

For more information, see the following:

- [Create an image classification job
  (Multi-label)](sms-image-classification-multilabel.md "sms-image-classification-multilabel.md")
- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A box that accepts input data.

###### Cannot be self-closing

Unlike the `input` element in the HTML standard, this element cannot be self-closed by putting a slash before the ending bracket, e.g. `<crowd-input ... />`. It must be followed with a `</crowd-input>` to close the element.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/wvgBZYW "https://codepen.io/sagemaker_crowd_html_elements/pen/wvgBZYW").

The following is an example of a Liquid template that uses the `<crowd-input>`
element. Copy the following code and save it in a file with the extension `.html`. Open
the file in any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <img style="max-width: 35vw; max-height: 50vh" src="{{ task.input.taskObject | grant_read_access }}">
  <crowd-input name="tag1" label="Word/phrase 1" required></crowd-input>
  <crowd-input name="tag2" label="Word/phrase 2" required></crowd-input>
  <crowd-input name="tag3" label="Word/phrase 3" required></crowd-input>

  <short-instructions>
    Your custom quick instructions and examples
  </short-instructions>

  <full-instructions>
    Your custom detailed instracutions and more examples
  </full-instructions>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### allowed-pattern

A regular expression that is used with the _auto-validate_ attribute to
ignore non-matching characters as the worker types.

### auto-focus

When the value is set to true, the browser places focus inside the input area after
loading. This way, the worker can start typing without having to select it first.

### auto-validate

A Boolean switch that, if present, turns on input validation. The behavior of the
validator can be modified by the _error-message_ and
_allowed-pattern_ attributes.

### disabled

A Boolean switch that, if present, displays the input area as disabled.

### error-message

The text to be displayed below the input field, on the left side, if validation
fails.

### label

A string that is displayed inside a text field.

This text shrinks and rises up above a text field when the worker starts typing in the
field or when the _value_ attribute is set.

### max-length

A maximum number of characters the input will accept. Input beyond this limit is
ignored.

### min-length

A minimum length for the input in the field

### name

Sets the name of the input to be used in the DOM and the output of the form.

### placeholder

A string value that is used as placeholder text, displayed until the worker starts entering data into the input, It is not used as a default value.

### required

A Boolean switch that, if present, requires the worker to provide input.

### type

Takes a string to set the HTML5 `input-type` behavior for the input. Examples
include `file` and `date`.

### value

A preset that becomes the default if the worker does not provide input. The preset appears
in a text field.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## Output

Provides a `name` string as the property name, and the text that was entered in
the field as its value.

###### Example: Sample JSON Output

The values for multiple elements are output in the same object, with their `name` attribute value as their property name. Elements with no input do not appear in the output. For example, let's use three inputs:

```
<crowd-input name="tag1" label="Word/phrase 1"></crowd-input>
<crowd-input name="tag2" label="Word/phrase 2"></crowd-input>
<crowd-input name="tag3" label="Word/phrase 3"></crowd-input>
```

This is the output if only two have input:

```
[
  {
    "tag1": "blue",
    "tag2": "red"
  }
]
```

This means any code built to parse these results should be able to handle the presence or absence of each input in the answers.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for identifying individual instances of specific objects within an image and creating a colored overlay for each labeled instance.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/PoWwvwG "https://codepen.io/sagemaker_crowd_html_elements/pen/PoWwvwG").

The following is an example of a Liquid template that uses the
`<crowd-instance-segmentation>`. Copy the following code and save it in a file
with the extension `.html`. Open the file in any browser to preview and interact with
this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-instance-segmentation
    name="annotatedResult"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Please label each of the requested objects in this image"
    labels="['Cat', 'Dog', 'Bird']"
  >
    <full-instructions header="Segmentation Instructions">
      <ol>
          <li><strong>Read</strong> the task carefully and inspect the image.</li>
          <li><strong>Read</strong> the options and review the examples provided to understand more about the labels.</li>
          <li><strong>Choose</strong> the appropriate label that best suits the image.</li>
      </ol>
    </full-instructions>

    <short-instructions>
      <p>Use the tools to label all instances of the requested items in the image</p>
    </short-instructions>
  </crowd-instance-segmentation>
</crowd-form>
```

Use a template similar to the following to allow workers to add their own categories
(labels).

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
  <crowd-instance-segmentation
    id="annotator"
    name="myTexts"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Click Instructions to add new labels."
    labels="['placeholder']"
  >
    <short-instructions>
      <h3>Add a label to describe each type of object in this image.</h3>
      <h3>Cover each instance of each object with a segmentation mask.</h3>
      <br>
      <h3>
        Add new label
      </h3>
      <crowd-input name="_customLabel" id="customLabel"></crowd-input>
      <crowd-button id="addLabel">Add</crowd-button>

      <br><br><br>
      <h3>
      Manage labels
      </h3>
      <div id="labelsSection"></div>
    </short-instructions>

    <full-instructions>
      Describe your task in more detail here.
    </full-instructions>
  </crowd-instance-segmentation>
</crowd-form>

<script>
  document.addEventListener('all-crowd-elements-ready', function(event) {
    document.querySelector('crowd-instance-segmentation').labels = [];
  });

  function populateLabelsSection() {
    labelsSection.innerHTML = '';
    annotator.labels.forEach(function(label) {
      const labelContainer = document.createElement('div');
      labelContainer.innerHTML = label + ' <a href="javascript:void(0)">(Delete)</a>';
      labelContainer.querySelector('a').onclick = function() {
        annotator.labels = annotator.labels.filter(function(l) {
          return l !== label;
        });
        populateLabelsSection();
      };
      labelsSection.appendChild(labelContainer);
    });
  }

  addLabel.onclick = function() {
    annotator.labels = annotator.labels.concat([customLabel.value]);
    customLabel.value = null;

    populateLabelsSection();
  };
</script>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### labels

A JSON formatted array of strings, each of which is a label that a worker can assign to an instance of an object in the image. Workers can generate different overlay colors for each relevant instance by selecting "add instance" under the label in the tool.

### name

The name of this widget. It is used as a key for the labeling data in the form
output.

### src

The URL of the image that is to be labeled.

## initial-value

A JSON object containing the color mappings of a prior instance segmentation job and a
link to the overlay image output by the prior job. Include this when you want a human
worker to verify the results of a prior labeling job and adjust it if necessary.

The attribute will appear as follows:

```
  initial-value="{
    "instances": [
      {
        "color": "#2ca02c",
        "label": "Cat"
      },
      {
        "color": "#1f77b4",
        "label": "Cat"
      },
      {
        "color": "#d62728",
        "label": "Dog"
      }
    ],
    "src": {{ "`S3 file URL for image`" | grant_read_access }}
  }"
```

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#instance-segmentation-regions-full-instructions "#instance-segmentation-regions-full-instructions"), [short-instructions](#instance-segmentation-regions-short-instructions "#instance-segmentation-regions-short-instructions")

## Regions

The following regions are supported by this element.

### full-instructions

General instructions about how to do image segmentation.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### labeledImage

A JSON Object containing a Base64 encoded PNG of the labels.

### instances

A JSON Array containing objects with the instance labels and colors.

- color – The hexadecimal value of the label's RGB color in the `labeledImage` PNG.
- label – The label given to overlay(s) using that color. This value may repeat, because the different instances of the label are identified by their unique color.

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

###### Example: Sample Element Outputs

The following is an example of output from this element.

```
[
  {
    "annotatedResult": {
      "inputImageProperties": {
        "height": 533,
        "width": 800
      },
      "instances": [
        {
          "color": "#1f77b4",
          "label": "`<*Label 1*>`":
        },
        {
          "color": "#2ca02c",
          "label": "`<*Label 1*>`":
        },
        {
          "color": "#ff7f0e",
          "label": "`<*Label 3*>`":
        },
      ],
      "labeledImage": {
        "pngImageData": "`<*Base-64 Encoded Data*>`"
      }
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

An element that displays instructions on three tabbed pages, **Summary**,
**Detailed Instructions**, and **Examples**, when the worker
clicks on a link or button.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJwbx "https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJwbx").

The following is an example of a Liquid template that used the
`<crowd-instructions>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  	<crowd-instructions link-text="View instructions" link-type="button">
		  <short-summary>
		    <p>Given an image, write three words or short phrases that summarize its contents.</p>
		  </short-summary>
		  <detailed-instructions>
		    <p>Imagine that you are describing an image to a friend or tagging it for a news website. Provide three specific words or short phrases that describe it.</p>
		  </detailed-instructions>
		  <positive-example>
		    <p><img src="https://s3.amazonaws.com/cv-demo-images/highway.jpg"/></p>
		    <p>
		    	<ul>
		    		<li>Highway</li>
		    		<li>Cars</li>
		    		<li>Gas station</li>
		    	</ul>
		    </p>
		  </positive-example>
		  <negative-example>
		    <p><img src="https://s3.amazonaws.com/cv-demo-images/highway.jpg"/></p>
		    <p>
		    	These are not specific enough:
		    	<ol>
		    		<li>Trees</li>
		    		<li>Outside</li>
		    		<li>Daytime</li>
		    	</ol>
		    </p>
		  </negative-example>
	</crowd-instructions>
    <p><strong>Instructions: </strong>Given an image, write three words or short phrases that summarize its contents.</p>
    <p>If someone were to see these three words or phrases, they should understand the subject and context of the image, as well as any important actions.</p>
	<p>View the instructions for detailed instructions and examples.</p>
	<p><img style="max-width: 100%; max-height: 100%" src="{{ task.input.taskObject | grant_read_access }}"></p>
  <crowd-input name="tag1" label="Word/phrase 1" required></crowd-input>
  <crowd-input name="tag2" label="Word/phrase 2" required></crowd-input>
  <crowd-input name="tag3" label="Word/phrase 3" required></crowd-input>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### link-text

The text to display for opening the instructions. The default is **Click for
instructions**.

### link-type

A string that specifies the type of trigger for the instructions. The possible values are
"link" (default) and "button".

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## Regions

The following regions are supported by this element.

### detailed-instructions

Content that provides specific instructions for a task. This appears on the page of the
"Detailed Instructions" tab.

### negative-example

Content that provides examples of inadequate task completion. This appears on the page of
the "Examples" tab. More than one example may be provided within this element.

### positive-example

Content that provides examples of proper task completion. This appears on the page of the
"Examples" tab.

### short-summary

A brief statement that summarizes the task to be completed. This appears on the page of
the "Summary" tab. More than one example may be provided within this element.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

Generates a tool to select and annotate key points on an image.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/GRrgaWN "https://codepen.io/sagemaker_crowd_html_elements/pen/GRrgaWN").

The following is an example of an Liquid template that uses the
`<crowd-keypoint>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <div id="errorBox"></div>

  <crowd-keypoint
    src="{{ task.input.taskObject | grant_read_access }}"
    labels="['Item A', 'Item B', 'Item C']"
    header="Please locate the centers of each item."
    name="annotatedResult">
    <short-instructions>
      Describe your task briefly here and give examples
    </short-instructions>
    <full-instructions>
      Give additional instructions and good/bad examples here
    </full-instructions>
  </crowd-keypoint>
</crowd-form>

<script>
  var num_obj = 1;

  document.querySelector('crowd-form').onsubmit = function(e) {
    const keypoints = document.querySelector('crowd-keypoint').value.keypoints || document.querySelector('crowd-keypoint')._submittableValue.keypoints;
    const labels = keypoints.map(function(p) {
      return p.label;
    });

    // 1. Make sure total number of keypoints is correct.
    var original_num_labels = document.getElementsByTagName("crowd-keypoint")[0].getAttribute("labels");

    original_num_labels = original_num_labels.substring(2, original_num_labels.length - 2).split("\",\"");
    var goalNumKeypoints = num_obj*original_num_labels.length;
    if (keypoints.length != goalNumKeypoints) {
      e.preventDefault();
      errorBox.innerHTML = '<crowd-alert type="error" dismissible>You must add all keypoint annotations and use each label only once.</crowd-alert>';
      errorBox.scrollIntoView();
      return;
    }

    // 2. Make sure all labels are unique.
    labelCounts = {};
    for (var i = 0; i < labels.length; i++) {
      if (!labelCounts[labels[i]]) {
        labelCounts[labels[i]] = 0;
      }
      labelCounts[labels[i]]++;
    }
    const goalNumSingleLabel = num_obj;

    const numLabels = Object.keys(labelCounts).length;

    Object.entries(labelCounts).forEach(entry => {
      if (entry[1] != goalNumSingleLabel) {
        e.preventDefault();
        errorBox.innerHTML = '<crowd-alert type="error" dismissible>You must use each label only once.</crowd-alert>';
        errorBox.scrollIntoView();
      }
    })
  };
</script>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### initial-value

An array, in JSON format, of keypoints to be applied to the image on start. For example:

```
initial-value="[
  {
    'label': 'Left Eye',
    'x': 1022,
    'y': 429
  },
  {
    'label': 'Beak',
    'x': 941,
    'y': 403
  }
]
```

###### Note

Please note that label values used in this attribute must have a matching value in the `labels` attribute or the point will not be rendered.

### labels

An array, in JSON format, of strings to be used as keypoint annotation labels.

### name

A string used to identify the answer submitted by the worker. This value will
match a key in the JSON object that specifies the answer.

### src

The source URI of the image to be annotated.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#keypoint-regions-full-instructions "#keypoint-regions-full-instructions"), [short-instructions](#keypoint-regions-short-instructions "#keypoint-regions-short-instructions")

## Regions

The following regions are required by this element.

### full-instructions

General instructions about how to annotate the image.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

### keypoints

An array of JSON objects containing the coordinates and label of a keypoint. Each object contains the following properties.

- label – The assigned label for the keypoint.
- x – The X coordinate, in pixels, of the keypoint on the image.
- y – The Y coordinate, in pixels, of the keypoint on the image.

###### Note

X and Y coordinates are based on 0,0 being the top left corner of the image.

###### Example: Sample Element Outputs

The following is a sample output from using this element.

```
[
  {
    "crowdKeypoint": {
      "inputImageProperties": {
        "height": 1314,
        "width": 962
      },
      "keypoints": [
        {
          "label": "dog",
          "x": 155,
          "y": 275
        },
        {
          "label": "cat",
          "x": 341,
          "y": 447
        },
        {
          "label": "cat",
          "x": 491,
          "y": 513
        },
        {
          "label": "dog",
          "x": 714,
          "y": 578
        },
        {
          "label": "cat",
          "x": 712,
          "y": 763
        },
        {
          "label": "cat",
          "x": 397,
          "y": 814
        }
      ]
    }
  }
]
```

You may have many labels available, but only the ones that are used appear in the output.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for drawing lines on an image. Each line is associated with a label, and output
data will report the starting and ending points of each line.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/NWdPVgw "https://codepen.io/sagemaker_crowd_html_elements/pen/NWdPVgw").

The following is an example of a Liquid template that uses the
`<crowd-line>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with
this template. For more examples, see this [GitHub repository](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images").

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-line
    name="crowdLine"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Add header here to describe the task"
    labels="['car','pedestrian','street car']"
  >
    <short-instructions>
        <p>Read the task carefully and inspect the image.</p>
        <p>Choose the appropriate label that best suits the image.</p>
        <p>Draw a line on each objects that the label applies to.</p>
    </short-instructions>

    <full-instructions>
        <p>Read the task carefully and inspect the image.</p>
        <p>Choose the appropriate label that best suits the image.
        <p>Draw a line along each object that the image applies to.
            Make sure that the line does not extend beyond the boundaries
            of the object.
        </p>
        <p>Each line is defined by a starting and ending point. Carefully
        place the starting and ending points on the boundaries of the object.</p>
    </full-instructions>

  </crowd-line>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### header

Optional. The text to display above the image. This is typically a question or
simple instruction for the worker.

### initial-value

Optional. An array of JSON objects, each of which sets a line when the component
is loaded. Each JSON object in the array contains the following properties:

- label – The text assigned to the
  line as part of the labeling task. This text must match one of the labels
  defined in the _labels_ attribute of the
  `<crowd-line>` element.
- vertices – the `x` and
  `y` pixel corrdinates of the start point and end point of the
  line, relative to the top-left corner of the image.

```
initial-value="{
    lines: [
    {
        label: 'sideline', // label of this line annotation
        vertices:[         // an array of vertices which decide the position of the line
        {
            x: 84,
            y: 110
        },
        {
            x: 60,
            y: 100
        }
        ]
    },
    {
        label: 'yardline',
        vertices:[
        {
            x: 651,
            y: 498
        },
        {
            x: 862,
            y: 869
        }
        ]
    }
   ]
}"
```

Lines set via the `initial-value` property can be adjusted. Whether or
not a worker answer was adjusted is tracked via an `initialValueModified`
boolean in the worker answer output.

### labels

Required. A JSON formatted array of strings, each of which is a label that a
worker can assign to the line.

**Limit:** 10 labels

### label-colors

Optional. An array of strings. Each string is a hexadecimal (hex) code for a
label.

### name

Required. The name of this widget. It's used as a key for the widget's input in
the form output.

### src

Required. The URL of the image on which to draw lines.

## Regions

The following regions are required by this element.

### full-instructions

General instructions about how to draw lines.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [short-instructions](#line-regions-short-instructions "#line-regions-short-instructions"), [full-instructions](#line-regions-full-instructions "#line-regions-full-instructions")

## Output

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

### lines

A JSON Array containing objects with the line labels and vertices.

- label – The label given to a
  line.
- vertices – the `x` and `y` pixel corrdinates
  of the start point and end point of the line, relative to the top-left
  corner of the image.

###### Example: Sample Element Outputs

The following is an example of output from this element.

```
{
    "crowdLine": { //This is the name you set for the crowd-line
      "inputImageProperties": {
        "height": 1254,
        "width": 2048
      },
      "lines": [
        {
          "label": "yardline",
          "vertices": [
            {
              "x": 58,
              "y": 295
            },
            {
              "x": 1342,
              "y": 398
            }
          ]
        },
        {
          "label": "sideline",
          "vertices": [
            {
              "x": 472,
              "y": 910
            },
            {
              "x": 1480,
              "y": 600
            }
          ]
        }
      ]
    }
  }
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A small window that pops up on the display when it is opened.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNmyK "https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNmyK").

The following is an example of the syntax that you can use with the
`<crowd-modal>` element. Copy the following code and save it in a file with the
extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-modal
link-text = "See Examples"
link-type = "button">
Example Modal Text</crowd-modal>
```

## Attributes

The following attributes are supported by this element.

### link-text

The text to display for opening the modal. The default is "Click to open modal".

### link-type

A string that specifies the type of trigger for the modal. The possible values are "link"
(default) and "button".

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for drawing polygons on an image and assigning a label to the portion of the
image that is enclosed in each polygon.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/eYgmajo "https://codepen.io/sagemaker_crowd_html_elements/pen/eYgmajo").

The following is an example of a Liquid template that uses the
`<crowd-polygon>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-polygon
    name="annotatedResult"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Draw a polygon around each of the requested target(s) of interest"
    labels="['Cat', 'Dog', 'Bird']"
  >
    <full-instructions header="Polygon instructions">
      <ul>
        <li>Make the polygon tight around the object</li>
        <li>You need to select a label before starting a polygon</li>
        <li>You will need to select a label again after completing a polygon</li>
        <li>To select a polygon, you can click on its borders</li>
        <li>You can start drawing a polygon from inside another polygon</li>
        <li>You can undo and redo while you're drawing a polygon to go back and forth between points you've placed</li>
        <li>You are prevented from drawing lines that overlap other lines from the same polygon</li>
      </ul>
    </full-instructions>

    <short-instructions>
      <p>Draw a polygon around each of the requested target(s) of interest</p>
      <p>Make the polygon tight around the object</p>
    </short-instructions>
  </crowd-polygon>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### labels

A JSON formatted array of strings, each of which is a label that a worker can assign to
the image portion enclosed by a polygon.

### name

The name of this widget. It's used as a key for the widget's input in the form
output.

### src

The URL of the image on which to draw polygons.

### initial-value

An array of JSON objects, each of which defines a polygon to be drawn when the component is loaded.
Each JSON object in the array contains the following properties.

- label – The text assigned to the polygon as part of
  the labeling task. This text must match one of the labels defined in the
  _labels_ attribute of the <crowd-polygon> element.
- vertices – An array of JSON objects. Each object
  contains an x and y coordinate value for a point in the polygon.

###### Example

An `initial-value` attribute might look something like this.

```
initial-value =
  '[
     {
     "label": "dog",
     "vertices":
       [
         {
            "x": 570,
            "y": 239
         },
        ...
         {
            "x": 759,
            "y": 281
         }
       ]
     }
  ]'
```

Because this will be within an HTML element, the JSON array must be enclosed in single or double quotes. The example above uses single quotes to encapsulate the JSON and double quotes within the JSON itself. If you must mix single and double quotes inside your JSON, replace them with their HTML entity codes (`&quot;` for double quote, `&#39;` for single) to safely escape them.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#polygon-regions-full-instructions "#polygon-regions-full-instructions"), [short-instructions](#polygon-regions-short-instructions "#polygon-regions-short-instructions")

## Regions

The following regions are required.

### full-instructions

General instructions about how to draw polygons.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### polygons

An array of JSON objects, each of which describes a polygon that has been created by the
worker. Each JSON object in the array contains the following properties.

- label – The text assigned to the polygon as part of
  the labeling task.
- vertices – An array of JSON objects. Each object
  contains an x and y coordinate value for a point in the polygon. The top left corner of the
  image is 0,0.

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

###### Example: Sample Element Outputs

The following are samples of outputs from common use scenarios for this element.

**Single Label, Single Polygon**

```
{
    "annotatedResult":
    {
      "inputImageProperties": {
        "height": 853,
        "width": 1280
      },
      "polygons":
      [
        {
          "label": "dog",
          "vertices":
          [
            {
              "x": 570,
              "y": 239
            },
            {
              "x": 603,
              "y": 513
            },
            {
              "x": 823,
              "y": 645
            },
            {
              "x": 901,
              "y": 417
            },
            {
              "x": 759,
              "y": 281
            }
          ]
        }
      ]
    }
  }
]
```

**Single Label, Multiple Polygons**

```
[
  {
    "annotatedResult": {
      "inputImageProperties": {
        "height": 853,
        "width": 1280
      },
      "polygons": [
        {
          "label": "dog",
          "vertices": [
            {
              "x": 570,
              "y": 239
            },
            {
              "x": 603,
              "y": 513
            },
            {
              "x": 823,
              "y": 645
            },
            {
              "x": 901,
              "y": 417
            },
            {
              "x": 759,
              "y": 281
            }
          ]
        },
        {
          "label": "dog",
          "vertices": [
            {
              "x": 870,
              "y": 278
            },
            {
              "x": 908,
              "y": 446
            },
            {
              "x": 1009,
              "y": 602
            },
            {
              "x": 1116,
              "y": 519
            },
            {
              "x": 1174,
              "y": 498
            },
            {
              "x": 1227,
              "y": 479
            },
            {
              "x": 1179,
              "y": 405
            },
            {
              "x": 1179,
              "y": 337
            }
          ]
        }
      ]
    }
  }
]
```

**Multiple Labels, Multiple Polygons**

```
[
  {
    "annotatedResult": {
      "inputImageProperties": {
        "height": 853,
        "width": 1280
      },
      "polygons": [
        {
          "label": "dog",
          "vertices": [
            {
              "x": 570,
              "y": 239
            },
            {
              "x": 603,
              "y": 513
            },
            {
              "x": 823,
              "y": 645
            },
            {
              "x": 901,
              "y": 417
            },
            {
              "x": 759,
              "y": 281
            }
          ]
        },
        {
          "label": "cat",
          "vertices": [
            {
              "x": 870,
              "y": 278
            },
            {
              "x": 908,
              "y": 446
            },
            {
              "x": 1009,
              "y": 602
            },
            {
              "x": 1116,
              "y": 519
            },
            {
              "x": 1174,
              "y": 498
            },
            {
              "x": 1227,
              "y": 479
            },
            {
              "x": 1179,
              "y": 405
            },
            {
              "x": 1179,
              "y": 337
            }
          ]
        }
      ]
    }
  }
]
```

You could have many labels available, but only the ones that are used appear in the output.

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for drawing polylines or lines on an image. Each polyline is associated with a
label and can include two or more vertices. A polyline can intersect itself and its starting
and ending points can be placed anywhere on the image.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/PoWwvyJ "https://codepen.io/sagemaker_crowd_html_elements/pen/PoWwvyJ").

The following is an example of a Liquid template that uses the
`<crowd-polyline>` element. Copy the following code and save it in a file
with the extension `.html`. Open the file in any browser to preview and interact
with this template. For more examples, see this [GitHub repository](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/tree/master/images").

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-polyline
    name="crowdPolyline"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Add header here to describe the task"
    labels="['car','pedestrian','street car']"
  >
    <full-instructions>
        <p>Read the task carefully and inspect the image.</p>
        <p>Choose the appropriate label that best suits the image.</p>
        <p>Draw a polyline around the boundaries of all objects
        that the label applies to.</p>
        <p>Use the <b>Enter</b> key to complete a polyline.</p>
        <p>Make sure that the polyline fits tightly around the boundary
        of the object.</p>
    </full-instructions>

    <short-instructions>
        <p>Read the task carefully and inspect the image.</p>
        <p>Review the tool guide to learn how to use the polyline tool.</p>
        <p>Choose the appropriate label that best suits the image.</p>
        <p>To draw a polyline, select a label that applies to an object of interest
            and add a single point to the photo by clicking on that point. Continue to
            draw the polyline around the object by adding additional points
            around the object boundary.</p>
        <p>After you place the final point on the polyline, press <b>Enter</b> on your
        keyboard to complete the polyline.</p>

    </short-instructions>
  </crowd-polyline>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### header

Optional. The text to display above the image. This is typically a question or
simple instruction for the worker.

### initial-value

Optional. An array of JSON objects, each of which sets a polyline when the
component is loaded. Each JSON object in the array contains the following
properties:

- label – The text assigned to the
  polyline as part of the labeling task. This text must match one of the
  labels defined in the _labels_ attribute of the
  `<crowd-polyline>` element.
- vertices – the `x` and
  `y` pixel corrdinates of the vertices of a polyline, relative
  to the top-left corner of the image.

```
 initial-value= "{
    polylines: [
    {
        label: 'sideline', // label of this line annotation
        vertices:[         // an array of vertices which decide the position of the line
        {
            x: 84,
            y: 110
        },
        {
            x: 60,
            y: 100
        }
        ]
    },
    {
        label: 'yardline',
        vertices:[
        {
            x: 651,
            y: 498
        },
        {
            x: 862,
            y: 869
        },
        {
            x: 1000,
            y: 869
        }
        ]
    }
   ]
}"
```

Polylines set via the `initial-value` property can be adjusted. Whether
or not a worker answer was adjusted is tracked via an
`initialValueModified` boolean in the worker answer output.

### labels

Required. A JSON formatted array of strings, each of which is a label that a
worker can assign to the line.

**Limit:** 10 labels

### label-colors

Optional. An array of strings. Each string is a hexadecimal (hex) code for a
label.

### name

Required. The name of this widget. It's used as a key for the widget's input in
the form output.

### src

Required. The URL of the image on which to draw polylines.

## Regions

The following regions are required by this element.

### full-instructions

General instructions about how to draw polylines.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [short-instructions](#polyline-regions-short-instructions "#polyline-regions-short-instructions"), [full-instructions](#polyline-regions-full-instructions "#polyline-regions-full-instructions")

## Output

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

### polylines

A JSON Array containing objects with polylines' labels and vertices.

- label – The label given to a
  line.
- vertices – the `x` and `y` pixel corrdinates
  of the vertices of a polyline, relative to the top-left corner of the
  image.

###### Example: Sample Element Outputs

The following is an example of output from this element.

```
 {
    "crowdPolyline": { //This is the name you set for the crowd-polyline
      "inputImageProperties": {
        "height": 1254,
        "width": 2048
      },
      "polylines": [
        {
          "label": "sideline",
          "vertices": [
            {
              "x": 651,
              "y": 498
            },
            {
              "x": 862,
              "y": 869
            },
            {
              "x": 1449,
              "y": 611
            }
          ]
        },
        {
          "label": "yardline",
          "vertices": [
            {
              "x": 1148,
              "y": 322
            },
            {
              "x": 1705,
              "y": 474
            },
            ,
            {
              "x": 1755,
              "y": 474
            }
          ]
        }
      ]
    }
  }
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A button that can be either checked or unchecked. When radio buttons are inside a radio
group, exactly one radio button in the group can be checked at any time. The following is an
example of how to configure a `crowd-radio-button` element inside of a
`crowd-radio-group` element.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/yLgyWGZ "https://codepen.io/sagemaker_crowd_html_elements/pen/yLgyWGZ").

The following is an example of the syntax that you can use with the
`<crowd-radio-button>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
<crowd-radio-group>
    <crowd-radio-button name="tech" value="tech">Technology</crowd-radio-button>
    <crowd-radio-button name="politics" value="politics">Politics</crowd-radio-button>
</crowd-radio-group>
</crowd-form>
```

The previous example can be seen in a custom worker task template in this GitHub example:
[entity recognition labeling job custom template](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/master/text/named-entity-recognition-with-additional-classification.liquid.html "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/master/text/named-entity-recognition-with-additional-classification.liquid.html").

Crowd HTML Element radio buttons do not support the HTML tag, `required`. To make
a radio button selection required, use `<input type="radio">` elements to create
radio buttons and add the `required` tag. The `name` attribute for all
`<input>` elements that belong to the same group of radio buttons must be the
same. For example, the following template requires the user to select a radio button in the
`animal-type` group before submitting.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
  <p>Select an animal type:</p>
<img src="https://images.unsplash.com/photo-1537151608828-ea2b11777ee8?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1539&q=80" style="height: 500; width: 400;"/>
<br><br>
<div>
  <input type="radio" id="cat" name="animal-type" value="cat" required>
  <label for="cat">Cat</label>
</div>
<div>
  <input type="radio" id="dog" name="animal-type" value="dog">
  <label for="dog">Dog</label>
</div>
<div>
  <input type="radio" id="unknown" name="animal-type" value="unknown">
  <label for="unknown">Unknown</label>
</div>
    <full-instructions header="Classification Instructions">
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
    </full-instructions>
    <short-instructions>
      <p>Read the task carefully and inspect the image.</p>
      <p>Choose the appropriate label that best suits the image.</p>
    </short-instructions>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### checked

A Boolean switch that, if present, displays the radio button as checked.

### disabled

A Boolean switch that, if present, displays the button as disabled and prevents it from being
checked.

### name

A string that is used to identify the answer submitted by the worker. This value will
match a key in the JSON object that specifies the answer.

###### Note

If you use the buttons outside of a [crowd-radio-group](sms-ui-template-crowd-radio-group.md "sms-ui-template-crowd-radio-group.md")
element, but with the same `name` string and different `value` strings,
the `name` object in the output will contain a Boolean value for each `value` string. To ensure that
only one button in a group is selected, make them children of a [crowd-radio-group](sms-ui-template-crowd-radio-group.md "sms-ui-template-crowd-radio-group.md")
element and use different name values.

### value

A property name for the element's boolean value. If not specified, it uses "on" as the default, e.g. `{ "<name>": { "<value>": <true or false> } }`.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-radio-group](sms-ui-template-crowd-radio-group.md "sms-ui-template-crowd-radio-group.md")
- Child elements: none

## Output

Outputs an object with the following pattern: `{ "<name>": { "<value>":
 <true or false> } }`. If you use the buttons outside of a [crowd-radio-group](sms-ui-template-crowd-radio-group.md "sms-ui-template-crowd-radio-group.md")
element, but with the same `name` string and different `value` strings,
the name object will contain a Boolean value for each `value` string. To ensure that
only one in a group of buttons is selected, make them children of a [crowd-radio-group](sms-ui-template-crowd-radio-group.md "sms-ui-template-crowd-radio-group.md")
element and use different name values.

###### Example Sample output of this element

```
[
  {
    "btn1": {
      "yes": true
    },
    "btn2": {
      "no": false
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A group of radio buttons. Only one radio button within the group can be selected. Choosing
one radio button clears any previously chosen radio button within the same group. For an example
of a custom UI template that uses the `crowd-radio-group` element, see this [entity recognition labeling job custom template](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/master/text/named-entity-recognition-with-additional-classification.liquid.html "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/master/text/named-entity-recognition-with-additional-classification.liquid.html").

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/KKawjPJ "https://codepen.io/sagemaker_crowd_html_elements/pen/KKawjPJ").

The following is an example of the syntax that you can use with the
`<crowd-radio-group>` element. Copy the following code and save it in a file
with the extension `.html`. Open the file in any browser to preview and interact with
this template.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<style>
	body {
		padding-left: 20px;
		margin-bottom: 20px;
	}
	#outer-container {
	    display: flex;
	    justify-content: space-around;
	    max-width: 900px;
	    margin-left: 100px;
	}
	.left-container {
    	margin-right: auto;
    	padding-right: 50px;
	}
	.right-container {
    	margin-left: auto;
    	padding-left: 50px;
	}
	#vertical-separator {
	    border: solid 1px #d5dbdb;
	}
</style>

<crowd-form>
    <div>
        <h1>Instructions</h1>
	Lorem ipsum...
    </div>
    <div>
        <h2>Background</h2>
    	<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
    </div>
    <div id="outer-container">
	<span class="left-container">
	    <h2>Option 1</h2>
	    <p>Nulla facilisi morbi tempus iaculis urna. Orci dapibus ultrices in iaculis nunc sed augue lacus.</p>
	</span>
	<span id="vertical-separator"></span>
	<span class="right-container">
	    <h2>Option 2</h2>
	    <p>Ultrices vitae auctor eu augue ut. Pellentesque massa placerat duis ultricies lacus sed turpis tincidunt id.</p>
	</span>
    </div>
    <div>
        <h2>Question</h2>
    	<p>Which do you agree with?</p>
	<crowd-radio-group>
	    <crowd-radio-button name="option1" value="Option 1">Option 1</crowd-radio-button>
	    <crowd-radio-button name="option2" value="Option 2">Option 2</crowd-radio-button>
	</crowd-radio-group>

    	<p>Why did you choose this answer?</p>
	<crowd-text-area name="explanation" placeholder="Explain how you reached your conclusion..."></crowd-text-area>
    </div>
</crowd-form>
```

## Attributes

No special attributes are supported by this element.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [crowd-radio-button](sms-ui-template-crowd-radio-button.md "sms-ui-template-crowd-radio-button.md")

## Output

Outputs an array of objects representing the [crowd-radio-button](sms-ui-template-crowd-radio-button.md "sms-ui-template-crowd-radio-button.md") elements within it.

###### Example Sample of Element Output

```
[
  {
    "btn1": {
      "yes": true
    },
    "btn2": {
      "no": false
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A widget for segmenting an image and assigning a label to each image segment.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/LYxEKEb "https://codepen.io/sagemaker_crowd_html_elements/pen/LYxEKEb").

The following is an example of a Liquid template that uses the
`<crowd-semantic-segmentation>` element. Copy the following code and save it in
a file with the extension `.html`. Open the file in any browser to preview and
interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-semantic-segmentation
    name="annotatedResult"
    src="{{ task.input.taskObject | grant_read_access }}"
    header="Please label each of the requested objects in this image"
    labels="['Cat', 'Dog', 'Bird']"
  >
    <full-instructions header="Segmentation Instructions">
      <ol>
          <li><strong>Read</strong> the task carefully and inspect the image.</li>
          <li><strong>Read</strong> the options and review the examples provided to understand more about the labels.</li>
          <li><strong>Choose</strong> the appropriate label that best suits the image.</li>
      </ol>
    </full-instructions>

    <short-instructions>
      <p>Use the tools to label the requested items in the image</p>
    </short-instructions>
  </crowd-semantic-segmentation>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### header

The text to display above the image. This is typically a question or simple instruction
for the worker.

### initial-value

A JSON object containing the color mappings of a prior semantic segmentation job and a link to the overlay image output by the prior job. Include this when you want a human worker to verify the results of a prior labeling job and adjust it if necessary.

The attribute would appear as follows:

```
  initial-value='{
    "labelMappings": {
        "Bird": {
          "color": "#ff7f0e"
        },
        "Cat": {
          "color": "#2ca02c"
        },
        "Cow": {
          "color": "#d62728"
        },
        "Dog": {
          "color": "#1f77b4"
        }
      },
    "src": {{ "`S3 file URL for image`" | grant_read_access }}
  }'
```

When using Ground Truth [built in task types](sms-task-types.md "sms-task-types.md") with
[annotation consolidation](sms-annotation-consolidation.md "sms-annotation-consolidation.md") (where more than one worker labels a single
image), label mappings are included in individual worker output records, however the overall
result is represented as the `internal-color-map` in the consolidated
results.

You can convert the `internal-color-map` to `label-mappings` in a custom template using the Liquid templating language:

```
initial-value="{
  'src' : '{{ task.input.manifestLine.`label-attribute-name-from-prior-job`| grant_read_access }}',
  'labelMappings': {
     {% for box in task.input.manifestLine.`label-attribute-name-from-prior-job`-metadata.internal-color-map %}
       {% if box[1]['class-name'] != 'BACKGROUND' %}
         {{ box[1]['class-name'] | to_json }}: {
           'color': {{ box[1]['hex-color'] | to_json }}
         },
       {% endif %}
     {% endfor %}
   }
}"
```

### labels

A JSON formatted array of strings, each of which is a label that a worker can assign to a
segment of the image.

### name

The name of this widget. It is used as a key for the widget's input in the form
output.

### src

The URL of the image that is to be segmented.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [full-instructions](#semantic-segmentation-regions-full-instructions "#semantic-segmentation-regions-full-instructions"), [short-instructions](#semantic-segmentation-regions-short-instructions "#semantic-segmentation-regions-short-instructions")

## Regions

The following regions are supported by this element.

### full-instructions

General instructions about how to do image segmentation.

### short-instructions

Important task-specific instructions that are displayed in a prominent place.

## Output

The following output is supported by this element.

### labeledImage

A JSON Object containing a Base64 encoded PNG of the labels.

### labelMappings

A JSON Object containing objects with named with the segmentation labels.

- color – The hexadecimal value of the label's RGB color in the `labeledImage` PNG.

### initialValueModified

A boolean representing whether the initial values have been modified. This is only included when the output is from an adjustment task.

### inputImageProperties

A JSON object that specifies the dimensions of the image that is being annotated by the
worker. This object contains the following properties.

- height – The height, in pixels, of the
  image.
- width – The width, in pixels, of the image.

###### Example: Sample Element Outputs

The following is a sample of output from this element.

```
[
  {
    "annotatedResult": {
      "inputImageProperties": {
        "height": 533,
        "width": 800
      },
      "labelMappings": {
        "`<*Label 2*>`": {
          "color": "#ff7f0e"
        },
        "`<*label 3*>`": {
          "color": "#2ca02c"
        },
        "`<*label 1*>`": {
          "color": "#1f77b4"
        }
      },
      "labeledImage": {
        "pngImageData": "`<*Base-64 Encoded Data*>`"
      }
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A bar with a sliding knob that allows a worker to select a value from a range of values by
moving the knob. The slider makes it a great choice for settings that reflect intensity levels,
such as volume, brightness, or color saturation.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNzWL "https://codepen.io/sagemaker_crowd_html_elements/pen/RwKNzWL").

The following is an example of a survey template that uses the `<crowd-slider>`
element. Copy the following code and save it in a file with the extension `.html`.
Open the file in any browser to preview and interact with this template.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
<crowd-instructions link-text="View instructions" link-type="button">
  <short-summary>
    <p>Provide a brief instruction here</p>
  </short-summary>

  <detailed-instructions>
    <h3>Provide more detailed instructions here</h3>
    <p>Include additional information</p>
  </detailed-instructions>

  <positive-example>
    <p>Provide an example of a good answer here</p>
    <p>Explain why it's a good answer</p>
  </positive-example>

  <negative-example>
    <p>Provide an example of a bad answer here</p>
    <p>Explain why it's a bad answer</p>
  </negative-example>
</crowd-instructions>

<div>
  <p>What is your favorite color for a bird?</p>
  <crowd-input name="favoriteColor" placeholder="example: pink" required></crowd-input>
</div>

<div>
  <p>Check this box if you like birds</p>
  <crowd-checkbox name="likeBirds" checked="true" required></crowd-checkbox>
</div>

<div>
  <p>On a scale of 1-10, how much do you like birds?</p>
  <crowd-slider name="howMuch" min="1" max="10" step="1" pin="true" required></crowd-slider>
</div>

<div>
  <p>Write a short essay describing your favorite bird</p>
  <crowd-text-area name="essay" rows="4" placeholder="Lorem ipsum..." required></crowd-text-area>
</div>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### disabled

A Boolean switch that, if present, displays the slider as disabled.

### editable

A Boolean switch that, if present, displays an up/down button that can be chosen to select
the value.

Selecting the value via the up/down button is an alternative to selecting the value by
moving the knob on the slider. The knob on the slider will move synchronously with the up/down
button choices.

### max

A number that specifies the maximum value on the slider.

### min

A number that specifies the minimum value on the slider.

### name

A string that is used to identify the answer submitted by the worker. This value will
match a key in the JSON object that specifies the answer.

### pin

A Boolean switch that, if present, displays the current value above the knob as the knob is moved.

### required

A Boolean switch that, if present, requires the worker to provide input.

### secondary-progress

When used with a `crowd-slider-secondary-color` CSS attribute, the progress bar
is colored to the point represented by the `secondary-progress`. For example, if
this was representing the progress on a streaming video, the `value` would represent
where the viewer was in the video timeline. The `secondary-progress` value would
represent the point on the timeline to which the video had buffered.

### step

A number that specifies the difference between selectable values on the slider.

### value

A preset that becomes the default if the worker does not provide input.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A component styled to look like a tab with information below.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/dyNPBGW "https://codepen.io/sagemaker_crowd_html_elements/pen/dyNPBGW").

The following is an example template that uses the `<crowd-tab>` element. Copy
the following code and save it in a file with the extension `.html`. Open the file in
any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-tabs>
    <crowd-tab header="Tab 1">
      <h2>Image</h2>

      <img
        src="https://images.unsplash.com/photo-1478382188900-5bb598fe27d3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80"
        style="max-width: 40%"
      >

      <h2>Text</h2>
      <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </p>
      <p>
      Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.
      </p>
    </crowd-tab>

    <crowd-tab header="Tab 2">
      <h2>Description</h2>
      <p>
      Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.
      </p>
    </crowd-tab>

    <crowd-tab header="Tab 3">
      <div style="width: 40%; display: inline-block">
        <img
          src="https://images.unsplash.com/photo-1472747459646-91fd6f13995f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
          style="max-width: 80%"
        >
        <crowd-input label="Input inside tab" name="inputInsideTab"></crowd-input>
        <input type="checkbox" name="checkbox" value="foo">Foo
        <input type="checkbox" name="checkbox" value="bar">Bar
        <crowd-button>Some button</crowd-button>
      </div>

      <div style="width: 40%; display: inline-block; vertical-align: top">
        Lorem ipsum dolor sit amet, lorem a wisi nibh, in pulvinar, consequat praesent vestibulum tellus ante felis auctor, vitae lobortis dictumst mauris.
        Pellentesque nulla ipsum ante quisque quam augue.
        Class lacus id euismod, blandit tempor mauris quisque tortor mauris, urna gravida nullam pede libero, ut suscipit orci faucibus lacus varius ornare, pellentesque ipsum.
        At etiam suspendisse est elementum luctus netus, vel sem nulla sodales, potenti magna enim ipsum diam tortor rutrum,
        quam donec massa elit ac, nam adipiscing sed at leo ipsum consectetuer. Ac turpis amet wisi, porttitor sint lacus ante, turpis accusantium, ac maecenas deleniti,
        nisl leo sem integer ac dignissim. Lobortis etiam luctus lectus odio auctor. Justo vitae, felis integer id, bibendum accumsan turpis eu est mus eros, ante id eros.
      </div>
    </crowd-tab>

  </crowd-tabs>

  <crowd-input label="Input outside tabs" name="inputOutsideTab"></crowd-input>

  <short-instructions>
    <p>Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.</p>
</short-instructions>

<full-instructions header="Classification Instructions">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p> Tempus egestas sed sed risus.</p>
</full-instructions>

</crowd-form>

```

## Attributes

The following attributes are supported by this element.

### header

The text appearing on the tab. This is usually some short descriptive name indicative of
the information contained below the tab.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-tabs](sms-ui-template-crowd-tabs.md "sms-ui-template-crowd-tabs.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A container for tabbed information.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ZELYdWz "https://codepen.io/sagemaker_crowd_html_elements/pen/ZELYdWz").

The following is an example template that uses the `<crowd-tabs>` element. Copy
the following code and save it in a file with the extension `.html`. Open the file in
any browser to preview and interact with this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <crowd-tabs>
    <crowd-tab header="Tab 1">
      <h2>Image</h2>

      <img
        src="https://images.unsplash.com/photo-1478382188900-5bb598fe27d3?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1351&q=80"
        style="max-width: 40%"
      >

      <h2>Text</h2>
      <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </p>
      <p>
      Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.
      </p>
    </crowd-tab>

    <crowd-tab header="Tab 2">
      <h2>Description</h2>
      <p>
      Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.
      </p>
    </crowd-tab>

    <crowd-tab header="Tab 3">
      <div style="width: 40%; display: inline-block">
        <img
          src="https://images.unsplash.com/photo-1472747459646-91fd6f13995f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
          style="max-width: 80%"
        >
        <crowd-input label="Input inside tab" name="inputInsideTab"></crowd-input>
        <input type="checkbox" name="checkbox" value="foo">Foo
        <input type="checkbox" name="checkbox" value="bar">Bar
        <crowd-button>Some button</crowd-button>
      </div>

      <div style="width: 40%; display: inline-block; vertical-align: top">
        Lorem ipsum dolor sit amet, lorem a wisi nibh, in pulvinar, consequat praesent vestibulum tellus ante felis auctor, vitae lobortis dictumst mauris.
        Pellentesque nulla ipsum ante quisque quam augue.
        Class lacus id euismod, blandit tempor mauris quisque tortor mauris, urna gravida nullam pede libero, ut suscipit orci faucibus lacus varius ornare, pellentesque ipsum.
        At etiam suspendisse est elementum luctus netus, vel sem nulla sodales, potenti magna enim ipsum diam tortor rutrum,
        quam donec massa elit ac, nam adipiscing sed at leo ipsum consectetuer. Ac turpis amet wisi, porttitor sint lacus ante, turpis accusantium, ac maecenas deleniti,
        nisl leo sem integer ac dignissim. Lobortis etiam luctus lectus odio auctor. Justo vitae, felis integer id, bibendum accumsan turpis eu est mus eros, ante id eros.
      </div>
    </crowd-tab>

  </crowd-tabs>

  <crowd-input label="Input outside tabs" name="inputOutsideTab"></crowd-input>

  <short-instructions>
    <p>Sed risus ultricies tristique nulla aliquet enim tortor at auctor. Tempus egestas sed sed risus.</p>
</short-instructions>

<full-instructions header="Classification Instructions">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</p>
    <p> Tempus egestas sed sed risus.</p>
</full-instructions>

</crowd-form>

```

## Attributes

This element has no attributes.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: [crowd-tab](sms-ui-template-crowd-tab.md "sms-ui-template-crowd-tab.md")

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A field for text input.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ZELYdOz "https://codepen.io/sagemaker_crowd_html_elements/pen/ZELYdOz").

The following is an example of a Liquid template designed to transcribe audio clips that uses
the `<crowd-text-area>` element. Copy the following code and save it in a file with
the extension `.html`. Open the file in any browser to preview and interact with this
template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <audio controls>
      <source src="{{ task.input.taskObject | grant_read_access }}" type="audio/mpeg">
      Your browser does not support the audio element.
  </audio>
  <h3>Instructions</h3>
  <p>Transcribe the audio</p>
  <p>Ignore "umms", "hmms", "uhs" and other non-textual phrases</p>
  <crowd-text-area name="transcription" rows="4"></crowd-text-area>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### allowed-pattern

A regular expression that is used with the _auto-validate_ attribute to
ignore non-matching characters as the worker types.

### auto-focus

A Boolean switch that, if present, puts the cursor in this element on-load so that users can immediately begin typing without having to click inside the element.

### auto-validate

A Boolean switch that, if present, turns on input validation. The behavior of the validator
can be modified by the _error-message_ and
_allowed-pattern_ attributes.

### char-counter

A Boolean switch that, if present, puts a small text field beneath the lower-right corner of the element, displaying the number of characters inside the element.

### disabled

A Boolean switch that, if present, displays the input area as disabled.

### error-message

The text to be displayed below the input field, on the left side, if validation
fails.

### label

A string that is displayed inside a text field.

This text shrinks and rises up above a text field when the worker starts typing in the
field or when the _value_ attribute is set.

### max-length

An integer that specifies the maximum number of characters allowed by the element. Characters typed or pasted beyond the maximum are ignored.

### max-rows

An integer that specifies the maximum number of rows of text that are allowed within a
crowd-text-area. Normally the element expands to accommodate new rows. If this is set, after
the number of rows exceeds it, content scrolls upward out of view and a scrollbar control
appears.

### name

A string used to represent the element's data in the output.

### placeholder

A string presented to the user as placeholder text. It disappears after the user puts
something in the input area.

### rows

An integer that specifies the height of the element in rows of text.

### value

A preset that becomes the default if the worker does not provide input. The preset appears
in a text field.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## Output

This element outputs the `name` as a property name and the element's text contents as the value. Carriage returns in the text are represented as `\n`.

###### Example Sample output for this element

```
[
  {
    "textInput1": "This is the text; the text that\nmakes the crowd go wild."
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A subtle notification that temporarily appears on the display. Only one crowd-toast is
visible.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaBgK "https://codepen.io/sagemaker_crowd_html_elements/pen/ExZaBgK").

The following is an example of a Liquid template that uses the `<crowd-toast>`
element. Copy the following code and save it in a file with the extension `.html`. Open
the file in any browser to preview and interact with this template.

```


<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <p>Find the official website for: <strong>{{ task.input.company }}</strong></p>
  <p>Do not give Yelp pages, LinkedIn pages, etc.</p>
  <p>Include the http:// prefix from the website</p>
  <crowd-input name="website" placeholder="http://example.com"></crowd-input>

  <crowd-toast duration="10000" opened>
    This is a message that you want users to see when opening the template. This message will disappear in 10 seconds.
   </crowd-toast>

</crowd-form>

```

## Attributes

The following attributes are supported by this element.

### duration

A number that specifies the duration, in milliseconds, that the notification appears on the
screen.

### text

The text to display in the notification.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

A button that acts as an ON/OFF switch, toggling a state.

See an interactive example of an HTML template that uses this Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJLNm "https://codepen.io/sagemaker_crowd_html_elements/pen/XWpJLNm").

The following example shows different ways you can use to use the
`<crowd-toggle-button>` HTML element. Copy the following code and save it in a file
with the extension `.html`. Open the file in any browser to preview and interact with
this template.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>

<crowd-form>
  <!--Toggle button without value-->
  <crowd-toggle-button name="toggleButtonWithoutValue"></crowd-toggle-button>

  <!--Toggle button with value-->
  <crowd-toggle-button name="toggleButtonWithValue" value="someValue"></crowd-toggle-button>

  <!--Toggle button disabled-->
  <crowd-toggle-button name="toggleButtonDisabled" disabled></crowd-toggle-button>

  <!--Toggle button marked invalid-->
  <crowd-toggle-button name="toggleButtonInvalid" invalid></crowd-toggle-button>

  <!--Toggle button marked required-->
  <crowd-toggle-button name="toggleButtonRequired" required></crowd-toggle-button>
</crowd-form>
```

## Attributes

The following attributes are supported by this element.

### checked

A Boolean switch that, if present, displays the button switched to the ON position.

### disabled

A Boolean switch that, if present, displays the button as disabled and prevents toggling.

### invalid

When in an off position, a button using this attribute, will display in an alert color. The standard is red, but may be changed in CSS. When toggled on, the button will display in the same color as other buttons in the on position.

### name

A string that is used to identify the answer submitted by the worker. This value matches a
key in the JSON object that specifies the answer.

### required

A Boolean switch that, if present, requires the worker to provide input.

### value

A value used in the output as the property name for the element's Boolean state. Defaults to "on" if not provided.

## Element Hierarchy

This element has the following parent and child elements.

- Parent elements: [crowd-form](sms-ui-template-crowd-form.md "sms-ui-template-crowd-form.md")
- Child elements: none

## Output

This element outputs the `name` as the name of an object, containing the
`value` as a property name and the element's state as Boolean value for the property.
If no value for the element is specified, the property name defaults to "on."

###### Example Sample output for this element

```
[
  {
    "theToggler": {
      "on": true
    }
  }
]
```

## See Also

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")

## Crowd HTML Elements V2

Crowd HTML V2 Elements introduce enhanced labeling capabilities designed to support workers,
with new features tailored for GenAI model training use cases. These
V2 elements are compatible with the Crowd HTML Elements
crowd-form, short-instructions, crowd-button, crowd-tabs, and crowd-tab. If you use other elements
with V2 elements, the annotation application won't work properly.

A widget for workers to slide and rank various text inputs based on dimensions that you specify.

See an interactive example of an HTML template that uses this Crowd HTML Element
in [CodePen](https://codepen.io/sagemaker_crowd_html_elements_2/pen/ZYGqBPQ "https://codepen.io/sagemaker_crowd_html_elements_2/pen/ZYGqBPQ").

```
<script src="https://assets.crowd.aws/crowd-html-elements-v2.js"></script>

<crowd-form>
  <crowd-text-ranking
    name="textRanking"
    ordinal-ranking-dimensions='[{"name":"Clarity","allowTie":true},{"name":"Inclusivity","allowTie":false}]'
    text="Explain why you can see yourself in a mirror at a level that a 16 year old can understand."
    responses='["When light is emitted from light source like a light bulb, some of it travels toward your body, where it may be reflected toward the mirror with some probability or it may be absorbed. If it were reflected off your body, then some of it could travel toward the mirror, where it could be reflected again. If it is the case where light strikes the mirror, the light is then again redirected as a reflection. If that light is pointed in the direction of your eyes, then the light will enter your eyes. Then, your brain processes the electrical signal made by your eyes and sees it as an image.","You can see yourself because of a series of light reflections. Light travels from the light source, hits and reflects off of your body and travels toward the mirror. Then, it reflects off of the mirror and travels to your eyes, where your brain registers it as a picture of yourself.","Light travels in various directions from a light source like a light bulb. Some of the light reflects off of your body with some probability, after which some of it travels to the mirror. Upon striking the mirror, the some of the light again reflects off the mirror and travels toward your eyes, wherein your eyes detect the light after absorbing it. After this process, your brain processes the signal as an image of yourself.","The phenomenon of self-visual perception via a mirror at an ontological plane derives from the intricate interplay of photons within the electromagnetic spectrum, quantum mechanical principles, and the neurocognitive processes underpinning self-recognition. In essence, the mirror serves as an interface wherein incident photons, emitted from an external object, interact with the reflective surface at a specific angle of incidence governed by the laws of geometric optics. This interaction culminates in the process of specular reflection, leading to the formation of a virtual image."]'
  >
    <short-instructions>
      <h1>Hello these are my instructions 1</h1>
      <p>Hello these are my instructions 2</p>
      <p>Hello these are my instructions 3</p>
    </short-instructions>
  </crowd-text-ranking>
</crowd-form>
```

#### Attributes

The following are attributes supported by this element.

##### text

The text or S3 reference to the text to reference when ranking the responses.

##### ordinal-ranking-dimensions

A required array of the `ordinal-ranking-dimensions` object, which specify the dimension on which to rank the responses.
This dimension contains a **name** and a property named **allowTie**, which determines whether
a worker can give responses the same ranking.

##### responses

A required array of the `ordinal-ranking-dimensions` object, which specify the dimension on which to rank the responses.
This dimension contains a **name** and a property named **allowTie**, which determines whether
a worker can give responses the same ranking.

##### name

A required string field that identifies the answer submitted that the worker submits. It matches a key in the output data contract of the worker submission.

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")
  A widget for workers to highlight sections of text and assign question and answer pairs based on your instructions

See an interactive example of an HTML template that uses this
Crowd HTML Element in [CodePen](https://codepen.io/sagemaker_crowd_html_elements_2/pen/zxGmobo "https://codepen.io/sagemaker_crowd_html_elements_2/pen/zxGmobo").

```
<script src="https://assets.crowd.aws/crowd-html-elements-v2.js"></script>

<crowd-form>
  <crowd-question-answer-generation
    name="questionAnswerGeneration"
    text='The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne; Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is a moist broadleaf forest that covers most of the Amazon basin of South America. This basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes territory belonging to nine nations. The majority of the forest is contained within Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French Guiana. States or departments in four nations contain "Amazonas" in their names. The Amazon represents over half of the planet's remaining rainforests, and comprises the largest and most biodiverse tract of tropical rainforest
    in the world, with an estimated 390 billion individual trees divided into 16,000 species. For a long time, it was thought that the
    Amazon rainforest was only ever sparsely populated, as it was impossible to sustain a large population through agriculture given the poor soil.
    Archeologist Betty Meggers was a prominent proponent of this idea, as described in her book Amazonia: Man and Culture in a Counterfeit Paradise.
    She claimed that a population density of 0.2 inhabitants per square kilometre (0.52/sq mi) is the maximum that can be sustained in the rainforest
    through hunting, with agriculture needed to host a larger population. However, recent anthropological findings have suggested that the region was
    actually densely populated. Some 5 million people may have lived in the Amazon region in AD 1500, divided between dense coastal settlements, such as that at
    Marajó, and inland dwellers. By 1900 the population had fallen to 1 million and by the early 1980s it was less than 200,000.'
    min-questions="1"
    max-questions="10"
    question-min-words="1"
    question-max-words="100"
    answer-min-words="1"
    answer-max-words="100"
    question-tags='[
      "tag1",
      "tag2",
      "tag3"
    ]'
    allow-custom-question-tags="true"
  >
    <short-instructions>
      <p>User instructions will be displayed here.</p>
    </short-instructions>
  </crowd-question-answer-generation>
</crowd-form>
```

#### Attributes

The following are attributes supported by this element.

##### text

The text or S3 reference to the text to reference when ranking the responses.

##### min-questions

Optional integer that specifies the minimum amount of questions that a worker would have to create during the task. If not provided,
you will be asked to write at least one question and answer pair.

##### max-questions

Optional integer that specifies the maximum amount of questions a worker can create during the task.

##### question-min-words

Optional integer that specifies the minimum amount of words allowed in an question. If not provided, you will be asked to provide at least one word in the question.

##### question-max-words

Optional integer that specifies the maximum amount of words allowed in an question.

##### answer-min-words

Optional integer that specifies the minimum amount of words allowed in an answer. If not provided, you will be asked to write at least one word in the answer.

##### answer-max-words

Optional integer that specifies the maximum amount of words allowed in an answer.

##### question-tags

A required array of strings that specifies the possible tags a worker can assign to a question-answer pair. If this array is empty, then question-tags field isn't visible.

##### allow-custom-question-tags

Required Boolean field that indicates whether a worker can specify a custom question tag.

##### name

A required string field that identifies the answer submitted that the worker submits. It matches a key in the output data contract of the worker submission.

For more information, see the following.

- [Training data labeling using humans with Amazon SageMaker Ground Truth](sms.md "sms.md")
- [Crowd HTML Elements Reference](sms-ui-template-reference.md "sms-ui-template-reference.md")
