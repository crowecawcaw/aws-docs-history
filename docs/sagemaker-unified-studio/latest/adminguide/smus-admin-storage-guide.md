# Source control and file storage in Amazon SageMaker Unified Studio

Every project in Amazon SageMaker Unified Studio includes S3 shared storage by default. S3 shared storage
is active from the moment a project is created and requires no administrator configuration.
All project members can immediately read, write, and share files.

Repositories are an optional, additive capability. When you configure a Git connection at
the domain level, project members can add repositories to their projects for version control,
branching, and commit-based collaboration. Adding repositories does not replace or disable S3
shared storage. Both options coexist in the same project.

As an administrator, your responsibilities include:

- Understanding the default S3 shared storage behavior (see
  [Default S3 storage](configuring-s3-storage.md "configuring-s3-storage.md"))
- Setting up Git connections if your teams need repository-based version control (see
  [Git connections](git-connections.md "git-connections.md"))
- Configuring cross-account permissions if your domain and tooling environments are in
  different accounts (see [Cross-account and cross-region Git configurations](cross-account-git.md "cross-account-git.md"))

###### Important

On July 30, 2026, Amazon SageMaker Unified Studio launched a new repository experience that provides
per-artifact version control, multi-repository support, and branch-based collaboration.
For documentation, see [Git connections](git-connections.md "git-connections.md"). If your
domain uses the previous force-push based storage model (where every save pushes directly
to the remote), see [Legacy experience and migration](legacy-git.md "legacy-git.md") for documentation on that experience.
For migration details, see [Migrating to the new repository experience](legacy-git.md#admin-migration "legacy-git.md#admin-migration").

## Storage options

Amazon SageMaker Unified Studio supports the following storage options for project files.

### S3 shared storage

S3 shared storage is the default option. It uses Amazon Simple Storage Service to provide a shared
storage area for project files. All project members have read, write, update, and
delete access to the shared storage area. This storage operates on a last-write-wins
principle, meaning that files are immediately visible to all project members when
modified. Team members must coordinate when working on the same files to avoid
overwriting each other's changes.

### Repositories

Repositories provide version control through Code Connections to GitHub,
GitHub Enterprise Server, GitLab, GitLab Self-Managed, and Bitbucket. Repositories
are additive. Administrators make them available by configuring Git connections
at the domain level.
