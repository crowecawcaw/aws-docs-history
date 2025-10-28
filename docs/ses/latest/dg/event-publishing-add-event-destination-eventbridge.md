# Set up an Amazon EventBridge

destination for event publishing

An Amazon EventBridge event destination notifies you about the email sending events you specify in a
configuration set. SES generates and sends email sending events that you define when
creating an event destination to the EventBridge default event bus. An [event bus](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md") is a router that receives events
and can deliver them to multiple destinations. You can learn more about integrating email
sending events with Amazon EventBridge in [Monitoring SES events using Amazon EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md"). Because an EventBridge
event destination can only be set up in a configuration set, you have to [create a configuration set](event-publishing-create-configuration-set.md "event-publishing-create-configuration-set.md")
before you add the event destination to the configuration set.

The procedure in this section shows how to add EventBridge event destination details to a
configuration set and assumes you have completed steps 1 through 6 in [Creating an event destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add").

You can also use the [UpdateConfigurationSetEventDestination](../APIReference-V2/API_UpdateConfigurationSetEventDestination.md "../APIReference-V2/API_UpdateConfigurationSetEventDestination.md") operation in the Amazon SES API V2 to create
and modify event destinations.

###### To add EventBridge event destination details to a configuration set using the

console

1. These are the detailed instructions for selecting EventBridge as your event destination
   type in [Step 7](event-destinations-manage.md#specify-event-dest-step "event-destinations-manage.md#specify-event-dest-step") and assumes you have
   completed all the previous steps in [Creating an event destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add"). After selecting the
   _Amazon EventBridge_
   **Destination type**, entering a destination
   **Name**, and enabling **Event publishing**,
   an **Amazon EventBridge event bus** informational pane is displayed.
2. Choose **Next**.
3. On the review screen, if you're satisfied with how you defined your event
   destination, choose **Add destination**. This will open the event
   destination's summary page where a success banner will confirm if your event
   destination was created or modified successfully.
