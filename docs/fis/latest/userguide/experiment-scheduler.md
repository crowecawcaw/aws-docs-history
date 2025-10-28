# Scheduling experiments

With AWS Fault Injection Service (FIS), you can perform fault injection experiments on
your AWS workloads. These experiments run on templates that contain one or more actions to
run on specified targets. You can now schedule your experiments as a one-time task or
recurring tasks natively from the FIS Console. In addition to [scheduled
rules](../../../eventbridge/latest/userguide/eb-create-rule-schedule.md "../../../eventbridge/latest/userguide/eb-create-rule-schedule.md"), FIS now offers a new scheduling capability. FIS now integrates with
EventBridge Scheduler and creates rules on your behalf. EventBridge Scheduler is a
serverless scheduler that allows you to create, run, and manage tasks from one central,
managed service.

###### Important

Experiment Scheduler with AWS Fault Injection Service is not available in AWS GovCloud (US-East) and AWS
GovCloud (US-West).

###### Topics

- [Create a scheduler role](getting-started.md "getting-started.md")
- [Create an experiment schedule](scheduling-an-experiment.md "scheduling-an-experiment.md")
- [Update an experiment schedule](update-schedule.md "update-schedule.md")
- [Disable or delete an experiment schedule](delete-schedule.md "delete-schedule.md")
