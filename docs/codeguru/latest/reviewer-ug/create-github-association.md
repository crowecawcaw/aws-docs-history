As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Create a GitHub or GitHub Enterprise Cloud

repository association in Amazon CodeGuru Reviewer

You can create a GitHub or GitHub Enterprise Cloud repository association using the
Amazon CodeGuru Reviewer console. You cannot create a GitHub or GitHub Enterprise Cloud repository
association using the AWS CLI or the CodeGuru Reviewer SDK. Before you create a GitHub or GitHub
Enterprise Cloud repository association, you must have a GitHub or GitHub Enterprise Cloud
repository.

###### Note

We recommend creating a new GitHub user (for example,
_MyCodeGuruUser_) and using that user to provide CodeGuru Reviewer with
access to your GitHub repositories. This ensures that CodeGuru Reviewer posts comments on behalf of
a unique user. This helps avoid confusion and make the account more transferable, so
that it doesn't belong to a single person who might not always be available to maintain
it.

###### To create a GitHub repository association

1.  Open the Amazon CodeGuru Reviewer console at
    [https://console.aws.amazon.com/codeguru/reviewer/](https://console.aws.amazon.com/codeguru/reviewer/ "https://console.aws.amazon.com/codeguru/reviewer/").
2.  In the navigation pane, choose **Repositories**.
3.  Choose **Associate repository and run analysis**.
4.  Choose **GitHub or GitHub Enterprise Cloud**.
5.  If you are not connected to GitHub, choose **Connect to GitHub or GitHub
    Enterprise Cloud** and follow the prompts to connect.
6.  From **Repository location**, choose the name of your GitHub
    repository that contains the source code you want CodeGuru Reviewer to analyze.
7.  (Optional) Expand **Encryption key - optional** to use
    your own AWS Key Management Service key (KMS key) to encrypt your associated repository. For more information,
    see [Encrypting a repository association in
    Amazon CodeGuru Reviewer](encrypt-repository-association.md "encrypt-repository-association.md").
    1. Select **Customize encryption settings (advanced)**.
    2. Do one of the following:
       - If you already have a KMS key that you manage, enter its Amazon Resource Name (ARN). For information
         about finding the ARN of your key using the console, see
         [Finding the
         key ID and key ARN](../../../kms/latest/developerguide/find-cmk-id-arn.md "../../../kms/latest/developerguide/find-cmk-id-arn.md") in the _AWS Key Management Service Developer Guide_.
       - If you want to create a KMS key, choose **Create an AWS KMS key** and follow
         the steps in the AWS KMS console. For more information, see
         [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
         _AWS Key Management Service Developer Guide_.

8.  In **Run a repository analysis**, specify information for your associated repository's
    first full scan. This scan generates your repository's initial code review. For more information, see
    [Get recommendations using full repository
    analysis](create-code-reviews.md#get-repository-scan "create-code-reviews.md#get-repository-scan").

        1. From **Source branch**, choose the branch to use.
        2. (Optional) In **Code review name**, type a name for your code review.
        3. (Optional) Expand **Analysis configuration file - optional** to download a sample `aws-codeguru-reviewer.yml` file to use as a template. Modify the file and upload it to the root directory of your repository. For more information about the analysis configuration file, see [Suppress
         recommendations](recommendation-suppression.md "recommendation-suppression.md").

    ![The Run a repository analysis section with settings and sample YAML file information.](images/run-repo-analysis-config-file.png)

9.  (Optional) Expand **Tags** to add one or more tags to your repository association.
    For more information, see [Tagging a repository association in
    Amazon CodeGuru Reviewer](tag-repository-association.md "tag-repository-association.md").
    1. Choose **Add new tag**.
    2. In **Key**, enter a name for the tag. You can add an optional
       value for the tag in **Value**.
    3. (Optional) To add another tag, choose **Add new tag**.

10. Choose **Associate repository and run analysis**. On the
    **Repositories** page, the **Status** is
    **Associating**. When the association is complete, the status
    changes to **Associated** and a full repository analysis begins.
    Refresh the page to check for the status change.
