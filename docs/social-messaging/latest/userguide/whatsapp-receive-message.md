# Responding to a message in AWS End User Messaging Social

Before you can receive a text or media message, you must have set up your WhatsApp
Business Account (WABA) and an event destination. When you receive an incoming message, an
event is saved in the event destination Amazon SNS topic. To receive a notification, you must
subscribe to the Amazon SNS topics endpoint.

For an example event of a received media message, see [Example WhatsApp JSON for receiving a media message](managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media "managing-event-destination-dlrs.md#managing-event-destination-dlrs-example-receive-media"). For more
information on configuring the AWS CLI, see [Configure the
AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in the _[AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md")_. For a list of
supported media file types, see [Supported media file types and sizes in WhatsApp](supported-media-types.md "supported-media-types.md").

###### Important

To receive incoming messages, you must have [event destinations](managing-event-destinations-add.md "managing-event-destinations-add.md") enabled for the WABA. For more information, see [Add a message and event destination to AWS End User Messaging Social](managing-event-destinations-add.md "managing-event-destinations-add.md").
