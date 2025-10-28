# Logging and monitoring

After you submit a quantum task through the Amazon Braket service, you can
closely monitor the status and progression of that task through the Amazon Braket
SDK and console. This provides you with a centralized interface to track the
implementation of your workloads, identify any potential bottlenecks or issues,
and take appropriate actions to optimize the performance and reliability of your
quantum applications. When the quantum task completes, Braket saves
the results in your specified Amazon S3 location. Completion time for quantum tasks can
vary, especially for those running on quantum processing unit (QPU) devices.
This is largely due to the length of the execution queue, as quantum hardware
resources are shared among multiple users.

**List of status types:**

- `CREATED` – Amazon Braket received your quantum task.
- `QUEUED` – Amazon Braket processed your quantum task and it is now waiting to
  run on the device.
- `RUNNING` – Your quantum task is running on a QPU or on-demand simulator.
- `COMPLETED` – Your quantum task finished running on the QPU or on-demand
  simulator.
- `FAILED` – Your quantum task attempted to run and failed. Depending on the
  reason your quantum task failed, try submitting your quantum task again.
- `CANCELLED` – You cancelled the quantum task. The quantum task did not run.

###### In this section:

- [Tracking quantum tasks from the Amazon Braket SDK](braket-monitor-tasks-sdk.md "braket-monitor-tasks-sdk.md")
- [Monitoring quantum tasks through the Amazon Braket console](braket-monitor-console.md "braket-monitor-console.md")
- [Tagging Amazon Braket resources](braket-tagging-resources.md "braket-tagging-resources.md")
- [Monitoring your quantum tasks with EventBridge](braket-monitor-eventbridge.md "braket-monitor-eventbridge.md")
- [Monitoring your metrics with CloudWatch](braket-monitor-metrics.md "braket-monitor-metrics.md")
- [Logging your quantum tasks with CloudTrail](braket-ctlogs.md "braket-ctlogs.md")
- [Advanced logging with Amazon Braket](braket-monitor-logging.md "braket-monitor-logging.md")
