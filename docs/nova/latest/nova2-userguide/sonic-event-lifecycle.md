

# Event lifecycle
<a name="sonic-event-lifecycle"></a>

The following diagram illustrates the complete bi-directional streaming event lifecycle:

![Bi-directional streaming flow between user, client, and Amazon Bedrock with audio and text.](http://docs.aws.amazon.com/nova/latest/nova2-userguide/images/Event-Lifecycle-Diagram_1.png)


The bidirectional streaming event lifecycle follows a structured pattern from session initialization through conversation completion. Each conversation involves input events (from your application) and output events (from Amazon Nova 2 Sonic) that work together to create natural voice interactions.