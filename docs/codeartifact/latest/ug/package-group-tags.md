# Tag a package group in CodeArtifact

Tags are key-value pairs associated with AWS resources. You can apply tags to your
package groups in CodeArtifact. For information about CodeArtifact resource tagging, use cases, tag key and
value constraints, and supported resource types, see [Tagging resources](tag-resources.md "tag-resources.md").

You can use the CLI to specify tags when you create a package group or add, remove, or update the value of
tags of an existing package group.

## Tag package groups (CLI)

You can use the CLI to manage package group tags.

If you haven't, configure the AWS CLI by following the steps in [Setting up with AWS CodeArtifact](get-set-up-for-codeartifact.md "get-set-up-for-codeartifact.md").

###### Tip

To add tags, you must provide the Amazon Resource Name (ARN) of the package group. To get the ARN of the package group, run
the `describe-package-group` command:

```
aws codeartifact describe-package-group \
   --domain `my_domain` \
   --package-group `/npm/scope/anycompany~` \
   --query packageGroup.arn
```

###### Topics

- [Add tags to a package group (CLI)](#package-group-tags-add-cli "#package-group-tags-add-cli")
- [View tags for a package group (CLI)](#package-group-tags-list-cli "#package-group-tags-list-cli")
- [Edit tags for a package group (CLI)](#package-group-tags-edit-cli "#package-group-tags-edit-cli")
- [Remove tags from a package group (CLI)](#package-group-tags-delete-cli "#package-group-tags-delete-cli")

### Add tags to a package group (CLI)

You can add tags to package groups when they are created, or to an existing package group.
For information about adding tags to a package group when you create it, see [Create a package group](create-package-group.md "create-package-group.md").

To add a tag to an existing package group with the AWS CLI, at the terminal or command line, run the **tag-resource** command,
specifying the Amazon Resource Name (ARN) of the package group where you want to add tags
and the key and value of the tag you want to add. For information about package group ARNs, see
[Package group ARNs](auth-and-access-control-permissions-reference.md#package-group-arns "auth-and-access-control-permissions-reference.md#package-group-arns").

You can add more than one tag to a
package group. For example, to tag a package group, `/npm/scope/anycompany~`
with two tags, a tag key named `key1` with
the tag value of `value1`, and a tag key named
`key2` with the tag value of
`value2`:

```
aws codeartifact tag-resource \
   --resource-arn arn:aws:codeartifact:`us-west-2`:`123456789012`:package-group/`my_domain`/`npm/scope/anycompany~` \
   --tags key=`key1`,value=`value1` key=`key2`,value=`value2`
```

If successful, this command has no output.

### View tags for a package group (CLI)

Follow these steps to use the AWS CLI to view the AWS tags for a package group. If no
tags have been added, the returned list is empty.

At the terminal or command line, run the **list-tags-for-resource**
command with the Amazon Resource Name (ARN) of the package group. For information about package group ARNs, see
[Package group ARNs](auth-and-access-control-permissions-reference.md#package-group-arns "auth-and-access-control-permissions-reference.md#package-group-arns").

For example, to view a list of tag keys and tag values for a package group, `/npm/scope/anycompany~` named with an
ARN value of
`arn:aws:codeartifact:`us-west-2`:`123456789012`:package-group/`my_domain`/`npm/scope/anycompany~``

```
aws codeartifact list-tags-for-resource \
   --resource-arn arn:aws:codeartifact:`us-west-2`:`123456789012`:package-group/`my_domain`/`npm/scope/anycompany~`
```

If successful, this command returns information similar to the following:

```
{
    "tags": {
        "key1": "value1",
        "key2": "value2"
    }
}
```

### Edit tags for a package group (CLI)

Follow these steps to use the AWS CLI to edit a tag for a package group. You can change
the value for an existing key or add another key. You can also remove tags from a
package group, as shown in the next section.

At the terminal or command line, run the **tag-resource** command,
specifying the ARN of the package group where you want to update a tag and specify the
tag key and tag value. For information about package group ARNs, see
[Package group ARNs](auth-and-access-control-permissions-reference.md#package-group-arns "auth-and-access-control-permissions-reference.md#package-group-arns").

```
aws codeartifact tag-resource \
   --resource-arn arn:aws:codeartifact:`us-west-2`:`123456789012`:package-group/`my_domain`/`npm/scope/anycompany~` \
   --tags key=`key1`,value=`newvalue1`
```

If successful, this command has no output.

### Remove tags from a package group (CLI)

Follow these steps to use the AWS CLI to remove a tag from a package group.

###### Note

If you delete a package group, all tag associations are removed from the deleted
package group. You do not have to remove tags before you delete a package group.

At the terminal or command line, run the **untag-resource**
command, specifying the ARN of the package group where you want to remove tags and the
tag key of the tag you want to remove. For information about package group ARNs, see
[Package group ARNs](auth-and-access-control-permissions-reference.md#package-group-arns "auth-and-access-control-permissions-reference.md#package-group-arns").

For example, to remove multiple tags on a
package group, `/npm/scope/anycompany~`, with the tag keys
`key1` and
`key2`:

```
aws codeartifact untag-resource \
   --resource-arn arn:aws:codeartifact:`us-west-2`:`123456789012`:package-group/`my_domain`/`npm/scope/anycompany~` \
   --tag-keys `key1` `key2`
```

If successful, this command has no output. After removing tags, you can
view the remaining tags on the package group using the `list-tags-for-resource` command.
