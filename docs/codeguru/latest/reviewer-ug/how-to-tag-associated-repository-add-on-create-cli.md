Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# Add a tag

when you create a CodeGuru Reviewer associated repository (AWS CLI)

You can use the AWS CLI to add tags to an associated repository when you create
it.

###### Note

Because you cannot use the AWS CLI to create a GitHub repository, you cannot
use the AWS CLI to add tags to a GitHub repository when you create it. You can
use the AWS CLI to add tags to an existing GitHub repository using
**tag-resource**. You can also add tags when you create a
GitHub repository association with the console.

###### To add a tag when you create a repository association

1. Make sure that you have configured the AWS CLI with the AWS Region in
   which you want to create your code reviews. To verify the Region, run
   the following command at the command line or terminal and review the
   information for the default name.

```
aws configure
```

The default Region name must match the AWS Region for the repository
in CodeCommit. 2. Run the **associate-repository** command specifying the
tags you want to add with the `--tags` parameter. Specify a
tag's key and value using an equal symbol (for example,
`my-key=my-value`). For more information about how to use
**associate-repository** to create an association
with your repository type, see one of the following:

    * [Create a CodeCommit repository association
     (AWS CLI)](create-codecommit-association.md#create-codecommit-association-cli "create-codecommit-association.md#create-codecommit-association-cli")
    * [Create a Bitbucket repository
     association (AWS CLI)](create-bitbucket-association.md#create-bitbucket-association-cli "create-bitbucket-association.md#create-bitbucket-association-cli")
    * [Create a GitHub Enterprise Server repository
     association (AWS CLI)](create-github-enterprise-association.md#create-github-enterprise-association-cli "create-github-enterprise-association.md#create-github-enterprise-association-cli")

The following example adds 3 tags when you create an AWS CodeCommit
repository association.

```
aws codeguru-reviewer associate-repository --repository CodeCommit={Name=`my-codecommit-repo`} /
--tags value-1=key-1,owner=admin,status=beta
```

3. If successful, this command outputs a [`RepositoryAssociation`](../reviewer-api/API_RepositoryAssociation.md "../reviewer-api/API_RepositoryAssociation.md") object that includes
   an array with the 3 tags.

```
{
    "RepositoryAssociation": {
        "AssociationId": "repository-association-uuid",
        "Name": "`my-codecommit-repo`",
        "LastUpdatedTimeStamp": 1595634764.029,
        "ProviderType": "CodeCommit",
        "CreatedTimeStamp": 1595634764.029,
        "Owner": "123456789012",
        "State": "Associating",
        "StateReason": "Pending Repository Association",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:repository-association-uuid",
    },
    "Tags": {
        "owner": "admin",
        "status": "beta",
        "value-1": "key-1",
    }
}
```
