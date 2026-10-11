

# Custom views in Connect Customer
<a name="view-resources-custom-view"></a>

You can create your own views with Connect Customer APIs. Views support AWS CloudFormation, AWS CloudTrail, and tagging.

## Views API example
<a name="view-resources-custom-view-example"></a>

This view nests two cards within a container and places a **Skip** button to their right.

The following command creates the view:

```
aws connect create-view --name CustomerManagedCards \
--status PUBLISHED --content file://view-content.json \
--instance-id $INSTANCE_ID --region $REGION
```

The `view-content.json` file contains the following:

```
{
  "Template": <stringified-template-json>
  "Actions": ["CardSelected", "Skip"]
}
```

The following is the template JSON before it's stringified:

```
{
    "Head": {
        "Title": "CustomerManagedCards",
        "Configuration": {
            "Layout": {
                "Columns": ["10", "2"] // Default column width for each component is 12, which is also the width of the entire view.
            }
        }
    },
    "Body": [
        {
            "_id": "card-container",
            "Type": "Container",
            "Props": {},
            "Content": [
                {
                    "_id": "cafe_card",
                    "Type": "Card",
                    "Props": {
                        
                        "Id": "cafe-card",
                        "Heading": "Cafe Card",
                        "Icon": "Cafe",
                        "Status": "Status Field",
                        "Description": "This is the cafe card.",
                        "Action": "CardSelected" // Note that these actions also appear in the view-content.json file.
                          
                    },
                    "Content": []
                },
                {
                    "_id": "no_icon_card",
                    "Type": "Card",
                    "Props": {
                        "Id": "NoIconCard",
                        "Heading": "$.NoIconCardHeading",
                        "Status": "Status Field",
                        "Description": "This is the icon card.",
                        "Action": "CardSelected" // Note that these actions also appear in the view-content.json file.
                    },
                    "Content": []
                }
            ]
        },
        {
            "_id": "button",
            "Type": "Button",
            "Props": { "Action": "Skip" }, // Note that these actions also appear in the view-content.json file.
            "Content": ["Skip"]
        }
    ]
}
```

## How the view renders
<a name="view-resources-custom-the-view"></a>

`$.NoIconCardHeading` indicates that an input for the field `NoIconCardHeading` is necessary to render the view.

Let's say `NoIconCardHeading` is set to `No Icon Card`.

The view renders as follows:

![Two cards in a container, with a Skip button to their right.](https://docs.aws.amazon.com/connect/latest/adminguide/images/view-resources-custom-the-view.png)


## View output example
<a name="view-resources-custom-view-output-example"></a>

A view returns two pieces of data: the `Action` taken, and the `Output` data.

When using a view with the [Show view](show-view-block.md) block, `Action` represents a branch, and `Output` data is set to the `$.Views.ViewResultData` flow attribute.

**Scenario 1: Choose the **Cafe Card** Card**

```
"Action": "CardSelected"
"Output": {
    "Heading": "CafeCard",
    "Id": "CafeCard"
}
```

**Scenario 2: Choose the **Skip** Button**

```
"Action": "Skip"
"Output": {
    "action": "Button"
}
```

## Form view output example
<a name="view-resources-custom-form-view-output-example"></a>

When using the AWS managed Form view, the form data is under `FormData`.

```
{
   "FormData": {
       "email": "user@example.com"
   }
}
```

In the Show view block, reference the data as `$.Views.ViewResultData.FormData.email`.

When using the **Custom view (with form component)**, the form data is directly under `Output`.

```
{
    "email": "user@example.com"
}
```

In the Show view block, reference the data as `$.Views.ViewResultData.email`.