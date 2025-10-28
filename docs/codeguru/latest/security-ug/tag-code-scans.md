On November 20, 2025, AWS will discontinue support for Amazon CodeGuru Security. After
November 20, 2025, you will no longer be able to access the /codeguru/security console, service
resources, or documentation. For more information, see [End of support for CodeGuru Security](end-of-support.md "end-of-support.md").

# Tag code scans

You can tag code scans when you create them, or tag existing scans. You can use the console,
the AWS CLI, or AWS SDKs to tag scans.

A _tag_ is a custom attribute label that you or AWS assigns to an AWS
resource. Each AWS tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, `Project`, or `Secret`). Tag keys are case
  sensitive.
- An optional field known as a _tag value_. Omitting the tag value is
  the same as using an empty string. Like tag keys, tag values are case sensitive.
  Together these are known as key-value pairs.

Tags help you identify and organize your AWS resources. Many AWS services support tagging,
so you can assign the same tag to resources from different services to indicate that the
resources are related. For example, you can assign the same tag to a scan that you assign to an
AWS CodePipeline pipeline. For more information about using tags, see
[Best Practices for Tagging AWS Resources](../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md "../../../whitepapers/latest/tagging-best-practices/tagging-best-practices.md").

In addition to organizing your resources with tags, you can use tags in IAM policies to
help control who can view and interact with your resources. For information about using
tags to control access to AWS resources, see [Controlling
Access to AWS Resources Using Resource Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User
Guide_.

###### Topics

- [Tag scans in the console](#tag-scans-console "#tag-scans-console")
- [Tag scans with the AWS CLI](#tag-scans-cli "#tag-scans-cli")
- [Tag scans with AWS SDKs](#tag-scans-sdks "#tag-scans-sdks")

## Tag scans in the console

You can only tag scans in the console when you create them.

1. To tag a new scan, open the Scans page in the CodeGuru Security console at
   [https://console.aws.amazon.com/codeguru/security/scans/](https://console.aws.amazon.com/codeguru/security/scans/ "https://console.aws.amazon.com/codeguru/security/scans/").
2. Choose **Create new scan**. On the Create scan page, upload
   your code file and enter a scan name.
3. In the **Tags** panel, choose **Add new
   tag**. Enter a tag key, and optionally a tag value, for your scan.
4. Choose **Create scan** to create the tagged scan.

## Tag scans with the AWS CLI

You can tag new or existing scans with the CLI. To tag a scan when you create it, add the
`--tags` option to the `create-scan` command. Specify a tag
`key` and an optional tag `value`:

```
aws codeguru-security create-scan \
--scan-name `scan-name`
--resource-id '{"codeArtifactId": `codeArtifactId`}'
--tags '`key-1`=`value-1`,`key-2`=`value-2`'

```

For more information on creating scans with the CLI, see
[Create a scan with the AWS CLI](create-scans-cli-sdk.md#create-scan-cli "create-scans-cli-sdk.md#create-scan-cli").

To tag an existing scan, use the `tag-resource` command. For
`resource-arn`, use the `scanNameArn` returned by
`get-scan` or `list-scans`.

```
aws codeguru-security tag-resource \
--resource-arn `scanNameArn`
--tags '`key-1`=`value-1`'

```

For more information about using the AWS CLI with CodeGuru Security, see the
[CodeGuru Security section of the AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-security/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-security/index.html").

## Tag scans with AWS SDKs

You can tag scans when you create them or tag existing scans with the AWS SDKs.

To tag a new scan, use the [`CreateScan`](../security-api/API_CreateScan.md "../security-api/API_CreateScan.md")
operation and specify the tag key and optional tag value for your scan.

To tag an existing scan, use the [`TagResource`](../security-api/API_TagResource.md "../security-api/API_TagResource.md") operation with the resource ARN, tag key, and optional tag
value. For the resource ARN, use the scan name ARN. You can retrieve the
`scanNameArn` by calling `ListScans` or `GetScan`.
