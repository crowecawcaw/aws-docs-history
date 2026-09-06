

# Tag a Recycle Bin retention rule
<a name="recycle-bin-tag-resource"></a>

You can assign custom tags to your retention rules to categorize them in different ways, for example, by purpose, owner, or environment. This helps you to efficiently find a specific retention rule based on the custom tags that you assigned.

You can assign a tag to a retention rule using one of the following methods.

------
#### [ Recycle Bin console ]

**To tag a retention rule**

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/)

1. In the navigation pane, choose **Retention rules**.

1. Select the retention rule to tag, choose the **Tags** tab, and then choose **Manage tags**.

1. Choose **Add tag**. For **Key**, enter the tag key. For **Value**, enter the tag value.

1. Chose **Save**.

------
#### [ AWS CLI ]

**To tag a retention rule**  
Use the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/rbin/tag-resource.html) AWS CLI command. For `--resource-arn`, specify the Amazon Resource Name (ARN) of the retention rule to tag, and for `--tags`, specify the tag key and value pair.

```
aws rbin tag-resource \
--resource-arn {{retention_rule_arn}} \
--tags key={{tag_key}},value={{tag_value}}
```

**Example**  
The following example command tags retention rule `arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3` with tag `purpose=production`.

```
aws rbin tag-resource \
--resource-arn arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3 \
--tags key=purpose,value=production
```

------

## View retention rule tags
<a name="recycle-bin-view-resource-tag"></a>

You can view the tags assigned to a retention rule using one of the following methods.

------
#### [ Recycle Bin console ]

**To view tags for a retention rule**

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/)

1. In the navigation pane, choose **Retention rules**.

1. Select the retention rule for which to view the tags, and choose the **Tags** tab.

------
#### [ AWS CLI ]

**To view the tags assigned to a retention rule**  
Use the [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/rbin/list-tags-for-resource.html) AWS CLI command. For `--resource-arn`, specify the ARN of the retention rule.

```
aws rbin list-tags-for-resource \
--resource-arn {{retention_rule_arn}}
```

**Example**  
The following example command lists the tags for retention rule `arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3`.

```
aws rbin list-tags-for-resource \
--resource-arn arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3
```

------

## Remove tags from retention rules
<a name="recycle-bin-untag-resource"></a>

You can remove tags from a retention rule using one of the following methods.

------
#### [ Recycle Bin console ]

**To remove a tag from a retention rule**

1. Open the Recycle Bin console at [https://console.aws.amazon.com/rbin/home/](https://console.aws.amazon.com/rbin/home/)

1. In the navigation pane, choose **Retention rules**.

1. Select the retention rule from which to remove the tag, choose the **Tags** tab, and then choose **Manage tags**.

1. Choose **Remove** next to the tag to remove.

1. Chose **Save**.

------
#### [ AWS CLI ]

**To remove a tag from a retention rule**  
Use the [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/rbin/untag-resource.html) AWS CLI command. For `--resource-arn`, specify the ARN of the retention rule. For `--tagkeys`, specify the tags keys of the tags to remove.

```
aws rbin untag-resource \
--resource-arn {{retention_rule_arn}} \
--tagkeys {{tag_key}}
```

**Example**  
The following example command removes tags that have a tag key of `purpose` from retention rule `arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3`.

```
aws rbin untag-resource \
--resource-arn arn:aws:rbin:us-east-1:123456789012:rule/nOoSBBtItF3 \
--tagkeys purpose
```

------