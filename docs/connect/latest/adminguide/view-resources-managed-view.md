

# Set up AWS managed views in Connect Customer
<a name="view-resources-managed-view"></a>

Connect Customer includes a set of AWS managed views. Choose a tab to see how to configure each one.

------
#### [ Detail view ]

The **Detail view** shows information and a list of actions the user can take. For example, use it for a screen pop at the start of a call.
+ Actions can move the user to the next step in a step-by-step guide or start a new workflow.
+ `Sections`, the body of the page, is the only required component.
+ The view also supports optional components, such as `AttributeBar`.

For an interactive example, see the [Detail view](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-detail--with-all) in the UI component reference.

The following image shows an example of a **Detail view**. It has a page heading, description, and four examples.

![The detail view, with the page heading, description, and four examples with attributes.](https://docs.aws.amazon.com/connect/latest/adminguide/images/details-view-page-heading-sq.png)


**Sections**
+ Content can be a static string, a TemplateString, or a key-value pair. It can be a single data point or a list. For more information, see [TemplateString](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#templatestring) or [AttributeSection](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute-section).

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ Is a list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, a user can navigate to a new browser page, which is configured with `Url`.
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

------
#### [ List view ]

The **List view** shows a list of items, each with a heading and description. Items can also be links with actions attached. The view can also show a back link and an attribute bar.

For an interactive example, see the [List view](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-list--with-all) in the UI component reference.

The following image shows an example of a List view. It has one column with three items in it.

![The List view, one list item with link, and two items without links.](https://docs.aws.amazon.com/connect/latest/adminguide/images/list-view-column-sq.png)


**Items**
+ Required. Displays these items as a list.
+ Each item can have a `Heading`, `Description`, `Icon`, and `Id`.
  + All properties are optional.
  + When you define `Id`, the output includes its value.

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ Is a list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, a user can navigate to a new browser page, which is configured with `Url`.
    + When it's `case`, the link opens the case that `ResourceId` identifies in the agent workspace.
  + `Copyable` lets users copy the `ResourceId` by choosing it.

**Back (Optional)**
+ Optional, but required if the view has no actions. If provided, displays the back navigation link.
+ Is an object with a *Label* which will control what is displayed in the link text.

**Heading (Optional)**
+ Optional. If provided, displays Text as the title.

**SubHeading (Optional)**
+ Optional. If provided, displays Text as the list title.

**Input data example**

```
{
    "AttributeBar": [
        { "Label": "Example", "Value": "Attribute" },
        { "Label": "Example 2", "Value": "Attribute 2" },
    { "Label": "Example 3", "Value": "Attribute 3", "LinkType": "external", "Url": "https://www.example.com" }
    ],
    "Back": {
        "Label": "Back"
    },
    "Heading": "José may be contacting about...",
    "SubHeading": "Optional List Title",
    "Items": [
        {
            "Heading": "List item with link",
            "Description": "Optional description here with no character limit.",
            "Icon": "School",
            "Id": "Select_Car"
        },
        {
            "Heading": "List item not a link",
            "Icon": "School",
            "Description": "Optional description here with no character limit."
        },
        {
            "Heading": "List item not a link and no image",
            "Description": "Optional description here with no character limit."
       },
        {
            "Heading": "List item no image and with link",
            "Description": "Optional description here with no character limit.",
            "Id": "Select_Item"
        }
    ]
}
```

**Output data example**

```
{
    "Action": "ActionSelected",
    "ViewResultData": {
        "actionName": "Select_Car"
    }
}
```

------
#### [ Form view ]

With the **Form view**, you can give users input fields to gather data and submit it to backend systems. The view has one or more sections, each with a header. Each section holds input fields in a column or grid layout.

For an interactive example, see the [Form view](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-form--with-all) in the UI component reference.

The following image shows an example of a Form view for a car rental reservation. It has location and date fields on it.

![The form view with location and date fields as examples.](https://docs.aws.amazon.com/connect/latest/adminguide/images/form-view-sq.png)


**Sections**
+ Holds the view's input and display fields.
+ **SectionProps**
  + **Heading**
    + Heading of the section
  + **Type**
    + Type of section
    + `FormSection`, for user input, or `DataSection`, for a list of labels and values.
  + **Items**
    + List of data based on the type. When `Type` is `DataSection`, the data should be attributes. If the `Type` is `FormSection`, the data should be form components.
  + **isEditable**
    + When the section type is `DataSection`, shows an Edit button in the header.
    + Boolean

**Wizard (Optional)**
+ Displays a `ProgressTracker` on the left side of the view.
+ Each item can have a `Heading`, `Description`, and `Optional` property. `Heading` is required.

**Back (Optional)**
+ An object or a string. Its `Label` sets the link text.

**Next (Optional)**
+ Appears on every step except the last.
+ An object (`FormActionProps`) or a string. For more information, see [FormActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**Cancel (Optional)**
+ This action is used when the step is not the first step.
+ An object (`FormActionProps`) or a string. For more information, see [FormActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**Previous (Optional)**
+ Appears on every step except the first.
+ An object (`FormActionProps`) or a string. For more information, see [FormActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**Edit (Optional)**
+ This action is shown when the section type is `DataSection`.
+ An object (`FormActionProps`) or a string. For more information, see [FormActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ Is a list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, a user can navigate to a new browser page, which is configured with `Url`.
    + When it's `case`, the link opens the case that `ResourceId` identifies in the agent workspace.
  + `Copyable` lets users copy the `ResourceId` by choosing it.

**Heading (Optional)**
+ String that displays as the page title.

**SubHeading (Optional)**
+ Secondary message for the page.

**ErrorText (Optional)**
+ Optional. Shows server-side error messages.
+ An object (`ErrorProps`) or a string.

**Input data example**

```
{
    "AttributeBar": [{
            "Label": "Queue",
            "Value": "Sales"
        },
        {
            "Label": "Case ID",
            "Value": "1234567"
        },
        {
            "Label": "Case",
            "Value": "New reservation"
        },
        {
            "Label": "Attribute 3",
            "Value": "Attribute"
        }
    ],
    "Back": {
        "Label": "Back Home"
    },
    "Next": {
        "Label": "Confirm Reservation",
        "Details": {
            "endpoint": "example.com/submit"
        }
    },
    "Cancel": {
        "Label": "Cancel"
    },
    "Heading": "Modify Reservation",
    "SubHeading": "Cadillac XT5",
    "ErrorText": {
        "Header": "Modify reservation failed",
        "Content": "Internal Server Error, please try again"
    },
    "Sections": [{
        "_id": "pickup",
        "Type": "FormSection",
        "Heading": "Pickup Details",
        "Items": [{
            "LayoutConfiguration": {
                "Grid": [{
                    "colspan": {
                        "default": "12",
                        "xs": "6"
                    }
                }]
            },
            "Items": [{
                "Type": "FormInput",
                "Fluid": true,
                "InputType": "text",
                "Label": "Location",
                "Name": "pickup-location",
                "DefaultValue": "Seattle"
            }]
        }, {
            "LayoutConfiguration": {
                "Grid": [{
                    "colspan": {
                        "default": "6",
                        "xs": "4"
                    }
                }, {
                    "colspan": {
                        "default": "6",
                        "xs": "4"
                    }
                }]
            },
            "Items": [{
                "Label": "Day",
                "Type": "DatePicker",
                "Fluid": true,
                "DefaultValue": "2022-10-10",
                "Name": "pickup-day"
            }, {
                "Label": "Time",
                "Type": "TimeInput",
                "Fluid": true,
                "DefaultValue": "13:00",
                "Name": "pickup-time"
            }]
        }]
    }, {
        "_id": "dropoff",
        "Heading": "Drop off details",
        "Type": "FormSection",
        "Items": [{
            "LayoutConfiguration": {
                "Grid": [{
                    "colspan": {
                        "default": "12",
                        "xs": "6"
                    }
                }]
            },
            "Items": [{
                "Label": "Location",
                "Type": "FormInput",
                "Fluid": true,
                "DefaultValue": "Lynnwood",
                "Name": "dropoff-location"
            }]
        }, {
            "LayoutConfiguration": {
                "Grid": [{
                    "colspan": {
                        "default": "6",
                        "xs": "4"
                    }
                }, {
                    "colspan": {
                        "default": "6",
                        "xs": "4"
                    }
                }]
            },
            "Items": [{
                "Label": "Day",
                "Type": "DatePicker",
                "Fluid": true,
                "DefaultValue": "2022-10-15",
                "Name": "dropoff-day"
            }, {
                "Label": "Time",
                "Type": "TimeInput",
                "Fluid": true,
                "DefaultValue": "01:00",
                "Name": "dropoff-time"
            }]
        }]
    }]
}
```

**Output data example**

```
{
    "Action": "Submit",
    "ViewResultData": { 
        FormData: {
            "dropoff-day": "2022-10-15",
            "dropoff-location": "Lynnwood",
            "dropoff-time": "01:00",
            "pickup-day": "2022-10-10",
            "pickup-location": "Seattle",
            "pickup-time": "13:00"
        },
       "StepName": "Pickup and drop off"
    }
}
```

------
#### [ Confirmation view ]

The **Confirmation view** shows users a page after they submit a form or complete an action. You can use it to summarize what happened, list next steps, and prompt the user. The **Confirmation view** supports an attribute bar, a graphic, a heading, a subheading, and a Next button.

For an interactive example, see the [Confirmation view](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-confirmation--with-all) in the UI component reference.

The following image shows an example of a Confirmation view.

![The confirmation view, a check mark and text to confirm the car rental.](https://docs.aws.amazon.com/connect/latest/adminguide/images/confirmation-view-check-sq.png)


**Next**
+ Required.
+ The button that moves the user to the next step.
  + `Label`: the button text.

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ Is a list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, a user can navigate to a new browser page, which is configured with `Url`.
    + When it's `case`, the link opens the case that `ResourceId` identifies in the agent workspace.
  + `Copyable` lets users copy the `ResourceId` by choosing it.

**Heading (Optional)**
+ String that displays as the page title.

**SubHeading (Optional)**
+ Secondary message for the page.

**Graphic (Optional)**
+ Displays an image.
+ Object with the following key:
  + `Include`: a Boolean. When `true`, the page shows the graphic.

**Input data example**

```
{
  "AttributeBar": [
    { "Label": "Attribute1", "Value": "Value1" },
    { "Label": "Attribute2", "Value": "Value2" },
    { "Label": "Attribute3", "Value": "Amazon", "LinkType": "external", "Url": "https://www.example.com" }
  ],
  "Next": {
    "Label": "Go Home"
  },
  "Graphic": {
    "Include": true
  },
  "Heading": "I have updated your car rental reservation for pickup on July 22.",
  "SubHeading": "You will be receiving a confirmation shortly. Is there anything else I can help with today?"
}
```

**Output data example**

```
{
    "Action": "Next",
    "ViewResultData": {
        "actionName": "Next",
        "Label": "Go Home"
    }
}
```

------
#### [ Cards view ]

With the **Cards view**, you can show users a list of topics to choose from, such as when an agent accepts a contact.

For an interactive example, see the [Cards view](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-cards--with-all) in the UI component reference.

The following image shows six cards: one to make a new reservation, and the others to review reservations for upcoming trips.

![A set of six cards.](https://docs.aws.amazon.com/connect/latest/adminguide/images/solve-view-sq.png)


When a user chooses a card, it opens to show more detail. The following image shows an open card for a reservation.

![An open card that shows details for a reservation.](https://docs.aws.amazon.com/connect/latest/adminguide/images/card-view-sq.png)


**Sections**
+ Required. A list of objects, each with a `Summary` and a `Detail`.
+ For more information, see [Summary and Detail](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-cards--with-all).

**AttributeBar (Optional)**
+ Optional. If provided, displays the Attribute bar at the top of the view.
+ Is a list of objects with required properties, `Label`, `Value`, and optional properties `LinkType`, `ResourceId`, `Copyable` and `Url`. For more information, see [Attribute](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#attribute).
  + `LinkType` can be `external` or a Connect Customer application, such as `case`.
    + When it is *external*, a user can navigate to a new browser page, which is configured with `Url`.
    + When it's `case`, the link opens the case that `ResourceId` identifies in the agent workspace.
  + `Copyable` lets users copy the `ResourceId` by choosing it.

**Heading (Optional)**
+ String that displays as the page title.

**Back (Optional)**
+ An object or a string. Its `Label` sets the link text. For more information, see [ActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**NoMatchFound (Optional)**
+ Text for a button below the cards. For more information, see [ActionProps](https://d3irlmavjxd3d8.cloudfront.net/?path=/docs/aws-managed-views-common-configuration--page#actionProps).

**Input data example**

```
{
    "AttributeBar": [{
            "Label": "Queue",
            "Value": "Sales"
        },
        {
            "Label": "Case ID",
            "Value": "1234567"
        },
        {
            "Label": "Case",
            "Value": "New reservation"
        },
        {
            "Label": "Attribute 3",
            "Value": "Attribute"
        }
    ],
    "Back": {
        "Label": "Back"
    },
    "Heading": "Customer may be contacting about...",
    "Cards": [{
              "Summary": {
                "Id": "lost_luggage",
                "Icon": "plus",
                "Heading": "Lost luggage claim"
              },
              "Detail": {
                "Heading": "Lost luggage claim",
                "Description": "Use this flow for customers that have lost their luggage and need to file a claim to get reimbursement. This workflow usually takes 5-8 minutes.",
                "Sections": {
                  "TemplateString": "<TextContent>Steps:<ol><li>Customer provides incident information</li><li>Customer provides receipts and agrees with amount</li><li>Customer receives reimbursement</li></ol></TextContent>"
                },
                "Actions": [
                  "Start a new claim",
                  "Something else"
                ]
              }
            },
            {
              "Summary": {
                "Id": "car_rental",
                "Icon": "Car Side View",
                "Heading": "Car rental - New York",
                "Status": "Upcoming Sept 17, 2022"
              },
              "Detail": {
                "Heading": "Car rental - New York",
                "Sections": {
                  "TemplateString": "<p>There is no additional information</p>"
                }
              }
            },
            {
              "Summary": {
                "Id": "trip_reservation",
                "Icon": "Suitcase",
                "Heading": "Trip to Mexico",
                "Status": "Upcoming Aug 15, 2022",
                "Description": "Flying from New York to Cancun, Mexico"
              },
              "Detail": {
                "Heading": "Trip to Mexico",
                "Sections": {
                  "TemplateString": "<p>There is no additional information</p>"
                }
              }
            },
            {
              "Summary": {
                "Id": "fligh_reservation",
                "Icon": "Airplane",
                "Heading": "Flight to France",
                "Status": "Upcoming Dec 5, 2022",
                "Description": "Flying from Miami to Paris, France"
              },
              "Detail": {
                "Heading": "Flight to France",
                "Sections": {
                  "TemplateString": "<p>There is no additional information</p>"
                }
              }
            },
            {
              "Summary": {
                "Id": "flight_refund",
                "Icon": "Wallet Closed",
                "Heading": "Refund flight to Atlanta",
                "Status": "Refunded July 10, 2022"
              },
              "Detail": {
                "Heading": "Refund flight to Atlanta",
                "Sections": {
                  "TemplateString": "<p>There is no additional information</p>"
                }
              }
            },
            {
              "Summary": {
                "Id": "book_experience",
                "Icon": "Hot Air Balloon",
                "Heading": "Book an experience",
                "Description": "Top experience for European travelers"
              },
              "Detail": {
                "Heading": "Book an experience",
                "Sections": {
                  "TemplateString": "<p>There is no additional information</p>"
                }
              }
            }],
    "NoMatchFound": {
        "Label": "Can't find match?"
    }

}
```

**Output data example**

```
{
    "Action": "ActionSelected",
    "ViewResultData": {
        "actionName": "Start a new claim"
    }
}
```

------