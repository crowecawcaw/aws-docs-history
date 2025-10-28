Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Step 2: Associate a repository

You must create a repository association to grant CodeGuru Reviewer access to read your source code
and create notifications on your repository. The notifications initiate an analysis on the
updated source code every time you create a pull request. When you create your repository
association, CodeGuru Reviewer automatically creates a full repository analysis code review. You must
initiate future full repository analysis code reviews. For more information, see [Working with repository associations in
Amazon CodeGuru Reviewer](working-with-repositories.md "working-with-repositories.md").

###### Note

The source code reviewed by CodeGuru Reviewer is not stored. For more information, see [Captured data in CodeGuru Reviewer](data-protection.md#data-captured "data-protection.md#data-captured").

To create a repository association, choose one of the following.

- If your repository type is AWS CodeCommit, see [Create a CodeCommit repository
  association](create-codecommit-association.md "create-codecommit-association.md").
- If your repository type is Bitbucket, see [Create a Bitbucket repository
  association](create-bitbucket-association.md "create-bitbucket-association.md").
- If your repository type is GitHub or GitHub Enterprise Cloud, see [Create a GitHub or GitHub
  Enterprise Cloud repository association](create-github-association.md "create-github-association.md").
- If your repository type is GitHub Enterprise Server, see [Create a GitHub Enterprise Server
  repository association](create-github-enterprise-association.md "create-github-enterprise-association.md").
