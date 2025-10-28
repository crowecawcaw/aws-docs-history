# Choosing Fargate task sizes for Amazon ECS

For AWS Fargate task definitions, you're required to specify CPU and memory at the
task level, and do not need to account for any overhead. You can also specify CPU and
memory at the container level for Fargate tasks. However, doing so isn't required. The
resource limits must be greater than or equal to any reservations that you declared. In
most cases, you can set them to the sum of the reservations of each of the container
that's declared in your task definition. Then, round the number up to the nearest
Fargate size. For more information about the available sizes, see [Task CPU
and memory](fargate-tasks-services.md#fargate-tasks-size "fargate-tasks-services.md#fargate-tasks-size").
