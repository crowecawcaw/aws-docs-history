# Process job documents

When you create an OTA task, the jobs handler runs the following steps on your device.
When an update is available, it requests the job document over MQTT.

1. Subscribes to the MQTT notification topics.
2. Calls the
   [StartNextPendingJobExecution](../APIReference/API_StartNextPendingJobExecution.md "../APIReference/API_StartNextPendingJobExecution.md")
   API for pending jobs.
3. Receives available job documents.
4. Processes updates based on your specified timeouts.
   Using the jobs handler, the application can determine whether to take action immediately or wait until a specified timeout period.
