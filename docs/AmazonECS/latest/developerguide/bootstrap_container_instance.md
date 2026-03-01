# Bootstrapping Amazon ECS Linux container instances to pass data

When you launch an Amazon EC2 instance, you can pass user data to the EC2 instance. The data
can be used to perform common automated configuration tasks and even run scripts when the
instance boots. For Amazon ECS, the most common use cases for user data are to pass configuration
information to the Docker daemon and the Amazon ECS container agent.

You can pass multiple types of user data to Amazon EC2, including cloud boothooks, shell
scripts, and `cloud-init` directives. For more information about these and other
format types, see the [Cloud-Init
documentation](https://cloudinit.readthedocs.io/en/latest/explanation/format.html "https://cloudinit.readthedocs.io/en/latest/explanation/format.html").

To pass the user data when using the Amazon EC2 launch wizard, see [Launching an Amazon ECS Linux container instance](launch_container_instance.md "launch_container_instance.md").

You can configure the container instance to pass data in the container agent configuration
or in the Docker daemon configuration.

## Amazon ECS container agent

The Linux variants of the Amazon ECS-optimized AMI look for agent configuration data in the
`/etc/ecs/ecs.config` file when the container agent starts. You
can specify this configuration data at launch with Amazon EC2 user data. For more information
about available Amazon ECS container agent configuration variables, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

To set only a single agent configuration variable, such as the cluster name, use
**echo** to copy the variable to the configuration file:

```
#!/bin/bash
echo "ECS_CLUSTER=`MyCluster`" >> /etc/ecs/ecs.config
```

If you have multiple variables to write to `/etc/ecs/ecs.config`,
use the following `heredoc` format. This format writes everything between the
lines beginning with **cat** and `EOF` to the configuration
file.

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
`ECS_CLUSTER=MyCluster
ECS_ENGINE_AUTH_TYPE=docker
ECS_ENGINE_AUTH_DATA={"https://index.docker.io/v1/":{"username":"my_name","password":"my_password","email":"email@example.com"}}
ECS_LOGLEVEL=debug`
`ECS_WARM_POOLS_CHECK=true`
EOF
```

To set custom instance attributes, set the `ECS_INSTANCE_ATTRIBUTES`
environment variable.

```
#!/bin/bash
cat <<'EOF' >> ecs.config
ECS_INSTANCE_ATTRIBUTES={"envtype":"prod"}
EOF
```

## Docker daemon

You can specify Docker daemon configuration information with Amazon EC2 user data. For more
information about configuration options, see [the Docker
daemon documentation](https://docs.docker.com/reference/cli/dockerd/ "https://docs.docker.com/reference/cli/dockerd/").

###### Note

AWS doesn't support custom Docker configurations, because they can sometimes conflict with future Amazon ECS changes or features without warning.

In the example below, the custom options are added to the Docker daemon configuration
file, `/etc/docker/daemon.json` which is then specified in the user
data when the instance is launched.

```
#!/bin/bash
cat <<EOF >/etc/docker/daemon.json
{"debug": true}
EOF
systemctl restart docker --no-block
```

In the example below, the custom options are added to the Docker daemon configuration
file, `/etc/docker/daemon.json` which is then specified in the user
data when the instance is launched. This example shows how to disable the docker-proxy
in the Docker daemon config file.

```
#!/bin/bash
cat <<EOF >/etc/docker/daemon.json
{"userland-proxy": false}
EOF
systemctl restart docker --no-block
```
