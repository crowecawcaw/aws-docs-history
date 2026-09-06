

# Viewing the service event log
<a name="next-gen-service-event-log"></a>

The service event log provides a chronological history of all events that have occurred for a service. You can use the event log to track changes, troubleshoot issues, and audit activity.

**To view the service event log (console)**

1. Navigate to your service.

1. Choose the **Actions** button.

1. Select **View event log**.

You can filter events by **Event type** and **Time range**. The following event types are recorded:
+ **Assertion created** – An assertion was added to the service.
+ **Assertion deleted** – An assertion was removed from the service.
+ **Assertion updated** – An existing assertion was modified.
+ **Achievability updated** – The achievability status of a policy component changed.
+ **Service created** – The service was created.
+ **Service deleted** – The service was deleted.
+ **Function created** – A service function was created.
+ **Function deleted** – A service function was deleted.
+ **Function resources added** – Resources were added to a service function.
+ **Function resources removed** – Resources were removed from a service function.
+ **Function updated** – A service function was updated.
+ **Input sources updated** – The service's input sources were modified.
+ **Policy associated** – A resilience policy was associated with the service.
+ **Policy disassociated** – A resilience policy was removed from the service.
+ **Resources associated** – New resources were discovered and associated with the service.
+ **Resources disassociated** – Resources were removed from the service.
+ **System associated** – The service was associated with a system.
+ **System disassociated** – The service was removed from a system.
+ **Workflow updated** – A workflow configuration was updated.

Each event entry shows the timestamp, event type, and a summary of what changed. Choose **Show details** to view additional information about a specific event.