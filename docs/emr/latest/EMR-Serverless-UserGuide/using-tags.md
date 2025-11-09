# Working with tags using the AWS CLI and the

Amazon EMR Serverless API

Use the following AWS CLI commands or Amazon EMR Serverless API operations to add, update,
list, and delete the tags for your resources.

| CLI commands and API operations for tags | Resource                 | Supports tags         | Supports tag propagation |
| ---------------------------------------- | ------------------------ | --------------------- | ------------------------ |
| Add or overwrite one or more tags        | `tag-resource`           | `TagResource`         |
| List tags for a resource                 | `list-tags-for-resource` | `ListTagsForResource` |
| Delete one or more tags                  | `untag-resource`         | `UntagResource`       |

The following examples demonstrate how to tag or untag resources using the AWS CLI.

**Tag an existing application**

The following command tags an existing application.

```
aws emr-serverless tag-resource --resource-arn resource_ARN --tags team=devs
```

**Untag an existing application**

The following command deletes a tag from an existing application.

```
aws emr-serverless untag-resource --resource-arn resource_ARN --tag-keys tag_key
```

**List tags for a resource**

The following command lists the tags associated with an existing resource.

```
aws emr-serverless list-tags-for-resource --resource-arn resource_ARN
```
