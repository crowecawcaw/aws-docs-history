# Sync an upstream registry with an Amazon ECR private registry

Using pull through cache rules, you can sync the contents of an upstream registry with
your Amazon ECR private registry.

Amazon ECR currently supports creating pull through cache rules for the following upstream
registries:

- Amazon ECR Public, Kubernetes container image registry, and Quay (doesn't require
  authentication)
- Docker Hub, Microsoft Azure Container Registry, GitHub Container Registry, and GitLab Container Registry (requires authentication with AWS Secrets Manager
  secret)
- Amazon ECR (requires authentication with AWS IAM role)
  For GitLab Container Registry, Amazon ECR supports pull through cache only with GitLab's Software as a Service
  (SaaS) offering. For more information about using GitLab's SaaS offering, see [GitLab.com](https://docs.gitlab.com/17.5/subscriptions/choosing_subscription/ "https://docs.gitlab.com/17.5/subscriptions/choosing_subscription/").

For upstream registries that require authentication with secrets (such as Docker Hub),
you must store your credentials in an AWS Secrets Manager secret. You can use the Amazon ECR console to
create Secrets Manager secrets for each authenticated upstream registry. For more information about
creating a Secrets Manager secret using the Secrets Manager console, see [Storing your upstream
repository credentials in an AWS Secrets Manager secret](pull-through-cache-creating-secret.md "pull-through-cache-creating-secret.md").

For Amazon ECR, you must create an IAM role if the upstream and downstream Amazon ECR registries
belong to different AWS account. For more information about creating an IAM role, see
[IAM policies
required for cross-account ECR to ECR pull through cache](pull-through-cache-private.md#pull-through-cache-private-permissions "pull-through-cache-private.md#pull-through-cache-private-permissions").

After you've created a pull through cache rule for the upstream registry, pull an
image from that upstream registry using your Amazon ECR private registry URI. Amazon ECR then creates
a repository and caches that image in your private registry. For subsequent pull requests of
the cached image with a given tag, Amazon ECR checks the upstream registry for a new version of
the image with that specific tag and attempts to update the image in your private registry
at least once every 24 hours.

## Repository creation templates

Amazon ECR has added support for repository creation templates, which gives you the control
to specify initial configurations for new repositories created by Amazon ECR on your behalf
using pull through cache rules. Each template contains a repository namespace prefix
which is used to match new repositories to a specific template. Templates can specify
the configuration for all repository settings including resource-based access policies,
tag immutability, encryption, and lifecycle policies. The settings in a repository
creation template are only applied during repository creation and don't have any effect
on existing repositories or repositories created using any other method. For more
information, see [Templates to control repositories created
during a pull through cache, create on push, or replication action](repository-creation-templates.md "repository-creation-templates.md").

## Considerations for using pull

through cache rules

Consider the following when using Amazon ECR pull through cache rules.

- Creating pull through cache rules isn't supported in the following
  Regions.
  - China (Beijing) (`cn-north-1`)
  - China (Ningxia) (`cn-northwest-1`)
  - AWS GovCloud (US-East) (`us-gov-east-1`)
  - AWS GovCloud (US-West) (`us-gov-west-1`)

- AWS Lambda doesn't support pulling container images from Amazon ECR using a pull
  through cache rule.
- When pulling images using pull through cache, the Amazon ECR FIPS service
  endpoints aren't supported the first time an image is pulled. Using the
  Amazon ECR FIPS service endpoints work on subsequent pulls though.
- For upstream repositories that require authentication, when an image is pulled through the
  Amazon ECR private registry URI for the first time or to update the cache, the image pulls are initiated by the
  user associated to the credentials configured in the pull through cache rule. Subsequent pulls
  will return the image directly from the cache in the customer's private registry.
- For upstream repositories that do not require authentication, when an image is pulled through the Amazon ECR private registry URI, the
  image pulls are initiated by AWS IP addresses.
- When a cached image is pulled through the Amazon ECR private registry URI,
  Amazon ECR checks the upstream repository at least once every 24 hours to verify
  whether the cached image is the latest version. If there is a newer image in
  the upstream registry, Amazon ECR attempts to update the cached image. This timer
  is based off the last pull of the cached image.
- If Amazon ECR is unable to update the image from the upstream registry for any
  reason and the image is pulled, the last cached image will still be
  pulled.
- When creating the Secrets Manager secret that contains the upstream registry
  credentials, the secret name must use the `ecr-pullthroughcache/`
  prefix. The secret must also be in the same account and Region that the pull
  through cache rule is created in.
- When a multi-architecture image is pulled using a pull through cache rule,
  the manifest list and each image referenced in the manifest list are pulled
  to the Amazon ECR repository. If you only want to pull a specific architecture,
  you can pull the image using the image digest or tag associated with the
  architecture rather than the tag associated with the manifest list.
- Amazon ECR uses a service-linked IAM role, which provides the permissions
  needed for Amazon ECR to create the repository, retrieve the Secrets Manager secret value
  for authentication, and push the cached image on your behalf. The
  service-linked IAM role is created automatically when a pull through cache
  rule is created. For more information, see [Amazon ECR service-linked role for pull through
  cache](slr-pullthroughcache.md "slr-pullthroughcache.md").
- By default, the IAM principal pulling the cached image has the
  permissions granted to them through their IAM policy. You may use the
  Amazon ECR private registry permissions policy to further scope the permissions
  of an IAM entity. For more information, see [Using registry
  permissions](pull-through-cache-iam.md#pull-through-cache-registry-permissions "pull-through-cache-iam.md#pull-through-cache-registry-permissions").
- Amazon ECR repositories created using the pull through cache workflow are
  treated like any other Amazon ECR repository. All repository features, such as
  replication and image scanning are supported.
- When Amazon ECR creates a new repository on your behalf using a pull through
  cache action, the following default settings are applied to the repository
  unless there is a matching repository creation template. You can use a
  repository creation template to define the settings applied to repositories
  created by Amazon ECR on your behalf. For more information, see [Templates to control repositories created
  during a pull through cache, create on push, or replication action](repository-creation-templates.md "repository-creation-templates.md").
  - Tag immutability – Tag immutability specifies whether image
    tags can be overwritten. By default, image tags are mutable (can be
    overwritten). You can modify tag behavior by configuring tag exclusion
    filters in either the **Mutable tag exclusion** text
    box when **Mutable** is selected, or the
    **Immutable tag exclusion** text box when
    **Immutable** is selected.
  - Encryption – The default `AES256` encryption is
    used.
  - Repository permissions – Omitted, no repository permissions
    policy is applied.
  - Lifecycle policy – Omitted, no lifecycle policy is
    applied.
  - Resource tags – Omitted, no resource tags are
    applied.

- Turning on image tag immutability for repositories using a pull through
  cache rule will prevent Amazon ECR from updating images using the same
  tag.
- When an image is pulled using the pull through cache rule for the first
  time a route to the internet may be required. There are certain
  circumstances in which a route to the internet is required so it's best to
  set up a route to avoid any failures. Thus, if you've configured Amazon ECR to
  use an interface VPC endpoint using AWS PrivateLink then you need to ensure
  the first pull has a route to the internet. One way to do this is to create
  a public subnet in the same VPC, with an internet gateway, and then route
  all outbound traffic to the internet from their private subnet to the public
  subnet. Subsequent image pulls using the pull through cache rule don't
  require this. For more information, see [Example routing
  options](../../../vpc/latest/userguide/route-table-options.md "../../../vpc/latest/userguide/route-table-options.md") in the _Amazon Virtual Private Cloud User Guide_.
