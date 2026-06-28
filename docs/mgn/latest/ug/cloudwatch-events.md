NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# AWS Transform MGN EventBridge sample events

AWS Transform MGN sends events to Amazon EventBridge whenever a Source server
launch has completed, a Source server reaches the READY\_FOR\_TEST lifecycle state for the first
time, and when the data replication state becomes Stalled or when the data replication state
is no longer Stalled . You can use EventBridge and these events to write rules that take
actions, such as notifying you, when a relevant event occurs. For more information, see [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")

AWS Transform MGN sends events on a best-effort basis to EventBridge. Event
delivery is not guaranteed.
