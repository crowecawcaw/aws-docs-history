# Amazon ECS container agent configuration

**Applies to**: EC2 instances

The Amazon ECS container agent supports a number of configuration options, most of which you
set through environment variables.

If your container instance was launched with a Linux variant of the Amazon ECS-optimized AMI, you
can set these environment variables in the `/etc/ecs/ecs.config` file and
then restart the agent. You can also write these configuration variables to your container
instances with Amazon EC2 user data at launch time. For more information, see [Bootstrapping Amazon ECS Linux container instances to pass data](bootstrap_container_instance.md "bootstrap_container_instance.md").

If your container instance was launched with a Windows variant of the Amazon ECS-optimized AMI,
you can set these environment variables with the PowerShell SetEnvironmentVariable command
and then restart the agent. For more information, see [Run commands when you launch an EC2 instance with user data input](../../../AWSEC2/latest/UserGuide/user-data.md "../../../AWSEC2/latest/UserGuide/user-data.md") in the _Amazon EC2 User Guide_
and [Bootstrapping Amazon ECS Windows container instances to pass data](bootstrap_windows_container_instance.md "bootstrap_windows_container_instance.md").

If you are manually starting the Amazon ECS container agent (for non Amazon ECS-optimized AMIs), you
can use these environment variables in the **docker run** command that you
use to start the agent. Use these variables with the syntax
`--env=`VARIABLE_NAME`=`VARIABLE_VALUE``.
 For sensitive information, such as authentication credentials for private repositories, you
 should store your agent environment variables in a file and pass them all at one time with
 the `--env-file `path_to_env_file`` option. You can use
the following commands to add the variables.

```
sudo systemctl stop ecs
sudo vi /etc/ecs/ecs.config
# And add the environment variables with VARIABLE_NAME=VARIABLE_VALUE format.
sudo systemctl start ecs
```

## Run the Amazon ECS agent with the host PID

namespace

By default, the Amazon ECS agent runs with its own PID namespace. In the following
configurations, you can configure the Amazon ECS agent to run with the host PID
namespace:

- SELinux enforcing mode is enabled.
- Docker's SELinux security policy is set to true.

You can configure this behavior by setting the
`ECS_AGENT_PID_NAMESPACE_HOST` environment variable to `true`
in your `/etc/ecs/ecs.config` file. When this variable is enabled,
`ecs-init` will start the Amazon ECS agent container with the host's PID
namespace (`--pid=host`), allowing the agent to bootstrap itself properly in
SELinux-enforcing environments. This feature is available in Amazon ECS agent version `1.94.0` and later.

To enable this feature, add the following line to your `/etc/ecs/ecs.config` file:

```
ECS_AGENT_PID_NAMESPACE_HOST=true
```

After making this change, restart the Amazon ECS agent for the change to take effect:

```
sudo systemctl restart ecs
```

The following features will not work SELinux enforcing mode is enabled and the Docker security policy is set to true, even when `ECS_AGENT_PID_NAMESPACE_HOST=true` is set.

- Amazon ECS Exec
- Amazon EBS task attach
- Service Connect
- FireLens for Amazon ECS

## Available parameters

For information about the available Amazon ECS container agent configuration parameters,
see [Amazon
ECS Container Agent](https://github.com/aws/amazon-ecs-agent/blob/master/README.md "https://github.com/aws/amazon-ecs-agent/blob/master/README.md") on GitHub.
