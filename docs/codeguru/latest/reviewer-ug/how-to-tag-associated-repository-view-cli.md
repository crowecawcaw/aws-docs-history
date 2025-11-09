As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# View tags for a CodeGuru Reviewer

associated repository (AWS CLI)

Follow these steps to use the AWS CLI to view the AWS tags for an associated
repository. If no tags have been added, the returned tags list in the response is
empty (`"Tags": {}`).

###### To view tags for an associated repository

1. Make sure that you have configured the AWS CLI with the AWS Region in
   which you want to create your code reviews. To verify the Region, run the
   following command at the command line or terminal and review the information
   for the default name.

```
aws configure
```

The default Region name must match the AWS Region for the repository in
CodeCommit. 2. Run the **describe-repository-association** command and
specify the Amazon Resource Name (ARN) of the associated repository.

```
aws codeguru-reviewer describe-repository-association /
  --association-arn arn:aws:codeguru-reviewer:`us-west-2`:`123456789012`:association:`repository-association-uuid`

```

3. If successful, this command outputs a [`RepositoryAssociation`](../reviewer-api/API_RepositoryAssociation.md "../reviewer-api/API_RepositoryAssociation.md") object that includes an
   array with its tags.

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
