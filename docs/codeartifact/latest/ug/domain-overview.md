# Domain overview

When you're working with CodeArtifact, domains are useful for the following:

- **Deduplicated storage**: An asset only needs to be stored
  once in a domain, even if it's available in 1 or 1,000 repositories. That means you only
  pay for storage once.
- **Fast copying**: When you pull packages from an upstream CodeArtifact
  repository into a downstream or use
  the [CopyPackageVersions API](copy-package.md "copy-package.md"), only metadata
  records must be updated. No assets are copied. This makes it fast to set up a new
  repository for staging or testing. For more information, see
  [Working with upstream repositories in CodeArtifact](repos-upstream.md "repos-upstream.md").
- **Easy sharing across repositories and teams**: All of
  the assets and metadata in a domain are encrypted with a single AWS KMS key (KMS key).
  You don't need to manage a key for each repository or grant
  multiple accounts access to a single key.
- **Apply policy across multiple repositories**: The domain
  administrator can apply policy across the domain. This includes restricting which
  accounts have access to repositories in the domain, and who can configure connections to
  public repositories to use as sources of packages. For more information, see [Domain policies](domain-policies.md "domain-policies.md").
- **Unique repository names**: The domain provides a
  namespace for repositories. Repository names only need to be unique within the domain.
  You should use meaningful names that are easy to understand.
  Domain names must be unique within an account.

You cannot create a repository without a domain. When you use the [CreateRepository](create-repo.md "create-repo.md") API to create a repository, you must
specify a domain name. You cannot move a repository from one domain to another.

A repository can be owned by the same AWS account that owns the domain, or a different
account. If the owning accounts are different, the repository-owning account must be
granted the `CreateRepository` permission on the domain resource. You can do
this by adding a resource policy to the domain using the [PutDomainPermissionsPolicy](domain-policies.md#set-domain-policy "domain-policies.md#set-domain-policy") command.

Although an organization can have multiple domains, the recommendation is to have a single
production domain that contains all published artifacts so that development teams can find and
share packages across their organization. A second pre-production domain can be useful for
testing changes to the production domain configuration.

## Cross-account domains

Domain names only need to be unique within an account, which means there could be multiple domains within a region that have the same name.
Because of this, if you want to access a domain that is owned by an account you are not authenticated to, you must provide the domain owner ID
along with the domain name in both the CLI and the console. See the following CLI examples.

**Access a domain owned by an account you are authenticated to:**

When accessing a domain within the account you're authenticated to, you only need to specify the domain name. The following example
lists packages in the `my_repo` repository in the `my_domain` domain that is owned by your account.

```
aws codeartifact list-packages --domain `my_domain` --repository `my_repo`
```

**Access a domain owned by an account that you are not authenticated to:**

When accessing a domain that is owned by an account that you're not authenticated to, you need to specify the domain owner as well as the domain name. The
following example lists packages in the `other-repo` repository in the `other-domain` domain that is owned
by an account that you are not authenticated to. Notice the addition of the `--domain-owner` parameter.

```
aws codeartifact list-packages --domain `other-domain` --domain-owner `111122223333` --repository `other-repo`
```

## Types of AWS KMS keys supported in CodeArtifact

CodeArtifact supports only [symmetric
KMS keys](../../../kms/latest/developerguide/concepts.md#symmetric-cmks "../../../kms/latest/developerguide/concepts.md#symmetric-cmks"). You can't use an [asymmetric KMS key](../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks "../../../kms/latest/developerguide/symmetric-asymmetric.md#asymmetric-cmks") to encrypt your CodeArtifact domains. For more
information, see [Identifying
symmetric and asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md"). To learn how to create a
new customer managed key, see [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

CodeArtifact supports AWS KMS External Key Stores (XKS). You are
responsible for the availability, durability, and latency of key operations with
XKS keys, which can affect availability, durability, and latency with CodeArtifact.
Some examples of effects of using XKS keys with CodeArtifact:

- Because every asset of a requested package and all of its
  dependencies is subject to decryption latency, build
  latency can be increased substantially with an increase in XKS operation latency.
- Because all assets are encrypted in CodeArtifact, a loss of XKS key materials
  will result in a loss of all assets associated with the domain using the XKS key.

For more information about XKS keys, see
[External key stores](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md")
in the _AWS Key Management Service Developer Guide_.
