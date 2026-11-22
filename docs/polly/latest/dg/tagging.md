

# Tagging Amazon Polly resources

A *tag* is a custom attribute label that you or AWS assigns to an AWS resource.

Tags help you do the following:
+ Identify and organize your AWS resources. Many AWS services support tagging. You can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to a Amazon Polly lexicon that you assign to the AWS Lambda function that uses it.
+ Control access to your resources. You can use tags in the `Condition` element of an IAM policy to allow or deny access to a lexicon based on its tags. For more information, see [ABAC with Amazon Polly](security_iam_service-with-iam.md#security_iam_service-with-iam-tags).

**Note**  
Amazon Polly charges for speech synthesis by the number of characters synthesized, not per lexicon. If you activate a tag on a lexicon as a cost allocation tag, the charges for synthesis requests that use that lexicon aren't attributed to the tag.

Tags have two parts:
+ A *tag key* (for example, `CostCenter`, `Environment`, or `Project`). Tag keys are case sensitive.
+ An optional field known as a *tag value* (for example, `12345` or `Production`). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

The following sections provide more information about tags for Amazon Polly.

## Supported resources in Amazon Polly
<a name="tagging-supported-resources"></a>

The following resources in Amazon Polly support tagging:
+ Lexicons – You can tag lexicons when you create them by using the [PutLexicon](https://docs.aws.amazon.com/polly/latest/APIReference/API_PutLexicon.html) API, or when you upload them in the Amazon Polly console. You can add tags to existing lexicons by using the [TagResource](https://docs.aws.amazon.com/polly/latest/APIReference/API_TagResource.html) API. You can also view and manage the tags of a lexicon on its details page in the Amazon Polly console.
+ Custom voices – You can tag custom voices when you create them by using the [CreateVoice](https://docs.aws.amazon.com/polly/latest/APIReference/API_CreateVoice.html) API. You can add tags to existing custom voices by using the [TagResource](https://docs.aws.amazon.com/polly/latest/APIReference/API_TagResource.html) API.

Lexicon ARNs have the following format:

```
arn:aws:polly:{{region}}:{{account-id}}:lexicon/{{LexiconName}}
```

Custom voice ARNs have the following format. To get the ARN of a voice, use `GetVoice`.

```
arn:aws:polly:{{region}}:{{account-id}}:voice/{{voice-id}}
```

For information about adding and managing tags, see [Managing tags](#tagging-add-edit-delete).

## Permissions for tagging resources on creation
<a name="tagging-on-create"></a>

When you include tags in a request that creates a resource, Amazon Polly checks that you have permission for both the create action and `polly:TagResource` on the resource. The following table lists the permissions for each operation.


| Operation | Permissions without tags | Permissions with tags | 
| --- | --- | --- | 
| PutLexicon | polly:PutLexicon | polly:PutLexicon and polly:TagResource | 
| CreateVoice | polly:CreateVoice | polly:CreateVoice and polly:TagResource | 

If you don't have permission for `polly:TagResource`, the request fails with an access denied error, and Amazon Polly doesn't create the resource.

The `AmazonPollyFullAccess` managed policy includes all of these permissions. For more information about managed policies, see [AWS managed (predefined) policies for Amazon Polly](security_iam_id-based-policy-examples.md#access-policy-aws-managed-policies).

To add, change, or remove the tags of an existing lexicon or custom voice, use `TagResource` and `UntagResource`.

`PutLexicon` can also overwrite an existing lexicon, so the following rules apply to lexicons only:
+ You can include tags in a `PutLexicon` request only when the request creates a lexicon. If a lexicon with the same name already exists, a request that includes tags fails with a `ValidationException`, and Amazon Polly doesn't change the lexicon or its tags.
+ A `PutLexicon` request without tags that overwrites an existing lexicon replaces the lexicon content and keeps the tags that the lexicon already has.

## Managing tags
<a name="tagging-add-edit-delete"></a>

Tags consist of the `Key` and `Value` properties on a resource. You can use the Amazon Polly console, the AWS CLI, or the Amazon Polly API to add, edit, or delete the values for these properties.

------
#### [ Console ]

You can add tags when you upload a lexicon. You need a PLS lexicon file (.pls or .xml) and permission for `polly:PutLexicon` and `polly:TagResource`.<a name="tagging-console-upload"></a>

**To add tags when you upload a lexicon**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Lexicons** tab, and then choose **Upload lexicon**.

1. Provide a name for the lexicon and choose the lexicon file.

1. Under **Tags**, choose **Add new tag**, and then enter a key and an optional value. Repeat for each tag that you want to add.

1. Choose **Upload lexicon**.

You can view, add, edit, and remove the tags of an existing lexicon on its details page.<a name="tagging-console-manage"></a>

**To view and manage the tags of an existing lexicon**

1. Sign in to the AWS Management Console and open the Amazon Polly console at [https://console.aws.amazon.com/polly/](https://console.aws.amazon.com/polly/).

1. Choose the **Lexicons** tab, and then choose the name of the lexicon.

1. In the **Tags** section, choose **Manage tags**.

1. Add, edit, or remove tags.

1. Choose **Save changes**.

   The updated tags appear in the **Tags** section.

------
#### [ AWS CLI ]

The following AWS CLI command adds tags when you create a lexicon by using the `--tags` option of the `put-lexicon` command:

```bash
aws polly put-lexicon \
--name w3c \
--content file://example.pls \
--tags Project=Alpha,Environment=Production
```

To add or update tags on an existing lexicon, use the `tag-resource` command. If a tag that has the same key already exists, its value is replaced. In the following examples, replace {{111122223333}} with your AWS account ID.

```bash
aws polly tag-resource \
--resource-arn arn:aws:polly:us-east-2:{{111122223333}}:lexicon/w3c \
--tags CostCenter=12345
```

To list the tags of a lexicon, use the `list-tags-for-resource` command.

```bash
aws polly list-tags-for-resource \
--resource-arn arn:aws:polly:us-east-2:{{111122223333}}:lexicon/w3c
```

The command returns the tags as a map of keys to values.

```json
{
    "Tags": {
        "CostCenter": "12345",
        "Environment": "Production",
        "Project": "Alpha"
    }
}
```

To remove tags from a lexicon, use the `untag-resource` command with one or more tag keys to remove.

```bash
aws polly untag-resource \
--resource-arn arn:aws:polly:us-east-2:{{111122223333}}:lexicon/w3c \
--tag-keys CostCenter Environment
```

------

For more information about tagging lexicons, see the following:
+ [TagResource](https://docs.aws.amazon.com/polly/latest/APIReference/API_TagResource.html), [UntagResource](https://docs.aws.amazon.com/polly/latest/APIReference/API_UntagResource.html), and [ListTagsForResource](https://docs.aws.amazon.com/polly/latest/APIReference/API_ListTagsForResource.html) in the *Amazon Polly API Reference*
+ [Working with Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/tag-editor.html) in the *Resource Groups User Guide*. You can use Tag Editor to find Amazon Polly lexicons by tag and to add, change, or remove their tags together with the tags of resources from other services.

## Tag limits and conventions
<a name="tagging-restrictions"></a>

Each Amazon Polly resource can have a maximum of 50 tags. The `aws:` prefix is reserved for AWS use, so you can't use it in tag keys or values that you create. For tag naming limits, character requirements, and recommended naming strategies that apply to all AWS resources, see [Best practices and strategies](https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html) in the *Tagging AWS Resources and Tag Editor User Guide*.

Don't store sensitive information, such as personal or confidential data, in tags. For more information, see [Data Protection in Amazon Polly](data-protection.md).