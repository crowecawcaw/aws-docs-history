

# Wave execution
<a name="transform-vmware-ms-wave-execution"></a>

After you complete the prerequisites and configure migration defaults, you migrate your servers in waves. Each wave represents a group of servers that are migrated together. For each wave, the agent walks you through the following steps:

1. [Step 1: Set up migration wave](transform-vmware-ms-setup-wave.md) – The agent configures your target account, validates permissions, and sets up resource tagging automatically.

1. [Step 2: Validate and confirm inventory](transform-vmware-ms-validate-inventory.md) – Review your server configurations, instance type recommendations, and network assignments before migration begins.

1. [Step 3: Deploy replication agents](transform-vmware-ms-deploy-agents.md) – The agent can deploy agents across all servers in a wave without requiring manual access to each server individually.

1. [Step 4: Data replication](transform-vmware-ms-data-replication.md) – Continuous block-level replication keeps your target environment synchronized with source servers until you are ready for cutover.

1. [Step 5: Test](transform-vmware-ms-testing.md) – Launch test instances to validate your migrated servers before committing to the final cutover, and mark applications as ready for cutover.

1. [Step 6: Cutover](transform-vmware-ms-cutover.md) – Complete the migration with minimal downtime. The agent coordinates the final switchover and verifies success.

For waves with a *containerize* migration strategy, AWS Transform runs the source code containerization workflow instead of the rehost steps. The containerization workflow guides you through cloning source code, generating Docker artifacts, publishing container images, and deploying to Amazon Elastic Container Service or Amazon Elastic Kubernetes Service. For the full containerization workflow, see [Source code containerization](transform-containers.md).