# Event enrichment in Amazon EventBridge Pipes

With the enrichment step of EventBridge Pipes, you can enhance the data from the source before
sending it to the target. For example, you might receive _Ticket
created_ events that don’t include the full ticket data. Using enrichment, you
can have a Lambda function call the `get-ticket` API for the full ticket details.
Pipes can then send that information to a [target](eb-pipes-event-target.md "eb-pipes-event-target.md").

You can configure the following enrichments when setting up a pipe in EventBridge:

- API destination
- Amazon API Gateway
- Lambda function
- Step Functions state machine

###### Note

EventBridge Pipes only supports [Express workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") as enrichments.
EventBridge invokes enrichments synchronously because it must wait for a response from the
enrichment before invoking the target.

Enrichment responses are limited to a maximum size of 6MB.

You can also transform the data you receive from the source before sending it for
enhancement. For more information, see [Amazon EventBridge Pipes input transformation](eb-pipes-input-transformation.md "eb-pipes-input-transformation.md").

## Filtering events using enrichment

EventBridge Pipes passes the enrichment responses directly to the configured target. This
includes array responses for targets that support batches. For more information about
batch behavior, see [Amazon EventBridge Pipes batching and concurrency](eb-pipes-batching-concurrency.md "eb-pipes-batching-concurrency.md"). You can also use your
enrichment as a filter and pass fewer events than were received from the source. If you
don’t want to invoke the target, return an empty response, such as `""`,
`{}`, or `[]`.

###### Note

If you want to invoke the target with an empty payload, return an array with empty JSON `[{}]`.

## Invoking enrichments

EventBridge invokes enrichments synchronously (invocation type set to `REQUEST_RESPONSE`) because it must wait for a response from the
enrichment before invoking the target.

###### Note

For Step Functions state machines, EventBridge only supports [Express
workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") as enrichments, because they can be invoked
synchronously.
