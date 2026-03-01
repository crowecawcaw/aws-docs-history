# Private registry settings in Amazon ECR

Amazon ECR uses private registry settings to configure features at the registry level. The
private registry settings are configured separately for each Region. You can use private
registry settings to configure the following features.

- **Registry permissions** – A registry permissions
  policy provides control over the replication and pull through cache permissions.
  For more information, see [Private registry permissions in Amazon ECR](registry-permissions.md "registry-permissions.md").
- **Pull through cache rules** – A pull through cache
  rule is used to cache images from an upstream registry in your Amazon ECR private
  registry. For more information, see [Sync an upstream registry with an Amazon ECR private registry](pull-through-cache.md "pull-through-cache.md").
- **Replication configuration** – The replication
  configuration is used to control whether your repositories are copied across
  AWS Regions or AWS accounts. For more information, see [Private image replication in Amazon ECR](replication.md "replication.md").
- **Repository creation templates** – A repository
  creation template is used to define the standard settings to apply when new
  repositories are created by Amazon ECR on your behalf. For example, repositories
  created by a pull through cache action, create on push, or replication. For more information, see [Templates to control repositories created during a pull through cache, create on push, or replication action](repository-creation-templates.md "repository-creation-templates.md").
- **Scanning configuration** – By default, your registry
  is enabled for basic scanning. You may enable enhanced scanning which provides
  an automated, continuous scanning mode that scans for both operating system and
  programming language package vulnerabilities. For more information, see [Scan images for software vulnerabilities in Amazon ECR](image-scanning.md "image-scanning.md").
- **Pull-time update exclusion** – You can configure
  pull-time update exclusions to prevent the last pull time from being updated for
  specific images when they are pulled. This is useful for images that are used
  for testing or CI/CD purposes where you don't want the pull time to affect
  lifecycle policy decisions. For more information, see [Pull-time update exclusions](pull-time-update-exclusions.md "pull-time-update-exclusions.md").
- **Blob mounting configuration** – The blob mounting configuration is used to
  control if the repositories within your registry share common layers rather than store
  duplicate layers. For more information, see [Blob mounting in Amazon ECR](blob-mounting.md "blob-mounting.md").
