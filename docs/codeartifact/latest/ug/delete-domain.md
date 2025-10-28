# Delete a domain

You can delete a domain using the CodeArtifact console or the AWS Command Line Interface (AWS CLI).

###### Topics

- [Restrictions on domain deletion](#delete-domain-restrictions "#delete-domain-restrictions")
- [Delete a domain (console)](#delete-domain-console "#delete-domain-console")
- [Delete a domain (AWS CLI)](#delete-domain-cli "#delete-domain-cli")

## Restrictions on domain deletion

Normally, you can't delete a domain that contains repositories. Before you delete the
domain, you must first delete its repositories. For more information, see [Delete a repository](delete-repo.md "delete-repo.md").

However, if CodeArtifact no longer has access to the domain's KMS key, you can delete the
domain even if it still contains repositories. This situation will occur if you delete
the domain's KMS key or revoke the [KMS
grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") that CodeArtifact uses to access the key. In this state, you cannot access the
repositories in the domain or the packages stored in them. Listing and deleting of
repositories is also not possible when CodeArtifact cannot access the domain's KMS key. For
this reason, domain deletion doesn't check whether the domain contains repositories when
the domain's KMS key is inaccessible.

###### Note

When a domain that still contains repositories is deleted, CodeArtifact will
asynchronously delete the repositories within 15 minutes. After the domain is
deleted, the repositories will still be visible in the CodeArtifact console and in the
output of the `list-repositories` command until the automatic repository
cleanup occurs.

## Delete a domain (console)

1. Open the AWS CodeArtifact console at [https://console.aws.amazon.com/codesuite/codeartifact/home](https://console.aws.amazon.com/codesuite/codeartifact/home "https://console.aws.amazon.com/codesuite/codeartifact/home").
2. In the navigation pane, choose **Domains**, then choose the
   domain that you want to delete.
3. Choose **Delete**.

## Delete a domain (AWS CLI)

Use the **delete-domain** command to delete a domain.

```
aws codeartifact delete-domain --domain `my_domain` --domain-owner `111122223333`
```

JSON-formatted data appears in the output with details about the deleted
domain.

```
{
    "domain": {
        "name": "`my_domain`",
        "owner": "`111122223333`",
        "arn": "arn:aws:codeartifact:`us-west-2`:`111122223333`:domain/`my_domain`",
        "status": "Active",
        "encryptionKey": "arn:aws:kms:`us-west-2`:`111122223333`:key/`your-kms-key`",
        "repositoryCount": 0,
        "assetSizeBytes": 0,
        "createdTime": "2020-10-12T16:51:18.039000-04:00"
    }
}
```
