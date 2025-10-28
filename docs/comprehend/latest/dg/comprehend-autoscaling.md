# Auto scaling with endpoints

Instead of manually adjusting the number of inference units provisioned for your document
classification endpoints and entity recognizer endpoints, you can use auto scaling to
automatically set endpoint provisioning to fit your capacity needs.

There are two ways to use auto scaling to adjust the number of inference units provisioned
for your endpoint:

- [Target tracking](targettracking.md "targettracking.md"): Set auto scaling to
  adjust endpoint provisioning to fit capacity needs based on usage.
- [Scheduled scaling](ScheduledScaling.md "ScheduledScaling.md"): Set auto scaling to
  adjust endpoint provisioning to fit capacity needs on a specified schedule.
  You can set auto scaling only with the AWS Command Line Interface (AWS CLI). For more information about auto
  scaling, see [What is Application Auto Scaling?](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md")
