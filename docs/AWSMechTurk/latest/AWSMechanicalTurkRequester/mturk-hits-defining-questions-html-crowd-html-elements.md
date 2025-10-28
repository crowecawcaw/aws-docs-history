# Crowd HTML

Elements

[Crowd HTML Elements](../AWSMturkAPI/ApiReference_HTMLCustomElementsArticle.md "../AWSMturkAPI/ApiReference_HTMLCustomElementsArticle.md") are web components, a web standard that abstracts HTML
markup, CSS, and JavaScript functionality into an HTML tag or set of tags. This allows you
to build powerful task interfaces more easily.

To use Crowd HTML Elements you must include the following in your task HTML.

```

<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
 

```

This imports the library and gives you access to all of the elements. You can then
replace the `form` element in your HTML with the `crowd-form`
element as shown below. In this example, we have the same task interface as the one
described in the previous section, but the HTML is simplified because the
`crowd-form` element encapsulates the necessary code to direct where the
response will be submitted, includes the `assignmentId`, and automatically adds
a **Submit** button if it's not present.

```

<!DOCTYPE html>
<script src="https://assets.crowd.aws/crowd-html-elements.js"></script>
<crowd-form>
  <p>Describe the current weather where you live</p>
  <p><textarea name="weather" cols="80" rows="3"></textarea></p>
</crowd-form>
 

```

Crowd HTML Elements includes a range of elements ranging from wrappers for common form
elements such as text fields and check boxes (`crowd-input` and
`crowd-checkbox`), to full task interfaces for tasks such as drawing bounding
boxes on images (`crowd-bounding-box`) and text entity annotation
(`crowd-entity-annotation`).

For a full list of the available elements, see the [Crowd HTML Elements Reference](../../../sagemaker/latest/dg/sms-ui-template-reference.md "../../../sagemaker/latest/dg/sms-ui-template-reference.md").
