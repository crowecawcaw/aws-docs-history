# Turning on Amazon ECS container metadata

You can turn on container metadata at the container instance level by setting the
`ECS_ENABLE_CONTAINER_METADATA` container agent variable to
`true`. You can set this variable in the
`/etc/ecs/ecs.config` configuration file and restart the agent.
You can also set it as a Docker environment variable at runtime when the agent container
is started. For more information, see [Amazon ECS container agent configuration](ecs-agent-config.md "ecs-agent-config.md").

If the `ECS_ENABLE_CONTAINER_METADATA` is set to `true` when the
agent starts, metadata files are created for any containers created from that point
forward. The Amazon ECS container agent cannot create metadata files for containers that were
created before the `ECS_ENABLE_CONTAINER_METADATA` container agent variable
was set to `true`. To ensure that all containers receive metadata files, you
should set this agent variable at container instance launch. The following is an example
user data script that will set this variable as well as register your container instance
with your cluster.

```
#!/bin/bash
cat <<'EOF' >> /etc/ecs/ecs.config
ECS_CLUSTER=`your_cluster_name`
ECS_ENABLE_CONTAINER_METADATA=true
EOF
```
