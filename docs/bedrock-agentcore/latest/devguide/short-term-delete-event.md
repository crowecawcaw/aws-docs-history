# Delete an event

The [DeleteEvent](../APIReference/API_DeleteEvent.md "../APIReference/API_DeleteEvent.md") operation removes individual events from your
AgentCore Memory. This operation helps maintain data privacy and relevance by letting you
selectively remove specific events from a session while preserving the broader
context and relationship structure within your application's memory.

###### Note

These are manual deletion operations, and do not overlap with automatic
deletion of events based on the `eventExpiryDuration` parameter set at the time of
[CreateEvent](../APIReference/API_CreateEvent.md "../APIReference/API_CreateEvent.md") operation. Also deleting an event doesn't remove
the structured information derived out of it from the long term memory. For more
information, see [DeleteMemoryRecord](../APIReference/API_DeleteMemoryRecord.md "../APIReference/API_DeleteMemoryRecord.md").
