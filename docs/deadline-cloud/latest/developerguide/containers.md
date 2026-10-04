

# Run portable jobs in containers
<a name="containers"></a>

Write job templates for the application interface that the workload needs. Don't write them for a specific execution technology. An environment can provide that interface in several ways. Examples include software installed on the worker, a conda or Rez environment, a Docker container, an Apptainer container, or another runtime.

Open Job Description (OpenJD) wrap actions separate what a task runs from where and how it runs. You can run the same job template locally without a wrapping environment. You can also attach a wrapping queue environment to run its actions in a container on Deadline Cloud. The job template doesn't contain Docker commands or identify a container image.

To set up container support on Deadline Cloud, you configure three layers:


| Layer | Responsibility | Configured in | 
| --- | --- | --- | 
| Fleet | Provides rootless Docker and optional GPU integration on workers. | A Linux service-managed fleet. | 
| Queue environment | Starts a session container and wraps environment and task actions. | The queue that receives container jobs. | 
| Job template | Defines the application command, arguments, parameters, and files. | A portable OpenJD job bundle. | 

The chapter includes the following topics:
+ [Set up container support in the console](containers-console-setup.md) prepares a fleet and queue.
+ [Building, tagging, and pushing a container image](containers-build-push.md) creates a versioned image in Amazon ECR.
+ [Docker queue environment overview](containers-queue-environment.md) explains how wrap actions run the job inside the image.
+ [Run a portable job locally and in a container](containers-portable-job.md) runs one job template locally and on Deadline Cloud.
+ [Share data between the worker session and container](containers-share-data.md) compares session and persistent storage.
+ [Security and best practices for container jobs](containers-security.md) describes image, runtime, and command construction practices.