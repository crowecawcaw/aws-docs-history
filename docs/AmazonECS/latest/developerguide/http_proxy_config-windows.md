# Using an HTTP proxy for Amazon ECS Windows container

instances

You can configure your Amazon ECS container instances to use an HTTP proxy for both the Amazon ECS
container agent and the Docker daemon. This is useful if your container instances do not
have external network access through an Amazon VPC internet gateway, NAT gateway, or
instance.

To configure your Amazon ECS Windows container instance to use an HTTP proxy, set the following
variables at launch time (with Amazon EC2 user data).

`[Environment]::SetEnvironmentVariable("HTTP_PROXY",
 "http://`proxy.mydomain:port`",
 "Machine")`

Set `HTTP_PROXY` to the hostname (or IP address) and port number of
an HTTP proxy to use for the Amazon ECS agent to connect to the internet. For
example, your container instances may not have external network access through
an Amazon VPC internet gateway, NAT gateway, or instance.

`[Environment]::SetEnvironmentVariable("NO_PROXY",
 "169.254.169.254,169.254.170.2,\\.\pipe\docker_engine", "Machine")`

Set `NO_PROXY` to
`169.254.169.254,169.254.170.2,\\.\pipe\docker_engine` to filter
EC2 instance metadata, IAM roles for tasks, and Docker daemon traffic from the
proxy.

###### Example Windows HTTP proxy user data script

The example user data PowerShell script below configures the Amazon ECS container agent and
the Docker daemon to use an HTTP proxy that you specify. You can also specify a cluster
into which the container instance registers itself.

To use this script when you launch a container instance, follow the steps in [Launching an Amazon ECS Windows container
instance](launch_window-container_instance.md "launch_window-container_instance.md"). Just copy and paste the PowerShell
script below into the **User data** field (be sure to substitute the
red example values with your own proxy and cluster information).

###### Note

The `-EnableTaskIAMRole` option is required to enable IAM roles for
tasks. For more information, see [Amazon EC2 Windows instance additional configuration](task-iam-roles.md#windows_task_IAM_roles "task-iam-roles.md#windows_task_IAM_roles").

```
<powershell>
Import-Module ECSTools

$proxy = "http://`proxy.mydomain:port`"
[Environment]::SetEnvironmentVariable("HTTP_PROXY", $proxy, "Machine")
[Environment]::SetEnvironmentVariable("NO_PROXY", "169.254.169.254,169.254.170.2,\\.\pipe\docker_engine", "Machine")

Restart-Service Docker
Initialize-ECSAgent -Cluster `MyCluster` -EnableTaskIAMRole
</powershell>
```
