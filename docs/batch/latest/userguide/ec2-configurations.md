# EC2 configurations

AWS Batch uses Amazon ECS optimized AMIs for EC2 and EC2 Spot compute environments. The default is
[Amazon Linux 2](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2ami "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2ami")
(`ECS_AL2`). Starting in January 2026, the default will change to [AL2023](../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2023ami "../../../AmazonECS/latest/developerguide/ecs-optimized_AMI.md#al2023ami") (`ECS_AL2023`).

AWS will end support for Amazon Linux 2. We recommend migrating AWS Batch Amazon ECS compute
environments to Amazon Linux 2023 to maintain optimal performance and security. For more
information, see [Amazon ECS Amazon Linux 2 AMI deprecation](ecs-al2-ami-deprecation.md "ecs-al2-ami-deprecation.md").

We recommend that you update existing Amazon Linux based compute environments to Amazon Linux 2023 to
prevent unforeseen workload interruptions, and continue to receive security and other
updates.

For help migrating AWS Batch from the Amazon Linux AMI to Amazon Linux 2023, see [How to migrate from ECS AL2 to ECS AL2023](ecs-migration-2023.md "ecs-migration-2023.md")

###### Topics

- [How to migrate from ECS AL2 to ECS AL2023](ecs-migration-2023.md "ecs-migration-2023.md")
