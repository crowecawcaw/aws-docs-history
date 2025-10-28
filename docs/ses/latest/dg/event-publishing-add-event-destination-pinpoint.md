# Set up an Amazon Pinpoint event

destination for event publishing

An Amazon Pinpoint event destination notifies you about the email sending events you specify in a
configuration set. Because an Amazon Pinpoint event destination can only be set up in a configuration
set, you have to [create a
configuration set](event-publishing-create-configuration-set.md "event-publishing-create-configuration-set.md") before you add the event destination to the configuration
set.

The procedure in this section shows how to add Amazon Pinpoint event destination details to a
configuration set and assumes you have completed steps 1 through 6 in [Creating an event destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add").

You can also use the [UpdateConfigurationSetEventDestination](../APIReference-V2/API_UpdateConfigurationSetEventDestination.md "../APIReference-V2/API_UpdateConfigurationSetEventDestination.md") operation in the Amazon SES API V2 to create
and modify event destinations.

There are additional charges for the types of channels you have configured in your Amazon Pinpoint
projects. For more information, see [Amazon Pinpoint
Pricing](https://aws.amazon.com/pinpoint/pricing/ "https://aws.amazon.com/pinpoint/pricing/").

###### To add Amazon Pinpoint event destination details to a configuration set using the

console

1. These are the detailed instructions for selecting Amazon Pinpoint as your event destination
   type in [Step 7](event-destinations-manage.md#specify-event-dest-step "event-destinations-manage.md#specify-event-dest-step") and assumes you have
   completed all the previous steps in [Creating an event destination](event-destinations-manage.md#event-destination-add "event-destinations-manage.md#event-destination-add").

###### Note

Amazon Pinpoint does not support event types **Delivery delays** or
**Subscriptions**.

After selecting the Amazon Pinpoint **Destination type**, entering a
destination **Name**, and enabling **Event
publishing**, the **Amazon Pinpoint project details**
pane is displayed—its fields are addressed in the following steps. 2. For **Project**, choose an existing Amazon Pinpoint project, or choose
**Create a new project in Amazon Pinpoint** to create a new one.

For information about creating a project, see [Create a project](../../../pinpoint/latest/userguide/gettingstarted-create-project.md "../../../pinpoint/latest/userguide/gettingstarted-create-project.md") in
the _Amazon Pinpoint User Guide_. 3. Choose **Next**. 4. On the review screen, if you're satisfied with how you defined your event
destination, choose **Add destination**. This will open the event
destination's summary page where a success banner will confirm if your event
destination was created or modified successfully.
