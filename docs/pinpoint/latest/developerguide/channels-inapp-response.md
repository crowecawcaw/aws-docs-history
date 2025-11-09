**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# `GetInAppMessages`

Amazon Pinpoint API response JSON example

When you call the [GetInAppMessages](../apireference/apps-application-id-endpoints-endpoint-id-inappmessages.md#GetInAppMessages "../apireference/apps-application-id-endpoints-endpoint-id-inappmessages.md#GetInAppMessages") API operation, it returns a list of messages that the
specified endpoint is entitled to. Your app can then render the message based on the
values in the response.

The following is an example of the JSON object that is returned when you call the
`GetInAppMessages` API:

```
{
  "InAppMessagesResponse":{
    "InAppMessageCampaigns":[
      {
        "CampaignId":"inAppTestCampaign-4c545b28d21a490cb51b0b364example",
        "DailyCap":0,
        "InAppMessage":{
          "Content":[
            {
              "BackgroundColor":"#f8e71c",
              "BodyConfig":{
                "Alignment":"CENTER",
                "Body":"This is a sample in-app message sent using Amazon Pinpoint.",
                "TextColor":"#d0021b"
              },
              "HeaderConfig":{
                "Alignment":"CENTER",
                "Header":"Sample In-App Message",
                "TextColor":"#d0021b"
              },
              "ImageUrl":"https://example.com/images/thumbnail.png",
              "PrimaryBtn":{
                "DefaultConfig":{
                  "BackgroundColor":"#d0021b",
                  "BorderRadius":50,
                  "ButtonAction":"CLOSE",
                  "Text":"Dismiss",
                  "TextColor":"#f8e71c"
                }
              }
            }
          ],
          "Layout":"MIDDLE_BANNER"
        },
        "Priority":3,
        "Schedule":{
          "EndDate":"2021-11-06T00:08:05Z",
          "EventFilter":{
            "Dimensions":{
              "Attributes":{

              },
              "EventType":{
                "DimensionType":"INCLUSIVE",
                "Values":[
                  "_session.start"
                ]
              },
              "Metrics":{

              }
            }
          }
        },
        "SessionCap":0,
        "TotalCap":0,
        "TreatmentId":"0"
      }
    ]
  }
}
```

The following sections provide information about the components of this
response, and their attributes.

## `InAppMessageCampaigns` object

The `InAppMessageCampaigns` object contains the following
attributes:

| Attribute      | Description                                                                                                                                                                                                        | Where it's set                                                                                                                                                                                                                                              |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CampaignId`   | A string that contains the name and unique campaign ID of<br>the Amazon Pinpoint campaign that the message was sent from. The name<br>precedes the campaign ID. The two values are separated with a<br>hyphen (-). | Automatically created by Amazon Pinpoint when you create<br>the campaign.                                                                                                                                                                                   |
| `TreatmentId`  | An integer that represents the ID of the campaign treatment<br>for this message. If the campaign only has one treatment, the<br>value is `0`.                                                                      |
| `Priority`     | The priority of the in-app message, expressed as an integer<br>between 1 and 5, inclusive, where 1 indicates the highest<br>priority, and 5 indicates the lowest priority.                                         | [Step<br>1](../userguide/campaigns-begin.md "../userguide/campaigns-begin.md") of the campaign creation process.                                                                                                                                            |
| `InAppMessage` | An [InAppMessage object](#channels-inapp-response-inappmessage-object "#channels-inapp-response-inappmessage-object") that contains information about<br>how the message is rendered.                              | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign.                                                          |
| `Schedule`     | A Schedule object that contains information<br>about when the message was sent.                                                                                                                                    | [Step<br>4](../userguide/campaigns-schedule.md "../userguide/campaigns-schedule.md") of the campaign creation process (if the campaign<br>was created in the console) or the `Schedule` object<br>(if the campaign was created using the API or an<br>SDK). |
| `DailyCap`     | The number of times, shown as an integer, that an in-app<br>message can be shown to the user during a 24-hour<br>period.                                                                                           | Inherited from [project-level<br>settings](../userguide/settings-general.md "../userguide/settings-general.md"). If the campaign includes settings that<br>override the project settings, then those are used<br>instead.                                   |
| `SessionCap`   | The number of times, expressed as an integer, that an<br>in-app message can be shown to the user during an application<br>session.                                                                                 |
| `TotalCap`     | The total number of times, expressed as an integer, that<br>any in-app message can be shown to an endpoint per<br>campaign.                                                                                        |

## `InAppMessage` object

The `InAppMessage` object contains the following attributes:

| Attribute | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Where it's set                                                                                                                                                                                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Content` | An array containing an [InAppMessageContent](#channels-inapp-response-inappmessagecontent-object "#channels-inapp-response-inappmessagecontent-object") object, which describes the<br>content of the message.                                                                                                                                                                                                                                                                                                                                                                                     | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `Layout`  | A string that describes how the in-app message will appear<br>on the recipient's device. Possible values are:<br>• `BOTTOM_BANNER` – a message that<br>appears as a banner at the bottom of the page.<br>• `TOP_BANNER` – a message that appears<br>as a banner at the top of the page.<br>• `OVERLAYS` – a message that covers<br>entire screen.<br>• `MOBILE_FEED` – a message that<br>appears in a window in front of the page.<br>• `MIDDLE_BANNER` – a message that<br>appears as a banner in the middle of the page.<br>• `CAROUSEL` – a scrollable layout of<br>up to five unique messages. |

## `HeaderConfig` object

The `HeaderConfig` object contains the following attributes:

| Attribute   | Description                                                                                                             | Where it's set                                                                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Alignment` | A string that specifies the text alignment of the header<br>text. Possible values are `LEFT`,<br>`CENTER`, and `RIGHT`. | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `Header`    | The message header text.                                                                                                |
| `TextColor` | The color of the header text, expressed as string<br>describing the hex color code (such as "#000000" for<br>black).    |

## `BodyConfig`

object

The `BodyConfig` object contains the following attributes:

| Attribute   | Description                                                                                                              | Where it's set                                                                                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Alignment` | A string that specifies the text alignment of the message<br>body. Possible values are `LEFT`,<br>`CENTER`, and `RIGHT`. | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `Body`      | The main body text of the message.                                                                                       |
| `TextColor` | The color of the body text, expressed as a string<br>containing a hex color code (such as "#000000" for<br>black).       |

## `InAppMessageContent` object

The `InAppMessageContent` object contains the following
attributes:

| Attribute         | Description                                                                                                                                                                                                                                                                  | Where it's set                                                                                                                                                                                     |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BackgroundColor` | The background color of the in-app message, expressed as a<br>string containing a hex color code (such as "#000000" for<br>black).                                                                                                                                           | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `BodyConfig`      | A [BodyConfig](#channels-inapp-response-bodyconfig-object "#channels-inapp-response-bodyconfig-object") object, which contains information<br>related to the main body content of the message.                                                                               |
| `HeaderConfig`    | A [HeaderConfig](#channels-inapp-response-headerconfig-object "#channels-inapp-response-headerconfig-object") object, which contains information<br>related to the header or title of the message.                                                                           |
| `ImageUrl`        | The URL of the image that appears in the<br>message.                                                                                                                                                                                                                         |
| `PrimaryBtn`      | An [InAppMessageButton](#channels-inapp-response-button-object "#channels-inapp-response-button-object") object that contains information<br>about the main button in the message.                                                                                           |
| `SecondaryBtn`    | An [InAppMessageButton](#channels-inapp-response-button-object "#channels-inapp-response-button-object") object that contains information<br>about the secondary button in the message. Not present if the<br>in-app message template doesn't specify a secondary<br>button. |

## `Schedule`

object

The `Schedule` object contains the following attributes:

| Attribute     | Description                                                                                                                                                                              | Where it's set                                                                                                                                                                                                                                           |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EndDate`     | The scheduled time, in ISO 8601 format, when the campaign will<br>end.                                                                                                                   | [Step 4](../userguide/campaigns-schedule.md "../userguide/campaigns-schedule.md") of<br>the campaign creation process (if the campaign was created in<br>the console) or the `Schedule` object (if the<br>campaign was created using the API or an SDK). |
| `EventFilter` | Information about the event that causes the in-app message<br>to be shown. When you generate an event that matches with an<br>Amazon Pinpoint in-app campaign, the message is displayed. |

## `InAppMessageButton` object

An `InAppMessageButton` object contains the following
attributes:

| Attribute       | Description                                                                                                                                                                                                                                                                                                  | Where it's set                                                                                                                                                                                     |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DefaultConfig` | A [DefaultButtonConfig](#channels-inapp-response-defaultbuttonconfig-object "#channels-inapp-response-defaultbuttonconfig-object") object that contains information<br>about the default settings for a button in an in-app<br>message.                                                                      | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `Android`       | An [OverrideButtonConfig](#channels-inapp-response-overridebuttonconfig-object "#channels-inapp-response-overridebuttonconfig-object") object that specifies the way<br>the button behaves on Android devices. This overrides the<br>default button configuration detailed in the<br>`DefaultConfig` object. |
| `IOS`           | An [OverrideButtonConfig](#channels-inapp-response-overridebuttonconfig-object "#channels-inapp-response-overridebuttonconfig-object") object that specifies the way<br>the button behaves on iOS devices. This overrides the default<br>button configuration detailed in the `DefaultConfig`<br>object.     |
| `Web`           | An [OverrideButtonConfig](#channels-inapp-response-overridebuttonconfig-object "#channels-inapp-response-overridebuttonconfig-object") object that specifies the way<br>the button behaves in web apps. This overrides the default<br>button configuration detailed in the `DefaultConfig`<br>object.        |

## `DefaultButtonConfig` object

An `DefaultButtonConfig` object contains the following
attributes:

| Attribute         | Description                                                                                                                                                                                                                                                                            | Where it's set                                                                                                                                                                                     |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BackgroundColor` | The background color of the button, expressed as a string<br>containing a hex color code (such as "#000000" for<br>black).                                                                                                                                                             | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `BorderRadius`    | The radius of the button's border in pixels, expressed as an<br>integer. A larger number results in more rounded corners.                                                                                                                                                              |
| `ButtonAction`    | A string that describes the action that occurs when a<br>recipient chooses a button in the in-app message. Possible<br>values are:<br>• `LINK` – A link to a web destination.<br>• `DEEP_LINK` – A link to a specific<br>page in an application.<br>• `CLOSE` – Dismisses the message. |
| `Link`            | The destination URL for a button. Not present for buttons<br>where the ButtonAction is `CLOSE`.                                                                                                                                                                                        |
| `Text`            | The text that appears on the button.                                                                                                                                                                                                                                                   |
| `TextColor`       | The color of the text on the button, expressed as a string<br>containing a hex color code (such as "#000000" for<br>black).                                                                                                                                                            |

## `OverrideButtonConfig` object

The `OverrideButtonConfig` object is only present if the in-app message
template uses override buttons. An override button is a button that has a specific
configuration for a particular device type, such as an iOS device, Android device,
or a web browser.

An `OverrideButtonConfig` object contains the following
attributes:

| Attribute      | Description                                                                                                                                                                                                                                                 | Where it's set                                                                                                                                                                                     |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ButtonAction` | The action that occurs when a recipient chooses a button in<br>the in-app message. Possible values are:<br>• `LINK` – A link to a web destination.<br>• `DEEP_LINK` – A link to a specific<br>page in an application.<br>• `CLOSE` – Dismisses the message. | Based on the content in the [in-app message template](../userguide/message-templates-creating-inapp.md "../userguide/message-templates-creating-inapp.md") that was specified for the<br>campaign. |
| `Link`         | The destination URL for a button. Not present for buttons<br>where the `ButtonAction` is<br>`CLOSE`.                                                                                                                                                        |
| `Text`         | The text that appears on the button.                                                                                                                                                                                                                        |
| `TextColor`    | The color of the text on the button, expressed as a string<br>containing a hex color code (such as "#000000" for<br>black).                                                                                                                                 |
