# Private registry permissions in Amazon ECR

Amazon ECR uses a **registry policy** to grant permissions to an AWS
principal at the private registry level.

The scope is set by choosing the registry policy version. There are two versions with
different registry policy scope: version 1 (V1) and version 2 (V2). V2 is the expanded
registry policy scope that includes all ECR permissions. For the full list of API
actions, see the*[Amazon ECR API Guide](../APIReference/Welcome.md "../APIReference/Welcome.md")*. The V2
version is the default registry policy scope. For more information about viewing or
setting your registry policy scope, see [Switching to the extended
registry policy scope](registry-permissions-account-settings.md "registry-permissions-account-settings.md"). For information about
general settings for your Amazon ECR private registry, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").

The versions are detailed as follows.

- **V1** – For version 1, Amazon ECR only
  enforces the following permissions at the private registry level.
  - `ecr:ReplicateImage` – Grants permission to another
    account, referred to as the source registry, to replicate its images to
    your registry. This is only used for cross-account replication.
  - `ecr:BatchImportUpstreamImage` – Grants permission
    to retrieve the external image and import it to your private
    registry.
  - `ecr:CreateRepository` – Grants permission to create
    a repository in a private registry. This permission is required if the
    repository storing either the replicated or cached images doesn't
    already exist in the private registry.

- **V2** – For version 2, Amazon ECR allows all
  ECR actions in the policy and enforces the registry policy in all ECR
  requests.
  You can use the console or the CLI to view or change your registry policy
  scope.

###### Note

While it is possible to add the `ecr:*` action to a private registry
policy, it is considered best practice to only add the specific actions required
based on the feature you're using rather than use a wildcard.

###### Topics

- [Private registry policy examples for
  Amazon ECR](registry-permissions-examples.md "registry-permissions-examples.md")
- [Switching to the extended
  registry policy scope](registry-permissions-account-settings.md "registry-permissions-account-settings.md")
- [Granting registry
  permissions for cross account replication in Amazon ECR](registry-permissions-create-replication.md "registry-permissions-create-replication.md")
- [Granting registry
  permissions for pull through cache in Amazon ECR](registry-permissions-create-pullthroughcache.md "registry-permissions-create-pullthroughcache.md")
