

# Collect disposition codes from agents when a contact ends
<a name="disposition-codes-sg"></a>

A step-by-step guide can ask agents for a disposition code, or other after contact work, when a contact ends. Create a flow with one [Show view](show-view-block.md) block and one [Set contact attributes](set-contact-attributes.md) block.
+ Use the [Show view](show-view-block.md) block to show a **Form** view with the required input field.
+ Use the [Set contact attributes](set-contact-attributes.md) block to save the response as contact attributes.

You can also use an [AWS Lambda function](invoke-lambda-function-block.md) block to send the data to an external system.

To show the guide when a contact ends, add a [Set event flow](set-event-flow.md) block to your contact flow, and set the **Disconnect flow for Agent UI** event to this flow. If the event is set before the contact ends, the agent workspace shows the form after the contact ends.

The following image shows the properties of a [Set contact attributes](set-contact-attributes.md) block, configured to save the response in a user-defined attribute.

![The properties page of the Set contact attributes block.](https://docs.aws.amazon.com/connect/latest/adminguide/images/dispo-codes-sq.png)
