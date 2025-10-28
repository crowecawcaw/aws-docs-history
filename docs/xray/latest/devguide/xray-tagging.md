# Tagging X-Ray sampling rules and groups

Tags are words or phrases that you can use to identify and organize your AWS resources.
You can add multiple tags to each resource. Each tag includes a key and an optional value
that you define. For example, a tag key might be `domain`, and the tag
value might be `example.com`. You can search and filter your resources
based on tags that you add. For more information about ways to use tags, see [Tagging AWS
resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference_.

You can use tags to enforce tag-based permissions on CloudFront distributions. For more information, see [Controlling Access to AWS
Resources Using Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

###### Note

[Tag Editor](../../../ARG/latest/userguide/tag-editor.md "../../../ARG/latest/userguide/tag-editor.md") and [AWS Resource Groups](../../../ARG/latest/userguide/welcome.md "../../../ARG/latest/userguide/welcome.md") do not currently
support X-Ray resources. You add and manage tags by using the AWS X-Ray console or
API.

You can apply tags to resources by using the X-Ray console, API, AWS CLI, SDKs, and
AWS Tools for Windows PowerShell. For more information, see the following documentation:

- X-Ray API – See the following operations in the _AWS X-Ray API Reference_:
  - [ListTagsForResource](../api/API_ListTagsForResource.md "../api/API_ListTagsForResource.md")
  - [CreateSamplingRule](../api/API_CreateSamplingRule.md "../api/API_CreateSamplingRule.md")
  - [CreateGroup](../api/API_CreateGroup.md "../api/API_CreateGroup.md")
  - [TagResource](../api/API_TagResource.md "../api/API_TagResource.md")
  - [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md")

- AWS CLI – See [xray](../../../cli/latest/reference/xray/index.md "../../../cli/latest/reference/xray/index.md") in the
  _AWS CLI Command Reference_
- SDKs – See the applicable SDK documentation on the [AWS
  Documentation](../../../index.md "../../../index.md") page

###### Note

If you cannot add or change tags on an X-Ray resource, or you cannot add a resource
that has specific tags, you might not have permissions to perform this operation. To
request access, contact an AWS user in your enterprise who has
**Administrator** permissions in X-Ray.

###### Topics

- [Tag restrictions](#xray-tagging-restrictions "#xray-tagging-restrictions")
- [Managing tags in the console](#xray-tagging-manage "#xray-tagging-manage")
- [Managing tags in the AWS CLI](#xray-tagging-manage-cli "#xray-tagging-manage-cli")
- [Control access to X-Ray resources based on
  tags](#xray-tagging-policy "#xray-tagging-policy")

## Tag restrictions

The following restrictions apply to tags.

- Maximum number of tags per resource – 50
- Maximum key length – 128 Unicode characters
- Maximum value length – 256 Unicode characters
- Valid values for key and value – a-z, A-Z, 0-9, space, and the following characters: \_ . :
  / = + - and @
- Tag keys and values are case sensitive.
- Don't use `aws:` as a prefix for keys; it's reserved for AWS
  use.

###### Note

You cannot edit or delete system tags.

## Managing tags in the console

You can add optional tags as you create an X-Ray group or sampling rule. Tags can
also be changed or deleted in the console later.

The following procedures explain how to add, edit, and delete tags for your groups and
sampling rules in the X-Ray console.

###### Topics

- [Add tags to a new group
  (console)](#xray-tagging-add-group-console "#xray-tagging-add-group-console")
- [Add tags to a new sampling rule
  (console)](#xray-tagging-add-rule-console "#xray-tagging-add-rule-console")
- [Edit or delete tags for a group
  (console)](#xray-tagging-change-group-console "#xray-tagging-change-group-console")
- [Edit or delete tags for a
  sampling rule (console)](#xray-tagging-change-rule-console "#xray-tagging-change-rule-console")

### Add tags to a new group

(console)

As you create a new X-Ray group, you can add optional tags on the
**Create group** page.

1. Sign in to the AWS Management Console and open the X-Ray console at
   [https://console.aws.amazon.com/xray/home](https://console.aws.amazon.com/xray/home "https://console.aws.amazon.com/xray/home").
2. In the navigation pane, expand **Configuration**, and
   choose **Groups**.
3. Choose **Create group**.
4. On the **Create group** page, specify a name and filter
   expression for the group. For more information about these properties, see
   [Configuring groups](xray-console-groups.md "xray-console-groups.md").
5. In **Tags**, enter a tag key, and optionally, a tag
   value. For example, you can enter a tag key of `Stage`,
   and a tag value of `Production`, to indicate that this
   group is for production use. As you add a tag, a new line appears for you to
   add another tag, if needed. See [Tag restrictions](#xray-tagging-restrictions "#xray-tagging-restrictions") in this topic for
   limitations on tags.
6. When you are finished adding tags, choose **Create
   group**.

### Add tags to a new sampling rule

(console)

As you create a new X-Ray sampling rule, you can add tags on the **Create
sampling rule** page.

1. Sign in to the AWS Management Console and open the X-Ray console at
   [https://console.aws.amazon.com/xray/home](https://console.aws.amazon.com/xray/home "https://console.aws.amazon.com/xray/home").
2. In the navigation pane, expand **Configuration**, and
   choose **Sampling**.
3. Choose **Create sampling rule**.
4. On the **Create sampling rule** page, specify a name,
   priority, limits, matching criteria, and matching attributes. For more
   information about these properties, see [Configuring sampling rules](xray-console-sampling.md "xray-console-sampling.md").
5. In **Tags**, enter a tag key, and optionally, a tag
   value. For example, you can enter a tag key of `Stage`,
   and a tag value of `Production`, to indicate that this
   sampling rule is for production use. As you add a tag, a new line appears
   for you to add another tag, if needed. See [Tag restrictions](#xray-tagging-restrictions "#xray-tagging-restrictions") in this topic for
   limitations on tags.
6. When you are finished adding tags, choose **Create sampling
   rule**.

### Edit or delete tags for a group

(console)

You can change or delete tags on an X-Ray group on the **Edit
group** page.

1. Sign in to the AWS Management Console and open the X-Ray console at
   [https://console.aws.amazon.com/xray/home](https://console.aws.amazon.com/xray/home "https://console.aws.amazon.com/xray/home").
2. In the navigation pane, expand **Configuration**, and
   choose **Groups**.
3. In the **Groups** table, choose the name of a
   group.
4. On the **Edit group** page, in **Tags**,
   edit tag keys and values. You cannot have duplicate tag keys. Tag values are
   optional; you can delete values if desired. For more information about other
   properties on the **Edit group** page, see [Configuring groups](xray-console-groups.md "xray-console-groups.md"). See
   [Tag restrictions](#xray-tagging-restrictions "#xray-tagging-restrictions") in this topic for
   limitations on tags.
5. To delete a tag, choose **X** at the right of the
   tag.
6. When you are finished editing or deleting tags, choose **Update
   group**.

### Edit or delete tags for a

sampling rule (console)

You can change or delete tags on an X-Ray sampling rule on the **Edit
sampling rule** page.

1. Sign in to the AWS Management Console and open the X-Ray console at
   [https://console.aws.amazon.com/xray/home](https://console.aws.amazon.com/xray/home "https://console.aws.amazon.com/xray/home").
2. In the navigation pane, expand **Configuration**, and
   choose **Sampling**.
3. In the **Sampling rules** table, choose the name of a
   sampling rule.
4. In **Tags**, edit tag keys and values. You cannot have
   duplicate tag keys. Tag values are optional; you can delete values if
   desired. For more information about other properties on the **Edit
   sampling rule** page, see [Configuring sampling rules](xray-console-sampling.md "xray-console-sampling.md"). See [Tag restrictions](#xray-tagging-restrictions "#xray-tagging-restrictions") in this topic for
   limitations on tags.
5. To delete a tag, choose **X** at the right of the
   tag.
6. When you are finished editing or deleting tags, choose **Update
   sampling rule**.

## Managing tags in the AWS CLI

You can add tags when you create an X-Ray group or sampling rule. You can also use
the AWS CLI to create and manage tags. To update tags on an existing group or sampling
rule, use the AWS X-Ray console, or the [TagResource](../api/API_TagResource.md "../api/API_TagResource.md") or [UntagResource](../api/API_UntagResource.md "../api/API_UntagResource.md") APIs.

###### Topics

- [Add tags to a new X-Ray group or sampling
  rule (CLI)](#xray-tagging-cli-create "#xray-tagging-cli-create")
- [Add tags to an existing resource
  (CLI)](#xray-tagging-cli-add "#xray-tagging-cli-add")
- [List tags on a resource (CLI)](#xray-tagging-cli-list "#xray-tagging-cli-list")
- [Delete tags on a resource (CLI)](#xray-tagging-cli-delete "#xray-tagging-cli-delete")

### Add tags to a new X-Ray group or sampling

rule (CLI)

To add optional tags as you're creating a new X-Ray group or sampling rule, use
one of the following commands.

- To add tags to a new group, run the following command, replacing
  `group_name` with the name of your group,
  `mydomain.com` with the endpoint of your
  service, `key_name` with a tag key, and optionally,
  `value` with a tag value. For more information
  about how to create a group, see [Groups](xray-api-configuration.md#xray-api-configuration-groups "xray-api-configuration.md#xray-api-configuration-groups").

```
aws xray create-group \
   --group-name "`group_name`" \
   --filter-expression "service(\"`mydomain.com`\") {fault OR error}" \
   --tags [{"Key": "`key_name`","Value": "`value`"},{"Key": "`key_name`","Value": "`value`"}]
```

The following is an example.

```
aws xray create-group \
   --group-name "AdminGroup" \
   --filter-expression "service(\"mydomain.com\") {fault OR error}" \
   --tags [{"Key": "Stage","Value": "Prod"},{"Key": "Department","Value": "QA"}]
```

- To add tags to a new sampling rule, run the following command, replacing
  `key_name` with a tag key, and optionally,
  `value` with a tag value. This command
  specifies the values in the `--sampling-rule` parameter as a JSON
  file. For more information about how to create a sampling rule, see [Sampling rules](xray-api-configuration.md#xray-api-configuration-sampling "xray-api-configuration.md#xray-api-configuration-sampling").

```
aws xray create-sampling-rule \
   --cli-input-json file://`file_name.json`
```

The following are the contents of the JSON file
`file_name.json` that is specified by the
`--cli-input-json` parameter.

```
{
    "SamplingRule": {
        "RuleName": "`rule_name`",
        "RuleARN": "string",
        "ResourceARN": "string",
        "Priority": integer,
        "FixedRate": double,
        "ReservoirSize": integer,
        "ServiceName": "string",
        "ServiceType": "string",
        "Host": "string",
        "HTTPMethod": "string",
        "URLPath": "string",
        "Version": integer,
        "Attributes": {"`attribute_name`": "`value`","`attribute_name`": "`value`"...}
    }
    "Tags": [
           {
               "Key":"`key_name`",
               "Value":"`value`"
           },
           {
               "Key":"`key_name`",
               "Value":"`value`"
           }
          ]
}
```

The following command is an example.

```
aws xray create-sampling-rule \
   --cli-input-json file://9000-base-scorekeep.json
```

The following are the contents of the example
`9000-base-scorekeep.json` file specified by the
`--cli-input-json` parameter.

```
{
    "SamplingRule": {
        "RuleName": "base-scorekeep",
        "ResourceARN": "*",
        "Priority": 9000,
        "FixedRate": 0.1,
        "ReservoirSize": 5,
        "ServiceName": "Scorekeep",
        "ServiceType": "*",
        "Host": "*",
        "HTTPMethod": "*",
        "URLPath": "*",
        "Version": 1
    }
    "Tags": [
           {
               "Key":"Stage",
               "Value":"Prod"
           },
           {
               "Key":"Department",
               "Value":"QA"
           }
          ]
}
```

### Add tags to an existing resource

(CLI)

You can run the `tag-resource` command to add tags to an existing
X-Ray group or sampling rule This method might be simpler than adding tags by
running `update-group` or `update-sampling-rule`.

To add tags to a group or a sampling rule, run the following command, replacing
the ARN with the ARN of the resource, and specifying the keys and optional values of
tags that you want to add.

```
aws xray tag-resource \
   --resource-arn "`ARN`" \
   --tag-keys [{"Key":"`key_name`","Value":"`value`"}, {"Key":"`key_name`","Value":"`value`"}]
```

The following is an example.

```
aws xray tag-resource \
   --resource-arn "arn:aws:xray:us-east-2:01234567890:group/AdminGroup" \
   --tag-keys [{"Key": "Stage","Value": "Prod"},{"Key": "Department","Value": "QA"}]
```

### List tags on a resource (CLI)

You can run the `list-tags-for-resource` command to list tags of an
X-Ray group or sampling rule.

To list the tags that are associated with a group or a sampling rule, run the
following command, replacing the ARN with the ARN of the resource.

```
aws xray list-tags-for-resource \
   --resource-arn "`ARN`"
```

The following is an example.

```
aws xray list-tags-for-resource \
   --resource-arn "arn:aws:xray:us-east-2:01234567890:group/AdminGroup"
```

### Delete tags on a resource (CLI)

You can run the `untag-resource` command to remove tags from an X-Ray
group or sampling rule.

To remove tags from a group or a sampling rule, run the following command,
replacing the ARN with the ARN of the resource, and specifying the keys of tags that
you want to remove.

You can remove only entire tags with the `untag-resource` command. To
remove tag values, use the X-Ray console, or delete tags and add new tags with the
same keys, but different or empty values.

```
aws xray untag-resource \
   --resource-arn "`ARN`" \
   --tag-keys ["`key_name`","`key_name`"]
```

The following is an example.

```
aws xray untag-resource \
   --resource-arn "arn:aws:xray:us-east-2:01234567890:group/`group_name`" \
   --tag-keys ["Stage","Department"]
```

## Control access to X-Ray resources based on

tags

You can attach tags to X-Ray groups or sampling rules, or pass tags in a
request to X-Ray. To control access based on tags, you provide tag
information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`xray:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. To learn more about these condition keys,
see [Controlling access to AWS resources
using resource tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Managing
access to X-Ray groups and sampling rules based on tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-manage-sampling-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-manage-sampling-tags").
