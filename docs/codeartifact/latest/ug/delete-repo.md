# Delete a repository

You can delete a repository using the CodeArtifact console or the AWS CLI. After a repository has
been deleted, you can no longer push packages to it or pull packages from it. All packages
in the repository become permanently unavailable and cannot be restored. You can create a
repository with the same name, but its contents will be empty.

###### Important

Deleting a repository cannot be undone. After you delete a repository, you are no
longer able to recover it and it cannot be restored.

###### Topics

- [Delete a repository (console)](#delete-repo-console "#delete-repo-console")
- [Delete a repository (AWS CLI)](#delete-repo-cli "#delete-repo-cli")
- [Protect repositories from being deleted](#delete-repo-protect "#delete-repo-protect")

## Delete a repository (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. On the navigation pane, choose **Repositories**, then choose the repository that you want to delete.
3. Choose **Delete** and then follow the steps to delete the domain.

## Delete a repository (AWS CLI)

Use the `delete-repository` command to delete a repository.

```
aws codeartifact delete-repository --domain `my_domain` --domain-owner `111122223333` --repository `my_repo`
```

Example output:

```
{
    "repository": {
        "name": "`my_repo`",
        "administratorAccount": "`123456789012`",
        "domainName": "`my_domain`",
        "domainOwner": "`123456789012`",
        "arn": "arn:aws:codeartifact:`region-id`:`123456789012`:repository/`my_domain`/`my_repo`",
        "description": "`My new repository`",
        "upstreams": [],
        "externalConnections": []
    }
}
```

## Protect repositories from being deleted

You can prevent a repository from being accidentally deleted by including a domain policy similar to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRepositoryDeletion",
 "Action": [
 "codeartifact:DeleteRepository"
 ],
 "Effect": "Deny",
 "Resource": "*",
 "Principal": "*"
 }
 ]
}`

```

This policy prevents all principals from deleting the repository, but if you decide later that you need to delete the repository,
you can do so by following these steps:

1. In the domain policy, update the policy to the following:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRepositoryDeletion",
 "Action": [
 "codeartifact:DeleteRepository"
 ],
 "Effect": "Deny",
 "NotResource": "`arn:aws:iam::*:role/Service*`",
 "Principal": "*"
 }
 ]
}`

```

Replace `repository-arn` with the ARN of the repository that you would like to delete. 2. In the AWS CodeArtifact console, choose **Repositories** and delete your chosen repository. 3. After you've deleted the repository, you can change the policy back to prevent acccidental delections.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyRepositoryDeletion",
 "Action": [
 "codeartifact:DeleteRepository"
 ],
 "Effect": "Deny",
 "Resource": "*",
 "Principal": "*"
 }
 ]
}`

```

Alternatively, you can include the same deny statement in a repository policy. This allow you to have more flexibility
to protect high-value repositories from deletion.
