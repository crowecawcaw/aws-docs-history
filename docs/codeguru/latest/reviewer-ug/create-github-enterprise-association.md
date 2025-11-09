As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Create a GitHub Enterprise Server repository

association in Amazon CodeGuru Reviewer

You can create a GitHub Enterprise Server repository association using the Amazon CodeGuru Reviewer console, the AWS CLI,
or the CodeGuru Reviewer SDK. Before you create a GitHub Enterprise Server repository association, you must have a
GitHub Enterprise Server repository.

###### Note

GitHub Enterprise Cloud repositories have a different procedure and different
prerequisites. If you're using GitHub Enterprise Cloud, [follow this procedure
instead](create-github-association.md "create-github-association.md").

###### Topics

- [GitHub Enterprise Server repository
  association prerequisites](#create-github-enterprise-association-requirements "#create-github-enterprise-association-requirements")
- [Create a GitHub Enterprise Server
  repository association (console)](#create-github-enterprise-association-console "#create-github-enterprise-association-console")
- [Create a GitHub Enterprise Server repository
  association (AWS CLI)](#create-github-enterprise-association-cli "#create-github-enterprise-association-cli")
- [Create a GitHub Enterprise Server
  repository association (AWS SDKs)](#create-github-enterprise-server-association-sdk "#create-github-enterprise-server-association-sdk")

## GitHub Enterprise Server repository

association prerequisites

To create a GitHub Enterprise Server repository association, you must have a GitHub Enterprise Server connection in
AWS CodeConnections. The connection must be in the same AWS account and Region in which you want your
code reviews. For more information, see [Create a connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md") and
[Create a connection
to GitHub Enterprise Server](../../../dtconsole/latest/userguide/connections-create-gheserver.md "../../../dtconsole/latest/userguide/connections-create-gheserver.md") in the _Developer Tools User Guide_.

###### Important

CodeConnections does not support GitHub Enterprise Server version 2.22.0 due to a known issue in the release.
To create a connection, use version 2.22.1 or later.

Your GitHub Enterprise Server connection requires a _host_. The host represents
your GitHub Enterprise Server instance and is to what your GitHub Enterprise Server connection connects. A host can be
an on-premises server or a Virtual Private Cloud (VPC). For more information, see [Amazon VPC configuration for your host](../../../dtconsole/latest/userguide/connections-create-gheserver-console.md#connections-create-gheserver-prereq "../../../dtconsole/latest/userguide/connections-create-gheserver-console.md#connections-create-gheserver-prereq") and [Create a host](../../../dtconsole/latest/userguide/connections-host-create.md "../../../dtconsole/latest/userguide/connections-host-create.md") in
the _AWS Developer Tools User Guide_.

## Create a GitHub Enterprise Server

repository association (console)

###### To create a GitHub Enterprise Server repository association

1.  Open the Amazon CodeGuru Reviewer console at
    [https://console.aws.amazon.com/codeguru/reviewer/](https://console.aws.amazon.com/codeguru/reviewer/ "https://console.aws.amazon.com/codeguru/reviewer/").
2.  In the navigation pane, choose **Repositories**.
3.  Choose **Associate repository and run analysis**.
4.  Choose **GitHub Enterprise Server**.
5.  From **Connect to GitHub Enterprise Server (with AWS CodeConnections)**, choose the
    connection you want to use. If you don't have a connection, choose **Create a
    GitHub Enterprise Server connection** to create one in the Developer Tools console. For more
    information, see [Create a
    connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md") in the _AWS Developer Tools User Guide_.
6.  From **Repository location**, choose the name of your GitHub Enterprise Server
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

    ![The Run a repository analysis section with settings and sample YAML file information.](/images/codeguru/latest/reviewer-ug/images/run-repo-analysis-config-file.png)

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

## Create a GitHub Enterprise Server repository

association (AWS CLI)

For information about using the AWS CLI with CodeGuru Reviewer, see the [CodeGuru Reviewer section of the AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html")

###### To create a GitHub Enterprise Server repository association

1. Make sure that you have configured the AWS CLI with the AWS Region in which you
   want to create your code reviews. To verify the Region, run the following command at
   the command line or terminal and review the information for the default name.

```
aws configure
```

2. Run the **associate-repository** command specifying the owner (or
   user name) of your GitHub Enterprise Server account, the name of your repository, and the Amazon
   Resource Name (ARN) of your connection.

```
aws codeguru-reviewer associate-repository --repository GitHubEnterpriseServer="{Owner=`github-enterprise-server-user-name`, Name=`repository-name`, \
 ConnectionArn=arn:aws:codeconnections:us-west-2:123456789012:connection/connection-uuid }"
```

3. If successful, this command outputs a [`RepositoryAssociation`](../reviewer-api/API_RepositoryAssociation.md "../reviewer-api/API_RepositoryAssociation.md") object.

```
{
    "RepositoryAssociation": {
        "ProviderType": "GitHubEnterpriseServer",
        "Name": "`repository-name`",
        "LastUpdatedTimeStamp": 1595966211.79,
        "AssociationId": "repository-association-uuid",
        "CreatedTimeStamp": 1595966211.79,
        "ConnectionArn": "arn:aws:codeconnections:us-west-2:123456789012:connection/connection-uuid",
        "State": "Associating",
        "StateReason": "Pending Repository Association",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-east-2:123456789012:association:repository-association-uuid",
        "Owner": "`github-enterprise-server-user-name`"
    }
}
```

4. When the **associate-repository** command succeeds, the status in
   the returned output is **Associating**. When the association is
   complete, the status changes to **Associated** and you can create a
   pull request or a full repository analysis to get recommendations. You can check your
   repository association's status using the `describe-repository` command
   with its Amazon Resource Name (ARN).

```
aws codeguru-reviewer describe-repository-association --association-arn arn:aws:codeguru-reviewer:us-west-2:123456789012:association:repository-association-uuid

```

5. If successful, this command outputs a [`RepositoryAssociation`](../reviewer-api/API_RepositoryAssociation.md "../reviewer-api/API_RepositoryAssociation.md") object which shows its status.

```
{
    "RepositoryAssociation": {
        "ProviderType": "GitHubEnterpriseServer",
        "Name": "`repository-name`",
        "LastUpdatedTimeStamp": 1595634764.029,
        "AssociationId": "repository-association-uuid",
        "CreatedTimeStamp": 1595634764.029,
        "ConnectionArn": "arn:aws:codeconnections:us-west-2:123456789012:connection/connection_uuid"
        "State": "Associated",
        "StateReason": "Pull Request Notification configuration successful",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:repository-association-uuid",
        "Owner": "`github-enterprise-server-user-name`"
    }
}
```

## Create a GitHub Enterprise Server

repository association (AWS SDKs)

To create a GitHub Enterprise Server repository association with the AWS SDKs, use the
`AssociateRepository` API. For more information, see [AssociateRepository](../reviewer-api/API_AssociateRepository.md "../reviewer-api/API_AssociateRepository.md") in the _Amazon CodeGuru Reviewer API Reference_.
