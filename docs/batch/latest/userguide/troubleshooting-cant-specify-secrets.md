# Can't retrieve Secrets Manager secrets

If you use an AMI with an Amazon ECS agent that's earlier than version 1.16.0-1, then you must
use the Amazon ECS agent configuration variable
`ECS_ENABLE_AWSLOGS_EXECUTIONROLE_OVERRIDE=true` to use this feature. You can add it
to the `./etc/ecs/ecs.config` file to a new container instance when you create that
instance. Or, you can add it to an existing instance. If you add it to an existing instance, you
must restart the ECS agent after you add it. For more information, see [Amazon ECS
Container Agent Configuration](../../../AmazonECS/latest/developerguide/ecs-agent-config.md "../../../AmazonECS/latest/developerguide/ecs-agent-config.md") in the _Amazon Elastic Container Service Developer Guide_.
