

# Use FSx for Windows File Server volumes with Amazon ECS
<a name="wfsx-volumes"></a>

FSx for Windows File Server provides fully managed Windows file servers, that are backed by a Windows file system. When using FSx for Windows File Server together with ECS, you can provision your Windows tasks with persistent, distributed, shared, static file storage. For more information, see [What Is FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).

**Note**  
EC2 instances that use the Amazon ECS-Optimized Windows Server 2016 Full AMI do not support FSx for Windows File Server ECS task volumes.  
You can't use FSx for Windows File Server volumes in a Windows containers on Fargate configuration. Instead, you can [modify containers to mount them on startup](https://aws.amazon.com/blogs/containers/use-smb-storage-with-windows-containers-on-aws-fargate/).

You can use FSx for Windows File Server to deploy Windows workloads that require access to shared external storage, highly-available Regional storage, or high-throughput storage. You can mount one or more FSx for Windows File Server file system volumes to an Amazon ECS container that runs on an Amazon ECS Windows instance. You can share FSx for Windows File Server file system volumes between multiple Amazon ECS containers within a single Amazon ECS task.

To enable the use of FSx for Windows File Server with ECS, include the FSx for Windows File Server file system ID and the related information in a task definition. This is in the following example task definition JSON snippet. Before you create and run a task definition, you need the following.
+ An ECS Windows EC2 instance that's joined to a valid domain. It can be hosted by an [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), on-premises Active Directory or self-hosted Active Directory on Amazon EC2.
+ An AWS Secrets Manager secret or Systems Manager parameter that contains the credentials that are used to join the Active Directory domain and attach the FSx for Windows File Server file system. The credential values are the name and password credentials that you entered when creating the Active Directory.

For a related tutorial, see [Learn how to configure FSx for Windows File Server file systems for Amazon ECS](tutorial-wfsx-volumes.md).

## Considerations
<a name="wfsx-volume-considerations"></a>

Consider the following when using FSx for Windows File Server volumes:
+ FSx for Windows File Server volumes are natively supported with Amazon ECS on Windows Amazon EC2 instances — Amazon ECS automatically manages the mount through task definition configuration.

  On Linux Amazon EC2 instances, Amazon ECS can't automatically mount FSx for Windows File Server volumes through task definitions. However, you can manually mount an FSx for Windows File Server file share on a Linux EC2 instance at the host level and then bind-mount that path into your Amazon ECS containers. For more information, see [Mounting Amazon FSx file shares from Linux](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/map-shares-linux.html).
**Important**  
This is a self-managed configuration. For guidance on mounting and maintaining FSx for Windows File Server file shares on Linux, refer to the [FSx for Windows File Server documentation](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/).
**Important**  
When using a manually mounted FSx for Windows File Server share on Linux EC2 instances, Amazon ECS and FSx for Windows File Server operate independently — Amazon ECS does not monitor the Amazon FSx mount, and FSx for Windows File Server does not track Amazon ECS task placement or lifecycle events. You are responsible for ensuring network reachability between your Amazon ECS container instances and the Amazon FSx file system, implementing mount health checks, and handling reconnection logic to tolerate failover events.
+ FSx for Windows File Server with Amazon ECS doesn't support AWS Fargate.
+ FSx for Windows File Server with Amazon ECS isn't supported on Amazon ECS Managed Instances.
+ FSx for Windows File Server with Amazon ECS with `awsvpc` network mode requires version `1.54.0` or later of the container agent.
+ The maximum number of drive letters that can be used for an Amazon ECS task is 23. Each task with an FSx for Windows File Server volume gets a drive letter assigned to it.
+ By default, task resource cleanup time is three hours after the task ended. Even if no tasks use it, a file mapping that's created by a task persists for three hours. You can configure the default cleanup time by using the Amazon ECS environment variable `ECS_ENGINE_TASK_CLEANUP_WAIT_DURATION`. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md).
+ Tasks typically only run in the same VPC as the FSx for Windows File Server file system. However, it's possible to have cross-VPC support if there's an established network connectivity between the Amazon ECS cluster VPC and the FSx for Windows File Server file-system through VPC peering.
+ You control access to an FSx for Windows File Server file system at the network level by configuring the VPC security groups. Only tasks that are hosted on EC2 instances joined to the Active Directory domain with correctly configured Active Directory security groups can access the FSx for Windows File Server file-share. If the security groups are misconfigured, Amazon ECS fails to launch the task with the following error message: `unable to mount file system {{fs-id}}`.” 
+ FSx for Windows File Server is integrated with AWS Identity and Access Management (IAM) to control the actions that your IAM users and groups can take on specific FSx for Windows File Server resources. With client authorization, customers can define IAM roles that allow or deny access to specific FSx for Windows File Server file systems, optionally require read-only access, and optionally allow or disallow root access to the file system from the client. For more information, see [Security](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/security.html) in the Amazon FSx Windows User Guide.