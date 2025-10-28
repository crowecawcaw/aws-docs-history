# AWS Batch events

AWS Batch sends job status change events to EventBridge. AWS Batch tracks the state of your jobs. If a previously submitted
job's status changes, an event is invoked. For example, if a job in the `RUNNING` status moves to the
`FAILED` status. These events are classified as job state change events.

###### Note

AWS Batch might add other event types, sources, and details in the future. If you're
programmatically deserializing event JSON data, make sure that your application is prepared to
handle unknown properties. This is to avoid issues if and when these additional properties are
added.
