# Alternatives for version control of source code in

AFT

AFT uses AWS CodeCommit for a source code version control system (VCS), and it allows other
[CodeConnections](../../../dtconsole/latest/userguide/supported-versions-connections.md "../../../dtconsole/latest/userguide/supported-versions-connections.md") that
meet your business requirements or existing architecture.

If you're deploying AFT for the first time and you don't have an existing CodeCommit
repository, you must specify an external VCS provider, as part of the AFT deployment
prerequisites.

###### AFT supports the following source code control alternatives:

- GitHub
- GitHub Enterprise Server
- BitBucket
- GitLab
- GitLab Self-managed

###### Note

If you specify AWS CodeCommit as your VCS, no additional steps are required. AFT creates
the necessary `git` repositories in your environment, with default names.
However, you can override the default repository names for CodeCommit, as needed, to comply
with your organizational standards.

## Set up an alternative source code version

control system (custom VCS) with AFT

To set up an alternative source code version control system for your AFT deployment,
follow these steps.

**Step 1: Create `git` repositories in a supported
third-party version control system (VCS).**

If you are not using AWS CodeCommit, you must create `git` repositories in your
AFT-supported, third-party VCS provider environment for the following items.

- **AFT account requests.**
  [Sample code available](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-request "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-request")
  . For more information
  about AFT account requests, see [Provision a new account with AFT](aft-provision-account.md "aft-provision-account.md").
- **AFT account provisioning customizations.**
  [Sample code available](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-provisioning-customizations "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-provisioning-customizations")
  . For more information
  on AFT account provisioning customizations, see [Create your AFT account provisioning
  customizations state machine](aft-provisioning-framework.md#aft-create-customizations "aft-provisioning-framework.md#aft-create-customizations").
- **AFT global customizations.**
  [Sample code available](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-global-customizations "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-global-customizations")
  . For more information
  on AFT global customizations, see [Account customizations](aft-account-customization-options.md "aft-account-customization-options.md").
- **AFT account customizations.**
  [Sample code available](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-customizations "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/tree/main/sources/aft-customizations-repos/aft-account-customizations")
  . For more information
  on AFT account customizations, see [Account customizations](aft-account-customization-options.md "aft-account-customization-options.md").

**Step 2: Specify the VCS configuration parameters required for
AFT deployment**

The following input parameters are needed to configure your VCS provider as part of
the AFT deployment.

- **vcs_provider**: If you are not using AWS CodeCommit, specify the
  VCS provider as `"bitbucket"`, `"github"`,
  `"githubenterprise"`, or `"gitlab"`, based on your use
  case.
- **github_enterprise_url**: For GitHub Enterprise customers
  only, specify the GitHub URL.
- **account_request_repo_name**: For AWS CodeCommit users, this
  value is set to `aft-account-request`. In an AFT-supported,
  third-party VCS provider environment, update this input value with your actual
  repository name. For BitBucket, Github, GitHub Enterprise, GitLab, and GitLab
  Self-managed, the repository name must have the format
  `[Org]/[Repo]`.
- **account_customizations_repo_name**: For AWS CodeCommit users,
  this value is set to `aft-account-customizations`. In an
  AFT-supported, third-party VCS provider environment, update this input value
  with your repository name. For BitBucket, Github, GitHub Enterprise, GitLab, and
  GitLab Self-managed, the repository name must have the format
  `[Org]/[Repo]`.
- **account_provisioning_customizations_repo_name**: For
  AWS CodeCommit users, this value is set to
  `aft-account-provisioning-customizations`. In an AFT-supported,
  third-party VCS provider environment, update this input value with your
  repository name. For BitBucket, Github, GitHub Enterprise, GitLab, and GitLab
  Self-managed, the repository name must have the format
  `[Org]/[Repo]`.
- **global_customizations_repo_name**: For AWS CodeCommit users,
  this value is set to `aft-global-customizations`. In an
  AFT-supported, third-party VCS provider environment, update this input value
  with your repository name. For BitBucket, Github, GitHub Enterprise, GitLab, and
  GitLab Self-managed, the repository name must have the format
  `[Org]/[Repo]`.
- **account_request_repo_branch**: The branch is
  `main` by default, but the value can be overridden.

By default, AFT sources from the `main` branch of each `git`
repository. You can override the branch name value with an additional input parameter.
For more information about input parameters, refer to the README file in the [AFT Terraform module](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/README.md#inputs "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/README.md#inputs").

###### For existing AWS CodeCommit customers

If you create a CodeCommit repository with a new name for AFT, you can update the
repository name by updating the values for these input parameters.

**Step 3: Complete the AWS CodeCommit connection for third-party VCS
providers**

When your deployment runs, AFT either creates the required AWS CodeCommit repositories, or
it creates an AWS CodeCommit connection for your chosen third-party VCS provider. In case of
the latter, you must manually sign in to the AFT management account’s console to
complete the pending CodeCommit connection. See [the AWS CodeCommit
documentation](../../../dtconsole/latest/userguide/connections-update.md "../../../dtconsole/latest/userguide/connections-update.md") for further instructions on completing the CodeCommit connection.
