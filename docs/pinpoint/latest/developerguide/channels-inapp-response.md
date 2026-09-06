

**End of support notice:** On October 30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of support](https://docs.aws.amazon.com/console/pinpoint/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by AWS End User Messaging.

# `GetInAppMessages` Amazon Pinpoint API response JSON example
<a name="channels-inapp-response"></a>

When you call the [GetInAppMessages](https://docs.aws.amazon.com/pinpoint/latest/apireference/apps-application-id-endpoints-endpoint-id-inappmessages.html#GetInAppMessages) API operation, it returns a list of messages that the specified endpoint is entitled to. Your app can then render the message based on the values in the response.

The following is an example of the JSON object that is returned when you call the `GetInAppMessages` API:

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

The following sections provide information about the components of this response, and their attributes.

## `InAppMessageCampaigns` object
<a name="channels-inapp-response-inappmessagecampaigns-object"></a>

The `InAppMessageCampaigns` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>CampaignId</code></td><td>A string that contains the name and unique campaign ID of the Amazon Pinpoint campaign that the message was sent from. The name precedes the campaign ID. The two values are separated with a hyphen (-).</td><td rowspan="2">Automatically created by Amazon Pinpoint when you create the campaign.</td></tr>
  <tr><td><code>TreatmentId</code></td><td>An integer that represents the ID of the campaign treatment for this message. If the campaign only has one treatment, the value is <code>0</code>.</td></tr>
  <tr><td><code>Priority</code></td><td>The priority of the in-app message, expressed as an integer between 1 and 5, inclusive, where 1 indicates the highest priority, and 5 indicates the lowest priority.</td><td><a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-begin.html">Step 1</a> of the campaign creation process.</td></tr>
  <tr><td><code>InAppMessage</code></td><td>An <a href="#channels-inapp-response-inappmessage-object">`InAppMessage` object</a> that contains information about how the message is rendered.</td><td>Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Schedule</code></td><td>A Schedule object that contains information about when the message was sent.</td><td><a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-schedule.html">Step 4</a> of the campaign creation process (if the campaign was created in the console) or the <code>Schedule</code> object (if the campaign was created using the API or an SDK).</td></tr>
  <tr><td><code>DailyCap</code></td><td>The number of times, shown as an integer, that an in-app message can be shown to the user during a 24-hour period.</td><td rowspan="3">Inherited from <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/settings-general.html">project-level settings</a>. If the campaign includes settings that override the project settings, then those are used instead.</td></tr>
  <tr><td><code>SessionCap</code></td><td>The number of times, expressed as an integer, that an in-app message can be shown to the user during an application session.</td></tr>
  <tr><td><code>TotalCap</code></td><td>The total number of times, expressed as an integer, that any in-app message can be shown to an endpoint per campaign.</td></tr>
</tbody>
</table>


## `InAppMessage` object
<a name="channels-inapp-response-inappmessage-object"></a>

The `InAppMessage` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>Content</code></td><td>An array containing an <a href="#channels-inapp-response-inappmessagecontent-object">InAppMessageContent</a> object, which describes the content of the message.</td><td rowspan="2">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Layout</code></td><td>A string that describes how the in-app message will appear on the recipient's device. Possible values are:<ul><li> <code>BOTTOM_BANNER</code> – a message that appears as a banner at the bottom of the page. </li><li> <code>TOP_BANNER</code> – a message that appears as a banner at the top of the page. </li><li> <code>OVERLAYS</code> – a message that covers entire screen. </li><li> <code>MOBILE_FEED</code> – a message that appears in a window in front of the page. </li><li> <code>MIDDLE_BANNER</code> – a message that appears as a banner in the middle of the page. </li><li> <code>CAROUSEL</code> – a scrollable layout of up to five unique messages. </li></ul></td></tr>
</tbody>
</table>


## `HeaderConfig` object
<a name="channels-inapp-response-headerconfig-object"></a>

The `HeaderConfig` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>Alignment</code></td><td>A string that specifies the text alignment of the header text. Possible values are <code>LEFT</code>, <code>CENTER</code>, and <code>RIGHT</code>.</td><td rowspan="3">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Header</code></td><td>The message header text.</td></tr>
  <tr><td><code>TextColor</code></td><td>The color of the header text, expressed as string describing the hex color code (such as "#000000" for black).</td></tr>
</tbody>
</table>


## `BodyConfig` object
<a name="channels-inapp-response-bodyconfig-object"></a>

The `BodyConfig` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>Alignment</code></td><td>A string that specifies the text alignment of the message body. Possible values are <code>LEFT</code>, <code>CENTER</code>, and <code>RIGHT</code>.</td><td rowspan="3">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Body</code></td><td>The main body text of the message.</td></tr>
  <tr><td><code>TextColor</code></td><td>The color of the body text, expressed as a string containing a hex color code (such as "#000000" for black).</td></tr>
</tbody>
</table>


## `InAppMessageContent` object
<a name="channels-inapp-response-inappmessagecontent-object"></a>

The `InAppMessageContent` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>BackgroundColor</code></td><td>The background color of the in-app message, expressed as a string containing a hex color code (such as "#000000" for black).</td><td rowspan="6">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>BodyConfig</code></td><td>A <a href="#channels-inapp-response-bodyconfig-object">BodyConfig</a> object, which contains information related to the main body content of the message.</td></tr>
  <tr><td><code>HeaderConfig</code></td><td>A <a href="#channels-inapp-response-headerconfig-object">HeaderConfig</a> object, which contains information related to the header or title of the message.</td></tr>
  <tr><td><code>ImageUrl</code></td><td>The URL of the image that appears in the message.</td></tr>
  <tr><td><code>PrimaryBtn</code></td><td>An <a href="#channels-inapp-response-button-object">InAppMessageButton</a> object that contains information about the main button in the message.</td></tr>
  <tr><td><code>SecondaryBtn</code></td><td>An <a href="#channels-inapp-response-button-object">InAppMessageButton</a> object that contains information about the secondary button in the message. Not present if the in-app message template doesn't specify a secondary button.</td></tr>
</tbody>
</table>


## `Schedule` object
<a name="channels-inapp-response-schedule-object"></a>

The `Schedule` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>EndDate</code></td><td>The scheduled time, in ISO 8601 format, when the campaign will end. </td><td rowspan="2"><a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/campaigns-schedule.html">Step 4</a> of the campaign creation process (if the campaign was created in the console) or the <code>Schedule</code> object (if the campaign was created using the API or an SDK).</td></tr>
  <tr><td><code>EventFilter</code></td><td>Information about the event that causes the in-app message to be shown. When you generate an event that matches with an Amazon Pinpoint in-app campaign, the message is displayed.</td></tr>
</tbody>
</table>


## `InAppMessageButton` object
<a name="channels-inapp-response-button-object"></a>

An `InAppMessageButton` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>DefaultConfig</code></td><td>A <a href="#channels-inapp-response-defaultbuttonconfig-object">DefaultButtonConfig</a> object that contains information about the default settings for a button in an in-app message.</td><td rowspan="4">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Android</code></td><td>An <a href="#channels-inapp-response-overridebuttonconfig-object">OverrideButtonConfig</a> object that specifies the way the button behaves on Android devices. This overrides the default button configuration detailed in the <code>DefaultConfig</code> object.</td></tr>
  <tr><td><code>IOS</code></td><td>An <a href="#channels-inapp-response-overridebuttonconfig-object">OverrideButtonConfig</a> object that specifies the way the button behaves on iOS devices. This overrides the default button configuration detailed in the <code>DefaultConfig</code> object.</td></tr>
  <tr><td><code>Web</code></td><td>An <a href="#channels-inapp-response-overridebuttonconfig-object">OverrideButtonConfig</a> object that specifies the way the button behaves in web apps. This overrides the default button configuration detailed in the <code>DefaultConfig</code> object.</td></tr>
</tbody>
</table>


## `DefaultButtonConfig` object
<a name="channels-inapp-response-defaultbuttonconfig-object"></a>

An `DefaultButtonConfig` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>BackgroundColor</code></td><td>The background color of the button, expressed as a string containing a hex color code (such as "#000000" for black).</td><td rowspan="6">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>BorderRadius</code></td><td>The radius of the button's border in pixels, expressed as an integer. A larger number results in more rounded corners.</td></tr>
  <tr><td><code>ButtonAction</code></td><td>A string that describes the action that occurs when a recipient chooses a button in the in-app message. Possible values are: <ul><li> <code>LINK</code> – A link to a web destination.  </li><li> <code>DEEP_LINK</code> – A link to a specific page in an application.  </li><li> <code>CLOSE</code> – Dismisses the message.  </li></ul></td></tr>
  <tr><td><code>Link</code></td><td>The destination URL for a button. Not present for buttons where the ButtonAction is <code>CLOSE</code>.</td></tr>
  <tr><td><code>Text</code></td><td>The text that appears on the button.</td></tr>
  <tr><td><code>TextColor</code></td><td>The color of the text on the button, expressed as a string containing a hex color code (such as "#000000" for black).</td></tr>
</tbody>
</table>


## `OverrideButtonConfig` object
<a name="channels-inapp-response-overridebuttonconfig-object"></a>

The `OverrideButtonConfig` object is only present if the in-app message template uses override buttons. An override button is a button that has a specific configuration for a particular device type, such as an iOS device, Android device, or a web browser.

An `OverrideButtonConfig` object contains the following attributes:


<table>
<thead>
  <tr><th>Attribute</th><th>Description</th><th>Where it's set</th></tr>
</thead>
<tbody>
  <tr><td><code>ButtonAction</code></td><td>The action that occurs when a recipient chooses a button in the in-app message. Possible values are: <ul><li> <code>LINK</code> – A link to a web destination.  </li><li> <code>DEEP_LINK</code> – A link to a specific page in an application.  </li><li> <code>CLOSE</code> – Dismisses the message.  </li></ul></td><td rowspan="4">Based on the content in the <a href="https://docs.aws.amazon.com/pinpoint/latest/userguide/message-templates-creating-inapp.html">in-app message template</a> that was specified for the campaign.</td></tr>
  <tr><td><code>Link</code></td><td>The destination URL for a button. Not present for buttons where the <code>ButtonAction</code> is <code>CLOSE</code>.</td></tr>
  <tr><td><code>Text</code></td><td>The text that appears on the button.</td></tr>
  <tr><td><code>TextColor</code></td><td>The color of the text on the button, expressed as a string containing a hex color code (such as "#000000" for black).</td></tr>
</tbody>
</table>
