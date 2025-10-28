# Repository policies

CodeArtifact uses resource-based permissions to control access. Resource-based
permissions let you specify who has access to a repository and what actions
they can perform on it. By default, only the repository owner has access to a
repository. You can apply a policy document that allows other IAM principals to
access your repository.

For more information, see [Resource-Based Policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based") and [Identity-Based Policies and Resource-Based Policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md").

## Create a resource policy to grant

read access

A resource policy is a text file in JSON format. The file must specify a principal
(actor), one or more actions, and an effect (`Allow` or `Deny`).
For example, the following resource policy grants the account `123456789012`
permission to download packages from the repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:ReadFromRepository"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Resource": "*"
 }
 ]
}`

```

Because the policy is evaluated only for operations against the repository that it's
attached to, you don't need to specify a resource. Because the resource is implied, you
can set the `Resource` to `*`. In order for a package manager to download
a package from this repository, a domain policy for cross-account access will also need to be
created. The domain policy must grant at least `codeartifact:GetAuthorizationToken`
permission to the principal. For an example of a full domain policy for granting cross-account
access, see this [Domain policy example](domain-policies.md#domain-policy-example "domain-policies.md#domain-policy-example").

###### Note

The `codeartifact:ReadFromRepository` action can only be used on a
repository resource. You cannot put a package's Amazon Resource Name (ARN) as a
resource with `codeartifact:ReadFromRepository` as the action to allow
read access to a subset of packages in a repository. A given principal can either
read all the packages in a repository or none of them.

Because the only action specified in the repository is `ReadFromRepository`,
users and roles from account `1234567890` can download packages from the
repository. However, they can't perform other actions on them (for example, listing
package names and versions). Typically, you grant permissions in the following policy in
addition to `ReadFromRepository` because a user who downloads packages from a
repository needs to interact with it in other ways too.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:DescribePackageVersion",
 "codeartifact:DescribeRepository",
 "codeartifact:GetPackageVersionReadme",
 "codeartifact:GetRepositoryEndpoint",
 "codeartifact:ListPackages",
 "codeartifact:ListPackageVersions",
 "codeartifact:ListPackageVersionAssets",
 "codeartifact:ListPackageVersionDependencies",
 "codeartifact:ReadFromRepository"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Resource": "*"
 }
 ]
}`

```

## Set a policy

After you create a policy document, use the
`put-repository-permissions-policy` command to attach it to a
repository:

```
aws codeartifact put-repository-permissions-policy --domain `my_domain` --domain-owner `111122223333` \
          --repository `my_repo` --policy-document `file:///PATH/TO/policy.json`
```

When you call `put-repository-permissions-policy`, the resource policy on the repository is ignored when evaluating permissions. This ensures
that the owner of a domain cannot lock themselves out of the repository, which would prevent them from being able to update the resource policy.

###### Note

You cannot grant permissions to another AWS account to update the resource policy on a repository using a resource policy, since the resource policy is ignored when calling put-repository-permissions-policy.

Sample output:

```
{
    "policy": {
        "resourceArn": "arn:aws:codeartifact:`region-id`:`111122223333`:repository/`my_domain`/`my_repo`",
        "document": "`{ ...policy document content...}`",
        "revision": "`MQlyyTQRASRU3HB58gBtSDHXG7Q3hvxxxxxxx=`"
    }
}
```

The output of the command contains the Amazon Resource Name (ARN) of the repository
resource, the full contents of the policy document, and a revision identifier. You can
pass the revision identifier to `put-repository-permissions-policy` using the
`--policy-revision` option. This ensures that a known revision of the
document is being overwritten, and not a newer version set by another writer.

## Read a policy

Use the `get-repository-permissions-policy` command to read an existing
version of a policy document. To format the output for readability, use the
`--output` and `--query policy.document` together with the
Python `json.tool` module.

```
aws codeartifact get-repository-permissions-policy --domain `my_domain` --domain-owner `111122223333` \
          --repository `my_repo` --output text --query policy.document | python -m json.tool
```

Sample output:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Action": [
 "codeartifact:DescribePackageVersion",
 "codeartifact:DescribeRepository",
 "codeartifact:GetPackageVersionReadme",
 "codeartifact:GetRepositoryEndpoint",
 "codeartifact:ListPackages",
 "codeartifact:ListPackageVersions",
 "codeartifact:ListPackageVersionAssets",
 "codeartifact:ListPackageVersionDependencies",
 "codeartifact:ReadFromRepository"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Delete a policy

Use the `delete-repository-permissions-policy` command to delete a policy
from a repository.

```
aws codeartifact delete-repository-permissions-policy --domain `my_domain` --domain-owner `111122223333` \
          --repository `my_repo`
```

The format of the output is the same as that of the `get-repository-permissions-policy` command.

## Grant read access to

principals

When you specify the root user of an account as the principal in a policy
document, you grant access to all of the users and roles in that account. To limit
access to selected users or roles, use their ARN in the `Principal`
section of the policy. For example, use the following to grant read access to the
IAM user `bob` in account `123456789012`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:ReadFromRepository"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`bob`"
 },
 "Resource": "*"
 }
 ]
}`

```

## Grant write access to

packages

The `codeartifact:PublishPackageVersion` action is used to control
permission to publish new versions of a package. The resource used with this action
must be a package. The format of CodeArtifact package ARNs is as follows.

```
arn:aws:codeartifact:`region-id`:`111122223333`:package/`my_domain`/`my_repo`/`package-format`/`package-namespace`/`package-name`
```

The following example shows the ARN for an npm package with scope
`@parity` and name `ui` in the `my_repo`
repository in domain `my_domain`.

```
arn:aws:codeartifact:`region-id`:`111122223333`:package/`my_domain`/`my_repo`/`npm`/`parity`/`ui`
```

The ARN for an npm package without a scope has the empty string for the namespace
field. For example, the following is the ARN for a package without a scope and with
name `react` in the `my_repo` repository in domain
`my_domain`.

```
arn:aws:codeartifact:`region-id`:`111122223333`:package/`my_domain`/`my_repo`/`npm`//`react`
```

The following policy grants account `123456789012` permission to publish
versions of `@parity/ui` in the `my_repo`
repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:PublishPackageVersion"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Resource": "arn:aws:codeartifact:`us-east-1`:`111122223333`:package/`my_domain`/`my_repo`/`npm`/`parity`/`ui`"
 }
 ]
}`

```

###### Important

To grant permission to publish Maven and NuGet package versions, add the following permissions in
addition to `codeartifact:PublishPackageVersion`.

1. NuGet: `codeartifact:ReadFromRepository` and specify the repository resource
2. Maven: `codeartifact:PutPackageMetadata`

Because this policy specifies a domain and repository as part of the resource, it
allows publishing only when attached to that repository.

## Grant write access to a

repository

You can use wildcards to grant write permission for all packages in a repository.
For example, use the following policy to grant an account permission to write to
all packages in the `my_repo` repository.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codeartifact:PublishPackageVersion"
 ],
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:root"
 },
 "Resource": "arn:aws:codeartifact:`us-east-1`:`111122223333`:package/`my_domain`/`my_repo`/*"
 }
 ]
}`

```

## Interaction between repository and domain policies

CodeArtifact supports resource policies on domains and repositories. Resource policies are optional. Each
domain may have one policy and each repository in the domain may have its own repository policy. If both a domain
policy and a repository policy are present, then both are evaluated when determining whether a request to a CodeArtifact
repository is allowed or denied. Domain and repository policies are evaluating using the following rules:

- No resource policies are evaluated when performing account-level operations such as
  [ListDomains](../APIReference/API_ListDomains.md "../APIReference/API_ListDomains.md")
  or [ListRepositories](../APIReference/API_ListRepositories.md "../APIReference/API_ListRepositories.md").
- No repository policies are evaluated when performing domain-level operations such as
  [DescribeDomain](../APIReference/API_DescribeDomain.md "../APIReference/API_DescribeDomain.md")
  or [ListRepositoriesInDomain](../APIReference/API_ListRepositoriesInDomain.md "../APIReference/API_ListRepositoriesInDomain.md").
- The domain policy is not evaluated when performing
  [PutDomainPermissionsPolicy](../APIReference/API_PutDomainPermissionsPolicy.md "../APIReference/API_PutDomainPermissionsPolicy.md").
  Note that this rule prevents lock-outs.
- The domain policy is evaluated when performing
  [PutRepositoryPermissionsPolicy](../APIReference/API_PutRepositoryPermissionsPolicy.md "../APIReference/API_PutRepositoryPermissionsPolicy.md"),
  but the repository policy is not evaluated.
- An explicit deny in any policy overrides an allow in another policy.
- An explicit allow is only required in one resource policy. Omitting an action from a repository policy will not result in an implicit deny if the
  domain policy allows the action.
- When no resource policy allows an action, the result is an implicit deny unless the calling principal’s account is the domain owner or repository administrator
  account and an identity-based policy allows the action.

Resource policies are optional when used to grant access in a single account scenario, where the caller account used to access a repository
is the same as the domain owner and repository administrator account. Resource policies are required to grant access in a cross-account scenario where
the caller’s account is not the same as the domain owner or repository administrator account. Cross-account access in CodeArtifact follows the general IAM
rules for cross-account access as described in
[Determining whether a
cross-account request is allowed](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md#policy-eval-cross-account "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md#policy-eval-cross-account") in the _IAM User Guide_.

- A principal in the domain owner account may be granted access to any repository in the domain through an identity-based policy. Note
  that in this case, no explicit allow is required in a domain or repository policy.
- A principal in the domain owner account may be granted access to any repository through a domain or repository policy. Note that
  in this case, no explicit allow is required in an identity-based policy.
- A principal in the repository administrator account may be granted access to the repository through an identity-based policy. Note that
  in this case, no explicit allow is required in a domain or repository policy.
- A principal in another account is only granted access when allowed by at least one resource policy and at least one identity-based
  policy, with no policy explicitly denying the action.
