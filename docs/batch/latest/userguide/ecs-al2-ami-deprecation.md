

# Amazon ECS Amazon Linux 2 AMI deprecation
<a name="ecs-al2-ami-deprecation"></a>

AWS is ending support for Amazon ECS Amazon Linux 2-optimized and accelerated AMIs on June 30, 2026. On January 12, 2026, AWS Batch changed the default AMI for new Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023. Effective June 30, 2026, AWS Batch will block creation of new Amazon ECS compute environments using Batch-provided Amazon Linux 2 AMIs. After this date, you can only create new Amazon ECS compute environments using Amazon Linux 2023 or customer-provided AMIs.

**Important**  
We strongly recommend migrating your existing AWS Batch Amazon ECS compute environments to Amazon Linux 2023 prior to June 30, 2026. Existing compute environments will continue to operate after this date, but will no longer receive software updates, security patches, or bug fixes from AWS. It is your responsibility to maintain Amazon Linux 2 compute environments after end-of-life.

You can track the migration status of your affected Amazon ECS compute environments using AWS Health planned lifecycle events. For more information, see [AWS Health Planned lifecycle events](batch-planned-lifecycle-events.md).

For more information about the Amazon Linux 2 end-of-life, see [Amazon Linux 2 FAQs](https://aws.amazon.com/amazon-linux-2/faqs/).

For information about differences between Amazon Linux 2 and Amazon Linux 2023, see [Compare Amazon Linux 2023 and Amazon Linux 2](https://docs.aws.amazon.com/linux/al2023/ug/compare-with-al2.html) in the *Amazon Linux 2023 User Guide*.

For information about changes in Amazon Linux 2023 for Amazon ECS-optimized AMI, see [Migrating from an Amazon Linux 2 to an Amazon Linux 2023 Amazon ECS-optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/al2-to-al2023-ami-transition.html) in the *Amazon ECS User Guide*.

For help migrating AWS Batch Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023, see [How to migrate from ECS AL2 to ECS AL2023](ecs-migration-2023.md).