

# Creating event archives in Amazon EventBridge
<a name="eb-archive-event"></a>

When you create an archive in EventBridge, you can determine which events are sent to the archive by specifying an [event pattern](eb-event-patterns.md). EventBridge sends events that match the event pattern to the archive. You also set the retention period to store events in the archive before they are discarded.

You can also create archives as part of [creating an event bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-event-bus.html). These archives have an indefinite retention policy and no event filter, although this can be [updated](https://docs.aws.amazon.com/eventbridge/latest/userguide/event-bus-update-archive.html) once the archive is created.

**Topics**
+ [Define the archive](#eb-create-archive-define)
+ [Build the event pattern (optional)](#eb-create-archive-event-pattern)

## Define the archive
<a name="eb-create-archive-define"></a>

First, enter a name and description for archive, and specify the event bus from which it receives events. Optionally, you can also set how long to retain events in the archive.

**To define the archive**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Navigate to the source event bus, or create the archive directly:
   + In the navigation pane, choose **Event buses**.

     On the events bus details page, choose the **Archives** tab.
   + In the navigation pane, choose **Archives**.

1. Choose **Create archive**.

1. Under **Archive detail**, enter a name and optionally, a description for the archive. 

    The name must be unique to your account in the selected Region. You can't change the name after you create the archive.

1. For **Source**, select the event bus you want to send events to the archive

   If you navigated from an existing event bus details page, the name of that event bus appears by default.

   You cannot change the source event bus once you have created the archive.

1. For **Retention period**, specify how long to retain the events in the archive:
   + Choose **Indefinite** to retain the events in the archive and not ever delete them.
   + For a set retention period, enter the number of days after which EventBridge should delete the events from the archive.

1. For **Encryption**, choose the KMS key for EventBridge to use when encrypting the events stored in the archive.
**Important**  
If you have specify that EventBridge use a customer managed key for encrypting the source event bus, we strongly recommend you also specify a customer managed key for any archives for the event bus as well.
   + Choose **Use AWS owned key** for EventBridge to encrypt the data using an AWS owned key.

     This AWS owned key is a KMS key that EventBridge owns and manages for use in multiple AWS accounts. In general, unless you are required to audit or control the encryption key that protects your resources, an AWS owned key is a good choice. 

     This is the default.
   + Choose **Use customer managed key** for EventBridge to encrypt the data using the customer managed key that you specify or create.

     Customer managed key are KMS keys in your AWS account that you create, own, and manage. You have full control over these KMS keys.

     1. Specify an existing customer managed key, or choose **Create a new KMS key />**.

       EventBridge displays the key status and any key aliases that have been associated with the specified customer managed key.

1. Choose **Next**.

## Build the event pattern (optional)
<a name="eb-create-archive-event-pattern"></a>

Next, as an optional step, you can build an event pattern to filter which events EventBridge sends to the archive. To do this, specify the event source, choose the basis for the event pattern, and define the attributes and values to match on. You can also generate the event pattern in JSON and test it against a sample event.

For more information on event patterns, see [](eb-event-patterns.md).

**To build the event pattern**

1. For **Event source**, choose **AWS events or EventBridge partner events**.

1. (Optional) In the **Sample events** section, choose a **Sample event type** against which you want to test your event pattern. 

   The following sample event types are available:
   + **AWS events **– Select from events emitted from supported AWS services.
   + **EventBridge partner events** – Select from events emitted from third-party services that support EventBridge, such as Salesforce.
   + **Enter my own** – Enter your own event in JSON text.

     You can also use an AWS or partner event as the starting point for creating your own custom event.

     1. Select **AWS events** or **EventBridge partner events**.

     1. Use the **Sample events** dropdown to select the event you want to use as a starting point for your custom event.

        EventBridge displays the sample event.

     1. Select **Copy**.

     1. Select **Enter my own** for **Event type.**

     1. Delete the sample event structure in the JSON editing pane, and paste the AWS or partner event in its place.

     1. Edit the event JSON to create your own sample event.

1. Choose a **Creation method**. You can create an event pattern from an EventBridge schema or template, or you can create a custom event pattern.

------
#### [ Existing schema ]

   To use an existing EventBridge schema to create the event pattern, do the following:

   1. In the **Creation method** section, for **Method**, select **Use schema**.

   1. In the **Event pattern** section, for **Schema type**, select **Select schema from Schema registry**.

   1. For **Schema registry**, choose the dropdown box and enter the name of a schema registry, such as `aws.events`. You can also select an option from the dropdown list that appears.

   1. For **Schema**, choose the dropdown box and enter the name of the schema to use. For example, `aws.s3@ObjectDeleted`. You can also select an option from the dropdown list that appears.

   1. In the **Models** section, choose the **Edit** button next to any attribute to open its properties. Set the **Relationship** and **Value** fields as needed, then choose **Set** to save the attribute.
**Note**  
For information about an attribute's definition, choose the **Info** icon next to the attribute's name. For a reference on how to set attribute properties in your event, open the **Note** section of the attribute properties dialog box.  
To delete an attribute's properties, choose the **Edit** button for that attribute, then choose **Clear**.

   1. Choose **Generate event pattern in JSON** to generate and validate your event pattern as JSON text. 

   1. (Optional) To test the sample event against your test pattern, choose **Test pattern**. 

      EventBridge displays a message box stating whether your sample event matches the event pattern.

      You can also choose any of the following options:
      + **Copy** – Copy the event pattern to your device's clipboard.
      + **Prettify** – Makes the JSON text easier to read by adding line breaks, tabs, and spaces.

------
#### [ Custom schema ]

   To write a custom schema and convert it to an event pattern, do the following:

   1. In the **Creation method** section, for **Method**, choose **Use schema**.

   1. In the **Event pattern** section, for **Schema type**, choose **Enter schema**.

   1. Enter your schema into the text box. You must format the schema as valid JSON text.

   1. In the **Models** section, choose the **Edit** button next to any attribute to open its properties. Set the **Relationship** and **Value** fields as needed, then choose **Set** to save the attribute.
**Note**  
For information about an attribute's definition, choose the **Info** icon next to the attribute's name. For a reference on how to set attribute properties in your event, open the **Note** section of the attribute properties dialog box.  
To delete an attribute's properties, choose the **Edit** button for that attribute, then choose **Clear**.

   1. Choose **Generate event pattern in JSON** to generate and validate your event pattern as JSON text. 

   1. (Optional) To test the sample event against your test pattern, choose **Test pattern**. 

      EventBridge displays a message box stating whether your sample event matches the event pattern.

      You can also choose any of the following options:
      + **Copy** – Copy the event pattern to your device's clipboard.
      + **Prettify** – Makes the JSON text easier to read by adding line breaks, tabs, and spaces.

------
#### [ Event pattern ]

   To write a custom event pattern in JSON format, do the following:

   1. In the **Creation method** section, for **Method**, choose **Custom pattern (JSON editor)**.

   1. For **Event pattern**, enter your custom event pattern in JSON-formatted text. 

   1. (Optional) To test the sample event against your test pattern, choose **Test pattern**. 

      EventBridge displays a message box stating whether your sample event matches the event pattern.

      You can also choose any of the following options:
      + **Copy** – Copy the event pattern to your device's clipboard.
      + **Prettify** – Makes the JSON text easier to read by adding line breaks, tabs, and spaces.
      + **Event pattern form** – Opens the event pattern in Pattern Builder. If the pattern can't be rendered in Pattern Builder as-is, EventBridge warns you before it opens Pattern Builder.

------

1. Choose **Create archive**.

To confirm that events are successfully sent to the archive, you can use the [`DescribeArchive`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DescribeArchive.html) operation of the EventBridge API to see if the `EventCount` reflects the number of events in the archive. If it is 0, there are no events in the archive.