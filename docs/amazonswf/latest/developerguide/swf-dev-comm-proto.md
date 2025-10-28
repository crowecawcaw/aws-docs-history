# Polling for tasks in Amazon SWF

Deciders and activity workers communicate with Amazon SWF using _long polling_. The decider or
activity worker periodically initiates communication with Amazon SWF, notifying Amazon SWF of its availability to accept a
task, and then specifies a task list to get tasks from.

If a task is available on the specified task list, Amazon SWF returns it immediately in the response. If no task is
available, Amazon SWF holds the TCP connection open for up to 60 seconds so that, if a task becomes available during that
time, it can be returned in the same connection. If no task becomes available within 60 seconds, it returns an empty
response and closes the connection. (An empty response is a Task structure in which the value of taskToken is an
empty string.) If this happens, the decider or activity worker should poll again.

Long polling works well for high-volume task processing. Deciders and activity workers can manage their own
capacity, and it is easy to use when the deciders and activity workers are behind a firewall.

For more information, see [Polling for Decision Tasks](swf-dg-dev-deciders.md#swf-dg-polling-decision-tasks "swf-dg-dev-deciders.md#swf-dg-polling-decision-tasks") and [Polling for Activity Tasks](swf-dg-develop-activity.md#swf-dg-polling-activity-tasks "swf-dg-develop-activity.md#swf-dg-polling-activity-tasks").
