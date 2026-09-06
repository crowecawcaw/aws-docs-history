

# Process job documents
<a name="process-job-documents-implementation"></a>

When you create an OTA task, the jobs handler runs the following steps on your device. When an update is available, it requests the job document over MQTT.

1. Subscribes to the MQTT notification topics.

1. Calls the [StartNextPendingJobExecution](https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_StartNextPendingJobExecution.html) API for pending jobs.

1. Receives available job documents.

1. Processes updates based on your specified timeouts.

Using the jobs handler, the application can determine whether to take action immediately or wait until a specified timeout period.