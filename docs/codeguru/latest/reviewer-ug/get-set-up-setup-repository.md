Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Create a repository for your source code

Before you use Amazon CodeGuru Reviewer to create code reviews, the source code that you want to analyze
must be set up in a supported repository type. CodeGuru Reviewer supports AWS CodeCommit, Bitbucket, GitHub,
and GitHub Enterprise Server. If you use Bitbucket or GitHub Enterprise Server, you must also
create a connection to your repository using CodeConnections. For more information, see [What are
connections?](../../../dtconsole/latest/userguide/welcome-connections.md "../../../dtconsole/latest/userguide/welcome-connections.md") in the _AWS Developer Tools User Guide_.

If you want to suppress recommendations from CodeGuru Reviewer, you can create and add to the root
directory of your repository an `aws-codeguru-reviewer.yml` file that lists files and
directories to exclude from analysis. For more information, see [Suppress
recommendations](recommendation-suppression.md "recommendation-suppression.md").

After you know the repository type and the name of your repository, you need to create a
repository association. For GitHub repositories, you can create a repository association using
only the CodeGuru Reviewer console. For the other supported repository types, you can use the console,
AWS CLI, or Amazon CodeGuru Reviewer SDK to create a repository association. For more information, see [Working with repository associations in
Amazon CodeGuru Reviewer](working-with-repositories.md "working-with-repositories.md").
