# Migration from public preview FAQ

This FAQ covers common questions about migrating AWS Agent Registry from public preview to general availability, including timeline, requirements, and migration resources.

AWS Agent Registry is currently available in public preview under the `bedrock-agentcore` namespace. Starting August 6, 2026, AWS Agent Registry moves to the generally available `agent-registry` namespace. If you use AWS Agent Registry during the public preview, you must migrate your registry data. You must also update your endpoints, IAM policies, SDK clients, CLI scripts, and configurations.

## What is changing in AWS Agent Registry?

Starting August 6, 2026, AWS Agent Registry moves from the public preview `bedrock-agentcore` namespace to the generally available `agent-registry` namespace. This change affects the following customer-facing surfaces:

- Service endpoints (data plane and control plane)
- IAM action prefixes and service principals
- SDK client class names and CLI command namespaces
- Resource ARN formats
- AWS CloudFormation, CDK, and Terraform resource types
- AWS CloudTrail event sources and Amazon EventBridge event sources
- Amazon CloudWatch metric namespaces
- AWS Service Quotas

You also need to migrate your existing registry data (registries and records) to the new namespace.

In addition to the namespace migration, AWS Agent Registry introduces API schema changes to registry and registry records that impact the Create, Update, Search, List, and Get APIs for these resources. These changes are in response to customer feedback during the public preview. We provide a comprehensive list of all API changes a few weeks before August 6, 2026, to help you plan your migration.

## Can I continue using Registry on the `bedrock-agentcore` namespace?

Your existing Registry usage on the `bedrock-agentcore` namespace continues to work without interruption until September 17, 2026. However, we recommend that you begin planning your migration as soon as migration tooling becomes available on August 6, 2026. This gives you six weeks to migrate to the new `agent-registry` namespace before the `bedrock-agentcore` namespace is shut down.

## Do I need to take action right now?

No immediate action is required—we provide advance notice with detailed migration instructions a few weeks before August 6, 2026, explaining what changes and how to migrate so you can plan accordingly. The migration officially begins on August 6, when we make migration tooling available.

## What is the migration timeline?

- **August 6, 2026**—New `agent-registry` namespace launches. Migration tooling available. You can begin migrating.
- **September 17, 2026**—Migration window closes. We shut down the old `bedrock-agentcore` namespace endpoints.

## What happens if I don’t migrate by September 17, 2026?

All calls to the old `bedrock-agentcore` endpoints receive `4xx` errors. You cannot access your data on the old namespace. To obtain any remaining data after this date, you must request it through AWS Support before permanent deletion.

## Will my data be automatically migrated?

No. You must initiate the migration yourself. We provide migration tooling to assist you.

## Will there be API shape changes or just a namespace change?

Yes, there are schema changes to registry and registry records that impact the Create, Update, Search, List, and Get APIs for these resources. We provide a comprehensive list of all API changes a few weeks before August 6, 2026.

## How long will the data migration take?

Details on the migration tooling are shared on August 6, 2026.

## Where can I get help?

For help, contact [AWS Support](https://aws.amazon.com/support "https://aws.amazon.com/support").
