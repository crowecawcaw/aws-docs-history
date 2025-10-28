# Private image replication in Amazon ECR

You can configure your Amazon ECR private registry to support the replication of your
repositories. Amazon ECR supports both cross-Region and cross-account replication. For
cross-account replication to occur, the destination account must configure a registry
permissions policy to allow replication from the source registry to occur. For more
information, see [Private registry permissions in Amazon ECR](registry-permissions.md "registry-permissions.md").

###### Topics

- [Cross-account replication policy
  requirements](#replication-policy-clarification "#replication-policy-clarification")
- [Considerations for private image
  replication](#replication-considerations "#replication-considerations")
- [Private image replication examples for
  Amazon ECR](registry-settings-examples.md "registry-settings-examples.md")
- [Configuring private image replication in
  Amazon ECR](registry-settings-configure.md "registry-settings-configure.md")
- [Removing private image replication settings
  in Amazon ECR](registry-settings-remove.md "registry-settings-remove.md")

## Cross-account replication policy

requirements

For cross-account ECR replication to work properly, you must understand which account
needs which policies configured. This section clarifies the policy requirements for both
source and destination accounts.

### Policy configuration overview

Cross-account ECR replication requires policy configuration on the **destination account only**. The source account does not require
any special repository or registry policies.

- **Source Account**: Configure replication rules
  in the registry settings. No additional policies required on source
  repositories.
- **Destination Account**: Configure a registry
  permissions policy to allow the source account to replicate images.

### Destination registry policy

requirements

The destination account must configure a registry permissions policy that grants the
source account permission to perform the following actions:

- `ecr:ReplicateImage` - Allows the source account to replicate
  images to the destination registry
- `ecr:CreateRepository` - Allows ECR to automatically create
  repositories in the destination registry if they don't already exist

###### Important

If you do not grant the `ecr:CreateRepository` permission, you must
manually create repositories with the same names in the destination account before
replication can succeed.

Example destination registry policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowCrossAccountReplication",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": [
 "ecr:ReplicateImage",
 "ecr:CreateRepository"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Source account requirements

The source account only needs to:

- Configure replication rules in the registry settings to specify the
  destination account and regions
- Ensure the IAM principal configuring replication has the necessary ECR
  permissions

**No additional policies are required on source
repositories.** The source repositories do not need repository policies
that grant replication permissions.

### Common misconceptions

The following are common misconceptions about ECR cross-account replication
policies:

- **Misconception**: The source repository needs a
  policy allowing the destination account to replicate images.

**Reality**: Source repositories do not need any
special policies for replication.

- **Misconception**: Both source and destination
  accounts need registry policies.

**Reality**: Only the destination account needs a
registry permissions policy.

- **Misconception**: Repository policies and
  registry policies are the same thing.

**Reality**: Repository policies control access
to individual repositories, while registry policies control registry-level
operations like replication.

### Troubleshooting replication

failures

If cross-account replication is failing, check the following:

- Verify the destination account has a registry permissions policy
  configured
- Ensure the registry policy includes both `ecr:ReplicateImage` and
  `ecr:CreateRepository` actions
- Confirm the source account ID is correctly specified in the destination
  registry policy
- Check that the destination repositories exist (if
  `ecr:CreateRepository` is not granted)
- Review CloudTrail logs for failed `CreateRepository` or
  `ReplicateImage` API calls

## Considerations for private image

replication

The following should be considered when using private image replication.

- Only repository content pushed to a repository after replication is configured
  is replicated. Any preexisting content in a repository isn't replicated. Once
  replication is configured for a repository, Amazon ECR keeps the destination and
  source synchronized.
- The repository name will remain the same across Regions and accounts when
  replication has occurred. Amazon ECR doesn't support changing the repository name
  during replication.
- The first time you configure your private registry for replication, Amazon ECR
  creates a service-linked IAM role on your behalf. The service-linked IAM
  role grants the Amazon ECR replication service the permission it needs to create
  repositories and replicate images in your registry. For more information, see
  [Using service-linked roles for
  Amazon ECR](using-service-linked-roles.md "using-service-linked-roles.md").
- For cross-account replication to occur, the private registry destination must
  grant permission to allow the source registry to replicate its images. This is
  done by setting a private registry permissions policy. For more information, see
  [Private registry permissions in Amazon ECR](registry-permissions.md "registry-permissions.md").
- If the permission policy for a private registry are changed to remove a
  permission, any in-progress replications previously granted may complete.
- For cross-Region replication to occur, both the source and destination
  accounts must be opted-in to the Region prior to any replication actions
  occurring within or to that Region. For more information, see [Managing
  AWS Regions](../../../general/latest/gr/rande-manage.md "../../../general/latest/gr/rande-manage.md") in the _Amazon Web Services General Reference_.
- Cross-Region replication is not supported between AWS partitions. For
  example, a repository in `us-west-2` can't be replicated to
  `cn-north-1`. For more information about AWS partitions, see
  [ARN
  format](../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax "../../../general/latest/gr/aws-arns-and-namespaces.md#arns-syntax") in the _AWS General Reference_.
- The replication configuration for a private registry may contain up to 25
  unique destinations across all rules, with a maximum of 10 rules total. Each
  rule may contain up to 100 filters. This allows for specifying separate rules
  for repositories containing images used for production and testing, for
  example.
- The replication configuration supports filtering which repositories in a
  private registry are replicated by specifying a repository prefix. For an
  example, see [Example: Configuring
  cross-Region replication using a repository filter](registry-settings-examples.md#registry-settings-examples-crr-filter "registry-settings-examples.md#registry-settings-examples-crr-filter").
- A replication action only occurs once per image push. For example, if you
  configured cross-Region replication from `us-west-2` to
  `us-east-1` and from `us-east-1` to
  `us-east-2`, an image pushed to `us-west-2` replicates
  to only `us-east-1`, it doesn't replicate again to
  `us-east-2`. This behavior applies to both cross-Region and
  cross-account replication.
- The majority of images replicate in less than 30 minutes, but in rare cases
  the replication might take longer.
- Registry replication doesn't perform any delete actions. Replicated images and
  repositories can be manually deleted when they are no longer being used.
- Repository policies, including IAM policies, and lifecycle policies aren't
  replicated and don't have any effect other than on the repository they are
  defined for.
- Repository settings aren't replicated by default, you can replicate the
  repository settings using repository creation templates. These settings include
  tag mutability, encryption, repository permissions, and lifecycle policies. For
  more information about repository creation templates, see [Templates to control repositories created
  during a pull through cache or replication action](repository-creation-templates.md "repository-creation-templates.md").
- If tag immutability is enabled on a repository and an image is replicated that
  uses the same tag as an existing image, the image is replicated but won't
  contain the duplicated tag. This might result in the image being
  untagged.
