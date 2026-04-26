# Private registry permissions in Amazon ECR

Amazon ECR uses a **registry policy** to grant permissions to an AWS
principal at the private registry level.

Amazon ECR allows all ECR actions in the policy and enforces the registry policy in all ECR requests. You can use registry policies to grant permissions for actions such as replication configuration, pull-through cache rule creation, and repository creation. For the full list of API
actions, see the*[Amazon ECR API Guide](../APIReference/Welcome.md "../APIReference/Welcome.md")*.
For information about
general settings for your Amazon ECR private registry, see [Private registry settings in Amazon ECR](registry-settings.md "registry-settings.md").

###### Note

While it is possible to add the `ecr:*` action to a private registry
policy, it is considered best practice to only add the specific actions required
based on the feature you're using rather than use a wildcard.

###### Topics

- [Private registry policy examples for Amazon ECR](registry-permissions-examples.md "registry-permissions-examples.md")
- [Granting registry permissions for cross account replication in Amazon ECR](registry-permissions-create-replication.md "registry-permissions-create-replication.md")
- [Granting registry permissions for pull through cache in Amazon ECR](registry-permissions-create-pullthroughcache.md "registry-permissions-create-pullthroughcache.md")
