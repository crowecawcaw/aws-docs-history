# Amazon AppFlow flows

With Amazon AppFlow, a _flow_ transfers data between a source and a
destination. Amazon AppFlow supports a variety of AWS services and SaaS applications as sources or
destinations.

A _data mapping_ determines how data from the source is placed in the
destination. You can map the fields in each source object to fields in the destination. You can
concatenate multiple fields in a source object to a single field in the destination. You can mask
the values of sensitive fields so that the destination field contains only an asterisk (\*). You
can also truncate fields to a fixed length.

A _filter_ controls which data records are transferred to the destination.
Amazon AppFlow transfers only the records that meet the filter criteria.

A _trigger_ determines how a flow runs. The following are the supported
flow trigger types:

- **Run on demand** — Users manually run the flow as needed.
- **Run on event** — Amazon AppFlow runs the flow in response to an event
  from a SaaS application.
- **Run on schedule** — Amazon AppFlow runs the flow on a recurring
  schedule.
  When a flow is run, Amazon AppFlow verifies that the data is available in the source, processes
  the data according to the flow configuration, and transfers the processed data to the
  destination.

###### To work with a flow

- [Creating flows](create-flow.md "create-flow.md")
- [Managing flows](flows-manage.md "flows-manage.md")
- [Cataloging flow output](flows-catalog.md "flows-catalog.md")
- [Partitioning and aggregating](flows-partition.md "flows-partition.md")
- [Flow triggers](flow-triggers.md "flow-triggers.md")
- [Private flows](private-flows.md "private-flows.md")
- [Flow notifications](flow-notifications.md "flow-notifications.md")
- [General information](general.md "general.md")
