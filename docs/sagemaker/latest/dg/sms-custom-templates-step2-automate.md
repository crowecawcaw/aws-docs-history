# Adding automation with Liquid

Our custom template system uses [Liquid](https://shopify.github.io/liquid/ "https://shopify.github.io/liquid/") for automation. It is an open source inline markup language. In Liquid, the text between single curly braces and percent symbols is an instruction or _tag_ that performs an operation like control flow or iteration. Text between double curly braces is a variable or _object_ that outputs its value.

The most common use of Liquid will be to parse the data coming from your input manifest file, and pull out the relevant variables to create the task. Ground Truth automatically generates the tasks unless a pre-annotation Lambda is specified. The `taskInput` object returned by Ground Truth or your [Pre-annotation Lambda](sms-custom-templates-step3-lambda-requirements.md#sms-custom-templates-step3-prelambda "sms-custom-templates-step3-lambda-requirements.md#sms-custom-templates-step3-prelambda") is the `task.input` object in your templates.

The properties in your input manifest are passed into your template as the `event.dataObject`.

###### Example manifest data object

```
{
  "source": "This is a sample text for classification",
  "labels": [ "angry" , "sad" , "happy" , "inconclusive" ],
  "header": "What emotion is the speaker feeling?"
}
```

###### Example sample HTML using variables

```
<crowd-classifier
  name='tweetFeeling'
  categories='{{ task.input.labels | to_json }}'
  header='{{ task.input.header }}' >
<classification-target>
  {{ task.input.source }}
</classification-target>
```

Note the addition of `| to_json` to the `labels` property above. That is a filter that turns the input manifest array into a JSON representation of the array. Variable filters are explained in the next section.

The following list includes two types of Liquid tags that you may find useful to
automate template input data processing. If you select one of the following
tag-types, you will be redirected to the Liquid documentation.

- [Control
  flow](https://shopify.github.io/liquid/tags/control-flow/ "https://shopify.github.io/liquid/tags/control-flow/"): Includes programming logic operators like
  `if/else`, `unless`, and
  `case/when`.
- [Iteration](https://shopify.github.io/liquid/tags/iteration/ "https://shopify.github.io/liquid/tags/iteration/"): Enables you to run blocks of code repeatedly using
  statements like for loops.

For an example of an HTML template that uses Liquid elements to create a
for loop, see [translation-review-and-correction.liquid.html](https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/8ae02533ea5a91087561b1daecd0bc22a37ca393/text/translation-review-and-correction.liquid.html "https://github.com/aws-samples/amazon-sagemaker-ground-truth-task-uis/blob/8ae02533ea5a91087561b1daecd0bc22a37ca393/text/translation-review-and-correction.liquid.html") in GitHub.
For more information and documentation, visit the [Liquid homepage](https://shopify.github.io/liquid/ "https://shopify.github.io/liquid/").

## Variable filters

In addition to the standard [Liquid filters](https://shopify.github.io/liquid/filters/abs/ "https://shopify.github.io/liquid/filters/abs/") and actions, Ground Truth offers a few additional filters. Filters are applied by placing a pipe (`|`) character after the variable name, then specifying a filter name. Filters can be chained in the form of:

###### Example

```
{{ <content> | <filter> | <filter> }}
```

### Autoescape and explicit escape

By default, inputs will be HTML escaped to prevent confusion between your variable text and HTML. You can explicitly add the `escape` filter to make it more obvious to someone reading the source of your template that the escaping is being done.

### escape_once

`escape_once` ensures that if you've already escaped your code, it doesn't get re-escaped on top of that. For example, so that &amp; doesn't become &amp;amp;.

### skip_autoescape

`skip_autoescape` is useful when your content is meant to be used as HTML. For example, you might have a few paragraphs of text and some images in the full instructions for a bounding box.

###### Use skip_autoescape sparingly

The best practice in templates is to avoid passing in functional code or markup with `skip_autoescape` unless you are absolutely sure you have strict control over what's being passed. If you're passing user input, you could be opening your workers up to a Cross Site Scripting attack.

### to_json

`to_json` will encode what you feed it to JSON (JavaScript Object Notation). If you feed it an object, it will serialize it.

### grant_read_access

`grant_read_access` takes an S3 URI and encodes it into an HTTPS URL with a short-lived access token for that resource. This makes it possible to display to workers the photo, audio, or video objects stored in S3 buckets that are not otherwise publicly accessible.

### s3_presign

The `s3_presign` filter works the same way as the `grant_read_access` filter. `s3_presign` takes an Amazon S3 URI and encodes it into an HTTPS URL with a short-lived access token for that resource. This makes it possible to display photo, audio, or video objects stored in S3 buckets that are not otherwise publicly accessible to workers.

###### Example of the variable filters

Input

```
auto-escape: {{ "Have you read 'James & the Giant Peach'?" }}
explicit escape: {{ "Have you read 'James & the Giant Peach'?" | escape }}
explicit escape_once: {{ "Have you read 'James &amp; the Giant Peach'?" | escape_once }}
skip_autoescape: {{ "Have you read 'James & the Giant Peach'?" | skip_autoescape }}
to_json: {{ jsObject | to_json }}
grant_read_access: {{ "s3://amzn-s3-demo-bucket/myphoto.png" | grant_read_access }}
s3_presign: {{ "s3://amzn-s3-demo-bucket/myphoto.png" | s3_presign }}
```

###### Example

Output

```
auto-escape: Have you read &#39;James &amp; the Giant Peach&#39;?
explicit escape: Have you read &#39;James &amp; the Giant Peach&#39;?
explicit escape_once: Have you read &#39;James &amp; the Giant Peach&#39;?
skip_autoescape: Have you read 'James & the Giant Peach'?
to_json: { "point_number": 8, "coords": [ 59, 76 ] }
grant_read_access: https://s3.amazonaws.com/amzn-s3-demo-bucket/myphoto.png?`<access token and other params>`
s3_presign: https://s3.amazonaws.com/amzn-s3-demo-bucket/myphoto.png?`<access token and other params>`
```

###### Example of an automated classification template.

To automate the simple text classification sample, replace the tweet text with a variable.

The text classification template is below with automation added. The changes/additions are highlighted in bold.

```
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
  <crowd-classifier
    name="tweetFeeling"
    categories="['positive', 'negative', 'neutral', 'cannot determine']"
    header="Which term best describes this tweet?"
  >
    <classification-target>
       **{{ task.input.source }}**
    </classification-target>

    <full-instructions header="Analyzing a sentiment">
      Try to determine the feeling the author
      of the tweet is trying to express.
      If none seem to match, choose "other."
    </full-instructions>

    <short-instructions>
      Pick the term best describing the sentiment
      of the tweet.
    </short-instructions>

  </crowd-classifier>
</crowd-form>

```

The tweet text in the prior sample is now replaced with an object. The `entry.taskInput` object uses `source` (or another name you specify in your pre-annotation Lambda) as the property name for the text, and it is inserted directly in the HTML by virtue of being between double curly braces.
