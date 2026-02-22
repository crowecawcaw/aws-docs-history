# Tagging Amazon OpenSearch Ingestion pipelines

Tags let you assign arbitrary information to an Amazon OpenSearch Ingestion pipeline so you can
categorize and filter on that information. A _tag_ is a metadata label
that you assign or that AWS assigns to an AWS resource. Each tag consists of a _key_ and a _value_. For tags
that you assign, you define the key and value. For example, you might define the key as
`stage` and the value for one resource as `test`.

Tags help you do the following:

- Identify and organize your AWS resources. Many AWS services support tagging,
  so you can assign the same tag to resources from different services to indicate that
  the resources are related. For example, you could assign the same tag to an
  OpenSearch Ingestion pipeline that you assign to an Amazon OpenSearch Service domain.
- Track your AWS costs. You activate these tags on the
  AWS Billing and Cost Management dashboard. AWS uses the tags to categorize your costs
  and deliver a monthly cost allocation report to you. For more
  information, see [Use Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the
  [AWS Billing User Guide](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Restrict access to pipelines using attribute based access control. For more
  information, see [Controlling access based on tag keys](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-tag-keys") in the IAM User Guide.
  In OpenSearch Ingestion, the primary resource is a pipeline. You can use the OpenSearch Service console, the
  AWS CLI, OpenSearch Ingestion APIs, or the AWS SDKs to add, manage, and remove tags from a
  pipeline.

###### Topics

- [Permissions required](#pipeline-tag-permissions "#pipeline-tag-permissions")
- [Working with tags (console)](#tag-pipeline-console "#tag-pipeline-console")
- [Working with tags (AWS CLI)](#tag-pipeline-cli "#tag-pipeline-cli")

## Permissions required

OpenSearch Ingestion uses the following AWS Identity and Access Management Access Analyzer (IAM) permissions for tagging
pipelines:

- `osis:TagResource`
- `osis:ListTagsForResource`
- `osis:UntagResource`

For more information about each permission, see [Actions, resources, and condition keys for OpenSearch Ingestion](../../../service-authorization/latest/reference/list_opensearchingestionservice.md "../../../service-authorization/latest/reference/list_opensearchingestionservice.md") in the
_Service Authorization Reference_.

## Working with tags (console)

The console is the simplest way to tag a pipeline.

###### **To create a tag**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/osis/home](https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines "https://console.aws.amazon.com/aos/osis/home#osis/ingestion-pipelines"). You'll be on the Pipelines page.
2. Select the pipeline you want to add tags to and go to the
   **Tags** tab.
3. Choose **Manage** and **Add new
   tag**.
4. Enter a tag key and an optional value.
5. Choose **Save**.

To delete a tag, follow the same steps and choose **Remove** on the
**Manage tags** page.

For more information about using the console to work with tags, see [Tag
Editor](../../../awsconsolehelpdocs/latest/gsg/tag-editor.md "../../../awsconsolehelpdocs/latest/gsg/tag-editor.md") in the _AWS Management Console Getting Started
Guide_.

## Working with tags (AWS CLI)

To tag a pipeline using the AWS CLI, send a `TagResource` request:

```
aws osis tag-resource
  --arn arn:aws:osis:`us-east-1`:`123456789012`:pipeline/`my-pipeline`
  --tags Key=`service`,Value=`osis` Key=`source`,Value=`otel`
```

Remove tags from a pipeline using the `UntagResource` command:

```
aws osis untag-resource
  --arn arn:aws:osis:`us-east-1`:`123456789012`:pipeline/`my-pipeline`
  --tag-keys `service`
```

View the existing tags for a pipeline with the `ListTagsForResource` command:

```
aws osis list-tags-for-resource
  --arn arn:aws:osis:`us-east-1`:`123456789012`:pipeline/`my-pipeline`
```
