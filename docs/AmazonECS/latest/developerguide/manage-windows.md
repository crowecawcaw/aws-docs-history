# Amazon ECS Windows container instance management

When you use EC2 instances for your Amazon ECS workloads, you are responsible for maintaining the instances.

Agent updates do not apply to Windows container instances. We recommend that you launch new
container instances to update the agent version in your Windows clusters.

###### Management procedures

- [Launching a container instance](launch_window-container_instance.md "launch_window-container_instance.md")
- [Bootstrapping container instances](bootstrap_windows_container_instance.md "bootstrap_windows_container_instance.md")
- [Using an HTTP proxy for Windows container
  instances](http_proxy_config-windows.md "http_proxy_config-windows.md")
- [Configuring container instances to receive Spot Instance notices](windows-spot-instance-draining-container.md "windows-spot-instance-draining-container.md")
