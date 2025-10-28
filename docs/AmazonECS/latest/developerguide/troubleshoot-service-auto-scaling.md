# Troubleshooting service auto

scaling in Amazon ECS

Application Auto Scaling turns off scale-in processes while Amazon ECS deployments are in progress, and they
resume once the deployment has completed. However, scale-out processes continue to
occur, unless suspended, during a deployment. For more information, see [Suspending and resuming scaling for Application Auto Scaling](../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md "../../../autoscaling/application/userguide/application-auto-scaling-suspend-resume-scaling.md").
