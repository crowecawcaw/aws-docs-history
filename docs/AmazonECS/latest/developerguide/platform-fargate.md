# Fargate platform versions for Amazon ECS

AWS Fargate platform versions are used to refer to a specific runtime environment for
Fargate task infrastructure. It is a combination of the kernel and container
runtime versions. You select a platform version when you run a task or when you create a
service to maintain a number of identical tasks.

New revisions of platform versions are released as the runtime environment evolves, for example, if
there are kernel or operating system updates, new features, bug fixes, or security updates.
A Fargate platform version is updated by making a new platform version revision. Each task
runs on one platform version revision during its
lifecycle. If you want to use the latest platform version revision, then you must start a new
task. A new task that runs on Fargate always runs on the latest revision
of a platform version, ensuring that tasks are always started on secure and patched infrastructure.

If a security issue is found that affects an existing platform version, AWS creates a
new patched revision of the platform version and retires tasks running on the
vulnerable revision. In some cases, you may be notified that your tasks on Fargate
have been scheduled for retirement. For more information, see [Task retirement and maintenance for AWS Fargate on Amazon ECS](task-maintenance.md "task-maintenance.md") .

You specify the platform version when you run a task, or deploy a service.

Consider the following when specifying a platform version:

- You can specify a a specific version number, for example `1.4.0`,
  or `LATEST`.

The **LATEST** Linux platform version is
`1.4.0`.

The **LATEST** Windows platform version is
`1.0.0`.

- If you want to update the platform version for a service, create a deployment.
  For example, assume that you have a service that runs tasks on the Linux
  platform version `1.3.0`. To change the service to run tasks on the
  Linux platform version `1.4.0`, you update your service and specify a
  new platform version. Your tasks are redeployed with the latest platform version
  and the latest platform version revision. For more information about
  deployments, see [Amazon ECS services](ecs_services.md "ecs_services.md").
- If your service is scaled up without updating the platform version, those
  tasks receive the platform version that was specified on the service's
  current deployment. For example, assume that you have a service that runs tasks
  on the Linux platform version `1.3.0`. If you increase the desired
  count of the service, the service scheduler starts the new tasks using the
  latest platform version revision of platform
  version `1.3.0`.
- New tasks always run on the latest revision of a platform version. This
  ensures tasks are always on secured and patched infrastructure.
- The platform version numbers for Linux containers and Windows
  containers on Fargate are independent. For example, the behavior, features, and software used
  in platform version `1.0.0` for Windows containers on Fargate aren't
  comparable to those of platform version `1.0.0` for Linux containers on Fargate.
- The following applies to Fargate Windows platform versions.

Microsoft Windows Server container images must be created from a specific version of Windows Server.
You must select the same version of Windows Server in the `platformFamily` when you run a task
or create a service that matches the Windows Server container image. Additionally, you can provide a
matching `operatingSystemFamily` in the task definition to prevent tasks from being run on
the wrong Windows version. For more information, see [Matching container host version with container image versions](https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility#matching-container-host-version-with-container-image-versions "https://learn.microsoft.com/en-us/virtualization/windowscontainers/deploy-containers/version-compatibility#matching-container-host-version-with-container-image-versions") on the
Microsoft Learn website.
