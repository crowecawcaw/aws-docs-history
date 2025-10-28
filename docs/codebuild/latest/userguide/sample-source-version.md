# Source version sample with AWS CodeBuild

This sample demonstrates how to specify a version of your source using a format other
than a commit ID (also known as a commit SHA). You can specify the version of your source in
the following ways:

- For an Amazon S3 source provider, use the version ID of the object that represents the
  build input ZIP file.
- For CodeCommit, Bitbucket, GitHub, and GitHub Enterprise Server, use one of the
  following:
  - Pull request as a pull request reference (for example,
    `refs/pull/1/head`).
  - Branch as a branch name.
  - Commit ID.
  - Tag.
  - Reference and a commit ID. The reference can be one of the
    following:
    - A tag (for example,
      `refs/tags/mytagv1.0^{full-commit-SHA}`).
    - A branch (for example,
      `refs/heads/mydevbranch^{full-commit-SHA}`).
    - A pull request (for example,
      `refs/pull/1/head^{full-commit-SHA}`).

- For GitLab and GitLab Self Managed, use one of the following:
  - Branch as a branch name.
  - Commit ID.
  - Tag.

###### Note

You can specify the version of a pull request source only if your repository is
GitHub or GitHub Enterprise Server.

If you use a reference and a commit ID to specify a version, the
`DOWNLOAD_SOURCE` phase of your build is faster than if you provide the
version only. This is because when you add a reference, CodeBuild does not need to download the
entire repository to find the commit.

- You can specify a source version with only a commit ID, such as
  `12345678901234567890123467890123456789`. If you do this, CodeBuild must
  download the entire repository to find the version.
- You can specify a source version with a reference and a commit ID in this format:
  ``refs`/`heads`/`branchname`^{`full-commit-SHA`}`(for example,`refs/heads/main^{12345678901234567890123467890123456789}`). If you do
  this, CodeBuild downloads only the specified branch to find the version. .

###### Note

To speed up the `DOWNLOAD_SOURCE` phase of your build, you can also to set
**Git clone depth** to a low number. CodeBuild downloads fewer versions
of your repository.

###### Topics

- [Specify a GitHub
  repository version with a commit ID](sample-source-version-github.md "sample-source-version-github.md")
- [Specify a GitHub
  repository version with a reference and commit ID](sample-source-version-github-ref.md "sample-source-version-github-ref.md")
