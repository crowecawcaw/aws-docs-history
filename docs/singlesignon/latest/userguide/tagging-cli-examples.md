# AWS CLI examples

The AWS CLI provides commands that you can use to manage the tags that you assign to
 your permission set. 


## Assigning tags


Use the following commands to assign tags to your permission set.


###### Example `tag-resource` Command for a permission set

Assign tags to a permission set by using [`tag-resource`](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/tag-resource.html "https://docs.aws.amazon.com/cli/latest/reference/sso-admin/tag-resource.html")
 within the `sso` set of commands:


```
`$` aws sso-admin tag-resource \
`>` --instance-arn `sso-instance-arn` \
`>` --resource-arn `sso-resource-arn` \
`>` --tags `Stage=Test`
```
This command includes the following parameters:


* `instance-arn` – The Amazon Resource Name (ARN) of
 the IAM Identity Center instance under which the operation will run.
* `resource-arn` – The ARN of the resource with the
 tags to be listed.
* `tags` – The key-value pairs of the tags.
To assign multiple tags at once, specify them in a comma-separated
 list:


```
`$` aws sso-admin tag-resource \
`>` --instance-arn `sso-instance-arn` \
`>` --resource-arn `sso-resource-arn` \
`>` --tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```

## Viewing tags


Use the following commands to view the tags that you have assigned to your
 permission set.


###### Example `list-tags-for-resource` Command for a permission set

View the tags that are assigned to a permission set by using [`list-tags-for-resource`](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/list-tags-for-resource.html "https://docs.aws.amazon.com/cli/latest/reference/sso-admin/list-tags-for-resource.html") within the `sso`
 set of commands:


```
`$` aws sso-admin list-tags-for-resource --resource-arn `sso-resource-arn`
```

## Removing tags


Use the following commands to remove tags from a permission set.


###### Example `untag-resource` Command for a permission set

Remove tags from a permission set by using [`untag-resource`](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/untag-resource.html "https://docs.aws.amazon.com/cli/latest/reference/sso-admin/untag-resource.html") within the `sso` set of
 commands:


```
`$` aws sso-admin untag-resource \
`>` --instance-arn `sso-instance-arn` \
`>` --resource-arn `sso-resource-arn` \
`>` --tag-keys `Stage CostCenter Owner`
```
For the `--tag-keys` parameter, specify one or more tag keys, and
 do not include the tag values.


## Applying tags when you create a
 permission set


Use the following commands to assign tags at the moment you create a permission
 set.


###### Example `create-permission-set` Command with tags

When you create a permission set by using the [`create-permission-set`](https://docs.aws.amazon.com/cli/latest/reference/sso-admin/create-permission-set.html "https://docs.aws.amazon.com/cli/latest/reference/sso-admin/create-permission-set.html") command, you can specify
 tags with the `--tags` parameter:


```
`$` aws sso-admin create-permission-set \
`>` --instance-arn `sso-instance-arn` \
`>` --name `permission=set-name` \
`>` --tags `Stage=Test,CostCenter=80432,Owner=SysEng`
```
