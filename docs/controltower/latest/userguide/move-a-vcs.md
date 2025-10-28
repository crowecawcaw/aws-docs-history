# Move AFT from AWS CodeCommit to another VCS provider

This section provides an overview of how you can move AWS Control Tower Account Factory for
Terraform (AFT) from AWS CodeCommit as your version control system (VCS) to another VCS
provider.

**Step 1.** Set up new repositories in the VCS of your choice.

**Step 2.** Add these repositories as new remotes in `git`.

**Step 3.** Execute `git push` to the new VCS provider.

###### Note

The repository structure that you create should be the same as in AWS CodeCommit.
Changing the structure impedes the ability of AFT to execute the desired code.

###### Repository structure:

- aft-account-request
- aft-account-customizations
- aft-global-customizations
- aft-account-provisioning-customizations
  **Step 4.** In your AWS Control Tower management account, update the Terraform module (bootstrap) to point
  to your VCS provider, as shown in the following example:

**Example:**
[GitLab with Terraform OSS](https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/examples/gitlab%2Btf_oss/main.tf "https://github.com/aws-ia/terraform-aws-control_tower_account_factory/blob/main/examples/gitlab%2Btf_oss/main.tf")

– Perform `terraform plan` to preview changes, then `terraform
 apply`.

**Step 5.** Complete the steps to finish setting up the CodeConnection (formerly known as
CodeStar):

1. Sign in to your AFT management account
2. Locate and complete the pending AWS CodeConnections for the new VCS provider, as described in [Update a pending connection](../../../dtconsole/latest/userguide/connections-update.md "../../../dtconsole/latest/userguide/connections-update.md"), or in the AWS console, [`https://us-east-1.console.aws.amazon.com/codesuite/settings/connections`].
3. Reference: [Post-deployment steps](aft-post-deployment.md "aft-post-deployment.md")

###### Note

Account pipelines retain the previous source until
`aft-invoke-customizations`
_Step Functions_ is invoked. This invocation can be done as part of
the upgrade or as part of the next customizations invocations.

For more information, see this blog: [How to migrate your AWS CodeCommit repository to another Git provider](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider "https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider").
