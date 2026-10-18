

# Display contact information in the agent workspace when a contact begins
<a name="display-contact-attributes-sg"></a>

A step-by-step guide can show contact attributes to the agent when a contact starts. This gives agents the context they need before the conversation begins. This pattern is also called a screen pop.

To show contact attributes, configure a **Detail view**, an [AWS managed view](view-resources-managed-view.md).

The **Detail view** shows information and a list of actions the user can take. For example, use it for a screen pop at the start of a call.
+ Actions can move the user to the next step in a step-by-step guide or start a new workflow.
+ `Sections`, the body of the page, is the only required component.
+ The view also supports optional components, such as `AttributeBar`.

**Tip**  
For interactive documentation that shows a preview of a **Detail view**, see [Detail](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-detail--with-all).

The following image shows an example of a **Detail view**. It has a page heading, description, and four examples.

![The Detail view, with the page heading, description, and four examples with attributes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/details-view-page-heading-sq.png)


**Sections**
+ Content can be a static string, a TemplateString, or a key-value pair. It can be a single data point or a list. For more information, see [TemplateString](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#templatestring) or [AttributeSection](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute-section).

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ A list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, an agent can navigate to a new browser page, which is configured with `Url`.
    + When it's `case`, the link opens the case that `ResourceId` identifies in the agent workspace.
  + `Copyable` lets users copy the `ResourceId` by choosing it.

**Back (Optional)**
+ Optional, but required if the view has no actions. If provided, displays the back navigation link.
+ Is an object with a *Label* which will control what is displayed in the link text.

**Heading (Optional)**
+ Optional. If provided, displays Text as the title.

**Description (Optional)**
+ Optional. If provided, displays description text under the title.

**Actions (Optional)**
+ Optional. If provided, displays a list of actions at the bottom of the page.

**Input example**

```
{
  "AttributeBar": [
    {"Label": "Example", "Value": "Attribute"},
    { "Label": "Example 2", "Value": "Attribute 3", "LinkType": "case", "ResourceId": "123456", "Copyable": true }
  ],
  "Back": {
    "Label": "Back"
  },
  "Heading": "Hello world",
  "Description": "This is a detail page",
  "Sections": [{
    "TemplateString": "This is an intro paragraph"
  }, "abc"],
  "Actions": ["Do thing!", "Update thing 2!"]
}
```

**Output example**

```
{
    "Action": "ActionSelected",
    "ViewResultData": {
        "actionName": "Do thing!"
    }
}
```