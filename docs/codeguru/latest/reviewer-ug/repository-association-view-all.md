Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# View all repository associations in

CodeGuru Reviewer

You can view all the associated repositories in your AWS Region and your AWS account
using the console or the AWS CLI.

###### Topics

- [View all associated
  repositories in CodeGuru Reviewer (console)](#repository-association-view-all-console "#repository-association-view-all-console")
- [View all repository associations
  in CodeGuru Reviewer (AWS CLI)](#repository-association-view-all-cli "#repository-association-view-all-cli")

## View all associated

repositories in CodeGuru Reviewer (console)

###### View all associated repositories

1. Open the Amazon CodeGuru Reviewer console at
   [https://console.aws.amazon.com/codeguru/reviewer/](https://console.aws.amazon.com/codeguru/reviewer/ "https://console.aws.amazon.com/codeguru/reviewer/").
2. In the navigation pane, choose **Associated repositories**.

## View all repository associations

in CodeGuru Reviewer (AWS CLI)

For information about using the AWS CLI with CodeGuru Reviewer, see the [CodeGuru Reviewer section](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html") and [list-repository-associations](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-repository-associations.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/list-repository-associations.html") in the _AWS CLI Command Reference_.

###### View all repository associations

1. Make sure that you have configured the AWS CLI with the AWS Region that
   contains the repository associations you want to view. Run the following command
   at the command line or terminal and review or configure the Region for the
   AWS CLI.

```
aws configure
```

2. Run **list-repository-associations**.

```
aws codeguru-reviewer list-repository-associations
```

3. If successful, this command outputs one [`RepositoryAssociationSummary`](../reviewer-api/API_RepositoryAssociationSummary.md "../reviewer-api/API_RepositoryAssociationSummary.md") object for each of
   your associated repositories.

```
{
    "RepositoryAssociationSummaries": [
        {
            "LastUpdatedTimeStamp": 1595886609.616,
            "Name": "test",
            "AssociationId": "0bdac454-f6af-4adf-a625-de4db4b4bca1",
            "Owner": "123456789012",
            "State": "Associated",
            "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:0bdac454-f6af-4adf-a625-de4db4b4bca1",
            "ProviderType": "Bitbucket"
        },
        {
            "LastUpdatedTimeStamp": 1595636969.035,
            "Name": "CodeDeploy-CodePipeline-ECS-Tutorial",
            "AssociationId": "eb2f7513-a132-47ad-81dc-bd718468ee1e",
            "Owner": "123456789012",
            "State": "Associated",
            "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:eb2f7513-a132-47ad-81dc-bd718468ee1e",
            "ProviderType": "CodeCommit"
        },
        {
            "LastUpdatedTimeStamp": 1595634785.983,
            "Name": "My-ecs-beta-repo",
            "AssociationId": "d79156d7-6297-4b08-ba5a-f05b274e3518",
            "Owner": "123456789012",
            "State": "Associated",
            "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:d79156d7-6297-4b08-ba5a-f05b274e3518",
            "ProviderType": "CodeCommit"
        }
    ]
}

```
